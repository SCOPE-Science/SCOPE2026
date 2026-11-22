"""Exact rational checks of phase-cycle firing rates for periodic opportunity clocks."""
from fractions import Fraction as Q
from itertools import combinations

def phase_cycle(gaps,s,start=0):
    assert len(gaps)==3 and sum(gaps)==1 and 0<s<1
    phases=[Q(0),gaps[0],gaps[0]+gaps[1]]
    transitions=[]
    for p in phases:
        options=[((q-p)%1 or Q(1),j) for j,q in enumerate(phases)]
        transitions.append(min((d,j) for d,j in options if d>=s))
    path=[]; seen={}; at=start
    while at not in seen:
        seen[at]=len(path);path.append(at);at=transitions[at][1]
    cycle=path[seen[at]:]
    duration=sum((transitions[i][0] for i in cycle),Q(0))
    return Q(len(cycle),1)/duration,tuple(transitions[i][0] for i in cycle),tuple(cycle)

def formula(g,s):
    a,b,c=sorted(g)
    if s<=a:return Q(3)
    if c<Q(1,2):
        if s<=c:return Q(2)
        if s<=1-c:return Q(3,2)
        return Q(1)
    return Q(2) if s<=1-c else Q(1)

checks=0
for u in range(1,20):
 for v in range(1,20-u):
    w=20-u-v
    if w<1:continue
    gaps=[Q(u,20),Q(v,20),Q(w,20)]
    boundaries=sorted(set([(q-p)%1 or Q(1) for p in [Q(0),gaps[0],gaps[0]+gaps[1]] for q in [Q(0),gaps[0],gaps[0]+gaps[1]]]))
    cases=sorted(set([Q(1,1000)]+[x for x in boundaries if x<1]+[(x+y)/2 for x,y in zip([Q(0)]+boundaries[:-1],boundaries)]))
    for s in cases:
        if not (0<s<1):continue
        expected=formula(gaps,s)
        for start in range(3):
            got,_,_=phase_cycle(gaps,s,start)
            assert got==expected,(gaps,s,start,got,expected)
            checks+=1
print('general_exact_rational_checks',checks)

gaps=[Q(1,4),Q(5,12),Q(1,3)]
# phases 0,1/4,2/3; ordered gaps 1/4,5/12,1/3
intervals=[(Q(0),Q(1,4),Q(3),(Q(1,4),Q(5,12),Q(1,3))),
           (Q(1,4),Q(1,3),Q(2),(Q(2,3),Q(1,3))),
           (Q(1,3),Q(5,12),Q(2),(Q(5,12),Q(7,12))),
           (Q(5,12),Q(7,12),Q(3,2),(Q(2,3),Q(7,12),Q(3,4))),
           (Q(7,12),Q(1),Q(1),(Q(1),))]
for l,r,rate,isi in intervals:
 for s in [(l+r)/2,r] if r<1 else [(l+r)/2]:
    for i in range(3):
        got,seq,cyc=phase_cycle(gaps,s,i)
        assert got==rate,(l,r,s,i,got,rate)
        assert sorted(seq)==sorted(isi),(l,r,s,i,seq,isi)
        checks+=1
    m=sum(isi,Q(0))/len(isi)
    var=sum(((v-m)**2 for v in isi),Q(0))/len(isi)
    print('regime',str(l),str(r),'rate',str(rate),'isi',list(map(str,isi)),'variance',str(var))
print('all_exact_checks',checks)
