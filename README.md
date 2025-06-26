# Deal Flow Assistant

A "horsepower" project built for the Caprae Capital AI Readiness Challenge. This is an AI-powered co-pilot for acquisition entrepreneurs, designed to automate deal flow analysis and empower the searcher with an analytical and emotional edge.

Instead of a generic sales scraper, this tool finds and analyzes businesses through the lens of a searcher looking for their next acquisition. It embodies the [#bleedandbuild](https://www.linkedin.com/feed/hashtag/?keywords=bleedandbuild) ethos by providing a scrappy, intelligent weapon for the underdog founder.

---

## 🎥 Demo
<video src="https://user-images.githubusercontent.com//video.mp4" controls width="600"></video>

---

## ✨ Core Features

* **Acquisition Signal Scraping**: Goes beyond simple tech stacks to find meaningful signals of owner fatigue (e.g., outdated copyrights, inactive blogs) and business stability.
* **Opinionated Fit Score**: Automatically calculates a "Potential Fit Score" (1-10) for each company based on a pre-defined search fund thesis: "find a stable, yet potentially neglected, business."
* **AI "Deal Memo" Generation**: Acts as an analyst-in-a-box, using Google's Gemini AI to generate a concise summary of the acquisition opportunity and justify the fit score.
* **Empathetic Outreach Crafting**: Generates a respectful, personalized email draft designed to start a human conversation with a business owner about their legacy, not just "sell" them.

---

## 🛠️ Technology Stack

* **Backend**: Python
* **Web Framework**: Streamlit
* **Web Scraping**: Selenium
* **AI Model**: Google Gemini API
* **Driver Management**: `webdriver-manager`

---

## 🚀 Setup and Installation

Follow these steps to get the Deal Flow Assistant running on your local machine.

### Step 1: Clone the Repository

First, clone this repository to your local machine using Git.

```bash
git clone [Your Repository SSH or HTTPS URL]
cd [your-repository-folder-name]
```

### Step 2: Set Up a Virtual Environment (Recommended)

It is highly recommended to use a virtual environment to keep project dependencies isolated.

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

### Step 3: Install Dependencies

Install all the required Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```
*(Note: If you haven't created one, a `requirements.txt` file should contain `streamlit`, `selenium`, `webdriver-manager`, `pandas`, and `google-generativeai`.)*

### Step 4: Configure Your API Key

This application uses the Google Gemini API to power its AI features. You will need to provide your own API key.

1.  Create a file named `.env` in the root directory of the project.
2.  Add your API key to this file in the following format:

    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

3.  The application uses the `python-dotenv` library (which should be in `requirements.txt`) to automatically load this key.

---

## ▶️ How to Run the Application

Once the setup is complete, you can run the Streamlit application with a single command:

```bash
streamlit run app.py
```

This will start the web server and open the application in your default web browser. You can now paste a list of websites and begin your analysis!