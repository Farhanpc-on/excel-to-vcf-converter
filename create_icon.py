import os
from PIL import Image, ImageDraw
import sys

def create_icon_from_jpeg():
    """Convert JPEG to ICO format for Windows application"""
    try:
        # Open the JPEG image
        img = Image.open('logo_excel2vcf.jpeg')
        
        # Convert to RGBA if needed
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Create multiple sizes for ICO (Windows standard)
        sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
        
        # Create ICO with multiple sizes
        ico_images = []
        for size in sizes:
            # Resize image
            resized_img = img.resize(size, Image.Resampling.LANCZOS)
            ico_images.append(resized_img)
        
        # Save as ICO
        ico_images[0].save('logo_excel2vcf.ico', format='ICO', sizes=sizes)
        
        print("✅ Successfully created logo_excel2vcf.ico")
        print("📁 Icon sizes created:", sizes)
        return True
        
    except FileNotFoundError:
        print("❌ Error: logo_excel2vcf.jpeg not found")
        print("📁 Make sure the JPEG file is in the same directory")
        return False
    except Exception as e:
        print(f"❌ Error creating icon: {e}")
        return False

if __name__ == "__main__":
    success = create_icon_from_jpeg()
    if success:
        print("\n🎯 Icon ready for use in build scripts!")
        print("💡 Update build_exe.py to include: '--icon=logo_excel2vcf.ico'")
    else:
        print("\n❌ Icon creation failed. Using build without icon.")
