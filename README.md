# Internet Speed Twitter Bot

A Python script using Selenium to automate the process of checking your internet speed and tweeting the results to your Twitter account.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Last Run](#last-run)

## Introduction

This project aims to automate the task of checking your internet speed and posting the results on your Twitter account. It uses the Selenium library to interact with the Speedtest.net website for measuring your internet speed and the Twitter website for tweeting the results.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python: You should have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Installation

To set up the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/internet-speed-twitter-bot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd internet-speed-twitter-bot
   ```

3. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Download the Chrome WebDriver for Selenium and place it in the project directory. You can download it from [chromedriver.chromium.org](https://sites.google.com/chromium.org/driver/).

## Usage

To use the Internet Speed Twitter Bot, follow these steps:

1. Open the `config.py` file and fill in your Twitter account credentials and other configuration options.

2. Run the script:

   ```bash
   python main.py
   ```

3. The bot will open a web browser, measure your internet speed using Speedtest.net, and tweet the results to your Twitter account.

## Configuration

You can configure the bot by editing the `config.py` file. Here are some of the configuration options:

- `UP_SPEED` and `DOWN_SPEED`: Set the minimum speed thresholds for upload and download speeds. If your internet speed is below these thresholds, the bot will tweet about it.

- `EMAIL` and `PASS`: Enter your Twitter login credentials.

- `chrome_driver_path`: Set the path to the Chrome WebDriver executable.

- You can also customize the browser options in `chrome_options` according to your needs.

## Contributing

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork the project.

2. Create your feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m 'Add some feature'
   ```

4. Push to the branch:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Last Run

The last run of this project was on April 1, 2023.
