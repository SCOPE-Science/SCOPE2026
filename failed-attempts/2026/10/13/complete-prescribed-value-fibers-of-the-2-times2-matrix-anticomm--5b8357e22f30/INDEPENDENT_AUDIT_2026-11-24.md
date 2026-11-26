# Independent mathematical audit

## correctness

PASS

RESULT.md lines 3–34 and 38–95 correctly count ordered unrestricted pairs for the ordinary anticommutator in every odd finite field. Direct check without Fourier: for X nonzero traceless, polarized Cayley–Hamilton gives T_X(Y)=tr(Y)X+tr(XY)I, with image span(I,X) and nullity 2. Every such X works for scalar B, and exactly q−1 such X work for a nonscalar B (the multiples of its traceless part). If tr X ≠ 0 and det X = 0, write X=t(I−P) for a unique rank-one idempotent P and nonzero t. In the eigenspace basis T_X has one-dimensional kernel span(P), and B is attained iff tr(PB)=0, in which case it has q preimages. For a given image line of P there are q, 0, or 1 eligible complements according as B acts as zero on that line, acts as a nonzero scalar there, or does not preserve it. Thus there are qz+q+1−e such P. The remaining nonzero-trace invertible X give one preimage each (their eigenvalue sums are all nonzero); there are q^4−2q^3+q. Finally X=0 contributes q^4 only at B=0. Adding gives the exact displayed formulas. For q≥3 the five nonscalar offsets −2,−1,0,q−2,q−1 are distinct and both scalar values are strictly larger; all types exist, including a split distinct nonzero pair when q=3. Independent replay: python /workspace/branches/independent_reproduction.py 3 row-reduced every left-factor map in GF(9) for one target in each stratum and matched all seven formulas. Additional independent direct enumeration checked every target at q=3,5 (replay /workspace/branches/af395f76-21c7-44d9-b5c6-b295f7bbbc09/independent_check.py). These bounded checks are not the all-field proof; the frozen verifier was inspected, not executed.

## originality

FAIL

A distinct published catalogue entry gives exactly the same nonzero-target census, and also the same zero count. Its catalogue date is later than this frozen finding; this is verified equivalent coverage in the current audit, not evidence that the frozen finding lacked priority on its original publication date. The zero-target specialization has older primary coverage independently of the catalogue overlap.

## value

FAIL

The exact anticommutator distribution is a natural and useful invariant in its own right. As submitted, however, the contribution is the exact census already fully available in the distinct matching entry, not a new use of the Fourier argument, a stronger result, or a distinct needed invariant. A proof-approach difference alone supplies no independently established surviving contribution here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
