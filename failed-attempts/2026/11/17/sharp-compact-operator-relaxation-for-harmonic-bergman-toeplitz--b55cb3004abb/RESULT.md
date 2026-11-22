# Sharp compact-operator relaxation for harmonic Bergman Toeplitz channels

## Finding

For the normal unital completely positive map \(\Psi_w\) associated with any admissible radial analytic Bergman weight, the following three statements hold together.

1. Every compact operator \(K\) is asymptotically erased in operator norm: \(\|\Psi_w^n(K)\|\to0\). Nevertheless, the restriction to compact operators is **not uniformly stable**: \(\|\Psi_w^n|_{\mathcal K}\|=1\) for each integer \(n\ge1\).
2. For the rank-one projection \(E_{pp}\) onto the \(p\)-th normalized monomial, every integer \(p\ge1\) has the **sharp exponential rate and amplitude**
\[
\lim_{n\to\infty}\frac{\|\Psi_w^n(E_{pp})\|}{\gamma_p^n}
= C_p,
\qquad
\gamma_p=1-\omega_1\frac{\omega_p}{\omega_{p+1}},
\qquad
C_p=\prod_{j=0}^{p-1}\frac{\delta_j}{\delta_j-\delta_p},
\quad \delta_j=\frac{\omega_j}{\omega_{j+1}}.
\]
Here \(0<\gamma_p<1\), \(\omega_j=\int_{\mathbb D}|z|^{2j}w(z)\,dA(z)\), and \(\Psi_w(E_{00})=0\). The whole diagonal profile satisfies
\[
\gamma_p^{-n}\Psi_w^n(E_{pp})\longrightarrow
\sum_{j=0}^{p}v_{p,j}E_{jj},\qquad
v_{p,j}=\prod_{r=j}^{p-1}\frac{\delta_r}{\delta_r-\delta_p}
\]
in operator norm (empty product one). In particular \(C_p=v_{p,0}>v_{p,1}>\cdots>v_{p,p}=1\).
3. For the normalized beta weights \(w_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\), with \(\alpha>-1\), the sharp constants are
\[
\gamma_p=\frac{(\alpha+1)p}{(\alpha+2)(p+1)},\qquad
C_p=\left(\frac{p+1}{\alpha+1}\right)^p\frac{(\alpha+2)_p}{p!},
\]
where \((\alpha+2)_p=\prod_{j=0}^{p-1}(\alpha+2+j)\). For the ordinary Bergman weight \(w\equiv1\), this gives the particularly simple amplitude \(C_p=(p+1)^{p+1}\) and rate \(\gamma_p=p/[2(p+1)]\).

## Assumptions and scope

Use normalized area measure \(dA=\pi^{-1}dx\,dy\) on the open unit disk \(\mathbb D\). An **admissible radial weight** is a nonnegative integrable radial function \(w\), of integral one, having positive mass in every annulus \(\{R<|z|<1\}\) for \(0\le R<1\). On the weighted analytic Bergman space \(A_w^2\), use normalized monomial basis \(e_j(z)=z^j/\sqrt{\omega_j}\), \(j\ge0\); write \(E_{pq}e_q=e_p\) and \(E_{pq}e_s=0\) for \(s\ne q\). The compact-operator ideal is \(\mathcal K=\mathcal K(A_w^2)\), with its inherited operator norm.

Put \(\delta_j=\omega_j/\omega_{j+1}\), \(Q_j\) for the orthogonal projection onto \(\operatorname{span}\{e_j,e_{j+1},\ldots\}\), and \(S'e_j=\sqrt{\delta_j}e_{j+1}\). The map is the specific Panja harmonic-Toeplitz channel
\[
\Psi_w(X)=\omega_1\left(S'^*XS'+\sum_{j=1}^{\infty}(\delta_{j-1}-\delta_j)Q_jXQ_j\right).
\]
The sum converges in operator norm. Each assertion is universal over every admissible radial \(w\), all indicated \(p\) and \(n\), and all compact \(K\); the asymptotic in \(n\) keeps \(p\) and \(w\) fixed. No assertion is made about uniform convergence as \(p\to\infty\).

## Proof

**Moment structure and complete positivity.** Let \(\mu\) be the probability distribution of \(|z|^2\) induced by \(w\,dA\). The moments \(\omega_j=\int_0^1 t^j\,d\mu(t)\) tend to zero, and the support has essential supremum one. Cauchy–Schwarz gives strict log-convexity \(\omega_{j+1}^2<\omega_j\omega_{j+2}\), since \(\mu\) is not concentrated at one point. Consequently \(\delta_0>\delta_1>\cdots>1\) with \(\delta_j\downarrow1\). The last limit follows from the root asymptotics \(\omega_j^{1/j}\to1\) and monotonicity of the ratios. Since \(\omega_0=1\), we also have \(\omega_1\delta_0=1\). The coefficients in the displayed formula for \(\Psi_w\) are nonnegative and summable, so it is completely positive. Its action on the identity has diagonal entries \(\omega_1(\delta_j+\delta_0-\delta_j)=1\), showing that it is unital and hence contractive in operator norm.

**Exact matrix-unit evolution.** Direct multiplication using the formula for \(S'\) and the diagonal tail projections gives, with \(m=\min\{p,q\}\),
\[
\Psi_w(E_{pq})=
\begin{cases}
\omega_1\sqrt{\delta_{p-1}\delta_{q-1}}E_{p-1,q-1}+b_mE_{pq},&p,q\ge1,\\
0,&m=0,
\end{cases}
\quad b_j=1-\omega_1\delta_j.
\]
The numbers \(b_0=0<b_1<b_2<\cdots<1\) are strictly increasing. Each matrix unit therefore generates a finite-dimensional invariant chain on which the matrix of \(\Psi_w\) is triangular with diagonal spectrum \(\{b_0,\ldots,b_m\}\). Every chain tends to zero exponentially, including the case \(m=0\) where it is killed in one step. Finite linear combinations of the matrix units are norm dense in \(\mathcal K\). Contractivity then gives \(\|\Psi_w^n(K)\|\to0\) for each \(K\in\mathcal K\); in particular \(\Psi_w(\mathcal K)\subset\mathcal K\).

**Nonuniformity.** Let \(F_m=\sum_{j=0}^{m}E_{jj}\). The diagonal identity \(b_j+\omega_1\delta_j=1\) implies \(\Psi_w(F_m)=F_{m-1}+b_mE_{mm}\) for \(m\ge1\), and \(\Psi_w(F_0)=0\). By induction, for \(0\le n\le m\), the positive contraction \(\Psi_w^n(F_m)\) acts as the identity on \(e_0,\ldots,e_{m-n}\). In particular \(\|\Psi_w^n(F_n)\|=1\) for every \(n\ge1\), whereas \(F_n\) is compact and has norm one. Contractivity supplies the reverse inequality, proving \(\|\Psi_w^n|_{\mathcal K}\|=1\).

**Sharp rank-one profile.** For fixed \(p\ge1\), the diagonal subspace spanned by \(E_{00},\ldots,E_{pp}\) is invariant. In the ordered basis it has a lower bidiagonal evolution: the diagonal entry is \(b_j\), and the transition from \(E_{jj}\) to \(E_{j-1,j-1}\) is \(a_j=\omega_1\delta_{j-1}\). Its distinct diagonal eigenvalues are \(b_0,\ldots,b_p\); hence it is diagonalizable and \(b_p\) is the unique dominant eigenvalue. Its eigenvector for \(b_p\), normalized to have coefficient one at \(E_{pp}\), has entries \(v_{p,p}=1\) and
\[
(b_p-b_j)v_{p,j}=a_{j+1}v_{p,j+1}\qquad(0\le j<p).
\]
Since \(b_p-b_j=\omega_1(\delta_j-\delta_p)\), this yields the products \(v_{p,j}\) displayed above. Every other eigenvector has zero \(E_{pp}\)-coefficient, so the coefficient of the dominant eigenvector in the decomposition of \(E_{pp}\) is exactly one. Dividing by \(b_p^n\) and letting \(n\to\infty\) establishes the operator-norm profile. Each product ratio exceeds one, so the leading norm coefficient is \(v_{p,0}=C_p\). This proves both the sharp exponential rate and amplitude, not merely an upper bound.

**Beta weights.** Direct beta integration gives \(\omega_j=\Gamma(\alpha+2)\Gamma(j+1)/\Gamma(j+\alpha+2)\), hence \(\delta_j=(j+\alpha+2)/(j+1)\) and \(\omega_1=1/(\alpha+2)\). Substitution yields the explicit rate and the product \(\prod_{j=0}^{p-1}(j+\alpha+2)(p+1)/[(\alpha+1)(p-j)]\), which simplifies to the displayed Pochhammer coefficient.

## Verification

The accompanying standalone Python file `checker.py` uses exact rational arithmetic for beta weights with integer exponents \(\alpha=0,1,2,3\). It independently constructs the lower bidiagonal matrix, checks its dominant eigenvector and closed-form amplitude through \(p=10\), compares iterative entries through the sixty-fifth power, and verifies finite-cutoff nonuniformity through twenty-five iterates. The script reports **232 passed exact-rational assertions**. These finite calculations are diagnostics; the universal proof is the preceding analytic argument. Run with `python checker.py` using the Python standard library only.

## Relationship to prior work

Panja's November 2026 paper supplies the unital completely positive map and identifies its fixed points with bounded-harmonic-symbol Toeplitz operators for arbitrary admissible radial weights; it also proves the absence of nonzero compact fixed points. It does not state norm decay on the entire compact ideal, the exact lack of uniform decay, or the sharp moment-dependent rank-one relaxation law established here. Zhang and Dou (2022) study fixed points and dual maps of general completely positive maps under additional hypotheses, rather than this channel's iteration rates. The diagonal moment recurrence and the full exponential eigenprofile are the additional ingredients; qualitative absence of fixed points alone would not imply norm stability. No claim of mathematical priority beyond the inspected evidence is made.

## Limitations

The map is the specific harmonic-Bergman channel defined above, not an arbitrary completely positive map. The rank-one asymptotic is for fixed \(p\), and the leading coefficient can become large with \(p\), consistently with the absence of uniform convergence on compact operators. The result concerns operator-norm dynamics on the compact ideal, not trace-preserving quantum evolution, and does not determine behavior of arbitrary noncompact inputs. Earlier literature may contain an equivalent triangular-operator treatment under different terminology. In particular, Li–Gao–Zhao–Ma (2024) investigate spectra of completely positive maps on compact operators, but the available first-page preview does not resolve whether a more general result implies any part of this specific moment-dependent dynamical classification.

## References

1. Samir Panja, *Toeplitz operators with bounded harmonic symbols on weighted Bergman spaces are the fixed points of a normal unital completely positive map*, arXiv:2611.09731v1 (first public version 2026-11-06), Sections 2–4. https://arxiv.org/abs/2611.09731
2. Haiyan Zhang and Yanni Dou, *Fixed points of completely positive maps and their dual maps*, Journal of Inequalities and Applications **2022**, article 163. https://doi.org/10.1186/s13660-022-02903-z
3. Issam Louhichi and Anders Olofsson, *Characterizations of Bergman space Toeplitz operators with harmonic symbols*, J. Reine Angew. Math. **617** (2008), 1–26. https://doi.org/10.1515/CRELLE.2008.024
4. Yuan Li, Shuhui Gao, Cong Zhao, and Nan Ma, *On spectra of some completely positive maps*, Positivity **28** (2024), article 22. https://doi.org/10.1007/s11117-024-01037-4 (first-page preview inspected; full article unavailable).
