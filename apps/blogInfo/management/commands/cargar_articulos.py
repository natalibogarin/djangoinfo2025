from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
from apps.blogInfo.models import Post, Categoria, Autor


class Command(BaseCommand):
    help = 'Carga 5 artículos de prueba en la base de datos con diferentes categorías'

    def handle(self, *args, **kwargs):
        self.stdout.write('Iniciando carga de artículos...')

        # Crear o obtener un usuario y autor
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@blog.com',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            user.set_password('admin123')
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Usuario "{user.username}" creado'))

        autor, created = Autor.objects.get_or_create(
            user=user,
            defaults={
                'nombre': 'Administrador del Blog',
                'email': 'admin@blog.com',
                'biografia': 'Editor principal del blog de tecnología e innovación'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Autor "{autor.nombre}" creado'))

        # Crear categorías
        categorias_data = [
            'Tecnología',
            'Programación',
            'Inteligencia Artificial',
            'Ciencia',
            'Desarrollo Web'
        ]

        categorias = []
        for cat_nombre in categorias_data:
            cat, created = Categoria.objects.get_or_create(nombre=cat_nombre)
            categorias.append(cat)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Categoría "{cat.nombre}" creada'))

        # Crear 5 artículos
        articulos_data = [
            {
                'titulo': 'El Futuro de la Inteligencia Artificial en 2025',
                'contenido': '''La inteligencia artificial continúa revolucionando el mundo tal como lo conocemos. En 2025, estamos viendo avances sin precedentes en áreas como el procesamiento del lenguaje natural, visión por computadora y aprendizaje automático.

Los modelos de lenguaje como GPT-4 y Claude han transformado la forma en que interactuamos con las computadoras, permitiendo conversaciones más naturales y asistencia en tareas complejas. Las empresas están adoptando IA para automatizar procesos, mejorar la toma de decisiones y crear experiencias personalizadas para los usuarios.

Sin embargo, también enfrentamos desafíos importantes. La ética en IA, la privacidad de datos y el impacto en el mercado laboral son temas que requieren atención urgente. Es fundamental desarrollar marcos regulatorios que permitan la innovación mientras protegen los derechos fundamentales.

El futuro de la IA es prometedor, pero depende de nosotros guiar su desarrollo de manera responsable y beneficiosa para toda la humanidad.''',
                'categorias': [categorias[2], categorias[0]]  # IA, Tecnología
            },
            {
                'titulo': 'Desarrollo Web Moderno: Frameworks y Tendencias 2025',
                'contenido': '''El desarrollo web ha evolucionado dramáticamente en los últimos años. Los frameworks modernos como React, Vue y Angular continúan dominando el panorama del frontend, mientras que en el backend vemos el auge de tecnologías como Node.js, Django y FastAPI.

Una de las tendencias más importantes es el enfoque en la experiencia del usuario (UX) y el rendimiento. Los Progressive Web Apps (PWA) están ganando terreno, ofreciendo experiencias similares a las aplicaciones nativas directamente desde el navegador.

El desarrollo full-stack se ha vuelto más accesible gracias a herramientas como Next.js y Nuxt.js, que permiten a los desarrolladores crear aplicaciones completas con una sola tecnología. La arquitectura de microservicios y las aplicaciones serverless también están redefiniendo cómo construimos y desplegamos aplicaciones web.

La seguridad sigue siendo una prioridad máxima, con énfasis en HTTPS, autenticación robusta y protección contra vulnerabilidades comunes como XSS y SQL injection.''',
                'categorias': [categorias[4], categorias[1]]  # Desarrollo Web, Programación
            },
            {
                'titulo': 'Python: El Lenguaje de Programación Más Versátil',
                'contenido': '''Python se ha consolidado como uno de los lenguajes de programación más populares y versátiles del mundo. Su sintaxis clara y legible lo hace ideal tanto para principiantes como para desarrolladores experimentados.

Las aplicaciones de Python son prácticamente ilimitadas. Desde desarrollo web con Django y Flask, hasta ciencia de datos con pandas y NumPy, pasando por machine learning con TensorFlow y PyTorch. La comunidad de Python es increíblemente activa, con miles de bibliotecas disponibles para casi cualquier tarea imaginable.

En el ámbito académico y científico, Python es el lenguaje preferido para análisis de datos, simulaciones y visualización. Herramientas como Jupyter Notebooks han transformado la forma en que los científicos comparten y reproducen investigaciones.

El ecosistema de Python continúa creciendo, con mejoras constantes en rendimiento y nuevas características que mantienen al lenguaje relevante y competitivo en 2025.''',
                'categorias': [categorias[1], categorias[0]]  # Programación, Tecnología
            },
            {
                'titulo': 'Descubrimientos Científicos que Están Cambiando el Mundo',
                'contenido': '''La ciencia continúa avanzando a un ritmo acelerado, trayendo descubrimientos que transforman nuestra comprensión del universo y mejoran la calidad de vida.

En el campo de la medicina, las terapias génicas y la medicina personalizada están revolucionando el tratamiento de enfermedades que antes eran incurables. CRISPR y otras tecnologías de edición genética prometen soluciones para enfermedades hereditarias.

La física cuántica está saliendo de los laboratorios para aplicaciones prácticas. Las computadoras cuánticas están cada vez más cerca de lograr la supremacía cuántica, lo que podría revolucionar campos como la criptografía, la simulación molecular y la optimización de sistemas complejos.

En astronomía, los nuevos telescopios espaciales están revelando exoplanetas potencialmente habitables y proporcionando datos sin precedentes sobre el origen del universo. La búsqueda de vida extraterrestre nunca ha sido más emocionante.

El cambio climático continúa siendo un desafío crítico, pero la ciencia está desarrollando soluciones innovadoras en energías renovables, captura de carbono y agricultura sostenible.''',
                'categorias': [categorias[3], categorias[0]]  # Ciencia, Tecnología
            },
            {
                'titulo': 'Machine Learning: De la Teoría a la Práctica',
                'contenido': '''El machine learning ha pasado de ser un campo académico especializado a una herramienta esencial en la industria tecnológica moderna. Comprender cómo implementar modelos de ML efectivos es una habilidad cada vez más demandada.

Los fundamentos del machine learning incluyen tres tipos principales de aprendizaje: supervisado, no supervisado y por refuerzo. Cada uno tiene aplicaciones específicas que van desde la clasificación de imágenes hasta sistemas de recomendación y agentes autónomos.

Las bibliotecas modernas como scikit-learn, TensorFlow y PyTorch han democratizado el acceso al ML, permitiendo a desarrolladores de todos los niveles experimentar con modelos sofisticados. Sin embargo, el verdadero desafío no es solo entrenar un modelo, sino hacerlo bien: seleccionar características relevantes, evitar el overfitting y optimizar el rendimiento.

La implementación en producción de modelos de ML requiere consideraciones adicionales como escalabilidad, monitoreo continuo y gestión de versiones. Herramientas como MLflow y Kubeflow están facilitando estos procesos.

El futuro del ML incluye modelos más eficientes, explicables y que requieran menos datos de entrenamiento, haciendo la tecnología más accesible y confiable.''',
                'categorias': [categorias[2], categorias[1], categorias[0]]  # IA, Programación, Tecnología
            }
        ]

        posts_creados = 0
        for articulo in articulos_data:
            # Verificar si el artículo ya existe
            if not Post.objects.filter(titulo=articulo['titulo']).exists():
                post = Post.objects.create(
                    autor_post=autor,
                    titulo=articulo['titulo'],
                    contenido=articulo['contenido'],
                    fecha_creacion=timezone.now(),
                    fecha_publicacion=timezone.now()
                )
                post.categorias.set(articulo['categorias'])
                posts_creados += 1
                self.stdout.write(self.style.SUCCESS(f'Artículo creado: "{post.titulo}"'))
            else:
                self.stdout.write(self.style.WARNING(f'El artículo "{articulo["titulo"]}" ya existe'))

        self.stdout.write(self.style.SUCCESS(f'\n¡Proceso completado! {posts_creados} artículos nuevos creados.'))
        self.stdout.write(self.style.SUCCESS(f'Total de artículos en BD: {Post.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Total de categorías en BD: {Categoria.objects.count()}'))
