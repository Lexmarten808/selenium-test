# Entorno de pruebas Selenium — Demo  (Localizadores y Ciclo de Vida)

## Requisitos
- Python 3.9+
- Google Chrome instalado
- (Selenium 4.6+ ya incluye Selenium Manager: descarga el chromedriver
  automáticamente, no hay que instalarlo a mano)

## Instalación
```bash
python -m venv venv             # en windows: py -m venv venv (en caso de que el anterior no funcione)
source venv/bin/activate        # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Archivos

| Archivo | Qué muestra | 
|---|---|
| `locators_demo.py` | Las 5 estrategias de localizadores (ID, NAME, CLASS_NAME, XPATH, CSS_SELECTOR) con `print()` explicativos | 
| `test_login_flow.py` | Los 4 pasos del ciclo de vida (init → navegar → interactuar → validar/cerrar), con caso positivo y negativo |

## Cómo correrlo

```bash
# Demo de localizadores 
python locators_demo.py

# Suite de pruebas con pytest 
pytest test_login_flow.py -v
```

