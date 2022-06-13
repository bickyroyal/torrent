import pathlib
import shutil

DESTINATION = pathlib.Path("C:\\Users\\Rene\\Desktop\\Films")


def archive(source):
    source = pathlib.Path(source)

    if not source.is_dir():
        return

    videos = []
    videos.extend(source.rglob("*.mp4"))
    videos.extend(source.rglob("*.mkv"))

    if (len(videos) != 1):
        return
    
    video = videos[0]
    shutil.move(video, DESTINATION / video.name)

    subtitles = []
    subtitles.extend(source.rglob("*.srt"))
    subtitles.extend(source.rglob("*.sub"))

    for subtitle in subtitles:
        shutil.move(subtitle, DESTINATION / f"{video.stem}--{subtitle.name}")
    
    shutil.rmtree(source)
    

if __name__ == "__main__":
    import sys
    archive(sys.argv[1])
        
