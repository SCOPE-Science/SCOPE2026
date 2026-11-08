"""Independent finite checks for variable-free one-action LoopPDL orbit types.

Run with Python 3.10 or newer. No external dependencies.
"""
from itertools import product

A = ('action',)
TOP = ('top',)

def seq(*ps):
    if not ps:
        return ('test', TOP)
    r = ps[0]
    for p in ps[1:]:
        r = ('seq', r, p)
    return r

def power(k):
    assert k >= 0
    return seq(*([A] * k))

def plus():
    return seq(A, ('star', A))

def dia(p, phi):
    return ('dia', p, phi)

def neg(phi):
    return ('neg', phi)

def conj(*xs):
    if not xs:
        return TOP
    z=xs[0]
    for x in xs[1:]:
        z=('and', z, x)
    return z

def loop(p):
    return ('loop', p)

def terminal_formula(h):
    return conj(dia(power(h), TOP), neg(dia(power(h+1), TOP)))

def period_formula(d):
    return conj(loop(power(d)), *(neg(loop(power(e))) for e in range(1, d) if d % e == 0))

def lasso_formula(t,d):
    if t == 0:
        return period_formula(d)
    return conj(dia(power(t), period_formula(d)), neg(dia(power(t-1), loop(plus()))))

def eval_formula(formula, successors):
    size=len(successors)
    univ=set(range(size))
    formula_cache={}
    prog_cache={}
    def compose(r,s):
        return {(a,c) for a,b in r for bb,c in s if b == bb}
    def eval_prog(p):
        if p in prog_cache:
            return prog_cache[p]
        tag=p[0]
        if tag=='action':
            r={(i,v) for i,v in enumerate(successors) if v is not None}
        elif tag=='seq':
            r=compose(eval_prog(p[1]),eval_prog(p[2]))
        elif tag=='union':
            r=eval_prog(p[1])|eval_prog(p[2])
        elif tag=='test':
            r={(i,i) for i in eval_f(p[1])}
        elif tag=='star':
            r={(i,i) for i in range(size)}|eval_prog(p[1])
            while True:
                nxt=r|compose(r,r)
                if nxt==r:break
                r=nxt
        else:
            raise AssertionError(tag)
        prog_cache[p]=r
        return r
    def eval_f(phi):
        if phi in formula_cache:
            return formula_cache[phi]
        tag=phi[0]
        if tag=='top':
            ans=univ
        elif tag=='neg':
            ans=univ-eval_f(phi[1])
        elif tag=='and':
            ans=eval_f(phi[1])&eval_f(phi[2])
        elif tag=='dia':
            trg=eval_f(phi[2]);ans={i for i,j in eval_prog(phi[1]) if j in trg}
        elif tag=='loop':
            ans={i for i,j in eval_prog(phi[1]) if i==j}
        else:
            raise AssertionError(tag)
        formula_cache[phi]=ans
        return ans
    return eval_f(formula)

def shape(successors,root):
    seen={}; sequence=[];u=root
    while u is not None and u not in seen:
        seen[u]=len(sequence)
        sequence.append(u)
        u=successors[u]
    if u is None:
        return ('end',len(sequence)-1)
    return ('cycle',seen[u],len(sequence)-seen[u])

def canonical(key):
    if key[0]=='end':
        h=key[1]
        return tuple(list(range(1,h+1))+[None])
    t,d=key[1:]
    return tuple(list(range(1,t+d))+[t])

def keys(n):
    return ([('end',h) for h in range(n)]
           +[('cycle',t,d) for t in range(n) for d in range(1,n-t+1)])

def check(n):
    ks=keys(n)
    forms={k:terminal_formula(k[1]) if k[0]=='end' else lasso_formula(k[1],k[2]) for k in ks}
    assert len(ks)==n*(n+3)//2
    for k in ks:
        successors=canonical(k)
        assert len(successors)<=n
        assert shape(successors,0)==k, (n,k,successors)
        hits=[other for other in ks if 0 in eval_formula(forms[other],successors)]
        assert hits==[k], (n,k,hits)
    print('canonical n=',n,'LoopPDL_types=',len(ks),'PDL_types=',n+1,'all characteristic formulas separate')

def exhaustive(n):
    possible={None,*range(n)}
    possible=[None]+list(range(n))
    actual=set()
    for successors in product(possible,repeat=n):
        for root in range(n):
            actual.add(shape(successors,root))
    assert actual==set(keys(n)),(n,len(actual),len(keys(n)),actual^set(keys(n)))
    print('exhaustive n=',n,'maps=',len(possible)**n,'roots=',n*len(possible)**n,'distinct=',len(actual))

if __name__=='__main__':
    for n in range(1,9):check(n)
    for n in range(1,6):exhaustive(n)
    print('ALL_CHECKS_OK')
