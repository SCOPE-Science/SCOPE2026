# Sharp nine-equilibrium window and complete stationary-point census for an invariant-cubic flow

## Finding
For the planar cubic vector field below, the exact number of distinct real equilibria is determined for **every real parameter** \(h\). There is an open, sharp interval on which all nine complex Bézout intersections are real, distinct and hyperbolic. Throughout that interval the phase portrait has exactly **five saddles, two sources and two sinks**. The underlying no-periodic-orbit statement is an existing result and is not claimed here.

Put
\[
\begin{aligned}
I_1&=(-7/120,1/6),\\
I_2&=(1/6-8\sqrt3/45,\;1/6+8\sqrt3/45),\\
I_3&=(19/6-13\sqrt{13}/15,\;19/6+13\sqrt{13}/15).
\end{aligned}
\]
For each \(i\), define \(r_i(h)=3\) inside \(I_i\), \(r_i(h)=2\) at either endpoint, and \(r_i(h)=1\) otherwise. The exact count is
\[
N(h)=r_1(h)+r_2(h)+r_3(h)-2\mathbf1_{\{h=1/6\}}.
\]
In particular, writing \(h_*=19/6-13\sqrt{13}/15\),
\[
N(h)=9\quad\Longleftrightarrow\quad h_*<h<1/6.
\]
The interval is nonempty, with \(h_*\approx0.04185556126454\). There are eight distinct real equilibria at \(h=h_*\), six at \(h=1/6\), and seven immediately above \(1/6\).

## Assumptions and scope
The parameter \(h\) is **any real number**, and the vector field is exactly
\[
\begin{aligned}
\dot x=P_h(x,y)&=-2h-y+x^2-4xy-y^2-\frac23x^3-3x^2y-5xy^2+\frac73y^3,\\
\dot y=Q_h(x,y)&=-h+x+\frac12x^2+3xy+2y^2-\frac43x^3-3x^2y+3xy^2+\frac{25}{6}y^3.
\end{aligned}
\]
An equilibrium means a point in \(\mathbb R^2\) satisfying \(P_h=Q_h=0\), counted only once even at an intersection of multiple lines. A saddle means the real Jacobian has negative determinant; a source or sink has positive determinant and respectively positive or negative trace. These last labels are asserted only in the open nine-equilibrium window, where the stated hyperbolicity is established.

## Proof
**Algebraic reduction.** Direct expansion gives the exact identity
\[
P_h-2Q_h=(2x+y)(x-2y-1)(x+3y+1).
\]
Hence every equilibrium belongs to at least one of the three lines. Their parameterizations by \(y\) are \(x=-y/2\), \(x=2y+1\), and \(x=-3y-1\). Substitution in \(Q_h=0\) gives, respectively,
\[
\begin{aligned}
q_1(y,h)&=(50y^3+15y^2-12y-24h)/24,\\
q_2(y,h)&=-(75y^3+90y^2+24y+6h-1)/6,\\
q_3(y,h)&=(25y^3+75y^2+36y+5-6h)/6.
\end{aligned}
\]
Conversely, any real root of one of these cubics, substituted into its line, satisfies both stationary equations, because \(P_h-2Q_h=0\) there.

**Root census.** Exact cubic discriminants are
\[
\begin{aligned}
\Delta_1(h)&=-\frac{125}{768}(6h-1)(120h+7),\\
\Delta_2(h)&=-\frac{25}{16}(2700h^2-900h-181),\\
\Delta_3(h)&=-\frac{25}{16}(300h^2-1900h+79).
\end{aligned}
\]
Each cubic has a nonzero leading coefficient independent of \(h\). Thus it has three, two, or one distinct real roots according as its discriminant is positive, zero, or negative. Factoring the displayed discriminants yields exactly the intervals \(I_i\). No complex-root multiplicities or points at infinity are counted in this real statement.

**Intersection correction.** The three distinct lines meet at the same point \((1/5,-2/5)\), and nowhere else pairwise. Substitution gives \(P_h=Q_h=0\) at that point **only if** \(h=1/6\). At this parameter the common point is represented three times by the three line cubics, so two duplicates must be subtracted; at all other parameters all roots from distinct lines are distinct. This proves the stated formula for \(N(h)\) with its endpoint cases.

**Sharp nine-point window.** The lower endpoints satisfy
\[
1/6-8\sqrt3/45<-7/120<19/6-13\sqrt{13}/15<1/6.
\]
The two remaining upper endpoints of \(I_2,I_3\) exceed \(1/6\). Hence all three discriminants are positive exactly when \(h_*<h<1/6\). There are then nine distinct real solutions and no line intersections, establishing both directions of sharpness.

**Hyperbolic types.** The Jacobian trace on the three lines, in order, is
\[
\frac{5y(5y-2)}4,\qquad -\frac{5y(5y+4)}2,\qquad -\frac{5(15y^2+18y+4)}2,
\]
while its determinant there is
\[
-\frac{(5y-1)(5y+2)^3}{8},\qquad
-\frac{(5y+2)^2(75y^2+60y+8)}2,\qquad
\frac{(5y+2)^2(25y^2+50y+12)}2.
\]
Their zeros along equilibrium branches in the open nine-point interval are excluded as follows: for the first line, the determinant zeros occur at \(y=1/5,-2/5\), which meet that line's cubic only at \(h=-7/120,1/6\), respectively. For the second and third lines the determinant zeros correspond to the discriminant endpoints of the respective cubics or to the concurrent point at \(h=1/6\). Thus all nine equilibria are hyperbolic throughout the connected interval. The signs of the trace at all positive-determinant equilibria do not vanish within this interval: on the first and second line this follows by substituting the finitely many trace zeros into \(q_i\); on the third line, the positive-determinant regions have strictly negative trace. The types therefore cannot change within the window. At the rational sample \(h=1/10\), exact rational root isolation of the three cubics and the stated determinant/trace polynomials yields on the first line one source and two saddles, on the second line one source and two saddles, and on the third line two sinks and one saddle. By connectedness, the classification is uniformly five saddles, two sources and two sinks. No numerical plot is used for a general proof.

## Verification
The independent *computational route* in the included `checker.py` uses exact symbolic expansion for the line factorization, three line-restricted cubic identities, three discriminants, and six Jacobian trace/determinant formulas. Exact rational polynomial-root isolation checks the counts at nine representative parameter values, and exact-rational sign isolation at \(h=1/10\) verifies the 5/2/2 type assignment. Run `python checker.py` with SymPy installed. These finite checks support, but do not replace, the all-real-parameter analytical arguments above. All equalities are reproducible from the displayed field alone.

## Relationship to prior work
Gasull and Giacomini, *Number of Limit Cycles for Planar Systems with Invariant Algebraic Curves* (first public preprint 27 October 2022; subsequently published in 2023), study precisely this flow in their equation (16) and prove the absence of periodic orbits (Proposition 7.2). That established exclusion is neither reproved nor counted as the new contribution. The new statement is instead its exact **equilibrium census for all real parameters**, including a sharp nine-point interval and the nine-point hyperbolic type partition. Llibre and Zhao (2007) investigate related invariant algebraic curves and limit cycles; the inspected sections did not yield the same parameter-dependent equilibrium classification. The three-line decomposition is algebraically explicit here and cannot be inferred from a generic upper bound of nine on complex cubic intersections alone.

## Limitations
This is a classification of **finite real stationary points**, not a global separatrix graph, a limit-cycle theorem, or a claim of nonlinear conjugacy. The 5/2/2 partition applies only in the open maximal-nine interval. At discriminant endpoints the coalesced equilibria need not be hyperbolic. The earliest public preprint date is established for the 2022 source; discovery priority remains subject to earlier unindexed formulations. The source's no-periodic-orbit theorem is prior work, not independently established here.

## References
- A. Gasull and H. Giacomini, *Number of Limit Cycles for Planar Systems with Invariant Algebraic Curves*, arXiv:2210.15803 (version 1, 2022-10-27); DOI: 10.1007/s12346-023-00746-7. See the equation numbered (16) and Proposition 7.2.
- J. Llibre and Y. Zhao, *Algebraic limit cycles in polynomial systems of differential equations*, Journal of Physics A 40 (2007), 14207–14222; DOI: 10.1088/1751-8113/40/47/012.
