# Review of distance-controlled zero crossings in Boolean-cube biharmonic heat

## Correctness
PASS. Walsh characters diagonalize the unnormalized cube Laplacian with eigenvalues \(2k\), giving exactly the lacunary polynomials \(P_{d,r}(x)\). The Krawtchouk coefficient sequence is a positive binomial multiple of a degree-\(r\) polynomial evaluated at ordered integers, so it has at most \(r\) variations. Descartes allows at most \(r\) positive roots. Independent Taylor support calculations show that \(x=1\) has precise multiplicity \(\lceil r/2\rceil\), leaving at most \(\lfloor r/2\rfloor\) zeros at positive time. Exact rational brackets and root-count saturation prove both four-cube antipodal crossings, and row-sum one gives the sharp endpoint norm. The standalone checker replayed 24,179 checks. Finite testing does not replace the general proof.

## Originality
PASS under the stated bounded historical comparison. The same operator on rectangular rook graphs was compared at complete published-result level, but \(K_a\square K_b\) does not include \(Q_4\). Related Boolean-cube Radau results concern rational timestep approximants, not \(\exp(-tL_d^2)\). Arora and Daners–Glück–Mui treat general eventual positivity for different analytic settings and do not state the dimension-independent Hamming zero-count or sharp four-cube reentrance. Extensive searches for equivalent Krawtchouk/finite Gaussian-difference formulas did not return a stronger coverage result; this is not proof of absolute novelty. Earlier unindexed discrete biharmonic/association-scheme work remains a priority risk.

## Mathematical value
PASS. The theorem replaces a potentially dimension-growing number of temporal sign changes with the uniform bound \(\lfloor r/2\rfloor\), governed by geometric distance alone. It identifies the first natural cube on which a single positive-time kernel entry reenters positivity, gives exact sign transition ordering, the sharp whole-operator positivity horizon, and complete induced \(\ell^1\)/\(\ell^\infty\) norm. These are motivated spectral/semigroup invariants, not a numerically isolated arbitrary case.

## Closest literature and limits
The closest direct operator comparison is the published rook-graph squared-Laplacian theorem, which has one threshold and a different spectrum. The cube Radau IIA paper shares the graph but changes the operator. The general locally eventual positivity literature proves qualitative behavior but not this exact crossing count. Unweighted Boolean cubes and the square of the combinatorial Laplacian only; the global distance bound need not be attained at every larger distance. No independent review has been performed.

Self-review: passed. Independent audit: not yet performed.
