import logging
import os
import json
import requests
from ..functions.config import connect_db


def reminder_confirm(phone, name, days):
    try:
        token = os.environ.get("TOKEN_WA")
        url = f"https://graph.facebook.com/v17.0/{os.getenv('ID_WA')}/messages"
        payload = json.dumps(
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": f"{phone}",
                "type": "template",
                "template": {
                    "name": "recordatorio_confirmacion",
                    "language": {"code": "es_MX"},
                    "components": [
                        {
                            "type": "body",
                            "parameters": [
                                {"type": "text", "text": f"{name}"},
                                {"type": "text", "text": f"{days}"},
                            ],
                        },
                    ],
                },
            }
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.status_code
    except Exception as ex:
        print("[ERROR] alert_admin")
        print("[ERROR] ", ex)
        return False


def reminder_pay_food(phone, name, day):
    try:
        token = os.environ.get("TOKEN_WA")
        url = f"https://graph.facebook.com/v17.0/{os.getenv('ID_WA')}/messages"
        payload = json.dumps(
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": f"{phone}",
                "type": "template",
                "template": {
                    "name": "recordatorio_desayuno",
                    "language": {"code": "es_MX"},
                    "components": [
                        {
                            "type": "body",
                            "parameters": [
                                {"type": "text", "text": f"{name}"},
                                {"type": "text", "text": f"{day}"},
                            ],
                        },
                    ],
                },
            }
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.status_code
    except Exception as ex:
        print("[ERROR] alert_admin")
        print("[ERROR] ", ex)
        return False


def list_pending_confirm(days):
    try:
        logging.info(
            "--------Obteniendo lista de invitados pendientes de confirmar--------"
        )
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT phone,name FROM guests WHERE status='sent'")
        result = cursor.fetchall()
        if result is not None:
            for item in result:
                logging.info(f"--------Enviando mensaje a  {item[1]}--------")
                response = reminder_confirm(item[0], item[1], days)
                if response == 200:
                    logging.info(
                        f"--------Mensaje enviado con exito a {item[1]}--------"
                    )
                else:
                    logging.info(f"--------Error al enviar mensaje a {item[1]}--------")
            return True
        else:
            return False
    except Exception as ex:
        print("[ERROR] list_pending_confirm")
        print("[ERROR] ", ex)
        logging.info(f"--------{ex}--------")
        return False

def list_pending_food(date):
    try:
        conn=connect_db()
        cursor=conn.cursor()
        cursor.execute("SELECT phone,name FROM food f INNER JOin guests g ON f.id_guest = g.id_guest WHERE f.status='unpaid' and confirm=1")
        result=cursor.fetchall()
        if result is not None:
            for item in result:
                logging.info(f"--------Enviando mensaje a  {item[1]}--------")
                response = reminder_pay_food(item[0], item[1], date)
                if response == 200:
                    logging.info(
                        f"--------Mensaje enviado con exito a {item[1]}--------"
                    )
                else:
                    logging.info(f"--------Error al enviar mensaje a {item[1]}--------")
            return True
    except Exception as ex:
        print("[ERROR] list_perding_food")
        print("[ERROR] ", ex)
        logging.info(f"--------{ex}--------")
        return False

def prueba_conexion():
    try:
        conn=connect_db()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM guests WHERE phone='5555059804'")
        result=cursor.fetchall()
        if result is not None:
            return True
        else:
            return False
    except Exception as ex:
        print("[ERROR] prueba_conexion")
        print("[ERROR] ", ex)
        return False