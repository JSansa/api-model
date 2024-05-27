<<<<<<< HEAD
FROM python:3.11

WORKDIR .
=======
FROM python:3.10

>>>>>>> d5cc808e57b1bb92dac99ba8c025111d4739779e

COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

<<<<<<< HEAD
CMD ["python", "./api_titanic.py"]
=======
CMD [ "python", "./api_titanic.py" ]
>>>>>>> d5cc808e57b1bb92dac99ba8c025111d4739779e
