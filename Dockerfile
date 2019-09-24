FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
ADD my_account.session /app/my_account.session
RUN pip install -r requirements.txt
ADD app /app/app
CMD [ "python3", "app" ]