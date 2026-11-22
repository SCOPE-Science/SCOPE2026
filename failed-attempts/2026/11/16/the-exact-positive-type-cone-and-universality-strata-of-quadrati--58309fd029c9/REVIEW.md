# Independent mathematical audit

## correctness

PASS

The SU2 Clebsch–Gordan coefficient identities give a0=L0, a1=2rL1 and for n>=1 a_n/((n+1)r^n)=[2L1+(n-1)L∞]/(n+1); Peter–Weyl therefore reduces nonnegative infinitely many coefficients to L0,L1,L∞>=0. Universality iff L0>0,L1>0,L∞>=0. Feasible vertices solve L0=L1=0 and L1=L∞=0, the third pair violates L1>=0; exact checks in su2_cone_verify.py support the formulas. This correctness is independently reinforced by the published stronger all-degree coefficient theorem, not proof of O or V.

## originality

FAIL

DECISIVE PRIOR COVERAGE: the published all-degree SU2 character-polynomial Abel positivity/universality theorem, read in full, already yields the precise assigned d=2 b=(1,s,t) 3-facet cone, universality boundary and affine spectral tail. This is not a novel independent result, regardless of different exact vertex notation.

## value

FAIL

The complete assigned family is an immediate fixed-degree 2 specialization of a published theorem valid for every polynomial degree d>=1. Its explicit vertices follow by solving three linear inequalities and do not constitute a previously unknown independently motivated structural fact. A correct calculation or detailed certificate cannot make this covered result scientifically valuable as a new claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
