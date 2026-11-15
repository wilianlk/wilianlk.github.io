# Portafolio de William Lucumí

Portafolio bilingüe (español/inglés) desarrollado con Astro, TypeScript y CSS. Es un sitio estático: no usa base de datos, autenticación ni formulario de contacto.

## Requisitos

- Node.js 22 o posterior
- Docker Desktop (solo para ejecutarlo como contenedor)

## Ejecutar en desarrollo

```powershell
npm install
npm run dev
```

Astro indicará una URL local, normalmente `http://localhost:4321`.

## Comprobar compilación de producción

```powershell
npm run build
```

El resultado estático se genera en `dist/`.

## Ejecutar con Docker

Construir y levantar el sitio:

```powershell
docker compose up --build -d
```

Abrir `http://localhost:8088`.

Revisar estado y registros:

```powershell
docker compose ps
docker compose logs -f portfolio
```

Detener el contenedor sin borrar la imagen:

```powershell
docker compose down
```

## Contenido editable

Todo el contenido público vive en `src/content/portfolio.ts`:

- `profile`: correo, LinkedIn, GitHub y CV. Los enlaces vacíos se ocultan automáticamente.
- `experience`: empresas, cargos, períodos y contribuciones. La sección pública muestra un estado pendiente mientras esté vacía.
- `education`: estudios, cursos y certificaciones confirmados.
- `content`: textos en español e inglés, habilidades y casos seleccionados.

Antes de publicar confirma: correo profesional, LinkedIn, GitHub, CV, experiencia laboral, formación y cualquier enlace a demostraciones públicas. No agregues datos internos, credenciales, dominios, endpoints ni capturas confidenciales.

## Variables de entorno

Actualmente no se requiere ninguna variable. `.env.example` existe como referencia y no contiene secretos.

## Publicación

El sitio se publica automáticamente en GitHub Pages cuando se envían cambios a la rama `main`. La URL esperada es `https://wilianlk.github.io`.

El flujo de despliegue está en `.github/workflows/deploy.yml` y usa la acción oficial de Astro. GitHub genera `dist/` durante el despliegue; esa carpeta no se sube al repositorio.
