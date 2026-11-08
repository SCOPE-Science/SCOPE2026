# Review of the exact bipartite distance-tail theorem

## Correctness
PASS. A prescribed path in \(K_{a,b}\) occurs in a uniform spanning tree with probability \((ar_B+br_A-r_Ar_B)/(a^{r_B}b^{r_A})\), where \(r_A,r_B\) count vertices of the path on each side. Contracting the path and using the weighted matrix-tree theorem establishes this, including degenerate one-part-size cases. Enumerating all simple paths between marked vertices and taking consecutive differences of the falling-factorial products yields the complete finite distance distribution. Log expansions of the products give the stated Rayleigh scaling under \(\min(a,b)\to\infty\). The independent checker passed 83,789 exact assertions on the actual scientific formulas. Computational checks complement rather than replace the proof.

## Originality
PASS with historical qualification. The 1993 Burton–Pemantle transfer-impedance theorem applies to any edge set and could imply the specialized path probabilities after a nontrivial determinant evaluation, but the inspected primary text concerns generic inclusion determinants, not the displayed \(K_{a,b}\) two-point distance law. Alappattu–Pitman (2006) derive complete-graph path-length birthday identities rather than the alternating two-part law. Archer–Shalev (2024) proves broad asymptotic UST scaling and mentions \(K_{2n/3,n/3}\), but does not give the exact finite distance tails, and the Rayleigh limit is not asserted as wholly new. Searches for exact/alias complete-bipartite UST distance laws, loop-erased path lengths, and tables did not locate direct coverage. Priority remains vulnerable to unlocated path-length specializations of general spanning-tree results.

## Value
PASS. Marked distance is a canonical intrinsic metric observable of uniform spanning trees, and the exact probability that it exceeds a given length is useful for finite-graph metric quantiles and benchmarks for loop-erased random walk. The two different endpoint-part geometries have distinct elementary product laws, both valid in the strongly unbalanced regime where standard dense-graph CRT theorems do not provide comparable all-size formulas. The result supplies exact finite data and a unified two-point scaling consequence; it does not claim a new general CRT theorem.

## Limits and related work
Primary comparisons: Burton–Pemantle, *Annals of Probability* 21 (1993), https://arxiv.org/abs/math/0404048; Alappattu–Pitman, https://arxiv.org/abs/math/0611775 (2006); Archer–Shalev, https://doi.org/10.1002/rsa.21213 (2024). Possible earlier specialized formulas and the generic implication of transfer-impedance determinants remain the main provenance uncertainties. The result is about one marked pair in a uniformly chosen spanning tree, not a minimum spanning tree.

Self-review: passed. Independent audit: not yet performed.
