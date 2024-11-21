import re
import os
import asyncio
import yt_dlp

def cleanLink(link):
    pattern = re.compile(r"^.*https:\/\/(?:m|www|vm)?\.?tiktok\.com\/((?:.*\b(?:(?:usr|v|embed|user|video)\/|\?shareId=|\&item_id=)(\d+))|\w+)")

    match = pattern.match(link)
    if match:
        clean_link = re.sub(r"\?.*$", "", link)
        return clean_link
    else:
        return None

async def downloadTiktok_mp3(link):
    await asyncio.sleep(1)
    
    save_path = 'media'

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    ydl_opts = {
        'format': 'b[url!^="https://www.tiktok.com/"]',
        'outtmpl': os.path.join(save_path, '%(id)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        # 'verbose': True, # Para depurar
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            filename = ydl.prepare_filename(info)
            filename_mp3 = filename.rsplit('.', 1)[0] + '.mp3'
            return filename_mp3
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