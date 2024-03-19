# AudioReplayAttackDetection

Audio Replay Attack Detection is a Python project for detecting replay attacks in audio recordings using a Support Vector Machine (SVM) model. The repository contains tools for dataset management, model training, and prediction.

## Dataset

The `dataset` directory contains audio recordings used for training and testing the SVM model. It includes 100 real and 100 replayed audio samples, each recorded in mono at a sampling rate of 20500 Hz. Additionally, the `raw` subdirectory provides raw real and replayed audio files that can be used to expand the dataset.

## Utilities

The `utilities` directory houses Python scripts for managing and analyzing the audio dataset. These scripts provide functionalities such as checking audio dataset information and extracting audio file details.

## Usage

### Training and Testing

To train and test the SVM model, run `main.py`. This script utilizes the provided dataset to train the model and saves the trained model files in `.pkl` format.

```bash
python main.py
Prediction
For making predictions on new audio recordings, utilize predict.py. This script loads the trained SVM model from the .pkl file and prompts the user to input the path of the audio file to be classified as real or replayed.

bash
Copy code
python predict.py
Contributors
Wali Muhammad Ahmad
License


Feel free to contribute, report issues, or suggest improvements!
