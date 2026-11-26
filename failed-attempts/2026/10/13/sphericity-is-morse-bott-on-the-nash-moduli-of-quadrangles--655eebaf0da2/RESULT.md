# Sphericity is Morse--Bott on the Nash moduli of quadrangles
## Finding
Let \(\mathcal Q\) be the eight-dimensional Nash manifold of labeled planar quadrangles constructed by Olberding--Walker, and let \(G\subseteq\operatorname{Sim}(\mathbb R^2)\) be any Nash subgroup. Write
\[
s:\mathcal Q\longrightarrow[0,1]
\]
for their sphericity function and \(\bar s:\mathcal Q/G\to[0,1]\) for its descended function.

Then \(s\) and \(\bar s\) are Morse--Bott in the clean differential-geometric sense: their critical sets are unions of embedded submanifolds and the Hessian kernel at each critical point equals the tangent space of the relevant critical submanifold. There are exactly two critical submanifolds:
\[
C_-={Q:\operatorname{aspect}(Q)=-1},\qquad
C_+={Q:\operatorname{aspect}(Q)=1}.
\]
For \(s\), \(C_-\) has codimension \(1\), critical value \(0\), and positive one-dimensional normal Hessian, hence Morse index \(0\). The locus \(C_+\) has codimension \(2\), critical value \(1\), and negative-definite two-dimensional normal Hessian, hence Morse index \(2\). For \(\bar s\), the critical manifolds are exactly \(C_-/G\) and \(C_+/G\), with the same codimensions, critical values, and normal indices. There are no other critical points.

## Assumptions and scope
All objects and terminology are those of arXiv:2610.02087v1. In particular, quadrangles retain the six labeled joining lines, and \(G\) is a Nash subgroup of the real similarity group. The source proves that \(\mathcal Q\) and \(\mathcal Q/G\) are Nash manifolds, that the action is free and proper, that the quotient is a principal \(G\)-bundle, and that sphericity is a similarity-invariant Nash function descending to the quotient.

Here “Morse--Bott” is used only in the local clean-Hessian sense stated above; no compactness of the critical manifolds is assumed.

## Proof
The source associates to every quadrangle a projective form \([a:b:c]\in\mathbb{RP}^2\), and the form map
\[
F:\mathcal Q\longrightarrow\mathbb{RP}^2
\]
is a Nash submersion. Its sphericity formula is
\[
s(Q)=\frac{(a+c)^2}{2(a^2+2b^2+c^2)}.
\]
Introduce homogeneous linear coordinates
\[
u=a+c,\qquad v=b,\qquad w=a-c.
\]
Since
\[
2(a^2+2b^2+c^2)=u^2+w^2+4v^2,
\]
the corresponding function on \(\mathbb{RP}^2\) is
\[
h([u:v:w])=\frac{u^2}{u^2+w^2+4v^2},
\qquad s=h\circ F.
\]

The aspect \(-1\) locus in form space is the projective line \(L=\{u=0\}\). Around any point of \(L\) with \(w\ne0\), use the chart \(w=1\):
\[
h(u,v)=\frac{u^2}{u^2+1+4v^2}.
\]
At \(u=0\), both first derivatives vanish, while the Hessian has
\[
\frac{\partial^2 h}{\partial u^2}(0,v)=\frac{2}{1+4v^2}>0,
\qquad
\frac{\partial^2 h}{\partial u\partial v}(0,v)=
\frac{\partial^2 h}{\partial v^2}(0,v)=0.
\]
At the one point of \(L\) not covered by \(w\ne0\), the chart \(v=1\) gives
\[
h(u,w)=\frac{u^2}{u^2+w^2+4},
\]
with the same conclusion. Thus \(L\) is a clean critical manifold, the Hessian kernel is its tangent line, and the transverse Hessian is positive.

The aspect \(1\) form is the single point \([1:0:0]\) in \([u:v:w]\)-coordinates. In the chart \(u=1\),
\[
h(v,w)=\frac{1}{1+w^2+4v^2}.
\]
Its only critical point is \((v,w)=(0,0)\), where
\[
\operatorname{Hess} h=
\begin{pmatrix}-8&0\\0&-2\end{pmatrix},
\]
so it is a nondegenerate maximum of index \(2\).

Olberding--Walker prove that sphericity is a submersion away from aspect \(\pm1\), so these are all critical points of \(h\circ F\). Because \(F\) is a submersion, pulling back the above local models adds only tangent directions along fibers of \(F\): the Hessian kernel on \(\mathcal Q\) is exactly the tangent space to \(C_-\) or \(C_+\), and the normal Hessian has the same sign and rank as in form space.

Finally, the quotient map \(\pi:\mathcal Q\to\mathcal Q/G\) is a principal-bundle Nash submersion and \(s=\bar s\circ\pi\). Local principal-bundle trivializations identify \(s\) with the pullback of \(\bar s\) from the quotient factor. Hence criticality and the normal Hessian are unchanged by removing the orbit directions, which already lie tangent to the invariant critical manifolds. Therefore the quotient critical manifolds are exactly \(C_-/G\) and \(C_+/G\), with codimensions \(1\) and \(2\) and Morse indices \(0\) and \(2\), respectively.

## Verification
The accompanying `verify.py` differentiates the two exact rational chart formulas symbolically and checks:
- vanishing of the gradient on the full aspect \(-1\) critical line;
- positivity and rank \(1\) of its normal Hessian;
- the unique aspect \(1\) critical point;
- the exact Hessian eigenvalues \(-8\) and \(-2\) there;
- the coordinate identity converting the source sphericity formula to \(u^2/(u^2+w^2+4v^2)\).

Its recorded output ends in `VERIFY_OK`.

The noncomputational inputs checked in the source are the Nash-submersion property of the form map, the free proper similarity action and principal quotient, the sphericity formula and descent, the identification of aspect \(\pm1\) level sets, and the source lemma that sphericity is a submersion away from those two aspect values.

## Relationship to prior work
Olberding--Walker identify the aspect \(-1,0,1\) fibers as exceptional for their aspect-based product decomposition. They prove that sphericity is Nash everywhere, that its interior-level fibers are embedded Nash submanifolds, and that it is a submersion away from aspect \(\pm1\). Their paper does not state a Morse--Bott theorem or compute the Hessian at the two endpoint fibers.

The present calculation closes that local question: both endpoint failures of submersivity are clean and quadratic, but of different normal ranks. The hyperbolic endpoint \(\operatorname{aspect}=-1\) is a codimension-one Morse--Bott minimum, whereas the circular endpoint \(\operatorname{aspect}=1\) is a codimension-two Morse--Bott maximum. Targeted searches for the paper together with “Morse--Bott”, “critical locus”, “Hessian”, and “sphericity” did not locate a prior statement of this refinement.

## Limitations
This is a local differential-geometric refinement of the source's sphericity stratification; it does not determine the global topology of either critical manifold or its quotient, and it does not claim a Morse-theoretic cell decomposition of the noncompact moduli space. The proof uses the source's form-map submersion and principal-bundle quotient theorems. A residual originality risk is that the same short Hessian observation could occur in unindexed notes or discussions.

## References
1. Bruce Olberding and Elaine A. Walker, *The Nash manifold of four-point configurations modulo similarity subgroups*, arXiv:2610.02087v1, 1 October 2026.
