# CRM Lead Extension for Odoo 18

Este módulo extiende la funcionalidad de CRM en Odoo para gestionar información adicional sobre oportunidades de negocio, incluyendo campos de instalación, soporte y aprobación interna.

## 🧩 Características

- Campo de categoría (`Residencial`, `Empresarial`, `Gubernamental`)
- Fecha límite de entrega e instalación
- Indicación de si requiere instalación o soporte
- Referencia de contrato
- Botón de aprobación con autocompletado de usuario y fecha
- Cálculo automático de los días desde la aprobación
- Campos agrupados en una pestaña propia ("Información adicional")

## 🚀 Instalación

1. Asegúrate de que el módulo está dentro del path de Odoo:  
   `custom_addons/crm_lead_extension`

2. Verifica que el volumen esté montado correctamente en `docker-compose.yml`:

   ```yaml
   - ./custom_addons:/mnt/extra-addons


## 🛠️Estructura del módulo

crm_lead_extension/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── crm_lead.py
├── views/
│   └── crm_order_view.xml
└── data/
    └── demo_data.xml
