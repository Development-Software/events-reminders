import datetime
import logging
import os

from .functions.reminders import (
    list_pending_confirm,
    list_pending_food,
    prueba_conexion,
    list_pending_hotel,
    list_reminder_confirm,
)
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    logging.info("--------Comenzando el proceso de recordatorios --------")
    fecha_actual = datetime.datetime.now()
    logging.info(f"--------Fecha actual {fecha_actual} --------")
    hora_actual = fecha_actual.strftime("%H:%M")
    logging.info(f"--------Hora actual {hora_actual} --------")
    # logging.info("--------Recordatorios para confirmación de asistencia --------")
    # logging.info("--------Configuración de recordatorios --------")
    # logging.info("--------29 Días--------")
    # logging.info("--------15 Días--------")
    # logging.info("--------1 Días--------")
    # fecha_confirmacion = datetime.datetime(2023, 10, 14)
    # diferencia = fecha_confirmacion - fecha_actual
    # logging.info(
    #     f"--------Días para llegar a la fecha compromiso {diferencia.days} --------"
    # )
    # if diferencia.days == 29 and hora_actual == os.getenv("HORA"):
    #     logging.info(
    #         f"--------Comenzando el proceso de recordatorios {diferencia.days} días para el evento --------"
    #     )
    #     list_pending_confirm("pocos")
    # elif diferencia.days == 15 and hora_actual == os.getenv("HORA"):
    #     logging.info(
    #         f"--------Comenzando el proceso de recordatorios {diferencia.days} días para el evento --------"
    #     )
    #     list_pending_confirm("15")
    # elif diferencia.days == 1 and hora_actual == os.getenv("HORA"):
    #     logging.info(
    #         f"--------Comenzando el proceso de recordatorios {diferencia.days} día para el evento --------"
    #     )
    #     list_pending_confirm("1")
    #
    # logging.info("--------Recordatorios para pago de comida --------")
    # logging.info("--------Configuración de recordatorios --------")
    # logging.info("--------7 Días--------")
    # logging.info("--------2 Días--------")
    # fecha_food = datetime.datetime(2023, 11, 1)
    # diferencia_food = fecha_food - fecha_actual
    # logging.info(
    #     f"--------Días para llegar a la fecha compromiso del pago de comida {diferencia_food.days} --------"
    # )
    # if hora_actual == os.getenv("HORA") and (diferencia_food.days == 7 or diferencia_food.days == 2):
    #     logging.info(
    #         f"--------Comenzando el proceso de recordatorios {diferencia_food.days} días para el pago de desayuno --------"
    #     )
    #     list_pending_food("01/11/2023")
    # logging.info("--------Recordatorios para pago de hotel --------")
    # logging.info("--------Configuración de recordatorios --------")
    # logging.info("--------25 Días--------")
    # logging.info("--------18 Días--------")
    # logging.info("--------2 Días--------")
    # fecha_hotel = datetime.datetime(2023, 10, 10)
    # diferencia_hotel = fecha_hotel - fecha_actual
    # logging.info(f"--------Días para llegar a la fecha compromiso {diferencia_hotel.days} --------")
    # if hora_actual == os.getenv("HORA") and (
    #         diferencia_hotel.days == 25 or diferencia_hotel.days == 18 or diferencia_hotel.days == -1):
    #     logging.info(
    #         f"--------Comenzando el proceso de recordatorios {diferencia_hotel.days} días para el pago de hotel --------"
    #     )
    #     list_pending_hotel()
    fecha_str = os.getenv("FECHA")
    logging.info(f"fecha str {fecha_str}")
    # fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
    # logging.info(f"fecha {fecha}")
    logging.info(f"fecha actual {fecha_actual}")
    logging.info(f"hora {os.getenv('HORA')}")
    logging.info("--------Recordatorios para observaciones de invitados --------")
    if hora_actual == os.getenv("HORA"):  # and fecha == fecha_actual:
        logging.info(
            "--------Comenzando el proceso de recordatorio observaciones de invitación --------"
        )
        list_reminder_confirm()
