# gunicorn.config.py
import multiprocessing

bind = "0.0.0.0:8080"
chdir = "portal"
workers = multiprocessing.cpu_count() * 2 + 1
