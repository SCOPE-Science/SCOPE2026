# Attracting three-cycle chirality at the two-saddle border-collision boundary

## Finding

Consider the continuous planar border-collision normal form
\[
F(x,y)=\begin{cases}
(ax+y+1,-bx),&x<0,\\
(-cx+y+1,-dx),&x>0.
\end{cases}
\]
Its four parameters are real, with \(a>|1+b|\) and \(c>|1+d|\). These are precisely the strict two-saddle hypotheses: the left affine branch has one multiplier greater than \(1\), and the right affine branch has one multiplier less than \(-1\); each also has a multiplier of modulus less than \(1\).

Define the following polynomials in the four parameters:
\[
\begin{aligned}
T&=-a^2c-ab-ad+bc, &D&=b^2d,\\
S&=1-T+D, &P&=1+T+D, &Q&=1-D,\\
N_0&=ac-ad-bd+b+c-1,\\
N_1&=ac-a+bc-bd+d-1,\\
N_2&=a^2+ab+a+b^2-b+1.
\end{aligned}
\]

**Exact three-cycle classification.** There exists a strictly branch-admissible, hyperbolically attracting prime-period-three orbit if and only if the five simultaneous strict inequalities
\[
\boxed{S>0,\quad P>0,\quad Q>0,\quad N_0>0,\quad N_1>0}
\]
hold. If it exists, it is unique up to cyclic reindexing, has itinerary \(LLR\), and its successive first coordinates are
\[
\boxed{(x_0,x_1,x_2)=(-N_0/S,-N_1/S,N_2/S).}
\]
The other coordinates are \((y_0,y_1,y_2)=(-d x_2,-b x_0,-b x_1)\). No strictly admissible hyperbolically attracting prime-three orbit with itinerary \(LRR\) exists anywhere in the stated two-saddle domain.

**An explicit two-saddle sink region near the saddle-multiplier edges.** Write
\[
\rho=\frac{\sqrt5-1}{2}.
\]
For every \(0<b<\rho\) and every
\[
\boxed{-\frac1{b^2}<d<-1-\frac1b,}
\]
there are arbitrarily small positive \(u,v\) for which \(a=1+b+u\) and \(c=-1-d+v\) satisfy the two-saddle hypotheses and the five strict inequalities. Hence an open four-parameter region has two saddle fixed points and an attracting three-cycle; the two-saddle property alone does not force exclusively chaotic attracting behavior. The displayed interval for \(d\) is nonempty **if and only if** \(0<b<\rho\); this sharp golden-ratio statement concerns this explicitly constructed saddle-edge strip, **not** all possible parameter regimes admitting such an orbit.

For a separate exact, easily inspected witness, take
\[
(a,b,c,d)=\left(\frac43,\frac14,4,-\frac92\right).
\]
The attracting orbit is
\[
\begin{aligned}
(-4524/335,5517/335)&\longmapsto(-36/67,1131/335)\\
&\longmapsto(1226/335,9/67)\\
&\longmapsto(-4524/335,5517/335).
\end{aligned}
\]
All three points lie strictly inside their indicated half-planes.

## Assumptions and scope

A strict itinerary means that no orbit point lies on the switching line. Hyperbolic attraction means both eigenvalues of the three-step Jacobian have modulus strictly less than one. Statements concern the autonomous map with constant positive forcing normalized to \(1\); switching-line orbits, neutral multipliers, other periods, global attraction, and coexistence with chaotic sets are not classified. The chosen first point of \(LLR\) is in the left half-plane.

## Proof

Put
\[
L=\begin{pmatrix}a&1\\-b&0\end{pmatrix},\qquad
R=\begin{pmatrix}-c&1\\-d&0\end{pmatrix},\qquad e=\binom10.
\]
For a prospective \(LLR\) cycle the first point solves \(z_0=RL^2z_0+(RL e+R e+e)\). Direct matrix multiplication gives \(\operatorname{tr}(RL^2)=T\), \(\det(RL^2)=D\), and \(\det(I-RL^2)=S\). When \(S\ne0\), solving this affine equation and applying the branch maps yields the three first coordinates given above. The second coordinates follow from the preceding branch's formula.

The third first-coordinate numerator is strictly positive for every real \(b\) and every \(a>0\), since
\[
N_2=\left(b+\frac{a-1}{2}\right)^2+\frac{3(a+1)^2}{4}>0.
\]
For a real two-by-two matrix with trace \(T\) and determinant \(D\), the strict Schur/Jury criterion is exactly \(1-T+D>0\), \(1+T+D>0\), \(1-D>0\). The five displayed inequalities are therefore sufficient for the affine solution to be strictly \(LLR\)-admissible and hyperbolically attracting. Conversely, every such attracting \(LLR\) orbit satisfies them. Strict admissibility makes the period exactly three, because its itinerary contains both letters.

For a putative attracting \(LRR\) orbit the monodromy is \(R^2L\). Direct elimination gives the first coordinate of its left-labelled point as
\[
x_0=\frac{K}{\det(I-R^2L)},\qquad
K=c^2-cd-c+d^2-d+1
=\left(d-\frac{c+1}{2}\right)^2+\frac{3(c-1)^2}{4}.
\]
The two-saddle inequality \(c>|1+d|\) excludes the only zero of \(K\), so \(K>0\). Attraction would require \(\det(I-R^2L)>0\) by the same Schur criterion and thus \(x_0>0\), a contradiction to the required left branch. Every mixed prime-three word is cyclically \(LLR\) or \(LRR\). A word with three identical letters cannot be a prime-three attractor because the corresponding single affine matrix is hyperbolic saddle-type and its third iterate has only its fixed point. Uniqueness follows from uniqueness of the affine fixed point for the surviving itinerary.

For the saddle-edge construction take \(0<b<\rho\) and \(-1/b^2<d<-1-1/b\). At the limiting parameter pair \(a=1+b\), \(c=-1-d\), all the following are strict:
\[
1+b^2d>0,\qquad -3(b+1)(d+1)>0,\qquad -3[b(d+1)+1]>0.
\]
Now hold \(a=1+b\) and set \(c=-1-d+v\), \(v>0\). Direct substitution produces
\[
\begin{aligned}
S&=(1+b+b^2)v,\\
P&=2(1+b^2d)-(1+b+b^2)v,\\
N_0&=-3(b+1)(d+1)+(b+2)v,\\
N_1&=-3[b(d+1)+1]+(2b+1)v,\\
Q&=1-b^2d.
\end{aligned}
\]
All five are positive for sufficiently small \(v>0\). Continuity permits a further arbitrarily small perturbation \(a=1+b+u\), \(u>0\), preserving all five signs and making both fixed points strict saddles. The admissible interval for \(d\) is nonempty precisely when \(b^2+b<1\), i.e. \(b<\rho\).

At the rational witness, the three-step Jacobian is
\[
RL^2=\begin{pmatrix}-58/9&-67/12\\55/8&6\end{pmatrix},
\]
with \(S=335/288\), \(P=79/288\), and \(Q=41/32\). The given orbit is a direct exact solution with negative, negative, positive first coordinates. This finishes the proof.

## Verification

Run `python VERIFY.py` using Python 3 and its standard library. The attached checker tests matrix/itinerary elimination over a rational grid, checks exact return and the two-saddle eigenvalue inequalities at the displayed witness, and verifies a rational point in the constructed saddle-edge strip. It reports \(`PASS 1056 exact-rational assertions`\). These finite tests support, but do not replace, the universal algebraic argument above.

## Relationship to prior work

Ghosh, McLachlan and Simpson (2024, arXiv:2402.05393, originally posted February 8, 2024) analyze the same two-saddle normal form, define the region used here, and describe stable low-period windows as a complication of chaotic-attractor classifications. Their text does not state this exact period-three semi-algebraic classification or the saddle-edge strip. Fatoyinbo and Simpson (2022, arXiv:2210.14445) analyze non-invertible parameters in both forcing signs, report an attracting \(LLR\) example outside the two-saddle region, and give general trace/determinant stability tests and period-three tongues. The existence of some attracting \(LLR\) orbits, the Schur test, the matrix word method, and the general theory of resonance tongues are therefore prior knowledge, not new claims.

The present assertion is the exact **two-saddle** \(LLR\)-versus-\(LRR\) classification, its positive-square obstruction, and a constructive saddle-edge parameter strip with an explicit sharp intersection threshold. A published four-cycle obstruction for the same non-invertible two-saddle family concerns \(LLLR\) rather than prime-period-three itineraries and neither implies nor contradicts this result. The earlier Ghosh–McLachlan–Simpson (2023) theorem establishes chaotic attractors within subsets of the two-saddle region, without a complete attracting three-cycle classification. The general itinerary methods of Simpson (2016) are essential background. Publication-priority uncertainty remains because the full text of that general review was not independently available for line-by-line comparison.

## Limitations

The interval \(-1/b^2<d<-1-1/b\) is a sufficient construction strip; no necessity is claimed for all parameter values. The exact five-inequality test is necessary and sufficient only within the stated two-saddle domain, for strict hyperbolically attracting prime-three cycles. The existence of other invariant sets or global basins is not addressed. The publication-priority comparison cannot exclude unpublished, unindexed, or inaccessible equivalent calculations. No independent audit has been performed.

## References

- I. Ghosh, R. I. McLachlan, and D. J. W. Simpson, *The bifurcation structure within robust chaos for two-dimensional piecewise-linear maps*, arXiv:2402.05393 (first posted 2024-02-08), https://arxiv.org/abs/2402.05393.
- H. O. Fatoyinbo and D. J. W. Simpson, *A synopsis of the non-invertible, two-dimensional, border-collision normal form with applications to power converters*, arXiv:2210.14445 (first posted 2022-10-26), https://arxiv.org/abs/2210.14445.
- I. Ghosh, R. I. McLachlan, and D. J. W. Simpson, *Robust chaos in orientation-reversing and non-invertible two-dimensional piecewise-linear maps*, arXiv:2307.05144 (first posted 2023-07-11), https://arxiv.org/abs/2307.05144.
- D. J. W. Simpson, *Border-Collision Bifurcations in* \(\mathbb R^N\), *SIAM Review* 58 (2016), 177–226, https://doi.org/10.1137/15M1006982 (general periodic-itinerary methods; full text not inspected).
- *No attracting three-left one-right four-cycle in the non-invertible two-saddle border-collision map*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-no-attracting-three-left-one-right-four-cycle-in-the-non-inverti--829828b41a37 (different word length).
