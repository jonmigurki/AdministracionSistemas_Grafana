FROM python:3.7-alpine
RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev
RUN pip install --upgrade pip && pip install crate && pip install pytrends
COPY $pwd/Conexion.py /home/Conexion.py
WORKDIR /home
ENTRYPOINT ["python3"]
CMD ["Conexion.py"]