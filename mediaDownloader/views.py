import os
import asyncio
from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings

from .forms import TiktokMP3Form, InstagramMP4Form, FacebookMP4Form
from . import functionalityTiktok_mp3
from . import functionalityInstagram_mp4
from . import functionalityFacebook_mp4

# Create your views here.

# Vista para la página principal
def index(request):
    return render (request, 'index.html')

# Vista para TikTok MP3 Downloader
async def tiktok_mp3(request):
    if request.method == 'GET':
        return render (request, 'tiktok_mp3.html', {
            'form': TiktokMP3Form()
        })
    else:
        raw_link = request.POST['video_url']
        clean_link = functionalityTiktok_mp3.cleanLink(raw_link)

        if clean_link is None:
            return render (request, 'tiktok_mp3.html', {
                'form': TiktokMP3Form(),
                'error': 'Error, ingrese un enlace de un video de TikTok.'
            })
        else:
            file_path = await functionalityTiktok_mp3.downloadTiktok_mp3(clean_link)
            if file_path:
                response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
                
                asyncio.create_task(functionalityTiktok_mp3.deleteFile_later(file_path))

                return response
            else:
                return render (request, 'tiktok_mp3.html', {
                    'form': TiktokMP3Form(),
                    'error': 'Error al descargar el audio, verifique el enlace.'
                })

# Vista para Instagram MP4 Downloader
async def instagram_mp4(request):
    if request.method == 'GET':
        return render (request, 'instagram_mp4.html', {
            'form': InstagramMP4Form()
        })
    else:
        raw_link = request.POST['video_url']
        clean_link = functionalityInstagram_mp4.cleanLink(raw_link)

        if clean_link is None:
            return render (request, 'instagram_mp4.html', {
                'form': InstagramMP4Form(),
                'error': 'Error, ingrese un enlace de un video de Instagram.'
            })

        else:
            file_paths = await functionalityInstagram_mp4.downloadInstagram_mp4(clean_link)
            
            if file_paths and len(file_paths) == 1 and os.path.exists(file_paths[0]):
                file_path = file_paths[0]
                response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
                
                asyncio.create_task(functionalityInstagram_mp4.deleteFile_later(file_path))

                return response

            elif file_paths and len(file_paths) > 1:
                download_links = [{
                    'url': os.path.join(settings.MEDIA_URL, os.path.basename(file_path)),
                }
                for file_path in file_paths]

                for file_path in file_paths:
                    asyncio.create_task(functionalityInstagram_mp4.deleteFile_later(file_path))

                return render (request, 'instagram_mp4.html', {
                    'form': InstagramMP4Form(),
                    'download_links': download_links
                })

            else:
                return render (request, 'instagram_mp4.html', {
                    'form': InstagramMP4Form(),
                    'error': 'Error al descargar el video, verifique el enlace.'
                })

# Vista para Facebook MP4 Downloader
async def facebook_mp4(request):
    if request.method == 'GET':
        return render (request, 'facebook_mp4.html', {
            'form': FacebookMP4Form()
        })
    else:
        raw_link = request.POST['video_url']
        clean_link = functionalityFacebook_mp4.cleanLink(raw_link)

        if clean_link is None:
            return render (request, 'facebook_mp4.html', {
                'form': FacebookMP4Form(),
                'error': 'Error, ingrese un enlace de un video de Facebook.'
            })
        else:
            file_path = await functionalityFacebook_mp4.downloadFacebook_mp4(clean_link)
            
            if file_path:
                response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
                
                asyncio.create_task(functionalityFacebook_mp4.deleteFile_later(file_path))

                return response
            else:
                return render (request, 'facebook_mp4.html', {
                    'form': FacebookMP4Form(),
                    'error': 'Error al descargar el video, verifique el enlace.'
                })