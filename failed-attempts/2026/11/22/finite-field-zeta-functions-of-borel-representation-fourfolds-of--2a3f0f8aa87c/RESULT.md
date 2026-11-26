# Finite-field zeta functions of Borel representation fourfolds of parafree groups

## Finding
For an integer \(m\ge2\), put \(n=2m+1\) and let \(G_m=\langle x,y,z\mid x^2y^3=z^n\rangle\). Let \(B\subset\mathrm{SL}_2\) be the upper-triangular Borel group. For every prime power \(q\) with characteristic \(p\nmid6n\), write \(X_m=\operatorname{Hom}(G_m,B)\) over \(\mathbb F_q\). At every extension degree \(r\ge1\), set \(Q=q^r\). Then
\[
\#X_m(\mathbb F_Q)=Q^2(Q-1)^2+Q^2(Q-1)e_{m,q}(r),
\]
with
\[
e_{m,q}(r)=\begin{cases}
8(\gcd(n,Q-1)-1),&Q\equiv1\pmod{12},\\
0,&Q\not\equiv1\pmod{12}.
\end{cases}
\]
The correction comes from a finite étale zero-dimensional coefficient-base scheme \(E_{m,q}\) of geometric length \(16m\). The entire zeta function is
\[
Z(X_m,T)=\frac{(1-q^3T)^2}{(1-q^2T)(1-q^4T)}\,\frac{Z(E_{m,q},q^3T)}{Z(E_{m,q},q^2T)}.
\]
These formulas are exact for all permitted \(q,m,r\).

## Assumptions and scope
All varieties are over \(\mathbb F_q\), with \(\operatorname{char}\mathbb F_q=p\nmid 6(2m+1)\), and the representation scheme is reduced. Matrices in \(B\) are \(M(\lambda,a)=\left(\begin{smallmatrix}\lambda&a\\0&\lambda^{-1}\end{smallmatrix}\right)\) with \(\lambda\ne0\). Define the Laurent polynomials
\[\sigma_j(t)=\sum_{i=0}^{j-1}t^{j-1-2i}.\]
The diagonal torus is \(T_m=\{(\lambda,\mu,\nu)\in\mathbb G_m^3:\lambda^2\mu^3=\nu^n\}\). Let \(E_{m,q}\subset T_m\) be cut out by \(\sigma_2(\lambda)=\sigma_3(\mu)=\sigma_n(\nu)=0\). No assertion is made in characteristics dividing \(6n\), where separability and the singular-fiber structure may change. The result is about *unquotiented* representation varieties, not their character varieties modulo conjugation.

## Proof
**1. Presentation and split torus.** Direct matrix multiplication gives \(M(t,a)^j=M(t^j,\sigma_j(t)a)\). Thus \(X_m\subset T_m\times\mathbb A^3\) has the linear-in-fiber equation
\[\mu^{-3}\sigma_2(\lambda)a+\lambda^2\sigma_3(\mu)b-\sigma_n(\nu)c=0.\]
The map \((s,\nu)\mapsto(s^3\nu^{-n},s^{-2}\nu^n,\nu)\) and inverse \((\lambda,\mu,\nu)\mapsto(\lambda\mu,\nu)\) give \(T_m\cong\mathbb G_m^2\) over every ground field.

**2. Fibers and the point-count identity.** Outside \(E_{m,q}\), at least one coefficient of the displayed linear form is nonzero, so every geometric fiber is \(\mathbb A^2\). Over \(E_{m,q}\), all coefficients vanish, so the fiber is \(\mathbb A^3\). This holds equally for rational fibers over any finite extension, hence
\[\#X_m(\mathbb F_Q)=Q^2((Q-1)^2-\#E_{m,q}(\mathbb F_Q))+Q^3\#E_{m,q}(\mathbb F_Q).\]
It remains to compute the finite étale scheme's rational point counts.

**3. Root-of-unity arithmetic.** Since \(p\nmid6n\), the identity \(\sigma_j(t)=t^{1-j}(t^{2j}-1)/(t^2-1)\) away from \(t=\pm1\), together with \(\sigma_j(\pm1)\ne0\), shows that all roots of \(\sigma_2,\sigma_3,\sigma_n\) are simple. In particular, \(E_{m,q}\) is finite étale (its defining coefficient equations have independent local differentials at every common zero).

The equation \(\sigma_2(\lambda)=0\) has two solutions exactly when \(4\mid Q-1\). The equation \(\sigma_3(\mu)=0\) has four solutions exactly when \(3\mid Q-1\). For odd \(Q\), these conditions hold simultaneously exactly when \(Q\equiv1\pmod{12}\). For each allowed \(\mu\), \(\mu^3\in\{1,-1\}\), while \(\lambda^2=-1\). Hence the torus relation becomes \(\nu^n\in\{1,-1\}\). Because \(n\) is odd, \(\nu=1\) or \(\nu=-1\), respectively, is one solution, and the total number of solutions is \(d=\gcd(n,Q-1)\), by the cyclic structure of \(\mathbb F_Q^\times\). Exactly one must be discarded because it is a forbidden root of \(\sigma_n\). Therefore each of the eight \((\lambda,\mu)\) pairs yields precisely \(d-1\) allowable \(\nu\). This proves the formula for \(e_{m,q}(r)\). Over an algebraic closure it gives \(8(n-1)=16m\) geometric points.

**4. Zeta factorization.** For any finite-type scheme \(Y/\mathbb F_q\), use \(Z(Y,T)=\exp(\sum_{r\ge1}\#Y(\mathbb F_{q^r})T^r/r)\). Substituting the point counts into this defining identity, then collecting terms \(q^{4r}-2q^{3r}+q^{2r}\) and \((q^{3r}-q^{2r})e_{m,q}(r)\), proves the displayed rational zeta identity. Since \(E_{m,q}\) is finite étale, its zeta function is an ordinary finite product of cyclotomic-type factors and the point-count formula specifies all of them.

For an explicit finite product, let \(M=\operatorname{lcm}(12,2n)\), let \(L\) be the multiplicative order of \(q\) modulo \(M\), and for \(d\mid L\) put \(c_d=d^{-1}\sum_{j\mid d}\mu(d/j)e_{m,q}(j)\), where \(\mu\) is the integer Möbius function. Then \(c_d\) is the number of degree-\(d\) closed points of \(E_{m,q}\) and
\[Z(E_{m,q},T)=\prod_{d\mid L}(1-T^d)^{-c_d}.\]
This is finite because all geometric roots lie in the group of \(M\)-th roots of unity.

## Verification
The companion program `verify_counts.py` enumerates the root triples in prime fields, comparing exact counts of \(E_{m,q}\) with the proposed gcd formula, and checks the induced point-count and split-zeta identities in example cases. The tested inputs are \((m,q)=(2,13),(2,61),(4,73),(3,37),(4,109)\), all in good characteristic. The symbolic proof above establishes the universal claim; finite examples are only cross-checks.

## Relationship to prior work
S. Liriano, *Exploring the Regular and Singular Loci of Group Representation Varieties* (arXiv:2611.09774v1, first submitted 6 November 2026), supplies the characteristic-zero coefficient presentation, the split torus and the geometric count of \(16m\) exceptional base points, together with the topology of the singular and regular loci. The new point-count formula is genuinely arithmetic: it determines the Frobenius splitting of these exceptional points and the complete zeta of the unquotiented variety in every good finite characteristic, not just the geometric number of points. Standard literature on arithmetic representation counting provides context but does not supply this specific family-wide gcd formula in the sources inspected.

## Limitations
The finite-characteristic results require \(p\nmid6n\); bad reduction is not analyzed. The point counts concern the reduced affine representation variety, not any GIT quotient. Geometric normality or singularity behavior over arbitrary characteristic is not independently asserted beyond the finite étale coefficient-base calculation and the fiber description. Mathematical priority against uncatalogued or unindexed work remains open; there is no independent validation.

## References
- S. Liriano, *Exploring the Regular and Singular Loci of Group Representation Varieties*, arXiv:2611.09774v1 (2026), https://arxiv.org/abs/2611.09774 . Sections 3, 4, 5, 6.
- F. Korthauer, *Arithmetic representation growth of virtually free groups* (2025), https://link.springer.com/article/10.1007/s00209-025-03690-1 . General contextual comparison, for different group families.
- Standard elementary results: cyclicity of finite-field multiplicative groups and Möbius inversion for closed-point degree counts.
