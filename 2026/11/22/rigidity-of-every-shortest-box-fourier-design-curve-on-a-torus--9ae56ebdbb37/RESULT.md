# Rigidity of every shortest box-Fourier design curve on a torus

## Finding

Fix integers \(d\ge 2\) and \(t\ge 1\), and put \(b=t+1\) and \(L_*=(\sum_{j=0}^{d-1} b^{2j})^{1/2}\). Every closed rectifiable unit-speed curve on \(\mathbb T^d\) that integrates exactly all box-frequency characters \(e^{2\pi i\langle m,x\rangle}\) with \(\|m\|_\infty\le t\) and has length exactly \(L_*\) is a translated straight Korobov geodesic. More precisely, after an arclength parametrization on \([0,L_*]\), every lift has the form

\[
\gamma(s)=x_0+\frac{s}{L_*}v,
\qquad \{|v_1|,\ldots,|v_d|\}=\{1,b,b^2,\ldots,b^{d-1}\}.
\]

Conversely, every such lift is an exact box-frequency \(t\)-design of length \(L_*\). Therefore the shortest-curve inequality of Ehler has **only** the signed, coordinate-permuted Korobov minimizers; this is a rigidity classification, not a new claim about the already established sharp lower bound. There are \(2^d d!\) possible oriented integer winding vectors, and orientation reversal identifies \(v\) and \(-v\).

## Assumptions and scope

The torus is \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\) with its quotient Euclidean metric. A closed rectifiable curve has a continuous, absolutely continuous unit-speed lift \(\gamma:[0,L]\to\mathbb R^d\), satisfying \(\gamma(L)-\gamma(0)\in\mathbb Z^d\). Exactness means

\[
\frac1L\int_0^L e^{2\pi i\langle m,\gamma(s)\rangle}\,ds=0
\quad\text{for every }m\in\mathbb Z^d\setminus\{0\}\text{ with }\|m\|_\infty\le t.
\]

No differentiability beyond absolute continuity of the arclength lift, no embeddedness and no prescribed winding class are required. The previously established lower bound is \(L\ge L_*=\sqrt{(b^{2d}-1)/(b^2-1)}\) [1]. The claim here is the **complete equality case** of this bound.

## Proof

**1. The sharp spectral inequality and saturation.** Set \(N=b^d\) and \(A=(\{0,\ldots,t\}-t/2)^d\). The characters \(f_a(s)=e^{2\pi i\langle a,\gamma(s)\rangle}\), \(a\in A\), are orthonormal in \(L^2([0,L],ds/L)\), because each difference of two elements of \(A\) is an integer box frequency. Since \(\sum_{a\in A}aa^\top=(Nt(t+2)/12)I_d\) and \(\|\gamma'(s)\|=1\) almost everywhere,

\[
\frac1N\sum_{a\in A}\frac1L\int_0^L|f_a'(s)|^2ds=\frac{4\pi^2t(t+2)}{12}.
\]

Write \(v=\gamma(L)-\gamma(0)\in\mathbb Z^d\). When \(t\) is even, all \(f_a\) are periodic; when \(t\) is odd, they are periodic if \(\sum_jv_j\) is even and antiperiodic otherwise. Expand them in the corresponding integer or half-integer Fourier eigenbasis on the parameter interval. If \(c_{a,k}\) is a Fourier coefficient, Bessel's inequality and Parseval give \(0\le p_k:=\sum_{a\in A}|c_{a,k}|^2\le1\), and \(\sum_kp_k=N\). The sum of eigenvalue squares weighted by \(p_k\) is at least the sum over the \(N\) smallest squared Fourier frequencies. In the periodic case with \(N\) odd, or the antiperiodic case with \(N\) even, this minimum divided by \(N\) is \((N^2-1)/12\). In the periodic case with \(N\) even it is \((N^2+2)/12\), strictly greater.

At \(L=L_*\), the sharp bound is saturated. Thus the periodic-even-\(N\) case is impossible, and every \(f_a\) has zero Fourier coefficients outside the *unique* band of the \(N\) lowest squared frequencies (a consecutive block of integers for odd \(N\), or of half-integers for even \(N\)). Indeed, any mass outside that band would strictly increase the weighted sum because the least squared frequency outside exceeds the greatest one inside. Consequently every \(f_a\) is a finite trigonometric polynomial in this band, and the \(N\) orthonormal functions fill all \(N\) frequency slots.

**2. Unimodular-polynomial rigidity.** A finite Laurent polynomial \(P(z)=\sum_{k=r}^{s}c_kz^k\) of constant modulus on \(|z|=1\) is a monomial: otherwise take the minimal and maximal exponents with nonzero coefficients, \(r<s\); the Fourier coefficient of \(|P|^2\) at exponent \(s-r\) is the single nonzero term \(c_s\overline{c_r}\), contradicting constancy. The same applies to half-integer Fourier bands after multiplication by one fixed unimodular half-frequency. Since \(|f_a(s)|=1\), there are real phases \(\theta_a\) and distinct allowed frequencies \(\kappa_a\) such that

\[
f_a(s)=e^{i\theta_a}e^{2\pi i\kappa_a s/L_*}.
\]

For each coordinate \(j\), select adjacent indices \(a,a+e_j\in A\), which exist because \(t\ge1\). Their ratio is \(e^{2\pi i\gamma_j(s)}\), hence

\[
e^{2\pi i\gamma_j(s)}=C_j e^{2\pi i (\kappa_{a+e_j}-\kappa_a)s/L_*}.
\]

Both frequencies lie in the same integer/half-integer lattice; therefore their difference is an integer. Continuity of the lift forces \(\gamma_j(s)=x_{0,j}+v_js/L_*\) for every \(s\), where \(v_j\in\mathbb Z\). Thus **the entire minimizing curve is affine**, and unit speed gives \(L_*^2=\sum_jv_j^2\).

**3. Unique positional digit representation.** With \(\gamma(s)=x_0+(s/L_*)v\), each \(f_a\) has frequency \(\kappa_a=\langle a,v\rangle\). All \(N\) distinct values occupy exactly the \(N\) consecutive Fourier frequency slots from Step 1. Replace each \(v_j\) by \(w_j=|v_j|\) and reverse its digit variable when \(v_j<0\). Translating the index cube gives

\[
\left\{\sum_{j=1}^d u_jw_j:u_j\in\{0,\ldots,t\}\right\}=\{0,1,\ldots,N-1\}
\]

with each sum occurring exactly once. In particular every \(w_j\) is positive. Sort the weights \(w_1\le\cdots\le w_d\). The value \(1\) must be representable, so \(w_1=1\). Inductively, if \(w_1,\ldots,w_k\) are \(1,b,\ldots,b^{k-1}\), their allowed digit sums are exactly \(0,\ldots,b^k-1\). Any next weight less than \(b^k\) would repeat an existing sum, while a next weight greater than \(b^k\) would leave the required value \(b^k\) unrepresentable. Hence \(w_{k+1}=b^k\), proving the claimed multiset of absolute winding coordinates.

**4. Converse.** For \(v\) a signed permutation of \((1,b,\ldots,b^{d-1})\), consider a box frequency \(m\in\mathbb Z^d\), \(\|m\|_\infty\le t\). If \(\langle m,v\rangle=0\), reduction modulo \(b\) forces the digit corresponding to weight \(1\) to vanish because its absolute value is less than \(b\); divide by \(b\) and repeat. Hence \(m=0\). Every nonzero box-frequency character has zero average along the closed straight curve. Its speed is one under the indicated parametrization and its length is \(\|v\|_2=L_*\). This proves both directions.

## Verification

A standalone exact-integer diagnostic, `CHECK.py`, enumerates all nonnegative integer winding vectors with squared length \(L_*^2\), then independently checks the box-frequency annihilator condition, for \(d=2,1\le t\le7\); \(d=3,1\le t\le4\); and \(d=4,t=1,2\). Its 13 complete finite bounded searches examine 545 sphere vectors and identify exactly 86 positive-orthant minimizers, all permutations of the predicted radix vector. The script separately checks the exact consecutive-digit representation of every predicted vector. Run `python3 CHECK.py` using Python's standard library. These finite checks support, but do not replace, the proof for arbitrary integers \(d,t\) and all rectifiable curves.

## Relationship to prior work

Ehler [1, Theorem 2.1 and Proposition 2.4, pages 3–7] proves the sharp minimum length and demonstrates equality for the standard Korobov family. Its Fourier-energy proof supplies the needed spectral bound, but does not state or prove a complete classification of all minimizers. The present result extracts the equality structure, proves that a general rectifiable minimizer must be an affine geodesic, and then classifies its integer winding vector via unique consecutive radix sums. Kunis [2, Section 4] constructs Korobov curves and studies exactness, covering and length, but does not classify arbitrary length minimizers. The sphere-specific results of King and Mixon [3] concern a different underlying manifold. The length formula and existence of Korobov minimizers are expressly credited as established facts rather than new claims.

## Limitations

This rigidity statement applies to **closed**, **unweighted arclength**, **box-frequency** design curves at **exact equality** in the sharp length bound. It does not classify weighted curve quadrature, near-minimizers, total-degree or hyperbolic-cross designs, or nonrectifiable parameterizations. Independent external validation is not asserted. Earlier literature phrased as equality-case rigidity or as a rearrangement theorem for Fourier moment curves may exist outside the inspected sources.

## References

1. M. Ehler, *Optimal bounds for design curves on the torus*, arXiv:2611.03362, first posted 2026-11-02. https://arxiv.org/abs/2611.03362 . Especially Theorem 2.1, Proposition 2.4 and the proof on pages 3–7.
2. S. Kunis, *Positive quadrature and mobile sampling of multivariate trigonometric polynomials*, arXiv:2608.11915, first posted 2026-08-12. https://arxiv.org/abs/2608.11915 . Especially Theorem 4.1, Remark 4.2 and Lemma 4.3.
3. E. J. King and D. G. Mixon, *Short spherical \(t\)-design curves*, arXiv:2607.15386, first posted 2026-07-16. https://arxiv.org/abs/2607.15386 . Geometrically related but not a torus-result source.
