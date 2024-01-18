# gif-generator


## Overview
This script allows users to create GIFs from any YouTube video. It's a simple tool that lets you specify the start and end time of a video segment and converts that segment into a GIF. 

## Features
- Download a specific segment of a YouTube video.
- Convert the downloaded video segment into a GIF.
- Simple command-line interface for ease of use.

## Installation
Before running the script, ensure you have Python installed on your system. Then, follow these steps to install the necessary dependencies.

1. Clone the repository:
`git clone https://github.com/prsuyal/gif-generator.git`

2. Navigate to the cloned directory:
`cd gif-generator`

3. Install any required Python packages:   
For example, `pip install pytube moviepy`


## Usage
Run the script from the command line:
`python main.py`

You will be prompted to:
- Enter the YouTube video URL. (ex: https://www.youtube.com/watch?v=example)
- Specify the start time for the GIF segment (in seconds). (ex: 10)
- Specify the end time for the GIF segment (in seconds). (ex: 20)
- Provide a filename for the output GIF. (ex: output.gif)

The script will download the specified video segment, convert it to a GIF, and save it to the specified filename.

## License
This project is open source and available under the [MIT License](LICENSE).
