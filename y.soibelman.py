from PIL import Image

try:
    # פתיחת התמונה ישירות מהתיקייה של הקובץ
    img = Image.open("image.png")
    img.show()
    
except FileNotFoundError:
    print("שגיאה: קובץ התמונה 'monkey.jpg' לא נמצא באותה התיקייה של קובץ הפייתון.")
except Exception as e:
    print(f"שגיאה בפתיחת התמונה: {e}")

