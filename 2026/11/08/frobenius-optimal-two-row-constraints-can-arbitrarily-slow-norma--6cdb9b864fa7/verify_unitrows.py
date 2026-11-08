#!/usr/bin/env python3
"""Exact-rational verification of normalized six-row selection and moment laws."""
import itertools
import sympy as sp


def verify(s, c):
    assert s > 0 and s < c and s*s+c*c==1
    z=sp.zeros(4,1)
    e=[sp.eye(4)[:,i] for i in range(4)]
    rows=[e[1], e[1], e[2], e[2], c*e[0]+s*e[3], c*e[0]-s*e[3]]
    xstar=e[1]+e[3]
    A=sp.Matrix.vstack(*[r.T for r in rows]); AtA=A.T*A
    assert AtA==sp.diag(2*c*c,2,2,2*s*s)
    assert AtA.eigenvals()[2*s*s]==1
    assert sp.simplify(2/(2*s*s)) == 1/(s*s)
    table={}
    for selected in itertools.combinations(range(6),2):
        C=sp.Matrix.hstack(*[rows[i] for i in selected]); CP=C*(C.T*C).pinv()*C.T
        P=sp.eye(4)-CP
        B=A*P
        frob=sp.trace(B.T*B)
        eig=[x for x in (B.T*B).eigenvals() if x>0]
        delta=min(eig)/frob
        table[selected]=(frob,delta,P)
    min_cost=min(v[0] for v in table.values())
    assert min_cost==2
    ids={ij for ij,(cost,_,_) in table.items() if cost==min_cost}
    assert ids=={(i,j) for i in (0,1) for j in (2,3)}
    best=max(v[1] for v in table.values())
    assert best==sp.Rational(1,2)
    assert {ij for ij,(cost,delta,P) in table.items() if delta==best}=={(4,5)}
    for ij in ids:
        assert table[ij][1]==s*s
    assert sp.simplify(best/(s*s))==1/(2*s*s)
    # Exact Markov evolution for each of the two compared fixed sets.
    for selected in ((0,2),(4,5)):
        P=table[selected][2]
        rem=[i for i in range(6) if i not in selected]
        projected=[(P*rows[i]).applyfunc(sp.simplify) for i in rem]
        denom=sum([(v.T*v)[0] for v in projected])
        prob=[sp.simplify((v.T*v)[0]/denom) for v in projected]
        operators=[sp.eye(4)-v*v.T/(v.T*v)[0] for v in projected]
        # E[e_t e_t^T] follows a finite matrix recursion.
        x0=(sp.eye(4)-P)*xstar
        error=x0-xstar
        M=error*error.T
        for t in range(6):
            actual=sp.simplify(sp.trace(M))
            if selected==(4,5):
                target=sp.Rational(1,2)**t
            elif t==0:
                target=1
            else:
                target=c*c*(1-2*c*c*s*s)**(t-1)
            assert sp.simplify(actual-target)==0,(s,c,selected,t,actual,target)
            M=sum((prob[j]*operators[j]*M*operators[j].T for j in range(4)),sp.zeros(4,4)).applyfunc(sp.simplify)
        # Second protocol: reject rows with zero current residual and resample.
        states=[(sp.Integer(1),error)]
        for t in range(6):
            actual=sum((wt*(err.T*err)[0] for wt,err in states),sp.Integer(0))
            if selected==(4,5):
                target=sp.Integer(1) if t==0 else sp.Integer(0)
            elif t==0:
                target=sp.Integer(1)
            else:
                target=c*c*(c*c-s*s)**(2*(t-1))
            assert sp.simplify(actual-target)==0,(s,c,selected,t,actual,target)
            newer=[]
            for wt,err in states:
                eligible=[j for j,v in enumerate(projected) if (v.T*err)[0]!=0]
                if not eligible:
                    newer.append((wt,err))
                    continue
                mass=sum(((projected[j].T*projected[j])[0] for j in eligible),sp.Integer(0))
                for j in eligible:
                    pn=(projected[j].T*projected[j])[0]/mass
                    errnext=(operators[j]*err).applyfunc(sp.simplify)
                    newer.append((sp.simplify(wt*pn),errnext))
            states=newer
    return len(table)


def main():
    total=0
    for s,c in [(sp.Rational(3,5),sp.Rational(4,5)),
                (sp.Rational(5,13),sp.Rational(12,13)),
                (sp.Rational(8,17),sp.Rational(15,17)),
                (sp.Rational(20,101),sp.Rational(99,101))]:
        total+=verify(s,c)
    print('PASS: exact spectra, all %s constrained pairs, and 96 exact moment identities' % total)

if __name__=='__main__':
    main()
