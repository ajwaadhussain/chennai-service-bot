from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def make_pdf(path=None):
    if path is None:
        # Default path relative to the script's location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(script_dir, "../data/chennai_services.pdf")
    c = canvas.Canvas(path, pagesize=letter)
    c = canvas.Canvas(path, pagesize=letter)
    text = c.beginText(40, 750)
    
    lines = [
        "Chennai Local Services Guide 2026",
        "",
        "HOSPITALS & HEALTHCARE",
        "",
        "Q: Which hospital is best for emergencies in T Nagar?",
        "A: Apollo Hospital T Nagar, No.21 Greams Lane, operates 24/7 emergency services.",
        "Phone: 044-2829 3333. Located near Panagal Park Metro Station.",
        "",
        "Q: Where can I find government hospitals in Chennai?",
        "A: Rajiv Gandhi Government General Hospital, Park Town is the largest.",
        "Stanley Medical College Hospital in Old Jail Road also provides free treatment.",
        "",
        "Q: Best hospital for maternity care?",
        "A: Fortis Malar Hospital in Adyar specializes in maternity and pediatrics.",
        "Phone: 044-4289 2222. Near Adyar Signal.",
        "",
        "TRANSPORTATION",
        "",
        "Q: How do I book Chennai Metro?",
        "A: Download CMRL app or buy tokens at stations. Blue Line: Washermenpet to Airport.",
        "Green Line: Wimco Nagar to St Thomas Mount. Operates 6 AM to 10 PM.",
        "",
        "Q: Best way to reach Chennai Airport from city center?",
        "A: Take Metro Blue Line to Airport Metro Station (direct connection).",
        "Or use Airport Taxi prepaid counter. Ola/Uber also available.",
        "",
        "Q: How to get MTC bus timings?",
        "A: Check official MTC Chennai app or visit mtcbus.tn.gov.in website.",
        "Major routes: 27B (Central to Airport), 21G (Koyambedu to Velachery).",
        "",
        "UTILITIES & SERVICES",
        "",
        "Q: How to pay electricity bill in Chennai?",
        "A: TANGEDCO online portal: www.tangedco.gov.in or use Paytm/PhonePe.",
        "Customer care: 94987 94987. Enter your Service Connection Number.",
        "",
        "Q: Water supply complaint number?",
        "A: Chennai Metro Water Board: 044-4567 4567 (24/7 helpline).",
        "Online: www.chennaimetrowater.gov.in",
        "",
        "Q: Gas cylinder booking for Chennai?",
        "A: HP Gas: 1800 2333 555, Indane: 1800 2333 555, Bharat Gas: 1800 2333 555.",
        "Or book via respective mobile apps.",
        "",
        "EDUCATION",
        "",
        "Q: Best coaching centers in Chennai for competitive exams?",
        "A: TIME (T Nagar), Career Launcher (Anna Nagar), IMS (Adyar).",
        "For UPSC: Shankar IAS Academy in West Mambalam.",
        "",
        "EMERGENCY CONTACTS",
        "",
        "Police: 100, Fire: 101, Ambulance: 108, Women Helpline: 181",
        "Disaster Management: 1070, Child Helpline: 1098",
    ]
    
    for line in lines:
        text.textLine(line)
    
    c.drawText(text)
    c.showPage()
    c.save()
    print(f"✅ PDF created successfully at: {path}")

if __name__ == "__main__":
    make_pdf()