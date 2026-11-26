# Independent mathematical audit

## correctness

PASS

Reconstructed the adjacency on unordered distinct pairs in RESULT.md 37–72. Core-pair to core-pair is U_r^T U_r−2I; mixed-to-mixed moves only the core label and give (J_r−I)⊗I_m. A core pair connects to a mixed pair precisely when the new mixed core label is one of the original two, and a peripheral pair connects to a mixed pair under the analogous peripheral-label condition. This gives exactly the two incidence couplings, with the all-ones vector for the other label. There is no peripheral-to-peripheral hop or direct core-pair to peripheral-pair hop. In each vertex space U_sU_s^T=(s−2)I+J, with eigenvalues 2(s−1) on the constants and s−2 on their orthogonal complement. Thus normalized incidence lifts give coupling strengths √(m(r−2)) and √(r(m−2)) in the two respective repeated two-dimensional sectors, with diagonals (r−4,−1) and (r−1,0). The uniform sector gives couplings √(2m(r−1)) and √(2r(m−1)), and diagonals (2r−4,r−1,0). The unused incidence kernels and mixed standard-standard sector yield exactly −2, 0 and −1 with the stated multiplicities. Determinants give A,B,C; the dimensions sum to all unordered pairs. A(0)<0, B(0)<0, C(0)>0 for all r,m≥3, including the endpoints, so no block adds a zero. The zero projector is supported on peripheral pairs, and its constant diagonal there is rank divided by binomial(m,2), including zero for m=3. The complementary evolved component remains orthogonal to the stationary projection even after peripheral restriction, so the peripheral probability is at least the projector weight d. The return amplitude equals d plus a term of modulus at most 1−d; for m≥6 the reverse triangle inequality gives the stated squared bound. Read VERIFICATION.md and verify_split_bosons.py without running the uploaded program; the invariant-subspace proof establishes the claim without the finite checks.

## originality

PASS

The supported new content is the full adjacency factorization for the complete-split two-token family, including the nonzero coupled sectors and proof of no additional zero modes. Symmetric-square/token methods and the peripheral incidence-kernel geometry, including the exact diagonal projector fraction, have substantive prior counterparts; they are not independent novelty claims. The closest exact-family Resultary source has the same adjacency graph but proves a maximum-cut theorem, not this spectrum.

## value

PASS

The fully coupled clique interacting with an extensive independent periphery is a natural exactly solvable test of hard-core two-particle transport. The uniform formula gives all nonzero symmetry channels and multiplicities, not just spectral radius or the already familiar dark incidence kernel. In particular, excluding every other zero mode identifies the whole stationary subspace and its exact weight for all clique sizes. The dynamical inequalities interpret this result; they are not asserted to be sharp exact return laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
