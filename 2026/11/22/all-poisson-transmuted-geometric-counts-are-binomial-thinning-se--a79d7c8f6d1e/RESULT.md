# All Poisson–transmuted geometric counts are binomial-thinning self-decomposable

## Finding
For every \(\lambda>0\), \(0<q<1\), and \(0<\alpha<1\), the Poisson–transmuted geometric count law \(Y\sim\operatorname{PoiTG}(\lambda,q,\alpha)\) of Nandi, Chakraborty and Biswas is **discrete self-decomposable under binomial thinning**. More precisely, for every \(0<c<1\), there is a nonnegative integer-valued innovation \(Z_c\), independent of \(Y\), such that
\[
Y\stackrel{d}{=}c\odot Y+Z_c,
\]
where \(c\odot Y\mid Y\sim\operatorname{Binomial}(Y,c)\) is formed with independent Bernoulli thinnings. Consequently the law is unimodal, infinitely divisible on the nonnegative integers, and admits an exact compound-Poisson representation with strictly positive jump intensities
\[
\nu_1=\lambda+q+q^2-r,\qquad
\nu_j=\frac{q^j+q^{2j}-r^j}{j}\quad(j\ge2),\qquad
r=\frac{q(q+\alpha)}{1+\alpha q}.
\]
The canonical sequence \(j\nu_j\) is strictly decreasing in \(j\ge1\), except that the first term additionally contains \(\lambda\). The same conclusion extends continuously to the natural limits \(\lambda=0\) and \(\alpha\in\{0,1\}\).

The square relationship between the two geometric components is mathematically material: an equally weighted mixture of independent zero-based geometric laws having respective survival ratios \(1/6\) and \(5/6\) is **not** self-decomposable under binomial thinning, and adding any independent Poisson count does not repair that failure.

## Assumptions and scope
The original model has \(Y=N+T\), with \(N\sim\operatorname{Poisson}(\lambda)\) and \(T\) independent, whose probability mass function is
\[
\Pr(T=k)=(1-\alpha)(1-q)q^k+\alpha(1-q^2)q^{2k},\quad k=0,1,2,\ldots.
\]
All parameters are real in the ranges stated in the Finding. The word *self-decomposable* here refers specifically to **binomial-thinning** self-decomposability of \(\mathbb N_0\)-valued laws, not self-decomposability under real scalar multiplication. A law with probability-generating function (PGF) \(P\) has this property when \(P(z)/P(1-c+cz)\) is a PGF for each \(c\in(0,1)\). The usual discrete Lévy-sequence criterion says that when \(P(z)=\exp(\sum_{j\ge1}\nu_j(z^j-1))\), \(\nu_j\ge0\), the thinning self-decomposability condition is that \(j\nu_j\) be nonincreasing in \(j\ge1\). This is a standard characterization, not claimed as new here (see Pakes, 2022, Definition 3 and canonical-sequence discussion).

## Proof
**Step 1: exact compound-Poisson representation.** The model's PGF is
\[
P(z)=e^{\lambda(z-1)}\left(\frac{(1-\alpha)(1-q)}{1-qz}+\frac{\alpha(1-q^2)}{1-q^2z}\right).
\]
Elementary rational simplification gives
\[
P(z)=e^{\lambda(z-1)}\frac{(1-q)(1+\alpha q)(1-rz)}{(1-qz)(1-q^2z)},\qquad r=\frac{q(q+\alpha)}{1+\alpha q}.
\]
Here
\[
r-q^2=\frac{\alpha q(1-q^2)}{1+\alpha q}>0,
\qquad q-r=\frac{q(1-q)(1-\alpha)}{1+\alpha q}>0,
\]
so \(q^2<r<q\). Expanding the analytic logarithm for \(|z|\le1\) yields the announced \(\nu_j\) (the independent Poisson contribution affects only \(j=1\)). Each \(\nu_j>0\), because \(r^j<q^j\). Their sum is finite and equals
\[
\sum_{j=1}^\infty\nu_j=\lambda-\log\bigl((1-q)(1+\alpha q)\bigr),
\]
so the representation is genuinely compound Poisson, not merely a formal series.

**Step 2: the key all-index inequality.** Fix an integer \(j\ge1\), put \(f_j(x)=x^j(1-x)\) for \(x\in[0,1]\), and set \(p=j/(j+1)\). Then \(f_j\) increases up to its unique maximizer \(p\) and decreases afterwards. We prove the strict inequality
\[
f_j(r)<f_j(q)+f_j(q^2)\qquad(q^2\le r\le q).
\]
If \(p\notin[q^2,q]\), the function \(f_j\) is monotone on \([q^2,q]\), so \(f_j(r)\le\max\{f_j(q),f_j(q^2)\}<f_j(q)+f_j(q^2)\).

If \(p\in[q^2,q]\), then \(p\le q\le\sqrt p\) and \(p^2\le q^2\le p\). Unimodality of \(f_j\) gives
\[
f_j(q)\ge f_j(\sqrt p)>\tfrac12 f_j(p),\qquad
f_j(q^2)\ge f_j(p^2)>\tfrac12 f_j(p).
\]
For completeness, the first strict bound follows exactly from
\[
\frac{f_j(\sqrt p)}{f_j(p)}=\frac{p^{-j/2}}{1+\sqrt p}>\frac12.
\]
For the second, \(f_j(p^2)/f_j(p)=p^j(1+p)>3/(2e)>1/2\), using \((1+1/j)^j<e<3\) and \(p\ge1/2\). Thus \(f_j(q)+f_j(q^2)>f_j(p)\ge f_j(r)\). The inequality is proved for every integer \(j\), not just finitely many tested indices.

**Step 3: thinning self-decomposability.** Define \(b_j=q^j+q^{2j}-r^j\). Then
\[
b_j-b_{j+1}=f_j(q)+f_j(q^2)-f_j(r)>0
\]
for every \(j\ge1\). Therefore \(j\nu_j=b_j\) for \(j\ge2\) decreases strictly, and \(\nu_1=\lambda+b_1>b_2=2\nu_2\), so \((j\nu_j)_{j\ge1}\) is strictly decreasing. The discrete canonical-sequence criterion from the Assumptions section establishes thinning self-decomposability. The standard unimodality implication follows. The PGF calculation is continuous at \(\lambda=0\) and \(\alpha=0,1\), and the same inequalities cover these limits.

**Step 4: why the geometric-ratio restriction matters.** A general equal-weight geometric mixture with survival ratios \(a=1/6\) and \(b=5/6\) has rational PGF proportional to \((1-sz)/[(1-az)(1-bz)]\), with \(s=13/18\). Its compound-Poisson canonical terms satisfy \(j\nu_j=a^j+b^j-s^j\). Exact rational calculation gives
\[
3\nu_3-2\nu_2=\frac{35}{5832}>0.
\]
Hence that generic mixture is not thinning self-decomposable. Convolution with any \(\operatorname{Poisson}(\lambda)\) changes only \(\nu_1\), so it cannot repair this violation. Thus the universal conclusion for the PoiTG family is not a generic property of all two-geometric mixtures.

## Verification
Run \(\texttt{python verify.py}\) in a Python installation with SymPy. The checker verifies the rational PGF factorization, both bounds for \(r\), the exact log-PGF coefficients, 25 rational parameter pairs across 89 adjacent-index inequalities, three Poisson intensities, and the rational generic-mixture counterexample. These finite checks are reproducibility supplements. The infinitely many canonical inequalities are established analytically by Step 2, rather than inferred from experiments.

## Relationship to prior work
Nandi, Chakraborty and Biswas (arXiv:2306.07219v1, first submitted 12 June 2023) introduce the PoiTG convolution, its PGF and graphical unimodality, as well as count-model inference. Their Section 2 defines the positive transmutation parameter, and Section 3 derives its generating functions, moments and reliability measures. Those formulas supply this result's starting distribution; the **new claim** is global thinning self-decomposability and its all-index canonical monotonicity, with an explicit jump-intensity formula. Ordinary infinite divisibility is not claimed as new: Chakraborty and Bhati (2016, Section 3.2) had already established infinite divisibility for the positive-transmutation geometric parent, and the PoiTG convolution with an independent Poisson variable inherits it. The source text does not state a self-decomposability theorem. Chakraborty and Bhati (2016, Section 3.2 and Theorem 4) establish infinite divisibility and the PGF of the parent transmuted geometric law; those findings already imply PoiTG infinite divisibility but do not provide the stricter thinning self-decomposability inequality. The 2019 follow-up analyzes the same parent model. Pakes (2022), *Mutant Number Laws and Infinite Divisibility*, reviews the general canonical-sequence criterion and geometric mixtures; that standard criterion alone does not show monotonicity for these special rational coefficients. The distinct-rate counterexample demonstrates why an unqualified geometric-mixture closure statement would not subsume the new theorem.

## Limitations
The self-decomposability theorem applies to the published PoiTG parameter domain \(0<\alpha<1\), and its stated boundary limits; no assertion is made for negative transmutation parameters. It concerns binomial thinning, not continuous scaling. The argument does not classify all finite geometric mixtures or derive statistical estimator performance. The claim's historical priority is based on the cited literature and semantic searches; no search can guarantee that an equivalent argument does not exist elsewhere. The verification program is not an independent mathematical audit.

## References
1. A. Nandi, S. Chakraborty, A. Biswas, “A new count model based on Poisson-Transmuted Geometric convolution,” arXiv:2306.07219v1, 12 June 2023, https://arxiv.org/abs/2306.07219. Full publicly readable transcription: https://www.researchgate.net/publication/371506994_A_new_count_model_based_on_Poisson-Transmuted_Geometric_convolution.
2. A. G. Pakes, “Mutant Number Laws and Infinite Divisibility,” *Axioms* 11 (2022), 584. https://doi.org/10.3390/axioms11110584. Definition 3 and canonical-sequence criterion; Section on geometric mixtures.
3. S. Chakraborty, D. Bhati, “Transmuted geometric distribution with applications in modeling and regression analysis of count data,” *SORT* 40 (2016), 153–176. https://www.idescat.cat/sort/sort401/40.1.7.chakraborty-bhati.pdf.
4. S. Chakraborty, D. Bhati, “Analysis of Count Data by Transmuted Geometric Distribution,” *Journal of Statistical Theory and Applications* 18 (2019), 450–463. https://doi.org/10.2991/jsta.d.191218.001.
