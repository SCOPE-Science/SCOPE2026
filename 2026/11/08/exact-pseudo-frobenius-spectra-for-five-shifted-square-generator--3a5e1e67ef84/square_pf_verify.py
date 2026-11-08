#!/usr/bin/env python3
"""Independent exact-integer checks for the square-shift pseudo-Frobenius theorem."""
from heapq import heappop, heappush

D = (1, 4, 9, 16)
C = (0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3, 2, 3, 4)
DELTA = (0, 1, 1, 2, 1, 2, 2, 3, 2, 1, 2, 2, 3, 2, 3, 3)
OFFSETS = (
(1,2,4,9),
(1,2,3,5,10),
(1,3,4,6,11),
(1,2,4,5,7,12),
(1,3,5,6,8,13),
(1,2,4,6,7,9,14),
(1,3,7,8,10,15),
(1,2,4,8,9,11,16),
(1,3,9,12),
(1,2,4,10,13),
(1,2,3,5,11,14),
(1,3,4,6,12,15),
(1,2,4,5,7,13,16),
(1,3,6,8,14),
(1,2,4,7,9,15),
(1,3,8,16),
)

# Dynamic programming is only a diagnostic; the mathematical proof establishes
# periodicity by a finite base check and strong induction on the coin recursion.
L=[0]
for m in range(1,20002):
    L.append(1+min(L[m-d] for d in D if m>=d))
assert tuple(L[:16]) == C
assert tuple(L[16+i]-1 for i in range(16)) == DELTA
assert all(L[m+16]==L[m]+1 for m in range(16,20001-16))

# Certified 16-by-16 table from the exact modular comparison in the proof.
def theta(q,k):
    return (q-k)//16 + DELTA[(q-k)%16]
for q in range(16):
    got=tuple(k for k in range(1,17)
              if all(theta(q,k)>=theta(q,k-d) for d in D if d<k))
    assert got==OFFSETS[q], (q, got, OFFSETS[q])

assert [r for r in range(1,16) if all(L[r]>=L[r+d] for d in D)] == [7,15]

# Finite base-block certificate for the sharp cutoff a>=34.
# All failures outside the listed sets have a NON-WRAPPING witness,
# so they remain failures after adding any multiple of 16 to a.
for a in range(34,50):
    passes=[]
    for k in range(1,17):
        r=a-k
        nonwrap=all(L[r]>=L[r+d] for d in D if d<k)
        wrap=all(L[r]+1>=L[d-k] for d in D if d>=k)
        if nonwrap:assert wrap, (a,k)
        if nonwrap and wrap: passes.append(k)
    assert tuple(passes)==OFFSETS[a%16],(a,passes)


def apery(a):
    dist=[10**40]*a
    dist[0]=0
    h=[(0,0)]
    while h:
        wt,r=heappop(h)
        if wt!=dist[r]:continue
        for d in D:
            s=(r+d)%a
            nw=wt+a+d
            if nw<dist[s]:
                dist[s]=nw
                heappush(h,(nw,s))
    return dist

def predicted_pf(a):
    residues={7,15}|{a-k for k in OFFSETS[a%16]}
    return sorted(r+a*(L[r]-1) for r in residues)

def actual_pf(a,w):
    gens=(a,)+(tuple(a+d for d in D))
    out=[]
    for r in range(1,a):
        candidate=w[r]-a
        if all(candidate+g>=w[(candidate+g)%a] for g in gens):
            out.append(candidate)
    return sorted(out)

count=0
for a in list(range(34,513))+[640,768,1024,2048,4096]:
    w=apery(a)
    assert all(w[r] == r+a*L[r] for r in range(a)),a
    actual=actual_pf(a,w)
    predicted=predicted_pf(a)
    assert actual==predicted, (a,actual,predicted)
    assert len(predicted)==len(OFFSETS[a%16])+2
    count+=1

# Extra direct reachability and definition check in the semigroup, avoiding Apéry.
for a in (34,37,48,55,71,96,101):
    gens=(a,a+1,a+4,a+9,a+16)
    maxcheck=max(predicted_pf(a))+max(gens)+1
    hit=bytearray(maxcheck+1)
    hit[0]=1
    for n in range(maxcheck+1):
        if hit[n]:
            for g in gens:
                if n+g<=maxcheck:hit[n+g]=1
    calc=[n for n in range(max(predicted_pf(a))+1)
          if not hit[n] and all(hit[n+g] for g in gens)]
    assert sorted(calc)==predicted_pf(a),(a,calc)
print('VERIFY_OK')
print('coin_recurrence_range=0..20001')
print('all_modular_offset_cases=16*16; low_residues=1..15')
print('apery_and_pf_dijkstra_parameter_count='+str(count))
print('direct_gap_parameter_count=7')
assert 65 not in actual_pf(33,apery(33))
assert 65 in predicted_pf(33)
print('sharp_failure_a33_candidate=65; candidate_plus_generator=114_not_in_semigroup')
print('type_table='+str(tuple(2+len(r) for r in OFFSETS)))
