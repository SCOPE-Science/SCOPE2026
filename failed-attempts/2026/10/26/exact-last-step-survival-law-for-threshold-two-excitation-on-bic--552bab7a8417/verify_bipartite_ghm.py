"""Self-contained finite certificate for threshold-two three-state excitable dynamics
on complete bipartite graphs. Only Python standard library is required.
Finite capped-signature exhaustion is logically complete for ALL part sizes
because threshold comparisons require only counts truncated at two.
"""
from itertools import product
from collections import Counter
from math import factorial, comb

THRESHOLD=2

def three_class_step(state, counts):
    left, right = state
    excited_left = sum(m for m,s in zip(counts[0], left) if s==1)
    excited_right = sum(m for m,s in zip(counts[1], right) if s==1)
    def move(s,trigger):
        return 1 if s==0 and trigger else (0 if s==0 else (s+1)%3)
    return (tuple(move(s,excited_right>=THRESHOLD) if counts[0][i] else -1
                  for i,s in enumerate(left)),
            tuple(move(s,excited_left>=THRESHOLD) if counts[1][i] else -1
                  for i,s in enumerate(right)))

def signature_orbit(counts):
    state=(tuple(i if counts[0][i] else -1 for i in range(3)),
           tuple(i if counts[1][i] else -1 for i in range(3)))
    seen={}
    while state not in seen:
        seen[state]=len(seen)
        state=three_class_step(state,counts)
        assert len(seen)<=729  # at most 3^6 distinguishable active color labels
    return seen[state],len(seen)-seen[state]

def full_step(state,a):
    left,right=state[:a],state[a:]
    le=left.count(1);re=right.count(1)
    return tuple((1 if re>=2 else 0) if s==0 else (s+1)%3 for s in left) + \
           tuple((1 if le>=2 else 0) if s==0 else (s+1)%3 for s in right)

def full_orbit(state,a):
    seen={}
    while state not in seen:
        seen[state]=len(seen)
        state=full_step(state,a)
        assert len(seen)<=30
    return seen[state],len(seen)-seen[state]

def H(n):
    return sum(factorial(n)//(factorial(x)*factorial(y)*factorial(n-x-y))
               for x in range(2,n+1) for y in range(2,n-x+1) if n-x-y>=2)

def J(n):
    return sum(comb(n,k) for k in range(2,n-1))

def P(n):
    # >=2 excited vertices and >=2 nonexcited vertices, the latter 0 or 2
    return sum(comb(n,e)*2**(n-e) for e in range(2,n-1))

def Q(n):
    # exactly one nonrest vertex of a prescribed color, rest >=2
    return n if n>=3 else 0

def is_thin(c):
    return c[0]==2 and ((c[1],c[2])==(1,0) or (c[1],c[2])==(0,1))

def is_fat(c):
    return c[1]==2 and c[0]+c[2]>=2

def sharp_T(a,b):
    lo,hi=sorted((a,b))
    if lo==hi==1:return 2
    if lo==1:return 3
    if lo==hi==2:return 3
    if lo==2:return 4
    if lo==hi==3:return 4
    return 5

def classify_signatures():
    class_counts=Counter();recurrent=Counter();max_by_size={};signature_count=0
    pre5_pairs=set()
    for vals in product(range(3),repeat=6):
        a=vals[:3];b=vals[3:]
        if not any(a) or not any(b):continue
        signature_count+=1
        t,p=signature_orbit((a,b))
        assert t<=5 and p in (1,3,4)
        class_counts[(t,p)]+=1
        if t==0:recurrent[p]+=1
        if t==5:pre5_pairs.add((sum(a),sum(b)))
        assert (t==5)==((is_thin(a) and is_fat(b)) or (is_fat(a) and is_thin(b))), (a,b,t,p)
        # For 1..6, an n-point side can realize a capped pattern either
        # by its exactly determined counts or by adding to a size-2 class.
        for A in range(1,7):
            if A<sum(a) or (A>sum(a) and 2 not in a):continue
            for B in range(1,7):
                if B<sum(b) or (B>sum(b) and 2 not in b):continue
                max_by_size[(A,B)]=max(max_by_size.get((A,B),0),t)
        if t==0 and p==3: assert a==(2,2,2) and b==(2,2,2)
        if t==0 and p==4: assert (a,b) in [((2,0,2),(2,2,0)),((2,2,0),(2,0,2))]
        if t==0 and p==1: assert all(x==0 for i,side in enumerate((a,b)) for x,c in enumerate(side) if c and x!=0)
    assert signature_count==676
    assert recurrent=={1:4,3:1,4:2},recurrent
    assert class_counts=={(0,1):4,(0,3):1,(0,4):2,(1,1):60,(1,4):10,
                          (2,1):324,(2,4):30,(3,1):160,(3,4):8,
                          (4,1):51,(4,4):2,(5,1):24},class_counts
    for (a,b),v in max_by_size.items():assert v==sharp_T(a,b),(a,b,v,sharp_T(a,b))
    assert (3,4) in pre5_pairs and (4,3) in pre5_pairs
    print('capped_type_signatures',signature_count)
    print('periodic_capped_classes',dict(sorted(recurrent.items())))
    print('transient_period_signature_table',dict(sorted(class_counts.items())))
    print('sharp_depth_pairs_1_to_6',len(max_by_size))
    print('uniform_depth5_structural_condition_verified',signature_count)

def independently_enumerate():
    tested=0
    for a,b in [(1,1),(2,3),(3,4),(4,4),(4,5),(6,6)]:
        c=Counter()
        for state in product(range(3),repeat=a+b):
            t,p=full_orbit(state,a)
            c[(t,p)]+=1
        assert sum(c.values())==3**(a+b)
        assert max(t for t,p in c)==sharp_T(a,b)
        for per,count in [(1,1),(3,H(a)*H(b)),(4,2*J(a)*J(b))]:
            assert c[(0,per)]==count,(a,b,per,c[(0,per)],count)
        assert all(p in (1,3,4) for _,p in c)
        assert c[(5,1)]==2*(P(a)*Q(b)+Q(a)*P(b)), (a,b,c[(5,1)])
        tested+=sum(c.values())
        print('brute_graph',a,b,'states',3**(a+b),'recurrent_counts',[(p,c[(0,p)]) for p in (1,3,4)],'depth5_count',c[(5,1)],'maxT',sharp_T(a,b))
    print('independently_tested_vertex_configurations',tested)

if __name__=='__main__':
    classify_signatures()
    independently_enumerate()
    print('BIPARTITE_GHM_VERIFY_OK')
