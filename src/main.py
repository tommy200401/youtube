import pytube


def downloader(url):
    yt = pytube.YouTube(url)
    yt.streams \
        .filter(only_audio=True) \
        .order_by('abr').desc().first().download(output_path="../download/")


if __name__ == "__main__":
    downloader(url="https://www.youtube.com/watch?v=o3nAc--MPo4&t=2500s&ab_channel=OtonashiKurumi2D")
