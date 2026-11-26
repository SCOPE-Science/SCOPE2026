# The projective-symmetry wall and hidden stabilizers of characteristic-two cuspidal curves

## Finding

Let \(k\) be an algebraically closed field of characteristic \(2\). For each integer \(n\geq1\), put \(q=2^n\) and consider the irreducible projective plane curve
\[
C_q:\quad Z^2Y^q+X^{q+2}+XZ^{q+1}=0\quad\subset\mathbb P^2_k.
\]
Write \(G_q\) for its group of **projective** automorphisms, i.e. those induced by \(\mathrm{PGL}_3(k)\), not all automorphisms of its abstract normalization.

**Theorem.** The full geometric projective automorphism group has the following sharp dichotomy:
\[
G_q=\begin{cases}
\{[X:Y:Z]\mapsto[\alpha^2X+\beta^2Z:\alpha Y+(\beta^4+\beta)Z:Z]:\alpha^3=1,\ \beta\in k\}\cong\mathbb G_a(k)\rtimes\mu_3(k),&q=2,\\
\{[X:Y:Z]\mapsto[\alpha^qX:\alpha Y:Z]:\alpha^{q+1}=1\}\cong\mu_{q+1}(k),&q\geq4.
\end{cases}
\]
In particular, for \(q\geq4\) it is cyclic of order exactly \(q+1\), while the degree-four member has a one-dimensional reduced projective symmetry group.

For **every** \(q\geq2\), the projective stabilizer group scheme \(\mathscr G_q=\operatorname{Stab}_{\mathrm{PGL}_3}(C_q)\) has \(\dim_k\operatorname{Lie}(\mathscr G_q)=3\) and is **non-smooth**. More quantitatively, it contains a finite closed subgroup scheme of length \(q^3(q+1)\), represented by
\[
[X:Y:Z]\longmapsto[d^qX:cX+dY+eZ:Z],\qquad
d^{q(q+1)}=1,\quad c^q=e^q=0.
\]
The infinitesimal symmetries are therefore invisible in the geometric-point group, even when \(q\geq4\) and that group is finite of odd order.

## Assumptions and scope

All automorphisms and group schemes are over the algebraically closed field \(k\). The statement is about the projective stabilizer of the **specified plane embedding**. It is not a classification of abstract automorphisms of \(\mathbb P^1\) or of the affine line, and it does not identify the entire nonreduced stabilizer scheme beyond its Lie algebra and an explicit closed subgroup. The index \(n\) is an integer at least one, so \(q\) ranges over \(2,4,8,\ldots\).

The source construction supplies the normalization on the chart \(Z=1\):
\[
x=t^q,\qquad y=t^{q+2}+t.
\]
The parametrization extends to \(\mathbb P^1\) with the sole preimage of the unique point at infinity at \(t=\infty\). The unique singular point is \(P=[0:1:0]\), and in the chart \(Y=1\) its tangent cone is \(Z^2\), so \(Z=0\) is its unique tangent line. Alternatively, these assertions follow directly from the equation and the displayed parametrization: \(F_X=Z^{q+1}\), \(F_Y=0\), and \(F_Z=XZ^q\), so every affine point is smooth and the only point with \(Z=0\) on the curve is \(P\).

## Proof

**1. Rigidity of projective transformations.** Any projective automorphism must fix the unique singular point \(P\) and preserve its unique tangent line \(Z=0\). After scaling its representing matrix, it therefore has affine action
\[
x\longmapsto A x+B,\qquad y\longmapsto Cx+Dy+E,\qquad AD\ne0.
\]
Because an automorphism of the curve lifts to its normalization and fixes \(t=\infty\), it induces \(t\longmapsto\alpha t+\beta\) with \(\alpha\ne0\). Comparing the first coordinate gives \(A=\alpha^q\) and \(B=\beta^q\). Comparing the second coordinate reduces to the polynomial identity
\[
C t^q+D(t^{q+2}+t)+E
=\alpha^{q+2}t^{q+2}+\alpha^q\beta^2t^q
+\beta^q\alpha^2t^2+\beta^{q+2}+\alpha t+\beta.
\]
For \(q\geq4\), the powers \(0,1,2,q,q+2\) are distinct. The coefficient of \(t^2\) forces \(\beta=0\). Comparison of the remaining coefficients gives \(C=E=0\) and \(D=\alpha=\alpha^{q+2}\), hence \(\alpha^{q+1}=1\). This proves the asserted exhaustive cyclic list. Each listed diagonal matrix preserves the defining equation up to the nonzero factor \(\alpha^q\).

For \(q=2\), the two terms of degree \(2\) on the right cancel in characteristic two; indeed \((\alpha t+\beta)^4=\alpha^4t^4+\beta^4\). Hence \(C=0\), \(D=\alpha=\alpha^4\), and \(E=\beta^4+\beta\), with \(\beta\) unrestricted. The matrices in the theorem realize these transformations and their composition is the affine group law \((\alpha,\beta)(\alpha',\beta')=(\alpha\alpha',\alpha\beta'+\beta)\). This proves the degree-four case.

**2. Lie algebra of the full projective stabilizer scheme.** For a first-order matrix deformation \(I+\varepsilon A\), with \(\varepsilon^2=0\) and \(A=(a_{ij})\), write \(\delta X=a_{11}X+a_{12}Y+a_{13}Z\) and \(\delta Z=a_{31}X+a_{32}Y+a_{33}Z\). For \(F=Z^2Y^q+X^{q+2}+XZ^{q+1}\) in characteristic two,
\[
\delta F=F_X\delta X+F_Y\delta Y+F_Z\delta Z
=Z^{q+1}\delta X+XZ^q\delta Z.
\]
The condition \(\delta F=\lambda F\) forces \(\lambda=0\) by the coefficient of \(X^{q+2}\). Comparing distinct remaining monomials forces
\[
a_{31}=a_{32}=a_{12}=a_{13}=0,\qquad a_{11}=a_{33}.
\]
The entire middle row \((a_{21},a_{22},a_{23})\) remains free. Modulo scalar matrices the Lie algebra consequently has dimension exactly \(3\). The reduced geometric stabilizer has dimension \(0\) for \(q\geq4\) and dimension \(1\) for \(q=2\), by Step 1. Therefore \(\mathscr G_q\) is non-smooth in every case.

**3. Explicit nonreduced finite subgroup.** For a commutative \(k\)-algebra \(R\), choose units \(d\in R^\times\) and \(c,e\in R\) satisfying
\[
d^{q(q+1)}=1,\qquad c^q=e^q=0.
\]
Set \(X'=d^qX\), \(Y'=cX+dY+eZ\), and \(Z'=Z\). The determinant is invertible and Frobenius gives
\[
F(X',Y',Z')=d^q F(X,Y,Z),
\]
so these matrices form a closed subgroup scheme of the stabilizer. Its coordinate ring is
\[
k[d,d^{-1},c,e]/(d^{q(q+1)}-1,c^q,e^q),
\]
which has \(k\)-length \(q(q+1)\,q\,q=q^3(q+1)\). This establishes the asserted quantitative infinitesimal structure. It does **not** assert that the subgroup equals the full stabilizer scheme.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It represents polynomials as monomial sets over \(\mathbb F_2\), enumerates all \(168\) elements of \(\mathrm{PGL}_3(\mathbb F_2)\), substitutes each into \(F\), and separately computes the linearized coefficient-map rank for \(q=2,4,8,16\). The observed geometric stabilizer counts over \(\mathbb F_2\) are \(2,1,1,1\), respectively, and the Lie dimension is \(3\) in all four examples. The executable ends with `VERIFY_OK`.

These finite-field checks cannot establish the full algebraically closed group classification or an infinite-family statement; Steps 1–3 do that. The formula for the subgroup scheme is an exact symbolic Frobenius identity, not a finite enumeration.

## Relationship to prior work

János Kollár's 2026 construction gives the parametrization, rationality, unique cusp and characteristic-dependent lifting phenomena of precisely these curves. Its inspected mathematical text does not classify the projective automorphism group or its nonreduced stabilizer scheme. The present statement concerns additional equivariant geometry of that explicit construction, not a new construction of the curves or their cusps.

Chen and Contreras investigate strange rational plane curves, but the degree-\(p\) family named in the accessible abstract has a different degree from \(q+2\) in characteristic \(2\), and is not a stated classification of the stabilizers here. Other accessible mathematical research records on projective stabilizers concern different objects and do not imply the displayed group formulas. The general possibility of non-smooth group schemes in positive characteristic is, of course, established background; the claim is the exact behavior of this specified infinite family.

## Limitations

The theorem does not compute the complete scheme-theoretic stabilizer, its full nilpotent coordinate ring, or automorphisms of the normalization unrelated to projective transformations. The existence of the finite subgroup scheme is not an equality claim. A distinct older treatment under the terminology of strange curves or inseparable Gauss maps could contain an equivalent classification; historical priority therefore remains provisional. No independent mathematical validation is claimed.

## References

1. János Kollár, *Planar, rational curves over \(\mathbb F_2\), whose only singularity is a double point*, arXiv:2603.04211, first submitted 2026-03-04, Example 1, Lemma 2, Example 3, and Remark 7; public full HTML: https://arxiv.org/html/2603.04211.
2. Qile Chen and Ryan Contreras, *Plane \(\mathbb A^1\)-curves on the complement of strange rational curves*, arXiv:2108.09024 (2021); abstract-level comparison only.
3. *Mathematics Subject Classification 2020*, class 14H37 (automorphisms of curves), https://mathscinet.ams.org/msc/msc2020.html?t=14H20.
