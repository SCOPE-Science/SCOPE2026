# Fibonacci Fourier rank of permutation descent patterns

## Finding

Let \(n\ge2\), \(G_n=(\mathbb F_2)^{n-1}\), and \(f_n:G_n\to\mathbb Z_{\ge0}\) count permutations \(\pi\in S_n\) having descent pattern \(b_i=\mathbf1_{\{\pi_i>\pi_{i+1}\}}\), \(1\le i<n\). Define unnormalized convolution by \((T_nu)(x)=\sum_{y\in G_n} f_n(y)u(x-y)\). For each frequency \(S\subseteq\{1,\ldots,n-1\}\), let \(\mathcal R(S)\) denote its maximal nonempty intervals of consecutive indices; each interval \(R\) has length \(\ell(R)\). Write \(A_m(t)=\sum_{\pi\in S_m}t^{\operatorname{des}(\pi)}\) for the Eulerian polynomial, and \(E_{2r+1}>0\) for the alternating-permutation (tangent) number, defined by \(\tan z=\sum_{r\ge0}E_{2r+1}z^{2r+1}/(2r+1)!\).

Every unnormalized Walsh multiplier of \(T_n\) is
\[
\widehat f_n(S)=n!\prod_{R\in\mathcal R(S)}\frac{A_{\ell(R)+1}(-1)}{(\ell(R)+1)!}.
\]
The empty product is one. Moreover, \(A_{2r}(-1)=0\) for \(r\ge1\) and \(A_{2r+1}(-1)=(-1)^rE_{2r+1}\). Thus **the multiplier is nonzero exactly when every maximal run of selected positions has even length**. At those frequencies it equals
\[
\widehat f_n(S)=n!\prod_{R\in\mathcal R(S)}(-1)^{\ell(R)/2}\frac{E_{\ell(R)+1}}{(\ell(R)+1)!}.
\]
With Fibonacci numbers \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\), the exact Fourier support and convolution rank satisfy
\[
\operatorname{rank}(T_n)=F_n,\qquad \operatorname{nullity}(T_n)=2^{n-1}-F_n.
\]
The maximal singular value is \(n!\), and the recoverable fraction is \(F_n/2^{n-1}\sim (2/\sqrt5)(\varphi/2)^n\), where \(\varphi=(1+\sqrt5)/2\).

## Assumptions and scope

The permutation is a uniformly weighted member of the full symmetric group; the mask counts *descent positions*, not permutation-matrix entries and not only the indicator of an admissible pattern. The domain has \(2^{n-1}\) elements. Fourier transform means \(\widehat f_n(S)=\sum_{b\in G_n}f_n(b)(-1)^{\sum_{i\in S}b_i}\). The convolution counting measure is unnormalized. The theorem covers all integers \(n\ge2\) and all frequencies, including the empty set and adjacent boundary positions.

## Proof

1. Let \(X_1,\ldots,X_n\) be independent continuous identically distributed random variables, with no ties. Their relative rank permutation is uniform on \(S_n\), and their comparison signs realize the descent-pattern distribution. For a run \(R=\{i,\ldots,i+\ell-1\}\), the product \(\prod_{j\in R}(-1)^{\mathbf1_{X_j>X_{j+1}}}\) depends only on the \(\ell+1\) variables \(X_i,\ldots,X_{i+\ell}\). Distinct maximal selected runs have at least one *unselected* position between them, so their respective variable blocks are disjoint. These block-products are independent. Since relative ranks within a block are uniform, the expected sign product of its \(\ell\) comparisons is \(A_{\ell+1}(-1)/(\ell+1)!\). Taking expectations and multiplying by the total number \(n!\) of permutations proves the first formula, including the empty case.

2. The classical exponential Eulerian generating identity, specialized at \(t=-1\), is \(\sum_{m\ge0}A_m(-1)z^m/m!=1+\tanh z\). In particular, all even coefficients at positive degree vanish, while the odd coefficients are signed tangent numbers, \(A_{2r+1}(-1)=(-1)^rE_{2r+1}\). The positive integers \(E_{2r+1}\) count alternating permutations, so no other factor vanishes. This gives the exact zero characterization and the signed product formula.

3. Let \(a_m\) count binary strings of length \(m\) for which every maximal run of ones has even length. The empty string and the one-bit zero string give \(a_0=a_1=1\). For \(m\ge2\), such a word either starts with zero, followed by an admissible word of length \(m-1\), or starts with two ones, followed by an admissible word of length \(m-2\). Removing or restoring an initial pair preserves the even-run property, even if it joins another initial run. This is a bijection, hence \(a_m=a_{m-1}+a_{m-2}\), yielding \(a_m=F_{m+1}\). The nonzero frequency masks have length \(n-1\), so their number is \(F_n\).

4. Characters diagonalize unnormalized additive convolution on \(G_n\); the rank is the number of nonzero multipliers, proving the rank and nullity formulas. All multipliers are signed sums of \(n!\) unit phases, so their absolute values are at most \(n!\); equality holds at the empty frequency. The final asymptotic follows from Binet's formula.

## Verification

Run `python3 verify_descents.py` with Python 3 (standard library). The checker independently enumerates every permutation for \(2\le n\le9\), constructs its descent-pattern histogram, applies an integer Walsh–Hadamard transform, and compares every resulting multiplier with the factorization obtained from separately enumerated signed Eulerian sums. It also verifies each zero mask and the Fibonacci rank. This gives 510 exact coefficient comparisons across eight sizes. It does not replace the all-\(n\) proof.

## Relationship to prior work

The descent and alternating-run statistics and their algebraic structure are classical; Josuat-Vergès and Pang (2016 preprint, revised 2018) study subalgebras based on alternating runs and descent sets, rather than the Boolean convolution spectrum of the *entire position-labelled descent histogram*. An earlier low-degree Fourier classification for all permutation pair-order variables covers particular path frequency graphs with at most four edges (including individual factors \(-1/3\), \(2/15\) and \(1/9\)); the present result does not claim those individual coefficients as novel. It determines all path-frequency orders and the exact Fibonacci support and nullity for the descent-pattern marginal. Standard Eulerian generating functions supply the local signed factor but not, by themselves, the all-frequency convolution theorem without the block factorization and run count.

## Limitations

The result applies to uniform permutations and ordinary adjacent descents. It does not classify general inversion-graph frequency supports, permutations under nonuniform measures, cyclic descents, conditional descent ensembles, or noise-amplification condition numbers on the recoverable subspace. Published priority cannot be guaranteed: an older, unindexed signed-descent correlation formula may imply the full statement.

## References

1. M. Josuat-Vergès and C. Y. Amy Pang, *Subalgebras of Solomon's descent algebra based on alternating runs*, arXiv:1609.04393, initial public version 2016-09-14, https://arxiv.org/abs/1609.04393 .
2. Classical Eulerian polynomial exponential generating identity and André's tangent-number interpretation of alternating permutations (used as established input, with all relevant normalizations stated above).
