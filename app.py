import streamlit as st
import random

# List of Motivational Quotes
quotes = [
        "The way to get started is to quit talking and begin doing. — Walt Disney",
    "Your time is limited, so don’t waste it living someone else’s life. — Steve Jobs",
    "It always seems impossible until it’s done. — Nelson Mandela",
    "Don’t count the days, make the days count. — Muhammad Ali",
    "Do what you can, with what you have, where you are. — Theodore Roosevelt",
    "Opportunities don’t happen. You create them. — Chris Grosser",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill",
    "The future belongs to those who believe in the beauty of their dreams. — Eleanor Roosevelt",
    "I have not failed. I've just found 10,000 ways that won’t work. — Thomas Edison",
    "When something is important enough, you do it even if the odds are not in your favor. — Elon Musk",
    "If you want to live a happy life, tie it to a goal, not to people or things. — Albert Einstein",
    "He who opens a school door, closes a prison. — Victor Hugo",
    "We become what we think about. — Earl Nightingale",
    "Do what you feel in your heart to be right, for you’ll be criticized anyway. — Eleanor Roosevelt",
    "I find that the harder I work, the more luck I seem to have. — Thomas Jefferson",
    "Act as if what you do makes a difference. It does. — William James",
    "Don’t be afraid to give up the good to go for the great. — John D. Rockefeller",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. — Ralph Waldo Emerson",
    "If you look at what you have in life, you’ll always have more. — Oprah Winfrey",
    "Courage is not the absence of fear, but rather the judgment that something else is more important than fear. — Ambrose Redmoon",
    "A person who never made a mistake never tried anything new. — Albert Einstein",
    "You miss 100% of the shots you don’t take. — Wayne Gretzky",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. — Ralph Waldo Emerson",
    "Dream big and dare to fail. — Norman Vaughan",
    "The best way to predict the future is to create it. — Peter Drucker",
    "It does not matter how slowly you go as long as you do not stop. — Confucius",
    "In the middle of every difficulty lies opportunity. — Albert Einstein",
    "Hardships often prepare ordinary people for an extraordinary destiny. — C.S. Lewis",
    "Doubt kills more dreams than failure ever will. — Suzy Kassem"



]

# Streamlit UI
st.title("🌟 Daily Motivation Quotes Generator")
st.subheader("Get Inspired Every Day!")

if st.button("Generate Quote"):
    random_quote = random.choice(quotes)
    st.success(random_quote)
