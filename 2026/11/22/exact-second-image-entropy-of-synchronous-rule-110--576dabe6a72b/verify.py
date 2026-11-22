"""Exact spatial-image entropy verification for two synchronous Rule-110 updates.

Run: python3 verify.py ; requires Python 3 and SymPy 1.14 or compatible.
Only integer/rational arithmetic decides the stated theorem.
"""
from collections import deque
from pathlib import Path
import json
import sympy as sy

X=sy.Symbol('x')
P17=(X**17-5*X**16+10*X**15-10*X**14+X**13+14*X**12
     -23*X**11+17*X**10+X**9-16*X**8+18*X**7-8*X**6
     -3*X**5+6*X**4-4*X**3+X-1)
P4=X**4-2*X**3+X**2-X-1

def local110(a,b,c):
    return (110 >> (4*a+2*b+c))&1

def composite_2(w):
    b=[(w >> (4-j))&1 for j in range(5)]
    return local110(local110(*b[:3]),local110(*b[1:4]),local110(*b[2:]))

def matrices(t):
    assert t in (1,2)
    size=1<<(2*t)
    # source state is an input word of length 2*t
    edges=[[0,0] for _ in range(size)]
    for w in range(2*size):
        label=(local110((w>>2)&1,(w>>1)&1,w&1)
               if t==1 else composite_2(w))
        edges[w>>1][label] |= 1<<(w&(size-1))
    full=(1<<size)-1
    states=[full]; ids={full:0}; transitions=[]
    # Expanding states in insertion order is a complete breadth-first closure.
    for S in states:
        row=[]
        for label in (0,1):
            target=0
            for i in range(size):
                if (S>>i)&1:target |= edges[i][label]
            if target and target not in ids:
                ids[target]=len(states);states.append(target)
            row.append(ids[target] if target else -1)
        transitions.append(row)
    # Every nonempty subset is accepting. Refine future-language equivalence
    # using the dead state -1 as a permanently nonaccepting sink.
    classes=[0]*len(states)
    while True:
        sig=[tuple(-1 if j<0 else classes[j] for j in row)
             for row in transitions]
        rank={s:i for i,s in enumerate(sorted(set(sig)))}
        new=[rank[s] for s in sig]
        if new==classes:break
        classes=new
    num=len(set(classes));A=sy.zeros(num)
    for c in range(num):
        representative=classes.index(c)
        for target in transitions[representative]:
            if target>=0:A[c,classes[target]]+=1
    # Every class has a representative, same-class transition signatures agree.
    for i,row in enumerate(transitions):
        actual=[-1 if j<0 else classes[j] for j in row]
        sample=transitions[classes.index(classes[i])]
        expected=[-1 if j<0 else classes[j] for j in sample]
        assert actual==expected
    return states,transitions,classes,A

def word_counts(A,start,nmax):
    v=sy.zeros(A.rows,1)
    v[start]=1
    out=[1]
    for _ in range(nmax):
        v=A.T*v
        out.append(int(sum(v)))
    return out

def brute_count(t,n):
    assert t in (1,2)
    outcomes=set()
    mask=(1<<(2*t+1))-1
    for block in range(1<<(n+2*t)):
        result=0
        for j in range(n):
            w=(block>>(n-j-1))&mask
            bit=(local110((w>>2)&1,(w>>1)&1,w&1)
                 if t==1 else composite_2(w))
            result=(result<<1)|bit
        outcomes.add(result)
    return len(outcomes)

def strongly_connected(A):
    vertices=range(A.rows)
    def reach(start):
        seen={start};queue=deque([start])
        while queue:
            i=queue.popleft()
            for j in vertices:
                if A[i,j] and j not in seen:
                    seen.add(j);queue.append(j)
        return seen
    return all(len(reach(k))==A.rows for k in vertices)

def cw_bracket(A,lower,upper,steps):
    # Collatz-Wielandt on the strictly positive integer vector A^steps 1.
    v=sy.ones(A.rows,1)
    for _ in range(steps):v=A*v
    w=A*v
    assert all(v[i]>0 for i in range(A.rows))
    assert all(w[i]*lower.q > lower.p*v[i] for i in range(A.rows))
    assert all(w[i]*upper.q < upper.p*v[i] for i in range(A.rows))
    return min(sy.Rational(w[i],v[i]) for i in range(A.rows)),max(sy.Rational(w[i],v[i]) for i in range(A.rows))

def run():
    results={}
    table=json.loads(Path(__file__).with_name("transition_table.json").read_text(encoding="utf-8"))
    for t in (1,2):
        states,transitions,classes,A=matrices(t)
        exp=(7,5) if t==1 else (41,20)
        assert (len(states),A.rows)==exp
        from_file=table[str(t)]
        assert from_file["start_class"]==classes[0]
        assert from_file["states"]==len(states) and from_file["classes"]==A.rows
        assert from_file["adjacency_matrix"]==[[int(A[i,j]) for j in range(A.cols)] for i in range(A.rows)]
        for c,entry in enumerate(from_file["transitions"]):
            rep=transitions[classes.index(c)]
            assert entry=={"state":c,"on_0":(-1 if rep[0]<0 else classes[rep[0]]),"on_1":(-1 if rep[1]<0 else classes[rep[1]])}
        assert strongly_connected(A)
        assert any(A[i,i]>0 for i in range(A.rows))
        assert sy.expand(A.charpoly(X).as_expr() - ((X-1)*P4 if t==1 else X**2*(X-1)*P17))==0
        counts=word_counts(A,classes[0],21)
        for n in range(1,11):
            assert counts[n]==brute_count(t,n),(t,n,counts[n])
        lo,hi=((sy.Rational(189717,100000),sy.Rational(189719,100000))
               if t==1 else (sy.Rational(185911,100000),sy.Rational(185912,100000)))
        a,b=cw_bracket(A,lo,hi,60)
        assert sy.polys.polytools.count_roots(A.charpoly(X).as_expr(),lo,hi)==1
        assert sy.polys.polytools.count_roots(A.charpoly(X).as_expr(),hi,sy.oo)==0
        results[t]=(counts,A.rows,len(states),lo,hi)
    c1,_,_,_,_=results[1];c2,_,_,_,_=results[2]
    assert c1[:10]==c2[:10]
    assert (c1[10],c2[10])==(769,768)
    assert c2[:18] == [1,2,4,8,16,31,59,112,213,405,768,1451,2732,5129,9608,17970,33572,62666]
    print('VERIFY_OK: exact state closure, minimization, characteristic polynomial,')
    print('strong connectivity, primitivity, rational Perron brackets, Sturm tests,')
    print('and independent direct input-block enumeration through length ten.')
    print('t=1: 7 reachable subsets, 5 minimized states; root in (1.89717,1.89719)')
    print('t=2: 41 reachable subsets, 20 minimized states; root in (1.85911,1.85912)')
    print('first image-language difference at word length 10: 769 versus 768')

if __name__=='__main__':run()
