# Independent mathematical audit

## correctness

PASS

An Euler tour in the binary order-two de Bruijn multigraph is equivalent to a single cyclic word; balance gives a=a′, b=b′, a+d=b+c and the non-isolated support must be connected. This equivalence includes n=1 and n=2 because the vertex overlaps are periodic. With both bridges present, put p=min(a,b), q=|a−b| and s=min(c,d); the length is u+v+4p+3q+2s, with one choice of bridge ordering at q=0 and two at q>0. This yields the four-vertex contribution z^4(1+z^3)/[(1−z)^2(1−z²)(1−z³)(1−z⁴)]. With only one bridge, the opposite loop must be absent, giving twice the triangle series; with no bridges there are only the alternating and two constant families. Their sum is the claimed rational function. Its degree-zero polynomial part affects only n=0, and the uncancelled primitive third and fourth poles force period divisible by 12. The fifth-order pole has coefficient 1/12, giving 1/288 on n^4. The code maximum is one per attained class. Independent literal enumeration through n=18 and formal-series numerator recovery through degree 60 matched (python3 /workspace/reproduce_reviews.py 1).

## originality

FAIL

The exact claim is already covered in distinct indexed records, most fully f0526690baa6: same ordered cyclic profile data down to n=1, same necessary and sufficient support cases, same count, least period, leading term and capacity interpretation, with an explicit quasipolynomial. These matching entries carry later catalogue dates than the frozen assignment's path. This finding of equivalent existing coverage does not establish earlier publication, independent discovery, derivation or attribution priority on either side. No mathematically distinct remainder of the frozen Finding is established.

## value

FAIL

The scalar count and period are useful for circular profile codes, and the mathematics is not trivial. As a distinct contribution in the checked literature and catalogue, however, the same exact invariant, realizability cases, least period and interpretation are already available, including a composition refinement. There is no additional exact invariant, boundary case or method in the frozen Finding whose distinct scientific value survives that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
