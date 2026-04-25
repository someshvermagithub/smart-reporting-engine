from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(kpis, insights, charts):
    doc = SimpleDocTemplate("reports/report.pdf")
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Smart Data Report", styles['Title']))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("Key Metrics", styles['Heading2']))
    for k, v in kpis.items():
        elements.append(Paragraph(f"{k}: Mean={v['mean']} | Sum={v['sum']}", styles['Normal']))

    elements.append(Paragraph("Insights", styles['Heading2']))
    for ins in insights:
        elements.append(Paragraph(ins, styles['Normal']))

    elements.append(Paragraph("Charts", styles['Heading2']))
    for chart in charts:
        elements.append(Image(chart, width=400, height=200))

    doc.build(elements)