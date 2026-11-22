"""Independent exhaustive word-level check of the all-length counting law.
No reuse of graph_checker functions. Python 3, standard library only.
"""

def valid(bits):
    m=len(bits)
    for b in range(m):
        if b>=2 and bits[b]==bits[b-1]==bits[b-2]:return False
        if b>=5:
            w=bits[b-5:b+1]
            a=w[0]+w[1]
            c=w[2]+w[3]
            d=w[4]+w[5]
            if a==c==d:return False
    return True

A=[]
for n in range(20):
    total=sum(valid(tuple((v>>j)&1 for j in range(n))) for v in range(1<<n))
    expected=([1,2,4,6,10,16,18,12][n] if n<8 else 10+2*(n%3==0))
    assert total==expected,(n,total,expected)
    A.append(total)
print('PASS exhaustive enumeration of all 2^n binary words for 0 <= n <= 19')
print('Counts',A)

# Independent verification of the first full Abelian-cube obstruction
for n in (9,10):
 total=0
 for v in range(1<<n):
    w=tuple((v>>j)&1 for j in range(n))
    if all(len({sum(w[i+k*p:i+(k+1)*p]) for k in range(3)})>1
           for p in range(1,n//3+1) for i in range(n-3*p+1)):
         total+=1
 assert total==(6 if n==9 else 0)
print('PASS separate known baseline: six all-Abelian-cube-free words of length 9, none at 10')
