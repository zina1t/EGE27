f = open('27Bdosrok.txt')
k = (int(f.readline()))
n = (int(f.readline()))
mb = 0
m = 0
a = [int(x) for x in f]
for i in range(k, n):
    mb = max(mb, a[i-k])
    m = max(m, mb + a[i])
print(m)