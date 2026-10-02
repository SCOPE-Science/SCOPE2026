# Independent audit — 2026-10-01

**Record:** `SCOPE-20260911-042`

## Correctness — PASS

The uniform torsion-freeness statement is correct. The published Swiatkowski complex computes unordered graph-configuration homology, and after smoothing the theta graph has exactly two essential vertices; each local factor contributes at most one degree-one half-edge state, so the complex has no degree-three chains. Therefore H_2 is the kernel of the degree-two differential inside a free abelian group and is itself free. A fresh matrix reconstruction independently reproduced the quoted ranks: for k=4, ranks(D1,D2)=(40,53) and H_2 rank 1; for k=5, ranks=(60,87) and H_2 rank 3.

## Originality — FAIL

The final theorem is a direct corollary of the published Swiatkowski chain model, not a new graph-specific theorem under the audit standard. Definition 2.7 gives exactly one possible homological degree-one local state per vertex factor, Theorem 2.10 identifies the complex with configuration-space homology, and smoothing the theta graph leaves two essential vertices. The no-C3 argument and consequent freeness of H2 are immediate. Later published work also treats the theta graph as an atomic generator for second homology of planar graph braid groups.

### Structured originality checks

- **equivalent_formulations:** Searches: Swiatkowski complex theta graph H2; theta graph unordered configuration H2 torsion. Evidence: The chain-level formulation makes H2 a kernel in degree two because C3=0. Reasoning: This is exactly equivalent to the claimed torsion-freeness and requires no extra theorem beyond the published chain model plus smoothing.
- **broader_coverage:** Searches: On the second homology of planar graph braid groups theta; Edge stabilization graph braid groups theta. Evidence: An-Knudsen treats theta as one of the atomic graphs generating planar-graph H2 phenomena; An-Drummond-Cole-Knudsen supplies the general complex for every graph. Reasoning: The general complex strictly subsumes the claimed special case.
- **exact_database_or_table:** Searches: published-result semantic search theta H2 torsion free; small graph configuration Betti data theta. Evidence: Related published records include the same theta homology and ordered/unordered comparisons. Reasoning: Even without a verbatim torsion-free table row, the general published model mechanically implies the theorem.
- **claim_vs_prior_implication:** Searches: Definition 2.7 Theorem 2.10 Swiatkowski complex; theta graph smoothing two essential vertices. Evidence: The primary full text states the generators, degrees, differential, smoothing invariance framework, and homology computation theorem. Reasoning: Counting the two degree-one vertex factors gives C3=0 immediately, so the result is a covered corollary.

## Scientific value — PASS

The uniform no-torsion diagnosis is a useful boundary check for a proposed persistent-torsion target and correctly redirects attention to graphs with at least three essential vertices or other degrees. Its scientific value does not overcome the originality failure.

## Source inspections

- **An, Drummond-Cole, Knudsen, Edge stabilization in the homology of graph braid groups** (arXiv:1806.05585). Full HTML including Definition 2.7, smoothing discussion, and theorem-level description that the complex computes homology. Assessment: COVERS_BY_DIRECT_COROLLARY. The local factors have degree at most one and the smoothed theta has two essential vertices, so C3=0 and H2 is a subgroup of a free C2.
- **An, Knudsen, On the second homology of planar graph braid groups** (arXiv:2008.10371). Abstract and indexed full-text metadata. Assessment: BROADER_COVERAGE. Treats the theta graph as an atomic generator in planar-graph second homology, reinforcing that theta H2 is established territory.

## Residual risks

- The scientific rejection is due to direct prior implication, not an error in the theorem.
- The k=4 and k=5 matrix computations are consistency checks; the uniform freeness conclusion already follows structurally.

## Disposition

**FAILED**. The mathematical claim is retained as evidence, but it does not pass the originality requirement and is not validated as a publishable independent finding.
