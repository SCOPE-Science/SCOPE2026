# A sharp two-price phase transition for mixed disk coverings on the triangular lattice

## Finding

Let \(\Lambda=\mathbb Z(1,0)+\mathbb Z(1/2,\sqrt3/2)\). Colour a lattice site \(m(1,0)+n(1/2,\sqrt3/2)\) as type A when \(m-n\equiv0\pmod3\), and as type B otherwise. Put a closed disk of radius \(r\ge0\) at every type-A site and one of radius \(s\ge0\) at every type-B site. The union covers the entire plane if and only if \(r\ge F(s)\), where the **complete sharp covering boundary** is

\[
F(s)=\begin{cases}
\sqrt{1-s+s^2},&0\le s\le\tfrac12,\\[2pt]
\tfrac12\bigl(\sqrt3-\sqrt{4s^2-1}\bigr),&\tfrac12\le s\le1,\\[2pt]
0,&s\ge1.
\end{cases}
\]

For a relative type-B quadratic price \(w>0\), the normalized expense of one A site and two B sites is \(J_w(r,s)=r^2+2ws^2\). Put \(c=1+2w\). Define the candidate pairs

\[
\begin{aligned}
s_1&=\frac1{2c},&r_1&=\sqrt{1-s_1+s_1^2},&E_1&=1-\frac1{4c},\\
s_2&=\frac12\sqrt{1+\frac3{c^2}},&r_2&=\frac{\sqrt3}{2}\left(1-\frac1c\right),&E_2&=\frac{c+2-3/c}{4}.
\end{aligned}
\]

Then the exact global minimum is \(\min\{E_1,E_2\}\). At the sharp critical relative price \(w_\ast=\sqrt3/2\), there are **exactly two** minimizing pairs, \((r_1,s_1)\) and \((r_2,s_2)\); for \(w>w_\ast\) the first is uniquely optimal, and for \(0<w<w_\ast\) the second is uniquely optimal. The optimal small-disk radius jumps discontinuously across \(w_\ast\), and the minimum cost has a downward jump of its first derivative, of magnitude \(\tfrac12+1/(1+\sqrt3)^2\). This is a genuine two-branch first-order design transition within a fixed periodic geometry.

## Assumptions and scope

The lattice's shortest separation is one. The two color classes and their populations are fixed (one A and two B per index-three period). Both radii are independently adjustable, and the only objective is a positive weighted sum of squared sensing radii. All disks are closed. The result optimizes the radii in **this particular three-colour triangular-lattice deployment**, not the positions, proportions, or covering structure of arbitrary disks in the plane. The zero-radius limiting cases are included only in the covering-profile statement; the price theorem assumes \(w>0\).

## Proof

**1. Reduction to a hexagonal cell.** The A sites form an index-three triangular sublattice with nearest spacing \(\sqrt3\). Its Voronoi region \(H\) about the origin is a regular hexagon of circumradius one. The six type-B sites at its vertices are \(v_j=(\cos(j\pi/3),\sin(j\pi/3))\), \(0\le j\le5\). Every other B site has norm at least two, hence its distance from a point of \(H\) is at least one. Conversely, partition \(H\) into the six equilateral triangles \(\operatorname{conv}\{0,v_j,v_{j+1}\}\): the squared distance from any point in one triangle to \(v_j\) is at most one, by convexity and the values at its three vertices. Thus the nearest B site to each point of \(H\) is among the six vertices. A disk of radius \(r\) at the origin covers exactly the part of \(H\) with \(|x|\le r\); all A cells are congruent. Therefore \(F(s)\) equals the largest radius of a point in \(H\) that is outside the six open B disks of radius \(s\) (with the obvious limiting interpretation when the uncovered set becomes empty).

**2. Disjoint B disks: \(0\le s\le1/2\).** Adjacent vertices are one unit apart, so the six disks of radius \(s\) have disjoint interiors. The norm has no interior local maximum away from the origin, hence a maximizer among the B-uncovered points occurs on an edge of \(H\) or a B-circle arc. On a hexagon edge parameterized from \(v_0\) to \(v_1\), the uncovered interval is \(x(t)=(1-t)v_0+tv_1\) with \(s\le t\le1-s\), and \(|x(t)|^2=1-t+t^2\le1-s+s^2\). On a radius-\(s\) arc about a vertex \(v_j\) lying inside the hexagon, the inward wedge condition gives \(v_j\cdot(x-v_j)\le-s/2\). Consequently \(|x|^2\le1-s+s^2\). Equality occurs at either side point whose distance from its adjacent vertex is \(s\). Therefore \(F(s)^2=1-s+s^2\).

**3. Overlapping B disks: \(1/2\le s\le1\).** Each point of a hexagon edge has distance at most \(1/2\) from a B vertex, so the B-uncovered part lies strictly inside \(H\), apart from tangencies at the endpoint. By sixfold symmetry use polar rays at angles \(0\le\theta\le\pi/6\) from \(v_0=(1,0)\). In this sector the nearest B vertex is \(v_0\). Along the ray the B exclusion inequality is

\[1+u^2-2u\cos\theta>s^2.\]

Since \(s\ge1/2\ge\sin\theta\), its inner crossing is \(u_-(\theta)=\cos\theta-\sqrt{s^2-\sin^2\theta}\). The ray's hexagonal endpoint lies in a B disk, and the origin does not for \(s<1\), so the uncovered segment is precisely \(0\le u<u_-(\theta)\). The derivative is

\[u_-'(\theta)=\sin\theta\left(\frac{\cos\theta}{\sqrt{s^2-\sin^2\theta}}-1\right)\ge0,\]

because \(s\le1\). Its maximum is at \(\theta=\pi/6\), giving \(F(s)=\sqrt3/2-\sqrt{4s^2-1}/2\). At \(s=1\) the B disks already cover all of \(H\); they do so for all larger radii. The two profile branches agree at \(s=1/2\).

**4. Global price minimization.** Since a positive coefficient multiplies \(r^2\), every optimum has \(r=F(s)\). It suffices to consider \(0\le s\le1\), since \(s\ge1\) costs at least \(2w\) and minimizes over that ray at \(s=1\), already part of the second branch. On the first branch,

\[J_w(F(s),s)=1-s+cs^2\]

has a unique minimum at \(s_1=1/(2c)\in(0,1/2)\), with value \(E_1\). On the second branch,

\[J_w(F(s),s)=\tfrac12+cs^2-\tfrac{\sqrt3}{2}\sqrt{4s^2-1}.\]

Its derivative is \(2s\bigl(c-\sqrt3/\sqrt{4s^2-1}\bigr)\), which changes sign from negative to positive exactly once, at \(s_2=\tfrac12\sqrt{1+3/c^2}\in(1/2,1)\). Substitution yields the stated \(r_2\) and \(E_2\). The only global candidates are the two strict minima, and

\[E_2-E_1=\frac{c-2-2/c}{4}.\]

This vanishes at the unique \(c>1\) satisfying \(c^2-2c-2=0\), namely \(c_\ast=1+\sqrt3\), or \(w_\ast=\sqrt3/2\). Its sign gives the claimed unique-optimum regimes and coexistence. On each branch the envelope derivative with respect to price is \(2s_i^2\), yielding the stated strictly positive slope drop \(2(s_2^2-s_1^2)=\tfrac12+1/c_\ast^2\). Both optimal pairs are distinct at coexistence. This completes all assertions.

## Verification

The accompanying self-contained Python script checks the exact cost formulas against independent direct minimization over ten thousand radii, compares all six adjacent B vertices against a larger lattice patch at forty thousand uniformly sampled points of the central hexagon, tests random covering points for twelve radii, and verifies boundary witness points. It prints `TWO_RADIUS_TRIANGULAR_WEIGHTED_COVERING_OK` on success. The proof above, rather than any finite sampling or grid, establishes coverage for every plane point and optimizes over every nonnegative radius.

## Relationship to prior work

Abbas and Koutsoukos studied deterministic complete coverings with two sensor radii in 2014 (journal issue 2015), including this classical three-class triangular deployment under **equal unit price**. At \(w=1\) the present first branch gives their known benchmark: small radius \(1/6\), large radius \(\sqrt{31}/6\), and normalized expense \(11/12\). That numerical benchmark is not claimed as original. The work here supplies the complete geometric feasibility boundary (including overlapping B disks), optimization for **every** positive relative price, and the new coexistence/first-order transition. General planar disk-covering theorems and stochastic heterogeneous-sensor models do not imply this branch-resolved price transition without a fixed deployment analysis.

## Limitations

The theorem does not compare arbitrary positions of heterogeneous sensors, other site proportions, arbitrary heterogeneous radii at individual sites, nonlinear power models, or finite boundary effects. A previously unindexed analysis of this particular weighted model could affect historical priority; the statement is not independently audited. The numerical checker is a diagnostic, not an infinite proof.

## References

1. W. Abbas and X. Koutsoukos, *Efficient Complete Coverage Through Heterogeneous Sensing Nodes*, IEEE Wireless Communications Letters 4 (2015), 14–17. First online 2014. DOI: 10.1109/LWC.2014.2358631.
2. R. Kershner, *The number of circles covering a set*, American Journal of Mathematics 61 (1939), 665–671. Classical homogeneous covering background.
3. B. Wang, *Coverage Problems in Sensor Networks: A Survey*, ACM Computing Surveys 43 (2011), article 32, DOI: 10.1145/1978802.1978811. Application context.
