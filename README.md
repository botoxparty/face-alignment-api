# Face Alignment API

The Face Alignment API is a web service that detects and aligns faces in images using dlib's face detection and facial landmark detection models. It can be used to process images from URLs, align detected faces, and return the aligned face as a base64-encoded string.

This tool can be particularly useful for scraping data when creating datasets.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Endpoint](#endpoint)
  - [Request](#request)
  - [Response](#response)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following dependencies installed:

- Python 3.x
- Flask (for the web application)
- dlib (for face detection and facial landmark detection)
- OpenCV (for image processing)
- Requests (for making HTTP requests)

You can install these dependencies using `pip`. For example:

```bash
pip install flask dlib opencv-python-headless requests
```

## Installation

To get started with the Face Alignment API, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/face-alignment-api.git
   ```

2. **Start the application**

    ```bash
    python face-alignment-api/app.py
    ```

The API will be accessible at http://localhost:5000.

## Usage

### Endpoint
The API provides a single endpoint:

`/detect_face (POST)`: Accepts a JSON request with an image URL and returns the aligned face as a base64-encoded string.

### Request
Send a POST request to the `/detect_face` endpoint with the following JSON payload:

    {
      "image_url": "https://example.com/your_image.jpg"
    }

Replace "https://example.com/your_image.jpg" with the URL of the image you want to process.

### Response
The API will respond with a JSON object containing the aligned face as a base64-encoded string:

    {
      "aligned_face_base64": "base64_encoded_string_here"
    }

## License
This project is licensed under the MIT License - see the LICENSE file for details.