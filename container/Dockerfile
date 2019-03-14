FROM ubuntu:16.04

RUN apt-get update -y && apt-get install software-properties-common -y
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update -y && apt-get install python3.6 libpython3.6 -y

RUN apt-get install -y --no-install-recommends \
         wget \
         python3.6 \
         python3-pip \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN pip3 install setuptools

# Set some environment variables. PYTHONUNBUFFERED keeps Python from buffering our standard
# output stream, which means that logs can be delivered to the user quickly. PYTHONDONTWRITEBYTECODE
# keeps Python from writing the .pyc files which are unnecessary in this case. We also update
# PATH so that the train and serve programs are found when the container is invoked.

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

# Set up the program in the image
COPY program /opt/program
WORKDIR /opt/program