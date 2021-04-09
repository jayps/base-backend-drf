FROM python:3.9.4-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
RUN ["chmod", "+x", "/code/entrypoint.sh"]
ENTRYPOINT /code/entrypoint.sh
