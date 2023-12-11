# Taller Sistema Experto

Código realizado por el grupo de **_Britne Vargas y Sergio Quintana_** como taller para la materia Inteligencia Computacional.

## Modo de uso

Para ejecutar el programa se debe tener instalado el lenguaje de programación Python en su versión 3.8 o superior. Como también se debe intslar la librería de **_Experta_** (https://pypi.org/project/experta/).

Se debe ejecutar el archivo **_diagnoses_gui.py_** para iniciar el programa. Ante un posible fallo en la ejecución del programa se debe modificar una linea en una de las librerías de Experta. Esto es debido a que hay problemas en las versiones de las librerías con las versiones de python; la solución se encuentra en el siguiente enlace: https://stackoverflow.com/questions/70749690/attributeerror-module-collections-has-no-attribute-mapping.

Igualmente se mostrará un paso a paso de la solución a continuación.

Si al ejecutar el programa se presenta el siguiente error:

![Error en consola](https://raw.githubusercontent.com/sergio1599/sistema-experto/main/assets/e66b8c4c-b3ed-4f0a-afbf-c833cac65f75.jpg)

Lo que debes hacer es lo siguiente:

Ir a la ruta donde se encuentra el error en este caso es : **File "C:\Users\britn\AppData\Local\Programs\Python\Python311\Lib\site-packages\frozendict\_\_init\_\_.py"**

Ingresando al archivo cambiar la linea 16 y cambiar el **class frozendict(collections.Mapping):**

![Error en consola](https://raw.githubusercontent.com/sergio1599/sistema-experto/main/assets/8807f5fd-72e3-48c4-9426-728a88c9e21d.jpg)

Por **class frozendict(collections.abc.Mapping):** como se muestra en la siguiente imagen:

![Error en consola](https://raw.githubusercontent.com/sergio1599/sistema-experto/main/assets/945658ce-60be-4ee6-aaa7-e33fa45b77db.jpg)

El paso siguiente es guardar y ejecutar el programa nuevamente.
