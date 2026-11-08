# Complete Ehrhart numerator phase diagram for products of Reeve tetrahedra

## Finding
For every pair of positive integers \(m,n\), the six-dimensional Cartesian product of Reeve tetrahedra has an explicit Ehrhart \(h^*\)-polynomial. The exact formula yields a complete classification of unimodality, log-concavity and real-rootedness. All such products are unimodal; log-concavity holds precisely under a finite arithmetic threshold; real-rootedness holds only for three ordered pairs.

Let \(a=m-1\), \(b=n-1\), \(t=ab\), \(u=10(a+b)\). Then
\[
H_{m,n}(z)=(1+z)\left(1+8z+(t+u+1)z^2+8tz^3+tz^4\right).
\]
Equivalently its degree-at-most-six coefficient vector is
\[
(h_0^*,\ldots,h_6^*)=(1,9,t+u+9,9t+u+1,9t,t,0).
\]
The coefficient sequence is unimodal for every pair. It is log-concave (with no internal zeros in its actual support) if and only if
\[
ab+10(a+b)\le 72.
\]
It has only real zeros if and only if
\[
(m,n)\in\{(1,1),(1,2),(2,1)\}.
\]
In the three real-rooted cases, all roots are simple and negative.

## Assumptions and scope
The Reeve tetrahedron is \(R_m=\operatorname{conv}\{(0,0,0),(1,0,0),(0,1,0),(1,1,m)\}\subset\mathbb R^3\) for an integer \(m\ge1\). The product \(R_m\times R_n\) uses the standard ambient lattice \(\mathbb Z^6\). Its Ehrhart function is \(L_{m,n}(k)=|(k(R_m\times R_n))\cap\mathbb Z^6|\), for integers \(k\ge0\). Define \(H_{m,n}\) by \(\sum_{k\ge0}L_{m,n}(k)z^k=H_{m,n}(z)/(1-z)^7\). Unimodality and log-concavity refer to the coefficient sequence up to the actual degree of \(H\), without appending a trailing zero; the displayed degree-six coefficient is zero. Real-rooted means all complex zeros (counted with multiplicity) are real.

## Proof
**Exact numerator.** A standard exact enumeration of the Reeve tetrahedron gives
\[
L_m(k)=\frac{mk^3+6k^2+(12-m)k+6}{6},\qquad
h^*_{R_m}(z)=1+(m-1)z^2.
\]
For an independent check, barycentric coordinates of \((x,y,w)\in kR_m\) give the integer inequalities \(0\le w\le mk\), \(mx\ge w\), \(my\ge w\), and \(m(x+y)\le mk+w\). Counting their integer solutions gives the same formula. The product identity \(L_{m,n}(k)=L_m(k)L_n(k)\) follows from the Cartesian lattice. In dimension six, the numerator coefficients satisfy
\[
h_j^*=\sum_{r=0}^j(-1)^r\binom7r L_m(j-r)L_n(j-r),\qquad 0\le j\le6.
\]
Substitution and ordinary polynomial expansion yield the displayed seven-term vector and factorization. This works at \(m=1\) or \(n=1\), not only for nonunimodular factors.

**Unimodality.** Write the six possible nonzero coefficients as \(c_0,\ldots,c_5\). Then \(1=c_0\le c_1=9\le c_2=t+u+9\); moreover \(c_3-c_2=8(t-1)\), and \(c_3=9t+u+1\ge c_4=9t\ge c_5=t\). Because \(t=ab\) is a nonnegative integer, if \(t=0\) the peak is \(c_2\) and if \(t\ge1\) the peak is \(c_3\), with a plateau when \(t=1\). Thus every product is unimodal.

**Log-concavity.** All coefficients through the actual degree are positive. The four nontrivial adjacent-minor differences are
\[
\begin{aligned}
c_1^2-c_0c_2&=72-t-u,\\
c_2^2-c_1c_3&=(t+u)^2-63t+9u+72,\\
c_3^2-c_2c_4&=72t^2+9tu+u^2-63t+2u+1,\\
c_4^2-c_3c_5&=t(72t-u-1).
\end{aligned}
\]
For \(a,b\ge0\), AM--GM gives \(u=10(a+b)\ge20\sqrt t\), hence \(u^2\ge400t\). The second and third displayed expressions are strictly positive. The fourth is zero when \(t=0\), where its trailing coefficients are absent; if \(t>0\), then \(a,b\ge1\) and
\[
72t-u-1=ab\left(72-\frac{10}{a}-\frac{10}{b}-\frac{1}{ab}\right)>0.
\]
Consequently the only restrictive condition is \(72-t-u\ge0\), as claimed. Equality at this threshold is allowed.

**Real-rootedness.** Remove the factor \(1+z\) and put
\[
Q(z)=1+8z+(t+u+1)z^2+8tz^3+tz^4.
\]
If \(t=0\), then \(Q\) is quadratic with discriminant \(60-4u=60-40(a+b)\); it is real-rooted precisely when the nonnegative integer \(a+b\) is at most one. In these cases its two roots are negative, distinct, and unequal to \(-1\).

If \(t>0\), both \(a,b\ge1\). Suppose \(Q\) has four real zeros. Since its coefficients are strictly positive, all four zeros must be negative. Therefore \(Q(z)=\prod_{i=1}^4(1+\lambda_i z)\) for four positive real numbers \(\lambda_i\). The linear coefficient yields \(\sum\lambda_i=8\). The quadratic coefficient is the pairwise product sum; the elementary bound
\[
\sum_{i<j}\lambda_i\lambda_j\le\frac{3}{8}\left(\sum_i\lambda_i\right)^2=24
\]
forces \(t+u+1\le24\). But when \(a+b\ge3\), one has \(t+u+1\ge2+30+1=33\), a contradiction. The remaining positive case is \(a=b=1\), for which \(Q(z)=z^4+8z^3+22z^2+8z+1\). For every nonzero real \(z\), writing \(w=z+z^{-1}\) gives
\[
Q(z)/z^2=(w+4)^2+4>0.
\]
Also \(Q(0)=1\), so \(Q\) has no real root at all. The asserted three-pair classification follows.

## Verification
The standalone file `verify_reeve_products.py` checks the Reeve point counts by direct integer-coordinate enumeration against the cubic formula for 81 parameter/dilation pairs. It compares the six-dimensional numerator obtained by finite differences of \(L_m(k)L_n(k)\) against the closed coefficient formula for 576 parameter pairs, and checks unimodality and the exact log-concavity condition on those same 576 pairs (1,152 assertions). All 1,809 checks pass. The infinite-parameter statements rely on the algebraic proof above, not finite testing. Run with `python3 verify_reeve_products.py`; it uses only Python's standard library.

## Relationship to prior work
Reeve's tetrahedron is the classical empty lattice tetrahedron; its Ehrhart polynomial and sparse numerator are standard. Liu, *Ehrhart Properties under Operations on Lattice Polytopes* (first submitted 5 October 2026), studies closure of Ehrhart properties under Cartesian products. Its Theorem 2.2 gives forward preservation of log-concavity and real-rootedness **when both factors already have those properties**. Nonunimodular Reeve tetrahedra have \(h^*=1+(m-1)z^2\), with an internal zero, so those preservation hypotheses do not apply. Liu's Section 2 also shows that unimodality is not preserved for arbitrary products of unimodal lattice polytopes. The present complete classification identifies a contrasting universal repair of unimodality for a canonical nonunimodal family and sharp thresholds for two stronger properties.

Liu--Tao--Xin's *Explicit Construction of Polytopes whose Ehrhart Polynomials Realize any Given Sign Pattern* uses Reeve factors in Cartesian constructions to prescribe Ehrhart **coefficient signs**, rather than classify \(h^*\) shapes of two Reeve factors. Liu--Mao's *Preservation of log-concavity under Hadamard products* gives a general conditional preservation theorem; it does not directly apply to the non-log-concave Reeve inputs. No claim is made about arbitrary products, three or more Reeve factors, or other empty simplices.

## Limitations
Novelty is asserted only relative to the specifically inspected sources and research-record searches; exhaustive historical priority is not proved. The result concerns the standard lattice product of **exactly two** Reeve tetrahedra and the three stated numerator properties. The proof and reproducibility script are provided; there has been no independent mathematical audit.

## References
- Feihu Liu, *Ehrhart Properties under Operations on Lattice Polytopes*, arXiv:2610.06338, version publicly submitted 2026-10-05. https://arxiv.org/abs/2610.06338 . Particularly Section 2, Theorem 2.2, and Section 7.2.
- Feihu Liu, Sihao Tao, Guoce Xin, *Explicit Construction of Polytopes whose Ehrhart Polynomials Realize any Given Sign Pattern*, arXiv:2605.23544, first public submission 2026-05-22. https://arxiv.org/html/2605.23544v2 .
- Yanxin Liu and Jianxi Mao, *Preservation of log-concavity under Hadamard products*, arXiv:2609.11589, first public submission 2026-09-10. https://arxiv.org/abs/2609.11589 .
- J. E. Reeve, *On the Volume of Lattice Polyhedra*, Proc. London Math. Soc. (3) 7 (1957), 378--395.
