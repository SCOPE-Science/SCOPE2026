# Marked ADE intersections of the gluing curve on the \(Z_{15}\) Kunev K3 tail

## Finding
Let \(Y\) be the general weighted K3 tail of type \(Z_{15}\) constructed in Lee--Scattone--Schaffler [1], in the weighted projective space \(\mathbb P(1,2,4,4,3)\) with coordinates \([\tau:\alpha:\beta:u:v]\). The natural gluing curve \(T\) is the reduced curve cut out by \(\tau=0\). Its marked ADE incidence is complete: exactly two singularities of type \(A_3\) and two of type \(A_1\), all four on \(T\). On the minimal resolution \(\pi:\widehat Y\to Y\), the strict transform \(\widehat T\) meets transversely one *end* component in each of the two \(A_3\) chains and the unique exceptional curve above each \(A_1\) point; no other exceptional intersections occur. In particular \(\widehat T^2=-2\), with local Weil-divisor intersection corrections \(3/4,3/4,1/2,1/2\). This is a marked incidence statement, rather than a claim that the unmarked basket is unknown.

## Assumptions and scope
Work over \(\mathbb C\). Consider the special weighted complete-intersection form of [1, §4.5]:
\[
Y=\{u^2=F_8(\tau,\alpha,\beta),\quad v^2=G_6(\tau,\alpha,\beta)\}\subset \mathbb P(1,2,4,4,3),
\]
with weighted degrees \(8\) and \(6\). The branch restrictions at \(\tau=0\) have the precise forms
\[
F_8(0,\alpha,\beta)=\beta(a\alpha^2+b\beta),\qquad G_6(0,\alpha,\beta)=\alpha(c\alpha^2+d\beta).
\]
Assume \(a,b,c,d\) are nonzero and \(ad-bc\ne0\); also take the remaining coefficients in a nonempty Zariski-open subset for which the complete intersection is quasismooth away from ambient cyclic-quotient strata. These assumptions are satisfied by the generic \(Z_{15}\) branch data in [1]. The reduced gluing curve \(T=Y\cap\{\tau=0\}\) has normalization \(\mathbb P^1\) by [1, §4.5]. We consider the canonical weighted-model gluing divisor, not arbitrary alternate models or all special boundary parameters.

## Proof
**1. All possible quotient points are on the gluing curve.** On \(\tau\ne0\) the ambient weighted space is smooth. The two branch linear systems there are base-point-free (the monomials \(\tau^8\), \(\tau^6\) are present), and Bertini/transversality, with \(\partial(u^2-F_8)/\partial u=2u\) and \(\partial(v^2-G_6)/\partial v=2v\), proves smoothness for general coefficients. On \(\tau=0\), a point with nontrivial ambient stabilizer and lying on both equations must have \(v=0\): since \(\operatorname{gcd}(3,2)=\operatorname{gcd}(3,4)=1\), a point with \(v\ne0\) and at least one even-weight coordinate nonzero has trivial stabilizer. The case all \(\alpha,\beta,u\) vanish is excluded by the equations. The equations at \(v=\tau=0\) require
\[
\alpha(c\alpha^2+d\beta)=0,\qquad u^2=\beta(a\alpha^2+b\beta).
\]
If \(\alpha=0\), then \(\beta\ne0\) and \(u/\beta=\pm\sqrt b\), giving two distinct points \(P_+,P_-\). If \(\alpha\ne0\), then \(\beta=-(c/d)\alpha^2\), so
\[
(u/\alpha^2)^2=-\frac{c(ad-bc)}{d^2}\ne0,
\]
giving two more distinct points \(Q_+,Q_-\). No other solutions exist. The two branch restrictions \(F_8=0\) and \(G_6=0\) have no common zero on \(\mathbb P(2,4)\), by \(abcd(ad-bc)\ne0\); thus there are no additional nonquotient singularities on \(\tau=0\), as the two equations are transversal in smooth uniformizing charts. More explicitly, if \(u,v\ne0\), the two covering derivatives are independent; if one vanishes, its branch equation has a nonvanishing derivative by the displayed factorizations. Quasismoothness away from \(\tau=0\) follows as above.

**2. Analytic types.** At either \(P_\pm\) use the chart \(\beta\ne0\), with residual \(\mu_4\) acting with weights \((1,2,0,0,3)\) on \((\tau,\alpha,\beta,u,v)\). The derivative of \(u^2-F_8\) in \(u\) is nonzero because \(u\ne0\), while the derivative of \(v^2-G_6\) in \(\alpha\) is \(-d\beta\ne0\). Eliminate \(u,\alpha\) analytically. Local uniformizing coordinates are \((\tau,v)\) with \(\mu_4\)-weights \((1,3)\), giving \(\frac14(1,3)=A_3\). At \(Q_\pm\), use \(\alpha\ne0\), with residual \(\mu_2\) and nonzero derivatives in \(u\) and \(\beta\); local coordinates \((\tau,v)\) both have odd weight, giving \(\frac12(1,1)=A_1\).

**3. Marked strict-transform intersections.** In each uniformizing chart the gluing curve is precisely the image of the axis \(\tau=0\) in \(\mathbb A^2_{\tau,v}/\mu_r(1,r-1)\), with \(r=4\) or \(2\). The minimal toric resolution of \(A_{r-1}\) has an exceptional chain of \(r-1\) rational \((-2)\)-curves. The torus-invariant boundary axis meets exactly one endpoint transversely and no other exceptional component. Since the axis is smooth after strict transformation, this gives the stated complete marked incidence. Away from these points \(T\) is smooth (or, equivalently, [1] proves its normalization is \(\mathbb P^1\)); hence \(\widehat T\) is a smooth rational curve. Adjunction on the minimal smooth K3 resolution gives \(\widehat T^2=-2\).

**4. Intersection-theoretic consistency.** Let \(H=\mathcal O_Y(1)\) as a rational Weil class. The standard weighted complete-intersection degree calculation gives
\[
H^2=\frac{6\cdot8}{1\cdot2\cdot4\cdot4\cdot3}=\frac12.
\]
The divisor \(T\) represents \(H\). For an \(A_n\) chain, an invariant axis meeting an endpoint has local correction \((C_{A_n}^{-1})_{11}=n/(n+1)\) to the square of the strict transform, where \(C_{A_n}\) is the positive Cartan matrix. The four contributions are therefore \(3/4,3/4,1/2,1/2\), and their sum is \(5/2\). Consequently \(T^2=\widehat T^2+5/2=-2+5/2=1/2\), agreeing independently with the weighted intersection number. The gluing marking is thus compatible with both the local resolution and global polarization.

## Verification
The accompanying `check_z15.py` checks exact symbolic branch intersections on representative general coefficients \((a,b,c,d)=(1,1,1,2)\), nonvanishing local partial derivatives, inverse-Cartan endpoint corrections for \(A_1,A_3\), and weighted intersection arithmetic. Run `python check_z15.py` with Python 3 and SymPy. The general assertion follows from the explicit factorization, quotient charts and open Bertini conditions, not from the finite specialization alone.

## Relationship to prior work
[1, Theorem 1.1 and §§4.5, 7] supplies the special \(Z_{15}\) weighted equations, the boundary gluing construction and the rationality of its preimage curve. [1, Table 4 and Theorem 7.2] identifies the tail as Iano-Fletcher codimension-two K3 family #19; the unmarked weighted singularity basket belongs to classical weighted-K3 classification [2]. The present statement adds the incidence of the *canonically marked gluing curve* with every ADE point, the exact endpoint attachment in the minimal resolution, and the local-to-global fractional intersection balance. Those marked facts are not claimed to follow from mere labels of singularity types, nor to classify every possible boundary specialization. Related KSBA boundary methods appear in [3] for a different class of surfaces.

## Limitations
The result applies to general special \(Z_{15}\) tail equations with nonzero generic parameters; collision walls or nonquasismooth specializations may have different baskets and attachment configurations. It does not determine the full Picard lattice or monodromy of the boundary family, nor establish historical publication priority beyond the checked literature. Independent validation has not been performed.

## References
[1] Y. Lee, E. Scattone, L. Schaffler, *K3 tails in the KSBA moduli of Kunev surfaces*, arXiv:2611.17149v1, publicly posted 12 November 2026, https://arxiv.org/html/2611.17149v1.

[2] A. R. Iano-Fletcher, *Working with weighted complete intersections*, in *Explicit Birational Geometry of 3-folds* (2000), Table 2, family #19. The family identification is cited in [1].

[3] P. Gallardo, G. Pearlstein, L. Schaffler, Z. Zhang, *Unimodal singularities and boundary divisors in the KSBA moduli of a class of Horikawa surfaces*, Math. Nachr. 297 (2024), 595–628.
