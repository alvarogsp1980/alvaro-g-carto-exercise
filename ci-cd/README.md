

## Paso 1: Crear un Proyecto en Azure DevOps

Si aún no tienes un proyecto en Azure DevOps, sigue estos pasos para crear uno:

1. Inicia sesión en tu cuenta de Azure DevOps: [https://dev.azure.com/](https://dev.azure.com/)

2. Haz clic en "Nuevo proyecto" para crear un nuevo proyecto. Sigue las instrucciones para completar la configuración básica del proyecto.

### Paso 2: Configurar un Repositorio en GitHub

Si aún no lo has hecho, asegúrate de que tu código fuente esté alojado en un repositorio de GitHub.

### Paso 3: Crear un Pipeline de CI/CD

1. En tu proyecto de Azure DevOps, navega a "Pipelines" en el menú lateral izquierdo.

2. Haz clic en "Nuevo pipeline" para crear un nuevo pipeline.

3. Selecciona el origen del repositorio donde está tu código fuente (GitHub).

4. Configura la conexión a tu cuenta de GitHub y selecciona el repositorio que deseas usar.

5. Selecciona "Node.js" como el tipo de aplicación y elige la plantilla que mejor se adapte a tus necesidades. Puedes empezar con la plantilla más básica y personalizarla según sea necesario.

6. Azure DevOps generará automáticamente un archivo `azure-pipelines.yml` en la raíz de tu repositorio. Este archivo define cómo se construirá y desplegará tu aplicación. Asegúrate de que este archivo se encuentre en tu repositorio de GitHub.

7. Haz clic en "Guardar y ejecutar" para activar el pipeline. Esto ejecutará una construcción de prueba para verificar que todo esté configurado correctamente.

### Paso 4: Personalizar el Archivo de Pipeline

El archivo `azure-pipelines.yml` generado por Azure DevOps se puede personalizar según tus necesidades. Aquí hay algunas configuraciones comunes que puedes ajustar:

- Define los pasos de construcción y prueba específicos para tu aplicación.
- Configura las variables de entorno y secretos necesarios para el proceso de CI/CD.
- Especifica los entornos de despliegue, como desarrollo, prueba y producción, y cómo se deben desplegar.

### Paso 5: Ejecutar el Pipeline de CI/CD

Una vez que hayas personalizado tu archivo de pipeline y guardado los cambios en GitHub, Azure DevOps ejecutará automáticamente el pipeline cada vez que se realicen cambios en el repositorio de GitHub.

### Paso 6: Monitorear y Gestionar el Pipeline

Puedes monitorear el progreso y los resultados de tus pipelines de CI/CD en Azure DevOps. Asegúrate de gestionar las notificaciones y el registro adecuadamente para estar al tanto de los despliegues exitosos o de los problemas que puedan ocurrir.

Con estos pasos, deberías estar en camino de configurar con éxito la parte 2.1 de tu ejercicio, que es la configuración de CI/CD en Azure DevOps. A medida que progreses, no dudes en hacerme preguntas adicionales o pedir ayuda específica.