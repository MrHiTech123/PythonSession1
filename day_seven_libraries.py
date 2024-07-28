import random
import time
import webbrowser
import os



# def time.sleep

x = random.random()

time.sleep(2)

print('Rizzler', x)



# webbrowser.open('https://www.bing.com/ck/a?!&&p=9db0b1787d9f71f9JmltdHM9MTcyMDQ4MzIwMCZpZ3VpZD0zZGRjMzQyZi1jNDEzLTY4ODktMGY0ZC0yMDhkYzU1NzY5OGEmaW5zaWQ9NTg4NA&ptn=3&ver=2&hsh=3&fclid=3ddc342f-c413-6889-0f4d-208dc557698a&u=a1L3ZpZGVvcy9yaXZlcnZpZXcvcmVsYXRlZHZpZGVvP3E9cmljaytyb2xsJm1pZD04M0QyRDlGOEM5OTg4Q0FBREZFQzgzRDJEOUY4Qzk5ODhDQUFERkVDJkZPUk09VklSRQ&ntb=1')

start = time.time()

for i in range(1000000):
    print('Hello world skibidi')

end = time.time()

print(f'It took {end - start}')




