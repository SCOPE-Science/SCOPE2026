# Sharp exterior zero barrier and radial escape for generalized-Hartogs vertex kernels

## Finding
For every real \(1<\gamma<2\), put
\[
\delta=1-\gamma^{-1},\qquad N=\lceil\delta^{-1}\rceil-1\ge2,\qquad \alpha=\delta^{-1}-N\in(0,1].
\]
The vertex-limit polynomial of the Bergman kernel of the generalized Hartogs triangle is
\[
P_\delta(v)=\sum_{j=1}^N j(1-j\delta)v^{j-1}=\delta Q_{N,\alpha}(v),\qquad
Q_{N,\alpha}(v)=\sum_{j=1}^N j(N+\alpha-j)v^{j-1}.
\]
**Theorem (sharp exterior barrier).** For every integer \(N\ge2\), the following hold.

1. If \(0<\alpha<1\), **every one of the \(N-1\) complex zeros of \(Q_{N,\alpha}\), counted with multiplicity, satisfies \(|v|>1\)**. This includes all nonreal and all potentially multiple zeros. If \(\alpha=1\), all \(N-1\) roots are simple and lie exactly on \(|v|=1\). Thus the unit radius is the sharp common lower bound, and equality occurs precisely at the parameter endpoint.
2. Write the distinct roots at \(\alpha=1\) as \(\zeta_j=e^{i\theta_j}\), \(0<\theta_j<2\pi\). Each has an analytic continuation \(v_j(\varepsilon)\) for sufficiently small nonnegative \(\varepsilon\), with \(Q_{N,1-\varepsilon}(v_j(\varepsilon))=0\), and the exact first-order escape law
\[
|v_j(\varepsilon)|=1+\frac{1-\cos\theta_j}{N+2}\,\varepsilon+O_N(\varepsilon^2).
\]
Every radial coefficient is strictly positive.
3. For every fixed \(\gamma\) for which \(0<\alpha<1\), there exists \(t_\gamma>0\) such that the Bergman kernel satisfies
\[
K_\gamma(tv,t)\ne0\qquad(0<t<t_\gamma,\quad |v|\le1),
\]
where \(K_\gamma(s,t)\) denotes the kernel in product variables \(s=z_1\overline{w_1}\), \(t=z_2\overline{w_2}\). Thus sufficiently near the singular vertex, the classical diagonal-scale core \(|s|\le|t|\) is zero-free on positive-\(t\) sections, even though those sections have the \(N-1\) nearby zeros established in the cited source, located strictly outside that core.

The third assertion does **not** extend to the closed unit disk at \(\alpha=1\) by this argument; the limiting polynomial then has boundary roots.

## Assumptions and scope
The domain is \(H_\gamma=\{(z_1,z_2)\in\mathbb C^2: |z_1|^\gamma<|z_2|<1\}\) with ordinary Lebesgue-volume Bergman kernel. The notation \(K_\gamma(s,t)\) is the holomorphic kernel expressed in the coordinate products of two points; every \((s,t)\) with \(0<|t|<1\) and \(|s|<|t|^{1/\gamma}\) is realizable. Assertions 1 and 2 concern the polynomial for all \(N\ge2\) and \(0<\alpha\le1\), independently of rationality of \(\gamma\). The limit in assertion 3 is along real positive \(t\downarrow0\), with \(\gamma\) fixed. The parameter \(\alpha=1\) corresponds to the discrete exponents \(\gamma=(N+1)/N\). No theorem on all kernel zeros across the unrestricted admissible section is asserted.

## Proof
**1. Reciprocal boundary polynomials.** For every integer \(m\ge1\) define
\[
C_m(z)=\sum_{j=1}^m j(m+1-j)z^{j-1}.
\]
Set \(C_1=1\). Elementary coefficient comparison gives the exact interpolation
\[
Q_{N,\alpha}=\alpha C_N+(1-\alpha)C_{N-1}.
\]
Two further polynomial identities, valid for every \(N\ge2\), follow by differentiating the sums or checking their coefficients:
\[
(N-1)C_N=z(z-1)C_{N-1}'+(N+2z)C_{N-1}, \tag{1}
\]
\[
(N+2)C_{N-1}=(1-z)C_N'+(N-1)C_N. \tag{2}
\]
For reference, the explicit geometric-series identity
\[
(1-z)^3 C_m(z)=m-(m+2)z+(m+2)z^{m+1}-mz^{m+2} \tag{3}
\]
also verifies these polynomial relations, including at \(z=1\) by continuity.

**2. Simple roots on the circle.** Let \(U_m\) be the Chebyshev polynomial of the second kind, normalized by \(U_m(\cos u)=\sin((m+1)u)/\sin u\). A direct trigonometric expansion of the preceding finite sum yields
\[
C_m(e^{i\theta})=\tfrac12 e^{i(m-1)\theta/2}
U_m'(\cos(\theta/2)),\qquad 0\le\theta\le2\pi. \tag{4}
\]
The polynomial \(U_m\) has the \(m\) simple real zeros \(\cos(k\pi/(m+1))\), \(k=1,\ldots,m\). By Rolle's theorem \(U_m'\), of degree \(m-1\), has exactly \(m-1\) distinct zeros in \((-1,1)\). Formula (4) therefore places all \(m-1\) roots of \(C_m\) simply on \(|z|=1\), none at \(z=1\). Moreover \(C_N\) and \(C_{N-1}\) have no common root: any common root \(\zeta\) would satisfy \(\zeta\ne0,1\), and (1) would force \(C'_{N-1}(\zeta)=0\), contradicting simplicity. For \(N=2\) this also follows from \(C_1=1\).

**3. No crossing of the unit circle.** Suppose \(0<\alpha<1\) and \(Q_{N,\alpha}(e^{i\theta})=0\). For \(\theta=0\) the polynomial is strictly positive. Otherwise \(0<\theta<2\pi\). Divide the interpolation in step 1, evaluated through (4), by \(e^{i(N-2)\theta/2}\). Its second summand is real; the imaginary part is
\[
\frac\alpha2\sin(\theta/2)U_N'(\cos(\theta/2))=0.
\]
Since \(\sin(\theta/2)>0\), we obtain \(C_N(e^{i\theta})=0\), hence also \(C_{N-1}(e^{i\theta})=0\), contradicting step 2. Thus no root of \(Q_{N,\alpha}\) lies on the unit circle for any interior parameter.

**4. Initial outward motion and global exclusion.** For \(N\ge3\), at \(\alpha=0\) the \(N-2\) finite zeros of \(C_{N-1}\) are simple and unimodular. Let \(z(\alpha)\) be the locally analytic root through one such zero \(\zeta\). The implicit-function theorem and (1) imply
\[
\frac{z'(0)}{\zeta}=-\frac{C_N(\zeta)}{\zeta C'_{N-1}(\zeta)}
=\frac{1-\zeta}{N-1},
\qquad
\left.\frac d{d\alpha}\log|z(\alpha)|\right|_{0}
=\frac{1-\operatorname{Re}\zeta}{N-1}>0. \tag{5}
\]
The remaining root tends to infinity as \(\alpha\downarrow0\): the leading coefficient of \(Q_{N,\alpha}\) is \(N\alpha\), while its next coefficient tends to the nonzero leading coefficient of \(C_{N-1}\). Thus all roots lie outside the closed unit disk when \(\alpha>0\) is sufficiently small. Root-count continuity and the no-crossing result of step 3 keep all \(N-1\) roots outside throughout \(0<\alpha<1\), even at possible collisions. For \(N=2\), the polynomial is \((1+\alpha)+2\alpha z\), whose sole root \(-(1+\alpha)/(2\alpha)\) has modulus strictly greater than one for \(0<\alpha<1\). At \(\alpha=1\), step 2 gives exactly \(N-1\) simple unimodular roots, establishing assertion 1.

**5. Sharp endpoint escape velocity.** Write \(\varepsilon=1-\alpha\) and fix a simple zero \(\zeta=e^{i\theta}\) of \(C_N\). By implicit differentiation of \(C_N+\varepsilon(C_{N-1}-C_N)\), followed by (2),
\[
\frac{z'(0)}{\zeta}=-\frac{C_{N-1}(\zeta)}{\zeta C_N'(\zeta)}
=\frac{1-\zeta^{-1}}{N+2}.
\]
Taking real parts gives \(\left.\frac{d}{d\varepsilon}\log |z(\varepsilon)|\right|_{\varepsilon=0}=(1-\cos\theta)/(N+2)\). Analyticity of each simple-root branch yields the stated expansion with \(O_N(\varepsilon^2)\), and its coefficient is positive because \(\zeta\ne1\). This proves assertion 2.

**6. Bergman-kernel consequence.** Fu's Lemma 2.3 establishes that for each fixed \(1<\gamma<2\) the normalized vertex section
\[
F_t(v)=\pi^2t(1-t)^2K_\gamma(tv,t)
\]
converges uniformly on every fixed compact \(v\)-disk to \(P_\delta(v)\) as real \(t\downarrow0\). For \(0<\alpha<1\), assertion 1 and compactness give \(m_\gamma:=\min_{|v|\le1}|P_\delta(v)|>0\). Choose \(t_\gamma>0\) so the uniform difference is below \(m_\gamma/2\) on \(|v|\le1\). Since \(t<t^{1/\gamma}\) for \(0<t<1\), the corresponding product variables are admissible. Therefore \(K_\gamma(tv,t)\ne0\) throughout that closed disk. The cited paper's Theorem 1.1 establishes nearby zeros, and their limiting positions are outside \(|v|=1\) by assertion 1; choosing their localization disks sufficiently small gives the stated separation. This proves assertion 3.

## Verification
Run `python CHECK.py` using the Python 3 standard library. The checker independently expands identities (1)–(3) with exact integer coefficients for every \(2\le N\le50\), verifies Chebyshev roots and the velocity algebra for small dimensions, compares all 112 numerically computed roots of selected interior-parameter polynomials with the strict exterior inequality, and verifies the endpoint radial velocities numerically on 36 roots. Its recorded run passed 196 exact identities, 91 Chebyshev-root/ratio comparisons, 112 exterior-root checks, and 36 velocity comparisons. The proof's global quantifiers rest on the analytic identities and no-crossing argument, not finite numerical testing.

## Relationship to prior work
Fu's 2026 full manuscript [1] constructs the precise polynomial \(P_\delta\), proves compact-uniform convergence of normalized Bergman sections, classifies possible multiple polynomial zeros, establishes zeros near the vertex, and describes angular concentration. Those theorems are credited as necessary background; the new statements here concern **all complex roots being strictly outside the unit disk**, the endpoint radial velocity of every root, and the consequent zero-free inner core. A published complete real-root classification [2] deals with negative real roots only, so its conclusions do not bound the nonreal roots' moduli. Edholm–Mathew [3] and Deng–Fu [4] study the distinct palindromic polynomial of the oblique rational restriction \(s=t\), with zeros inside rather than outside a disk; their zero counts do not imply the present rescaled vertex exclusion. Fell [5] treats convex combinations of monic equal-degree polynomials, with different hypotheses and root-locus conclusions; its theorem does not directly cover the consecutive-degree pair here. The standard Chebyshev zero theorem itself is classical and is not claimed as new. Unlocated stronger polynomial-stability literature remains a possible priority risk.

## Limitations
The zero-free kernel section is established only for fixed non-endpoint exponents and sufficiently small positive product parameter \(t\); it is not a uniform bound in \(\gamma\), not a statement on all complex \(t\), and not a classification of all zeros in the full admissible section. At \(\alpha=1\) the polynomial has roots on the boundary, so the argument does not decide whether the finite-\(t\) kernel has zeros in \(|v|\le1\). Interior polynomial roots may collide off the unit disk; no assertion of simplicity for every \(0<\alpha<1\) is made. The radial expansion fixes \(N\) and does not give a uniform error as \(N\to\infty\). An older unlocated polynomial-stability theorem could potentially imply the same root barrier.

## References
1. Q. Fu, *Bergman Kernel Zeros on Generalized Hartogs Triangles*, arXiv:2611.15406v1, first public 2026-11-11, https://arxiv.org/abs/2611.15406 (especially Lemma 2.3, Lemma 3.1 and Theorems 1.1 and 1.5).
2. *Parity-controlled real zeros of generalized Hartogs vertex polynomials* (2026), public research report, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-parity-controlled-real-zeros-of-generalized-hartogs-vertex-polyn--46a4566901e8 (full result compared).
3. L. D. Edholm and V. T. Mathew, *Arithmetic properties and zeros of the Bergman kernel on a class of quotient domains*, arXiv:2505.20489, first public 2025-05-26; *Mathematische Zeitschrift* 313 (2026), https://arxiv.org/abs/2505.20489 .
4. G. Deng and Q. Fu, *Bergman Kernel Zeros on Rational Hartogs Triangles*, arXiv:2611.07480v1, first public 2026-11-05, https://arxiv.org/abs/2611.07480 .
5. H. J. Fell, *On the zeros of convex combinations of polynomials*, *Pacific J. Math.* 89 (1980), 43–50, https://msp.org/pjm/1980/89-1/pjm-v89-n1-p05-s.pdf .
