# Independent audit — 2026-09-29
- Source: `2026/09/13/070`
- Assigned/current tree SHA: `28bd30330f3f22e89ae3552d4266eab2c2bf97cd`
- Disposition: **failed**

## Three-axis assessment

### Correctness

**PASSED** — The separator itself is correct: every infinite pure set has a transposition, while an order-preserving automorphism of a linear order cannot have nontrivial finite order. Topos equivalence preserves automorphism groups of points, so the two classifying toposes cannot be equivalent. The Bell versus ordered-Bell orbit counts in the committed script are also correct.

### Originality

**FAILED** — The result is a direct, routine instantiation of standard classifying-topos/topological-Galois machinery. Atomic two-valued classifying toposes are represented as continuous actions of automorphism groups of homogeneous models; the Schanuel topos is explicitly the continuous-action topos of the permutation group of N. After that framework, distinguishing S_infinity from Aut(Q,<) by the existence of a transposition versus torsion-freeness is an elementary observation rather than a new theorem or computation.

### Scientific value

**FAILED** — As packaged, the claim is best viewed as an expository example of a standard invariant. The pair-specific 2-torsion argument and small orbit-count table do not add enough mathematical substance beyond known general representation theorems and textbook properties of the two automorphism groups to support a research finding.

## Independent checks

- proved directly that any finite-order increasing automorphism of a linear order is the identity
- checked a transposition is an automorphism of every infinite pure set
- reran the Bell/Fubini recurrences conceptually against the committed artifacts/orbit_counts.py values
- compared the claim with standard topological Galois representations of atomic two-valued toposes and the published Schanuel-to-continuous-actions description
- confirmed main has no changes under this record since the inventory commit

## Limitations

- The correctness failure is not mathematical; the rejection is on originality and scientific value.
- Open-access sources were sufficient; Oxford Download was not needed.

## Citations

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/13/070
- https://arxiv.org/abs/1301.0300
- https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.70430
