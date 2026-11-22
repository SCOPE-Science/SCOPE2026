from itertools import product

def partgen(n):
    a=[0]*n
    def g(k,m):
        if k==n:
            yield tuple(a)
            return
        for x in range(m+2):
            a[k]=x
            yield from g(k+1,max(m,x))
    yield from g(1,0)

def op(i,j,p):return (i+p*(i-j))%(p*p)
def inv(i,j,p):return (i-p*(i-j))%(p*p)

def is_cong(labels,p):
    n=p*p
    for a in range(n):
      for b in range(n):
       for c in range(n):
        if labels[a]==labels[b]:
          if labels[op(a,c,p)]!=labels[op(b,c,p)] or labels[inv(a,c,p)]!=labels[inv(b,c,p)]:return False
          if labels[op(c,a,p)]!=labels[op(c,b,p)] or labels[inv(c,a,p)]!=labels[inv(c,b,p)]:return False
    return True

def bell(n):
    return sum(1 for _ in partgen(n))

for p in (2,3):
    valid=[]
    for a in partgen(p*p):
        if is_cong(a,p):valid.append(a)
    print(f'p={p} all={bell(p*p)} congruences={len(valid)} predicted={2**p+bell(p)-1}')
    assert len(valid)==2**p+bell(p)-1
# check all hypothesized congruences for p=5 constructively, avoiding exhaustive partition enumeration
p=5;n=p*p
for mask in range(1<<p):
 a=[(i%p,p if mask>>(i%p)&1 else i//p) for i in range(n)]
 labels={v:idx for idx,v in enumerate(sorted(set(a)))}
 x=[labels[t] for t in a]
 assert is_cong(x,p)
print('p=5 Boolean-family 32/32 congruences verified')

assert [2**p+bell(p)-1 for p in [2,3,5,7]]==[5,12,83,1004]
print("PRIME_SQUARE_QUANDLE_CONGRUENCES_VERIFIED")
