# colwagen-bigdata-bi
# Proyecto: Arquitectura Big Data, ETL y BI para Colwagen

Este repositorio contiene el diseño de una solución de Big Data y Business Intelligence (BI) orientada a la Gestión del Conocimiento para el área de posventa de la empresa automotriz Colwagen.

## 1. Diseño de la Arquitectura (Integrando BI y ETL)

```text
[FASE 1: EXTRACCIÓN (Extract) - Orígenes de Datos]
   |-- IoT y Escáneres (Telemetría de vehículos)
   |-- ERP/CRM (Historial del cliente y repuestos)
   |-- Notas de voz y texto de Técnicos (Conocimiento tácito)
          |
          v
[FASE 2: TRANSFORMACIÓN (Transform) - Refinamiento de Datos]
   |-- Data Lake en la Nube (Almacenamiento crudo)
   |-- Limpieza de datos (Data Cleansing)
   |-- Procesamiento de Lenguaje Natural (NLP) para estructurar notas técnicas
          |
          v
[FASE 3: CARGA (Load) - Estructuración]
   |-- Data Warehouse (Bodega de datos optimizada para consultas)
   |-- Creación de modelos relacionales de fallas vs. soluciones
          |
          v
[FASE 4: BUSINESS INTELLIGENCE (BI) & GESTIÓN DEL CONOCIMIENTO]
   |-- Dashboards interactivos en Tablets para el taller (Power BI / Tableau)
   |-- Visualización predictiva: Sugerencia de diagnósticos para Técnicos Junior
   |-- Generación de "Lecciones Aprendidas" dinámicas (Ciclo SECI)
