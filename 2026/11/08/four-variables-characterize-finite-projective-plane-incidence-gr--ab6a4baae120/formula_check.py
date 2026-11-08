#!/usr/bin/env python3
"""Independently construct and evaluate a capture-safe FO^4 recognition sentence."""
from itertools import product

def Eq(a,b):return ('eq',a,b)
def Ed(a,b):return ('edge',a,b)
def Not(a):return ('not',a)
def And(*args):return ('and',args)
def Or(*args):return ('or',args)
def Im(a,b):return Or(Not(a),b)
def Ex(v,a):return ('exists',v,a)
def All(v,a):return ('forall',v,a)
# The witness variable w is always local; no C instance occurs in a
# clause where w is free outside that instance.
def C(a,b):return Or(Eq(a,b),Ex('w',And(Ed(a,'w'),Ed(b,'w'))))

clauses=[
    Ex('x',Ex('y',Not(C('x','y')))),
    All('x',All('y',All('z', Im(And(C('x','y'),C('y','z')),C('x','z'))))),
    All('x',All('y',All('z', Im(And(Not(C('x','y')),Not(C('x','z'))),C('y','z'))))),
    All('x',All('y',Im(Ed('x','y'),Not(C('x','y'))))),
    All('x',Ex('y',Ex('z',Ex('w',And(Ed('x','y'),Ed('x','z'),Ed('x','w'),Not(Eq('y','z')),Not(Eq('y','w')),Not(Eq('z','w'))))))),
    All('x',All('y',All('z',All('w',Im(And(Not(Eq('x','y')),Ed('x','z'),Ed('y','z'),Ed('x','w'),Ed('y','w')),Eq('z','w')))))),
]

def all_names(f):
    op=f[0]
    if op in ('eq','edge'):return {f[1],f[2]}
    if op=='not':return all_names(f[1])
    if op in ('and','or'):return set().union(*(all_names(a) for a in f[1]))
    if op in ('exists','forall'):return {f[1]}|all_names(f[2])
    raise AssertionError(op)

def free(f):
    op=f[0]
    if op in ('eq','edge'):return {f[1],f[2]}
    if op=='not':return free(f[1])
    if op in ('and','or'):return set().union(*(free(a) for a in f[1]))
    if op in ('exists','forall'):return free(f[2])-{f[1]}
    raise AssertionError(op)

def evaluate(f,E,env):
    op=f[0]
    if op=='eq':return env[f[1]]==env[f[2]]
    if op=='edge':return E[env[f[1]]][env[f[2]]]
    if op=='not':return not evaluate(f[1],E,env)
    if op=='and':return all(evaluate(a,E,env) for a in f[1])
    if op=='or':return any(evaluate(a,E,env) for a in f[1])
    if op in ('exists','forall'):
        v,body=f[1],f[2]; had=v in env; old=env.get(v)
        try:
            if op=='exists':
                for t in range(len(E)):
                    env[v]=t
                    if evaluate(body,E,env):return True
                return False
            for t in range(len(E)):
                env[v]=t
                if not evaluate(body,E,env):return False
            return True
        finally:
            if had:env[v]=old
            else:env.pop(v,None)
    raise AssertionError(op)

def plane(q):
    v=[]
    for a in product(range(q),repeat=3):
        if not any(a):continue
        t=next(x for x in a if x)
        inv=pow(t,-1,q)
        v.append(tuple(x*inv%q for x in a))
    v=sorted(set(v));n=len(v)
    E=[[False]*(2*n) for _ in range(2*n)]
    for i,p in enumerate(v):
        for j,l in enumerate(v):
            if sum(x*y for x,y in zip(p,l))%q==0:
                E[i][n+j]=E[n+j][i]=True
    return E

def fano_complement():
    E=plane(2)
    n=len(E)//2
    for i in range(n):
        for j in range(n,2*n):
            E[i][j]=E[j][i]=not E[i][j]
    return E

assert len(clauses)==6
assert all(all_names(c)<={'x','y','z','w'} and not free(c) for c in clauses)
for name,E,expect in [('FANO',plane(2),True),('COMPLEMENT_FANO',fano_complement(),False),('PG2_OVER_F3',plane(3),True)]:
    values=[evaluate(c,E,{}) for c in clauses]
    assert all(values)==expect
    print(name,'CLAUSES',','.join('1' if a else '0' for a in values))
print('FOUR_NAMES_ALL_CLAUSES_CLOSED=PASS')
print('FO4_FORMULA_EVALUATION=PASS')
