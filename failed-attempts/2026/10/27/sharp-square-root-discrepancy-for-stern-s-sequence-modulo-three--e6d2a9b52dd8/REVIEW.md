# Independent mathematical audit

## correctness

PASS

The binary updates preserve nonzero pairs modulo three and also descend to four projective states: the two axes, the equal-coordinate class E and the mixed class M. An axis sends one child to itself and one to E; E sends both to M; M sends one to each axis. On axis-symmetric state observables the operator is (a,e,m) -> (a+e,2m,2a). For the centered observable 4*1_{first coordinate zero}-1 its symmetric part is (1,-1,-1), annihilated by P^2+P+2I, and its axis-antisymmetric part is an eigenfunction of eigenvalue 1 vanishing at E. The dyadic row starts from E, so d_0=-1, d_1=-2 and the announced recurrence follows; its generating numerator is -1-3z. For any aligned block the initial state can be arbitrary, giving uniform O(2^(r/2)) for block length 2^r using the quadratic roots of modulus sqrt(2) and the bounded antisymmetric contribution. The binary decomposition proves the bound for all prefixes, including n=0. A nonzero initial recurrence vector under a conjugated sqrt(2)-dilation yields a positive normalized limsup along dyadic level counts; differencing adjacent dyadic prefix discrepancies transfers this to the asserted prefix limsup. The separate exact integer replay (reproductions/frozen_checks.py, argument 3) reproduces the frozen eight-state characteristic polynomial and squarefree annihilator.

## originality

FAIL

Dispositive earlier coverage: Bruce Reznick's public arXiv:math/0610601v1 gives exactly the same level counts and equivalent exact recurrence, the uniform O(sqrt(N)) estimate for the same prefix count, and its optimality via an exact oscillatory dyadic formula. Removing the geometric leading term yields the frozen order-two recurrence and rational generating function without any new counting result. The later Resultary comparison is recorded separately and is not needed to establish prior coverage.

## value

FAIL

The precise discrepancy is intrinsically a natural statistic, but as a proposed new finding this recomputes an already available exact result. Centering the known dyadic count and deriving its generating function are routine transformations, and the separate eight-state check supplies corroboration rather than a distinct demonstrated scientific advance. No surviving independent claim is established by this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
