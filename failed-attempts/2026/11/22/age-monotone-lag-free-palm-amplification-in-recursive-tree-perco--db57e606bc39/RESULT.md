# Age-monotone, lag-free Palm amplification in recursive-tree percolation

## Finding

Fix a bond-retention parameter \(0<p<1\). Grow a uniform recursive tree with vertices \(1,2,\ldots\), and independently retain every new edge with probability \(p\). Write \(I_j\) for the indicator that vertex \(j\) belongs to the open component of the root \(1\), and \(S_m=\sum_{i=1}^m I_i\). Define the finite products
\[
 A_m(p)=\prod_{r=1}^{m-1}\left(1+\frac{p}{r}\right),\qquad
 B_m(p)=\prod_{r=1}^{m-1}\left(1+\frac{2p}{r}\right),
\]
where the empty products are one.

**Theorem (permanent, age-monotone amplification).** For every integer \(j\ge2\), every \(k>j\), and every \(m\ge j\),
\[
\boxed{\quad
\frac{\mathbb P(I_k=1\mid I_j=1)}{\mathbb P(I_k=1)}
=\frac{\mathbb E[S_m\mid I_j=1]}{\mathbb E[S_m]}
=R_j(p):=\frac{2B_{j-1}(p)}{A_{j-1}(p)A_j(p)}.\quad}
\]
In particular, the multiplicative information supplied by a successful attachment at birth index \(j\) is **exactly independent of the later birth index** \(k\), and also independent of the future observation horizon \(m\). Moreover,
\[
 R_2(p)=\frac{2}{1+p},\qquad
 \frac{R_{j+1}(p)}{R_j(p)}
 =1+\frac{p(1-p)}{(j-1+p)(j+p)}>1,
\]
so that amplification is strictly increasing in the observed birth index and
\[
 \lim_{j\to\infty}R_j(p)
 =\frac{2\Gamma(1+p)^2}{\Gamma(1+2p)}>1.
\]
The exact marked two-point law is
\[
 \mathbb P(I_j=1,I_k=1)
 =\frac{p^2 A_{j-1}(p)A_{k-1}(p)}{(j-1)(k-1)}R_j(p),\qquad 2\le j<k,
\]
while \(\mathbb P(I_j=1)=pA_{j-1}(p)/(j-1)\). Thus the two membership indicators are strictly positively correlated for every pair of distinct nonroot birth labels; for all \(k>j\) the ratio of their joint probability to the product of their marginal probabilities depends only on \(j\).

## Assumptions and scope

For each \(t\ge2\), independently choose the parent \(P_t\) uniformly from \(\{1,\ldots,t-1\}\). Independently, retain its edge with Bernoulli probability \(p\). The retained root component is evaluated in the tree induced by the first \(m\) vertices. Since parent labels are always smaller, each \(I_j\) is fixed at birth and does not change when later vertices arrive. All formulas hold exactly for arbitrary finite indices within a common infinite-growth construction and for every fixed \(p\in(0,1)\). The limiting assertion concerns the observation index \(j\), not an asymptotic in \(p\) or the later label.

## Proof

Let \(\mathcal F_m\) be the natural history through birth \(m\). The parent-choice and independent-retention rules give
\[
 \mathbb P(I_{m+1}=1\mid\mathcal F_m)=\frac{pS_m}{m},\qquad
 \mathbb E[S_{m+1}\mid\mathcal F_m]=\left(1+\frac pm\right)S_m.
\]
Iteration from \(S_1=1\) proves \(\mathbb E S_m=A_m(p)\) and, for \(m\ge j\),
\[
 \mathbb E[S_m\mid\mathcal F_j]=\frac{A_m(p)}{A_j(p)}S_j.
\]

A second identity is obtained by setting \(F(s)=s(s+1)\): because \(F(s+1)-F(s)=2(s+1)\),
\[
 \mathbb E[F(S_{m+1})\mid\mathcal F_m]
 =\left(1+\frac{2p}{m}\right)F(S_m).
\]
Since \(F(S_1)=2\), this yields \(\mathbb E[S_m(S_m+1)]=2B_m(p)\). At birth \(j\),
\[
 \mathbb P(I_j=1)=\frac{p}{j-1}\mathbb E S_{j-1}=\frac{pA_{j-1}(p)}{j-1},
\]
and, because \(S_j=S_{j-1}+I_j\),
\[
 \mathbb E[I_jS_j]
 =\frac{p}{j-1}\mathbb E[S_{j-1}(S_{j-1}+1)]
 =\frac{2pB_{j-1}(p)}{j-1}.
\]
Dividing by the positive probability of \(I_j=1\) gives
\[
 \frac{\mathbb E[S_j\mid I_j=1]}{\mathbb E S_j}
 =\frac{2B_{j-1}(p)}{A_{j-1}(p)A_j(p)}=R_j(p).
\]
The conditional mean identity above carries this same ratio forward to every \(m\ge j\). For \(k>j\), conditioning the birth-\(k\) success indicator first on \(\mathcal F_{k-1}\) gives
\[
 \mathbb P(I_k=1\mid I_j=1)
 =\frac{p}{k-1}\mathbb E[S_{k-1}\mid I_j=1]
 =\frac{pA_{k-1}(p)}{k-1}R_j(p),
\]
which establishes the theorem's ratio and joint probability.

Finally, \(A_{m+1}/A_m=1+p/m\) and \(B_{m+1}/B_m=1+2p/m\). Substitution into \(R_{j+1}/R_j\) gives
\[
 \frac{j(j-1+2p)}{(j-1+p)(j+p)}
 =1+\frac{p(1-p)}{(j-1+p)(j+p)}.
\]
It is strictly greater than one for \(0<p<1\). The gamma-product identity
\(A_m=\Gamma(m+p)/(\Gamma(1+p)\Gamma(m))\), and its counterpart for \(B_m\), together with the gamma-ratio asymptotic, give the stated finite positive limit. Strict monotonicity from \(R_2>1\) also proves the limiting constant exceeds one, completing the proof.

## Verification

The self-contained Python standard-library checker `verify.py` enumerates every possible recursion-parent vector and independent edge-retention pattern through eight vertices. For retention probabilities \(1/3,2/3,1/2\), it evaluates the exact rational probabilities and conditional-size moments, compares them to the theorem's formulas, and also checks the strict-ratio recurrence algebraically at these parameter values. Running `python3 verify.py` produced five verified enumeration cases and `PASS: 145 symbolic/rational assertions, exhaustive through n=8`. This is a finite independent consistency check; validity for all indices and real parameters follows from the preceding proof.

## Relationship to prior work

Baur and Bertoin's *Cutting edges at random in large recursive trees* (arXiv:1406.2238, originally public 9 June 2014) describes the recursive-tree, percolation and Pólya–Hoppe urn connection and a scaling limit of root-cluster size, but its percolation lemma does not state the marked conditional two-time ratio. Baur's *Percolation on random recursive trees* (arXiv:1407.2508) principally studies near-unit retention and cluster genealogy. Kürsten's *Random Recursive Trees and the Elephant Random Walk* (arXiv:1512.05275, 2015, equation (44)) gives an exact finite root-cluster second moment, but not the exact labelled two-vertex conditional ratio. Desmarais, Holmgren and Wagner's *Broadcasting-induced colorings of preferential attachment trees* (2023, DOI 10.1002/rsa.21142) studies global color statistics and root-cluster size moments; its inspected root-cluster statements are unmarked by birth label. Zheng's *Can the root cluster remain largest forever in random recursive tree percolation?* (arXiv:2606.01881, 2026) explicitly gives the Simon-type restaurant transition and cluster-leadership results, but does not state the exact lag-free labelled-vertex Palm law or the age-monotonicity formula. These earlier results give the model and some ingredients; the asserted contribution is the exact finite-index **conditional persistence/amplification identity and its sharp age ordering**, not the root-cluster size law or its Mittag–Leffler limit.

## Limitations

The theorem concerns the root component of the uniformly attaching recursive tree with a common fixed bond-retention probability. It does not apply verbatim to site percolation, preferential attachment with nonuniform parent probabilities, or conditioning on multiple marked birth events. The theorem establishes two-point membership dependence and conditional first moments; it does not claim conditional distributional equality, joint independence, or a central limit theorem. Publication-priority questions for all general reinforced-urn formulations remain subject to independent literature review, especially where an unstated specialization of a broader result could imply the same formula.

## References

1. E. Baur and J. Bertoin, *Cutting edges at random in large recursive trees*, arXiv:1406.2238, version 1 publicly posted 9 June 2014. https://arxiv.org/abs/1406.2238
2. E. Baur, *Percolation on random recursive trees*, arXiv:1407.2508, version 1 publicly posted 9 July 2014. https://arxiv.org/abs/1407.2508
3. C. Desmarais, C. Holmgren and S. Wagner, *Broadcasting-induced colorings of preferential attachment trees*, Random Structures & Algorithms 63 (2023), 364–405. https://doi.org/10.1002/rsa.21142
4. Y. Zheng, *Can the root cluster remain largest forever in random recursive tree percolation?*, arXiv:2606.01881, posted 1 June 2026. https://arxiv.org/abs/2606.01881
5. R. Kürsten, *Random Recursive Trees and the Elephant Random Walk*, arXiv:1512.05275v1, originally public 16 December 2015. https://arxiv.org/abs/1512.05275
