#!/usr/bin/env python
import os
import pika
import random
import time


queue = os.environ['RABBITMQ_QUEUE']

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbitmq'))
channel = connection.channel()


while True:
    channel.queue_declare(queue=queue)

    channel.basic_publish(exchange='',
                      routing_key=queue,
                      body='Hello World!')

    print(" [x] Sent 'Hello World!'")

    time.sleep(random.random() * random.randint(1, 2))


connection.close()
