# Youtube Song Downloader
Youtube Song Downloader 0.3 by [Palash Sureka](https://github.com/fast-and-curious-1910) and modified by [Brian Leek](https://github.com/BrianLeek).

## About 
This is a song downloader made in Python. Have you ever wanted to download a song for your phone, class, zumba / yoga or anything else? Guess what, this script has you covered!

The modifications I made to this script is making it run with just one file and ask the user for the song name and creates the "songs.txt" file for you and deletes it after the script finishes. All the user needs to do is run the script and enter the song name and the script handles the rest. It's better then editing the songs file and running two different Python files.

## Usage

*Important Note: Chromewebdriver path must be set in config.py where it says "DriverPath".

Run main.py then the script will ask you for the song you would like to download and then the magic will happen. Then a few things will happen:

1. A new tab will open in Chrome.
2. It will go to YouTube.com and copy the link of the first result.
3. Then it will got to YTMP3.cc, paste the link and download the file.

That's it! It isn't the fastest method or the best but it works.

## Options

### Enabling Headless Mode
By enabling headless mode you can run the script in the background well your doing other things with no broswer window in the way. To enable headless mode just open `config.py` and find `Headless = False` and change it to `True`.

### Move Downloaded Files
By setting `MoveDownloadedFile` to `True` in `config.py` allows the script to move all files downloaded to your default downloads folder and move all files that end in .mp3 to another folder that you set. Open `config.py` and make sure you set the path to your default downloads folder in `DownloadFolderPath` and the path where you want to move the files in `MoveDownloadPath`. Thats it! The next time the script runs it should move the files.

## Changelog:
0.3:
 - Code improvements
 - Added a config.py file
 - Option to enable headless mode
 - Option to move downloaded songs
0.2:
 - Code improvements
 - Merge 2 files into 1.
0.1:
 - initial release

## Contributing
If you would like to contribute to this project in any way, feel free too. You will be credited for any work you do. Please make sure to test your code before submitting it. Thanks!


I did not create this script it was created by [Palash Sureka](https://github.com/fast-and-curious-1910) which can be found [here](https://github.com/fast-and-curious-1910/Youtube-Song-Downloader).