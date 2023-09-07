# Use Python 3.9 as base image
FROM python:3.9

# Set the environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV GECKODRIVER_VER v0.31.0
ENV FIREFOX_VER 96.0.1

# Update packages and install necessary packages
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    libc6 wget bzip2 libxtst6 firefox-esr libgtk-3-0 libx11-xcb-dev \
    libdbus-glib-1-2 libxt6 libpci-dev libx11-xcb1 libdbus-glib-1-2 


# Download and install Firefox and Geckodriver in a single layer
WORKDIR /tmp
RUN curl -sSLO https://download-installer.cdn.mozilla.net/pub/firefox/releases/${FIREFOX_VER}/linux-x86_64/en-US/firefox-${FIREFOX_VER}.tar.bz2 \
    && tar -jxf firefox-* -C /opt/ \
    && chmod 755 /opt/firefox \
    && chmod 755 /opt/firefox/firefox \
    && curl -sSLO https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VER}/geckodriver-${GECKODRIVER_VER}-linux64.tar.gz \
    && tar zxf geckodriver-*.tar.gz -C /usr/bin/ \
    && rm -rf /tmp/* \
    && echo 'PATH="/usr/bin:${PATH}"' >> /etc/profile

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000


# Run the Python script
CMD ["python", "./api.py"]
