import google.generativeai as genai
import os

# Configure the key
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("❌ Error: GEMINI_API_KEY is not set in environment variables.")
else:
    genai.configure(api_key=api_key)
    print(f"🔑 Key found: {api_key[:5]}... (hidden)")
    print("🔍 Checking available models...")

    try:
        found_any = False
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"✅ AVAILABLE: {m.name}")
                found_any = True
        
        if not found_any:
            print("⚠️ No chat models found. Your key might have restricted permissions.")
            
    except Exception as e:
        print(f"❌ Crash: {e}")