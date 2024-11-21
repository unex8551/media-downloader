import re
import os
import asyncio
import yt_dlp

def cleanLink(link):
    pattern = re.compile(r"(?:https?:\/\/)?(?:www.)?instagram.com\/?([a-zA-Z0-9\.\_\-]+)?\/([p]+)?([reel]+)?([tv]+)?([stories]+)?\/([a-zA-Z0-9\-\_\.]+)\/?([0-9]+)?")

    match = pattern.match(link)
    if match:
        clean_link = re.sub(r"\?.*$", "", link)
        return clean_link
    else:
        return None

async def downloadInstagram_mp4(link):
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

            if 'entries' in info:
                file_paths = []
                for entry in info['entries']:
                    filename = ydl.prepare_filename(entry)
                    filename_mp4 = filename.rsplit('.', 1)[0] + '.mp4'
                    file_paths.append(filename_mp4)
                return file_paths
            else:
                filename = ydl.prepare_filename(info)
                filename_mp4 = filename.rsplit('.', 1)[0] + '.mp4'
                return [filename_mp4]
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