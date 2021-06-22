from pytube import YouTube

link = input("Digite o link do vídeo: ")

youtube = YouTube(link)
dw = youtube.streams.filter(progressive = True, file_extension = 'mp4')\
.order_by('resolution')\
.desc()\
.first()\
.download()

print("Seu vídeo foi baixado com sucesso!")
