# The complete Walsh Fourier-support spectrum of eight-point binary sets

## Finding

Let \(d\geq3\), \(G=\mathbb F_2^d\), and let \(E\subset G\) have exactly eight distinct points. Define the unnormalized Walsh transform
\[
W_E(u)=\sum_{x\in E}(-1)^{u\cdot x},\qquad
s(E)=\#\{u\in G:W_E(u)\ne0\},
\]
and let \(r(E)=\dim_{\mathbb F_2}\operatorname{span}(E-E)\) be the affine dimension. Necessarily \(3\leq r(E)\leq\min(d,7)\). The **complete list**, for each possible \(r=r(E)\), is

| Affine dimension \(r\) | Possible \(s(E)/2^{d-r}\) | Counts among canonical basis-normalized configurations |
| --- | --- | --- |
| 3 | \(1\) | \(1:1\) |
| 4 | \(5,9,11\) | \(5:10,\ 9:20,\ 11:135\) |
| 5 | \(13,21,23,25\) | \(13:10,\ 21:90,\ 23:150,\ 25:75\) |
| 6 | \(29,45,49\) | \(29:1,\ 45:35,\ 49:21\) |
| 7 | \(93\) | \(93:1\) |

Every listed number is attained in every ambient dimension \(d\ge r\); the table does not claim that the third-column counts are numbers of affine-equivalence classes. For \(d\ge7\), the possible values of \(s(E)/2^{d-7}\) are exactly
\[
\{16,40,52,58,72,84,88,90,92,93,98,100\}.
\]
All twelve values are distinct, and **\(s(E)\) determines the affine dimension \(r(E)\)** for every \(d\ge3\). For \(d\ge4\), among eight-point sets that are not affine three-planes, the sharp minimum is
\[
s(E)\ge5\cdot2^{d-4}.
\]
Equality holds precisely for the single affine-equivalence class of products of a two-point affine line with a four-point affine-independent simplex. One representative in \(\mathbb F_2^4\) is
\[
\{0,e_1\}+\{0,e_2,e_3,e_4\}.
\]

## Assumptions and scope

The Fourier support counts **nonzero unnormalized complex/integer Walsh coefficients**, not Fourier-character bases, and the coefficients are of the indicator function \(\mathbf1_E\). The affine dimension is the dimension of the smallest affine space containing \(E\); it is unrelated to the span dimension of the Fourier support. All Fourier characters use the nondegenerate standard dot product. Ambient embeddings, invertible affine transformations, and changes of nondegenerate identification between the group and its dual preserve the nonzero support count. No claim is made for weighted eight-point functions, other cardinalities, or other characteristics.

## Proof

**1. Exhaustive normal form.** Translate \(E\) to contain zero and put \(r=\dim\operatorname{span}(E)\). Choose \(r\) of the other seven points as a basis of this span, and change coordinates. The set is then
\[
E=\{0,e_1,\ldots,e_r\}\cup B,
\quad B\subset\mathbb F_2^r\setminus\{0,e_1,\ldots,e_r\},
\quad |B|=7-r.
\]
Conversely, every such \(B\) gives a set of exactly eight points of affine dimension \(r\). Therefore every equivalence class occurs among exactly
\[
\binom{2^r-r-1}{7-r}
\]
possibly redundant configurations, which are \(1,165,325,57,1\) for \(r=3,4,5,6,7\), respectively. The redundancy does not affect either completeness or attainability.

**2. Exact zero criterion.** For \(u\in\mathbb F_2^r\) put
\[
q_B(u)=\operatorname{wt}(u)+\sum_{b\in B}(u\cdot b\bmod2).
\]
Precisely \(q_B(u)\) of the seven nonzero points of \(E\) evaluate to \(-1\) under the character \(u\). Thus
\[
W_E(u)=8-2q_B(u),\qquad
s_r(B)=2^r-\sum_{u\in\mathbb F_2^r}\mathbf1_{\{q_B(u)=4\}}.
\]
This identity is independent of the choice of basis and involves only integers. It is also the weight-four-count identity for the binary evaluation code of the seven nonzero points; it is not a statement about general code weight distributions.

**3. Complete finite classification.** For each \(r=3,4,5,6,7\), loop over the \(\binom{2^r-r-1}{7-r}\) subsets \(B\) from Step 1 and over all \(2^r\) dual vectors in Step 2. The complete tabulation, with each distinct value followed by its frequency among these normalized configurations, is
\[
\begin{array}{c|l}
 r & s_r(B):\text{ frequency}\\\hline
3 & 1:1\\
4 & 5:10,\ 9:20,\ 11:135\\
5 & 13:10,\ 21:90,\ 23:150,\ 25:75\\
6 & 29:1,\ 45:35,\ 49:21\\
7 & 93:1
\end{array}.
\]
The attached `CHECK.py` is a complete, dependency-free certificate for this bounded tabulation: it explicitly implements both the character sum and the independent weight-four identity, checks their equality for every configuration, compares the full histograms against the displayed table, and separately enumerates all \(\binom{16}{8}=12870\) eight-point subsets in dimension four. No floating-point threshold or statistical inference enters the proof. The loops and ranges are small and fully specified, and every eight-point set has a normal form among their inputs.

**4. Ambient lifting and rank identification.** Restriction of ambient frequencies to the affine span is surjective with fibers of size \(2^{d-r}\). Therefore \(s(E)=2^{d-r}s_r(B)\). The twelve possible integers \(2^{7-r}s_r(B)\) are
\[
\begin{array}{c|l}
3&16\\4&40,72,88\\5&52,84,92,100\\6&58,90,98\\7&93
\end{array}.
\]
No integer occurs twice, proving that the Fourier-support cardinality determines the affine dimension. All entries occur by Step 3, and exactly those with \(r\le d\) are possible in ambient dimension \(d\).

**5. Sharp nonaffine boundary and equality.** An eight-point set of affine dimension three is the entire affine three-plane. All remaining rows have normalized support at least \(5\cdot2^{d-4}\), with equality only for \(r=4\), \(s_4(B)=5\). The complete finite tabulation additionally checks that each of the ten basis-normalized \(r=4\) equality configurations has exactly two additive periods (including zero). Let \(L\) be its nontrivial one-dimensional period subspace. The quotient \(E/L\) is a four-point set in \(\mathbb F_2^3\) whose affine span has dimension three: otherwise the original set would have affine dimension at most three. Thus \(E/L\) is a four-point affine-independent simplex, proving the claimed unique affine-equivalence type. Direct character summation for \(\{0,e_1\}+\{0,e_2,e_3,e_4\}\) gives five nonzero frequencies in dimension four, completing the equality proof.

## Verification

Run `python CHECK.py` with Python 3.10 or later. The checker prints:

`CHECK_OK normalized_representatives=549 support_types=12 dimension_four_subsets=12870`

It verifies both zero-count formulas on all 549 normalized inputs, every exact distribution and its binomial total, the distinction between the twelve ambient-normalized values, period rigidity for all ten sharp nonaffine normalized inputs, and the full unrelated dimension-four subset census. The finite enumeration is exhaustive because of the basis-normalization argument in Step 1. It does not assert a theorem about arbitrary signal coefficients or arbitrary support size.

## Relationship to prior work

Ferguson and Iosevich (arXiv:2610.36417, first posted October 26, 2026) establish structural Fourier-support facts needed for the finite binary Fuglede problem. Their Lemma 3.1 uses the same zero-at-Hamming-weight-four reduction for arbitrary eight-point sets, and their Proposition 7.1 explicitly analyzes a rank-six example whose local support size is 29. Those known ingredients and the example are acknowledged. The complete rank-stratified support-cardinality spectrum and the rank-detection conclusion are additional assertions requiring classification of the permitted evaluation subspaces; the inspected Sections 3 and 7 do not supply this table.

Kadowaki (arXiv:2610.24022, first posted October 16, 2026) also uses the eight-point weight-four reduction to build universal spectra, not to classify all possible counts of nonzero coefficients. A published Boolean four-cube spectral-partner census, *Exact Walsh-spectrum multiplicities for eight-point subsets of the Boolean four-cube* (2026), determines orthogonal frequency-partner counts for ambient dimension four, a different invariant. Its rank-four strata provide closely related prior information and should not be treated as new here; the present statement concerns all affine ranks through seven and all ambient dimensions. The general Fourier-sparsity literature, including Gopalan et al. (2011), concerns testing, not this complete fixed-cardinality table in its inspected abstract. The data may also be recoverable from classical length-seven binary linear-code classifications; this is an explicit residual priority risk.

## Limitations

The result is an exact eight-point, binary-character classification. It is not a general Fourier uncertainty theorem for arbitrary functions or a general spectral/tiling classification. The tabular part rests on short, fully exhaustive integer computations and explicit normalization; it does not establish related classifications for nine or more points. Although relevant recent full texts and an indexed published comparison were inspected, a previously tabulated equivalent length-seven code weight spectrum cannot be ruled out. Independent mathematical audit has not been performed.

## References

1. S. J. Ferguson and J. Iosevich, *Fuglede's conjecture holds in eight dimensions over the field with two elements*, arXiv:2610.36417v1 (2026-10-26). https://arxiv.org/abs/2610.36417
2. A. Kadowaki, *Fuglede's conjecture holds in the seven-dimensional binary space*, arXiv:2610.24022v1 (2026-10-16). https://arxiv.org/abs/2610.24022
3. *Exact Walsh-spectrum multiplicities for eight-point subsets of the Boolean four-cube*, publicly released October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-walsh-spectrum-multiplicities-for-eight-point-subsets-of-t--b981e436a3b1
4. P. Gopalan, R. O'Donnell, R. A. Servedio, A. Shpilka, K. Wimmer, *Testing Fourier Dimensionality and Sparsity*, SIAM J. Comput. 40 (2011), 1075–1100. https://doi.org/10.1137/100785429
