# Anomaly_detection_in_transactions

Read full article on https://medium.com/@smruti.po1106/anomaly-detection-in-transactions-d7e10e90f01f

🕵️‍♂️ Transaction Anomaly Detector
Detect anomalous transactions using Machine Learning (Isolation Forest) and a user-friendly Gradio interface.

📌 Overview
This project demonstrates how to apply anomaly detection to financial transactions using the Isolation Forest algorithm. The model is trained on a dataset with key transaction features and deployed through a Gradio web interface, allowing users to test the system by inputting custom transaction data.

💡 Features
Uses Isolation Forest to detect anomalies.

Lightweight and interpretable model.

Real-time predictions through a Gradio interface.

Easy-to-use interface for experimentation and demo purposes.

📊 Dataset
The model uses a dataset (transaction_anomalies_dataset.csv) with the following relevant features:

Transaction_Amount

Average_Transaction_Amount

Frequency_of_Transactions

Note: Make sure the dataset is placed in the same directory as the script.

🛠️ How It Works
Load the dataset using pandas.

Train an Isolation Forest model on selected features.

Use the trained model to label each transaction as either normal or anomalous.

Provide a simple web interface to test new transaction inputs.

🚀 Getting Started
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/transaction-anomaly-detector.git
cd transaction-anomaly-detector
2. Install dependencies
We recommend using a virtual environment:

bash
Copy
Edit
pip install -r requirements.txt
requirements.txt

text
Copy
Edit
pandas
scikit-learn
gradio
3. Add your dataset
Place your transaction_anomalies_dataset.csv file in the root of the project.

4. Run the app
bash
Copy
Edit
python app.py
The Gradio interface will launch in your browser.

🖥️ Interface Preview
You’ll see a form with 3 inputs:

Transaction Amount

Average Transaction Amount

Frequency of Transactions

It will return either:

✅ Normal

⚠️ Anomaly

📂 Project Structure
bash
Copy
Edit
├── app.py                       # Main script with model and UI
├── transaction_anomalies_dataset.csv
├── requirements.txt
└── README.md
