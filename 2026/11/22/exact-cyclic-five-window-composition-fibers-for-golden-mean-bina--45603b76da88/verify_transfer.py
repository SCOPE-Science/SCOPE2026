"""Independent eight-state 5-window de Bruijn transfer certificate."""
from collections import Counter, defaultdict
from verify_direct import gap_fibers

STATES=tuple(x for x in range(16) if not x&(x<<1))
assert len(STATES)==8
TRANS={a:[] for a in STATES}
for a in STATES:
    for bit in (0,1):
        if (a&1) and bit:continue
        v=((a<<1)&15)|bit
        # State's most significant bit is the first bit of the 5-window.
        t=(a<<1)|bit
        TRANS[a].append((v,(a>>3)&1,int(t.bit_count()==2),int(t.bit_count()==3)))


def transfers(maxn):
    current={(a,a,0,0,0):1 for a in STATES}
    for n in range(1,maxn+1):
        new=defaultdict(int)
        for (start,state,w,b,t),cnt in current.items():
            for dst,dw,db,dt in TRANS[state]:
                new[(start,dst,w+dw,b+db,t+dt)]+=cnt
        current=new
        if n>=5:
            res=Counter()
            for (start,state,w,b,t),cnt in current.items():
                if start==state:res[(w,b,t)]+=cnt
            yield n,res


def main():
    for n,dp in transfers(30):
        gap=gap_fibers(n)
        assert dp==gap,(n,len(dp),len(gap),(dp-gap).most_common(3),(gap-dp).most_common(3))
        print(n,len(dp),sum(dp.values()))
    print('PASS: all exact profile fibers through n=30 using independent 8-state walk')

if __name__=='__main__':main()
