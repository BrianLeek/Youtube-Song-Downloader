import selenium
from selenium import webdriver
import os
from os import path
import sys
import time
import random

print("Enter the songs name followed by the artist name.")
print("Exmaple: Never Gonna Give You Up - Rick Astley")

songname = input("Song: ") # Ask the user for the songs name and save it to use later.
original_stdout = sys.stdout # Save a reference to the original standard output.

# Example: webdriver.Chrome("C:/Users/User123/Downloads/chromedriver_win32/chromedriver.exe")
driverpath = webdriver.Chrome() # The path to Chromedriver, if this isn't set right the script will not work. See https://sites.google.com/a/chromium.org/chromedriver/home. Default = webdriver.Chrome()

# Check and see if the "songs.txt" file is found, if so remove it.
if path.exists("songs.txt"):
    os.remove("songs.txt")
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
		self.driver.get(f'https://www.youtube.com/results?search_query={song}')
		time.sleep(2)
		thumbnail = self.driver.find_element_by_id('thumbnail')
		link = thumbnail.get_attribute('href')
		
		return link

	def downloadproces(self, muzieklink):
		try:
			self.driver.get('https://ytmp3.cc/en13/')
			time.sleep(2)
			inputbox = self.driver.find_element_by_id('input')
			inputbox.send_keys(str(muzieklink))
			button = self.driver.find_element_by_id('submit')
			button.click()
			time.sleep(6)
			dloadbut = self.driver.find_element_by_xpath("//*[contains(text(), 'Download')]")
			dloadbut.click()
		except Exception as e:
			print(e)
			pass

with open('songs.txt', 'r') as reader:
	songslist = reader.readlines()

for choice in songslist:
	app = MainApp()
	link_songs = app.youtube(choice)
	app.downloadproces(link_songs)
	time.sleep(10)
	app.driver.close()

os.remove("songs.txt") # Removes the "songs.txt" file.

print(f"Successfully downloaded '{songname}'! Run the script to download another song.")

sys.exit()
