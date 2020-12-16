Headless = False # If set to True the script will run in the background with no browser window.
# Example: webdriver.Chrome("C:/Users/FakeUser/Downloads/chromedriver_win32/chromedriver.exe"). See https://sites.google.com/a/chromium.org/chromedriver/home.
DriverPath = "C:/Users/FakeUser/Downloads/chromedriver_win32/chromedriver.exe" # If this isn't set right the script will not work.
SongListFileName = "songs.txt"

# Move the downloaded songs from the downloads folder to another folder if enabled. Note: This will move ALL files ending in .mp3 not the one just downloaded to the new folder.
MoveDownloadedFile = False # Set to True to move the songs to another folder after the script runs.
DownloadFolderPath = "" # The path which Chrome downloads file too. Only needs to be set if the above option is set to True and needs to end with a slash. Example: C:/Users/FakeUser/Downloads/
MoveDownloadPath = "" # The path to move the files from the downloads folder. Only needs to be set if the above option is set to True. Doesn't need to end with a slash. Example: C:/Users/FakeUser/Music/FakeUser's Music Download

# Change the default path which Chrome downloads file to. This may not work or will be buggy.
UseCustomDownloadPath = False # Set to True to use a custom download path. In development / will not work.
CustomDownloadPath = "" # Path to the custom downloads folder. In development / will not work.

TimeSleepBeforeClose = 15 # Time in seconds which the script will close after clicking download.
