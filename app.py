import pandas as pd
import gradio as gr
from sklearn.ensemble import IsolationForest

# Load dataset
data = pd.read_csv("transaction_anomalies_dataset.csv")

# Feature columns
relevant_features = ['Transaction_Amount', 'Average_Transaction_Amount', 'Frequency_of_Transactions']

# Flag anomalies using IsolationForest
model = IsolationForest(contamination=0.02, random_state=42)
model.fit(data[relevant_features])
data['Is_Anomaly'] = model.predict(data[relevant_features])
data['Is_Anomaly'] = data['Is_Anomaly'].apply(lambda x: 1 if x == -1 else 0)

# Gradio prediction function
def predict_anomaly(transaction_amount, avg_transaction_amount, frequency):
    input_df = pd.DataFrame([{
        'Transaction_Amount': transaction_amount,
        'Average_Transaction_Amount': avg_transaction_amount,
        'Frequency_of_Transactions': frequency
    }])
    pred = model.predict(input_df)[0]
    return "Anomaly" if pred == -1 else "Normal"

# Gradio interface
demo = gr.Interface(
    fn=predict_anomaly,
    inputs=[
        gr.Number(label="Transaction Amount"),
        gr.Number(label="Average Transaction Amount"),
        gr.Number(label="Frequency of Transactions"),
    ],
    outputs="text",
    title="Transaction Anomaly Detector",
    description="Detect if a transaction is anomalous using Isolation Forest model."
)

if __name__ == "__main__":
    demo.launch()
