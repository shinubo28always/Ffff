FROM python:3.10-slim-bullseye
WORKDIR /app

COPY requirements.txt requirements.txt

# Pip ko update karke install karne se speed badh jati hai
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Check kar lena file ka naam main.py hai ya bot.py
CMD ["python3", "main.py"]

