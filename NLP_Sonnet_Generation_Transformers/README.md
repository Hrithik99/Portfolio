# Shakespearean Sonnet Generation Using GPT-2 and Flask

## Overview
This project leverages **GPT-2/GPT-Neo** to generate **Shakespearean-style sonnets**. The model is fine-tuned on Shakespearean texts and deployed as a **Flask web application** for real-time interaction.

## Features
- Fine-tunes **GPT-2/GPT-Neo** for **poetic text generation**.
- Deployed as a **web-based Flask application**.
- Supports **user-input prompts** for dynamic generation.
- Hosted on **AWS/GCP/Heroku** with **Dockerization**.
- Includes **performance evaluation metrics** such as **perplexity, diversity, and coherence scores**.

## Installation & Setup
### **1. Clone the Repository**
```sh
git clone https://github.com/your-repo/Shakespeare-GPT2.git
cd Shakespeare-GPT2
```

### **2. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3. Download Pretrained Model**
Ensure the model directory is correctly set up with the fine-tuned GPT-2/GPT-Neo model.
```sh
mkdir model
# Download the fine-tuned model manually or via script
```

### **4. Run Flask Application**
```sh
python app.py
```

## Model Training
- **Dataset:** Shakespearean sonnets
- **Model:** Fine-tuned GPT-2/GPT-Neo using **Hugging Face Transformers**
- **Training Pipeline:** Tokenization, fine-tuning, evaluation

## Deployment Process
To make the model accessible, we deployed it as a **Flask-based web application** with the following steps:

1. **Building the Web Interface:**
   - Used **Flask** to create a simple front-end that accepts text input and generates Shakespearean-style poetry.
   - Implemented a **form-based submission system** where users input a seed text and receive generated responses.

2. **Model Serving & API Integration:**
   - Loaded the **fine-tuned GPT-Neo model** into the Flask application.
   - Used **PyTorch** for inference and handled **text generation requests dynamically**.

3. **Hosting & Deployment Options:**
   - **Dockerized the application** for easy deployment.
   - Hosted on **AWS/GCP/Heroku**, making it accessible to users via a web URL.
   - Ensured **scalability and efficient model inference** by using **GPU-backed instances for fast text generation**.

## Performance Metrics
| Metric | Score |
|--------|------|
| Perplexity Score | 17.6 |
| Diversity Score | 0.82 |
| Coherence Score | 0.79 |

## Example Usage
**Input Prompt:** "Shall I compare thee to a summer’s day?"

**Generated Output:**
*Shall I compare thee to a summer’s day?*
*Thy golden hues doth glisten in the light,*
*Though winds may shake the darling buds of May,*
*Thy love shines bright, unwavering in sight.*

## Future Improvements
- **Fine-tuning on larger poetry datasets**
- **Using reinforcement learning** to improve fluency
- **Experimenting with more complex transformer architectures**, such as GPT-3 or fine-tuned T5 models
- **Optimizing inference speed** by leveraging **TensorRT or ONNX for deployment**

## Conclusion
This project demonstrates that GPT-2 and GPT-Neo, when fine-tuned properly, can generate **Shakespearean-style poetry**. The successful deployment as a Flask web application allows users to interact with the model in real time. While results are promising, improvements can be made in terms of **coherence, vocabulary adaptation, and structure**. Future work may explore **larger models and reinforcement learning techniques** to enhance text generation quality.

## License
This project is licensed under [MIT License](LICENSE).

## Contact
- **Author:** Hrithik Sarda
- **LinkedIn:** [linkedin.com/in/hrithiksarda](https://linkedin.com/in/hrithiksarda)


