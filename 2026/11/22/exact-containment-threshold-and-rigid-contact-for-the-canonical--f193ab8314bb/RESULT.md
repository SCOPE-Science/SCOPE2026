# Exact containment threshold and rigid contact for the canonical unit Z-arc in Wetzel chord trims

## Finding

Let \(\Pi\) be the circular sector of radius one and opening angle \(30^\circ\), with vertex at the origin and lower radius on the positive horizontal axis. For \(0<t<30^\circ\), let \(H_t\) be its intersection with the half-plane through the radius-one points at polar angles \(t\) and \(30^\circ\) that contains the origin. Thus the circular arc from \(t\) to \(30^\circ\) is replaced by its chord. Consider the unit-length polygonal arc \(\mathcal Z\) with consecutive vertices
\[
Z_0=(0,0),\quad Z_1=(1/12,0),\quad Z_2=(1/2,5\sqrt3/12),\quad Z_3=(7/12,5\sqrt3/12).
\]
The three edge lengths sum to one. Reflected copies are allowed.

**Theorem.** There is a sharp threshold
\[
t_{\mathcal Z}=30^\circ-2\arctan\!\left(\frac{24\sqrt{37}-131}{37\sqrt3}\right)
=3.6761221929409723759\ldots^\circ,
\]
where \(\arctan\) denotes the degree-valued inverse tangent, such that \(H_t\) contains a congruent copy of \(\mathcal Z\) **if and only if** \(t\ge t_{\mathcal Z}\). At \(t=t_{\mathcal Z}\), the embedded arc is unique as a geometric (unparametrized) subset, up to reversal of its traversal direction.

The underlying support functional has a stronger exact transition formula. For every \(t\in[3.6^\circ,3.7^\circ]\), let \(M(t)\) denote the minimum over all rotations and reflections of the sum-of-three-supports necessary condition in Lemma 6.5 of Panraksa--Wichiramala, minus the available chord support. Then
\[
M(t)=\rho\sin\!\left(\frac{t_{\mathcal Z}-t}{2}\right),\qquad
\rho=\sqrt{\left(1-\frac{131}{24\sqrt{37}}\right)^2+\frac{111}{576}},
\]
where the sine argument is converted to radians. Consequently the obstruction is strictly positive before, exactly zero at, and negative after the critical angle.

In particular, the universal unit-arc covering threshold of the chord trims is **at least** \(t_{\mathcal Z}\), sharpening the prior explicit \(3.6^\circ\) obstruction. This is a statement about the canonical test arc, **not** a determination of the universal-cover threshold.

## Assumptions and scope

The sector, trims, and Z-arc are the objects defined above; the only admissible placements are Euclidean isometries, including reflections. The source establishes the nesting \(H_{t_1}\subseteq H_{t_2}\) for \(t_1<t_2\), together with absence of the test arc for all \(t\le3.6^\circ\) and an explicit reflected placement for \(t\ge3.7^\circ\). The present result determines the exact interval missing from those two bounds.

Write \(p_\phi=(\cos\phi,\sin\phi)\), \(s=(t+30^\circ)/2\), and \(d=(30^\circ-t)/2=30^\circ-s\). In angular differentiation all angles are measured in radians, while numerical degree values denote corresponding fixed angles. Set \(\beta\in(0,90^\circ)\) by \(\cos\beta=6/\sqrt{111}\) and \(\sin\beta=5\sqrt3/\sqrt{111}\).

## Proof

**1. Support inequality and finite orientation reduction.** By Lemma 6.5 in the source, any copy contained in \(H_t\) must satisfy
\[
G_s^\pm(\theta)\le\cos d,\qquad
G_s^\pm(\theta)=\frac{f_s(\theta)+\sqrt{111}\,f_s(\theta\pm\beta)}{12},
\]
with
\[
f_s(\phi)=\sin(120^\circ-s)|\sin\phi|+\cos s\,|\cos(\phi-120^\circ)|+\tfrac12|\cos(\phi-s)|.
\]
The plus sign represents a direct placement and the minus sign a reflected placement. The derivation combines three half-plane support inequalities with strictly positive coefficients and cancels translation. The source also establishes that for each sign the function is concave on every angular interval between the six breakpoints
\[
0,\ 30^\circ,\ 90^\circ+s,\ \mp\beta,\ 30^\circ\mp\beta,\ 90^\circ+s\mp\beta\pmod {180^\circ}.
\]
Indeed, on each open breakpoint interval \((G_s^\pm)''=-G_s^\pm<0\), so a minimum can occur only at the indicated breakpoints and cannot occur strictly inside any interval.

**2. One strictly dominant orientation across the unresolved interval.** At \(s_0=16.8^\circ\), evaluate the twelve breakpoint values, six for each sign. The unique smallest is the reflected breakpoint \(\theta=\beta\):
\[
G_{s_0}^-(\beta)=0.973878384482908855\ldots.
\]
The next-smallest breakpoint (the direct \(\theta=30^\circ-\beta\)) exceeds it by \(0.012047763931534189\ldots\). The enclosed-interval checker `critical_zarc.py` proves the sharper rational assertion that **all other eleven** breakpoint values exceed it by more than \(1/100\), without assuming numerical rounding accuracy.

For a moving breakpoint \(\phi(s)=c+s\) or a fixed breakpoint, the derivative of each absolute-sine or absolute-cosine term (where it exists) has modulus at most the speed of its angle argument. Thus \(f_s(\phi(s))\) is \(4\)-Lipschitz in \(s\) in radians. Since \((1+\sqrt{111})/12<1\), each breakpoint value of \(G\) is also \(4\)-Lipschitz. The difference between any two breakpoint values can therefore decrease by at most \(8|s-s_0|\). Over \(s\in[16.8^\circ,16.85^\circ]\), this is bounded by \(8\pi/3600=\pi/450<1/100\). Hence throughout \(3.6^\circ\le t\le3.7^\circ\), the **unique global minimizing placement orientation** is reflected with \(\theta=\beta\pmod{180^\circ}\).

**3. Closed form and the threshold.** The reflected placement constructed in Example 6.4 of the source has vertices \(Q_0,Q_2,Q_1,Q_3\), with
\[
Q_0=(3/(4\sqrt{111}),0),\quad Q_1=(10/\sqrt{111},0),\quad
Q_2=(5/(4\sqrt{111}),5\sqrt3/(12\sqrt{111})),
\]
\[
Q_3=(21/(2\sqrt{111}),5\sqrt3/(12\sqrt{111})).
\]
Its two side-support constraints at angles \(270^\circ\) and \(120^\circ\) are tight. Substitution into the support expression gives the **identity**
\[
\min_{\theta,\pm}G_s^\pm(\theta)
=G_s^-(\beta)=\langle Q_3,p_s\rangle
= A\cos d+B\sin d,
\]
where
\[
A=\frac{131}{24\sqrt{37}},\qquad B=\frac{\sqrt{111}}{24}.
\]
Thus the exact optimal support gap is
\[
M(t)=B\sin d-(1-A)\cos d
=\sqrt{B^2+(1-A)^2}\,\sin(d-d_*),
\]
where \(d_*:=\arctan((1-A)/B)\), i.e. \(\tan d_*=(24\sqrt{37}-131)/(37\sqrt3)\). Since \(0<d_*<15^\circ\), the gap changes sign exactly at \(t_{\mathcal Z}=30^\circ-2d_*\).

**4. Necessity, sufficiency, and uniqueness.** For \(t<t_{\mathcal Z}\) but \(t\ge3.6^\circ\), we have \(M(t)>0\), contradicting the necessary support inequality. For \(t\le3.6^\circ\), noncontainment follows from Proposition 6.6 of the cited source. Conversely, at \(t=t_{\mathcal Z}\), the explicit reflected \(Q\)-placement satisfies \(\langle Q_3,p_s\rangle=\cos d\); its three other vertices satisfy the chord inequality strictly, and all four lie in the radius-one sector (in particular \(|Q_3|^2=5317/5328<1\)). It is therefore contained in \(H_{t_{\mathcal Z}}\). Nesting yields containment at every larger \(t\).

At the critical angle, any placement must attain equality in the support bound. Strict angular minimality forces the reflected orientation \(\theta=\beta\pmod{180^\circ}\). Since the three positive multipliers in the source's support cancellation sum three nonpositive slacks to zero, each half-plane slack must vanish. Contacts on the two radial boundary lines determine the translation uniquely. This recovers precisely the listed \(Q\)-placement, with orientation modulo \(180^\circ\) corresponding to reversal of the same traced arc. Hence the threshold copy is unique.

## Verification

The supplied `critical_zarc.py` computes all eleven strict breakpoint gaps using 65-decimal-place enclosing interval arithmetic (`mpmath.iv`), checks that each gap at \(s_0\) exceeds \(1/100\), verifies \(\pi/450<1/100\), and independently verifies \(G_s^-(\beta)=\langle Q_3,p_s\rangle\) at both endpoints. It also prints the critical-angle value. The analytical proof handles the continuum of angles; no finite sampling or numerical optimizer is used as an infinite proof.

## Relationship to prior work

Panraksa and Wichiramala, *A One-Sided Chord Trim of Wetzel's Sector Covers Unit Arcs*, first publicly posted 12 November 2026, Theorem 1.1 and Section 6, prove that \(H_{15^\circ}\) covers every unit arc and that the particular Z-arc is absent for \(t\le3.6^\circ\) but present for \(t\ge3.7^\circ\). Their Lemma 6.5 furnishes the weighted-support inequality, Example 6.4 furnishes the critical candidate placement, and Table 4 evaluates the twelve orientations at \(t=3.6^\circ\). The new contribution is to prove uniform angular dominance on the **entire unresolved interval**, derive an exact algebraic-trigonometric cutoff, and establish uniqueness of the contact configuration at equality. The paper does not claim this exact threshold, but the present argument builds transparently on its essential lemmas and coordinates. No priority claim beyond the particular sharpened result is made.

## Limitations

The threshold pertains only to one explicitly defined unit Z-arc. It gives a lower bound for the global covering threshold and does not determine whether \(H_t\) covers every unit arc for any \(t<15^\circ\). The original lower bound \(3.6^\circ\) is sharpened by about \(0.07612^\circ\), not by an order-of-magnitude change. The numerical interval certificate uses the documented interval backend; the finite strict comparisons can also be checked using elementary Taylor bounds. Independent mathematical validation and exhaustive historical priority verification have not been performed.

## References

1. C. Panraksa and W. Wichiramala, *A One-Sided Chord Trim of Wetzel's Sector Covers Unit Arcs*, arXiv:2611.16204v1 (12 November 2026), https://arxiv.org/html/2611.16204v1, especially Lemma 6.5, Proposition 6.6, Example 6.4, Table 4.
2. Movshovich, work on unit Z-arcs (bibliographic reference [11] of Panraksa--Wichiramala). Only the attribution and geometrical setup from the inspected primary paper are used here.
