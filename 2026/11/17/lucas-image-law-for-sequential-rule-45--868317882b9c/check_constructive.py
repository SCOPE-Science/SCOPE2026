"""Independent constructive predecessor check for Rule 45 sequential images."""
from functools import lru_cache

def rule45(a,b,c):
    bits = [1,0,1,1,0,1,0,0]  # index 000 through 111
    return bits[(a<<2)|(b<<1)|c]

def sweep(x):
    z=list(x)
    n=len(z)
    for i in range(n):
        z[i]=rule45(z[(i-1)%n],z[i],z[(i+1)%n])
    return tuple(z)

def characterization(y):
    n=len(y)
    marks=[int(y[i]==y[i-1]) for i in range(1,n-1)]
    if any(a and b for a,b in zip(marks,marks[1:])):
        return False
    b=y[0]
    q=y[-1]^y[-2]
    if b==0:
        return q==1
    return (not marks[-1]) if q==0 else (not marks[0])

# Check every target against an independent existential predecessor solver;
# do not re-use the counting argument to construct an input.
def preimage_exists(y):
    n=len(y)
    for x0 in (0,1):
      for x1 in (0,1):
        for xl in (0,1):
          if rule45(xl,x0,x1)!=y[0]:continue
          poss={x1}
          for i in range(1,n-1):
              new=set()
              for cur in poss:
                  for nex in (0,1):
                      if rule45(y[i-1],cur,nex)==y[i]:new.add(nex)
              poss=new
              if not poss:break
          if xl in poss and rule45(y[n-2],xl,y[0])==y[n-1]:
              return True
    return False

def lucas(n):
    a,b=2,1
    for _ in range(2,n+1):a,b=b,a+b
    return b

for n in range(3,16):
    from itertools import product
    outputs={sweep(x) for x in product((0,1),repeat=n)}
    criterion={y for y in product((0,1),repeat=n) if characterization(y)}
    assert outputs==criterion,(n,len(outputs),len(criterion))
    assert len(outputs)==lucas(n)
    if n<=11:
       assert all(preimage_exists(y)==(y in outputs) for y in product((0,1),repeat=n))
    print(n,len(outputs))
print('CONSTRUCTIVE_PREIMAGE_PASS')
