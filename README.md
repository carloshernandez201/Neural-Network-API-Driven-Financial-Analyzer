# TradeGPT: AI-Powered Market Intelligence & Portfolio Simulator 💹🧠

**TradeGPT** is an intelligent, full-stack financial web app that blends real-time market data, AI-powered news summarization, and predictive analytics to help users simulate investment strategies like a pro.

## 🔥 Key Features

- **Real-Time Stock Tracking**  
  Fetches live stock prices via the Financial Modeling Prep API to simulate purchases, track performance, and analyze ROI in real-time.

- **Portfolio Simulation Engine**  
  Add stocks to your simulated portfolio, monitor sector breakdowns, and observe how market movements affect your total valuation.

- **AI-Driven Market News**  
  Uses **LangChain** and **ChatGPT** to pull and summarize trending market news from **Finnhub**, giving users a concise snapshot of relevant financial developments.

- **LSTM-Based Stock Prediction**  
  Implements a **Long Short-Term Memory (LSTM)** neural network to forecast future stock prices based on historical trends, aiding decision-making.

- **Streamlined Interface**  
  Intuitive frontend for exploring tickers, managing a portfolio, and accessing smart insights without bloat.

## 🚀 Tech Stack

- **Frontend**: React  
- **Backend**: Python (FastAPI or Flask)  
- **AI/NLP**: LangChain, OpenAI GPT, Finnhub API  
- **Data**: Financial Modeling Prep API  
- **ML**: PyTorch / TensorFlow (for LSTM model)

## 🛠 Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/tradegpt.git
   cd tradegpt
   ```

2. **Install Python dependencies**  
   ```bash
   pip install langchain
   ```

3. **Set up API keys**  
   Create a `.env` file in the root directory and include:
   ```env
   OPENAI_API_KEY=your_openai_key
   FINNHUB_API_KEY=your_finnhub_key
   FMP_API_KEY=your_financial_modeling_prep_key
   LANCGCHAIN_API_KEY = you_langhchainapikey
   ```

4. **Run the app**  
   ```bash
   python app.py
   ```

## 📈 Example Use Cases

- Simulate investment strategies before going live
- Get a daily GPT-powered market brief
- Explore historical vs predicted performance of assets
- Build a smarter portfolio with both data and insight

---

**Disclaimer**: This tool is for educational and simulation purposes only. It does not constitute financial advice.
