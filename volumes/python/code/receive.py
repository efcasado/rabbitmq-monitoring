#!/usr/bin/env python
import os
import pika
import random
import time


queues = os.environ['RABBITMQ_QUEUES']
queues = str.split(queues, ",")

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbitmq'))
channel = connection.channel()

for q in queues:
    channel.queue_declare(queue=q)


while True:
    qi = random.randint(0, len(queues) - 1)
    channel.basic_get(queue = queues[qi])
    time.sleep(random.random() * random.randint(1, 2))



