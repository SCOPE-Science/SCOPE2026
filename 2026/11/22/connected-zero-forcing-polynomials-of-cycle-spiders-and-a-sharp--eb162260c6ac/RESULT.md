# Connected zero-forcing polynomials of cycle spiders and a sharp real-root transition

## Finding

For every integer \(c\ge3\), every integer \(t\ge2\), and any positive path lengths \(p_1,\ldots,p_t\), attach \(t\) disjoint pendant paths of the prescribed lengths to one vertex \(v\) of the cycle \(C_c\). This defines the *cycle spider* \(G(c;p_1,\ldots,p_t)\). With
\[
F_c(z)=\sum_{j=1}^{c-2}(j+1)z^j+z^{c-1},\qquad H_i(z)=\sum_{j=1}^{p_i}z^j,
\]
the complete connected zero-forcing polynomial is
\[
\boxed{Z_C(G;z)=zF_c(z)\left(\prod_{i=1}^tH_i(z)+\sum_{j=1}^t\prod_{i\ne j}H_i(z)\right).}
\]
The minimum connected forcing cardinality is \(t+1\), attained by exactly \(2t\) sets; the total number of connected forcing sets is
\[
\binom c2\left(\prod_{i=1}^t p_i+\sum_{j=1}^t\prod_{i\ne j}p_i\right).
\]
For the natural subfamily with exactly one pendant path of length two and the remaining \(t-1\) pendant paths of length one,
\[
Z_C(G(c;2,1,\ldots,1);z)=z^tF_c(z)(z^2+tz+t).
\]
This polynomial has only real complex roots precisely when \(c\in\{3,4\}\) and \(t\ge4\), producing a sharp four-arm transition.

## Assumptions and scope

All graphs are finite, undirected and simple. A standard zero-forcing set is a set of initially blue vertices from which repeated applications of the rule *a blue vertex with exactly one white neighbor colors that neighbor blue* eventually color every vertex. A connected forcing set additionally induces a connected subgraph. The polynomial \(Z_C(G;z)=\sum_{S}z^{|S|}\) sums over these connected forcing sets. A pendant path of edge length \(p_i\ge1\) has \(p_i\) new vertices, with its first vertex adjacent to the common cycle vertex \(v\). The graph order is \(c+\sum_i p_i\). We require \(t\ge2\); the one-arm boundary is different because a connected forcing set need not include \(v\).

## Proof

**1. The hub belongs to every connected forcing set.** Delete \(v\). There remain \(t\) pendant-path components and one path on the other \(c-1\) cycle vertices. If a connected initial set \(S\) misses \(v\), it lies in exactly one component. Forcing may reach \(v\), but no other component has an initially blue vertex. If \(S\) is in a pendant path, the two cycle neighbors of \(v\) remain white and no force can enter the cycle. If \(S\) lies in the cycle component, at least two wholly white pendant paths remain; only \(v\) can enter them and it always has at least two white neighbors. Hence neither case forces the graph.

**2. Characterization for sets containing the hub.** Induced connectivity forces the selected vertices on each pendant path to be an initial prefix from \(v\), possibly empty, and the selected cycle vertices to form a cyclic interval containing \(v\), possibly only \(v\). If no cycle neighbor of \(v\) is initially blue, both cycle directions remain white and neither can start. If at least two pendant paths are wholly unseeded, no vertex other than \(v\) is adjacent to their first vertices, so neither can ever receive a first force. Thus a connected forcing set must select a nontrivial cycle interval and seed at least \(t-1\) pendant paths. Conversely, such a set forces: a selected cycle vertex at a boundary of the remaining white cycle arc forces along it until that arc vanishes; each seeded path's last initially blue vertex forces along its remaining white suffix; finally the common hub forces the sole possible unseeded pendant path after the cycle and other paths are blue. All forcing steps use exactly one white neighbor at the forcing vertex.

**3. Counting.** A cyclic interval containing \(v\) with exactly \(j\) other selected cycle vertices, \(1\le j\le c-2\), has exactly \(j+1\) choices, distributed between the two directions. The fully selected cycle has one choice. This gives \(F_c(z)\). Each seeded pendant path contributes one of the prefixes of lengths \(1,\ldots,p_i\), giving \(H_i(z)\). One may seed all arms or omit exactly one of the \(t\) arms. The two types are disjoint and counted by the displayed product-plus-sum expression, with an additional factor \(z\) for \(v\). For the lowest power, one selected cycle neighbor has two choices and exactly one arm is omitted, giving \(2t\) sets of size \(t+1\). Evaluating at \(z=1\), observe \(F_c(1)=\binom c2\) and \(H_i(1)=p_i\), which yields the total count.

**4. Sharp real-rootedness transition.** In the subfamily with \(p_1=2\) and \(p_2=\cdots=p_t=1\), direct expansion of the exact formula gives \(Z_C=z^tF_c(z)(z^2+tz+t)\). For \(c=3\) and \(c=4\), respectively, \(F_c(z)=z(z+2)\) and \(F_c(z)=z(z+1)(z+2)\), so these factors have only real zeros. The quadratic has discriminant \(t(t-4)\), hence has only real roots exactly for integer \(t\ge4\). For every \(c\ge5\), write \(F_c(z)=zQ_c(z)\), with \(Q_c\) of degree \(d=c-2\ge3\) and lowest three coefficients \(2,3,4\). If \(Q_c\) were real-rooted, its positive coefficients would require its roots to be negative, and Newton's inequalities for its binomially normalized coefficients would give \((3/d)^2\ge 2\cdot4/\binom d2\), equivalently \(9(d-1)\ge16d\), impossible. Therefore \(F_c\) has a nonreal root when \(c\ge5\), irrespective of \(t\). This completes both implications.

## Verification

The accompanying standalone Python program `verify.py` independently constructs the graph, enumerates all nonempty vertex subsets, checks their connectivity by reachability and standard forcing by iterative unique-white-neighbor closure, and compares every cardinality coefficient with the formula. It checks 170 instances, each having at least two pendant paths and at most 15 vertices, examining 1,301,942 nonempty subsets in total. It independently tests the minimum-set coefficient and scalar total on every instance, and the exact discriminant threshold for integers from 2 through 99. Output: `INDEPENDENT_FULL_SUBSET_CENSUS_PASS`, `SHARP_ONE_SUBDIVIDED_ARM_DISCRIMINANT_PASS`, and `VERIFY_OK`. Finite checks corroborate but do not prove the all-order statement; the above proof supplies that argument.

## Relationship to prior work

Mukherjee and Ray (arXiv:2611.10985v1, first public November 7, 2026) determine connected zero-forcing polynomials for **trees** and pose general-graph and unicyclic extension problems (Problems 5.4 and 5.2). A cycle spider is unicyclic, not a tree, and the present coefficientwise enumeration and root transition are not consequences of a tree-only theorem. Earlier ordinary zero-forcing results, including Eroh, Kang and Yi's discussion of bouquets of cycles, study a different forcing invariant or family and do not supply this connected cycle-spider polynomial. Published exact enumerators for *perfect edge domination* of one-hub cycle spiders concern a distinct edge-set property; they do not imply connected vertex zero-forcing counts. The work does not claim the connected zero-forcing invariant itself is new, nor does it claim priority over inaccessible or unindexed historical results.

## Limitations

The classification is for one cycle and all pendant paths meeting the same cycle hub, with at least two pendant paths; it does not classify arbitrary unicyclic graphs or arbitrary cacti. The real-rootedness equivalence is asserted only for the special one-subdivided-arm subfamily, not for arbitrary arm lengths. Historical novelty has not been independently certified; older sources or unindexed instances could establish overlapping formulas. Computational verification is exhaustive only for the explicitly specified finite graph instances.

## References

1. S. Mukherjee and P. Ray, *On the connected zero forcing polynomial of finite trees*, arXiv:2611.10985v1 (first posted November 7, 2026). https://arxiv.org/abs/2611.10985v1
2. L. Eroh, C. X. Kang and E. Yi, *Metric dimension and zero forcing number of two families of line graphs*, Mathematica Bohemica 139 (2014), 467–483, DOI:10.21136/MB.2014.143937. https://dml.cz/manakin/bitstream/handle/10338.dmlcz/143937/MathBohem_139-2014-3_3.pdf
