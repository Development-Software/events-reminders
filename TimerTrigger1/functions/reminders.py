import logging
import os
import json
import requests
import datetime
from ..functions.config import connect_db


#from config import connect_db


def reminder_last(phone, name):
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
                    "name": "reminder_invite",
                    "language": {"code": "es_MX"},
                    "components": [
                        {
                            "type": "body",
                            "parameters": [
                                {"type": "text", "text": f"{name}"},
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
        return response
    except Exception as ex:
        logging.info("[ERROR] reminder_last")
        logging.info("[ERROR] ", ex)
        return False


def message_itinerario(phone, name, hotel):
    try:
        template = "itinerario"
        link = ""
        if hotel == "Hotel Villa Pralaya":
            link = "466NkfD"
        elif hotel == "Quinta Mina":
            link = "3FKoqaX"

        token = os.environ.get("TOKEN_WA")
        url = f"https://graph.facebook.com/v17.0/{os.getenv('ID_WA')}/messages"
        payload = json.dumps(
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": f"{phone}",
                "type": "template",
                "template": {
                    "name": f"{template}",
                    "language": {"code": "es_MX"},
                    "components": [
                        {
                            "type": "header",
                            "parameters": [
                                {
                                    "type": "text",
                                    "text": f"{hotel}",
                                }
                            ],
                        },
                        {
                            "type": "body",
                            "parameters": [
                                {"type": "text", "text": f"{name}"},
                                {"type": "text", "text": f"{hotel}"},
                            ],
                        },
                        {
                            "type": "button",
                            "sub_type": "url",
                            "index": "0",
                            "parameters": [{"type": "text", "text": f"{link}"}],
                        }
                    ],
                },
            }
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response
    except Exception as ex:
        logging.info("[ERROR] reminder_last")
        logging.info("[ERROR] ", ex)
        return False


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
        if response.status_code == 200:
            video_confirm(phone)
        return response
    except Exception as ex:
        logging.info("[ERROR] alert_admin")
        logging.info("[ERROR] ", ex)
        return False


def video_confirm(phone):
    try:
        token = os.environ.get("TOKEN_WA")
        url = f"https://graph.facebook.com/v17.0/{os.getenv('ID_WA')}/messages"
        payload = json.dumps({
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": f"{phone}",
            "type": "template",
            "template": {
                "name": "video_confirmacion",
                "language": {
                    "code": "es_MX"
                },
                "components": [
                    {
                        "type": "header",
                        "parameters": [
                            {
                                "type": "video",
                                "video": {
                                    "link": "https://xvivonne.com/static/assets/videos/xvivonnevf.mp4"
                                }
                            }
                        ]
                    }
                ]
            }
        })
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response
    except Exception as ex:
        logging.info("[ERROR] alert_admin")
        logging.info("[ERROR] ", ex)
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
        return response
    except Exception as ex:
        logging.info("[ERROR] alert_admin")
        logging.info("[ERROR] ", ex)
        return False


def reminder_pay_hotel(phone, name, hotel, rooms, amount_x_room, amount_total, paid_amount, last_paid, pending_amount):
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
                    "name": "recordatorio_hotel",
                    "language": {"code": "es_MX"},
                    "components": [
                        {
                            "type": "body",
                            "parameters": [
                                {"type": "text", "text": f"{name}"},
                                {"type": "text", "text": f"{rooms}"},
                                {"type": "text", "text": f"{amount_x_room}"},
                                {"type": "text", "text": f"{amount_total}"},
                                {"type": "text", "text": f"{paid_amount}"},
                                {"type": "text", "text": f"{last_paid}"},
                                {"type": "text", "text": f"{pending_amount}"},
                                {"type": "text", "text": f"{hotel}"},
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
        return response

    except Exception as ex:
        logging.info("[ERROR] alert_admin")
        logging.info("[ERROR] ", ex)
        return False


def list_pending_confirm(days):
    try:
        logging.info(
            "--------Obteniendo lista de invitados pendientes de confirmar--------"
        )
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT phone,name,id_guest FROM guests WHERE status in('sent','income')")
        # cursor.execute("SELECT phone,name,id_guest FROM guests WHERE status in('test')")
        result = cursor.fetchall()
        if result is not None:
            for item in result:
                logging.info(f"--------Enviando mensaje a  {item[1]}--------")
                response = reminder_confirm(item[0], item[1], days)
                if response.status_code == 200:
                    logging.info(
                        f"--------Mensaje enviado con exito a {item[1]}--------"
                    )
                    load_records(item[2], item[1], item[0], "confirmacion", "success", "")
                else:
                    logging.info(f"--------Error al enviar mensaje a {item[1]}--------")
                    load_records(item[2], item[1], item[0], "confirmacion", "error", response.text)
            return True
        else:
            return False
    except Exception as ex:
        logging.info("[ERROR] list_pending_confirm")
        logging.info("[ERROR] ", ex)
        logging.info(f"--------{ex}--------")
        return False


def list_pending_food(date):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT phone,name FROM food f INNER JOin guests g ON f.id_guest = g.id_guest WHERE f.status='unpaid' and confirm=1")
        result = cursor.fetchall()
        if result is not None:
            for item in result:
                logging.info(f"--------Enviando mensaje a  {item[1]}--------")
                response = reminder_pay_food(item[0], item[1], date)
                if response.status_code == 200:
                    logging.info(
                        f"--------Mensaje enviado con exito a {item[1]}--------"
                    )
                    load_records(item[2], item[1], item[0], "desayuno", "success", "")
                else:
                    logging.info(f"--------Error al enviar mensaje a {item[1]}--------")
                    load_records(item[2], item[1], item[0], "desayuno", "error", response.text)
            return True
    except Exception as ex:
        logging.info("[ERROR] list_perding_food")
        logging.info("[ERROR] ", ex)
        logging.info(f"--------{ex}--------")
        return False


def list_pending_hotel():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""SELECT g.id_guest,phone,name,hotel,number_room,amount_x_room,amount_total,paid_amount,CASE WHEN last_paid IS NULL THEN 'Sin pago' ELSE last_paid END last_paid,pending_amount
                                    FROM guests g
                                    INNER JOIN statement s ON g.id_guest = s.id_guest
                                    WHERE s.status = 'unpaid' """)
        result = cursor.fetchall()
        if result is not None:
            for item in result:
                logging.info(f"--------Enviando mensaje a  {item[2]}--------")
                response = reminder_pay_hotel(item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8],
                                              item[9])
                if response.status_code == 200:
                    logging.info(
                        f"--------Mensaje enviado con exito a {item[2]}--------"
                    )
                    load_records(item[0], item[2], item[1], "hotel", "success", "")
                else:
                    logging.info(f"--------Error al enviar mensaje a {item[2]}--------")
                    load_records(item[0], item[2], item[1], "hotel", "error", response.text)
            return True
    except Exception as ex:
        logging.info("[ERROR] list_perding_food")
        logging.info("[ERROR] ", ex)
        logging.info(f"--------{ex}--------")
        return False


def list_reminder_confirm():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT phone,name,id_guest FROM guests WHERE status='confirmed' ")
        result = cursor.fetchall()
        if result is not None:
            for item in result:
                logging.info(f"--------Enviando mensaje a  {item[1]}--------")
                response = reminder_last(item[0], item[1])
                if response.status_code == 200:
                    logging.info(
                        f"--------Mensaje enviado con exito a {item[1]}--------"
                    )
                    load_records(item[2], item[1], item[0], "last_reminder", "success", "")
                else:
                    logging.info(f"--------Error al enviar mensaje a {item[1]}--------")
                    load_records(item[2], item[1], item[0], "last_reminder", "error", response.text)
        else:
            return False
    except Exception as ex:
        logging.info("[ERROR] list_reminder_confirm")
        logging.info("[ERROR] ", ex)
        return False


def program():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT phone,name,hotel FROM guests g INNER JOIN statement S on S.id_guest=g.id_guest ")
        result = cursor.fetchall()
        if result is not None:
            for item in result:
                logging.info(f"--------Enviando mensaje a  {item[1]}--------")
                response = message_itinerario(item[0], item[1], item[2])
                if response.status_code == 200:
                    logging.info(
                        f"--------Mensaje enviado con exito a {item[1]}--------"
                    )
                    load_records(item[2], item[1], item[0], "last_reminder", "success", "")
                else:
                    logging.info(f"--------Error al enviar mensaje a {item[1]}--------")
                    load_records(item[2], item[1], item[0], "last_reminder", "error", response.text)
        else:
            return False
    except Exception as ex:
        logging.info("[ERROR] program")
        logging.info("[ERROR] ", ex)
        return False


def prueba_conexion():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM guests WHERE phone='5555059804'")
        result = cursor.fetchall()
        if result is not None:
            return True
        else:
            return False
    except Exception as ex:
        logging.info("[ERROR] prueba_conexion")
        logging.info("[ERROR] ", ex)
        return False


def load_records(id_guest, name, phone, type, status, error):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO reminders (id_guest, name, phone, type, status, error) VALUES ('{id_guest}','{name}','{phone}','{type}','{status}','{error}')")
        conn.commit()
        return True
    except Exception as ex:
        logging.info("[ERROR] load_records")
        logging.info("[ERROR] ", ex)
        return False


if __name__ == "__main__":
    logging.info("--------Comenzando el proceso de recordatorios --------")
    fecha_actual = datetime.datetime.now()
    logging.info(f"--------Fecha actual {fecha_actual} --------")
    hora_actual = fecha_actual.strftime("%H:%M")
    logging.info(f"--------Hora actual {hora_actual} --------")
    fecha_itinerario = os.getenv("FECHA_ITINERARIO")
    fecha_i = datetime.datetime.strptime(fecha_itinerario, "%d/%m/%Y")
    fecha_param_i = fecha_i.strftime("%d/%m/%Y")
    short_actual_i = fecha_actual.strftime("%d/%m/%Y")
