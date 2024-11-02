import asyncio
#1
# async def remove_numbers_from_password(password):
#     updated_password = password
#     while any(char.isdigit() for char in updated_password):
#         updated_password = ''.join(char for char in updated_password if not char.isdigit())
#         await asyncio.sleep(0.1)
#     return updated_password
#
# async def main():
#     password = str(input(' = '))
#     updated_password = await remove_numbers_from_password(password)
#     print(f"Yangilangan parol: {updated_password}")
#
#
# asyncio.run(main())
#---------------------------------------------------------------------------
#2
# async def first_ten(text):
#     if len(text) > 10:
#         i = 0
#         while i < 10:
#             print(text[i], end='')
#             i += 1
#             await asyncio.sleep(0.1)
#         print()
#     else:
#         print("Matn 10 belgidan qisqa.")
#
# async def main():
#     text = "Salom bu matn 10 harfdan uzun"
#     await first_ten(text)
#
# asyncio.run(main())
#-------------------------------------------------------------------------------
#3
# async def remove_numbers(name):
#     updated_name = name
#     while any(char.isdigit() for char in updated_name):
#         updated_name = ''.join(char for char in updated_name if not char.isdigit())
#         await asyncio.sleep(0.1)
#     return updated_name
#
# async def main():
#     name = "vali1j2o3n"
#     cleaned_name = await remove_numbers(name)
#     print(f"Tozalangan ism: {cleaned_name}")
#
# asyncio.run(main())
#---------------------------------------------------------------------------------
#4
# async def process_text(text):
#     updated_text = text
#     while any(char.isupper() for char in updated_text) or ' ' in updated_text:
#         updated_text = ''.join(char.lower() for char in updated_text if char != ' ')
#         await asyncio.sleep(0.1)
#     return updated_text
#
# async def main():
#     text = "Bu Matnni Tozalash Va Kichik Harflarga O'zgartirish."
#     cleaned_text = await process_text(text)
#     print(f"Tozalangan matn: {cleaned_text}")
#
# asyncio.run(main())
#---------------------------------------------------------------------------------
#
# async def unli_harflarni_top(matn):
#     unli_harflar = "aeiouAEIOU"
#     natija = []
#
#     for harf in matn:
#         await asyncio.sleep(0.1)
#         if harf in unli_harflar:
#             natija.append(harf)
#
#     return ''.join(natija)
#
# async def main():
#     matn = "Hello world"
#     unli_harflar = await unli_harflarni_top(matn)
#     print(f"Unli harflar: {unli_harflar}")
#
# asyncio.run(main())
#----------------------------------------------------------------

# async def ozgartirish(matn):
#     i = 0
#     natija = ""
#
#     while i < len(matn):
#         if i < len(matn) - 1 and matn[i] == 'a' and matn[i + 1] == 'b':
#             natija += '#'
#             i += 2
#         else:
#             natija += matn[i]
#             i += 1
#         await asyncio.sleep(0.1)
#
#     return natija
#
# async def main():
#     soz = "abacabadab"
#     natija = await ozgartirish(soz)
#     print(f"O'zgartirilgan so'z: {natija}")
#
# asyncio.run(main())
#-----------------------------------------------------------------------------------
#
# async def teskari_matn(matn):
#     natija = ""
#     i = len(matn) - 1
#
#     while i >= 0:
#         if matn[i].isdigit():
#             natija += matn[i]
#         else:
#             return "Barcha belgilar raqam bo'lishi kerak."
#         i -= 1
#         await asyncio.sleep(0.1)
#
#     return natija
#
# async def main():
#     raqamli_matn = "123456789"
#     natija = await teskari_matn(raqamli_matn)
#     print(f"Teskari matn: {natija}")
#
# asyncio.run(main())
#--------------------------------------------------------------------------------
#
# async def ortadagi_harfni_olib_tashlash(matn):
#     if len(matn) == 0:
#         return matn
#
#     ortasi = len(matn) // 2
#     natija = ""
#     i = 0
#
#     while i < len(matn):
#         if i != ortasi:
#
#             natija += matn[i]
#
#             i += 1
#
#     await asyncio.sleep(0.1)
#     return natija
#
#
#
#
#
# async def main():
#     soz = "Python"
#     natija = await ortadagi_harfni_olib_tashlash(soz)
#     print(f"O'rtadagi harf olib tashlangan so'z: {natija}")
#
#     asyncio.run(main())
#-------------------------------------------------------------------------------

# async def ismni_kichik_qilish(ism):
#     await asyncio.sleep(0.1)
#
#     if ism.endswith('a'):
#         return ism.lower()
#     else:
#         return ism
#
# async def main():
#     ism = "Masha"
#     natija = await ismni_kichik_qilish(ism)
#     print(f"O'zgartirilgan ism: {natija}")
#
# asyncio.run(main())
#-----------------------------------------------------------------

# async def takrorlanayotgan_harflarni_olib_tashlash(matn):
#     natija = ""
#     korilgan_harflar = set()
#
#     i = 0
#     while i < len(matn):
#         harf = matn[i]
#         if harf not in korilgan_harflar:
#             natija += harf
#             korilgan_harflar.add(harf)
#         i += 1
#         await asyncio.sleep(0.1)
#
#     return natija
#
# async def main():
#     matn = "balibek"
#     natija = await takrorlanayotgan_harflarni_olib_tashlash(matn)
#     print(f"Takrorlanmagan harflar: {natija}")
#
# asyncio.run(main())
#----------------------------------------------------------------

# async def unli_harflarni_tasdiqlash(soz):
#     unli_harflar = "aeiouAEIOU"
#
#
#     for harf in soz:
#         await asyncio.sleep(0.1)
#         if harf not in unli_harflar:
#             return soz
#
#     return soz.upper()
#
#
# async def main():
#     soz = "aeiou"
#     natija = await unli_harflarni_tasdiqlash(soz)
#     print(f"O'zgartirilgan so'z: {natija}")
#
#
# asyncio.run(main())


