# YouTube Manager App

A lightweight command-line application to manage and organize your favorite YouTube videos with persistent storage using SQLite and JSON.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Key Functions](#key-functions)
- [Future Improvements](#future-improvements)
- [Author](#author)

## Overview

YouTube Manager App is a simple yet effective CLI-based tool that allows users to maintain a personal collection of favorite YouTube videos. The application stores video metadata (name and duration) in a JSON file with SQLite database integration, enabling easy management of your video library. This project demonstrates fundamental concepts in file handling, data persistence, and command-line interface design using Python.

## Features

- **List All Videos** – Display all saved videos with their names and durations in a formatted table
- **Add Videos** – Add new favorite videos to your collection with custom names and duration
- **Update Videos** – Modify video details (name and duration) by index number
- **Delete Videos** – Remove videos from your collection
- **Persistent Storage** – Videos are automatically saved to `youtube.text` (JSON format) and database
- **Menu-Driven Interface** – User-friendly command-line menu with numbered options
- **Data Validation** – Input validation for video operations

## Tech Stack

- **Language:** Python 3
- **Data Storage:** JSON file format + SQLite database (`youtube_manager.db`)
- **Data Format:** JSON for serialization
- **No External Dependencies:** Uses only Python standard library

## Project Structure

```
YOUTUBE_MANAGER_APP/
├── youtube_manager.py          # Main application with CLI logic
├── youtube_manager_db.py       # Database management module
├── youtube.text                # JSON file storing video data
├── youtube_manager.db          # SQLite database file
└── README.md                   # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/surag29/YOUTUBE_MANAGER_APP.git
cd YOUTUBE_MANAGER_APP

# No additional dependencies required (uses only Python standard library)
```

### Running the Application

```bash
python youtube_manager.py
```

## Usage

Once you run the application, you'll see an interactive menu:

```
 YOUTUBE MANAGER
 1 . LIST FAV YOUTUBE VIDEOS
 2 . ADD A YOUTUBE VIDEO
 3 . UPDATE THE YOUTUBE VIDEO DETAILS
 4 . DELETE A YOUTUBE VIDEO
 5 . EXIT THE APP
 ENTER YOUR CHOICE:
```

### Example Workflow

1. **Add a video:**
   - Select option `2`
   - Enter video name: `Python Tutorial for Beginners`
   - Enter video duration: `2:30:45`

2. **List all videos:**
   - Select option `1`
   - View all saved videos with their index numbers

3. **Update a video:**
   - Select option `3`
   - Choose video number to update
   - Enter new name and duration

4. **Delete a video:**
   - Select option `4`
   - Choose video number to delete

5. **Exit:**
   - Select option `5` to close the application

## Key Functions

| Function | Purpose |
|----------|----------|
| `load_data()` | Loads video data from `youtube.text` JSON file |
| `save_data_helper(videos)` | Saves video data to `youtube.text` |
| `list_all_videos(videos)` | Displays all videos in formatted table |
| `add_video(videos)` | Adds new video to collection |
| `update_video(videos)` | Updates existing video details |
| `delete_video(videos)` | Removes video from collection |
| `main()` | Main loop handling user menu interaction |

## Future Improvements

- [ ] Implement full SQLite integration for robust data persistence
- [ ] Add search functionality to find videos by name or duration
- [ ] Create REST API using Flask/FastAPI for web access
- [ ] Build web interface with Streamlit for better UX
- [ ] Add video rating and categorization features
- [ ] Implement data export (CSV, Excel formats)
- [ ] Add unit tests for core functionality
- [ ] Support for video thumbnails and YouTube API integration
- [ ] Add sorting and filtering options
- [ ] Deploy as CLI tool to PyPI

## Author

**Surag Devadiga**  
- GitHub: [@surag29](https://github.com/surag29)
- LinkedIn: https://www.linkedin.com/in/surag-devadiga-233477329
- Email: surudev29@gmail.com

---

**Note:** This is a beginner-level project designed for learning Python fundamentals including file I/O, data structures, and user interaction patterns.
