"""Generate the public, sanitized CV bundled with the portfolio."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "cv-william-lucumi.pdf"
OUT.parent.mkdir(exist_ok=True)
FONT_DIR = Path("C:/Windows/Fonts")
pdfmetrics.registerFont(TTFont("Arial", str(FONT_DIR / "arial.ttf")))
pdfmetrics.registerFont(TTFont("ArialBold", str(FONT_DIR / "arialbd.ttf")))

navy = colors.HexColor("#14223b")
blue = colors.HexColor("#345fe6")
gray = colors.HexColor("#48566c")
styles = {
    "name": ParagraphStyle("name", fontName="ArialBold", fontSize=20, leading=23, textColor=navy, spaceAfter=5),
    "title": ParagraphStyle("title", fontName="ArialBold", fontSize=10.5, leading=14, textColor=blue, spaceAfter=8),
    "contact": ParagraphStyle("contact", fontName="Arial", fontSize=8.2, leading=12, textColor=gray, spaceAfter=10),
    "section": ParagraphStyle("section", fontName="ArialBold", fontSize=9, leading=12, textColor=blue, spaceBefore=14, spaceAfter=5),
    "body": ParagraphStyle("body", fontName="Arial", fontSize=8.7, leading=13, textColor=navy, spaceAfter=5),
    "bullet": ParagraphStyle("bullet", fontName="Arial", fontSize=8.7, leading=13, leftIndent=10, firstLineIndent=-8, textColor=navy, spaceAfter=4),
}

def para(text, kind="body"):
    return Paragraph(text, styles[kind])

story = []
def section(title, body):
    story.append(para(title, "section"))
    for item in body:
        story.append(para(item, "bullet" if item.startswith("•") else "body"))

story += [para("WILLIAM LUCUMÍ", "name"), para("LÍDER TÉCNICO · DESARROLLADOR FULL STACK", "title"),
          para("Cali, Colombia  |  wilian.andres@hotmail.es  |  github.com/wilianlk<br/>linkedin.com/in/william-andres-lucumi-hurtado-243743248  |  Portafolio: <link href=\"https://wilianlk.github.io\" color=\"#345fe6\">wilianlk.github.io</link>", "contact"),
          HRFlowable(width="100%", color=blue, thickness=1)]
section("PERFIL", ["Más de 9 años de experiencia en desarrollo, arquitectura de soluciones y liderazgo técnico. Conecto necesidades de negocio con productos digitales, ecommerce e integraciones empresariales, desde el alcance y el MVP hasta producción y operación. He llevado a producción 27 soluciones full stack."])
section("CAPACIDADES", ["<b>Desarrollo:</b> C#, .NET, React, TypeScript, JavaScript y APIs REST/SOAP.",
                       "<b>Plataformas:</b> VTEX, Shopify, ecommerce y pasarelas de pago.",
                       "<b>Entrega y operación:</b> arquitectura, CI/CD, diagnóstico, observabilidad y coordinación técnica."])
section("CASOS REPRESENTATIVOS", ["• Integración entre ecommerce y operación logística para intercambio de pedidos, consulta de estados y seguimiento de inconsistencias.",
                                  "• Integración de servicios externos SOAP, con validación de solicitudes y respuestas en pruebas y producción.",
                                  "• Flujos de checkout, pasarelas de pago y retorno conectados con los estados del pedido.",
                                  "• Aplicaciones internas para inventario, requisiciones y seguimiento de procesos operativos."])
section("EXPERIENCIA", ["<b>2024–actualidad · Recamier S.A. · Liderazgo técnico de soluciones.</b> Arquitectura, desarrollo full stack, ecommerce regional, integraciones, proveedores y operación.",
                       "<b>2022–2024 · Studio F · Desarrollo y análisis funcional ecommerce.</b> Soluciones frontend y backend sobre VTEX para operación regional.",
                       "<b>2016–2022 · Moda de Colombia S.A.S. · Desarrollo de sistemas.</b> Ecommerce, inventario, aplicaciones internas, incidentes y capacitación técnica.",
                       "<b>2015–2016 · Análisis de sistemas.</b> Requerimientos, diseños funcionales y formación de usuarios."])
section("FORMACIÓN", ["Ingeniería Informática, en curso · Técnico en Análisis y Desarrollo de Sistemas de Información · Foundational C# with Microsoft (freeCodeCamp)."])

story += [PageBreak(), para("WILLIAM LUCUMÍ", "name"), para("TECHNICAL LEADER · FULL STACK DEVELOPER", "title"),
          para("Cali, Colombia  |  wilian.andres@hotmail.es  |  github.com/wilianlk<br/>linkedin.com/in/william-andres-lucumi-hurtado-243743248  |  Portfolio: <link href=\"https://wilianlk.github.io\" color=\"#345fe6\">wilianlk.github.io</link>", "contact"),
          HRFlowable(width="100%", color=blue, thickness=1)]
section("PROFILE", ["9+ years of experience in development, solution architecture, and technical leadership. I connect business needs with digital products, ecommerce, and enterprise integrations, from scope and MVP to production and operations. I have delivered 27 full stack solutions to production."])
section("CAPABILITIES", ["<b>Development:</b> C#, .NET, React, TypeScript, JavaScript, and REST/SOAP APIs.",
                         "<b>Platforms:</b> VTEX, Shopify, ecommerce, and payment gateways.",
                         "<b>Delivery and operations:</b> architecture, CI/CD, diagnosis, observability, and technical coordination."])
section("SELECTED WORK", ["• Ecommerce and logistics integration for order exchange, status queries, and inconsistency tracking.",
                          "• External SOAP service integration with request and response validation in test and production environments.",
                          "• Checkout, payment gateway, and return flows connected to order states.",
                          "• Internal applications for inventory, requests, and operational process tracking."])
section("EXPERIENCE", ["<b>2024–present · Recamier S.A. · Technical solutions leadership.</b> Architecture, full stack development, regional ecommerce, integrations, vendors, and operations.",
                       "<b>2022–2024 · Studio F · Ecommerce development and functional analysis.</b> Frontend and backend VTEX solutions for regional operations.",
                       "<b>2016–2022 · Moda de Colombia S.A.S. · Systems development.</b> Ecommerce, inventory, internal applications, incidents, and technical training.",
                       "<b>2015–2016 · Systems analysis.</b> Requirements, functional design, and user training."])
section("EDUCATION", ["Computer Engineering, in progress · Information Systems Analysis and Development Technician · Foundational C# with Microsoft (freeCodeCamp)."])

doc = SimpleDocTemplate(str(OUT), pagesize=(595.28, 841.89), leftMargin=48, rightMargin=48, topMargin=42, bottomMargin=42,
                        title="William Lucumí | CV público", author="William Lucumí")
doc.build(story)
print(OUT)
