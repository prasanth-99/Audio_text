import whisper
from datetime import datetime
import os
import csv
import pandas as pd

# Load the whisper model
model = whisper.load_model("base")

# Set the directory path containing audio files
audio_dir = "C:/Users/pathaluri/Documents/data/H01/dyadH01A1w/audio/"

# Read in the existing CSV file or create a new one if it doesn't exist
try:
    df = pd.read_csv("output.csv")
except:
    df = pd.DataFrame(columns=["Date", "Transcription"])

# Iterate through all audio files in the directory
for file_name in os.listdir(audio_dir):
    if file_name.endswith(".m4a"):
        file_path = os.path.join(audio_dir, file_name)
        result = model.transcribe(file_path)
        answer = result['text']

        # Get the file's creation time
        ctime = os.path.getctime(file_path)

        # Convert the timestamp to a datetime object
        recorded_date = datetime.fromtimestamp(ctime)

        # Format the date to your desired format
        formatted_date = recorded_date.strftime('%Y-%m-%d %H:%M:%S')

        # Create a new row with the transcripted data
        new_row = {"Date": formatted_date, "Transcription": answer}

        # Append the new row to the DataFrame
        df = df.append(new_row, ignore_index=True)

# Write the DataFrame out to the CSV file
df.to_csv("output.csv", index=False)
