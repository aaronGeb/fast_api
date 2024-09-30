#!/usr/bin/env python3
import asyncio as A
import time
async def q():
  print('WHy can\'t programme tell jokes')
  await A.sleep(10)
  print('Because they always wait for the right time to laugh') 


async def p():
  print('I am a programmer')


async def main():
  await A.gather(q(), p())


if __name__ == '__main__':
  A.run(main())