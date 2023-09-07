import datetime
import logging
from .functions.reminders import (
    list_pending_confirm,
    list_pending_food,
    prueba_conexion,
)
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    logging.info("--------Comenzando el proceso de recordatorios --------")
    fecha_actual = datetime.datetime.now()
    fecha_confirmacion = datetime.datetime(2023, 10, 14)
    diferencia = fecha_confirmacion - fecha_actual
    logging.info(
        f"--------Días para llegar a la fecha compromiso {diferencia.days} --------"
    )
    if diferencia.days == 29:
        logging.info(
            f"--------Comenzando el proceso de recordatorios 29 días para el evento --------"
        )
        list_pending_confirm("pocos")
    elif diferencia.days == 15:
        logging.info(
            f"--------Comenzando el proceso de recordatorios 15 días para el evento --------"
        )
        list_pending_confirm("15")
    elif diferencia.days == 1:
        logging.info(
            f"--------Comenzando el proceso de recordatorios 1 día para el evento --------"
        )
        list_pending_confirm("1")
    fecha_food = datetime.datetime(2023, 11, 1)
    diferencia_food = fecha_food - fecha_actual
    logging.info(
        f"--------Días para llegar a la fecha compromiso del pago de comida {diferencia_food.days} --------"
    )
    if diferencia_food.days == 40:
        logging.info(
            f"--------Comenzando el proceso de recordatorios 40 días para el pago de desayuno --------"
        )
        list_pending_food("01/11/2023")
    elif diferencia_food.days == 26:
        logging.info(
            f"--------Comenzando el proceso de recordatorios 26 días para el pago de desayuno --------"
        )
        list_pending_food("01/11/2023")
    elif diferencia_food.days == 12:
        logging.info(
            f"--------Comenzando el proceso de recordatorios 12 días para el pago de desayuno --------"
        )
        list_pending_food("01/11/2023")
