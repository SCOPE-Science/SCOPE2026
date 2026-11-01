from math import comb
from itertools import product
import random

def conv_power(coeff, h, d):
    cur={(0,)*d:1}
    for _ in range(h):
        nxt={}
        for a,va in cur.items():
            for e,ve in coeff.items():
                k=tuple(a[j]+e[j] for j in range(d))
                nxt[k]=nxt.get(k,0)+va*ve
        cur=nxt
    return cur

def moment(coeff,h,d):
    q=conv_power(coeff,h,d)
    return sum(v*v for v in q.values())

def check():
    for h in range(2,11):
        s=sum(comb(h,2*k)*comb(2*k,k)*4**(h-k) for k in range(h//2+1))
        assert s == comb(2*h,h)*2**h
    cases=0
    random.seed(2711)
    for d in range(1,5):
        eps=list(product([0,1], repeat=d))
        for h in range(2,6):
            C_num=comb(2*h,h)
            C_den=2**h
            # exact product extremizer c_e=1
            coeff={e:1 for e in eps}
            lhs=moment(coeff,h,d)
            s2=sum(v*v for v in coeff.values())
            assert lhs*(C_den**d) == (C_num**d)*(s2**h)
            cases += 1
            # deterministic exact integer stress cases
            for _ in range(20):
                coeff={e:random.randint(-3,3) for e in eps}
                if all(v==0 for v in coeff.values()):
                    continue
                lhs=moment(coeff,h,d)
                s2=sum(v*v for v in coeff.values())
                assert lhs*(C_den**d) <= (C_num**d)*(s2**h)
                cases += 1
    print(f'VERIFY_OK local_identities=9 exact_cases={cases} d=1..4 h=2..5')
if __name__=='__main__':
    check()
