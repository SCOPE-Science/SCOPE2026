# Six cusps, four nonsplit nodes, and the generalized Jacobian of the characteristic-five Wiman sextic

## Finding
Let \(C\subset\mathbb P^2_{\mathbb F_5}\) be the reduced plane sextic given by the coefficientwise reduction of Wiman's classical equation
\[
F_0=X^6+Y^6+Z^6+(X^2+Y^2+Z^2)(X^4+Y^4+Z^4)-12X^2Y^2Z^2.
\]
Its ten geometric singular points are all rational: six ordinary cusps of type \(A_2\) and four nonsplit nodes of type \(A_1\). Over \(\mathbb F_5\),
\[
\operatorname{Pic}^0(C)\simeq\mathbb G_a^6\times (\operatorname{Res}^{1}_{\mathbb F_{25}/\mathbb F_5}\mathbb G_m)^4.
\]
For every \(m\ge1\) and \(q=5^m\),
\[
\#C(\mathbb F_q)=q+1-4(-1)^m,\quad Z(C/\mathbb F_5,T)=\frac{(1+T)^4}{(1-T)(1-5T)},\quad \#\operatorname{Pic}^0(C)(\mathbb F_q)=q^6(q-(-1)^m)^4.
\]
In particular, the smooth locus \(C^{\rm sm}\) has no points over \(\mathbb F_5\), although it has twelve points over \(\mathbb F_{25}\).

## Assumptions and scope
All equations are in the displayed projective plane over \(\mathbb F_5\); all singularities are geometric, and all group-scheme identifications are over the base field itself. The notation \(\operatorname{Res}^{1}_{\mathbb F_{25}/\mathbb F_5}\mathbb G_m\) means the one-dimensional norm-one torus. The curve is the coefficientwise plane model, not a stable-reduction assertion about another integral model. The geometric rationality of this mod-five curve is a pre-existing theorem of Giulietti--Kawakita--Lia--Montanucci [2] used explicitly below.

## Proof
Set \(S=X^2+Y^2+Z^2\). Newton identities in the squared variables give the integral identity \(F_0=2S^3-5S(X^2Y^2+Y^2Z^2+Z^2X^2)-9X^2Y^2Z^2\); hence in characteristic five
\[
F=2S^3+X^2Y^2Z^2,
\qquad F_X=2X(S^2+Y^2Z^2)
\]
and likewise cyclically. If one coordinate, say \(X\), vanishes at a singular point, the other two nonzero coordinates and their derivative equations force \(S=0\). Since \(-1=2^2\) in \(\mathbb F_5\), this yields two points on each coordinate line, namely
\[
[0:2:1],[0:3:1],[2:0:1],[3:0:1],[2:1:0],[3:1:0].
\]
If no coordinate vanishes, subtracting the three derivative equations yields \(X^2=Y^2=Z^2\); these are the four points \([1:1:1],[1:-1:1],[-1:1:1],[-1:-1:1]\). They satisfy \(F=0\) and exhaust the geometric singular set.

At \([0:2:1]\), and similarly at every axis point by sign changes/permutation, use local étale coordinates \(u=XY\) and \(v=S\) on \(Z=1\). Their Jacobian determinant is nonzero because \(Y\ne0\). The defining equation is exactly \(u^2+2v^3=0\), so each is an ordinary \((2,3)\) cusp with one rational branch, delta invariant one, and local normalization-units quotient \(\mathbb G_a\).

At the four points with \(Z=1\) and \(X,Y\in\{\pm1\}\), the quadratic term is equivalent over \(\mathbb F_5\) to \(2u^2+3uv+2v^2\). Its discriminant \(3^2-4\cdot2\cdot2=3\) modulo five is nonsquare, giving a geometrically ordinary node whose two normalization branches are exchanged by Frobenius. The local normalization-units quotient is the nonsplit one-dimensional torus \(\operatorname{Res}_{\mathbb F_{25}/\mathbb F_5}\mathbb G_m/\mathbb G_m\cong\operatorname{Res}^{1}_{\mathbb F_{25}/\mathbb F_5}\mathbb G_m\).

Geometric integrality/rationality of this exceptional characteristic-five Wiman sextic is established in [2, Remark 3.1 and Theorem 3.4]; no new rationality theorem is claimed. Its plane arithmetic genus is \((6-1)(6-2)/2=10\); the six cusps and four nodes contribute delta sum ten, also confirming geometric genus zero. Every smooth genus-zero curve over a finite field has a rational point, so the normalization \(\widetilde C\) is \(\mathbb P^1_{\mathbb F_5}\).

The normalization exact sequence for invertible sheaves gives the connected generalized Jacobian as the product of the ten local normalization-unit quotients because \(\operatorname{Pic}^0(\widetilde C)=0\). This gives the asserted base-field group-scheme isomorphism. For an extension \(\mathbb F_q/\mathbb F_5\), each cusp contributes the same unique rational normalization branch; each nonsplit rational node replaces zero rational branches by one rational singular point when \(m\) is odd, and replaces two branches by one point when \(m\) is even. Therefore \(\#C(\mathbb F_q)=q+1-4(-1)^m\). Taking the point-count exponential yields the zeta formula. The norm-one torus has \(q+1\) points for odd \(m\) and \(q-1\) for even \(m\), proving the generalized-Jacobian count. For \(m=1\), the curve has ten points, exactly its ten singularities; for \(m=2\), the curve has twenty-two points, of which ten are singular.

## Verification
Run `python verify_wiman5.py`. This standalone exact computation reconstructs the characteristic-five polynomial identity and gradients, verifies the ten explicit singular points, the nonsplit-node quadratic discriminants, and full projective counts over \(\mathbb F_5\) and \(\mathbb F_{25}\), yielding 10 and 22. The all-extension formulas follow from normalization and are not inferred from these two counts. A successful recorded run appears in `verification_output.txt`.

## Relationship to prior work
Inoue--Kato [1] present the classical Wiman sextic and its four characteristic-zero nodes. Giulietti--Kawakita--Lia--Montanucci [2] explicitly prove that the characteristic-five curve is rational; this stronger earlier fact is adopted as an input rather than claimed new. Their discussion of the exceptional reduction does not present the six-cusp/four-nonsplit-node arithmetic profile or the connected generalized-Jacobian decomposition computed here. Edge [3] studies the complex four-nodal sextic pencil. The six-cusp classification, Frobenius splitting and algebraic-group structure are more precise than the previously known genus-zero statement.

## Limitations
The geometric rationality premise is sourced from published work, not reproved from scratch. The result concerns only the specified coefficientwise reduction and not arbitrary deformations, stable models, or Jacobian specializations. The originality comparison relies on accessible primary passages and indexed mathematical records; historical priority is not independently certified. An independent scientific audit has not been performed.

## References
[1] N. Inoue and F. Kato, *On the geometry of Wiman's sextic*, J. Math. Kyoto Univ. 45 (2005), 743--757, doi:10.1215/kjm/1250281655 (catalogued public publication date 2006-07-14).

[2] M. Giulietti, M. Kawakita, S. Lia, M. Montanucci, *An \(\mathbb F_{p^2}\)-maximal Wiman's sextic and its automorphisms*, arXiv:1805.06317, 2018, Remark 3.1 and Theorem 3.4, https://arxiv.org/abs/1805.06317.

[3] W. L. Edge, *A pencil of four-nodal plane sextics*, Mathematical Proceedings of the Cambridge Philosophical Society, available online 2008-10-24.
