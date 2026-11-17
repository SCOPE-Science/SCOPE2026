# Grassmann distance degree equals Euclidean distance degree for every rational-normal-scroll ruling curve

## Finding
Let \(d\ge 2\) and let \(n_1,\ldots,n_d\ge2\) be arbitrary integers. Let \(\mathcal R_{\mathbf n}\subset\operatorname{Gr}(d,\sum_i(n_i+1))\) be the smooth rational curve of the ruling \((d-1)\)-planes of the rational normal scroll \(S(n_1,\ldots,n_d)\), with the standard block-monomial embedding and standard nondegenerate symmetric bilinear form. Define
\[
 s_i(t)=\sum_{j=0}^{n_i}t^{2j},\quad L(t)=\operatorname{lcm}_{1\le i\le d}s_i(t),\quad \delta=\deg L.
\]
For generic rank-\(d\) symmetric orthogonal-projector data, count stationary points of the squared Frobenius/chordal-distance objective on the smooth model away from its algebraic cut locus. Then
\[
\boxed{\operatorname{GDdeg}(\mathcal R_{\mathbf n})=2\delta-2=\operatorname{EDdeg}(\mathcal R_{\mathbf n}).}
\]
Equivalently, with \(\varphi\) Euler's totient function,
\[
\delta=\sum_{\substack{e>2\\\exists i:\ e\mid 2(n_i+1)}}\varphi(e).
\]
This includes arbitrary unequal block degrees, including shared cyclotomic factors. For instance, the unbalanced scroll \(S(2,3)\) has \(\delta=10\) and Grassmann distance degree \(18\).

## Assumptions and scope
Everything is over \(\mathbb C\) in characteristic zero. Put \(M=\sum_i(n_i+1)\). In a coordinate block of length \(n_i+1\), set \(v_i(t)=(1,t,\ldots,t^{n_i})\); the \(d\times M\) matrix \(A(t)\) has row \(i\) equal to \(v_i(t)\) in its own block and zeros elsewhere. Its row span parametrizes \(\mathcal R_{\mathbf n}\). The map extends to an embedding of \(\mathbb P^1\) in the Grassmannian and is real-Zariski dense. Away from zeros of \(\prod_i s_i\), the symmetric projector onto its row span is
\[
 P(t)=\operatorname{diag}_i\frac{v_i(t)^{\mathsf T}v_i(t)}{s_i(t)}.
\]
An admissible data matrix \(Q\) satisfies \(Q^{\mathsf T}=Q\), \(Q^2=Q\), \(\operatorname{rank}Q=d\). The algebraic cut locus is \(\{t:\operatorname{rank}(QP(t))<d\}\). The optimization critical equation is \(\frac{d}{dt}\operatorname{tr}(P(t)Q)=0\) outside poles and this cut locus. The count is for generic \(Q\) in the irreducible projector Grassmannian, without multiplicities.

## Proof
**1. A genuine family of projector data.** Choose independent block vectors \(u_i\in\mathbb C^{n_i+1}\) with \(\kappa_i=u_i^{\mathsf T}u_i\ne0\). Set \(Q_{\mathbf u}=\operatorname{diag}_i(u_i u_i^{\mathsf T}/\kappa_i)\). This is an actual symmetric idempotent projector of rank \(d\), not an arbitrary symmetric data matrix. Let \(f_i(t)=\sum_{j=0}^{n_i}u_{i,j}t^j\). The objective is
\[
 F_{\mathbf u}(t)=\operatorname{tr}(P(t)Q_{\mathbf u})=\sum_i\frac{f_i(t)^2}{\kappa_i s_i(t)}=\frac{G_{\mathbf u}(t)}{L(t)},\quad
 G_{\mathbf u}=\sum_i\frac{f_i^2}{\kappa_i}\frac{L}{s_i}.
\]
The factors \(s_i\) are squarefree, since \(s_i=(t^{2(n_i+1)}-1)/(t^2-1)\). So \(L\) is squarefree. At each root \(\alpha\) of \(L\), the residue of \(F_{\mathbf u}\) is a nonzero rational function of the free block vectors: varying an individual \(u_i\) for which \(s_i(\alpha)=0\) changes it. Consequently, on a nonempty Zariski open set of block choices, \(G_{\mathbf u}\) and \(L\) are coprime and \(F_{\mathbf u}:\mathbb P^1\to\mathbb P^1\) is a degree-\(\delta\) rational map, with \(\delta\) simple finite poles.

**2. No ramification at poles or infinity.** A simple pole has local mapping degree one. At infinity put \(z=1/t\). Its objective expansion is
\[
 F_{\mathbf u}(1/z)=\sum_i\frac{u_{i,n_i}^2}{\kappa_i}
 +2z\sum_i\frac{u_{i,n_i}u_{i,n_i-1}}{\kappa_i}+O(z^2).
\]
The coefficient of \(z\) is generically nonzero, so infinity is also unramified. Riemann–Hurwitz now gives total ramification weight \(2\delta-2\), all at finite nonpoles.

**3. All these points are simple, not merely counted with multiplicity.** Work in the smooth parameter space of the \(u_i\) with nonzero \(\kappa_i\), and remove poles in the \(t\)-line. Choose a nonempty open parameter set on which each \(f_i\) has only simple roots and, for every finite \(t\), the vectors \(u_1\) and \(u_2\) are not simultaneously in the respective two-dimensional spaces \(\operatorname{span}\{v_1(t),v_1'(t)\}\) and \(\operatorname{span}\{v_2(t),v_2'(t)\}\). The latter is possible: for a fixed \(t\), the two membership conditions have total codimension at least \((n_1-1)+(n_2-1)\ge2\); allowing the one-dimensional parameter \(t\) still leaves a proper incidence image.

Fix any parameter choice in that open set and any nonpole \(t\). For at least one \(i\in\{1,2\}\), the three coefficient vectors \(u_i,v_i(t),v_i'(t)\) are linearly independent. If \(f_i(t)\ne0\), vary \(u_i\) by \(\dot u_i\) with \(u_i\cdot\dot u_i=v_i(t)\cdot\dot u_i=0\) but \(v_i'(t)\cdot\dot u_i\ne0\). This leaves \(\kappa_i,f_i(t)\) unchanged to first order and changes \(F'_{\mathbf u}(t)\) by \(2f_i(t)(v_i'(t)\cdot\dot u_i)/(\kappa_i s_i(t))\ne0\). If \(f_i(t)=0\), then \(f_i'(t)\ne0\) by squarefreeness; varying \(u_i\) with \(u_i\cdot\dot u_i=0\) and \(v_i(t)\cdot\dot u_i\ne0\) changes \(F'_{\mathbf u}(t)\) by \(2f_i'(t)(v_i(t)\cdot\dot u_i)/(\kappa_i s_i(t))\ne0\). Thus the universal incidence equation \(F'_{\mathbf u}(t)=0\) is smooth and transverse in the parameter direction. Generic smoothness in characteristic zero gives a nonempty open of projector choices for which every finite nonpole critical root is simple.

**4. The critical points avoid the cut locus.** For the block projectors above, the algebraic cut equation is precisely \(\prod_i f_i(t)=0\), since the determinant of the pairing of the two rank-\(d\) row spaces is a nonzero factor times that product. Fix \(i\) and choose any \(j\ne i\). At a root of \(f_i\), the derivative \(F'_{\mathbf u}\) is not identically zero as a function of the independent vector \(u_j\): the nonconstant monomial map \(v_j(t)\) permits a variation with nonzero derivative at that fixed \(t\). Generically the two equations \(f_i(t)=0\) and \(F'_{\mathbf u}(t)=0\) are independent; their incidence over the one-dimensional \(t\)-line has a proper image in parameter space. Equivalently, the resultant of their cleared numerators is nonzero on a nonempty open. Intersecting these finitely many opens over \(i\), all critical points avoid the cut locus.

**5. Pass to generic Grassmann data.** For any symmetric \(Q\), the rational objective has denominator dividing \(L\) and its cleared derivative numerator has degree at most \(2\delta-2\). Thus no generic data can have more than that many finite isolated critical points away from poles and cut. Steps 1–4 give genuine projector data exhibiting exactly \(2\delta-2\) such distinct points. Coprimality with \(L\), squarefreeness of the critical numerator, nonzero leading coefficient, and nonvanishing of the cut-resultant are nonempty Zariski-open conditions on the irreducible rank-\(d\) projector variety. Therefore every generic projector has exactly this number of admissible critical points. The equality with the published ED degree is Theorem 2.2 of Friedman–Hoşten–Rosana. Cyclotomic factorization of \(s_i\) gives the totient expression.

## Verification
The accompanying `verify.py` performs exact symbolic arithmetic for genuine rank-two block projector data on several balanced and unbalanced scrolls, including an explicit \(S(2,3)\) witness. It checks denominator degree, critical-numerator degree, simple roots, nonpole roots and avoidance of all cut points by polynomial greatest-common-divisor tests. These finite examples are checks of the algebra; the unrestricted proof uses incidence transversality, generic smoothness and Riemann–Hurwitz.

## Relationship to prior work
Friedman, Hoşten and Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018 (first public version October 1, 2026), Example 2.1 and Theorem 2.2, already prove the entire **Euclidean-distance** formula for the rational-normal-scroll ruling curve using arbitrary symmetric data. Section 4 defines the Grassmann-distance count for projector data and removes the algebraic cut locus; it does not state the Grassmann-distance formula for arbitrary unbalanced scrolls. Friedman, Rosana and Sturmfels, *Distance Optimization in the Grassmannian of Lines*, arXiv:2601.22843 (January 30, 2026), introduced the GD invariant. The claim here is only the equality after restricting data to genuine rank-\(d\) projectors, including proof of simplicity and avoidance of cut points despite the restriction. For the balanced case, an earlier separate calculation established the equality; the present contribution treats every unequal block list, including cyclotomic overlaps, in one uniform theorem.

## Limitations
The theorem uses the standard block-monomial embedding, standard symmetric bilinear form and characteristic zero. It does not classify real local minima or claim that all complex critical points are real. It does not assert an equality for arbitrary Grassmannian models. It counts critical points off the algebraic cut locus and excludes the isotropic metric-indeterminacy boundary. Historical priority for all aliases of the scroll-ruling model remains a research risk.

## References
Friedman, Hannah; Hoşten, Serkan; Rosana, Andrea. *Euclidean Distance Optimization Within the Grassmannian*. arXiv:2610.02018v2, 2026, Sections 2 and 4. https://arxiv.org/html/2610.02018v2 .

Friedman, Hannah; Rosana, Andrea; Sturmfels, Bernd. *Distance Optimization in the Grassmannian of Lines*. arXiv:2601.22843v1, 2026. https://arxiv.org/abs/2601.22843 .
