from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

c = canvas.Canvas("original.pdf", pagesize=letter)
c.setFont("Helvetica", 12)
c.drawString(72, 720, "Original PDF for Digital Signature Demo")
c.save()
