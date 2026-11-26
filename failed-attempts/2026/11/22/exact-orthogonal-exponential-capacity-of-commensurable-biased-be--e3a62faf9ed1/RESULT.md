# Exact orthogonal exponential capacity of commensurable biased Bernoulli convolutions

## Finding

For any finite family of positive commensurable real lengths \(a_1,\ldots,a_m\), and arbitrary Bernoulli probabilities \(0<p_j<1\), consider the compactly supported probability measure
\[
\mu=\bigast_{j=1}^{m}\bigl((1-p_j)\delta_0+p_j\delta_{a_j}\bigr).
\]
Choose any common positive scale \(q\) with \(a_j=qn_j\), all \(n_j\) positive integers. Put
\[
S=\{\nu_2(n_j):p_j=\tfrac12\},\qquad r=|S|.
\]
Then the largest possible cardinality of a pairwise orthonormal family of exponential characters \(x\mapsto e^{2\pi i\lambda x}\) in \(L^2(\mu)\), over arbitrary real frequencies \(\lambda\), is **exactly**
\[
\boxed{\mathcal O(\mu)=2^{r}.}
\]
The count \(r\) is independent of the chosen common scale, because changing scale adds a constant to all dyadic valuations. An explicit optimal family, containing the zero frequency, is
\[
\boxed{\Lambda_* = \frac1q\left\{\sum_{s\in S}\frac{\epsilon_s}{2^{s+1}}:\epsilon_s\in\{0,1\}\right\}.}
\]
In particular, adding arbitrarily many factors at an already represented dyadic scale does not increase the maximum number of mutually orthogonal exponentials. Unbalanced Bernoulli factors contribute no additional orthogonal dimensions. A finite convolution in this family has a complete orthogonal exponential basis precisely when every factor is fair and the dyadic valuations of all the step integers are distinct. This last qualitative spectrality consequence is consistent with previously known valuation criteria; the quantitative capacity formula, including nonspectral and biased cases, is the subject here.

## Assumptions and scope

Fix an integer \(m\ge1\), positive commensurable real \(a_j\), and probabilities \(p_j\in(0,1)\). All support atoms have positive measure; repeated subset sums are combined with their weights. A set of exponentials is called *orthonormal* when the characters have norm one (automatic for a probability measure) and distinct characters have zero pairwise inner product. The supremum \(\mathcal O(\mu)\) is taken over all finite sets of real frequencies; the resulting maximum is finite. Dyadic valuation \(\nu_2(n)\) for a nonzero integer is the exponent of two dividing \(n\). The case \(S=\varnothing\) has \(\mathcal O(\mu)=1\). The conclusion concerns exact orthogonality and is not a numerical conditioning estimate for nearly orthogonal systems.

## Proof

**1. Exact Fourier zero set.** Adopt \(\widehat\mu(t)=\int e^{-2\pi itx}\,d\mu(x)\). Direct convolution gives
\[
\widehat\mu(t)=\prod_{j=1}^{m}\bigl(1-p_j+p_je^{-2\pi ita_j}\bigr).
\]
For real \(t\), the \(j\)-th factor vanishes if and only if \(p_j=1/2\) and \(t a_j\in\mathbb Z+1/2\): equality of the moduli of \(1-p_j\) and \(p_j\) forces fairness, after which the complex phase must be \(-1\). Hence, after changing frequency coordinates to \(u=qt\), the *entire* nonzero Fourier zero set is
\[
\mathcal Z=\bigcup_{\{j:p_j=1/2\}}\left\{\frac{2k+1}{2n_j}:k\in\mathbb Z\right\}.
\tag{1}
\]
For a balanced step \(n_j=2^s b_j\) with odd \(b_j\), each zero has valuation \(-s-1\). The exact progressions in (1) are generally **proper subsets** of all rationals of the corresponding valuations; the upper bound uses only the necessary valuation restriction, while the lower-bound construction checks exact divisibility and does not assume a converse.

**2. Upper bound by binary branching.** Translate an arbitrary orthogonal family of frequencies so that one frequency equals zero. Since every nonzero frequency difference must be a zero of \(\widehat\mu\), after multiplication by \(q\) all its elements are rational, and valuations of all their nonzero pairwise differences belong to the finite set
\[
K=\{-s-1:s\in S\},\qquad |K|=r.
\]
We use the following elementary binary-branching lemma: if a finite set \(A\subset\mathbb Q\) has \(\nu_2(x-y)\in K\) whenever \(x\ne y\), then \(|A|\le 2^{|K|}\). For \(K=\varnothing\) there is at most one point. Otherwise put \(k=\min K\) and fix \(x_0\in A\). Because each difference from \(x_0\) has valuation at least \(k\), all points lie in the one dyadic coset \(x_0+2^k\mathbb Z_{(2)}\), where \(\mathbb Z_{(2)}\) consists of rationals with odd denominators. Its quotient by \(2^{k+1}\mathbb Z_{(2)}\) has exactly two classes. In each class, every nonzero difference has valuation greater than \(k\) and hence belongs to \(K\setminus\{k\}\). Induction bounds each class by \(2^{r-1}\), establishing \(|A|\le2^r\). Applying the lemma to the frequency family proves \(\mathcal O(\mu)\le2^r\).

**3. Construction attaining the upper bound.** For every \(s\in S\), choose a fair factor with \(n_j=2^s b_j\) and \(b_j\) odd. The proposed set \(q\Lambda_*\) has exactly \(2^r\) distinct elements because the least 2-adic valuation of any nontrivial signed sum \(\sum_s\eta_s2^{-s-1}\), with \(\eta_s\in\{-1,0,1\}\), is determined by the largest index \(s\) for which \(\eta_s\ne0\). For two distinct elements, their difference \(u\) has precisely that valuation \(-s-1\). More specifically, \(2n_j u=2^{s+1}b_j u\) is an **odd integer**, since the term with index \(s\) contributes \(\pm b_j\) and all terms of smaller index contribute even integers. Thus \(n_j u\in\mathbb Z+1/2\), so the selected fair factor of \(\widehat\mu(u/q)\) vanishes. Every pair is orthogonal, completing the proof.

**4. Completeness classification.** If all factors are fair with distinct step valuations, then \(r=m\), and the \(2^m\) subset sums of their positive steps are distinct: any nontrivial signed difference has a uniquely lowest dyadic valuation. Thus \(L^2(\mu)\) has dimension \(2^m=\mathcal O(\mu)\), so \(\Lambda_*\) is an orthonormal basis. Conversely, if \(r<m\), take one representative step at each of the \(r\) fair valuation classes. Their subset sums form a set of \(2^r\) distinct support points. Any additional positive step \(a>0\) produces the strictly larger finite union \(A\cup(A+a)\), because a finite nonempty set cannot be invariant under positive translation. Thus \(|\operatorname{supp}\mu|>2^r\), while every orthogonal exponential family has at most \(2^r\) members; no basis exists.

## Verification

The proof of the infinite family of statements is analytic; the finite computer checks provide independent diagnostics rather than substituting for induction. Running `python3 checker.py` with the standard Python library exhaustively constructs the graph of all Fourier-zero frequencies modulo the unit period for 816 small integer-step/bias masks, determines its largest clique exactly using rational arithmetic, and confirms both the \(2^r\) formula and the displayed constructive frequency family in every case. The graph enumeration is exhaustive for each tested instance because every orthogonal set may be translated to contain zero, every remaining normalized frequency must itself lie in the finite zero set modulo one, and pairwise orthogonality is checked by exact rational membership.

## Relationship to prior work

T. Zhou, *Spectrality of convolution and product measures: a block decomposition approach*, arXiv:2610.33987 (first public 25 October 2026), characterizes complete convolution spectra under a strong additive-subgroup condition on the first factor's Fourier-zero set, and investigates block decompositions of complete orthogonal bases. The current finite atomic coset-zero set does not satisfy that additive-subgroup hypothesis: it contains a nonintegral zero but no nonzero integer, while multiples of such zeros produce integers. That result consequently does not yield this sharp maximum size for incomplete orthogonal families.

Y.-S. Cao, Q.-R. Deng, M.-T. Li and S. Wu, *A Note on the Spectrality of Moran-Type Bernoulli Convolutions by Deng and Li*, Bull. Malays. Math. Sci. Soc. 47 (2024), article 127, doi:10.1007/s40840-024-01720-5, supplies a known valuation criterion for spectrality of a broader infinite, bounded-digit Moran-type family. Its Lemma 2.3(ii) gives a construction of a full basis for finite *distinct-valuation* subfamilies. The construction and qualitative complete-basis question are not new here. They do not provide the exact maximum number of orthogonal exponentials for a generally *nonspectral finite convolution with repeated valuations or biased factors*. The present statement solves that quantitative problem by an upper-bound argument valid for every orthogonal family, not just possible bases.

An indexed study, *Odd-relation rigidity for orthogonal exponentials of three irrational Bernoulli factors* (2026), concerns pairwise irrational length ratios and gives possible maxima two or three. The rational commensurability hypothesis in the present theorem is substantive: its dyadic valuation argument is not applicable to the irrational setting, and the existing irrational result does not imply the present all-length formula.

## Limitations

The theorem requires finite positive commensurable lengths and strictly interior Bernoulli probabilities. With irrationally related lengths, dyadic valuations in a common rational coordinate do not exist, and the maximal orthogonal cardinality can behave differently. It classifies the **maximum cardinality**, not all maximal-by-inclusion sets or all optimizers. It makes no claim of a general spectrality criterion for infinite convolutions, and it does not address approximate orthogonality. The spectrality corollary is not asserted as independently novel. Unindexed older partial-orthogonality results may constitute residual bibliographic risk. Independent mathematical audit has not been performed.

## References

1. T. Zhou, *Spectrality of convolution and product measures: a block decomposition approach*, arXiv:2610.33987 (2026). https://arxiv.org/abs/2610.33987
2. Y.-S. Cao, Q.-R. Deng, M.-T. Li and S. Wu, *A Note on the Spectrality of Moran-Type Bernoulli Convolutions by Deng and Li*, Bull. Malays. Math. Sci. Soc. 47, 127 (2024). https://doi.org/10.1007/s40840-024-01720-5
3. *Odd-relation rigidity for orthogonal exponentials of three irrational Bernoulli factors* (2026), published finding identifier `f57900f12015` (scientific index).
