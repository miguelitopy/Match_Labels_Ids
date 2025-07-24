#!/bin/bash

sleep 5

cd /home/backcover/Documentos/BackCoverMatchFoolProof

python3 scanner1.py &
sleep 1
python3 scanner2.py &
sleep 1
python3 server.py &

sleep 5

xdg-open http://127.0.0.1:5000

wait

