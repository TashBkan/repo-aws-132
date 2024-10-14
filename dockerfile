FROM Python:3.9.16

WORKDIR /project

COPY . .

RUN pip install -r requierement.txt

CMD ["python", "server.py"]