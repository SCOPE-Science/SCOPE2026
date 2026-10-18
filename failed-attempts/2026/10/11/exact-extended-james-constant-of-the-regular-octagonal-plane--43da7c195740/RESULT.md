# Exact extended James constant of the regular octagonal plane
## Finding
Let \(X_8=(\mathbb R^2,N)\), where
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For the extended James constant introduced by Chen, Yang, Liu and Li,
\[
J_4(X)=\sup_{\lVert x\rVert^2+\lVert y\rVert^2=2}
\min\{\lVert x+y\rVert,\lVert x-y\rVert\},
\]
one has
\[
J_4(X_8)=2\sqrt{2-\sqrt2}.
\]
Thus \(J_4(X_8)>J(X_8)=\sqrt2\): on this classical non-Hilbert plane the extended domain in the definition produces a strict increase over the ordinary James constant.

## Assumptions and scope
All scalars are real. Put \(q=\sqrt2-1\). The displayed norm has regular-octagonal unit ball with vertices \((\pm1,\pm q)\) and \((\pm q,\pm1)\). The claim concerns only the constant \(J_4\) under the quadratic normalization \(\lVert x\rVert^2+\lVert y\rVert^2=2\).

A proof ingredient needed below is the exact ordinary modulus of smoothness on the relevant interval:
\[
\rho_{X_8}(t)=qt\qquad(0\le t\le1).
\]
This identity is proved here rather than assumed from a numerical experiment.

## Proof
Write
\[
F=\left\{\left(\cos\frac{k\pi}{4},\sin\frac{k\pi}{4}\right):0\le k\le7\right\}.
\]
Then \(N(z)=\max_{f\in F}f(z)\), so the dual unit ball is the regular octagon \(\operatorname{conv}F\). For unit vectors \(u,v\) and \(0\le t\le1\), finiteness of \(F\) and independence of \(u,v\) give
\[
\sup_{u,v\in S_{X_8}}\bigl(N(u+tv)+N(u-tv)\bigr)
 =\max_{f,g\in F}\bigl(N_*(f+g)+tN_*(f-g)\bigr).
\]
By dihedral symmetry only the angular separation \(m\pi/4\), \(0\le m\le4\), matters. The radial boundary of the dual octagon has Euclidean radius \(1\) in vertex directions and \(\cos(\pi/8)\) in edge-normal directions. Using \(\tan(\pi/8)=q\), the five pairs
\[
\bigl(N_*(f+g),N_*(f-g)\bigr)
=(2,0),(2,2q),(\sqrt2,\sqrt2),(2q,2),(0,2)
\]
correspond respectively to \(m=0,1,2,3,4\). For \(0\le t\le1\), the second affine function dominates the others. The two nontrivial comparisons reduce exactly to
\[
2+2qt-\sqrt2(1+t)=(2-\sqrt2)(1-t)\ge0
\]
and
\[
2+2qt-(2q+2t)=2(1-q)(1-t)\ge0.
\]
The endpoint functions are smaller as well. Hence
\[
\sup_{u,v\in S_{X_8}}\frac{N(u+tv)+N(u-tv)}2=1+qt,
\]
which proves \(\rho_{X_8}(t)=qt\) on \([0,1]\).

Now take any admissible pair \(x,y\). Interchange them if necessary so that \(a=\lVert x\rVert\ge b=\lVert y\rVert\). If \(b=0\), the objective is \(\sqrt2\), already below the claimed value. Otherwise put \(t=b/a\in(0,1]\), \(u=x/a\), and \(v=y/b\). Since \(a^2+b^2=2\),
\[
a=\sqrt{\frac{2}{1+t^2}}.
\]
The minimum is at most the arithmetic mean, and the smoothness identity gives
\[
\min\{N(x+y),N(x-y)\}
\le \frac{\sqrt2(1+qt)}{\sqrt{1+t^2}}.
\]
The square of the proposed optimum minus the square of this upper bound is
\[
2(1+q^2)-\frac{2(1+qt)^2}{1+t^2}
=\frac{2(t-q)^2}{1+t^2}\ge0.
\]
Therefore \(J_4(X_8)\le2\sqrt{2-\sqrt2}\).

For equality, take
\[
u=(1,q),\qquad v=(-q,1),\qquad t=q.
\]
Both \(u\) and \(v\) are unit vectors. Moreover,
\[
u+qv=(2q,2q),\qquad u-qv=(1+q^2,0),
\]
and both vectors have norm \(1+q^2\). Set
\[
a=\sqrt{\frac{2}{1+q^2}},\qquad x=au,\qquad y=aqv.
\]
Then \(N(x)^2+N(y)^2=2\), while
\[
N(x+y)=N(x-y)=a(1+q^2)=2\sqrt{2-\sqrt2}.
\]
This attains the upper bound.

## Verification
The accompanying `verify.py` uses exact arithmetic in \(\mathbb Q(\sqrt2)\) to check the algebraic identities in the dual-octagon table, the affine dominance reductions, the scalar maximization identity, and the equality witness. The proof of the infinite optimization is analytic; the checker is a replay of its exact identities, not a finite-sampling substitute.

## Relationship to prior work
Chen, Yang, Liu and Li introduced \(J_4\) in 2022 and established general comparisons with the James constant and the Takahashi--Kato constant; their article describes further study of the new James-type constants as open-ended. The inspected full text does not calculate \(J_4\) for the regular octagonal plane.

The regular octagon is a standard benchmark for Banach-space geometric constants. Yang, Li and Yang compute exact \(L_{YJ}(\lambda,\mu,X)\) and \(L'_{YJ}(\lambda,\mu,X)\) values for this plane and explicitly classify that work under primary MSC 46B20. Those functionals are quadratic sums of skew combinations and do not determine the minimum appearing in \(J_4\). Their paper also records \(J(X_8)=\sqrt2\), making the strict inequality in the present result directly interpretable.

Targeted searches for the exact \(J_4\) value, its radical form, the regular-octagon modulus-of-smoothness profile, and broader regular-polygon coverage did not locate a statement implying this formula. Published-index hits concerning regular polygons use different invariants, such as equilateral perimeter. These searches are supporting evidence rather than a proof of priority.

## Limitations
The theorem is for the real regular-octagonal plane only. It does not claim an all-polygon formula, nor does it claim that the modulus-of-smoothness identity persists beyond \(0\le t\le1\). Literature searches cannot exclude unindexed or inaccessible work; originality is assessed against the defining full text, the closest exact regular-octagon paper inspected in full relevant sections, targeted database searches, and the available prior-result ledger.

## References
1. B. Chen, Z. Yang, Q. Liu, Y. Li, *Some New James Type Geometric Constants in Banach Spaces*, Symmetry 14 (2022), 405. DOI: 10.3390/sym14020405.
2. X. Yang, H. Li, C. Yang, *On the \(L_{YJ}(\lambda,\mu,X)\) constant for the regular octagon space*, Filomat 38 (2024), 1583--1593. DOI: 10.2298/FIL2405583Y.
