FROM python:3.9.6
WORKDIR /app

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

RUN apt-get update && \
	apt-get install -y gcc google-chrome-stable && \
	dpkg --add-architecture i386 && \
	apt clean && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --upgrade pip && \
	pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3", "-u", "main.py"]