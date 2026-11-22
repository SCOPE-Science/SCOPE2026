# Exact one-deletion sphere spectrum and Gaussian law for layered permutations

## Finding

Let \(\mathcal L_n=\operatorname{Av}_n(231,312)\) denote the layered permutations of length \(n\). A permutation-invariant deletion (PID) removes exactly one entry and replaces the remaining entries with their relative ranks. Let \(V(\pi)\) be the cardinality of the set of distinct outputs, rather than the number of deletion positions. The spectrum of \(V\) across this entire permutation class has the exact bivariate generating function
\[
\sum_{n\ge1} z^n\sum_{\pi\in\mathcal L_n}u^{V(\pi)}
=\frac{uz+u(u-1)z^3}{(1-z)^2-uz^2(1-z)-u^2z^3}.
\]
Thus the exact probability \(\Pr(V(\Pi_n)=j)\) for uniform \(\Pi_n\in\mathcal L_n\) is \(2^{1-n}[z^n u^j]\) times the displayed rational function.

For every \(n\ge1\), the attainable values are **exactly**
\[
1,2,\ldots,\left\lfloor\frac{2n+1}{3}\right\rfloor.
\]
The number of maximum-volume permutations for \(n=3k+r\), \(r\in\{0,1,2\}\), is
\[
\begin{cases}
k+1,&r=0\ (k\ge1),\\
1,&r=1,\\
2k+1+\binom{k+2}{2},&r=2.
\end{cases}
\]
For \(n\ge2\), exactly two layered permutations have volume one: the increasing and decreasing permutations; for \(n=1\) these coincide.

For uniform \(\Pi_n\in\mathcal L_n\),
\[
\mathbb E V(\Pi_n)=\frac{3(n+1)}8 \quad (n\ge3),\qquad
\operatorname{Var}(V(\Pi_n))=\frac{7(n-1)}{64} \quad(n\ge5).
\]
The exceptional small cases are \(\mathbb E V(\Pi_1)=\mathbb E V(\Pi_2)=1\), and the variances for lengths \(1,2,3,4\) are respectively \(0,0,1/4,23/64\). Finally,
\[
\frac{V(\Pi_n)-3(n+1)/8}{\sqrt{7n}/8}
\xrightarrow{\mathrm d}\mathcal N(0,1).
\]

## Assumptions and scope

The input is any layered permutation, equivalently any permutation avoiding both classical patterns \(231\) and \(312\). Every such permutation is uniquely a direct sum of decreasing blocks with positive integer sizes \((b_1,\ldots,b_m)\) summing to \(n\). The source distribution is uniform over the \(2^{n-1}\) choices of composition. The channel standardizes values **after** deleting one coordinate; no absolute labels are supplied to the receiver. All enumerations distinguish permutations, not deletion choices. All formulas cover arbitrary positive lengths, subject only to the stated small-case restrictions on moment formulas.

## Proof

**1. Output equivalence and layers.** Homberger's deletion/bond theorem [2, Theorem 6] proves for every permutation that the number of distinct standardized single-deletion descendants is its length minus the number of adjacent pairs with consecutive values. In a layered permutation, a block of size \(b_i\) contributes exactly \(b_i-1\) such bonds. At the boundary between consecutive blocks the value difference is \(b_i+b_{i+1}-1\), so that boundary is a bond if and only if both blocks are singletons. Consequently
\[
V(\pi)=m-\sum_{i=1}^{m-1}{\boldsymbol 1}\{b_i=b_{i+1}=1\}.
\]
Merge each maximal consecutive run of singleton blocks into one *singleton-run component*, retaining every nonsingleton block as its own *long component*. This gives a unique ordered component representation, with no adjacent singleton-run components, and \(V(\pi)\) equals exactly its number of components.

**2. Complete generating function.** The length generating functions for one singleton-run component and for one long component, each marked by \(u\), are respectively
\[
A(z,u)=\frac{uz}{1-z},\qquad B(z,u)=\frac{uz^2}{1-z}.
\]
Let \(F_A\) and \(F_B\) count nonempty component sequences ending in the respective types. The forbidden adjacency of two singleton-run components gives
\[
F_A=A(1+F_B),\qquad F_B=B(1+F_A+F_B).
\]
Solving and substituting yields
\[
F_A+F_B=\frac{A+B+AB}{1-B-AB}
=\frac{uz+u(u-1)z^3}{(1-z)^2-uz^2(1-z)-u^2z^3}.
\]
Each composition has a unique component representation, proving the exact coefficient law for every length and volume.

**3. Sharp support and extremal multiplicities.** In a component sequence of length \(j\) at least \(\lfloor j/2\rfloor\) components must be long: singleton-run components cannot touch. Thus its total underlying permutation length is at least \(j+\lfloor j/2\rfloor\). Alternating singleton-run and length-two long components attain this bound, giving \(j\le\lfloor(2n+1)/3\rfloor\). Conversely, for every \(j\) satisfying this inequality, construct a minimum-length sequence with \(j\) components and lengthen one of its long components; when \(j=1\), use a single singleton-run. Hence every intermediate volume occurs.

To count the maximum, write \(n=3k+r\). When \(r=0\), there are \(k\) long and \(k\) singleton-run components, all of minimum sizes; placing nonadjacent singleton runs has \(k+1\) choices. When \(r=1\), the unique minimum sequence has \(k+1\) singleton runs alternating with \(k\) long components. When \(r=2\), either add one unit of length to one of the \(2k+1\) components of that alternating sequence, or use \(k+1\) minimum-sized long components and \(k\) singleton-run components, admitting \(\binom{k+2}{2}\) placements. These cases are exhaustive and disjoint. Volume one corresponds to a single long block or a single all-singleton run, giving the two monotone permutations for \(n\ge2\).

**4. Exact moments.** Let \(X_1,\ldots,X_{n-1}\) be independent fair Bernoulli indicators of cuts between consecutive positions, and set boundary indicators \(X_0=X_n=1\). The formula from Step 1 is precisely
\[
V(\Pi_n)=1+\sum_{i=1}^{n-1}Y_i,\qquad
Y_i=X_i(1-X_{i-1}X_{i+1}).
\]
For \(n\ge3\), the two boundary summands have mean \(1/4\), while the \(n-3\) interior summands have mean \(3/8\). This proves the stated expectation. For distinct interior summands, their variance and covariances at distances one and two are
\[
\operatorname{Var}(Y_i)=\frac{15}{64},\quad
\operatorname{Cov}(Y_i,Y_{i+1})=-\frac5{64},\quad
\operatorname{Cov}(Y_i,Y_{i+2})=\frac1{64},
\]
with zero covariance at greater distances. The two boundary variances are each \(3/16\); the two adjacent boundary/interior covariances are each \(-3/32\); and the two distance-two boundary/interior covariances are each \(1/32\) when \(n\ge5\). Adding these contributions gives exactly \(7(n-1)/64\). The lengths below five follow from direct expansion of the rational generating function.

**5. Limit law.** The interior \(Y_i\) are a bounded, stationary, two-dependent process with covariance sum
\[
\frac{15}{64}+2\left(-\frac5{64}+\frac1{64}\right)=\frac7{64}>0.
\]
Separate the interior into blocks of length \(\lfloor n^{1/3}\rfloor\), placing two unused coordinates between blocks. The block sums are independent, uniformly bounded by the block length, and thus satisfy the Lindeberg condition after \(\sqrt n\) normalization. The omitted terms have total variance \(o(n)\) by two-dependence, and the two boundary terms are bounded. The independent-block central limit theorem and the exact variance coefficient yield the displayed Gaussian convergence.

## Verification

The standalone program `verify_direct.py` enumerates all layered permutations through length twelve, directly standardizes the output of each deletion, and compares the resulting cardinalities with the component identity, predicted support, extremal counts, and moments. It does not use the general bond formula for its deletion oracle.

The independent program `verify_distribution.py` compares (a) a structural dynamic program over long blocks and maximal runs of singleton layers with (b) direct coefficient extraction from the rational generating-function recurrence through length thirty. It separately checks total counts, all extrema, the mean and the variance. The accompanying text files record the actual outputs. These finite verifications are cross-checks only; Steps 1–5 provide all-length arguments.

## Relationship to prior work

The September 29, 2026 work of Wu, Bui, Niu, Vu and Wang [1] formalizes systematic codes under permutation-invariant deletion, where the receiver retains only relative rankings. The present result concerns the exact single-deletion output-volume law on the natural hereditary layered-permutation source, not a systematic encoder or code-distance bound.

Homberger [2] already proves \(V(\pi)=n-\#\text{bonds}(\pi)\) for arbitrary permutations and studies the unconditional distribution over the full symmetric group. That pointwise identity is used rather than claimed. Neither its unconditional generating function nor its uniform-permutation moments determines the distribution *conditioned on avoiding both* \(231\) and \(312\); this conditioned law and its sharp cutoff, counts, and Gaussian scaling are the contribution. Kabela, Král', Noel and Pierron [3] describe the established layered class and its block structure in a different, pattern-density setting.

## Limitations

The theorem counts distinct descendants for **exactly one** permutation-invariant deletion from a uniform layered source. It does not assert a code-size optimum, decoding algorithm, multiple-deletion distribution, or analogous law for a uniform unrestricted permutation. The stated formulas depend on uniformity across all layered permutations; other input distributions can give different moments and limits. Priority remains subject to further examination of any unindexed equivalent enumeration.

## References

[1] B. Wu, Q. D. Bui, K. Niu, V. K. Vu and S. Wang, *Order-Optimal Systematic Permutation Codes for Correcting t Deletions*, first public 2026-09-29, https://arxiv.org/abs/2609.37578.

[2] C. Homberger, *Counting Fixed-Length Permutation Patterns*, first public 2012-11-29, https://arxiv.org/abs/1211.7117. In particular Theorem 6 and the all-permutation distribution of Section 4.

[3] A. Kabela, D. Král', J. A. Noel and T. Pierron, *Density maximizers of layered permutations*, first public 2021-10-04, https://arxiv.org/abs/2110.01723, Section 1.
