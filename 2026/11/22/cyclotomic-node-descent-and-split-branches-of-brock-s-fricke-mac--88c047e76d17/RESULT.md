# Cyclotomic node descent and split branches of Brock's Fricke–Macbeath octic

## Finding
Let \(C\subset\mathbb P^2_{\mathbb Q}\) be the degree-eight plane curve whose affine equation is
\[
F(x,y)=1+7xy+21x^2y^2+35x^3y^3+28x^4y^4+2x^7+2y^7=0.
\]
Set \(\zeta=\zeta_7\) to be a primitive seventh root of unity, and let \(r_+,r_-\) be the two roots of \(2r^2+r+1=0\). The **entire geometric singular locus**, with no singularities at infinity, is
\[
N=\left\{(\zeta^j r_\epsilon,\zeta^{-j}r_\epsilon):
\epsilon\in\{+,-\},\ 0\le j\le6\right\}.
\]
All fourteen points are ordinary nodes, and the two tangent lines at each node are the horizontal and vertical lines through it. In particular, the two normalization branches are separately defined over the residue field of every closed node.

Over \(\mathbb Q\), the reduced node scheme has exactly three closed points, of degrees \(2,6,6\). Their common splitting field is **exactly** \(\mathbb Q(\zeta_7)\), and each degree-six closed point already has that residue field. Equivalently, the node \(x\)-coordinate polynomial factors over \(\mathbb Q\) as
\[
\begin{aligned}
128x^{14}-13x^7+1={}&(2x^2+x+1)\\
&\cdot(8x^6-16x^5+18x^4-15x^3+9x^2-4x+1)\\
&\cdot(8x^6+12x^5+4x^4-x^3+2x^2+3x+1),
\end{aligned}
\]
with all three factors irreducible over \(\mathbb Q\).

For every finite field \(\mathbb F_q\) of characteristic different from \(2\) and \(7\), the same fourteen distinct split nodes occur geometrically, and the Frobenius orbit partition is determined *entirely* by \(q\bmod7\):

| \(q\bmod7\) | Frobenius node cycles | Node-scheme zeta function \(Z(N_q,T)\) |
|---|---|---|
| \(1\) | \(1^{14}\) | \((1-T)^{-14}\) |
| \(2,4\) | \(1^2 3^4\) | \((1-T)^{-2}(1-T^3)^{-4}\) |
| \(6\) | \(2^7\) | \((1-T^2)^{-7}\) |
| \(3,5\) | \(2^1 6^2\) | \((1-T^2)^{-1}(1-T^6)^{-2}\) |

Writing \(\widetilde C_q\) for the smooth normalization of \(C_q\), for every \(m\ge1\),
\[
\#\widetilde C_q(\mathbb F_{q^m})-\#C_q(\mathbb F_{q^m})
=\#N_q(\mathbb F_{q^m}),\qquad
\frac{Z(\widetilde C_q,T)}{Z(C_q,T)}=Z(N_q,T).
\]
This gives the *complete* normalization correction to the plane-octic point counts and zeta function, for every extension degree, without computing the genus-seven zeta function itself.

## Assumptions and scope
The characteristic-zero statement concerns **this displayed rational plane model** of the genus-seven Fricke–Macbeath curve, rather than every rational twist or canonical model. The finite-field statements apply to its coefficientwise reductions for all prime powers \(q\) with \(\operatorname{char}(\mathbb F_q)\notin\{2,7\}\). In particular, the excluded characteristics are not assigned any node or branch profile. All singular points are regarded geometrically over an algebraic closure before their arithmetic descent is considered. For a finite field \(\mathbb F_q\), \(Z(X,T)=\exp(\sum_{m\ge1}\#X(\mathbb F_{q^m})T^m/m)\).

## Proof
Put \(t=xy\) and \(P(t)=1+7t+21t^2+35t^3+28t^4\), so \(F=P(t)+2x^7+2y^7\). At a finite singular point, the two partial derivative equations, multiplied respectively by \(x\) and \(y\), give
\[
14x^7=14y^7=-tP'(t).
\]
If \(t=0\), these force \(x=y=0\) (in the stated characteristics), contradicting \(F(0,0)=1\). Thus \(t\ne0\). Substitution into \(F=0\), followed by taking the product of the two seventh-power identities, yields
\[
7P(t)-2tP'(t)=0,\qquad 196t^5-P'(t)^2=0.
\]
The exact integer identities are
\[
\begin{aligned}
7P-2tP'&=-7(t^2-2t-1)(4t^2+3t+1),\\
196t^5-P'^2&=-49(4t^2+3t+1)
(64t^4+71t^3+35t^2+9t+1).
\end{aligned}
\]
The resultant of the quadratic \(t^2-2t-1\) and the displayed quartic factor is \(392=2^3\cdot7^2\). Hence, in every characteristic under consideration, any singular point must have \(4t^2+3t+1=0\). Conversely, take either root \(r\) of \(2r^2+r+1=0\); then \(t=r^2=-(r+1)/2\) satisfies that equation. Direct reduction modulo \(2r^2+r+1\) gives \(F(r,r)=F_x(r,r)=F_y(r,r)=0\). The symmetry \((x,y)\mapsto(\zeta^j x,\zeta^{-j}y)\) preserves \(F\) and produces the seven listed singular points from each \(r\). They are all distinct, so these are exactly the fourteen finite singular points.

The homogeneous degree-eight equation is
\[
Z^8+7XYZ^6+21X^2Y^2Z^4+35X^3Y^3Z^2+28X^4Y^4+2(X^7+Y^7)Z=0.
\]
At \(Z=0\), its only points are \([1:0:0]\) and \([0:1:0]\), and in each case the derivative with respect to \(Z\) is \(2\ne0\). Thus the singular list is exhaustive in the projective plane.

For ordinary-branch splitting, the second partial derivatives satisfy
\[
\begin{aligned}
x^2F_{xx}&=t\bigl(tP''-6P'\bigr),\\
y^2F_{yy}&=t\bigl(tP''-6P'\bigr),\\
F_{xy}&=P'+tP''.
\end{aligned}
\]
Modulo \(4t^2+3t+1\), the first parenthesis vanishes identically and
\[
P'+tP''=\frac{49}{4}(1-t).
\]
This last scalar is nonzero: \(t=1\) would contradict \(4t^2+3t+1=0\) because its left side at \(t=1\) equals \(8\). Therefore each tangent cone is a nonzero multiple of \(dX\,dY\). It consists of two distinct lines, both over the node's residue field, proving that every singularity is an ordinary **split** node.

For completeness, geometric integrality of the reductions can be verified without assuming that point enumeration implies it. In the function field set \(u=x^7\); the equation gives \(2u^2+P(t)u+2t^7=0\), whose discriminant factors as
\[
P(t)^2-16t^7=(4t^2+3t+1)^2 Q(t),\quad
Q(t)=49t^4+48t^3+26t^2+8t+1.
\]
Here \(\operatorname{disc}(Q)=2^{12}7^2\), so \(v^2=Q(t)\) is a smooth genus-one curve in all stated characteristics. In its function field, \(u=((4t^2+3t+1)v-P(t))/4\). At one of the two places above \(t=\infty\), choose the sign \(v\sim-7t^2\); then \(u\sim-14t^4\), a pole of order four. Therefore \(u\) is not a seventh power; Kummer theory (characteristic not seven) makes \(x^7=u\) an irreducible degree-seven extension. Thus the plane octic is geometrically integral. Its normalization has genus \((8-1)(8-2)/2-14=7\).

For arithmetic descent, write \(r_\pm=(-1\pm\sqrt{-7})/4\). The quadratic Gauss sum
\[
\sqrt{-7}=\zeta+\zeta^2+\zeta^4-\zeta^3-\zeta^5-\zeta^6
\]
(with an appropriate choice of sign) lies in \(\mathbb Q(\zeta)\) and changes sign precisely under nonsquare multipliers in \((\mathbb Z/7)^{\times}\). Thus a Galois element \(\sigma_a:\zeta\mapsto\zeta^a\) sends \((r_\epsilon,j)\) to \((r_{\chi_7(a)\epsilon},aj)\). The two \(j=0\) nodes form one degree-two orbit. Each of the two orbits among \(j\ne0\) has six points; moreover the ratio of the two coordinates of any such node is \(\zeta^{2j}\), so its residue field is exactly \(\mathbb Q(\zeta)\). This proves the claimed fields and orbit degrees. Replacing \(a\) by \(q\bmod7\) gives the four finite-field cycle rows.

Finally, over a perfect field every split ordinary node has two distinct, separately rational normalization preimages over its residue field. The difference between the normalization and singular-curve counts over any finite extension is therefore exactly the number of nodes rational over that extension. Exponentiating this equality in the definition of zeta functions yields the displayed quotient.

## Verification
Run `python3 verify_brock_octic.py` with SymPy installed. The script checks both elimination factorizations, their critical resultant, the genus-one discriminant identity, the Hessian and diagonal-node substitutions, the irreducible \(2+6+6\) coordinate factorization, the quadratic Gauss-sum identity, all six multipliers' Frobenius cycle decompositions, and exhaustive direct affine singular-point counts over twelve auxiliary prime fields. It prints `BROCK_OCTIC_NODE_GALOIS_AND_BRANCH_CERTIFICATE_OK` on success. The finite-field loops are supplementary checks; the all-characteristic and all-extension conclusions are consequences of the symbolic identities and the proof, not of finite enumeration.

## Relationship to prior work
Hidalgo's openly posted 2012 study records Brock's rational affine equation and explains the Fricke–Macbeath descent. Top and Verschoor's later full-text study explicitly identifies its fourteen nodes and absence of singularities at infinity, and gives good-reduction and point-count results for the normalization as well as the seventh-order automorphism. Those geometric, model, group-action, and normalization facts are treated as **prior knowledge**, not newly discovered. The result here refines the fourteen-node statement by determining its exact arithmetic closed-point fields and universal Frobenius spectra, and refines its good-reduction statement by determining *both individual normalization branches* over every node's residue field, hence the precise zeta correction for the displayed singular octic. Existing arithmetic formulas for the smooth normalization do not themselves specify the point-count correction for this singular plane presentation.

## Limitations
This theorem concerns a fixed plane model, not every rational form of the Fricke–Macbeath curve. It excludes characteristics two and seven, for which the elimination and tangent arguments can fail. The displayed zeta identity determines the normalization-to-plane correction, not the numerical zeta numerator of the normalization. The existence of older equivalent arithmetic-node computations, particularly in unindexed theses or appendices, cannot be ruled out solely by the searches reported in the accompanying review; independent priority assessment has not been performed.

## References
1. R. A. Hidalgo, *A computational note about Fricke-Macbeath's curve*, arXiv:1203.6314, publicly posted 2012-03-28. https://arxiv.org/abs/1203.6314
2. J. Top and C. Verschoor, *Counting points on the Fricke–Macbeath curve over finite fields*, Journal de Théorie des Nombres de Bordeaux **30** (2018), 117–129, DOI:10.5802/jtnb.1019. Lawful full text: https://manypoints.org/upload/1751058917.pdf
3. A. M. Macbeath, *On a curve of genus 7*, Proceedings of the London Mathematical Society **15** (1965), 527–542, DOI:10.1112/plms/s3-15.1.527. Background on the geometric genus-seven Hurwitz curve.
