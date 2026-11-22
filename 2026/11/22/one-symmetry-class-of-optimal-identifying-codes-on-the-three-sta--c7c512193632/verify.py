"""Independent pure-Python exhaustive enumeration of identifying codes on cyclic 3-butterfly."""
from itertools import combinations
from collections import Counter

def main():
    r=3
    vertices=[(i,a) for i in range(r) for a in range(1<<r)]
    index={v:k for k,v in enumerate(vertices)}
    adj={v:{v} for v in vertices}
    for i in range(r):
        for a in range(1<<r):
            for b in (a,a ^ (1<<i)):
                x=(i,a); y=((i+1)%r,b)
                adj[x].add(y); adj[y].add(x)
    rows=[]
    for v in vertices:
        rows.append(frozenset(adj[v]))
    for i in range(len(vertices)):
        for j in range(i+1,len(vertices)):
            rows.append(frozenset(adj[vertices[i]]^adj[vertices[j]]))
    assert len(rows)==300 and all(rows)
    rows_masks=[sum(1<<index[v] for v in row) for row in rows]
    # Order mandatory constraints from most restrictive upwards.
    rows_masks=sorted(set(rows_masks),key=lambda m:(m.bit_count(),m))
    counts={}
    valid_codes=[]
    for k in range(10):
        total=0
        for combo in combinations(range(24),k):
            code=sum(1<<j for j in combo)
            if all(code&row for row in rows_masks):
                total+=1
                if k==9:valid_codes.append(code)
        counts[k]=total
    assert counts=={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:48},counts
    base=valid_codes[0]
    # The evident address translations and ring rotations/reflections.
    def rotated(a,k):
        return sum(1<<((t+k)%r) for t in range(r) if a&(1<<t))
    def reflected(a):
        return sum(1<<(r-1-t) for t in range(r) if a&(1<<t))
    orbit=set()
    for sh in range(r):
        for mask in range(1<<r):
            for refl in range(2):
                out=0
                for j,(i,a) in enumerate(vertices):
                    if not base>>j&1:continue
                    ni=((-i if refl else i)+sh)%r
                    na=rotated(reflected(a) if refl else a,sh)^mask
                    out|=1<<index[(ni,na)]
                orbit.add(out)
    assert len(orbit)==48 and orbit==set(valid_codes)
    from pathlib import Path
    saved={int(line,16) for line in Path('OPTIMA.txt').read_text(encoding='utf-8').splitlines() if line and not line.startswith('#')}
    assert saved==orbit, 'Listed optimizers differ from exact exhaustive census'
    profile=Counter(tuple(sum(1 for j in range(i*8,i*8+8) if code>>j&1) for i in range(3)) for code in valid_codes)
    print('VERIFY_OK k<=9',counts,'orbit_size',len(orbit),'level_profiles',sorted(profile.items()),'representative',[(i,format(a,'03b')) for j,(i,a) in enumerate(vertices) if base>>j&1])
if __name__=='__main__':main()
