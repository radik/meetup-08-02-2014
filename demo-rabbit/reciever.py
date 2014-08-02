#!/usr/bin/env python
import pika
import sys


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

if __name__ == '__main__':
    if not len(sys.argv) == 3:
        sys.exit('Usage: python sender.py -host -port')

    host = sys.argv[1]
    port = int(sys.argv[2])
    conn = pika.BlockingConnection(pika.ConnectionParameters(host, port))
    channel = conn.channel()
    channel.queue_declare(queue='hello')
    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
