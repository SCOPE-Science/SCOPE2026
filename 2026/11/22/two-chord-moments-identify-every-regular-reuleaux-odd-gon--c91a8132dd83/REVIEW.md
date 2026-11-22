# Scientific review

**Correctness: PASS.** The proof parametrizes each circular arc, computes two radial moments, invokes the independent-pair covariance identity, and establishes strict moment-ratio ordering with two analytic monotonicity arguments. The derivative inequality is proved for the whole parameter interval, and the quartic and sextic coefficients follow from convergent Taylor expansions. The accompanying standard-library checker directly integrates boundary pairs and supports, but does not replace, the all-orders proof.

**Originality: PASS, with qualification.** The 2023 disk-polygon paper concerns perimeter and area approximation. The closely related published regular-Reuleaux boundary-chord result identifies the arc count using near-diameter tail events, not two low moments; the published Reuleaux polar-inertia calculation integrates over the interior, not the boundary. The present low-moment injectivity and quartic inverse degeneration are not direct consequences of these claims. Searches did not uncover an indexed equivalent; a classical unindexed identity remains a priority risk.

**Mathematical value: PASS.** Regular Reuleaux odd-gons are the canonical curved-polygon family connecting the area-minimizing Reuleaux triangle with the circle. Exact distance-only recognition using just two low moments is a natural geometric-tomography invariant, and strict injectivity plus quartic ill-conditioning identifies precisely what those measurements can and cannot recover. This concerns all odd side counts, not an arbitrarily chosen numerical case.

The inverse conclusion is restricted to this known shape family and assumes exact arclength-uniform sampling. No broader uniqueness or statistical finite-sample guarantee is claimed. See `RESULT.md` for analytic details and bibliographic comparisons.

Self-review: passed. Independent audit: not yet performed.
