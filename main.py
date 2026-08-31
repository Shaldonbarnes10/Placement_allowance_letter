import re

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# =========================
# INPUT
# =========================
# Accepts one or more companies, e.g.:
#   "Datazymes (August 10)"
#   "Datazymes (Aug 13), QuestKart (Aug 18), Unicourt (Aug 24), Incture (Aug 26)"

companies_input = input(
    "Enter company name(s) and date(s), comma-separated "
    "(e.g. Datazymes (Aug 13), QuestKart (Aug 18)): "
)
letter_date = input("Enter letter date (e.g. 27th August 2026): ")

student_name = "Shaldon Barnes"
usn = "NNM23CS172"
year_section = "4th Year, Section C"
teacher_name = "Dr. Minu P. Abraham"
teacher_designation = "Assistant Professor Gd. III"
college_name = "NMAM Institute of Technology, Nitte"

# Parse each "Company (Date)" entry into a (company, date) tuple
placements = []
for entry in companies_input.split(","):
    entry = entry.strip()
    if not entry:
        continue
    match = re.match(r"^(.*?)\s*\((.*?)\)\s*$", entry)
    if match:
        placements.append((match.group(1).strip(), match.group(2).strip()))
    else:
        placements.append((entry, ""))

# Build a filesystem-safe filename from all company names
company_names_for_file = "_".join(p[0].replace(" ", "") for p in placements)
output_file = f"condonation_{company_names_for_file}.pdf"

is_plural = len(placements) > 1


# =========================
# PDF SETUP
# =========================

doc = SimpleDocTemplate(
    output_file,
    pagesize=A4,
    rightMargin=70,
    leftMargin=70,
    topMargin=50,
    bottomMargin=50,
)

styles = getSampleStyleSheet()

body_style = ParagraphStyle(
    "Body",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=11,
    leading=15,
    alignment=TA_LEFT,
    spaceAfter=8,
)


# =========================
# CONTENT
# =========================

story = []

story.append(Paragraph("To", body_style))
story.append(Paragraph(f"{teacher_name}", body_style))
story.append(Paragraph(f"{teacher_designation}", body_style))
story.append(Paragraph(f"{college_name}", body_style))
story.append(Paragraph(f"Date: {letter_date}", body_style))

story.append(Spacer(1, 6))

story.append(Paragraph("<b>Subject: Request for Condonation of Attendance</b>", body_style))

story.append(Spacer(1, 6))

story.append(Paragraph("Respected Madam,", body_style))

activity_word = "placement activities" if is_plural else "a placement activity"
story.append(
    Paragraph(
        f"I am writing to kindly request condonation of attendance for the classes "
        f"I was unable to attend due to my participation in {activity_word}. "
        f"I was required to be present for the placement process{'es' if is_plural else ''}, "
        f"which resulted in my absence from the scheduled classes.",
        body_style,
    )
)

detail_label = "The details of the placement activities are as follows:" if is_plural \
    else "The details of the placement activity are as follows:"
story.append(Paragraph(detail_label, body_style))

if is_plural:
    for company, pdate in placements:
        if pdate:
            story.append(Paragraph(f"Company Name: {company} — Date of Participation: {pdate}", body_style))
        else:
            story.append(Paragraph(f"Company Name: {company}", body_style))
else:
    company, pdate = placements[0]
    story.append(Paragraph(f"Company Name: {company}", body_style))
    if pdate:
        story.append(Paragraph(f"Date of Participation: {pdate}", body_style))

story.append(
    Paragraph(
        f"I kindly request you to consider my participation in the placement "
        f"{'activities' if is_plural else 'activity'} and grant me condonation of "
        f"attendance for the classes missed on the above-mentioned date"
        f"{'s' if is_plural else ''}. I would be grateful for your kind consideration "
        f"and approval of my request.",
        body_style,
    )
)

story.append(Paragraph("Thank you for your consideration.", body_style))

story.append(Spacer(1, 12))

story.append(Paragraph("Yours faithfully,", body_style))
story.append(Paragraph(f"{student_name}", body_style))
story.append(Paragraph(f"USN: {usn}", body_style))
story.append(Paragraph(f"{year_section}", body_style))


# =========================
# CREATE PDF
# =========================

doc.build(story)

print(f"\nPDF created successfully: {output_file}")