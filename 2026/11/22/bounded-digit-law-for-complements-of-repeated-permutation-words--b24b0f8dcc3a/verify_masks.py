"""Independent positional enumeration of distinct deletion-complement words."""
from itertools import combinations, product
from math import comb

def direct(q,m,k):
    P='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:q]
    w=P*(m+k); target=P*k
    out=set()
    for indices in combinations(range(len(w)), len(target)):
        if ''.join(w[i] for i in indices)!=target:
            continue
        selected=set(indices)
        out.add(''.join(c for i,c in enumerate(w) if i not in selected))
    return out

def claimed(q,m,k):
    P='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:q]
    rotations=[P[t:]+P[:t] for t in range(q)]
    out=set()
    for ds in product(range(q),repeat=m):
        if sum(ds)>q*k:continue
        s=0; parts=[]
        for d in ds:
            s=(s+d)%q;parts.append(rotations[s])
        out.add(''.join(parts))
    return out

def main():
    checks=0;counts=[]
    for q in (2,3,4):
        for m in range(0,5):
            for k in range(0,4):
                if q*(m+k)>20:continue
                a=direct(q,m,k);b=claimed(q,m,k)
                if a!=b:raise AssertionError((q,m,k,len(a),len(b),list(a-b)[:3],list(b-a)[:3]))
                checks+=1
                if m==4 and k==2:counts.append((q,len(a)))
    print('PASS direct positional-mask versus lifted-phase languages')
    print('parameter_cases',checks)
    print('m4_k2_counts',counts)
if __name__=='__main__':main()
