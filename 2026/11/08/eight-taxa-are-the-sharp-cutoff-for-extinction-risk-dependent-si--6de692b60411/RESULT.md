# Eight taxa are the sharp cutoff for extinction-risk-dependent single-species phylogenetic rescue

## Finding

**Theorem.** Let \(T\) be any finite rooted, non-plane, full binary phylogenetic tree having \(2\le n\le7\) leaves and unit length on every edge. Initially each taxon survives independently with the same probability \(p\in(0,1)\). One taxon can be protected completely, increasing its survival probability to one without affecting the others. There is a leaf of \(T\) whose protection maximizes expected rooted phylogenetic diversity for **every** \(p\in(0,1)\).

The leaf-count bound is sharp: at eight leaves, the tree with Newick shape `((((a,b),(c,d)),e),((f,g),h));` has no universally optimal protected taxon. Put \(q=1-p\). The taxon gains for the two competing groups are
\[
G_{a,b,c,d}(q)=q+q^2+q^4+q^5,\qquad G_{f,g}(q)=q+q^2+q^3.
\]
Their exact difference is \(q^3(q^2+q-1)\). Thus protection of one of \(a,b,c,d\) is optimal for \(0<p<(3-\sqrt5)/2\), whereas protection of \(f\) or \(g\) is optimal for \((3-\sqrt5)/2<p<1\); both groups tie exactly at \(p=(3-\sqrt5)/2\). The other two leaves are never optimal in the open range. In the degenerate one-leaf tree the unique taxon is automatically optimal.

## Assumptions and scope

Rooted phylogenetic diversity of a surviving taxon set \(S\) is the sum of the lengths of all edges on paths from the root to at least one leaf of \(S\). All \(2n-2\) tree edges have length one, including pendant edges. There is no additional stem edge above the root. Every internal node has exactly two children; child order and taxon labels do not affect the small-tree classification. Survival events of distinct unprotected taxa are independent, identically distributed Bernoulli events. The only allowed intervention fully saves exactly one taxon; every taxon has the same intervention cost. The claim concerns the **optimal identity**, not the magnitude of expected diversity, and is not asserted for heterogeneous edge lengths, unequal risks, multiple simultaneous interventions, unresolved trees, or a clock-constrained (ultrametric) tree class.

## Proof

**1. Exact objective.** For every rooted edge \(e\), let \(C_e\) be the descendants of its child endpoint and let \(s_e=|C_e|\). Its contribution to baseline expected rooted PD is \(1-q^{s_e}\). Protecting leaf \(x\) forces the presence of an edge exactly when \(e\) lies on the root-to-\(x\) path. Hence its gain in expected PD, with no normalization omitted, is
\[
G_x(q)=\sum_{e\in P_T(x)}q^{s_e}.
\]
For a leaf \(x\), form its **ascending clade-size profile** \(\sigma_x=(s_1,\ldots,s_d)\), where the descendant counts on its root path are listed increasingly (from pendant edge toward the root). Then \(G_x(q)=\sum_{i=1}^{d}q^{s_i}\). The entries increase strictly, begin at one, and end below \(n\).

**2. Structural dominance.** If \(\sigma_x\) has at least as many entries as \(\sigma_y\), and its first \(|\sigma_y|\) entries are componentwise no larger than those of \(\sigma_y\), then \(G_x(q)\ge G_y(q)\) for every \(0<q<1\). This follows term by term because \(q^t\) decreases with exponent \(t\), and every extra profile term is positive. Consequently, a leaf whose profile dominates all others is an optimum for the entire probability interval.

**3. Complete small-tree certificate.** Let \(\mathcal U_1\) consist of the single leaf. Recursively construct \(\mathcal U_n\) by attaching unordered pairs \((A,B)\), with \(A\in\mathcal U_j\), \(B\in\mathcal U_{n-j}\), for every \(1\le j<n\), and discard duplicate unordered root shapes by canonical ordering. Every rooted non-plane full binary tree is in this collection by decomposing at its root. Exact enumeration gives \(|\mathcal U_n|=1,1,1,2,3,6,11\) for \(n=1,\ldots,7\). The file `SHAPE_CERTIFICATE.tsv` displays all \(24\) shapes with \(2\le n\le7\), each in anonymous Newick notation and accompanied by an **actual leaf profile** dominating every profile in that shape. The standalone `verify.py` regenerates the complete shape family and checks each displayed witness profile against every leaf. For an independent completeness control, it separately generates all labeled rooted binary trees: \(1,1,3,15,105,945,10395\) for \(n=1,\ldots,7\); every one independently has a profile that dominates the profiles of all its leaves. Thus the structural dominance result proves a single globally optimal leaf exists for every \(2\le n\le7\), not just at sampled probabilities.

**4. Sharp eight-leaf witness.** The Newick tree has five leaves in the left rooted subtree and three in the right. The respective profile multiset, in the order above, is
\[
\{(1,2,4,5)^{\times4},\;(1,5),\;(1,2,3)^{\times2},\;(1,3)\}.
\]
The profile \((1,5)\) is strictly dominated by \((1,2,4,5)\), and \((1,3)\) by \((1,2,3)\). Comparing the other two possible maxima yields
\[
G_{a}(q)-G_f(q)=q^4+q^5-q^3=q^3(q^2+q-1).
\]
Since \(q^2+q-1\) is strictly increasing on \((0,1)\), with unique zero \((\sqrt5-1)/2\), there is exactly one optimal-group switch and no leaf is optimal for the whole interval. Translating \(q=1-p\) gives the stated threshold. This eight-leaf obstruction and the complete seven-leaf certificate prove sharpness.

## Verification

Run `python3 verify.py` beside `SHAPE_CERTIFICATE.tsv`. It needs only the Python standard library. The checker computes the unlabelled-shape recurrence, checks every componentwise dominance assertion and the exact certificate table, and *independently* enumerates all labeled rooted binary trees through seven leaves. For the eight-leaf witness, it checks profiles and exact rational gains at \(q=1/4\) and \(q=3/4\); it separately enumerates all \(2^7\) survival outcomes for the seven unprotected taxa to recompute expected PD and gain for each of eight possible protected taxa. These finite enumerations are exhaustive because the recursive generator covers every rooted binary split; the continuum of probabilities is handled symbolically by dominance and the factored polynomial, not by sampling.

## Relationship to prior work

Hartmann and Steel (2006) establish the Noah's Ark optimization framework and its expected-PD expression. Steel, Mimoto, and Mooers (2007, Theorem 3.1) give the general HED marginal-diversity formula; their corresponding HEDGE value and the fixed-risk prioritization problem encompass the present objective at a fixed \(p\). Faller, Pardi, and Steel (2008) study distributions of future PD, and Billionnet (2022) studies how miscalibration of extinction probabilities affects multi-species prioritization. The distinct result proved here is the **exact topology-only minimum of eight leaves for failure of a universally optimal single protected taxon** under unit lengths and a common varying survival probability. No priority or authorship claim is made for the classical expected-PD or HED formulas.

## Limitations

The equal-unit-edge, full-binary, independent-equal-risk conditions are mathematically substantive and are not a claim about realistic phylogenetic timescales, molecular clocks, empirical extinction risks, varying costs, or protection of more than one species. Complete enumeration is provided only through seven leaves; no characterization is asserted for every larger topology. The result has not undergone independent external audit. The exact minimum and finite certificate were not found in the inspected literature, but unseen priority results remain possible, especially in specialist phylogenetic distinctiveness literature; one related 2007 optimization paper was accessible only by abstract. A failed literature search is not a proof of novelty.

## References

- Hartmann, K. and Steel, M. (2006), *Maximizing Phylogenetic Diversity in Biodiversity Conservation: Greedy Solutions to the Noah's Ark Problem*, Systematic Biology 55, 644–651. https://doi.org/10.1080/10635150600873876 (first publication verified 2006-08-01).
- Steel, M., Mimoto, A. and Mooers, A. Ø. (2007), *Hedging Our Bets: The Expected Contribution of Species to Future Phylogenetic Diversity*, Evolutionary Bioinformatics 3. https://doi.org/10.1177/117693430700300024
- Faller, B., Pardi, F. and Steel, M. (2008), *Distribution of phylogenetic diversity under random extinction*, Journal of Theoretical Biology 251, 286–296. https://doi.org/10.1016/j.jtbi.2007.11.034
- Billionnet, A. (2022), *Quantifying extinction probabilities of endangered species for phylogenetic conservation prioritization may not be as sensitive as might be feared*, arXiv:2203.12278. https://arxiv.org/abs/2203.12278
- Pardi, F. and Goldman, N. (2007), *Resource-aware taxon selection for maximizing phylogenetic diversity*, Systematic Biology 56, 431–444. https://doi.org/10.1080/10635150701411279 (abstract consulted; full text not verified).
