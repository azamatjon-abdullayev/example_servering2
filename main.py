# import time
# import asyncio
#
#
# async def generate_number():
#     i = 1
#     while True:
#         print(i)
#         if i ==10:
#             break
#         await asyncio.sleep(1)
#         i +=1
#
# async def text():
#     i = 1
#     while True:
#         if i == 10:
#             break
#         await asyncio.sleep(1)
#         i += 1
#         print("Asinxromlik ishladi")
#
# async def main():
#     task1 = generate_number()
#     task2 = text()
#
#     await asyncio.gather(task1, task2)
#
# asyncio.run(main())

#========================================================================================

# import time
# import asyncio
#
#
# async def generate_number():
#     i = 1
#     while True:
#         print(i)
#         if i ==10:
#             break
#         await asyncio.sleep(1)
#         i +=1
#
# async def text():
#     i = 1
#     while True:
#         if i == 10:
#             break
#         await asyncio.sleep(1)
#         i += 1
#         print("Asinxromlik ishladi")
#
# async def main():
#     task1 = asyncio.create_task(generate_number())
#     task2 = asyncio.create_task(text())
#     await task1
#     await task2
#
#
# asyncio.run(main())
#----------------------------------------------------------------------------

