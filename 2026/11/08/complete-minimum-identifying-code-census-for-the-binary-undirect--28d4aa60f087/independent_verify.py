"""Independent direct-neighborhood Boolean branching verifier (stdlib only)."""
from collections import Counter
from itertools import combinations
from pathlib import Path

def exact_sets(n, k):
    words=[format(i,'0%db'%n) for i in range(1<<n)]
    N=len(words)
    # Reconstruct the underlying graph from literal overlap equalities.
    B=[]
    for i,u in enumerate(words):
        neighbors={i}
        for j,v in enumerate(words):
            if u[1:]==v[:-1] or v[1:]==u[:-1]:neighbors.add(j)
        B.append(sum(1<<j for j in neighbors))
    clauses=set(B)
    for i,j in combinations(range(N),2):
        d=B[i]^B[j]
        assert d!=0
        clauses.add(d)
    clauses=sorted(clauses,key=int.bit_count)
    answers=set()
    def search(selected, excluded):
        chosen=selected.bit_count()
        if chosen>k or chosen+N-(selected|excluded).bit_count()<k:return
        undecided=[]
        for c in clauses:
            if selected&c:continue
            residual=c&~excluded
            if not residual:return
            undecided.append(residual)
        if not undecided:
            if chosen==k:answers.add(selected)
            else:
                remaining=[i for i in range(N) if not (selected|excluded)&(1<<i)]
                for supplement in combinations(remaining,k-chosen):
                    answers.add(selected|sum(1<<i for i in supplement))
            return
        if chosen==k:return
        clause=min(undecided,key=int.bit_count)
        frequency=Counter(i for c in undecided for i in range(N) if c&(1<<i))
        x=max((i for i in range(N) if clause&(1<<i)),key=lambda j:frequency[j])
        bit=1<<x
        search(selected|bit, excluded)
        search(selected,excluded|bit)
    search(0,0)
    return answers,B

def image(mask,reverse=False,complement=False):
    out=0
    for i in range(32):
        if mask>>i&1:
            j=i^31 if complement else i
            if reverse:j=int(format(j,'05b')[::-1],2)
            out|=1<<j
    return out

def verify():
    expected={int(line) for line in Path(__file__).with_name('optima_58.txt').read_text().splitlines()}
    assert len(expected)==58
    no11,_=exact_sets(5,11)
    assert no11==set(), '11-vertex identifying code exists'
    got,B=exact_sets(5,12)
    assert got==expected,(len(got),len(expected),got^expected)
    assert len(B)==32 and len({x for x in B})==32
    # Independently verify every raw (unreduced) identification signature.
    for C in got:
        assert C.bit_count()==12
        observations=[b&C for b in B]
        assert all(observations) and len(set(observations))==32
    classes=[];visited=set()
    for C in sorted(got):
        if C in visited:continue
        orbit={image(C,a,b) for a in (False,True) for b in (False,True)}
        assert orbit<=got
        visited|=orbit
        classes.append(orbit)
    assert Counter(map(len,classes))=={4:13,2:3}
    orbit_file=Path(__file__).with_name('orbits_16.tsv').read_text().strip().splitlines()
    assert orbit_file[0]=='representative_mask_decimal\torbit_size'
    pairs={(int(min(orbit)),len(orbit)) for orbit in classes}
    assert pairs=={tuple(map(int,line.split('\t'))) for line in orbit_file[1:]}
    assert sum(image(C,complement=True)==C for C in got)==6
    assert sum(image(C,reverse=True)==C for C in got)==0
    assert sum(image(C,reverse=True,complement=True)==C for C in got)==0
    absent=[i for i in range(32) if not any(C>>i&1 for C in got)]
    assert absent==[0,4,10,14,17,21,27,31],absent
    small,_=exact_sets(4,6)
    assert len(small)==2
    print('INDEPENDENT_EXACT_11=0')
    print('INDEPENDENT_EXACT_12=58')
    print('SYMMETRY_ORBITS=13x4+3x2')
    print('NEVER_SELECTED_8=00000,00100,01010,01110,10001,10101,11011,11111')
    print('INDEPENDENT_COMPLETE_OK')
if __name__=='__main__':verify()
