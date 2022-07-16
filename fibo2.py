#! /usr/bin/env python3

# Fibonacci for any integers via recursive Python

import sys
import time
import argparse
import locale
locale.setlocale(locale.LC_ALL, '')

def fibo(n) :
    if n>1 :
        # return(fibo(n-1) + fibo(n-2))
        fib, fibprev = 1, 0
        # for loop
        for x in range(2, n+1) :
            fib, fibprev = fib + fibprev, fib
        return(fib)
    elif n==1 :
        return(1)
    elif n==0 :
        return(0)
    else : # n is a negative integer
        # Fibonacci number of a negative integer is its positive equivalent * ((-1)**n)*(-1)
        return(int(fibo(-n)*((-1)**n)*(-1)))

if __name__ == '__main__' :
    parser = argparse.ArgumentParser(description = 'Fibonacci for any integers in recursive Python')
    parser.add_argument('-n', '--number', type = int, default = 5,
            help = 'enter an integer number to calculate its Fibonacci')

    args = parser.parse_args()
    # print(f'The arguments received are: {vars(args)}.')

    start = time.time()
    result = fibo(args.number)
    stop = time.time()
    print(f'Fibonacci number {args.number:,} is {result:,} (calculated in {stop-start} seconds).')
    