# Finite-Blaschke boundedness rigidity on a lacunary Hardy space

## Finding
Fix an integer \(q\ge3\) and a real \(\gamma>0\). For the coefficient-weighted analytic Hardy Hilbert space \(H^2(\beta)\) defined below, and any nonconstant finite Blaschke product \(B\), the composition operator \(C_Bf=f\circ B\) extends boundedly to \(H^2(\beta)\) **if and only if** \(B(z)=\xi z^{q^j}\) for some integer \(j\ge0\) and \(|\xi|=1\). Every allowed operator has norm exactly \(1\) and is noncompact.

For every forbidden finite Blaschke product, let \(e_k(z)=(k+1)^{\gamma/2}z^{q^k}\) for \(k\ge1\); these are unit vectors in \(H^2(\beta)\). Then the **universal sharp divergence law** is
\[
\lim_{k\to\infty}(k+1)^{-\gamma/2}\|C_Be_k\|_{H^2(\beta)}=1.
\]
If \(B\) is nonmonomial, the ratio on the left equals \(1+o(1)\) from below; if \(B(z)=\xi z^d\) with \(d\) not a power of \(q\), the ratio equals \(1\) for every \(k\ge1\).

At the same time, the sets of symbols inducing Hilbert–Schmidt composition operators on \(H^2(\beta)\) and on classical \(H^2\) are equal. **This Hilbert–Schmidt assertion is a direct application of the pre-existing Theorem 1.3(b) of Cruz-Zamorano–Dellepiane–Seco; it is included solely as context, not claimed as new.** The new claim is the complete finite-Blaschke boundedness classification with the sharp normalized-power divergence law.

## Assumptions and scope
Let \(\mathbb D\) denote the unit disk. Write \(f(z)=\sum_{n=0}^\infty a_nz^n\) and set
\[
\beta_n=\begin{cases}(k+1)^{-\gamma},&n=q^k\text{ for an integer }k\ge1,\\1,&\text{otherwise},\end{cases}
\qquad
\|f\|_{H^2(\beta)}^2=\sum_{n=0}^\infty\beta_n|a_n|^2.
\]
Thus \(\beta_0=\beta_1=1\), all weights lie in \((0,1]\), and \(\liminf_{n\to\infty}\beta_n^{1/n}=1\), so this is a Hilbert space of functions holomorphic in \(\mathbb D\). A finite Blaschke product means \(B(z)=\xi\prod_{t=1}^d(z-a_t)/(1-\overline{a_t}z)\), with \(d\ge1\), \(|a_t|<1\), and \(|\xi|=1\). The notation \(C_B\) initially denotes composition on analytic polynomials; boundedness means existence of its bounded extension to all of \(H^2(\beta)\). There are no claims for arbitrary infinite Blaschke products or arbitrary inner symbols.

## Proof
**1. The nonmonomial Fourier-mass escape lemma.** Let \(B\) be a finite Blaschke product not of the form \(\xi z^d\), and set \(a_m(N)=\widehat{B^N}(m)\) for integers \(m,N\ge0\). We prove
\[
\sum_{j\ge1}|a_{q^j}(N)|^2=o(1)\qquad(N\to\infty).
\]
The finite product is holomorphic on \(|z|\le R\) for some \(R>1\) and has an analytic, real-valued boundary argument \(\theta(t)\), so \(B(e^{it})=e^{i\theta(t)}\) with \(\theta(t+2\pi)=\theta(t)+2\pi d\). If \(\theta'\) were constant, the boundary function, and hence \(B\) by analytic uniqueness, would equal \(\xi z^d\). Thus \(\theta'\) is nonconstant and real analytic. At every point of the compact circle, at least one derivative \(\theta^{(r)}\), with an integer \(r\ge2\), is nonzero. Compactness supplies finitely many intervals on which some such derivative is bounded away from zero. On these intervals the \(r\)-th derivative of the phase \(N\theta(t)-mt\) is \(N\theta^{(r)}(t)\), independent of \(m\). The higher-derivative van der Corput estimate, applied interval by interval, therefore yields constants \(C>0\) and \(\eta>0\), depending on \(B\) but not \(m,N\), with
\[
\sup_{m\ge0}|a_m(N)|\le C N^{-\eta}\qquad(N\ge1).
\]
This type of uniform Fourier-coefficient decay is also established, in sharper form, by Borichev–Fouchet–Zarouf (arXiv:2401.17520, Theorem 1); it is prior mathematical input, not novel here.

Write \(M_R=\max_{|z|=R}|B(z)|\). Cauchy's estimate gives \(|a_m(N)|\le M_R^N R^{-m}\). Choose \(A>0\) large enough that \(A\log R>\log M_R\). Then
\[
\sum_{m>AN}|a_m(N)|^2\le\frac{M_R^{2N}R^{-2\lfloor AN\rfloor-2}}{1-R^{-2}}=O(e^{-cN})
\]
for some \(c>0\). There are at most \(1+\log_q(AN)\) indices \(q^j\) not exceeding \(AN\); hence
\[
\sum_{j\ge1}|a_{q^j}(N)|^2=O((1+\log N)N^{-2\eta})+O(e^{-cN})=o(1).
\]
The estimate covers finite Blaschke products with any number of zero factors at the origin, since they still have analytic boundary arguments. By Parseval and the inner property, \(\sum_{m\ge0}|a_m(N)|^2=\|B^N\|_{H^2}^2=1\). Therefore
\[
\|B^N\|_{H^2(\beta)}^2=1-\sum_{j\ge1}(1-(j+1)^{-\gamma})|a_{q^j}(N)|^2=1-o(1).
\]
In particular, for \(N=q^k\),
\[
\|C_Be_k\|_{H^2(\beta)}=(k+1)^{\gamma/2}\bigl(1+o(1)\bigr),
\]
which excludes bounded extension and gives the asserted exact coefficient.

**2. Monomial finite Blaschke products.** For \(B(z)=\xi z^d\) with \(d\ge1\), the monomial basis vectors map into pairwise orthogonal monomial vectors; hence the norm of the composition map on polynomials is the supremum of \(\sqrt{\beta_{dn}/\beta_n}\) over \(n\ge0\). If \(d=q^j\), then \(n\notin\{q^k:k\ge1\}\) implies \(dn\notin\{q^k:k\ge1\}\), except possibly \(n=1\); but for \(n=1\), \(\beta_{dn}\le\beta_1=1\). For \(n=q^k\) with \(k\ge1\), the ratio is \(((k+1)/(k+j+1))^\gamma\le1\). Thus \(\|C_B\|=1\), attained on constants. The distinct nonexceptional degrees give an infinite sequence of unit vectors whose images are mutually orthogonal with norm \(1\), so the operator is not compact.

If \(d\) is not a power of \(q\), every \(dq^k\) lies outside \(\{q^j:j\ge1\}\), and
\[
\|C_Be_k\|_{H^2(\beta)}=(k+1)^{\gamma/2}\qquad(k\ge1).
\]
This excludes bounded extension with the exact stated divergence. The two cases exhaust all finite Blaschke products.

**3. Hilbert–Schmidt context (previous theorem).** The exceptional indices \(q^k\), \(k\ge1\), have successive ratio \(q>2\); the complementary weights are identically \(1\), and
\[
\inf_{k\ge1}q^k\beta_{q^k}=\inf_{k\ge1}\frac{q^k}{(k+1)^\gamma}>0.
\]
Theorem 1.3(b) of Cruz-Zamorano, Dellepiane and Seco (2026) consequently gives equality of Hilbert–Schmidt composition-symbol sets. No new proof or priority is asserted for that fact.

## Verification
A standalone Python/NumPy diagnostic checks exact monomial weight ratios for several bases and exponents and finite Fourier coefficients of powers of representative nonmonomial finite Blaschke products. To reproduce from this package, run `python check_result.py` with NumPy installed. It tests finite truncations only and is **not** a substitute for the uniform van der Corput argument, the Cauchy tail bound, Parseval, or the operator-norm proof. No numerical extrapolation is used in proving an infinite statement.

## Relationship to prior work
Cruz-Zamorano–Dellepiane–Seco (arXiv:2610.40148v1, Theorem 1.3(b) and Section 4.2) already prove the Hilbert–Schmidt symbol-class equality for lacunary weights satisfying these hypotheses; that assertion is credited directly. Borichev–Fouchet–Zarouf (arXiv:2401.17520, Theorem 1 and Section 4) establish sharp uniform Fourier-coefficient decay for powers of finite Blaschke products; their bounds underpin the Fourier escape argument. Lefèvre–Li–Queffélec–Rodríguez-Piazza (arXiv:2312.03482, Theorem 1.2 and Sections 3–4) classify weights allowing all composition operators and analyze disk automorphisms, but do not give the present exact classification for one sparsely depressed weight. Hou–Jiang (arXiv:2302.08233) study weights whose successive weight ratios tend to one; that regularity fails for the present sharp sparse dips. The specific finite-inner boundedness classification and universal normalized-power divergence are not statements supplied by these prior papers.

## Limitations
This result concerns only finite Blaschke symbols and the precisely defined lacunary weights; it does not extend automatically to infinite inner functions or all analytic disk maps. The exponent \(\eta\) in the van der Corput estimate may depend on the finite product. The Hilbert–Schmidt equality is known from 2026 literature and is not an original component. The novelty comparison is based on inspected accessible literature and mathematical implication checks; publication priority outside those sources remains open to independent verification.

## References
1. F. J. Cruz-Zamorano, E. Dellepiane and D. Seco, *Compact and Hilbert–Schmidt composition operators on weighted Hardy spaces*, arXiv:2610.40148v1 (first publicly submitted 2026-10-29), especially Theorem 1.3(b), Section 4.2. https://arxiv.org/abs/2610.40148
2. A. Borichev, K. Fouchet and R. Zarouf, *On the Fourier coefficients of powers of a finite Blaschke product*, arXiv:2401.17520v1 (2024), especially Theorem 1 and Section 4. https://arxiv.org/abs/2401.17520
3. P. Lefèvre, D. Li, H. Queffélec and L. Rodríguez-Piazza, *Characterization of weighted Hardy spaces on which all composition operators are bounded*, arXiv:2312.03482 (2023), Sections 3–4. https://arxiv.org/abs/2312.03482
4. B. Hou and C. Jiang, *Composition operators on weighted Hardy spaces of polynomial growth*, arXiv:2302.08233v1 (2023), Definition 1.1 and Sections 2–4. https://arxiv.org/abs/2302.08233
