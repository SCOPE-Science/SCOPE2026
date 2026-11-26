# Independent mathematical audit

## correctness

PASS

The unit path has the simple cosine spectrum λ_k=2−2 cos(πk/n) with normalized half-step eigenvector entries. If d=gcd(2j−1,n)>1, the mode k=n/d has a cosine zero. Otherwise multiplication by 2j−1 permutes the residue pairs ±k modulo 2n, preserving the product of squared cosines; the fixed classes 0 and n are excluded from the permutation. The sine product gives ∏_{k=1}^{n−1}cos²(πk/(2n))=n/4^(n−1), so including eigenvector normalization gives ∏_k v_k(j)²=(2n)^(1−n). The Vandermonde then fixes the nonzero absolute Kalman determinant independent of j; the distance-triangular endpoint basis gives value one. In modal coordinates W_j has the common time kernel flanked by the diagonal input vector; distinct exponentials on a positive interval make the kernel positive definite, including μ=0 with the time-integral convention at the constant mode. This proves the two determinant cases and φ(2n) maximizing sites; for powers of two this is every site. The positive-damping infinite-horizon Cauchy identity and the small-time trace difference are also consistent. The common value is for each fixed (T,μ), not numerically constant as those parameters change. Independently generating the actual edge Krylov matrices and eliminating modulo 1009 at all sites of orders 21,22,25,27,30,32 gave respectively 12,20,20,18,16,32 nonzero residues, all ±1 and at precisely the predicted sites. This is corroboration, not the proof; the supplied code was read without execution.

## originality

FAIL

The exact main theorem is covered by a distinct indexed result plus the published Chebyshev resultant identity, not just by the 2011 qualitative rank criterion. The distinct all-positive-weight path theorem independently establishes the exact magnitude/resultant and finite-horizon spectral-factor formulas, explicitly identifies the uniform zero-or-unit and common-volume classification as background, and has a direct unit-weight specialization once the cut-block resultant is evaluated by Louboutin's theorem. The resulting tie and normalization cover the quantitative claim itself; no distinct substantive remainder is established for the frozen result. This is a statement-coverage judgment, not a claim that one of the two same-day records was posted first. The inaccessible Dilip paper is not the reason for failure.

## value

PASS

As a mathematical classification, this answers a natural all-size question about reachable volume and integer control, distinguishing a determinant tie from graph automorphism, trace or conditioning. At dyadic sizes the endpoint and interior have different degrees yet tie at every horizon, which is a useful constraint on actuator-placement intuition. This scientific usefulness does not establish independent originality over the checked stronger result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
