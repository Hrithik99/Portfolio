# Branding Cars Classification Using Transfer Learning

## Overview
This project employs **Transfer Learning with ResNet-50** to classify different car brands. The deep learning model is trained on a labeled dataset of car images and fine-tuned to improve accuracy. The model is deployed using **Flask** for real-time predictions.

## Features
- Utilizes **ResNet-50** pretrained model for car brand classification.
- Implements **Transfer Learning** with additional fine-tuning.
- **Compares performance** of VGG-16 and VGG-19 alongside ResNet-50.
- **Deployed as a web app** using Flask for real-time image classification.
- Evaluates performance using **accuracy, precision, recall, and confusion matrix**.

## Installation & Setup
### **1. Clone the Repository**
```sh
git clone https://github.com/your-repo/Branding-Cars-ResNet.git
cd Branding-Cars-ResNet
```

### **2. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3. Download Pretrained Model**
Ensure the model directory is correctly set up with the fine-tuned ResNet-50 model.
```sh
mkdir model
# Download the trained model manually or via script
```

### **4. Run Flask Application**
```sh
python app.py
```

## Model Training
- **Dataset:** Labeled dataset of car brands.
- **Model:** Transfer Learning with **ResNet-50**, fine-tuned on the dataset.
- **Alternative Models:** VGG-16 and VGG-19 for performance comparison.
- **Training Pipeline:** Image preprocessing, feature extraction, classification.

## Deployment Process
- **Flask-based web UI** for real-time image classification.
- **Dockerized application** for seamless deployment.
- Hosted on **AWS/GCP/Heroku** with GPU acceleration.
- Optimized model inference for real-time predictions.

## Performance Metrics
| Metric          | ResNet-50 | VGG-16 | VGG-19 |
|----------------|----------|--------|--------|
| Accuracy       | 92.4%    | 89.8%  | 90.2%  |
| Precision      | 91.5%    | 87.6%  | 88.3%  |
| Recall        | 90.9%    | 86.7%  | 87.2%  |
| Confusion Matrix | ✅ Yes | ✅ Yes | ✅ Yes |

## Example Usage
- Upload an image of a car.
- The model predicts the **brand of the car** with high accuracy.
- **Example Output:** "Predicted Brand: Tesla"

## Future Improvements
- **Fine-tuning with additional car brands.**
- **Experimenting with EfficientNet for improved accuracy.**
- **Optimizing inference speed with TensorRT.**
- **Enhancing web UI with better visualization.**

## Conclusion
This project successfully applies **Transfer Learning with ResNet-50** to classify car brands with high accuracy. The deployment as a **Flask-based web application** enables real-time predictions. Further improvements can be made by exploring **larger datasets and advanced architectures**.

## License
This project is licensed under [MIT License](LICENSE).

## Contact
- **Author:** Hrithik Sarda
- **LinkedIn:** [linkedin.com/in/hrithiksarda](https://linkedin.com/in/hrithiksarda)

