# Strict coefficientwise Godbersen interpolation along reflected simplices

## Finding

Let \(n\ge2\), let \(\Delta\subset\mathbb R^n\) be any full-dimensional simplex, and put
\[
K_t=(1-t)\Delta+t(-\Delta),\qquad 0\le t\le1.
\]
For \(1\le k\le n-1\), define the dimensionless reflected mixed-volume coefficient
\[
Q_{n,k}(t)=\frac{V_n(K_t[n-k],(-K_t)[k])}{\operatorname{vol}_n(K_t)}.
\]
Here \(V_n\) is the symmetric, Minkowski-multilinear polarization of ordinary \(n\)-dimensional volume, and the bracketed counts are repeated arguments. The coefficients obey
\[
\boxed{Q_{n,k}(t)=Q_{n,k}(1-t),\qquad Q_{n,k}(0)=Q_{n,k}(1)=\binom nk,\qquad Q_{n,k}(1/2)=1.}
\]
For every \(k\) in this range, \(Q_{n,k}\) is **strictly decreasing on \([0,1/2]\)** and **strictly increasing on \([1/2,1]\)**. In particular, all interior Godbersen ratios follow the same strict interpolation, simultaneously in every dimension. At the centrally symmetric endpoint the precise second-order recovery is
\[
\boxed{Q_{n,k}(t)=1+\frac{2k(n-k)}{2n-1}(1-2t)^2+O_{n,k}((1-2t)^4),\quad t\to1/2.}
\]
The claim concerns the complete coefficient vector of the reflected mixed-volume polynomial along this one-parameter family, not only the volume of the unbalanced difference body.

## Assumptions and scope

All Minkowski sums and dilations have nonnegative coefficients; the reflection of \(K\) is \(-K=\{-x:x\in K\}\). Translation does not change any volume or mixed volume appearing above. The dimension \(n\), simplex \(\Delta\), index \(k\), and parameter \(t\) range exactly as displayed. At the midpoint the body is centrally symmetric; at the endpoints it is a simplex (up to reflection). Since the expressions are invariant under invertible affine transformations, it suffices to prove the result for the standard simplex. No such monotonicity is asserted for a general convex body.

## Proof

**1. The standard-simplex volume polynomial.** By affine invariance, take \(\Delta=\operatorname{conv}(0,e_1,\ldots,e_n)\), whose volume is \(1/n!\). For nonnegative \(a,b\), the body \(a\Delta+b(-\Delta)\) consists precisely of vectors \(x\) satisfying \(\sum_i\max(x_i,0)\le a\) and \(\sum_i\max(-x_i,0)\le b\): necessity follows from any representation \(x=y-z\) with \(y\in a\Delta,z\in b\Delta\), and sufficiency follows by taking the positive and negative parts of \(x\). In each orthant with \(j\) negative coordinates the corresponding volume is \(a^{n-j}b^j/((n-j)!j!)\). Summing the \(\binom nj\) orthants of that type gives
\[
\frac{\operatorname{vol}_n(a\Delta+b(-\Delta))}{\operatorname{vol}_n(\Delta)}
=F_n(a,b):=\sum_{j=0}^n\binom nj^2 a^{n-j}b^j.
\]
Thus the simplex has the known sharp Godbersen coefficients, now with their complete positive homogeneous volume polynomial explicitly derived.

**2. A one-variable polynomial.** For \(a+b=1\), write \(p=ab\), and set
\[
H_n(p)=\sum_{j=0}^{\lfloor n/2\rfloor}\frac{n!}{(n-2j)!(j!)^2}p^j.
\]
The coefficient identity
\[
F_n(a,b)=[z^n](1+az)^n(1+bz)^n=[z^n](1+z+pz^2)^n=H_n(p)
\]
is valid for all such \(a,b\) and follows directly from the binomial theorem. In particular, the volume of \(K_t\) is \(\operatorname{vol}(\Delta)H_n(t(1-t))\).

**3. Real negative zeros of the reduced volume polynomial.** The polynomials \(H_n\) have generating function
\[
\sum_{n\ge0}H_n(p)z^n=\frac{1}{\sqrt{1-2z+(1-4p)z^2}}.
\]
Indeed, the coefficient formula in step 2 is the constant-term expansion of \((1+\sqrt p\,w+\sqrt p\,w^{-1})^n\), whose sum over \(n\) gives the displayed quadratic-square-root generating function. Comparing with the standard Legendre generating function \(\sum_{n\ge0}P_n(x)w^n=(1-2xw+w^2)^{-1/2}\) yields the polynomial identity
\[
H_n(p)=(1-4p)^{n/2}P_n\bigl((1-4p)^{-1/2}\bigr).
\]
Every Legendre polynomial \(P_n\) has \(n\) simple real zeros in \((-1,1)\). If \(\xi_1,\ldots,\xi_m\), \(m=\lfloor n/2\rfloor\), are its positive zeros, the previous relation gives the **entire** factorization
\[
H_n(p)=\prod_{i=1}^{m}(1+\lambda_i p),\qquad
\lambda_i=\frac{4\xi_i^2}{1-\xi_i^2}>0.
\]
The degree on each side is \(m\), and their constant terms equal one. When \(n\) is odd, the zero at the origin of \(P_n\) produces no finite root of \(H_n\); the degree count includes precisely the \(m\) positive Legendre zeros.

**4. Exact normalized reflected-volume polynomial.** Put \(a=1-t\), \(b=t\), \(p=ab\). For \(s,u\ge0\),
\[
sK_t+u(-K_t)=(as+bu)\Delta+(bs+au)(-\Delta).
\]
The two coefficients on the right sum to \(s+u\), and their product equals \(p(s+u)^2+(1-4p)su\). Homogeneity and step 2 give, with the value at \(s=u=0\) understood polynomially,
\[
\begin{aligned}
R_{n,p}(s,u)&:=\frac{\operatorname{vol}_n(sK_t+u(-K_t))}{\operatorname{vol}_n(K_t)}\\
&=(s+u)^n\frac{H_n\bigl(p+(1-4p)su/(s+u)^2\bigr)}{H_n(p)}\\
&=(s+u)^n\prod_{i=1}^{m}\left(1+r_i(p)\frac{su}{(s+u)^2}\right),
\end{aligned}
\]
where
\[
r_i(p)=\frac{\lambda_i(1-4p)}{1+\lambda_i p}\ge0,\qquad 0\le p\le\tfrac14.
\]
On expanding by the elementary symmetric polynomials \(e_j\),
\[
R_{n,p}(s,u)=\sum_{j=0}^{m}e_j(r_1(p),\ldots,r_m(p))(s+u)^{n-2j}(su)^j.
\]
Hence its coefficient of \(s^{n-k}u^k\) is exactly
\[
A_{n,k}(p)=\sum_{j=0}^{\min\{k,n-k,m\}}
\binom{n-2j}{k-j}\,e_j(r_1(p),\ldots,r_m(p)),
\]
and the mixed-volume polarization formula shows \(A_{n,k}(p)=\binom nk Q_{n,k}(t)\).

**5. Strict coefficientwise monotonicity.** For each \(i\),
\[
r_i'(p)=-\frac{\lambda_i(4+\lambda_i)}{(1+\lambda_i p)^2}<0
\qquad(0\le p\le1/4).
\]
All \(r_i\) are positive when \(p<1/4\) and vanish at \(p=1/4\). Therefore every \(e_j(r(p))\) with \(j\ge1\) is nonincreasing in \(p\); \(e_1\) decreases strictly. For every \(1\le k\le n-1\), its coefficient in \(A_{n,k}\) is \(\binom{n-2}{k-1}>0\). Thus \(A_{n,k}(p)\), and therefore \(Q_{n,k}(t)\), decreases strictly for \(0\le p\le1/4\). As \(p=t(1-t)\) increases on \([0,1/2]\) and decreases on \([1/2,1]\), the claimed monotonicity and symmetry follow. The endpoints are exact: at \(p=0\), \(R_{n,0}(s,u)=F_n(s,u)\), giving \(Q_{n,k}=\binom nk\); at \(p=1/4\), every \(r_i=0\), so \(R_{n,1/4}(s,u)=(s+u)^n\) and \(Q_{n,k}=1\).

**6. Sharp center expansion.** Let \(q=(1-2t)^2=1-4p\). The exact formula in step 4 gives
\[
r_i(p)=q\frac{\lambda_i}{1+\lambda_i/4}+O_n(q^2),\qquad
\sum_i\frac{\lambda_i}{1+\lambda_i/4}=\frac{H_n'(1/4)}{H_n(1/4)}.
\]
To evaluate the logarithmic derivative, set \(a=(1+\varepsilon)/2\), \(b=(1-\varepsilon)/2\), so \(p=(1-\varepsilon^2)/4\). In \(F_n(a,b)\), the normalized weights at \(\varepsilon=0\) are \(\binom nj^2/\binom{2n}n\), the hypergeometric distribution with mean \(n/2\) and variance \(n^2/[4(2n-1)]\). Differentiating the sum twice in \(\varepsilon\) at zero gives
\[
\left.\frac{\partial^2_\varepsilon F_n((1+\varepsilon)/2,(1-\varepsilon)/2)}{F_n(1/2,1/2)}\right|_{\varepsilon=0}
=\frac{n^2}{2n-1}-n=-\frac{n(n-1)}{2n-1}.
\]
Differentiating \(H_n((1-\varepsilon^2)/4)\) instead yields \(-H_n'(1/4)/(2H_n(1/4))\), so
\[
\frac{H_n'(1/4)}{H_n(1/4)}=\frac{2n(n-1)}{2n-1}.
\]
All terms in \(A_{n,k}\) with \(j\ge2\) are \(O_{n,k}(q^2)\). Its \(j=1\) contribution is \(q\binom{n-2}{k-1} 2n(n-1)/(2n-1)+O(q^2)\). Dividing by \(\binom nk\) proves exactly the stated coefficient \(2k(n-k)/(2n-1)\) and the \(O_{n,k}((1-2t)^4)\) remainder.

## Verification

The proof applies for every integer \(n\ge2\), each interior index, and every \(0\le t\le1\). The accompanying standalone `verify.py` uses only the Python standard library and exact rational arithmetic. It independently compares the reduced-polynomial and direct mixed-volume expansions, tests strict coefficientwise monotonicity for representative rational parameters in dimensions 2 through 16, checks both endpoint normalizations, and verifies the exact logarithmic derivative identity. It reports `PASS 1605` when run with Python 3. These finite checks serve only as reproducibility diagnostics; the all-dimensional theorem follows from the Legendre factorization and strict sign argument above.

## Relationship to prior work

Fryš, Kotrbatý, Mouamine, and Wang (2026) prove the Godbersen mixed-volume bound and characterize simplices as the unique full-dimensional equality bodies. Their inequality supplies the two endpoint comparison levels, but it does not order the intermediate **normalized mixed-volume coefficients** along a reflected-simplex Minkowski interpolation. Artstein-Avidan and Putterman (2024 preprint; 2025 journal) investigate unbalanced difference bodies and weighted mixed-volume inequalities. Their results concern the primal volume of \((1-t)K+t(-K)\) relative to \(K\), not the mixed-volume coefficients of that *new body* with its own reflection, each divided by its volume. Fryš and Kotrbatý (2026) extend unbalanced difference bodies to higher-order constructions, without stating this coefficientwise profile for the original one-parameter simplex family.

The separately published geometric result *Strict Mahler-product monotonicity along simplex asymmetric difference bodies* studies the Santaló polar volume product for the same unbalanced simplex family; its polar factor and extremal quantity are different and do not imply the present all-index normalized mixed-volume inequalities. Another published record describes a Godbersen profile for single-vertex truncated simplices, a different deformation. No assertion that a keyword search alone proves historical novelty is made.

## Limitations

The monotonicity statement is restricted to Minkowski interpolations of a full-dimensional simplex with its own reflection. The proof does not establish coefficientwise monotonicity for unbalanced difference bodies of arbitrary convex bodies. The explicit quartic-order remainder is local near the symmetric midpoint; the monotonicity itself is global. Historical priority remains subject to independent literature review, and independent mathematical audit has not been performed.

## References

1. F. Fryš, J. Kotrbatý, M. A. Mouamine and S. Wang, *Higher-order Godbersen inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806, first public version 2026-10-05. https://arxiv.org/abs/2610.06806
2. S. Artstein-Avidan and E. Putterman, *On unbalanced difference bodies and Godbersen's conjecture*, arXiv:2412.05308; *Proceedings of the American Mathematical Society* 153 (2025), 5345–5359. https://arxiv.org/abs/2412.05308
3. F. Fryš and J. Kotrbatý, *Around higher-order Godbersen conjectures*, arXiv:2609.08612, first public version 2026-09-08. https://arxiv.org/abs/2609.08612
4. Classical Legendre-polynomial generating function and the location and simplicity of Legendre zeros, e.g. G. Szegő, *Orthogonal Polynomials*, 4th edition, American Mathematical Society, 1975, Chapters 3–4.
