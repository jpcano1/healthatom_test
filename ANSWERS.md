## **Answers**
- ¿Qué consideraciones tendrías sobre donde guardar estos datos en el
data warehouse?
  1. **Tabla de Tipo de Cambio**: Se puede crear una tabla específica para almacenar 
    los tipos de cambio. Esta tabla podría tener campos como fecha, moneda 
    original, moneda de conversión, y tasa de cambio.
  2. **Modelo Dimensional**: Considerar si el tipo de cambio debería tratarse 
    como una dimensión o como una tabla de hechos. Esto dependerá de cómo 
    se planea realizar los análisis posteriores.
  3. **Historización**: Se debe considerar si es necesario mantener un historial de 
     cambios en los tipos de cambio a lo largo del tiempo.
- ¿Cómo disponbilizarías estos datos, junto a la información de venta, para el
área comercial?
  1. **Vistas o consultas**: Se pueden crear vistas que combinen información de 
    ventas con tipos de cambio
  2. **Dashboards y reportes**: Se pueden utilizar herramientas de visualización
    como PowerBI o Tableau que muestren la información de las ventas en diferentes monedas
- ¿Sobre qué campos realizarás el cruce con la información de venta? ¿Qué
consideraciones hay que tener sobre estos datos?
  1. **Fecha**: La fecha es necesaria pero hay que asegurarse que las fechas de las tablas
    sean compatibles.
  2. **Moneda**: Para saber qué moneda debemos investigar.
- ¿Cuál sería tu estrategia para actualizar estos datos en el tiempo? Para esta parte hay que tener
en cuenta 4 factores.
  1. Frecuencia de actualización.
  2. Mecanismo de extracción.
  3. Control de cambios.
  4. Registro de errores.

  Con esos 4 factores en mente, es bueno averiguar una herramienta como Apache
Airflow para desplegar pipelines productivos y procesos de ETL.
