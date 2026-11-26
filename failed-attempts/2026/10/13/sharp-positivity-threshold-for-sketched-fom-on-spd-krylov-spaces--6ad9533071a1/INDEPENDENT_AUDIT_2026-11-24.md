# Independent mathematical audit

## correctness

PASS

The pencil has positive definite Gram factor M=(SV)^*(SV), so an eigenvector Vz gives lambda=(Vz)^*S^*SA(Vz)/[(Vz)^*S^*S(Vz)]. The Gram perturbation bound extends to the complexification of the real embedded space, which contains both Vz and AVz, also after exact breakdown. A^2 <= (mu+L)A-mu*L I gives the sharp turning-angle constant c=2*sqrt(mu*L)/(mu+L) by minimizing t/sqrt((mu+L)t-mu*L) over [mu,L]. Thus the real numerator is at least (1-eps/c)*(Vz)^*A(Vz), and the denominator is at most (1+eps)*||Vz||^2, yielding the asserted positive lower bound. The two-row sketch has exact distortion eps on span(b,Ab); the computed scalar denominator is positive and the numerator changes sign at eps=c. The zero and negative examples are existential, not a claim of failure for all sketches. When mu=L direct substitution gives mu*I for any admissible sketch, including the one-dimensional case. The independent rational replay `python3 /workspace/review_replay.py 3` returns 15/323, 0 and -15/13 for the stated three epsilon values. The frozen verifier was inspected, not executed.

## originality

FAIL

Demonstrably covered by the distinct indexed 2026-10-12 harmonic frontier SCOPE-f6a519d77ab4 via exact inversion of both operator and pencil. The change of name from harmonic to ordinary FOM does not produce a distinct positivity theorem here: the embedding space and distortion are unchanged, and the prior exact witness becomes the frozen scalar witness with the same compressive Gram matrix. The result is correct but not original; this rests on statement-level coverage, not search misses or intent about priority.

## value

FAIL

The underlying threshold is useful for selecting an embedding quality that keeps sketched Ritz values in the domain of reciprocal functions. As a purported new contribution, however, the positivity classification and compression witness are exact re-expressions of the existing harmonic theorem and example. The nonoptimal quantitative bound is an immediate numerator/denominator estimate from the old proof. No additional natural invariant, stronger guarantee, or independent motivated gap is established in the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
