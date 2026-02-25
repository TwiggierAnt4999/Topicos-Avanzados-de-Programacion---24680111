La versión alternativa del formulario, es una versión en modo oscuro del formulario original, simple y sencillamente para evitar fatiga visual al momento de revisión

REPORTE DE PRÁCTICA Desarrollo de Formulario con Validación en Flet

1.  DATOS GENERALES Nombre de la práctica: Desarrollo de formulario con
    validación de datos Lenguaje: Python Framework: Flet

2.  OBJETIVO Desarrollar una aplicación tipo formulario utilizando el
    framework Flet en Python, implementando validaciones de entrada de
    datos y mostrando mensajes mediante cuadros de diálogo.

3.  DESCRIPCIÓN DE LA PRÁCTICA En esta práctica se desarrolló una
    interfaz gráfica que permite capturar los siguientes datos:

-   Nombre
-   Número de control
-   Email
-   Carrera (mediante un Dropdown)
-   Semestre
-   Género (mediante RadioGroup)

El formulario fue diseñado utilizando componentes visuales como
TextField, Dropdown, RadioGroup, Row, Column y ElevatedButton.

Se implementó validación para asegurar que: - Todos los campos sean
obligatorios. - Número de control y semestre contengan únicamente
valores numéricos. - Se muestre retroalimentación visual marcando en
rojo los campos con error. - Se despliegue un cuadro de diálogo
(AlertDialog) indicando el error o confirmando el registro exitoso.

4.  FUNCIONAMIENTO El botón “Enviar” ejecuta una función de validación
    que:

-   Limpia errores previos.
-   Verifica que los campos no estén vacíos.
-   Valida que los campos numéricos contengan solo dígitos.
-   Muestra mensajes de error en caso de incumplimiento.
-   Si todos los datos son correctos, muestra un resumen con la
    información capturada.

5.  RESULTADOS La aplicación funciona correctamente validando datos en
    tiempo real al presionar el botón. Se logró mantener una estructura
    organizada del código utilizando funciones auxiliares para
    validación, limpieza de errores y manejo de diálogos.

6.  CONCLUSIÓN Se comprendió el uso de componentes gráficos en Flet y la
    implementación de validaciones en formularios interactivos. Esta
    práctica refuerza conceptos de programación estructurada, manejo de
    eventos y diseño de interfaces gráficas en Python.
