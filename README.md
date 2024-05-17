# Attendance Management System Using Facial Recognition

This project is an Attendance Management System that utilizes facial recognition technology to mark attendance. The system is developed using Python and employs the LBPH (Local Binary Patterns Histograms) algorithm for face recognition and the Haar Cascade classifier for face detection. The graphical user interface (GUI) is built with Tkinter.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Face Recognition Technology](#face-recognition-technology)
  - [LBPH (Local Binary Patterns Histograms)](#lbph-local-binary-patterns-histograms)
  - [Haar Cascade Classifier](#haar-cascade-classifier)
- [Contributing](#contributing)
- [License](#license)

## Features
- User-friendly GUI for managing student data, training the recognition model, and performing face recognition.
- Real-time face detection and recognition.
- Automatic attendance marking and logging.
- Image management for storing and accessing photos of students.

## Requirements
- Python 3.x
- Tkinter
- PIL (Pillow)
- OpenCV
- NumPy
- MySQL Connector

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/attendance-management-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd attendance-management-system
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the main application:
   ```bash
   python main.py
   ```
2. Use the GUI to manage student details, train the face recognition model, and recognize faces to mark attendance.

## Project Structure
```
attendance-management-system/
│
├── images/                     # Directory containing images used in the application
├── data/                       # Directory where captured images are stored
├── attendance_register.csv     # File where attendance logs are saved
│
├── student.py                  # Module for managing student details
├── train.py                    # Module for training the face recognition model
├── face_recognition.py         # Module for performing face recognition
├── attendance.py               # Module for handling attendance
│
├── main.py                     # Main application script
├── README.md                   # Project README file
└── requirements.txt            # Required dependencies
```

## Face Recognition Technology
### LBPH (Local Binary Patterns Histograms)
The LBPH algorithm is used for face recognition. It operates by:
1. Dividing the facial image into multiple grids.
2. Calculating Local Binary Patterns (LBP) for each grid.
3. Creating histograms of the LBP for each grid.
4. Concatenating the histograms into a single feature vector.

This method is robust against changes in lighting conditions and can recognize faces with different expressions and from different angles.

### Haar Cascade Classifier
The Haar Cascade classifier is used for face detection. It works by:
1. Using a cascade function that is trained with a lot of positive and negative images.
2. Scanning the input image at different scales and locations to detect faces.
3. Applying the classifier to each region of the image and identifying the areas with a high probability of containing a face.

The classifier is efficient and provides real-time performance, making it suitable for applications requiring quick face detection.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize and extend the functionality as needed for your specific requirements. If you encounter any issues or have suggestions for improvements, please open an issue on GitHub.
