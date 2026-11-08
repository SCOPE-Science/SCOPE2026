# Global finite-time seven-cycle capture outside a one-dimensional exceptional set

## Finding

Let \(b\le -2\) and consider the continuous piecewise-affine map
\[
F_b(x,y)=(|x|-y-1,\ x-|y|+b).
\]
Let \(\mathcal P_b\) and \(\mathcal Q_b\) be the respective primitive attracting and repelling seven-point orbits given explicitly below, and \(p_b=(-b,-1)\). The source's established global graph-capture and graph-dynamics results imply, for **every** \(b\le-2\), the exact identity
\[
\boxed{\mathbb R^2\setminus\bigcup_{n\ge0}F_b^{-n}(\mathcal P_b)
=\{p_b\}\cup\bigcup_{n\ge0}F_b^{-n}(\mathcal Q_b).}
\]
In addition, **if \(b\) is irrational or rational with reduced denominator not divisible by \(15\)**, then the set on the right has planar Lebesgue measure zero, is meager, and has Hausdorff dimension **exactly one**. In particular, for every such \(b\), planar Lebesgue-almost every initial point and a dense residual set of initial points reach the attracting period-seven orbit in finite time. No claim is made here for the planar measure or dimension of the exceptional set at rational parameters whose reduced denominator is divisible by \(15\).

## Assumptions and scope

The parameter \(b\) is any real number at most \(-2\). For rational \(b=p/q\) the denominator \(q>0\) is understood to be reduced. The original work of Cima, Gasull, Mañosa and Mañosas (Proposition 25) establishes the two distinct seven-orbits
\[
\begin{aligned}
\mathcal P_b=\{&(-b-2,-1),(-b-2,-3),(-b,-5),(-b+4,-5),\\
&(-b+8,-1),(-b+8,7),(-b,1)\},\\
\mathcal Q_b=\{&(-b-16/15,-1/15),(-b-2,-17/15),(-b-28/15,-47/15),\\
&(-b+4/15,-5),(-b+64/15,-71/15),(-b+8,-7/15),\\
&(-b+112/15,113/15)\}.
\end{aligned}
\]
The ordered orbit points above are the exact source coordinates; their discovery and the finite-time capture result **on the invariant graph** are not claimed here as new. Define \(E_b\) as the set of points whose forward orbits never enter \(\mathcal P_b\). All preimages are taken in the whole plane, rather than inside the invariant graph.

## Proof

**1. Complete noncaptured-set identity (all \(b\le-2\)).** Proposition 17 of the cited primary work implies that any point except the fixed point \(p_b\) eventually visits the union of the first and third closed quadrants. Proposition 18(b) then sends every such point into the compact invariant polygonal graph in at most eleven additional iterates. Proposition 25(b) proves that every point on that graph outside \(\mathcal Q_b\) reaches \(\mathcal P_b\) in finitely many further iterates, and that \(\mathcal Q_b\) is a periodic orbit disjoint from \(\mathcal P_b\). Thus every noncaptured initial condition either equals \(p_b\) or eventually enters \(\mathcal Q_b\). Conversely, periodicity of \(p_b\) and \(\mathcal Q_b\) and disjointness from \(\mathcal P_b\) show that all listed points are noncaptured. Hence the equality, with no parameter arithmetic restriction.

**2. Arithmetic obstruction to a constant branch reaching \(\mathcal Q_b\).** Set \(\Lambda_b=\mathbb Z+b\mathbb Z\), an additive subgroup of \(\mathbb R\). The four linear parts of the map, on coordinate-sign quadrants, have integer entries, and their common translation is \((-1,b)\in\Lambda_b^2\). Thus every finite itinerary of length \(n\) has an affine representation
\[
F_b^n(z)=M_\omega z+w_\omega,\qquad
M_\omega\in\mathbb Z^{2\times2},\quad w_\omega\in\Lambda_b^2,
\]
on a (possibly empty) polygonal sign-itinerary cell. If \(M_\omega=0\), its constant image is in \(\Lambda_b^2\).

Each point of \(\mathcal Q_b\) has **at least one coordinate** of the form \(r/15\) or \(-b+r/15\), with \(r\) an integer not divisible by \(15\). Indeed, six points have their listed second coordinates equal to \(-1/15,-17/15,-47/15,-71/15,-7/15,113/15\); the remaining point has first coordinate \(-b+4/15\). If \(b\) is irrational, no such coordinate belongs to \(\Lambda_b\): equality with \(m+kb\) would force \(k=0\) (or \(k=-1\)) and then force \(r/15\) to be an integer. If \(b=p/q\) is reduced and \(15\nmid q\), then \(\Lambda_b=q^{-1}\mathbb Z\); equality of \(r/15\) or \(-b+r/15\) with an element of this group requires \(15\mid q\), impossible. Therefore
\[
\mathcal Q_b\cap\Lambda_b^2=\varnothing
\]
for every parameter in the stated arithmetic range, and no constant branch of any iterate can land on \(\mathcal Q_b\).

**3. Measure, category, and upper dimension.** Fix \(n\ge0\). On each of finitely many two-dimensional sign-itinerary cells, the equation \(F_b^n(z)=q\) with \(q\in\mathcal Q_b\) becomes \(M_\omega z=q-w_\omega\). By step 2, the rank-zero case has no solution. If the rank is one, the solutions lie on an affine line; if the rank is two, there is at most one point. The itinerary boundaries are subsets of finitely many affine lines, because all branch inequalities are affine. Hence \(F_b^{-n}(\mathcal Q_b)\) is contained in a finite union of lines and isolated points. It has planar measure zero, Hausdorff dimension at most one, and empty interior. It is also closed, since \(F_b\) is continuous and \(\mathcal Q_b\) finite; consequently it is nowhere dense. Taking the countable union in step 1 and adding \(\{p_b\}\) proves that \(E_b\) is null, meager, and of Hausdorff dimension at most one. Its complement is residual and has full planar Lebesgue measure.

**4. Matching lower dimension.** For every \(t>0\), the point \((t-b-1/15,t)\) lies in the strictly positive quadrant. Its image is
\[
F_b(t-b-1/15,t)=(-b-16/15,-1/15)\in\mathcal Q_b.
\]
Thus a whole nondegenerate half-line belongs to \(E_b\). This proves \(\dim_H E_b\ge1\), and step 3 yields equality. The half-line is a genuine two-dimensional-phase-space preimage, not an edge of the published compact invariant graph.

## Verification

The supplied standalone `check.py` uses exact rational arithmetic and symbolic affine expressions \(u+vb\) to verify both ordered seven-cycle identities uniformly for all \(b\le-2\), the unique listed fixed point, the collapsing half-line, and the denominator obstruction for every repelling-orbit point. It additionally evaluates a finite exact-rational grid at five parameters to check consistency with finite-time capture. The checker prints `SYMBOLIC_SEVEN_CYCLE_AND_ARITHMETIC_CHECK_OK`. The universal full-plane conclusion follows from the four analytical steps, not from finite sampling. The cited paper is the source of the global graph-capture and graph-dynamics premises; these premises are not re-proved by the checker.

## Relationship to prior work

Cima–Gasull–Mañosa–Mañosas, arXiv:2410.01052, Propositions 17, 18 and 25, establish the polygonal graph, explicit periodic orbits and its finite-time dynamics. Their Section 6 distinguishes graphwise results from a full-plane Lebesgue-measure assertion and identifies the latter type of question for further study. Their follow-up arXiv:2503.02411, Theorem 3 and Proposition 10, proves full-measure statements **on graphs** for certain parameters, including this regime, but expressly leaves planar-basin geometry aside. The present contribution is the global **planar** exceptional-set formula together with a new arithmetic rank obstruction and its sharp Hausdorff dimension, for all parameters in the stated uncountable arithmetic range. The source's original orbit coordinates and graphwise statements are not claimed as original.

## Limitations

The proof does not determine planar exceptional-set size for reduced rational parameters with denominator divisible by \(15\), where constant branches could potentially land on the repelling orbit. It provides neither a uniform bound on finite capture time nor a closed-form classification of each individual preimage component. The argument relies on the published Propositions 17, 18 and 25 rather than reproducing their global itinerary classification. The current originality assessment is literature-dependent; equivalent work in unindexed sources remains possible. No independent audit is asserted.

## References

1. A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Invariant graphs and dynamics of a family of continuous piecewise linear planar maps*, arXiv:2410.01052, first submitted 2024-10-01; *Qualitative Theory of Dynamical Systems* **24** (2025), article 70, doi:10.1007/s12346-025-01221-1. Propositions 17, 18, 25; Section 6. https://arxiv.org/abs/2410.01052 ; https://link.springer.com/article/10.1007/s12346-025-01221-1
2. A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Entropy and omega-limit sets on invariant graphs for a class of planar piecewise linear maps*, arXiv:2503.02411 (2025; version inspected dated 2026-07-30), Theorem 3 and Proposition 10. https://arxiv.org/abs/2503.02411
