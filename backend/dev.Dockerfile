FROM python:3.14

# Create python virtual environment to isolate the app and installs from system level python
RUN python -m venv /opt/venv/
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app 

# Copy local folder/file container destination
COPY requirements.txt /tmp/requirements.txt

# Run within container while building
RUN pip install -r /tmp/requirements.txt
COPY ./src .

CMD ["python","-m","http.server","8000"]