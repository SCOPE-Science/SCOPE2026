# Universal fixed-gap condensation of rational Hartogs Bergman-kernel zeros

## Finding
For a fixed integer \(k\ge4\), let \(m>k\) run through integers with \(\gcd(m,k)=1\), and set \(n=m-k\). Write \(Q_{m,n}\) for the degree-\(2k\) palindromic *oblique-diagonal Bergman numerator* of the rational Hartogs triangle \(H_{m/n}\), normalized exactly as in the references below. The following coefficientwise limit, with an entrywise error of order \(O_k(m^{-2})\), holds:
\[
\frac{6k^2}{m^3}Q_{m,m-k}(z)
 = (z^2+4z+1)(1+z+\cdots+z^{k-1})^2+O_k(m^{-2}).
\]
The error is uniform on any fixed compact subset of the complex plane. Put \(\beta=-2+\sqrt3\) and \(\omega_j=e^{2\pi i j/k}\) for \(1\le j<k\). For every sufficiently large admissible \(m\), all \(2k\) zeros are simple. Exactly \(k\) lie in the punctured unit disk: one zero \(\beta_m\) satisfies \(|\beta_m-\beta|=O_k(m^{-2})\), and each remaining interior zero \(u_{m,j}\) is uniquely associated to \(\omega_j\), with **sharp order of Euclidean approach**
\[
 0<c_k\le m|u_{m,j}-\omega_j|\le C_k<\infty
 \qquad(1\le j<k).
\]
Here \(c_k,C_k\) are positive constants depending only on the fixed gap \(k\), not on \(m\) or \(j\). The exterior roots have reciprocal-conjugate pairings \(1/\overline{\beta_m}\) and \(1/\overline{u_{m,j}}\). Hence the interior zero multiset converges, with multiplicity, to \(\{\beta,\omega_1,\ldots,\omega_{k-1}\}\). Each interior zero yields an actual off-diagonal Bergman-kernel zero on \(H_{m/n}\times H_{m/n}\).

## Assumptions and scope
Let \(H_{m/n}=\{(z_1,z_2)\in\mathbb C^2:|z_1|^m<|z_2|^n<1\}\). For positive coprime integers \(m>n\), let \(s=z_1\overline{w_1}\), \(t=z_2\overline{w_2}\), and use the published kernel representation
\[
 K_{m/n}(z,w)=\frac{P_{m,n}(s,t)}{m\pi^2(1-t)^2(t^n-s^m)^2},
 \qquad Q_{m,n}(z)=z^{1-2n}P_{m,n}(z,z).
\]
For \(A\in\mathbb Z\), put \(W_m(A)=\max(0,m-|A|)\). The precise coefficients are those in the published centered formula
\[
 Q_{m,n}(z)=\sum_{A,B\in\mathbb Z}W_m(A)W_m(nA+mB)z^{m-n+A+B}.
\]
The sum is finite, and its coefficients are nonnegative, real and reciprocal. The theorem is about **fixed \(k\ge4\) followed by \(m\to\infty\)**, not a uniform joint limit with growing \(k\). No claim that the roots occur at exactly the limiting angles is made.

## Proof
**1. Exact one-dimensional trapezoid formula.** For a fixed \(j\in\{0,\ldots,2k\}\), set \(A+B=j-k\) in the centered numerator. Since \(n=m-k\),
\[
 nA+mB=m(j-k)-kA.
\]
Writing \(\ell=A+m\), the nonzero summands have \(1\le\ell\le2m-1\), and the coefficient \(q_j=[z^j]Q_{m,m-k}(z)\) is exactly
\[
 q_j=m^2\sum_{\ell=1}^{2m-1}
 T(\ell/m-1)T(j-k\ell/m),\qquad
 T(x)=(1-|x|)_+.
\tag{1}
\]
This follows directly from the finite centered formula and involves no approximation. Note that the formula is valid at every admissible \(m\), not only asymptotically.

**2. A cubic-scale limiting polynomial with a quadratic relative remainder.** Write \(f_j(x)=T(x-1)T(j-kx)\). On \([0,2]\), each \(f_j\) is continuous and piecewise quadratic with finitely many corners (for fixed \(k\)), vanishes at the two endpoints, and has bounded piecewise second derivative and finite derivative jumps. The composite trapezoid estimate, obtained by treating the finitely many corner cells separately, therefore gives
\[
 \frac1m\sum_{\ell=1}^{2m-1}f_j(\ell/m)
 =\int_0^2 f_j(x)\,dx+O_k(m^{-2}).
\tag{2}
\]
The integral is explicitly
\[
 I_{k,j}=\begin{cases}
 1/(6k^2),&j=0,2k,\\
 j/k^2,&1\le j<k,\\
 1/k-1/(3k^2),&j=k,\\
 (2k-j)/k^2,&k<j<2k.
 \end{cases}
\tag{3}
\]
Indeed, for \(1\le j<k\) the support of the second tent is on \([0,1]\), where \(T(x-1)=x\); the center is \(j/k\), and the tent has integral \(1/k\). For \(j=0\), integrate \(x(1-kx)\) from \(0\) to \(1/k\). For \(j=k\), integrate \(2(1-x)(1-kx)\) from \(0\) to \(1/k\). Reflection about \(x=1\) handles \(j>k\).

Equations (1)--(3) give \(q_j=m^3I_{k,j}+O_k(m)\). The polynomial with coefficients \(6k^2I_{k,j}\) factors as
\[
 \sum_{j=0}^{2k}6k^2I_{k,j}z^j
 =(z^2+4z+1)\left(\sum_{r=0}^{k-1}z^r\right)^2.
\tag{4}
\]
Comparing the explicit coefficients proves the identity. Summing the finitely many coefficient estimates gives the asserted locally uniform \(O_k(m^{-2})\) remainder after rescaling.

**3. Root matching and quantitative upper bounds.** The polynomial in (4) has simple roots \(\beta=-2+\sqrt3\) and \(\beta^{-1}=-2-\sqrt3\), and double roots at the \(k-1\) distinct nontrivial \(k\)-th roots of unity. All are isolated. The argument principle (or Rouché's theorem) applied on fixed small disjoint circles shows that, for sufficiently large admissible \(m\), precisely one root of the rescaled polynomial is near each simple root and precisely two are near each double root. Applying the same theorem on circles of radii \(M_k/m^2\) about the simple roots and \(M_k/m\) about the double roots gives the stated upper bounds: on such circles the limiting polynomial has modulus bounded below by a constant times the radius or its square, respectively, while the perturbation is bounded by \(E_k/m^2\). Choose the fixed \(M_k\) large enough.

**4. Which side of the unit circle, and simplicity.** The 2026 positivity theorem of Deng and Fu states that \(e^{-ik\theta}Q_{m,m-k}(e^{i\theta})>0\) for all real \(\theta\). Therefore no root lies on the unit circle. The polynomial is real and palindromic, so the map \(u\mapsto1/\overline{u}\) preserves its root multiset. For each \(\omega_j\), this map takes a sufficiently small neighborhood of \(\omega_j\) into itself. Since exactly two roots, counted with multiplicity, occupy that neighborhood and neither can be fixed by the map, they are one distinct interior/exterior pair, each simple. The simple root near \(\beta\) lies inside, and the root near \(\beta^{-1}\) lies outside. These account for all \(2k\) roots and give exactly one interior root per limiting \(\omega_j\).

**5. Matching lower bounds at the boundary roots.** Deng and Fu's stronger inequality states
\[
 |Q_{m,m-k}(\omega_j)|\ge m\sin^2(\pi j/k)>0.
\tag{5}
\]
Factor \(Q\) into its \(2k\) roots. Its leading coefficient is \(m^3/(6k^2)+O_k(m)\) by (1)--(3), and all roots remain in a bounded set. At \(\omega_j\), the two nearby factors are \(\omega_j-u_{m,j}\) and \(\omega_j-1/\overline{u_{m,j}}\); their absolute values are \(d\) and \(d/|u_{m,j}|\) with \(d=|\omega_j-u_{m,j}|\). Since \(|u_{m,j}|\to1\), the product of the other \(2k-2\) factors is bounded above by a constant depending only on \(k\). Consequently \(|Q(\omega_j)|\le M_km^3d^2\). Combined with (5) and the finite positive minimum of \(\sin^2(\pi j/k)\), this gives \(d\ge c_k/m\). Thus the Euclidean scale \(m^{-1}\) is two-sided sharp.

**6. Realization as kernel zeros.** Each \(u_{m,j}\) and \(\beta_m\) has modulus strictly between zero and one, since \(Q_{m,n}(0)>0\). Write any such root as \(u=\rho e^{i\phi}\), and choose \(z=(\sqrt\rho,\sqrt\rho)\), \(w=(\sqrt\rho e^{-i\phi},\sqrt\rho e^{-i\phi})\). Both lie in \(H_{m/n}\), their coordinate products satisfy \(s=t=u\), and the kernel denominator does not vanish, while \(P_{m,n}(u,u)=u^{2n-1}Q_{m,n}(u)=0\). This is an off-diagonal kernel zero.

## Verification
Execute `python CHECK.py` from the directory containing this file. The checker recomputes exact finite centered-numerator coefficients in two independent summation forms for all coprime small gaps and sizes, confirms palindromicity and \(Q_{m,n}(1)=m^3\), compares the predicted limiting polynomial in several large fixed-gap examples, and checks finite root locations. These checks are reproducible but do **not** prove the asymptotic theorem; steps 1--6 above supply the infinite proof.

## Relationship to prior work
Edholm and Mathew introduce the oblique-diagonal polynomials, prove the reciprocal symmetry, and explicitly discuss the limiting roots in gaps one and two (their Remarks 4.6 and 4.18). Those small-gap limit statements are **prior art**, not a contribution here. Deng and Fu prove the unit-circle positivity and exact number of interior roots for every coprime pair, which this proof uses as an input. A separately published gap-three result gives a sharper radial constant in that special case. The contribution here is the **uniform-in-arithmetic-residue, every-fixed-gap \(k\ge4\) limiting factorization and two-scale root geometry**, including sharp-order separation at every nontrivial root of unity. Neither existence nor total root count alone implies that geometry.

## Limitations
The constants implicit in the rate bounds depend on the fixed integer gap and are not optimized. No explicit directional/radial asymptotic coefficient is claimed, only sharp Euclidean order. The argument does not treat gaps growing simultaneously with the denominator, arbitrary off-diagonal zeros away from the chosen slice, or irrational domain exponents. Independent mathematical audit and publication-priority verification have not been performed.

## References
1. L. D. Edholm and V. T. Mathew, *Arithmetic properties and zeros of the Bergman kernel on a class of quotient domains*, arXiv:2505.20489v1 (first posted 2025-05-26), especially Theorem 1.5 and Remarks 4.6, 4.18; open-access journal text: https://link.springer.com/article/10.1007/s00209-026-04059-8 .
2. G. Deng and Q. Fu, *Bergman Kernel Zeros on Rational Hartogs Triangles*, arXiv:2611.07480v1 (first posted 2026-11-05), especially Lemma 2.1, Theorem 1.1, Proposition 3.2, and Proposition 4.1: https://arxiv.org/html/2611.07480v1 .
3. published-finding corpus, *Cubic-root condensation of diagonal Bergman-kernel zeros in gap-three Hartogs triangles*, 2026-10-11, public record ID `2026/10/11/SCOPE-cubic-root-condensation-of-diagonal-bergman-kernel-zeros-in-gap--78891bb4627f` (special gap-three result; no claim here of its novelty).
