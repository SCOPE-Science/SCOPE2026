# Sharp and typical entropy loss across minimal-jump-rank affine interval maps

## Finding

For every integer \(n\ge2\), consider the \(2^n\) equal-branch affine Markov interval maps \(F_\varepsilon\) associated with orientation words \(\varepsilon\in\{-1,+1\}^n\) in Oliveira's construction [1, Theorem 7.1]. These maps have \(n\) monotonicity branches and attain the least signed-jump-homology rank possible for their prescribed orientation word. Write
\[
\lambda_\varepsilon=\rho(M_\varepsilon),\qquad h_\varepsilon=\log\lambda_\varepsilon,\qquad D_\varepsilon=\log n-h_\varepsilon,
\]
where \(M_\varepsilon\) is the source's \(n\)-state Markov matrix.

**Theorem (the orientation entropy landscape).** The following statements hold for this *specific affine Markov construction*, not for all piecewise-monotone maps with the same orientation words.

1. Among all \(2^n\) words, the **unique** minimum-entropy word is \((-1,+1,-1,+1,\ldots)\), starting with a decreasing branch and strictly alternating thereafter. Exactly the two constant-orientation words attain the maximum entropy \(\log n\). If \(\lambda_{\min}(n)\) is the Perron root at the unique minimum, then for even \(n=2m\) it is the largest real root of
\[
\lambda^3-n\lambda^2+(n-1)\lambda-(m-1)=0,
\]
and for odd \(n=2m+1\) it is the largest real root of
\[
\lambda^3-(n-1)\lambda^2-\lambda+m=0.
\]
In particular,
\[
\lambda_{\min}(n)=n-1+\frac1{2n}+O(n^{-2}),\qquad
\max_\varepsilon D_\varepsilon=\frac1n+O(n^{-3})
\]
as \(n\to\infty\).

2. The **complete entropy multiset**, counting orientation words with multiplicity, is given by the following three families. Put \(\kappa=\#\{j:1\le j<n,\ \varepsilon_{j-1}\ne\varepsilon_j\}\).

| Final orientation pair | Allowed \(\kappa\) | Number of words for each \(\kappa\) | Equation defining \(\lambda_\varepsilon\) |
| --- | --- | --- | --- |
| Equal | \(0\le\kappa\le n-2\) | \(2\binom{n-2}{\kappa}\) | \(\lambda^2-n\lambda+\kappa=0\) |
| \((-1,+1)\) | \(1\le\kappa\le n-1\) | \(\binom{n-2}{\kappa-1}\) | \(\lambda^3-n\lambda^2+\kappa\lambda-\lfloor\kappa/2\rfloor=0\) |
| \((+1,-1)\) | \(1\le\kappa\le n-1\) | \(\binom{n-2}{\kappa-1}\) | \(\lambda^3-(n-1)\lambda^2+(\kappa-n)\lambda+\lfloor\kappa/2\rfloor=0\) |

In each row, take the largest-modulus eigenvalue of the nonnegative Markov matrix, equivalently the unique relevant root in \([n-1,n]\). The families are a **multiset**: different entries can yield the same entropy, and their multiplicities must then be added.

3. If \(\varepsilon\) is uniform on \(\{-1,+1\}^n\), then the transition count \(\kappa\) has the exact \(\operatorname{Binomial}(n-1,1/2)\) law. The entropy deficit obeys the **uniform deterministic estimate**
\[
\left|D_\varepsilon-\frac{\kappa}{n^2}\right|\le\frac2{n^2},\qquad n\ge3.
\]
Consequently, as \(n\to\infty\),
\[
nD_\varepsilon\xrightarrow{\mathbb P}\frac12,
\qquad
n^{3/2}\left(D_\varepsilon-\frac1{2n}\right)
\xrightarrow{\mathrm d}\mathcal N\left(0,\frac14\right).
\]
Thus the unique extremal word has leading entropy loss \(1/n\), while the typical loss is \(1/(2n)\) with Gaussian fluctuations on the \(n^{-3/2}\) scale.

## Assumptions and scope

Fix \(n\ge2\). The map is **exactly** the affine Markov map prescribed by [1, Theorem 7.1]: partition \([0,1]\) at \(c_j=j/n\), choose each of the \(n\) branches to be affine and increasing or decreasing according to \(\varepsilon_j\), and use the one-sided endpoint prescriptions from that theorem. In particular all interior cuts are genuine jumps. For clarity, write these prescriptions explicitly. At \(c_i\) the ordered left/right one-sided images are \((0,1)\) for \((-1,-1)\), \((1,0)\) for \((+1,+1)\), \((0,c_1)\) for \((-1,+1)\), and \((1,c_{n-1})\) for \((+1,-1)\). At the external endpoints take \(F(0^+)=1\) for a decreasing first branch and \(0\) otherwise, and \(F(1^-)=0\) for a decreasing last branch and \(1\) otherwise; interpolate uniquely and affinely on each branch. One-sided and endpoint conventions at the discontinuities do not affect the symbolic entropy under the source's cylinder definition. 

The Markov partition has \(n\) open cells. Its transition matrix is
\[
M_\varepsilon=\mathbf 1\mathbf 1^{\mathsf T}-u e_0^{\mathsf T}-v e_{n-1}^{\mathsf T},
\]
where \(u_j=1\) precisely for the transitions \((-1,+1)\), \(v_j=1\) precisely for \((+1,-1)\), and \(u_0=v_0=0\). This exact matrix and the equality \(h_\varepsilon=\log\rho(M_\varepsilon)\) are from [1, Section 7], and are not claimed as new results. The new statements are the all-word exact distribution, the unique worst orientation and its sharp asymptotics, and the typical-orientation limit theorem.

## Proof

**Step 1: Scalar Perron equation.** Put \(A=\sum_j u_j\), \(B=\sum_j v_j\), \(\kappa=A+B\), \(a=u_{n-1}\), and \(b=v_{n-1}\). For any \(n\ge3\), the rows of \(M\) have sums \(n\) or \(n-1\). Its Perron root \(\lambda\) lies in \([n-1,n]\). Let \(z\) be a positive right eigenvector, \(S=\sum_j z_j\). The first and last rows give
\[
\lambda z_0=S,\qquad \lambda z_{n-1}=S-a z_0-b z_{n-1}.
\]
Hence \(r=z_{n-1}/z_0\) is
\[
r(\lambda)=\begin{cases}1,&a=b=0,\\1-1/\lambda,&a=1,\\\lambda/(\lambda+1),&b=1.\end{cases}
\]
Summing all rows yields
\[
\boxed{\lambda(n-\lambda)=A+B r(\lambda).}\tag{1}
\]
Conversely, for the unique root \(\lambda\in[n-1,n]\) of (1), setting \(z_0=1\), \(z_{n-1}=r(\lambda)\) and \(z_j=1-(u_j+v_j r(\lambda))/\lambda\) gives a strictly positive eigenvector: its coordinates sum to \(\lambda\), and all rows hold. Thus the relevant root is indeed the Perron root, without relying on an unproved root choice. The scalar function \(\lambda(n-\lambda)-A-Br(\lambda)\) decreases strictly on \([n-1,n]\) for \(n\ge3\); its endpoint signs guarantee uniqueness. The \(n=2\) case follows from direct two-by-two matrices.

**Step 2: Exact multiset.** A sign word is determined by its first sign and the subset of its \(n-1\) flip positions. If the final pair is equal and \(\kappa\) flips occur, there are \(2\binom{n-2}{\kappa}\) choices. For either specified last flip, there are \(\binom{n-2}{\kappa-1}\) choices. In the last \((-1,+1)\) case \(A=\lceil\kappa/2\rceil\), \(B=\lfloor\kappa/2\rfloor\); in the last \((+1,-1)\) case the two values are reversed. Substituting these counts into [1, Theorem 7.2]'s cubic Markov determinant (or multiplying (1) by \(\lambda\) or \(\lambda+1\)) proves all three equations and the multiplicities. Coincident algebraic roots are not identified as distinct entropies.

**Step 3: Strict extremizers.** If \(\kappa=0\), \(M=\mathbf 1\mathbf 1^{\mathsf T}\) and \(\lambda=n\). If \(\kappa>0\), the right side of (1) is positive, so \(\lambda<n\). Hence only the two constant words maximize entropy. For \(n\ge3\), if the word is not strictly alternating, then \(\kappa\le n-2\), so \(A+Br(\lambda)\le n-2\). For a strictly alternating word, \(\kappa=n-1\); its score \(A+Br(\lambda)\) exceeds \(n-2\) throughout \([n-1,n]\). As the left side minus the score is strictly decreasing, **every** alternating word has smaller Perron root than **every** nonalternating one. The two alternating words are distinguished as follows. If \(n=2m\), the score for the word starting with \(-1\) is \(n-1-(m-1)/\lambda\), whereas for the word starting with \(+1\) it is \(n-1-m/(\lambda+1)\). The first is strictly larger since \(\lambda>m-1\). If \(n=2m+1\), the corresponding scores are \(n-1-m/(\lambda+1)\) and \(n-1-m/\lambda\), again with the first larger. The decreasing-root comparison proves uniqueness of the negative-start alternator. For \(n=2\), the roots for \((-1,+1)\) and \((+1,-1)\) are \(1\) and \((1+\sqrt5)/2\), respectively, so the claim also holds. The characteristic equations follow by substituting the alternating transition counts.

**Step 4: Extremal asymptotics.** For the minimizing word write \(\lambda=n-1+\alpha_n\). Substitution in (1) gives
\[
(n-2)\alpha_n+\alpha_n^2=\begin{cases}
(m-1)/\lambda,&n=2m,\\
m/(\lambda+1),&n=2m+1.
\end{cases}
\]
The right side tends to \(1/2\), while \(n-2\) diverges. Expanding this exact positive-root identity shows \(\alpha_n=(2n)^{-1}+O(n^{-2})\). Taking a logarithm yields \(\log(n/\lambda)=n^{-1}+O(n^{-3})\).

**Step 5: Uniform loss and Gaussian law.** For \(n\ge3\), let \(\Delta=n-\lambda\in[0,1]\). The formula for \(r\) gives \(0\le B(1-r)\le1\). Equation (1) implies
\[
n\Delta-\kappa=\Delta^2-B(1-r),\qquad |\Delta-\kappa/n|\le1/n.
\]
Since \(0\le\Delta/n\le1/n\), the standard logarithm remainder estimate gives \(0\le-\log(1-\Delta/n)-\Delta/n\le 1/[2n(n-1)]\), proving the displayed bound \(|D_\varepsilon-\kappa/n^2|\le 2/n^2\). For uniformly sampled independent signs, the transformation from the first sign and \(n-1\) successive flip bits to the full word is bijective; the flip bits are independent fair Bernoulli variables. The binomial weak law and central limit theorem then give the two limits because the uniform remainder, multiplied by \(n^{3/2}\), vanishes. This is an infinite-family proof; finite enumerations are used only as cross-checks.

## Verification

The standalone `check_orientation_entropy.py` uses only the Python standard library and may be executed as `python3 check_orientation_entropy.py`. It checks 1,512 **exact integer** characteristic-polynomial evaluations against the direct Markov determinants for every word with \(3\le n\le8\), and it enumerates all 32,764 words with \(2\le n\le14\), confirming the three binomial multiplicity formulas, unique minimum, maximum, and the uniform entropy-loss estimate. These are supplementary finite tests; the proofs above establish all \(n\).

## Relationship to prior work

Oliveira [1] establishes the exact family, the minimal signed-jump-homology rank, the rank-three Markov matrix identity, its cubic determinant, and a coarse high-entropy bound \(\log n-h_\varepsilon\le\log(n/(n-1))\). Those are treated as **premises**. The new result optimizes this specified family over all orientation words, supplies its full entropy multiset and multiplicities, and gives an orientation-sampling central limit law. Separate calculations for the same canonical maps already describe physical invariant laws for some word classes and spectral mixing bounds for all signs; neither statement determines the entropy-minimizing word, the full orientation-word multiset, or its Gaussian entropy-deficit law. The general weighted kneading theory of Rugh and Tan [2] covers entropy determinants but does not itself specify this orientation optimization.

## Limitations

The claim is specific to Oliveira's canonical equal-branch affine Markov realizations. A different map with the same orientation word can have a different entropy, so no optimization over *all* interval maps is asserted. The Gaussian probability law samples **orientation words**, not initial points or physical invariant measures. The eigenvalue equations may coincide for different word classes; the displayed table is a multiset with multiplicities, not a list of distinct algebraic numbers. Scientific priority is assessed against inspected sources and accessible search records, not certified by an exhaustive worldwide literature review. Independent mathematical audit has not been performed.

## References

[1] H. M. Oliveira, *Homological reduction and entropy of discontinuous interval maps*, arXiv:2611.03287v1, first publicly posted 2026-11-02, especially Theorems 7.1–7.2 and Corollary 7.3. https://arxiv.org/abs/2611.03287

[2] H. H. Rugh and L. Tan, *Kneading with weights*, Journal of Fractal Geometry **2** (2015), 339–375, DOI:10.4171/JFG/24. https://ems.press/journals/jfg/articles/13331
