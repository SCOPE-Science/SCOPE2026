#!/usr/bin/env python3
"""Independent bounded checks of a symbolic classification of row deletion.
Uses only Python's standard library. All set, semigroup and gap tests are direct.
"""

def in_s(x,a,b):
    if x<0:return False
    if x%3==0:return True
    if x%3==1:return x>=3*a+1
    return x>=3*b+2

def build(a,b):
    if not (a>=1 and b>=1 and b<=2*a and a<=2*b+1):return None
    F=max(3*a+1,3*b+2)-3
    small=[x for x in range(F+2) if in_s(x,a,b)]
    gaps=[x for x in range(1,F+1) if x not in small]
    pf=[x for x in gaps if all(in_s(x+s,a,b) for s in small if s>0)]
    return F,small,gaps,pf

def deletion(F,small,pf):
    removed=pf[:-1]
    Fp=F-len(removed)
    return Fp,{x-sum(p<x for p in removed) for x in small if x<=F+1}

def predicted_A(a,Fp):
    u=3*a-1
    return {x for x in range(Fp+2) if any(x-3*j>=0 and (x-3*j)%u==0 for j in range(x//3+1))}

def predicted_B(b,Fp):
    return {x for x in range(Fp+2) if (
        (x%3==0 and (x<=3*b-3 or x>=6*b))
        or (x%3==1 and x>=3*b+1)
        or (x%3==2 and x>=3*b-1))}

def actual_defects(T,Fp):
    ordered=[]
    for x in sorted(T):
        if x==0:continue
        for y in sorted(T):
            if y==0:continue
            if x+y<=Fp and x+y not in T:
                ordered.append((x,y,x+y))
    return ordered

n=0
for a in range(1,31):
    for b in range(1,31):
        result=build(a,b)
        if result is None: continue
        F,small,gaps,pf=result
        # Independently check closure on all small elements, and Apéry genus.
        for x in small:
            for y in small:
                assert in_s(x+y,a,b), (a,b,x,y)
        assert len(gaps)==a+b,(a,b)
        assert max(gaps)==F
        almost=(2*len(gaps)==F+2 and len(pf)==2)
        assert almost==((b==2*a-1 and b>=a) or (a==2*b and a>b)), (a,b,pf)
        if not almost:continue
        assert len(pf)==2 and pf==[F//2,F], (a,b,pf)
        Fp,T=deletion(F,small,pf)
        assert Fp==F-1
        assert len(T)==len(set(T))
        # Original gap deletion and target numerical-set complement are checked directly.
        assert Fp not in T
        assert all(((x in T) != (Fp-x in T)) for x in range(Fp+1))
        if b==2*a-1 and b>=a:
            expected=predicted_A(a,Fp)
            assert T==expected,(a,b,T^expected)
            assert actual_defects(T,Fp)==[]
        else:
            expected=predicted_B(b,Fp)
            assert T==expected,(a,b,T^expected)
            defect=actual_defects(T,Fp)
            targets={z for _,_,z in defect}
            assert targets==set(range(3*b,6*b-5,3)),(a,b,targets)
            assert len(defect)==b*(b-1)//2,(a,b,len(defect))
            assert (len(defect)==0)==(b==1)
        n+=1
print('VERIFY_OK; all eligible Apéry pairs a,b<=30; pseudo-symmetric cases:',n)
