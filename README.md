# gif-generator


## Overview
This Python script allows users to create GIFs from any YouTube video. It's a simple yet powerful tool that lets you specify the start and end time of a video segment and converts that segment into a GIF. This project is ideal for those looking to quickly generate GIFs from YouTube content, whether for educational, entertainment, or personal use.

## Features
- Download a specific segment of a YouTube video.
- Convert the downloaded video segment into a GIF.
- Simple command-line interface for ease of use.

## Installation
Before running the script, ensure you have Python installed on your system. Then, follow these steps to install the necessary dependencies.

1. Clone the repository:
`git clone https://github.com/your-username/your-repo-name.git`

2. Navigate to the cloned directory:
`cd your-repo-name`

3. Install the required Python packages:
`pip install pytube moviepy`


## Usage
Run the script from the command line:
`python youtube_to_gif.py`

You will be prompted to:
- Enter the YouTube video URL.
- Specify the start and end time for the GIF segment (in seconds).
- Provide a filename for the output GIF.

Example:
`Enter the YouTube video URL: https://www.youtube.com/watch?v=example
Enter the start time of the GIF (in seconds): 10
Enter the end time of the GIF (in seconds): 20
Enter the filename for the GIF (with .gif extension): output.gif`

The script will download the specified video segment, convert it to a GIF, and save it to the specified filename.

## Contributing
Contributions to this project are welcome! Feel free to fork the repository, make changes, and submit pull requests. If you find any issues or have suggestions for improvements, please submit them as issues in the repository.

## License
This project is open source and available under the [MIT License](LICENSE).
