# Comparison-shattering supports of 231-avoiding permutations form a partition matroid

## Final finding

For each integer \(n\ge1\), let \(\operatorname{Av}_n(231)\) be the permutations \(\pi\) of \([n]\) having no indices \(i<j<k\) with \(\pi(k)<\pi(i)<\pi(j)\). For every fixed position pair \(1\le i<j\le n\), let \(q_{ij}(\pi)=\mathbf 1[\pi(i)<\pi(j)]\). A set \(S\) of such binary queries is *VC-shattered* if every map \(S\to\{0,1\}\) occurs on some member of \(\operatorname{Av}_n(231)\).

**Theorem (complete support classification).** The set \(S\) is VC-shattered if and only if, for every left endpoint \(i\), at most one pair \((i,j)\) belongs to \(S\). Thus the shattered-support simplicial complex is the independence complex of a partition matroid with parts \(E_i=\{(i,j):i<j\le n\}\), \(1\le i<n\), of sizes \(n-i\). Its complete face enumerator, including the empty support, is
\[
\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}
=\prod_{j=1}^{n-1}(1+jz)
=\sum_{k=0}^{n-1}\left[{n\atop n-k}\right]z^k,
\]
where the brackets are unsigned Stirling numbers of the first kind. Consequently \(\operatorname{VCdim}=n-1\), there are \((n-1)!\) maximum supports, and there are \(n!\) shattered supports in total. For \(n=1\), the query domain is empty and \(\Phi_1(z)=1\).

## Proof

**Necessity.** Suppose \((i,j),(i,k)\in S\) with \(i<j<k\). The labeling \(q_{ij}=1\), \(q_{ik}=0\) would require \(\pi(j)>\pi(i)>\pi(k)\), a forbidden \(231\) pattern at those three positions. Thus such a support cannot be shattered. This proves the one-per-left-endpoint requirement.

**Sufficiency.** Fix a support satisfying the requirement, and any target labeling on it. Starting with an empty suffix, construct a permutation from right to left by inserting a new first entry and standardizing all entries to consecutive integers at each stage. At step \(i\), insert the new entry as a minimum if the support has no edge out of \(i\), or if the unique edge \((i,j)\) is required to have value one; otherwise insert it as a maximum. The new entry is then smaller than *every* suffix entry when required to return one, and larger than *every* suffix entry when required to return zero. Thus the prescribed query at \(i\) is realized and earlier choices cannot change it. Since the new leftmost entry is an extreme of the entries now present, it cannot be the middle-ranked first entry of a \(231\) triple. Earlier suffixes already avoided \(231\), so induction preserves avoidance. This realizes all labelings and proves the converse for every \(n\).

**Enumeration and boundary cases.** From each part \(E_i\) choose zero edges or one of its \(n-i\) edges, independently. Multiplying the corresponding terms gives \(\prod_{i=1}^{n-1}(1+(n-i)z)\). The identity \(\prod_{j=1}^{n-1}(x+j)=\sum_{r=1}^{n}\left[{n\atop r}\right]x^{r-1}\) gives the stated coefficients after homogenizing. The top degree is \(n-1\) with coefficient \((n-1)!\); substituting \(z=1\) gives \(n!\). All formulas hold at \(n=1\) under empty-product conventions.

## Scope and relationship to earlier results

This theorem classifies **all shattered comparison supports**, not merely their maximum size. The already published 2 November 2026 result *Wilf-equivalent length-three avoidance classes separate in adaptive comparison dimension* proves \(\operatorname{VCdim}=n-1\) for all length-three avoided patterns and exact finite Littlestone dimensions through \(n=8\). Its queries compare the positions of specified **symbols**, whereas the present theorem compares values at specified **positions**. Inverting a permutation exchanges the two conventions and sends avoidance of \(231\) to avoidance of \(312\). Hence the earlier finite value \(\operatorname{Ldim}=8\) at \(n=7\) applies here. Coupling that value with the elementary direct-sum closure of \(\operatorname{Av}(231)\) gives the linear lower bound \(\operatorname{Ldim}(\mathcal H_{7q})\ge8q\) and its gap \(\ge q+1\). These are **prior-covered or immediate consequences**, not independent findings of this repaired theorem.

The retained auxiliary files `depth8_tree.json` and `verify.py` encode and check one complete depth-eight witness for the covered finite online fact, and finite checks of the static profile. They are ancillary evidence and do not define the novelty claim. The present theorem makes no claim to a new Littlestone dimension or a new linear-gap construction.

Johnson and Wickes, *Shattering k-sets with Permutations* (arXiv:2112.01946; *Order* 2023), study a different notion: all \(k!\) induced orders of a chosen \(k\)-set, not all independent binary outcomes on chosen pair queries. The full public preprint's definitions and main results do not give this exact support classification. Guingona et al. (arXiv:2109.04805) concern linear zero-set classes and do not supply this restricted-permutation support polynomial. The 25 October 2026 result *Comparison shattering in 321-avoiding permutations* has a different forbidden pattern and proves the dimension and a different online gap, not this support matroid. No available inspected theorem was found implying this coefficientwise classification; historical priority under inversion-set, Dyck-path, and stack-sortable terminology remains a best-of-knowledge risk.

## Reproducible verification

The proof above is all-order and does not depend on numerical experiments. Independent finite direct enumeration of all \(231\)-avoiding permutations and all query subsets checked the complete coefficient lists through \(n=6\): \(n=3\): \((1,3,2)\), \(n=4\): \((1,6,11,6)\), \(n=5\): \((1,10,35,50,24)\), \(n=6\): \((1,15,85,225,274,120)\). The original bundled `verify.py` checks through \(n=8\), but a recorded success message alone is not proof. The independent reproduced depth-eight tree has 255 internal labels and all 256 branches nonempty against all 429 \(231\)-avoiding seven-permutations. This confirms an already-covered online fact, not new mathematical priority.

## Limitations

The classification is for the **fixed positional-comparison query domain** and the single classical forbidden pattern \(231\); variants for other avoided patterns can have different support complexes. The explicit enumerator and facet count, although proved, may have appeared in alternate Catalan, inversion-set, or shattering-complex formulations not identified in the inspected sources. Originality is a best-of-knowledge assessment, not external attestation.

## References

- *Wilf-equivalent length-three avoidance classes separate in adaptive comparison dimension* (2 November 2026).
- *Comparison shattering in 321-avoiding permutations: the first two-round gap and an unbounded separation* (25 October 2026).
- J. R. Johnson and B. Wickes, *Shattering k-sets with Permutations*, arXiv:2112.01946, *Order* (2023), DOI:10.1007/s11083-023-09637-7.
- V. Guingona, A. Kolesnikov, J. Nierwinski, R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805 (2021).
