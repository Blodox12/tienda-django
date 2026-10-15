import datetime
from ..domain.interfaces import ProcesadorPago

ARCHIVO_LOG = "pagos_locales_Johan_Peña.log"


class BancoNacionalProcesador(ProcesadorPago):
    """
    Implementación concreta de la infraestructura.
    Simula un banco local escribiendo en un log.
    """
    def pagar(self, monto: float) -> bool:
        with open(ARCHIVO_LOG, "a") as f:
            f.write(f"[{datetime.datetime.now()}] BANCO NACIONAL - Cobro procesado: ${monto}\n")
        return True