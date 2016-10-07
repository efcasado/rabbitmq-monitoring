#!/usr/bin/env python
import pika
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbitmq'))
channel = connection.channel()

while True:
    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

    print(" [x] Sent 'Hello World!'")

    time.sleep(random.random() * random.randint(1, 2))
connection.close()
