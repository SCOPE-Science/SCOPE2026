# Self-review

## Correctness — PASS

**Claim checked:** The canonical inclusion of the wedge of the factor length-filtered enriched nerves into the enriched nerve of a finite strict one-point directed metric gluing is a realization homotopy equivalence at every cutoff. The proof explicitly pairs mixed nondegenerate tuples by inserting/deleting the marked point at the first factor switch. This insertion has exactly zero length cost by the cross-distance definition, and each upper cell has its lower partner as a unique regular face. In any directed alternating matching cycle, an unmatched descent to another matched lower cell would remove a nonbasepoint, strictly decreasing a nonnegative integer, which is impossible on a loop. The minimum positive directed off-diagonal distance bounds cell dimension at each cutoff. These facts establish a finite relative acyclic matching with critical cells exactly the factor wedge. Naturality, homology splitting, and vanishing cross-cup products follow from the levelwise inclusion. The package checker reconstructs the pairing and full directed incidence graph from its own code, passing 76 instances and 2521 cells. This is a proof for all stated finite spaces, not an extrapolation from tests.

## Originality — PASS, subject to priority risk

**Closest results and statement-level comparisons:** Bi–Feng–Li–Wu, arXiv:2601.03685v1, concerns fixed-length magnitude homology applied to an externally filtered *family of spaces*; its notion of persistence is distinct from length-cutoff blurred magnitude. Ivanov–Xu, arXiv:2411.01857, identifies the ordered \(\ell_1\)-Vietoris–Rips simplicial set with blurred magnitude and establishes filtered-colimit and other general results but does not assert homotopy preservation for finite metric pushouts. Adamaszek et al., SoCG 2018, show a metric-gluing wedge theorem for unordered diameter-controlled Vietoris–Rips and Čech complexes, not ordered sum-of-length simplicial sets. Roff's discussion of fixed-length magnitude-homology Mayer–Vietoris and Livernet–Roff–Whitehouse's pagewise spectral-sequence Mayer–Vietoris do not imply a simultaneous realization-level collapse for the filtered ordered-path nerve. Searches of a public semantic research index found no statement covering the same objects and map. This is not a uniqueness proof. An unindexed stronger simplicial-set gluing theorem remains a residual risk.

## Mathematical value — PASS

The result settles a natural compositional question for the full filtered homotopy types of blurred-magnitude nerves and gives a constructive collapse for every finite strict metric cut-vertex gluing, even with asymmetric distances. It allows integral persistence and positive-degree multiplicative structure to be calculated factorwise; the two-four-cycle example has nontrivial positive-degree groups at successive scales, so this is not merely a connectedness observation. The length-preserving matching is needed to make the answer valid simultaneously at all cutoffs, a feature unavailable from the ordinary Vietoris–Rips wedge theorem. Scope and the distinct persistence conventions are explicitly disclosed.

## Residual limitations

The conclusion is not claimed for non-strict or infinite spaces, general gluing subspaces, arbitrary shortcut distances, or other \(\ell_p\) parameter values. The finite checks are not an infinite certificate. Searches cannot establish absolute publication priority. The review concerns the present mathematical statement only.

Self-review: passed. Independent audit: not yet performed.
