import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import glob, shutil, glob
from shutil import copyfile
from os import path
import sys
import time
import random
import config

options = Options()
options.headless = config.Headless

print("Enter the songs name followed by the artist name.")
print("Exmaple: Never Gonna Give You Up - Rick Astley")

songname = input("Song: ") # Ask the user for the songs name and save it to use later.

while songname == "":
    songname = input("Song: ") # Ask the user for the songs name and save it to use later.
else:
    # Tell the user if the script is in headless mode.
    if config.Headless == True:
        print("\nThe script is running in headless mode.\n")

    original_stdout = sys.stdout # Save a reference to the original standard output.
    driverpath = webdriver.Chrome(executable_path=config.DriverPath,chrome_options=options) # Path to the webdriver set in config.py.

    # Check and see if the song file is found, if so remove it.
    if path.exists(config.SongListFileName):
        print(f"Found old {config.SongListFileName} file.")
        print(f"Deleting the old {config.SongListFileName} file.")
        os.remove(config.SongListFileName)
    else:
        pass

    with open('songs.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(f'{songname}') # Add the song name to the file we just created.
        sys.stdout = original_stdout # Reset the standard output to its original value

    class MainApp:
        def __init__(self):
            self.driver = driverpath

        def searcher(self,site):
            self.driver.get(site)

        def youtube(self, song):
            global song_name_yt
            self.driver.get(f'https://www.youtube.com/results?search_query={song}')
            time.sleep(2)
            song_name_yt = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "video-title")))
            print(f"\nGetting info from {song_name_yt.text}...")
            thumbnail = self.driver.find_element_by_id('thumbnail')
            link = thumbnail.get_attribute('href')

            return link

        def downloadproces(self, muzieklink):
            global song_name_ytmp3
            try:
                self.driver.get('https://ytmp3.cc/en13/')
                time.sleep(2)
                inputbox = self.driver.find_element_by_id('input')
                inputbox.send_keys(str(muzieklink))
                button = self.driver.find_element_by_id('submit')
                button.click()
                song_name_ytmp3 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "title")))
                time.sleep(3)
                print(f"Waiting for the download link for {song_name_ytmp3.text}...")
                time.sleep(2)
                print(f"Downloading {song_name_ytmp3.text}...")
                dloadbut = self.driver.find_element_by_xpath("//*[contains(text(), 'Download')]")
                dloadbut.click()
                print(f"Successfully downloaded '{song_name_ytmp3.text}'! Finishing up...")
            except Exception as e:
                print(e)
                pass

    with open(config.SongListFileName, 'r') as reader:
        songslist = reader.readlines()

    for choice in songslist:
        app = MainApp()
        link_songs = app.youtube(choice)
        app.downloadproces(link_songs)
        time.sleep(config.TimeSleepBeforeClose)
        app.driver.close()

    # Move the downloaded songs from the downloads folder to another folder. Set in config.py.
    if config.MoveDownloadedFile == True:
        print(f"Moving files from {config.DownloadFolderPath} to {config.MoveDownloadPath}.")
        for f in glob.glob(f"{config.DownloadFolderPath}*.mp3"):
            shutil.move(f, f"{config.MoveDownloadPath}")
            print(f"Successfully moved all files ending in .mp3 to {config.MoveDownloadPath}.")
    else:
        pass

    print(f"Removing the {config.SongListFileName} file.")
    os.remove(config.SongListFileName) # Remove the songs file.

    print("\nThanks for using my script. Run the script to download another song.")
