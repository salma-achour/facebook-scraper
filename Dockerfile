FROM python:3.8-slim-bullseye
WORKDIR /FbPageScraper/
COPY ./requirements.txt /FbPageScraper/src/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /FbPageScraper/src/requirements.txt
EXPOSE 5000
COPY . /FbPageScraper/
ENV PYTHONPATH "${PYTHONPATH}:/FbPageScraper/app"
ENTRYPOINT [ "uvicorn", "app.main:app" , "--port", "5000", "--host", "0.0.0.0"]