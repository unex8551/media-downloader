import re
import os
import asyncio
import yt_dlp

def cleanLink(link):
    patterns = [
        r"^(?:https?:\/\/)?(?:www\.)?facebook\.com\/watch\/?\?(?:\w+=)?v=([\d]+)",
        r"^(?:https?:\/\/)?(?:www\.)?facebook\.com\/share\/(?:v|r)\/([\w-]+)\/?",
        r"^(?:https?:\/\/)?fb\.watch\/([\w-]+)\/?",
        r"^(?:https?:\/\/)?(?:www\.)?facebook\.com\/reel\/(\d+)",
        r"^(?:https?:\/\/)?(?:www\.)?facebook\.com\/(?:\d+|[\w.-]+)\/videos\/(\d+)"
    ]
    
    for pattern in patterns:
        match = re.match(pattern, link)
        if match:
            return match.group(0)
    return None


async def downloadFacebook_mp4(link):
    await asyncio.sleep(1)

    save_path = 'media'

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(save_path, '%(id)s.%(ext)s'),
        # 'verbose': True, # Para depurar
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            filename = ydl.prepare_filename(info)
            filename_mp4 = filename.rsplit('.', 1)[0] + '.mp4'
            return filename_mp4
    except Exception as e:
        print(f"Un error ha ocurrido: {e}")
        return None

async def deleteFile_later(file_path):
    await asyncio.sleep(60)

    try:
        os.remove(file_path)
        print(f"Archivo {file_path} eliminado correctamente")
    except OSError as e:
        print(f"Error al eliminar el archivo: {e}")