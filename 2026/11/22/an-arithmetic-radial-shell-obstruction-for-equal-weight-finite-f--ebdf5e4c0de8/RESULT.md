# An arithmetic radial-shell obstruction for equal-weight finite Fock frames

## Finding
Let \(m\ge2\) be an integer and \(n=2m-1\). In the degree-\(n\) Bargmann–Fock polynomial Hilbert space
\[
\mathcal P_n=\operatorname{span}\{e_k(z)=z^k/\sqrt{k!}:0\le k\le n\},\qquad
\left\|\sum_{k=0}^n c_ke_k\right\|^2=\sum_{k=0}^n|c_k|^2,
\]
consider a nonempty finite multiset of sample locations \(Z=(z_1,\ldots,z_M)\subset\mathbb C\) and the equally weighted, Gaussian-compensated observation form
\[
\mathcal S_Z(f)=\sum_{s=1}^M e^{-|z_s|^2}|f(z_s)|^2.
\]
If \(\mathcal S_Z(f)=C\|f\|^2\) for every \(f\in\mathcal P_n\) with any \(C>0\), **then the locations occupy at least \(m+1\) distinct radii**. This impossibility holds with no restrictions on angular positions, total number of samples, or repeated sites. The same conclusion holds with any *common* strictly positive external weight multiplying all summands.

The threshold \(m\) is nevertheless **attainable with individually adjustable positive weights**: there are exactly \(m\) distinct positive radii and \(m(n+1)\) distinct locations, arranged as regular \((n+1)\)-gons, with a strictly positive weight at each sample, giving an exact Parseval identity. Thus the minimal number of radii for *positively weighted* tight Gaussian-coherent sampling is exactly \(m\), while the equal-external-weight minimum is at least \(m+1\). No assertion of an equal-weight construction with \(m+1\) radii is made.

The obstruction has an arithmetic origin: exactness at \(m\) radii forces the squared radii to be the distinct positive zeros of the degree-\(m\) Laguerre polynomial and the effective radial masses to be algebraic Gauss–Laguerre weights, while equal external sample weights demand that their ratios contain the exponential of a nonzero algebraic number.

## Assumptions and scope
The Gaussian factor is \(e^{-|z_s|^2}\), corresponding to measurements of \(e^{-|z_s|^2/2}f(z_s)\). These are full-Fock compensated coherent evaluations, **not** evaluations normalized by the reproducing kernel of the truncated polynomial space. Equality is an operator identity on the entire complex space \(\mathcal P_n\), not only on monomials. An indexed sample may repeat a point; the number of distinct *radii* counts the distinct values \(|z_s|\), including zero if present. Equal weight means a single positive scalar prefactor across all indexed observations; variable-weight sampling permits an individual strictly positive prefactor per observation. The result covers all odd degrees \(n\ge3\) and arbitrary finite sample counts. At degree one, a single circle with a regular two-point polygon is already equal-weight tight, so the lower bound excluding \(m\) radii is intentionally not asserted for \(m=1\).

## Proof
**1. Reduce the exact frame equations to radial moments.** Let \(x_1,\ldots,x_r\ge0\) be the distinct squared radii and let \(q_j\in\mathbb Z_{>0}\) count indexed samples on the \(j\)-th radius. Evaluating the asserted tightness identity at each unit-norm monomial \(e_k\), for \(0\le k\le2m-1\), gives
\[
\sum_{j=1}^r q_je^{-x_j}\frac{x_j^k}{k!}=C.
\]
Set \(\alpha_j=q_je^{-x_j}/C>0\). Since \(\int_0^\infty e^{-x}x^k\,dx=k!\), these identities are exactly
\[
\sum_{j=1}^r\alpha_j x_j^k=\int_0^\infty x^ke^{-x}\,dx
\quad (k=0,\ldots,2m-1).\tag{1}
\]
They are necessary for *every* angular configuration, even one for which the off-diagonal frame equations fail. Thus excluding (1) excludes tightness unconditionally.

**2. Fewer than \(m\) radii are impossible even with free positive weights.** If \(r<m\), put \(Q(x)=\prod_{j=1}^r(x-x_j)\). Its square has degree \(2r\le2m-2\), so (1), by linearity, would imply
\[
0=\sum_j\alpha_jQ(x_j)^2=\int_0^\infty Q(x)^2e^{-x}\,dx>0,
\]
a contradiction. This argument holds for arbitrary positive radial masses.

**3. Exactly \(m\) radii force algebraic nodes and weights.** Suppose \(r=m\) and define the monic polynomial \(P(x)=\prod_{j=1}^m(x-x_j)\). For each \(0\le h<m\), the product \(x^hP(x)\) has degree at most \(2m-1\). By (1),
\[
\int_0^\infty x^hP(x)e^{-x}\,dx
=\sum_{j=1}^m\alpha_jx_j^hP(x_j)=0.\tag{2}
\]
There is exactly one monic degree-\(m\) polynomial satisfying (2): the lower \(m\) coefficients solve a linear system with Gram matrix \(H_{hk}=(h+k)!\) for \(0\le h,k<m\); this is positive definite because \(\int_0^\infty |\sum c_kx^k|^2e^{-x}\,dx>0\) for every nonzero coefficient vector. Hence the solution has **rational coefficients**, since the Gram matrix and right-hand side consist of integers. It is the monic multiple \((-1)^m m!L_m(x)\) of the ordinary Laguerre polynomial. In particular every distinct \(x_j\) is an algebraic number.

The first \(m\) equations (1) form a nonsingular Vandermonde system for \((\alpha_1,\ldots,\alpha_m)\), with algebraic entries \(x_j^k\) and rational right-hand side \(k!\). Consequently each \(\alpha_j\) is a **strictly positive algebraic number**. For any distinct indices \(i,j\), their defining formulas give
\[
e^{x_i-x_j}=\frac{q_i\alpha_j}{q_j\alpha_i}.\tag{3}
\]
The right side is nonzero algebraic, because the multiplicities \(q_i,q_j\) are positive integers. The left side is transcendental by the Hermite–Lindemann theorem, since \(x_i-x_j\ne0\) is algebraic. Because \(m\ge2\), choose such a pair; the contradiction proves the equal-weight obstruction.

**4. Construct a positive weighted tight sampler on exactly \(m\) radii.** Let \(P_m=(-1)^mm!L_m\) be the monic polynomial defined by (2). The standard real orthogonal-polynomial root argument shows it has \(m\) distinct roots \(0<x_1<\cdots<x_m\): otherwise the product of its distinct sign-changing factors in \((0,\infty)\), a polynomial of degree less than \(m\), would have a nonzero constant-sign product with \(P_m\) on \((0,\infty)\), contradicting orthogonality. Let \(\ell_j\) be the degree-\(m-1\) Lagrange polynomial taking values \(\ell_j(x_i)=\mathbf1_{i=j}\), and define \(\alpha_j=\int_0^\infty\ell_j(x)e^{-x}\,dx\).

Every polynomial \(F\) of degree at most \(2m-1\) splits uniquely into \(F=P_mQ+R\), with \(\deg Q,\deg R\le m-1\). Orthogonality kills \(\int P_mQe^{-x}\,dx\), and the values at the roots are those of \(R\). Lagrange interpolation of \(R\) therefore proves the exact quadrature identity
\[
\int_0^\infty F(x)e^{-x}\,dx=\sum_{j=1}^m\alpha_jF(x_j).\tag{4}
\]
Applying (4) to \(F=\ell_j^2\), whose degree is at most \(2m-2\), yields \(\alpha_j=\int_0^\infty\ell_j(x)^2e^{-x}\,dx>0\). Hence (4) provides a genuinely positive quadrature rule.

Put \(Q=n+1=2m\) and \(\zeta=e^{2\pi i/Q}\). On each radius \(\sqrt{x_j}\), take the \(Q\) distinct points \(z_{j,s}=\sqrt{x_j}\,\zeta^s\) (\(0\le s<Q\)) and assign each the **external** weight
\[
w_{j,s}=\frac{\alpha_je^{x_j}}{Q}>0.
\]
For \(0\le k,l\le n\), the discrete angular identity \(Q^{-1}\sum_{s=0}^{Q-1}\zeta^{s(k-l)}=\mathbf1_{k=l}\) annihilates all off-diagonal weighted frame entries. The diagonal at degree \(k\) becomes \(\sum_j\alpha_jx_j^k/k!=1\) by (4). Thus
\[
\boxed{\sum_{j=1}^m\sum_{s=0}^{Q-1}w_{j,s}e^{-|z_{j,s}|^2}|f(z_{j,s})|^2=\|f\|^2\quad(f\in\mathcal P_n).}
\]
Step 2 proves that no positive-weight design can use fewer distinct radii, so \(m\) is the exact positive-weight minimum.

**5. Smallest obstructed odd degree.** At \(n=3\), there are \(m=2\) forced squared radii \(x_\pm=2\pm\sqrt2\) and corresponding Gauss–Laguerre weights \(\alpha_\pm=\tfrac12\mp\tfrac{\sqrt2}{4}\). Their ratio is algebraic, whereas equal external weights would require an algebraic multiple of \(e^{2\sqrt2}\) to equal it. Thus even unrestricted angular oversampling on two circles cannot produce an equal-weight exact tight frame of degree three. The eight-site positively weighted construction above does give exact tightness on those two circles.

## Verification
Run `python3 CHECK.py` using the Python 3 standard library. It verifies, with integer arithmetic, that the monic Laguerre polynomial is orthogonal to the lower monomials for each \(1\le m\le12\), and checks its exact positive squared norm. It also verifies all four Gaussian moment identities for the explicit \(m=2\) nodes and algebraic quadrature weights in \(\mathbb Q(\sqrt2)\), using rational arithmetic. The executed checker reported `RADIAL_GAUSS_CHECKS_PASS 106`. These finite checks are supplementary only: the all-\(m\) proof uses exact moment identities, a positive Hankel matrix, and the classical Hermite–Lindemann theorem, none of which is certified by finite enumeration.

## Relationship to prior work
Bownik and Yu [1] prove nearly tight uniformly discrete frames from continuous tight frames, including Gabor systems. Their theorem concerns near-tight infinite-dimensional discretization; it does not impose exact tightness or a finite radial-shell count. Gröchenig and Ortega-Cerdà [2] study Marcinkiewicz–Zygmund sampling for Fock polynomials, without the present uniform-external-weight radial obstruction in the compared material. The published radial-complexity theorem [3] establishes an order-\(\sqrt n\) necessary and sufficient number of radii for *uniformly conditioned, positively weighted* Fock sampling; it neither forces exact tightness nor compares equal and variable external weights at the Gaussian-quadrature threshold. The one-circle optimum [4] rules out a single tight circle for \(n\ge2\), but has no all-odd-degree \(m\)-circle equal-weight claim. The degree-two positive cubature [5] uses nonuniform sample weights, while the two-circle conditioning theorem [6] gives an asymptotic instability rate for fixed equally populated circles rather than an exact all-angular obstruction.

Gaussian quadrature and the Laguerre root/weight identities [7] are classical, as is the transcendence result [8]. These ingredients are *not* claimed to be new. The claim here is their particular consequence for unweighted Gaussian-coherent frame exactness at the natural minimal radial count. An equivalent reformulation might exist in older equal-coefficient Gaussian cubature or coherent-state moment literature; scholarly priority is not independently established.

## Limitations
The obstruction concerns **equal external weights applied to full-Fock Gaussian-compensated observations** and odd-degree truncations \(n\ge3\). If weights may vary by sample, exactly \(m\) radii suffice. For equal weights the theorem proves only that at least \(m+1\) radii are necessary; it does **not** establish achievability with \(m+1\) radii, the minimal number of individual sample locations, any quantitative near-tight frame gap, or results for even-degree truncations. The proof does not depend on angular geometry, but it does depend on exact tightness, strictly positive common weight, finitely many samples, and the Gaussian factorial moment sequence. No independent mathematical audit has been performed.

## References
[1] M. Bownik and P.-T. Yu, *Uniform discretization of continuous frames*, arXiv:2603.10423v1, publicly posted 2026-03-11, https://arxiv.org/html/2603.10423v1.

[2] K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz–Zygmund inequalities for polynomials in Fock space*, arXiv:2109.11825, https://arxiv.org/abs/2109.11825.

[3] *Optimal-order radial complexity for positive sampling of Gaussian Fock polynomials*, mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-optimal-order-radial-complexity-for-positive-sampling-of-gaussia--23fa3fb029d8.

[4] *Sharp circle-only coherent-frame conditioning and angular-design rigidity*, mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-circle-only-coherent-frame-conditioning-and-angular-design--f8620afd3717.

[5] *Four nodes are necessary and sufficient for exact tight sampling of quadratic Fock polynomials*, mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-four-nodes-are-necessary-and-sufficient-for-exact-tight-sampling--df9aaaf372ae.

[6] *Sharp exponential stability barrier for two circular Fock sampling orbits*, mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-exponential-stability-barrier-for-two-circular-fock-sampli--41ad9e016c9b.

[7] E. W. Weisstein, *Laguerre-Gauss Quadrature*, MathWorld, https://mathworld.wolfram.com/Laguerre-GaussQuadrature.html.

[8] M. Waldschmidt, *Introduction to Diophantine Methods: Irrationality and Transcendence*, Theorem 2.1 (Hermite–Lindemann), https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/IntroductionDiophantineMethods.pdf.
