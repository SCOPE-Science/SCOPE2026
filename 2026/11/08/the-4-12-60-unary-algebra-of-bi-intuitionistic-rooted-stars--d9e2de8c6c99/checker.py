#!/usr/bin/env python3
"""Reproduce the one-letter bi-intuitionistic formula-algebra census on finite rooted stars.

No dependencies beyond the Python standard library.  The proof of the upper
bound and of completeness of the normal forms is in RESULT.md.
"""
from itertools import product

P = ('p',)
BOT = ('bot',)
TOP = ('top',)

def AND(x,y): return ('and',x,y)
def OR(x,y): return ('or',x,y)
def IMP(x,y): return ('imp',x,y)
def SUB(x,y): return ('sub',x,y)
def NEG(x): return IMP(x,BOT)
def C(x): return SUB(TOP,x)

NP = NEG(P)
NNP = NEG(NP)
selectors = (
    NEG(C(NP)),               # empty valuation
    NEG(C(P)),                # full valuation
    AND(NEG(C(NNP)), C(P)),   # all leaves only
    AND(C(NNP), C(NP)),       # some, but not all leaves
)

def union_disj(seq):
    out = BOT
    for x in seq:out = OR(out,x)
    return out

normal_forms = [union_disj((AND(selectors[0],x),
                            AND(selectors[1],y),
                            AND(selectors[2],z),
                            AND(selectors[3],w)))
                for x,y,z,w in product((BOT,TOP),(BOT,TOP),
                                      (BOT,P,TOP),
                                      (BOT,P,NP,OR(P,NP),TOP))]
assert len(normal_forms)==60


def algebra(m,p):
    leafmask=(1<<m)-1
    full=(1<<(m+1))-1
    cache={}
    def rec(f):
        if f in cache:return cache[f]
        tag=f[0]
        if tag=='p': result=p
        elif tag=='top':result=full
        elif tag=='bot':result=0
        else:
            x,y=rec(f[1]),rec(f[2])
            if tag=='and':result=x&y
            elif tag=='or':result=x|y
            elif tag=='imp':
                result=((~x)|y)&leafmask
                if (x&~y)==0:result|=1<<m
            elif tag=='sub':
                if (x&(1<<m)) and not (y&(1<<m)):result=full
                else:result=x&~y&leafmask
            else:raise ValueError(tag)
        cache[f]=result
        return result
    return rec


def world_eval(m,p,f,w):
    # Independent point-quantified semantics, not algebraic bitset identities.
    @__import__('functools').lru_cache(maxsize=None)
    def rec(formula,world):
        tag=formula[0]
        if tag=='p':return bool((p>>world)&1)
        if tag=='top':return True
        if tag=='bot':return False
        if tag=='and':return rec(formula[1],world) and rec(formula[2],world)
        if tag=='or':return rec(formula[1],world) or rec(formula[2],world)
        if tag=='imp':
            future=range(m+1) if world==m else (world,)
            return all(not rec(formula[1],v) or rec(formula[2],v) for v in future)
        if tag=='sub':
            past=(m,) if world==m else (m,world)
            return any(rec(formula[1],v) and not rec(formula[2],v) for v in past)
        raise ValueError(tag)
    return rec(f,w)


def closure_size(m):
    leafmask=(1<<m)-1
    full=(1<<(m+1))-1
    values=list(range(1<<m))+[full]
    def run(tag,x,y):
        if tag=='and':return x&y
        if tag=='or':return x|y
        if tag=='imp':return ((~x|y)&leafmask) | ((1<<m) if not (x&~y) else 0)
        if tag=='sub':return full if ((x&(1<<m)) and not (y&(1<<m))) else (x&~y&leafmask)
    tab={op:{x:{y:run(op,x,y) for y in values} for x in values} for op in ('and','or','imp','sub')}
    vals=[tuple([0]*len(values)),tuple([full]*len(values)),tuple(values)]
    seen=set(vals)
    i=0
    while i<len(vals):
        a=vals[i]
        for b in vals[:i+1]:
            for op in tab:
                for v,w in ((a,b),(b,a)):
                    c=tuple(tab[op][x][y] for x,y in zip(v,w))
                    if c not in seen:seen.add(c);vals.append(c)
        i+=1
    return len(vals),set(vals)


def main():
    for m in range(6):
        leafmask=(1<<m)-1
        full=(1<<(m+1))-1
        valuations=list(range(1<<m))+[full]
        masks=[]
        for f in normal_forms:
            out=[]
            for p in valuations:
                direct=algebra(m,p)(f)
                pointwise=sum((1<<w) for w in range(m+1) if world_eval(m,p,f,w))
                assert direct==pointwise,(m,p,direct,pointwise)
                out.append(direct)
            masks.append(tuple(out))
        count=len(set(masks))
        assert count==({0:4,1:12}.get(m,60)),(m,count)
        # Selectors isolate their four valuation classes at every world.
        for p in valuations:
            category=(0 if p==0 else 1 if p==full else 2 if p==leafmask else 3)
            assert [algebra(m,p)(f) for f in selectors]==[full if j==category else 0 for j in range(4)]
        print('m=%d valuations=%d distinct_normal_forms=%d independent_world_semantics=OK'% (m,len(valuations),count))
    for m,expected in ((0,4),(1,12),(2,60)):
        count,functions=closure_size(m)
        assert count==expected,(m,count)
        valuations=list(range(1<<m))+[(1<<(m+1))-1]
        certified={tuple(algebra(m,p)(f) for p in valuations) for f in normal_forms}
        assert functions==certified
        print('m=%d exhaustive_generated_closure=%d exact_normal_forms=OK'%(m,count))
    print('BIINT_ROOTED_STAR_UNARY_4_12_60_OK')

if __name__=='__main__':main()
