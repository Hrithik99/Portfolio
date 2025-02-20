# **Compression of Information Using Huffman Coding and LSB Steganography**

## **Overview**

This project explores an advanced method of data compression and steganography by combining **Huffman coding** with **Least Significant Bit (LSB) embedding**. The goal is to enhance data concealment efficiency while preserving image quality.

Steganography allows the embedding of secret messages within digital media, and **LSB substitution** is one of the most widely used techniques for hiding data in images. However, the amount of data that can be embedded is often limited. By integrating **Huffman coding**, a lossless compression algorithm, we can significantly reduce the size of the secret message before embedding, thus increasing the capacity of hidden information without sacrificing image quality.

This approach is ideal for **secure communication, watermarking, and digital forensics** applications where covert data transmission is required.

---

## **Table of Contents**

- [Installation](#installation)
- [Data](#data)
- [Usage](#usage)
- [Methodology](#methodology)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [Future Work](#future-work)
- [License](#license)
- [Contact](#contact)

---

## **Installation**

To set up and run this project, follow these steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/huffman-lsb-compression.git

# Navigate to the project directory
cd huffman-lsb-compression

# Install required dependencies
pip install -r requirements.txt
```

Ensure that **Python 3.x** is installed before proceeding.

---

## **Data**

The project works with:
- **Cover images**: PNG/JPG images where the secret message is embedded.
- **Secret messages**: Text-based information that needs to be compressed and hidden.

These inputs are processed, compressed, and embedded into the image files using Huffman coding and LSB techniques.

---

## **Usage**

To run the encoding and decoding processes, execute:

```bash
# Run the main script
python main.py
```

This script will:
1. Read the input image and secret text.
2. Compress the text using Huffman encoding.
3. Embed the compressed binary data into the image using LSB.
4. Save the modified image.

For **decoding**, the script will:
1. Extract the LSB from the modified image.
2. Decode the extracted bits using the Huffman dictionary.
3. Recover the original secret message.

---

## **Methodology**

### **1. Encoding Process**
✅ Convert the cover image to **grayscale** for uniform pixel intensity.
✅ **Resize** the image if necessary to match the data requirements.
✅ Convert the **secret message** into binary format.
✅ Apply **Huffman coding** to compress the binary message, reducing its size.
✅ Embed the **compressed message** into the **Least Significant Bits (LSB)** of pixel values.
✅ Save the stego-image containing the hidden information.

### **2. Decoding Process**
✅ Extract the **LSB bits** from the stego-image.
✅ Use the **Huffman dictionary** to **decode the extracted bits**.
✅ Retrieve and reconstruct the **original secret message**.

### **Why Huffman + LSB?**
🔹 **Huffman Coding** reduces the message size, allowing **more data to be embedded** in the image.
🔹 **LSB Steganography** ensures that changes in pixel values are **imperceptible to the human eye**.
🔹 Combining these techniques allows for **higher capacity and improved image quality**.

---

## **Results**

### **📌 Key Findings:**
✔ **Compression Efficiency**: Huffman coding reduced the message size by **up to 57%**.
✔ **Steganographic Performance**:
   - **Peak Signal-to-Noise Ratio (PSNR)** for **LSB + Huffman**: **77.53 dB**
   - **PSNR for pure LSB**: **73.79 dB**
✔ **Data Capacity Increase**: Allowed **20-30% more data** to be hidden compared to standard LSB steganography.

### **📊 Observations:**
- **Higher compression ratios** improved embedding capacity while keeping distortions minimal.
- **PSNR scores indicate excellent image quality** after data embedding.
- The **decoding accuracy** remained **100%** across all test cases.

---

## **Technologies Used**

The project was developed using:

- **Python 3.x**  
- **NumPy** – for numerical computations  
- **Pillow (PIL)** – for image processing  
- **Matplotlib** – for visualization  
- **Bit Manipulation Techniques**  

These libraries allow efficient image manipulation and binary-level data embedding.

---

## **Future Work**

🔹 Implement **additional compression techniques** (e.g., Arithmetic Coding) for comparison.  
🔹 Test the model on **different image formats (JPEG, BMP, GIF)** to analyze compression efficiency.  
🔹 **Enhance security** by integrating **encryption** before embedding.  
🔹 Explore the use of **deep learning** for **adaptive steganography** to dynamically optimize embedding.  
🔹 Study the effects of **lossy compression (JPEG)** on message recovery.  

---

## **License**

This project is released under the **MIT License**.

```
MIT License
Copyright (c) 2025 Your Name
```

---

## **Contact**

For any inquiries or contributions, feel free to reach out:

📧 **Email**: [hrithiksarda4@gmai.com](mailto:your.email@example.com) 

---

