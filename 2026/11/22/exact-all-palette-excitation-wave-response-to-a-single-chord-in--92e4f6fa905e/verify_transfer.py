"""Independent path transfer count, without using the closed-form path formula.

Run: python3 verify_transfer.py
"""
from collections import defaultdict
from verify_bruteforce import predicted

def path_table(k, L):
    dp=defaultdict(int)
    for e in range(k):
        dp[(e,e,int(e==1))]+=1
    for _ in range(1,L):
        ndp=defaultdict(int)
        for (r,prev,f),v in dp.items():
            for e in range(k):
                if prev==k-1 or e==1:
                    ndp[((r+e)%k,e,f)]+=v
        dp=ndp
    out=defaultdict(int)
    for (r,prev,f),v in dp.items():
        out[(r,f,int(prev==k-1))]+=v
    return out

def transfer_count(k,a,b,tab):
    total=0
    for (d,ua,va),c in tab[a].items():
        for (dd,ub,vb),cc in tab[b].items():
            if d!=dd: continue
            if (ua or ub or d==1) and (va or vb or d==k-1): total+=c*cc
    return k*total

def main():
    tests=0
    for k in range(3,9):
        tab={L:path_table(k,L) for L in range(2,61)}
        for n in range(4,62):
            for a in range(2,n-1):
                b=n-a
                if b<2 or a>60 or b>60:continue
                direct=transfer_count(k,a,b,tab)
                claimed=predicted(k,n,a)
                assert direct==claimed,(k,n,a,direct,claimed)
                tests+=1
    print('PASS independent endpoint-transfer counting: %d (k,n,a) cases'%tests)
    print('k=4, n=10, chord length 3: %d primitive four-orbits'%(predicted(4,10,3)//4))

if __name__=='__main__':main()
