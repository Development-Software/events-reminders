import datetime
import logging
from .functions.reminders import (
    list_pending_confirm,
    list_pending_food,
    prueba_conexion,
    list_pending_hotel,
)
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    logging.info("--------Comenzando el proceso de recordatorios --------")
    fecha_actual = datetime.datetime.now()
    logging.info(f"--------Fecha actual {fecha_actual} --------")
    hora_actual = fecha_actual.strftime("%H:%M")
    logging.info(f"--------Hora actual {hora_actual} --------")

    logging.info("--------Recordatorios para confirmación de asistencia --------")
    fecha_confirmacion = datetime.datetime(2023, 10, 14)
    diferencia = fecha_confirmacion - fecha_actual
    logging.info(
        f"--------Días para llegar a la fecha compromiso {diferencia.days} --------"
    )
    if diferencia.days == 29 and hora_actual > "16:00":
        logging.info(
            f"--------Comenzando el proceso de recordatorios {diferencia.days} días para el evento --------"
        )
        list_pending_confirm("pocos")
    elif diferencia.days == 15 and hora_actual == "16:00":
        logging.info(
            f"--------Comenzando el proceso de recordatorios {diferencia.days} días para el evento --------"
        )
        list_pending_confirm("15")
    elif diferencia.days == 1 and hora_actual == "16:00":
        logging.info(
            f"--------Comenzando el proceso de recordatorios {diferencia.days} día para el evento --------"
        )
        list_pending_confirm("1")

    logging.info("--------Recordatorios para pago de comida --------")
    fecha_food = datetime.datetime(2023, 11, 1)
    diferencia_food = fecha_food - fecha_actual
    logging.info(
        f"--------Días para llegar a la fecha compromiso del pago de comida {diferencia_food.days} --------"
    )
    if hora_actual == "16:00" and (diferencia_food.days == 7 or diferencia_food.days == 2):
        logging.info(
            f"--------Comenzando el proceso de recordatorios {diferencia_food.days} días para el pago de desayuno --------"
        )
        list_pending_food("01/11/2023")
    logging.info("--------Recordatorios para pago de hotel --------")
    fecha_hotel = datetime.datetime(2023, 10, 10)
    diferencia_hotel = fecha_hotel - fecha_actual
    if hora_actual == "16:00" and (diferencia_hotel.days == 25 or diferencia_hotel.days == 18 or diferencia_hotel.days == 10 or diferencia_hotel.days == 4):
        logging.info(
            f"--------Comenzando el proceso de recordatorios {diferencia_hotel.days} días para el pago de hotel --------"
        )
        list_pending_hotel()
