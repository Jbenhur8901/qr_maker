import qrcode
from PIL import Image

def generate_styled_qr_code(url, logo_path=None, fill_color="black", back_color="white", output_file="styled_qr_code.png"):
    # Créer un objet QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Haut niveau de correction d'erreur
        box_size=10,
        border=4,
    )
    
    # Ajouter l'URL au QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Créer une image du QR code
    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')
    
    # Ajouter un logo au centre du QR code (si un chemin de logo est fourni)
    if logo_path:
        logo = Image.open(logo_path)
        
        # Redimensionner le logo pour qu'il s'adapte au QR code
        logo_size = 100  # Taille du logo
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)  # Utilisation de LANCZOS
        
        # Calculer la position pour centrer le logo
        qr_width, qr_height = qr_img.size
        logo_position = (
            (qr_width - logo_size) // 2,
            (qr_height - logo_size) // 2
        )
        
        # Coller le logo au centre du QR code
        qr_img.paste(logo, logo_position, logo)
    
    # Sauvegarder le QR code stylisé
    qr_img.save(output_file)
    print(f"QR code stylisé sauvegardé sous {output_file}")

# Exemple d'utilisation
url = "https://vitrine-mag.vercel.app/"
generate_styled_qr_code(url, fill_color="black", back_color="white", output_file="vitrine_qr_code.png")