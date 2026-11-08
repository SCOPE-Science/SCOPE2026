#!/usr/bin/env python3
"""Independent finite checks for rational-base binary digit-sum parity."""

def digits_parity(n):
    parity=0
    while n:
        remainder=n%3
        parity^=remainder&1
        n=2*(n-remainder)//3
    return parity

def build_by_recurrence(size):
    x=bytearray(size)
    for j in range(1,size):
        n,r=divmod(j,3)
        x[j]=(x[2*n]+r)&1
    return x

N=100000
x=build_by_recurrence(N)
y=x[::2]
for j in range(N):
    assert digits_parity(j)==x[j],('digit parity',j)
for n in range(N//3):
    assert tuple(x[3*n:3*n+3]) == (y[n],1-y[n],y[n])
for n in range((len(y)-2)//3):
    assert tuple(y[3*n:3*n+3]) == (y[2*n],y[2*n],1-y[2*n+1])
assert y[6:11] == bytes([1]*5)
assert x[18:33] == bytes([1,0,1]*5)
assert not any(all(y[j]==y[i] for j in range(i,i+6)) for i in range(len(y)-5))
assert not any(all(y[i+j] != y[i+j+1] for j in range(3)) for i in range(len(y)-3))
assert not any(all(x[i+j] != x[i+j+1] for j in range(9)) for i in range(N-9))
for word,name in [(x,'x'),(y,'y')]:
    maxperiod=80
    for p in range(1,maxperiod+1):
        matches=0
        for i in range(p,len(word)):
            if word[i]==word[i-p]:
                matches+=1
            else:
                matches=0
            assert matches < 4*p+1, ('periodic factor length >= 5p+1',name,p,i)
    print(f'{name}: no period-p factor of length 5p+1 for 1 <= p <= 80 in {len(word)} terms')
print(f'100000 independently computed base-3/2 digit-parity values agree with recurrence')
print(f'33333 x blocks and { (len(y)-2)//3 } y blocks satisfy exact identities')
print('forbidden six-constant y, four-alternating y, ten-alternating x patterns absent')
print('fivefold factor: x[18:33]=(101)^5; auxiliary y[6:11]=11111')
print('all finite checks passed; no finite computation certifies the infinite theorem')
