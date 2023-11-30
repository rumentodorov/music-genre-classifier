from __future__ import unicode_literals
import yt_dlp

songs = [
    {
        "name" : "Eminem - Without Me",
        "url" : "https://www.youtube.com/watch?v=YVkUvmDQ3HY",
        "genre" : "Hip-hop"
    },
        {
        "name" : "Busta Rhymes - Break Ya Neck",
        "url" : "https://www.youtube.com/watch?v=W7FfCJb8JZQ",
        "genre" : "Hip-hop"
    },        
    {
        "name" : "Chopin - Nocturne Op. 72 No. 1 in E minor",
        "url" : "https://www.youtube.com/watch?v=i5XgcakgWf4",
        "genre" : "Classical"
    },
    {
        "name" : "Carl Orff - O Fortuna ~ Carmina Burana",
        "url" : "https://www.youtube.com/watch?v=GXFSK0ogeg4",
        "genre" : "Classical"
    },
    {
        "name" : "Josh Turner - Your Man",
        "url" : "https://www.youtube.com/watch?v=nADTbWQof7Y",
        "genre" : "Country"
    },
    {
        "name" : "Just a closer walk with thee - Patsy Cline And Willie Nelson",
        "url" : "https://www.youtube.com/watch?v=OOKaircCiGI",
        "genre" : "Country"
    },
    {
        "name" : "Bob Marley & The Wailers - Buffalo Soldier",
        "url" : "https://www.youtube.com/watch?v=uMUQMSXLlHM",
        "genre" : "Reggae"
    },
    {
        "name" : "Dave Brubeck - Take Five",
        "url" : "https://www.youtube.com/watch?v=PHdU5sHigYQ",
        "genre" : "Jazz"
    },
    {
        "name" : "Dua Lipa - New Rules",
        "url" : "https://www.youtube.com/watch?v=k2qgadSvNyU",
        "genre" : "Pop"
    },
    {
        "name" : "Christina Aguilera - Genie In A Bottle",
        "url" : "https://www.youtube.com/watch?v=kIDWgqDBNXA",
        "genre" : "Pop"
    },
    {
        "name" : "Sandra - Maria Magdalena",
        "url" : "https://www.youtube.com/watch?v=4jjzu1Z2RZc",
        "genre" : "Disco"
    },
    {
        "name" : "Bee Gees - Stayin' Alive",
        "url" : "https://www.youtube.com/watch?v=fNFzfwLM72c",
        "genre" : "Disco"
    },
    {
        "name" : "Still Got The Blues",
        "url" : "https://www.youtube.com/watch?v=0dWDM0k3OE8",
        "genre" : "Blues"
    },
    {
        "name" : "B.B. King - The Thrill Is Gone",
        "url" : "https://www.youtube.com/watch?v=oica5jG7FpU",
        "genre" : "Blues"
    },
    {
        "name" : "Lynyrd Skynyrd - Sweet Home Alabama",
        "url" : "https://www.youtube.com/watch?v=-p8GXZcdrIk",
        "genre" : "Rock"
    },
    {
        "name" : "Bill Haley & His Comets - Rock Around The Clock",
        "url" : "https://www.youtube.com/watch?v=ZgdufzXvjqw",
        "genre" : "Rock"
    },
    {
        "name" : "Metallica - Seek & Destroy",
        "url" : "https://www.youtube.com/watch?v=FLTchCiC0T0",
        "genre" : "Metal"
    },
    {
        "name" : "Iron Maiden - Aces High",
        "url" : "https://www.youtube.com/watch?v=CfPKxm9O04Y",
        "genre" : "Metal"
    },
]


ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "wav",
    },],
    "outtmpl": "../data/youtube/%(title)s.%(ext)s"
}


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    urls = []
    for song in songs:
        urls.append(song["url"])
    
    ydl.download(urls)