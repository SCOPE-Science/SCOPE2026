"""Exact finite-quotient certificate for three-state excitable dynamics on Dutch windmills.

Run: python3 verify_friendship.py
Writes: state_certificate.csv (in the same directory as the script).
Uses only the Python 3 standard library.
"""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import csv
import hashlib

PAIRS = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
WEIGHTS = [1,2,2,1,2,1]
assert sum(WEIGHTS)==9

def advance(z, fires):
    if z == 1: return 2
    if z == 2: return 0
    return int(bool(fires))

def pair_advance(pair, hub):
    a,b=pair
    return (advance(a,hub==1 or b==1), advance(b,hub==1 or a==1))

def trans(s):
    hub,mask=s
    h2=advance(hub, any(1 in PAIRS[i] for i in range(6) if (mask>>i)&1))
    sm2=0
    for i in range(6):
        if (mask>>i)&1:
            newpair=tuple(sorted(pair_advance(PAIRS[i],hub)))
            sm2|=1<<PAIRS.index(newpair)
    return h2,sm2

def itinerary(s):
    seen={};seq=[]
    while s not in seen:
        seen[s]=len(seq);seq.append(s);s=trans(s)
        assert len(seq)<=189
    return seen[s],len(seq)-seen[s],seq

def check_lifted_recurrence(s,t,p,seq):
    # The quotient forgets the order of the two vertices in each pair.
    # Verify that the ordered two-vertex lift is genuinely p-periodic
    # once the quotient enters its period (no hidden swaps).
    initial=seq[t]
    for i in range(6):
        if not ((initial[1]>>i)&1): continue
        a,b=PAIRS[i]
        for j in range(p):
            a,b=pair_advance((a,b),seq[t+j][0])
        if (a,b)!=PAIRS[i]:return False
    return True

def coeff_onto(mask):
    # Every petal is a LABELLED ordered pair, and the six symmetry types
    # have weights 1,2,2,1,2,1. Möbius inversion counts exact support.
    A=[i for i in range(6) if mask>>i&1]
    out=Counter()
    for z in range(len(A)+1):
        for subset in combinations(A,z):
            k=sum(WEIGHTS[i] for i in subset)
            out[k]+=(-1)**(len(A)-z)
    return out

EXPECTED = {
    (0,1): {1:1},
    (0,3): {1:-3,3:3},
    (1,1): {1:-1,4:2},
    (1,3): {1:1,3:-1,4:-1,6:1},
    (2,1): {7:1},
    (2,3): {1:1,3:-1,7:-1,9:1},
    (3,1): {3:1,4:-1,7:1},
    (3,3): {1:1,3:-1,7:-1,9:1},
    (4,1): {3:-1,4:-1,7:1},
    (4,3): {4:1,6:-1,7:-1,9:1},
}

def run():
    totals=Counter();polys=defaultdict(Counter);records=[]
    for hub in range(3):
        for mask in range(1,64):
            state=(hub,mask)
            t,p,path=itinerary(state)
            assert p in (1,3) and t<=4
            assert check_lifted_recurrence(state,t,p,path), (state,t,p)
            totals[t,p]+=1
            for e,v in coeff_onto(mask).items():polys[t,p][e]+=v
            records.append((hub,mask,t,p,*trans(state)))
    assert len(records)==189
    assert set(polys)==set(EXPECTED)
    for key, poly in polys.items():
        assert {i:v for i,v in poly.items() if v and i}==EXPECTED[key],(key,poly)
    assert totals == Counter({(0,1):1,(0,3):6,(1,1):13,(1,3):6,
                              (2,1):31,(2,3):30,(3,1):27,(3,3):30,
                              (4,1):21,(4,3):24})
    # Periodic configurations at the signature level are exactly the
    # ones found at t=0; same ordered-lift periods hold by the test above.
    assert sum(v for (t,p),v in totals.items() if t==0)==7
    out=Path(__file__).with_name('state_certificate.csv')
    with out.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f,lineterminator='\n')
        w.writerow(['hub','mask','entry_time','least_period','next_hub','next_mask'])
        w.writerows(records)
    data=out.read_bytes()
    print('STATE_CERTIFICATE 189',len(data),hashlib.sha256(data).hexdigest())
    print('SIGNATURE_CLASSES',dict(sorted(totals.items())))
    for (t,p),coeff in sorted(EXPECTED.items()):
        print('COEFF',(t,p),' '.join(f'{k}:{v:+d}' for k,v in sorted(coeff.items())))
    for r in range(1,9):
        n={key:sum(v*k**r for k,v in c.items()) for key,c in EXPECTED.items()}
        assert sum(n.values())==3*9**r
        assert sum(v for (t,p),v in n.items() if p==1)==3*7**r
        assert sum(v for (t,p),v in n.items() if p==3)==3*(9**r-7**r)
        assert all(v>=0 for v in n.values())
        print('PARAMETER',r,'t4_1',n[4,1],'t4_3',n[4,3])
    print('PROOF_CHECK_OK')

if __name__=='__main__':run()
