import pytest
from src.main import obtenerAccion

@pytest.mark.parametrize(
    "esObligatorio_test, esDocente_test, esExterno_test, tipoPersonaDestino_test, estadoRegistro_test, result_test",
    [
        ("si", True, False, "externo", "vigente", "actualizar"),
        ("no", True, False, "docente", "vigente", "matricular"),
        ("si", False, True, "externo", "Por confirmar", "actualizar"),
        ("no", False, True, "externo", "vigente", "registrar"),
        ("si", False, True, "docente", "vigente", "actualizar"),
    ]
)

def test_obtenerAccion(esObligatorio_test, esDocente_test, esExterno_test, tipoPersonaDestino_test, estadoRegistro_test, result_test):
    assert obtenerAccion(esObligatorio_test, esDocente_test, esExterno_test, tipoPersonaDestino_test, estadoRegistro_test) == result_test