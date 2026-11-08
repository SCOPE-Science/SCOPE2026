"""Standalone state-complexity checks for disjoint binary Coxeter factors."""
from collections import deque
from itertools import product

# None represents infinite dihedral I_2(infty).
def belongs(word, exponents):
    if not word: return False
    if word != word[::-1]: return False
    owner = word[0] // 2
    if any(x // 2 != owner for x in word): return False
    if any(x == y for x,y in zip(word,word[1:])): return False
    bound = exponents[owner]
    return bound is None or len(word) <= bound

def naive_dfa(exponents):
    """Explicit formal-language automaton with finite-prefix states and 2-cycle for each infinity factor."""
    f = len(exponents); sigma = tuple(range(2*f))
    states = [('start',), ('dead',)]
    for i, p in enumerate(exponents):
        if p is None:
            states += [('inf',i,b,k) for b in (0,1) for k in (1,2)]
        else:
            states += [('fin',i,b,k) for b in (0,1) for k in range(1,p+1)]
    idx = {st:j for j,st in enumerate(states)}
    T=[]; F=[]
    for st in states:
        typ=st[0]
        F.append(typ in ('fin','inf') and st[-1]%2==1)
        line=[]
        for c in sigma:
            if typ=='start': ns=('inf',c//2,c%2,1) if exponents[c//2] is None else ('fin',c//2,c%2,1)
            elif typ=='dead': ns=('dead',)
            else:
                _,i,b,k=st
                if c//2 != i or c%2 != (b ^ (k%2)):
                    ns=('dead',)
                elif typ=='inf': ns=('inf',i,b,3-k)
                elif k == exponents[i]: ns=('dead',)
                else: ns=('fin',i,b,k+1)
            line.append(idx[ns])
        T.append(tuple(line))
    return T,F

def minimize(T,F):
    # Partition refinement is independent of the analytical Myhill--Nerode proof.
    blocks=[{i for i,x in enumerate(F) if x},{i for i,x in enumerate(F) if not x}]
    blocks=[s for s in blocks if s]
    while True:
        mp={x:j for j,b in enumerate(blocks) for x in b}
        nxt=[]
        for block in blocks:
            by={}
            for x in block:
                signature=tuple(mp[y] for y in T[x])
                by.setdefault(signature,set()).add(x)
            nxt.extend(by.values())
        if len(nxt)==len(blocks): return len(blocks)
        blocks=nxt

def formula(exponents):
    infinite=sum(p is None for p in exponents)
    finite=[p for p in exponents if p is not None]
    return 2 + 4*infinite + 2*sum((p if p%2 else p-1)-1 for p in finite) + int(bool(finite))

def run():
    ncases=0; words=0
    for f in range(1,6):
        for es in product((2,3,4,5,None),repeat=f):
            if f==5 and es.count(None)==0 and max(es)>=4: continue
            T,F=naive_dfa(es)
            got=minimize(T,F); expected=formula(es)
            assert got==expected,(es,got,expected)
            ncases+=1
            if ncases<=200 or (ncases%37==0):
                alphabet=range(2*f)
                for n in range(0,5):
                    for w in product(alphabet,repeat=n):
                        state=0
                        for c in w: state=T[state][c]
                        assert F[state]==belongs(w,es),(es,w)
                        words+=1
    # The four-state diagram in Bapat, Proposition 4.1 (p. 5), has the
    # indicated transitions q0--s-->q1--t-->q0--t-->q2 (accepting).
    # Thus it accepts stt, whose consecutive t letters make it nonreduced.
    pictured = {'0':{'s':'1','t':'2'},
                '1':{'s':'3','t':'0'},
                '2':{'s':'0','t':'3'},
                '3':{'s':'3','t':'3'}}
    state='0'
    for c in 'stt': state=pictured[state][c]
    assert state in ('1','2')
    assert not belongs((0,1,1),(None,))
    assert minimize(*naive_dfa((None,)))==6
    assert minimize(*naive_dfa((2,)))==3
    assert minimize(*naive_dfa((3,)))==7
    print({'parameter_tuples':ncases,'direct_word_checks':words,'minimized_max_states':max(formula(es) for es in product((2,3,4,5,None),repeat=4))})
if __name__ == '__main__': run()
