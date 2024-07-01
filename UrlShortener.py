# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hwXqJfJnbsAlAK2HQ83B1RuC2sI8twnw
"""

from collections import defaultdict

# Character set for generating short URLs
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# In-memory storage (replace with database for persistence)
url_map = defaultdict(str)  # key: short URL, value: long URL

def generate_short_url():
  """Generates a random, unique short URL"""
  short_url = ""
  while True:
    for _ in range(6):  # Length of the short URL (can be adjusted)
      short_url += characters[random.randint(0, len(characters) - 1)]
    if short_url not in url_map:
      return short_url

def shorten_url(long_url):
  """Shortens a long URL and adds it to the mapping"""
  short_url = generate_short_url()
  url_map[short_url] = long_url
  return short_url

def get_long_url(short_url):
  """Retrieves the long URL for a given short URL"""
  if short_url in url_map:
    return url_map[short_url]
  else:
    return None

# Example usage
long_url = "https://www.example.com/very/long/url/to/shorten"
short_url = shorten_url(long_url)
print(f"Long URL: {long_url}")
print(f"Short URL: {short_url}")

# Redirect functionality (can be integrated into a web server)
redirected_url = get_long_url("your_short_code")
if redirected_url:
  # Redirect user to the long URL using a web framework
  pass
else:
  print("Invalid short URL")