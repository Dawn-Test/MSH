# from collections import Counter
#
    # li = [1, 2, 3, 1, 1, 2, 3, 1, 2, 5, 6, 4, 1, 2, 4, 5, 6]
# N = 5
# li_counts = Counter(li)
# top_three = li_counts.most_common(N)
# """
# most_common:列出最常见的n个元素及其计数至少是普通的。如果n为None，则列出所有元素计数。
# """
# print(li_counts)
# print(top_three)
# def sort(N):
#      d = {}
#      for i in L:
#          d[i] = L.count(i)
#      #print(d)
#      dd = sorted(d.items(),key= lambda item : item[1],reverse= True)
#      print(dd)
#      for i in range(0,N):
#         print("出现次数排第%d的数字是%d,共出现了%d次" % (i+1,dd[i][0],dd[i][1]))
#
# if __name__ == '__main__':
#      L = [1, 2, 3, 2, 3, 1, 2, 1, 2, 3, 2, 1, 4, 3, 2]
#      l = len(set(L))
#      N = int(input("请输入一个不大于%d的数:" % l))
#      sort(N)
#

my_list=[1,3,5,7]
def fn(x):
    return x*x

result=map(fn,my_list)
result=[i for i in result if i>10]
print(result)