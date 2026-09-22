from pathlib import Path
import re,html,json
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Preformatted
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
ROOT=Path(__file__).parent
FONT=Path('/usr/share/fonts/truetype/dejavu')
for name,file in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf'),('Mono','DejaVuSansMono.ttf')]:pdfmetrics.registerFont(TTFont(name,str(FONT/file)))
styles={
 'body':ParagraphStyle('body',fontName='Body',fontSize=9.6,leading=13,spaceAfter=7,textColor=HexColor('#243746')),
 'h1':ParagraphStyle('h1',fontName='Bold',fontSize=20,leading=23,spaceAfter=14,textColor=HexColor('#102a3a')),
 'h2':ParagraphStyle('h2',fontName='Bold',fontSize=13,leading=18,spaceAfter=10,textColor=HexColor('#1e5d65')),
 'h3':ParagraphStyle('h3',fontName='Bold',fontSize=10.5,leading=15,spaceBefore=5,spaceAfter=8,textColor=HexColor('#1e5d65')),
 'code':ParagraphStyle('code',fontName='Mono',fontSize=8.3,leading=12,spaceBefore=5,spaceAfter=10,backColor=HexColor('#edf4f5'),borderPadding=8),
 'bullet':ParagraphStyle('bullet',fontName='Body',fontSize=9.6,leading=13,spaceAfter=5,leftIndent=10,firstLineIndent=-8,textColor=HexColor('#243746'))}
def fmt(text):
 text=html.escape(text)
 text=re.sub(r'`([^`]+)`',r'<font name="Mono">\1</font>',text)
 text=re.sub(r'(https://[^\s]+)',lambda m:'<link href="'+m.group(1)+'" color="#1e5d65">'+m.group(1)+'</link>',text)
 return text
story=[]
for n,part in enumerate((ROOT/'Manifold_Descent_Repaired.md').read_text().split('---PAGE---')):
 if n:story.append(PageBreak())
 lines=part.strip().splitlines();buf=[];code=[]
 def flush():
  if buf:story.append(Paragraph(fmt(' '.join(buf)),styles['body']));buf.clear()
 def flushcode():
  if code:story.append(Preformatted('\n'.join(code),styles['code']));code.clear()
 for line in lines:
  if line.startswith('    '):flush();code.append(line[4:]);continue
  flushcode()
  if not line.strip():flush();continue
  if line.startswith('# '):flush();story.append(Paragraph(fmt(line[2:]),styles['h1']))
  elif line.startswith('## '):flush();story.append(Paragraph(fmt(line[3:]),styles['h2']))
  elif line.startswith('### '):flush();story.append(Paragraph(fmt(line[4:]),styles['h3']))
  elif line.startswith('- '):flush();story.append(Paragraph('• '+fmt(line[2:]),styles['bullet']))
  else:buf.append(line)
 flush();flushcode()
def page(c,doc):
 w,h=A4;c.saveState();c.setStrokeColor(HexColor('#60b0a5'));c.line(48,h-37,w-48,h-37);c.setFont('Bold',8);c.setFillColor(HexColor('#24646a'));c.drawString(48,h-27,'SAR / REM WORK');c.setFont('Body',8);c.drawRightString(w-48,h-27,'THE MANIFOLD DESCENT · REPAIR 0.2');c.setStrokeColor(HexColor('#c4d5da'));c.line(48,39,w-48,39);c.setFont('Body',7.5);c.setFillColor(HexColor('#496572'));c.drawString(48,26,'Steve Brown / SAR · Technical repair: OpenAI assistant · 22 September 2026');c.drawRightString(w-48,26,str(doc.page));c.restoreState()
doc=SimpleDocTemplate(str(ROOT/'SAR_REM_Manifold_Descent.pdf'),pagesize=A4,rightMargin=48,leftMargin=48,topMargin=57,bottomMargin=52,title='The Manifold Descent - SAR REM Technical Repair v0.2',author='Steve Brown / SAR; technical repair by OpenAI assistant')
doc.build(story,onFirstPage=page,onLaterPages=page)
print('PDF built')
