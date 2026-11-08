# Projective symmetries and arithmetic descent of the characteristic-two cuspidal curves

## Finding

For each integer \(n\ge2\), set \(q=2^n\), let \(k=\overline{\mathbb F}_2\), and consider the reduced plane curve
\[
C_q:\quad Z^2Y^q=X^{q+2}+XZ^{q+1}\quad\subset\mathbb P_k^2.
\]
The entire projective linear stabilizer, **as a group of geometric points**, is
\[
\operatorname{Stab}_{\operatorname{PGL}_3(k)}(C_q)=
\left\{[X:Y:Z]\longmapsto[\alpha^qX:\alpha Y:Z]:\ \alpha^{q+1}=1\right\}
\cong C_{q+1}.
\]
For each positive integer \(r\), its subgroup defined over \(\mathbb F_{2^r}\) is cyclic of order
\[
\gcd(2^n+1,2^r-1).
\]
Thus the projective stabilizer over \(\mathbb F_2\) is trivial, although its geometric stabilizer has order \(2^n+1\). All geometric projective stabilizers are defined over \(\mathbb F_{2^{2n}}\), and no smaller finite extension defines the entire group.

## Assumptions and scope

The base field is the algebraic closure of \(\mathbb F_2\). The integer \(n\) is arbitrary subject only to \(n\ge2\); all formulas are simultaneous in this infinite range. A projective stabilizer means an element of the **ordinary group** \(\operatorname{PGL}_3(k)\) that preserves the embedded reduced curve setwise (equivalently as a reduced closed subscheme). The results over finite fields concern \(\operatorname{PGL}_3(\mathbb F_{2^r})\). No claim is made about the possibly nonreduced stabilizer group scheme, abstract automorphisms of the normalization, or arbitrary Cremona transformations.

The plane curve and its unicuspidal geometry were introduced by Kollár; only the explicit stabilizer and arithmetic descent statements are asserted here as the new finding.

## Proof

**1. Unique distinguished point and tangent.** Write
\[
F=Z^2Y^q+X^{q+2}+XZ^{q+1}.
\]
In characteristic two with \(q=2^n\), its partial derivatives are
\[
F_X=Z^{q+1},\qquad F_Y=0,\qquad F_Z=XZ^q.
\]
The only geometric singular point of \(C_q\) is \(P=[0:1:0]\). Indeed every singular point has \(Z=0\), and then the equation forces \(X=0\). In the chart \(Y=1\), the local equation at \(P\) has initial homogeneous term \(z^2\), so its unique tangent line is \(L=(Z=0)\). Any projective transformation preserving \(C_q\) must fix \(P\) and preserve \(L\).

**2. The affine curve is exactly an affine line.** On \(Z=1\), the defining equation reads
\[
y^q=x^{q+2}+x.
\]
It has the explicit parametrization
\[
\varphi(t)=(t^q,t^{q+2}+t)=(x,y).
\]
This gives a closed embedding: for each algebraically closed-field point of the affine curve the value \(t\) is uniquely the \(q\)-th root of \(x\), and the defining equation forces the displayed value of \(y\). Its polynomial inverse on the coordinate ring is
\[
t=x^q+\sum_{j=0}^{n-1}x^{2^j-1}y^{2^j}.
\]
For completeness, from \(y=t+xt^2\) one has the characteristic-two recurrence \(t=y+xt^2\). Substituting this recurrence \(n\) times gives
\[
t=\sum_{j=0}^{n-1}x^{2^j-1}y^{2^j}+x^{q-1}t^q.
\]
As \(t^q=x\), the displayed polynomial inverse follows. Consequently \(C_q\setminus\{P\}\cong\mathbb A^1_k\), and every automorphism of this affine curve induces \(t\mapsto\alpha t+\beta\), where \(\alpha\in k^\times\), \(\beta\in k\).

**3. Coefficient comparison determines every projective transformation.** A projective linear transformation fixing \(P\) and preserving \(L\) has, after scaling its matrix, the affine form
\[
x\longmapsto Ax+B,\qquad y\longmapsto Cx+Dy+E,
\qquad A,D\in k^\times.
\]
Its induced action on \(C_q\setminus\{P\}\cong\mathbb A^1\) is some \(t\mapsto\alpha t+\beta\). Comparing first coordinates yields
\[
A=\alpha^q,\qquad B=\beta^q.
\]
Comparing the second coordinates gives the polynomial identity
\[
C t^q+D(t^{q+2}+t)+E
=(\alpha t+\beta)^{q+2}+\alpha t+\beta.
\]
In characteristic two the right-hand side equals
\[
\alpha^{q+2}t^{q+2}+\alpha^q\beta^2t^q+
\alpha^2\beta^q t^2+\beta^{q+2}+\alpha t+\beta.
\]
Because \(q\ge4\), the powers \(0,1,2,q,q+2\) are distinct. There is no \(t^2\) term on the left, so \(\alpha^2\beta^q=0\) and hence \(\beta=0\). Matching the remaining coefficients gives
\[
D=\alpha^{q+2}=\alpha,\qquad C=E=0,
\qquad\alpha^{q+1}=1.
\]
Thus any projective stabilizer is necessarily the stated diagonal element. Conversely these elements preserve the polynomial equation: the weights of \(Z^2Y^q\), \(X^{q+2}\), and \(XZ^{q+1}\) all agree because \(\alpha^{q+1}=1\). The set of roots \(\mu_{q+1}(k)\) is cyclic of order \(q+1\), which is odd, so the geometric group is precisely \(C_{q+1}\).

**4. Descent and minimal defining field.** The above projective matrix has been uniquely normalized to have lower-right entry one. It has coefficients in \(\mathbb F_{2^r}\) exactly if \(\alpha\in\mathbb F_{2^r}\). Since \(\mathbb F_{2^r}^{\times}\) is cyclic,
\[
\#\operatorname{Stab}_{\operatorname{PGL}_3(\mathbb F_{2^r})}(C_q)
=\gcd(q+1,2^r-1).
\]
Now \(2^n\equiv-1\pmod{q+1}\), so \(2^{2n}\equiv1\pmod{q+1}\). If its multiplicative order were a proper divisor \(d\) of \(2n\), then \(d\le n\), whence \(0<2^d-1<2^n+1\), contradicting divisibility by \(2^n+1\). Therefore \(\operatorname{ord}_{q+1}(2)=2n\), and \(\mathbb F_{2^{2n}}\) is the smallest finite field containing all \((q+1)\)-st roots of unity. Finally \(\gcd(q+1,1)=1\), proving the \(\mathbb F_2\)-stabilizer is trivial.

## Verification

The standalone `verify.py` uses exact binary-polynomial arithmetic to check the parametrization and polynomial inverse for \(2\le n\le6\). It also explicitly constructs \(\mathbb F_{2^{2n}}\) for \(n=2,3,4\), enumerates all \((q+1)\)-st roots of unity, checks the derived diagonal action pointwise, and tests the finite-field subgroup counts and minimal defining degrees. Executing `python3 verify.py` produced `CERTIFICATE_OK`; no external dependencies are needed. The all-\(n\) theorem is proved above, not inferred from these finite checks.

## Relationship to prior work

Kollár's *Planar, rational curves over \(\mathbb F_2\), whose only singularity is a double point* (arXiv:2603.04211) supplies the family, its affine parametrization, and its distinguished unicuspidal singularity in Example 3 and Lemma 2. The projective stabilizer and its arithmetic descent are not stated in the inspected full text.

Hemmig's *Isomorphisms between complements of projective plane curves* (arXiv:1902.06324) studies birational and complement equivalence of unicuspidal curves over arbitrary algebraically closed fields; the relevant introductory and unicuspidal sections treat a different equivalence problem and do not determine this family's embedding-preserving projective stabilizer. The polynomial inverse and affine automorphism argument are consistent with standard facts about embeddings of \(\mathbb A^1\).

## Limitations

The theorem is restricted to the displayed characteristic-two family and ordinary projective linear automorphisms (field-valued points); it neither calculates the infinitesimal structure of a group scheme nor describes the much larger automorphism group of the abstract normalization \(\mathbb P^1\). Its comparison with earlier literature supports provisional originality rather than exhaustive historical priority, and independent external mathematical validation has not been performed.

## References

1. J. Kollár, *Planar, rational curves over \(\mathbb F_2\), whose only singularity is a double point*, arXiv:2603.04211, first submitted 2026-03-04, Example 3 and Lemma 2. https://arxiv.org/html/2603.04211
2. M. Hemmig, *Isomorphisms between complements of projective plane curves*, arXiv:1902.06324 (2019), Sections 1 and 3. https://arxiv.org/abs/1902.06324
