# # # items = {'공책':325, '연필':427, '지우개':125, '복사지':510}
# # # num =int(input("파악 재고수 기준 : "))
# # # for key in items:
# # #   if(items[key]<num):
# # #     print(key," : ",items[key])

# # engkor_dict = dict()
# # while (1):
# #   eng = input("영어 단어 : ")
# #   if len(eng)==0:
# #     break
# #   if len(engkor_dict)<=0:
# #     print("사전이 비어 있습니다.")
# #   if eng in engkor_dict:
# #     print(eng, " : ",engkor_dict[eng])
# #   else:
# #     if len(engkor_dict)>0:
# #         print(eng," 단어가 등록되어 있지 않습니다.")
# #     print("단어를 추가합니다.")
# #     kor=input("한글 단어 : ")
# #     engkor_dict[eng]=kor
# # print(engkor_dict)

# import math
# moneys = {1:50000, 2:10000, 3:5000, 4:1000, 5:500, 6:100, 7:50, 8:10, 9:5, 10:1}
# p = int(input("금액 : "))
# c=0
# n=0
# for i in moneys:
#   print(moneys[i]," : ", math.trunc(p/moneys[i]))
#   if math.trunc(p/moneys[i])!=0:
#     c+=1
#     n+=math.trunc(p/moneys[i])
#   p=p-math.trunc(p/moneys[i])*moneys[i]
# print("총 ", c," 종류 ",n," 개 필요")

import turtle
import math

r = 100
t = turtle.Turtle()
t.penup()
for a in range(0, 361):
  rad = math.radians(a)
  x = r*math.cos(rad)
  y = r*math.sin(rad)
  t.goto(x,y)
  t.pendown()
turtle.exitonclick()

asdf