#!/bin/bash
# Starting RabbitMQ in background
sudo service rabbitmq-server start

# Starting the actual python app
exec python start.py
