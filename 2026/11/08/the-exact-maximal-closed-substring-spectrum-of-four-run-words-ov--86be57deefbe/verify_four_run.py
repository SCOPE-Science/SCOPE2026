from itertools import product
from collections import Counter
from math import comb

def is_closed(v):
    n=len(v)
    if n==1:return True
    for ell in range(1,n):
        if v[:ell]==v[-ell:]:
            count=sum(v[j:j+ell]==v[:ell] for j in range(n-ell+1))
            if count==2:return True
    return False

def exhaustive_mcs(word):
    n=len(word)
    closed={(i,j):is_closed(word[i:j+1]) for i in range(n) for j in range(i,n)}
    return {(i,j) for i in range(n) for j in range(i,n) if closed[(i,j)] and not closed.get((i-1,j),False) and not closed.get((i,j+1),False)}

def predicted(letter,length):
    a,b,c,d=length; x,y,z,w=letter
    out={(0,a-1),(a,a+b-1),(a+b,a+b+c-1),(a+b+c,a+b+c+d-1)}
    for i,j in ((0,2),(1,3),(0,3)):
        if letter[i]!=letter[j]:continue
        if (i,j)==(0,2):
            for t in range(1,min(a,c)+1):
                if y==w and t==c:continue
                out.add((a-t,a+b+t-1))
        elif (i,j)==(1,3):
            for t in range(1,min(b,d)+1):
                if x==z and t==b:continue
                out.add((a+b-t,a+b+c+t-1))
        elif (i,j)==(0,3):
            for t in range(1,min(a,d)+1):
                out.add((a-t,a+b+c+t-1))
    if x==z and y==w:
        i=min(a,c);j=min(b,d)
        out.add((a-i,a+b+c+j-1))
    return out

def count_formula(L,length):
    a,b,c,d=length;x,y,z,w=L
    if len(set(L))==4:return 4
    if x==z and y==w:return 5+min(a,c)+min(b,d)-(c<=a)-(b<=d)
    if x==z:return 4+min(a,c)
    if y==w:return 4+min(b,d)
    if x==w:return 4+min(a,d)
    assert False

tried=0
for q,maxrun in ((2,6),(3,4),(4,3)):
 for L in product(range(q),repeat=4):
  if any(L[i]==L[i+1] for i in range(3)):continue
  for A in product(range(1,maxrun+1),repeat=4):
   w=''.join(str(v)*k for v,k in zip(L,A))
   actual=exhaustive_mcs(w)
   wanted=predicted(L,A)
   if actual!=wanted or len(actual)!=count_formula(L,A):
    print('FAIL',q,L,A,actual,wanted); raise SystemExit(1)
   tried+=1
 print('q',q,'done',tried)
print('PASS direct occurrence comparisons:',tried)

def choose(n,k):
    return comb(n,k) if n>=k>=0 else 0

def generating_coefficient(q,n,k):
    distinct=q*(q-1)*(q-2)*(q-3)
    single=3*q*(q-1)*(q-2)
    alternate=q*(q-1)
    ans=distinct*choose(n-1,3) if k==4 else 0
    t=k-5
    if t>=0:
        r=n-4-2*t
        ans += single*(choose(r+2,2)+choose(r+1,2))
    for j,cj in enumerate((1,2,1)):
        t=k-5-j
        r=n-4-j-2*t
        if t>=0 and r>=0:
            ans += alternate*cj*(t+1)*(r+1)
    return ans

for q in (2,3,4,5):
    for n in range(4,15):
        observed=Counter()
        for L in product(range(q),repeat=4):
            if any(L[i]==L[i+1] for i in range(3)):continue
            for a in range(1,n-2):
                for b in range(1,n-a-1):
                    for c in range(1,n-a-b):
                        d=n-a-b-c
                        observed[count_formula(L,(a,b,c,d))]+=1
        predicted=Counter({k:generating_coefficient(q,n,k) for k in range(4,n+2) if generating_coefficient(q,n,k)>0})
        assert observed==predicted,(q,n,observed,predicted)
        assert sum(predicted.values())==q*(q-1)**3*choose(n-1,3)
print('PASS generating-series coefficients for q=2..5 and n=4..14')
