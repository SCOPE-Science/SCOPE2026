#!/usr/bin/env python3
"""Self-contained certificate checker for short two-read deletion reconstruction codes.

Python 3 standard library only. Run: python3 verify.py certificates.json
"""
import sys, json, itertools, math

def deletion_outputs(w):
    return {w[:i]+w[i+1:] for i in range(len(w))}

def case(n, k, record):
    letters = '0123456789'[:k]
    words = {''.join(w) for w in itertools.product(letters, repeat=n)
             if set(w)==set(letters)}
    outputs = {w: deletion_outputs(w) for w in words}
    conflicting = lambda x,y: len(outputs[x] & outputs[y]) >= 2
    I = record['independent_words']; M = record['matching_edges']
    assert len(I)==len(set(I)) and set(I)<=words
    assert all(not conflicting(x,y) for x,y in itertools.combinations(I,2))
    touched=[]
    for x,y in M:
        assert x!=y and x in words and y in words and conflicting(x,y)
        touched.extend([x,y])
    assert len(touched)==len(set(touched))
    assert len(I)+len(M)==len(words)
    return len(I),len(M),len(words)

def run(file):
    data=json.load(open(file,encoding='utf-8'))
    expected={(3,1):(1,0,1),(3,2):(4,2,6),(3,3):(3,3,6),
              (4,1):(1,0,1),(4,2):(8,6,14),(4,3):(18,18,36),(4,4):(12,12,24)}
    got={}
    for rec in data['cases']:
        n,k=rec['n'],rec['support_size']; assert (n,k) not in got
        got[n,k]=case(n,k,rec)
    assert got==expected,(got,expected)
    alphas={n:{k:got[n,k][0] for k in range(1,n+1)} for n in (3,4)}
    for q in range(2,50):
        assert sum(math.comb(q,k)*a for k,a in alphas[3].items() if k<=q) == q*q*(q+1)//2
        assert sum(math.comb(q,k)*a for k,a in alphas[4].items() if k<=q) == q*q*(q*q+1)//2
    # Direct q-ary conflict-graph decomposition, checked separately at q=3.
    for n in (3,4):
      words=[''.join(w) for w in itertools.product('012', repeat=n)]
      D={w:deletion_outputs(w) for w in words}
      for x,y in itertools.combinations(words,2):
        if set(x)!=set(y):assert len(D[x]&D[y])<=1
    print('VERIFY_OK cases=7 independent_set_and_matching_certificates=7 q_formula_checks=48 direct_support_check_q=3')

if __name__=='__main__':run(sys.argv[1] if len(sys.argv)>1 else 'certificates.json')
