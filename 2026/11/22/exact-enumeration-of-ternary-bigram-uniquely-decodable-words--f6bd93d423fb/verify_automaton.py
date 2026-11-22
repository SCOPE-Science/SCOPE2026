"""Exact enumerator for ternary words determined by their adjacent ordered pairs.

Public, standalone stdlib code. Prints automaton counts and proves an all-length
rational series by exact integer vectors, not by extrapolation.
"""
from collections import defaultdict,deque
from itertools import product

Q=3
TRIPLES=tuple((x,a,b) for x in range(Q) for a in range(Q) if a!=x for b in range(Q) if b!=x)

# For (x,a,b): I recognizes a x [not a]* b; J recognizes a [not x]* b.
# An underlying letter pattern may be found anywhere in the word.
def step(state,c):
    new=[]
    for (x,a,b),(i,j) in zip(TRIPLES,state):
        if i == 3:
            ni=3
        elif i == 2 and c == b:
            ni=3
        elif c == a:
            ni=1
        elif i == 1 and c == x:
            ni=2
        elif i == 2:
            ni=2
        else:
            ni=0
        if j == 2:
            nj=2
        elif c == x:
            nj=0
        elif j == 1 and c == b:
            nj=2
        elif c == a or j == 1:
            nj=1
        else:
            nj=0
        if ni == 3 and nj == 2:
            return None
        new.append((ni,nj))
    return tuple(new)

START=((0,0),)*len(TRIPLES)
STATES=[START]
INDEX={START:0}
TRANS=[]
for state in STATES:
    row=[]
    for c in range(Q):
        nxt=step(state,c)
        if nxt is None:
            row.append(-1)
        else:
            if nxt not in INDEX:
                INDEX[nxt]=len(STATES)
                STATES.append(nxt)
            row.append(INDEX[nxt])
    TRANS.append(tuple(row))

# Let M be the integer transition adjacency, with M_{ij} counting symbols
# leading from state i to state j. v_n=M^n 1 counts admissible continuations.
def forward(v):
    return [sum(v[j] for j in row if j>=0) for row in TRANS]

vec=[1]*len(STATES)
vs=[]
for n in range(300):
    vs.append(vec)
    vec=forward(vec)

# Target third finite difference is zero for every n>=6, as a *vector*.
def difference(vs,n):
    return [vs[n+3][i]-3*vs[n+2][i]+3*vs[n+1][i]-vs[n][i] for i in range(len(STATES))]
K=min(k for k in range(150) if not any(difference(vs,k)))
print('TRIPLES:',len(TRIPLES))
print('REACHABLE_DFA_STATES:',len(STATES))
print('FIRST_15_COUNTS:',[vs[n][0] for n in range(15)])
print('SMALLEST_UNIFORM_VECTOR_THIRD_DIFF_VANISH:',K)
print('UNIFORM_DIFF_AT_6_ZERO:',not any(difference(vs,6)))
print('UNIFORM_DIFF_AT_12_ZERO:',not any(difference(vs,12)))
print('INIT_CERTIFIED:',vs[0][0:1],vs[1][0:1],vs[2][0:1],vs[3][0:1],vs[4][0:1],vs[5][0:1],vs[6][0:1],vs[7][0:1],vs[8][0:1])

# IMPORTANT: Vanishing of the third difference at one n is insufficient
# unless the vector identity is propagated via commute: M(M-I)^3=(M-I)^3M.
assert not any(difference(vs,K))
assert [vs[i][0] for i in range(13)]==[1,3,9,27,69,135,207,273,345,423,507,597,693]
# Direct independent exhaustive profile count through length ten.
from collections import Counter
for n in range(1,11):
    counts=Counter()
    for w in product(range(Q),repeat=n):
        profile=[0]*(Q*Q)
        for x,y in zip(w,w[1:]):profile[Q*x+y]+=1
        counts[(w[0],w[-1],*profile)]+=1
    brute=sum(c==1 for c in counts.values())
    assert brute==vs[n][0],(n,brute,vs[n][0])
print('BRUTE_PROFILE_CROSSCHECK_N_1_TO_10: PASS')
