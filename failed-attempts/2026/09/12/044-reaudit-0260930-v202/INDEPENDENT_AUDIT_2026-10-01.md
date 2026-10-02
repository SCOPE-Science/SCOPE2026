# Independent scientific audit — 2026-10-01

**Disposition: FAILED — not a validated finding.**

## Final claim assessed

The stated octahedron multiwedge has minimal nonfaces of sizes 2, 2, and 5 on disjoint vertex blocks, hence is a join whose moment-angle manifold is the product of spheres of dimensions 3, 3, and 9, with the listed Tor algebra and rational formality.

## Correctness — PASS

The conclusion is reconstructible without trusting the saved success text: the iterated minimal-nonface wedge rule gives, up to relabelling, three disjoint minimal nonfaces {0,1}, {2,3}, and {4,5,6,7,8}. A simplicial complex whose minimal nonfaces are exactly those three disjoint full vertex blocks is the join of the three corresponding simplex boundaries. Standard polyhedral-product identities then give Z_K = the product of spheres of dimensions 3, 3, and 9. The exterior cohomology and rational formality follow immediately; the exact Hochster/Koszul scripts are consistent with that decomposition.

## Originality — FAIL

The exact tuple was not found as a distinct prior database entry, but the scientific statement is mechanically implied by standard J-construction/minimal-nonface rules and the standard moment-angle join/product and simplex-boundary identities. Limonchenko provides the general simplicial-multiwedge framework; no new implication-independent theorem is needed once the three disjoint minimal nonfaces are obtained.

## Scientific value — FAIL

After the join decomposition is observed, the advertised manifold, Tor algebra, and formality are routine textbook consequences for a product of odd spheres. The particular multi-index is not motivated as a natural classification boundary, extremal case, or unknown invariant needed independently, so this is a worked specialization rather than a worthwhile new mathematical gap.

## Originality checks

### equivalent_formulations

The claim is equivalently a join decomposition from three disjoint minimal nonfaces; this formulation exposes that the topological conclusion is standard.

Evidence: Resultary returned this record itself as the exact match.; Limonchenko, arXiv:1711.00461, gives the general simplicial multiwedge/polyhedral-product framework.

### broader_coverage

General identities dominate the one-off parameter choice once its minimal nonfaces are known.

Evidence: General multiwedge theory covers the construction class; the standard polyhedral-product identity Z_{K*L}=Z_K x Z_L and Z_{boundary simplex}=odd sphere covers the stated consequence.

### exact_database_or_table

Absence of an exact row does not establish originality when general identities imply the row mechanically.

Evidence: No distinct prior Resultary record beyond the record under audit was returned as an exact table row.

### claim_vs_prior_implication

The final claim is a direct specialization of established general machinery, so originality fails even without an exact-number predecessor.

Evidence: The assigned code itself reduces the complex to disjoint minimal nonfaces; standard prior identities then force the claimed product of spheres.

## Sources inspected

- Topology of polyhedral products over simplicial multiwedges — https://arxiv.org/abs/1711.00461: broader construction framework; exact tuple not needed for the implication comparison
- Assigned package 2026/09/12/044 — https://github.com/SCOPE-Science/SCOPE2026/tree/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/12/044: correct join/product conclusion; novelty/value do not survive the standard reduction

## Residual risks

- No exhaustive historical search of every toric-topology table was performed; this does not affect the failure because the claim is already mechanically implied by standard general identities.
- The exact 205-triple count was not independently rerun, but it is unnecessary for the formality conclusion once the product-of-spheres decomposition is established.
