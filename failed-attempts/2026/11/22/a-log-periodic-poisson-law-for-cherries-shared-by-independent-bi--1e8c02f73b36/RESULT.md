# A log-periodic Poisson law for cherries shared by independent binary tries

## Finding

Two independent binary Patricia tries built from independent fair-bit strings for the same \(n\) labelled keys retain a nontrivial but *log-periodic* number of identical labelled cherries. Write \(H_{n,q}\) for the number of unordered pairs of keys that form a cherry in **all** of \(q\) independently built tries. Define, for real \(s\),
\[
F(s)=\frac12\sum_{j\in\mathbb Z}2^{s+j}e^{-2^{s+j}},\qquad
\lambda(s)=\frac12F(s)^2,\qquad s_n=\{\log_2 n\}.
\]
Then the series converges locally uniformly, \(F\) is strictly positive and nonconstant, and
\[
d_{\rm TV}\bigl(\mathcal L(H_{n,2}),\operatorname{Poisson}(\lambda(s_n))\bigr)\longrightarrow0.
\]
Thus every sequence with \(s_n\to s\) modulo one gives a Poisson limit with parameter \(\lambda(s)\), but the complete integer sequence has no single limiting law. For any fixed integer \(q\ge3\),
\[
\Pr(H_{n,q}\ge1)\sim\mathbb EH_{n,q}
=\binom n2p_n^q
\sim\frac{F(s_n)^q}{2n^{q-2}},
\]
where the precise finite probability of any specified pair being a cherry is
\[
p_n=\sum_{\ell\ge0}2^{-\ell-1}(1-2^{-\ell})^{n-2}.
\]
The one-tree cherry expectation and its dyadic periodicity are established prior work; the claimed result is the **cross-tree labelled-pair Poisson law and the fixed-many-tree rare-overlap threshold**.

## Assumptions and scope

For each \(n\ge2\), fix labels \(\{1,\ldots,n\}\). For each label and each of \(q\) trees, independently sample an infinite sequence of fair binary digits. The Patricia trie is the rooted binary prefix trie after suppressing every unary node. A cherry is exactly two leaves with a common parent (no third leaf). The label pair, not merely the unlabelled tree shape, must be common. Take \(n\to\infty\) with \(q\) fixed and at least two; the summation in \(F\) is over all integers. Convergence of \(s_n\) is on the unit circle, so \(s=0\) and \(s=1\) represent the same phase.

## Proof

**1. Exact probability for one specified cherry.** Two independent strings share an initial prefix of length \(\ell\) and disagree at the next digit with probability \(2^{-\ell-1}\). The two strings form a cherry precisely when none of the remaining \(n-2\) strings starts with that common prefix. The corresponding length-\(\ell\) cylinder has mass \(2^{-\ell}\); summing the disjoint first-disagreement events proves the stated formula for \(p_n\). Expanding the binomial and summing the geometric series also gives the exact finite identity
\[
p_n=\sum_{a=0}^{n-2}(-1)^a\binom{n-2}{a}\frac{2^a}{2^{a+1}-1}.
\]

**2. Multiple prescribed disjoint cherries.** For any fixed \(r\ge1\) consider \(r\) prescribed, mutually disjoint labelled pairs. For pair \(i\), draw its two strings and let \(L_i\) be their common-prefix length, \(X_i=2^{-L_i}\), and \(C_i\) the associated prefix cylinder. The cylinders are independent as random marked cylinders, with \(\Pr(L_i=\ell)=2^{-\ell-1}\). All pairs are simultaneously cherries if and only if their cylinders are pairwise disjoint and each of the \(n-2r\) other strings avoids their union. Therefore their joint probability is exactly
\[
B_{n,r}=\mathbb E\left[\mathbf1_{\{C_1,\ldots,C_r\,\text{pairwise disjoint}\}}
\left(1-\sum_{i=1}^r X_i\right)^{n-2r}\right],\qquad n\ge2r.
\]
For each fixed \(r\), we claim \(B_{n,r}=p_n^r(1+o(1))\). To prove this uniformly in the dyadic phase, first restrict all \(nX_i\) to \([\varepsilon,M]\). In this range, independent random cylinders fail to be disjoint with probability at most \(r(r-1)M/n\), since for two cylinders the containment probability is their larger mass, at most \(M/n\). On disjoint cylinders, uniformly in this range,
\[
\left(1-\sum_i X_i\right)^{n-2r}
=\prod_i(1-X_i)^{n-2}\bigl(1+O_{r,M}(n^{-1})\bigr).
\]
Outside the range, the one-pair weighted geometric sums have the uniform relative bounds \(O(\varepsilon)\) for \(nX<\varepsilon\) and \(O((M+1)e^{-M/2})\) for \(nX>M\) (for large enough \(n\)); the same bounds apply to the joint expression by \((1-\sum_iX_i)^{n-2r}\le\prod_i(1-X_i)^{n-2r}\). As \(p_n\asymp n^{-1}\), first sending \(n\to\infty\) and then \(\varepsilon\downarrow0\), \(M\uparrow\infty\) proves the claim. The case \(r=1\) is exact.

**3. Periodic mean.** Put \(n=2^{k+s_n}\). Replacing \((1-2^{-\ell})^{n-2}\) in the weighted sum by \(e^{-n2^{-\ell}}\) and using standard exponential bounds gives a uniform \(O(n^{-1})\) error after multiplication by \(n\). Reindex \(j=k-\ell\), and complete the exponentially negligible missing far-negative tail to obtain
\[
np_n=F(s_n)+O(n^{-1}).
\]
In fact the Fourier coefficient of the smooth one-periodic function \(F\), at integer frequency \(h\), is
\[
\widehat F(h)=\frac{\Gamma(1-2\pi i h/\log2)}{2\log2}.
\]
Because the Gamma function has no zeros, the nonzero frequency coefficients do not vanish: \(F\) and \(\lambda\) are genuinely nonconstant. Also \(F(s)>0\) on the compact circle.

**4. Poisson moments and rare collision.** Since distinct cherries within the same tree have disjoint labels, selecting \(r\) *ordered* cherries among \(n\) labels gives exactly \((n)_{2r}/2^r\) choices. The trees are independent, hence for every fixed \(r\)
\[
\mathbb E(H_{n,q})_r=\frac{(n)_{2r}}{2^r}B_{n,r}^q.
\]
For \(q=2\), this equals \(\lambda(s_n)^r+o(1)\). Along any phase-convergent subsequence, the method of factorial moments therefore gives the stated Poisson weak limit; tightness, integer-valuedness and convergence of point masses imply convergence in total variation. Compactness of the phase circle upgrades this to the displayed phase-varying total-variation assertion. Since the nonconstant parameter has distinct subsequential limits, the unphased laws do not converge. For fixed \(q\ge3\), the first factorial moment has the displayed asymptotics, and the second moment is \(O(n^{4-2q})=o(n^{2-q})\); first- and second-order Bonferroni bounds prove the rare-overlap probability formula.

## Verification

A standalone standard-library script, `check.py`, checks two algebraically different exact expressions for \(p_n\) for \(2\le n\le16\), checks joint specified-pair probabilities \(B_{n,2}\) by a separate prefix-cylinder sum against exact split recurrences for \(4\le n\le16\), and tests the limiting approximations at five increasing sizes. The checks run with `python check.py`. The finite exact two-tree law for \(n=4\) is
\[
\Pr(H_{4,2}=0)=\frac{106}{147},\quad
\Pr(H_{4,2}=1)=\frac{32}{147},\quad
\Pr(H_{4,2}=2)=\frac3{49}.
\]
Finite rational checks are corroboration, not proofs of asymptotic convergence or uniqueness.

## Relationship to prior work

Mahmoud and Ward establish mean counts and dyadic Mellin oscillations for cousins in single random tries; in the binary case a pair of leaf siblings is a two-cousin. The exact one-tree formula and first-moment periodicity here are not claimed as original. Holmgren treats record/cutting statistics in split-tree families including tries. Janson analyzes frequencies of individual fringe shapes in one Patricia trie, not identical labelled cherries simultaneously shared by independent copies. These published results do not, by their stated single-tree conclusions alone, give cross-tree labelled-pair factorial moments or the joint collision law. Potential earlier multi-trie pattern-matching results remain a priority risk.

## Limitations

Only fixed \(q\) is covered, with independent uniform fair-bit keys and identically labelled sets. No general biased alphabet, dependent keys, nonuniform key lengths, or growing \(q\) conclusion is established. The dyadic periodic amplitude is small; nonconstancy is mathematically exact, not a claim of large empirical effect. The proof is analytic and has not undergone independent validation.

## References

1. H. M. Mahmoud and M. D. Ward, *Average-Case Analysis of Cousins in m-ary Tries*, Journal of Applied Probability 45 (2008), 888–900. DOI: 10.1239/jap/1222441835. Lawful author PDF: https://www.cs.auckland.ac.nz/~mcw/Teaching/refs/tries/cousins.pdf
2. C. Holmgren, *A Weakly 1-Stable Limiting Distribution for the Number of Random Records and Cuttings in Split Trees*, arXiv:1005.4590, first posted 2010-05-25. https://arxiv.org/abs/1005.4590
3. S. Janson, *Fringe trees of Patricia tries, compressed binary search trees, and three other random full binary trees*, arXiv:2405.01239, first posted 2024-05-02. https://arxiv.org/abs/2405.01239
