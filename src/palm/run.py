import os
import google.generativeai as palm


PALM_KEY = os.getenv("PALM_KEY")
palm.configure(api_key=PALM_KEY)

response = palm.chat(messages='Hello')
print(response.last)
