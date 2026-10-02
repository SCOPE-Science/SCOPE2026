# Independent mathematical audit — SCOPE-20260920-4185b4e0fd93

Final disposition: **FAILED**.

## Correctness
**PASS** — The quantitative construction is mathematically consistent. Karagulyan's logarithmic finite Fourier obstruction supplies a prescribed bad permutation; Lewko's two-copy coloring lemma is made quantitative by bounding exceptional colorings and inserting Gowers's quantitative Szemeredi theorem. With \(D_m=2^{2^{m+9}}\) and \(Q_m\) as defined, the sufficient scale \(X_m=2^{2^{Q_m^{D_m}}}\) gives \(L_3(X_m)=D_m\log_2Q_m\), hence \(L_5(X_m)=m+O(1)\), so a \(\log m\) obstruction becomes an \(L_6(N)\) lower bound. Lewko's complete source confirms the two-copy mechanism and the real-valued \(\sqrt2\) realification. An earlier published proof independently establishes the same six-logarithm lower rate.

## Originality
**FAIL** — A September 17 published result already proves \(G(N)\ge c\log_{(6)}N\) for all sufficiently large \(N\) by exactly the same Lewko-Karagulyan-Gowers synthesis and fivefold-exponential inversion. The assigned explicit \(X_m\) bookkeeping is a quantitative unpacking of that proof, while its real-valued \(\sqrt2\) corollary is the standard realification already present qualitatively in Lewko's primary paper. The central final claim is therefore exactly covered, and the remaining details are routine refinements rather than an original theorem.

### Equivalent formulations
The different notation for iterated logarithms and the more explicit finite threshold do not change the scientific implication.

### Broader coverage
The assigned record adds no stronger asymptotic rate or new obstruction mechanism.

### Exact database or table
This direct positive prior-coverage hit is decisive.

### Claim versus prior implication
The final scientific content is mechanically covered.

## Value
**FAIL** — Once the six-iterated-logarithm lower bound has already been published by the identical mechanism, replacing an \(E_5(Cm)\) threshold by one explicit enormous formula and appending the standard realification does not create a separate mathematically motivated contribution. The record is useful exposition but fails the independent value bar.

## Source inspections
- **An explicit iterated-log lower bound for the finite Garsia rearrangement constant** (https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-quantitative-garsia-rearrangement-lower-bound--7325492acf77): complete published RESULT.md Method: published-record full-text inspection. Assessment: EXACT_PRIOR_COVERAGE. Evidence: It proves \(G(N)\ge c\log_{(6)}N\) from the same three quantitative ingredients and the same two-copy construction.
- **On Kolmogorov's rearrangement problem and Garsia's conjecture** (https://arxiv.org/abs/2609.18491): complete eight-page primary preprint Method: authorized full-text inspection after open full text was unavailable. Assessment: PRIMARY_QUALITATIVE_SOURCE_AND_REALIFICATION. Evidence: The paper gives the finite two-copy construction, says the proof has no useful \(N\)-versus-\(H\) rate, and gives real-valued examples bounded by \(\sqrt2\).

## Checked sources
- https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-quantitative-garsia-rearrangement-lower-bound--7325492acf77
- https://arxiv.org/abs/2609.18491

## Residual risks
- No correctness defect is asserted; rejection is exact prior coverage and lack of surviving independent value.
