# Independent Audit — 2026-09-29

**Record:** `2026/09/12/050`  
**Title:** Wild mod-3 DW gluing boundary at Q(sqrt(-3)): disproof (1 vs 1/3)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `5ce9684c2e6ccf75308250891efd0a406515062a`  
**Disposition:** **FAILED**

## Independent checks

- Checked the special fiber of μ3 in characteristic 3 against the Stacks Project and compared it to the constant finite étale group scheme.
- Compared the gauge-group conventions and invertibility scope against the HKM primary source.
- Traced the three-class full-ring count to Kummer H^1 for μ3 and verified that this is the exact point where the gauge theory changes.

## Three-axis assessment

- **Correctness — FAIL**: The headline comparison changes the gauge group at the wild prime. The record asserts that the fppf sheaves constant Z/3 and μ3 are identified because ζ3 is a global unit. That is false on the characteristic-3 special fiber: μ3 is nonreduced and not étale, whereas the constant group scheme Z/3 is finite étale. Consequently the three Kummer classes in H^1_fppf(X,μ3) are μ3-torsors, not torsors for the constant finite gauge group G=Z/3 used by Hirano–Kim–Morishita. For the constant Z/3 gauge group on the class-number-one full ring there is no corresponding pair of extra flat torsors. Thus Z_full=1 and Z_pred=1/3 are not values of the same theory, and the claimed disproof does not follow.
- **Originality — NOT_REACHED**: A priority judgment cannot rescue a mathematically invalid headline. The wild-boundary question is interesting, but the submitted witness fails before originality can be credited because it conflates two nonisomorphic group schemes exactly at the prime where 3 is not invertible.
- **Scientific Value — FAIL**: The unit, class-number, and ramification calculations may be useful ingredients, but the record’s central 2/3 “wild mass gap” is an artifact of replacing constant Z/3 by μ3. As filed it would misstate the scope of arithmetic Dijkgraaf–Witten gluing rather than establish a valid counterexample.

## Findings

- The current main tree equals the assigned source-tree SHA; no stale-tree issue was found.
- At the residue characteristic 3 fiber, μ3=Spec(k[T]/((T−1)^3)) is nonreduced, so it cannot be isomorphic to the constant étale group scheme Z/3.
- The Kummer computation H^1_fppf(X,μ3)=O_K^*/(O_K^*)^3 therefore computes torsors for a different group scheme from the finite constant gauge group in HKM.
- The fatal mismatch occurs precisely at the wild prime, so it is not a harmless choice of coefficients or normalization.

## Sources compared

- Stacks Project, Section 101.35 (étale morphisms): https://stacks.math.columbia.edu/tag/0CIK — Uses μ_p in characteristic p as a nonreduced group scheme and notes the resulting map is not étale; this distinguishes μ3 from the constant étale Z/3 group scheme on the special fiber.
- Hirano–Kim–Morishita, On arithmetic Dijkgraaf–Witten theory: https://arxiv.org/abs/2106.02308 — Sets up arithmetic Chern–Simons/DW theory with a finite gauge group G and removes primes dividing N in the gluing formalism; it does not identify constant G=Z/3 with μ3 at residue characteristic 3.

## Limitations

- This audit does not claim that no coherent flat group-scheme version of arithmetic DW theory can be defined; it finds that the filed record has not supplied one that makes its two sides comparable.
- The algebraic facts about O_K units, class number, and μ3-Kummer torsors were not rejected; only their use as constant-Z/3 gauge fields is invalid.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
