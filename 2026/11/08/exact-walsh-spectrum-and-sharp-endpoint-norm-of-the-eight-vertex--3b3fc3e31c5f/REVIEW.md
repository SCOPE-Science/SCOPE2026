# Mathematical review: perfect-matching Walsh spectrum on eight vertices

## Correctness

**PASS.** Each of the 105 perfect matchings contributes one monomial in distinct edge signs. The seven-edge vertex-switching normalization has fibers of size 128; the reduced 21-edge assignments are enumerated without sampling. The exact integer Walsh butterfly certificate and the independent C11 direct 105-term hafnian evaluation both reproduce all 23 multiplicities, the absolute first moment 16854180, the second moment 220200960, and the fourth moment 84777369600. The moment identities also follow separately from orthogonality and XOR-difference counts. The two endpoint norms coincide with the \(\ell^1\) norm of the corresponding convolution kernel, with explicit equality inputs. The claim is exclusively about order eight, for which the enumeration is exhaustive.

## Originality

**PASS, with a bounded-priority limitation.** The hafnian representation of perfect-matchings is classical, and the natural comparison source Rudelson–Samorodnitsky–Zeitouni (arXiv:1409.3905) studies Gaussian randomized estimators for nonnegative matrices. Its main theorems concern concentration of random determinants under expansion conditions, not a Rademacher signed-hafnian histogram at order eight. Published hafnian definitions and sign-gauge identities do not themselves give a 23-level multiplicity census. The nearest related finite signed-permanent example concerns a five-by-five *bipartite* permutation-matrix orbit; it does not imply the distribution on the 28 edges of a nonbipartite complete graph. Broad and parameter-specific searches did not locate the order-eight histogram or its sharp endpoint constant, but a missing older tabulation or an equivalent signed-matching enumerator remains possible. Failed searches do not prove priority.

## Value

**PASS.** The perfect-matching orbit of the complete graph is a canonical highly symmetric Fourier frequency set. Its absolute Fourier-multiplier kernel determines a sharp endpoint amplification constant unavailable from cardinality or Parseval alone. The full signed-hafnian amplitude law distinguishes 23 nonzero levels and their precise probabilities; its exact first absolute moment is a new-type invariant relative to known second moments, asymptotic estimators, and the separate bipartite permanent problem. The eight-vertex case has 105 distinct matching monomials and a substantial \(2^{28}\)-point character domain. It is a complete natural finite invariant, not a hand-selected subfamily or an extrapolated conjecture.

## Residual limitations

Independent mathematical validation has not been performed. Literature coverage is bounded rather than exhaustive. Exact finite integer computation is a proof for order eight, not evidence for a general even-order formula. The source paper is cited for context and the classical hafnian definition, not for priority of the new histogram.

Self-review: passed. Independent audit: not yet performed.
