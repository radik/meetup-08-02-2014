#!/usr/bin/env python
import pika
import time
import sys

if __name__ == '__main__':
    if not len(sys.argv) == 3:
        sys.exit('Usage: python sender.py -host -port')

    host = sys.argv[1]
    port = int(sys.argv[2])
    conn = pika.BlockingConnection(pika.ConnectionParameters(host, port))
    channel = conn.channel()
    channel.queue_declare(queue='hello')
    while True:
        time.sleep(5)
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body='Hello World!')
