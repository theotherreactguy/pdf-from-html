FROM alpine

RUN apk update && apk add --no-cache \
    python3 \
    py-pip \
    gcc \
    python3-dev \
    python2-dev \
    linux-headers \
    libc-dev \
    libffi \
    libffi-dev \
    cairo \
    pango \
    gdk-pixbuf \
    libxml2 \
    libxslt \
    libffi

WORKDIR /app
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
