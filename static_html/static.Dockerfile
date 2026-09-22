# declare what image to use in the format `FROM image_name:version`
FROM python:3.14

WORKDIR /app

# COPY local_folder container_folder
# RUN mkdir -p /static_folder
# COPY ./static_html /static_folder
# COPY ./static_html /app/

COPY ./src .

# RUN echo "hello" > index.html

# docker build -f Dockerfilename -t username/appname:version . 
# docker run -it appname
# docker push username/appname:version

# To run built-in python web server

# python -m http.server 8000 
# docker command to have container running on a port
#docker run -it -p localport:containerport appname
# CMD ["python","-m","http.server","8000"]