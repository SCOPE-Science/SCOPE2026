"""Independent finite-field and exact packing checks for the F7 permutation/deletion code."""
from itertools import combinations
Q=7
FIELD=set(range(Q))
GROUP=[(a,b) for a in range(1,Q) for b in range(Q)]
TRIPLES=set(combinations(range(Q),3))

def map_set(T,a,b):
    return tuple(sorted((a*x+b)%Q for x in T))

def orbit(T):
    return {map_set(T,a,b) for a,b in GROUP}

def incidence(T):
    return {frozenset((x,y)) for x,y in combinations(T,2)}

def packing_families(V):
    V=sorted(V)
    # Two triples may coexist if they share at most one element.
    conflicts=[sum(1<<j for j,W in enumerate(V) if i!=j and len(set(T)&set(W))>=2)
               for i,T in enumerate(V)]
    best=0
    sols=[]
    def visit(candidates,selected):
        nonlocal best,sols
        if not candidates:
            if len(selected)>best:
                best=len(selected);sols=[tuple(V[i] for i in selected)]
            elif len(selected)==best:
                sols.append(tuple(V[i] for i in selected))
            return
        if len(selected)+candidates.bit_count()<best:
            return
        v=(candidates&-candidates).bit_length()-1
        visit(candidates&~(1<<v)&~conflicts[v],selected+(v,))
        visit(candidates&~(1<<v),selected)
    visit((1<<len(V))-1,())
    return best,sols

def source_reads(S):
    # Distinct output words, after a uniformly arbitrary coordinate permutation
    # followed by exactly one deletion. Sets are canonical for distinct symbols.
    S=sorted(S)
    messages={}
    for a in range(Q):
        for b in range(Q):
            word=tuple((a+b*x)%Q for x in S)
            outputs={tuple(sorted(word[:i]+word[i+1:])) for i in range(4)}
            messages[(a,b)]=(word,outputs)
    return messages

def test(T0,expected_orbit,expected_best,expected_count,expected_multiplicity):
    Ts=orbit(T0)
    assert len(Ts)==expected_orbit
    S=tuple(sorted(FIELD-set(T0)))
    reads=source_reads(S)
    const={a for a,b in reads if b==0}
    assert len(const)==Q
    # Nonconstant message-support multiplicity agrees with the stabilizer size.
    fibers={}
    for a in range(Q):
        for b in range(1,Q):
            support=frozenset(reads[(a,b)][0])
            fibers.setdefault(support,[]).append((a,b))
    assert len(fibers)==expected_orbit
    assert all(len(f)==expected_multiplicity for f in fibers.values())
    assert {tuple(sorted(FIELD-set(SP))) for SP in fibers}==Ts
    assert all(all(len(y)==3 and len(set(y))==3 for y in reads[m][1]) for f in fibers.values() for m in f)
    best,sols=packing_families(Ts)
    assert best==expected_best and len(sols)==expected_count, (best,len(sols))
    # Every extremal triple packing maps to a realizable correcting code:
    for solution in sols:
        chosen=[next(iter(fibers[frozenset(FIELD-set(t))])) for t in solution]
        selected=[(a,0) for a in range(Q)]+chosen
        read_sets=[reads[m][1] for m in selected]
        assert all(read_sets[i].isdisjoint(read_sets[j]) for i in range(len(selected)) for j in range(i+1,len(selected)))
    # Directly verify overlap equivalence for all ordered pairs of nonconstant source codewords.
    pairs=0
    for m,(_,r1) in reads.items():
        for m2,(_,r2) in reads.items():
            if m<m2:
                s1=frozenset(reads[m][0]);s2=frozenset(reads[m2][0])
                assert bool(r1&r2)==(s1==s2 if len(s1)<4 else len(s1&s2)>=3)
                pairs+=1
    print(f'T={T0} |orbit|={len(Ts)} support-fiber={expected_multiplicity} packing={best} maximal-packings={len(sols)} max-codes={len(sols)*expected_multiplicity**best} pairs={pairs}')
    return sols

def main():
    ap=orbit((0,1,2))
    neq=orbit((0,1,3))
    assert ap.isdisjoint(neq) and ap|neq==TRIPLES
    s1=test((0,1,2),21,6,14,2)
    s2=test((0,1,3),14,7,2,3)
    # Fine classification of six-AP-block extremizers by their three uncovered pairs.
    omissions=[]
    for pack in s1:
        used=set().union(*(incidence(b) for b in pack))
        missing={frozenset(p) for p in combinations(range(Q),2)}-used
        assert len(missing)==3
        points=set().union(*missing)
        assert len(points)==3
        assert {frozenset(p) for p in combinations(sorted(points),2)}==missing
        assert tuple(sorted(points)) in neq
        omissions.append(tuple(sorted(points)))
    assert len(set(omissions))==14
    # Two Fano systems partition the 14 non-AP triples.
    assert set(s2[0]).isdisjoint(s2[1])
    assert set(s2[0])|set(s2[1])==neq
    print('PASS: complete triple-orbit decomposition, all optimal packings, omission bijection, exact channel equivalence')
if __name__=='__main__': main()
