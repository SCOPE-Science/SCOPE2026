# Sharp multiplicity and stability transitions for repeated-height three-cycles of nilpotent-Jacobian maps

## Finding
For a real polynomial \(P\) of degree \(d\geq1\) with \(P(0)=0\), consider the polynomial map
\[
F_P(x,y,z)=\bigl(P(y+x^2),\ z-2xP(y+x^2),\ P(y+x^2)^2\bigr).
\]
Its Jacobian is nilpotent at every point. Under the explicit polynomial coordinate change in the proof it is conjugate to
\[
G_P(X,Y,Z)=\bigl(P(Y)-P(Z),\ Z,\ [P(Y)-P(Z)]^2\bigr).
\]
Call a primitive period-three orbit **repeated-height** when two of its three \(Z\)-coordinates in this canonical normal form agree. Exactly one orbit arises for every positive root of \(P(s)^2=s\), and every repeated-height primitive three-cycle arises this way. Consequently their number \(N_{\mathrm{rh}}(P)\) obeys the **sharp degree bound**
\[
1\leq N_{\mathrm{rh}}(P)\leq 2d-1.
\]
For every \(d\geq1\), the upper bound is attained by a nonempty open set of coefficients: there are \(2d-1\) distinct hyperbolic saddle three-cycles of this type simultaneously. Thus the count is unbounded as the polynomial degree grows, despite the pointwise nilpotent Jacobian.

For the natural quadratic family \(P_\kappa(t)=\kappa t(t-1)\), \(\kappa>0\), the repeated-height cycle count is exactly one for \(\kappa^2<27/4\), two for \(\kappa^2=27/4\), and three for \(\kappa^2>27/4\). The additional middle cycle is locally attracting exactly in the interval
\[
\frac{27}{4}<\kappa^2<\frac{125}{12},
\]
with a superattracting instance at \(\kappa^2=8\). All other repeated-height cycles of this quadratic family are saddles wherever they are hyperbolic. The collision cycle at \(\kappa^2=27/4\), and the middle cycle at \(\kappa^2=125/12\), have a unit multiplier; no nonlinear stability assertion is made at these endpoints.

## Assumptions and scope
All dynamics are over \(\mathbb R^3\) and use ordinary forward iteration. The phrase *repeated-height* refers specifically to the third coordinate \(Z\) of the defined canonical conjugate \(G_P\); it is **not** an assertion that every period-three orbit has repeated heights. Polynomials may have other prime-three cycles with three distinct heights. All cycle counts in this result concern the repeated-height stratum only, including at bifurcation endpoints, and count orbits rather than points.

The polynomial \(P\) has exact degree \(d\) and zero constant term (a constant term has no effect on \(G_P\)). The explicit attaining family is \(P_\kappa(t)=\kappa t\prod_{j=1}^{d-1}(t-j)\) with sufficiently large real \(\kappa>0\), interpreting the empty product as one for \(d=1\). The open-set statement is relative to the coefficient space \(\{P:\deg P=d, P(0)=0\}\).

## Proof
**1. Nilpotency and conjugacy.** Write \(h=y+x^2\), \(p=P(h)\), and \(q=P'(h)\). Direct differentiation gives
\[
DF_P=\begin{pmatrix}2xq&q&0\\-2p-4x^2q&-2xq&1\\4xpq&2pq&0\end{pmatrix}.
\]
Its characteristic polynomial is \(\lambda^3\): the trace, determinant, and sum of principal \(2\times2\) minors vanish. By Cayley–Hamilton the matrix is nilpotent at every point. The polynomial automorphism
\[
\Psi(X,Y,Z)=\bigl(X+P(Y),\ Y-[X+P(Y)]^2,\ Z+P(Y)[P(Y)+2X]\bigr)
\]
has the polynomial inverse obtained successively from \(Y=y+x^2\), \(X=x-P(Y)\), and \(Z=z-P(Y)[P(Y)+2X]\). Direct substitution yields \(\Psi^{-1}\circ F_P\circ\Psi=G_P\).

**2. Characterization of all repeated-height cycles.** On a full orbit of \(G_P\), write \(Z_j\) for the third coordinate at time \(j\). Since \(Y_j=Z_{j-1}\),
\[
Z_{j+1}=[P(Z_{j-1})-P(Z_j)]^2.
\]
For a period-three orbit, if two of the \(Z\)-values coincide at \(s\), the remaining value is zero. If \(s=0\), all three coordinates are zero and the orbit is fixed. Otherwise \(s>0\), and the recurrence requires \(P(s)^2=s\). Conversely, every \(s>0\) satisfying this equation gives the exact orbit
\[
(0,s,0)\longmapsto(P(s),0,s)\longmapsto(-P(s),s,s)\longmapsto(0,s,0).
\]
It is primitive, since \(s>0\) and \(P(s)\ne0\). Different positive roots give distinct orbits because each orbit has exactly one point with first coordinate zero. These exhaust the repeated-height primitive-three orbits up to cyclic permutation.

**3. Sharp polynomial-degree bound and its robust attainment.** Factor \(P(s)=sQ(s)\), where \(Q\) has degree \(d-1\). For \(s>0\), the cycle equation is equivalent to \(sQ(s)^2=1\), a polynomial equation of degree \(2d-1\). Thus \(N_{\mathrm{rh}}(P)\le2d-1\). The polynomial \(sQ(s)^2-1\) is negative at zero and tends to positive infinity as \(s\to\infty\), so it has at least one positive root.

For \(P_\kappa(s)=\kappa s\prod_{j=1}^{d-1}(s-j)\), write
\[
H_\kappa(s)=\kappa^2s\prod_{j=1}^{d-1}(s-j)^2-1.
\]
At each endpoint \(0,1,\ldots,d-1\), this is \(-1\). In each bounded interval \((j-1,j)\), \(1\le j\le d-1\), the value at \(j-1/2\) is positive for all sufficiently large \(\kappa\). Hence there are at least two distinct roots in every such interval. Beyond \(d-1\) the function increases from \(-1\) to infinity and has at least one root. The resulting \(2(d-1)+1=2d-1\) distinct positive roots exhaust the polynomial degree, hence each is simple. For \(d=1\), the single root is \(s=\kappa^{-2}\). The strict signs and simple roots persist under sufficiently small coefficient perturbations, giving a nonempty open coefficient region with the maximal count.

**4. Hyperbolic saddle persistence in the attaining family.** At a canonical three-cycle with \(a=P(s)\), \(b=P'(s)\), \(c=P'(0)\), the derivative of \(G_P^3\) at \((0,s,0)\) has spectrum
\[
\{0,0,\Lambda(s)\},\qquad \Lambda(s)=4P(s)^2P'(s)^2=4sP'(s)^2.
\]
For the displayed attaining polynomial, the root equation reduces this to
\[
\Lambda(s)=4\left(1+s\sum_{j=1}^{d-1}\frac1{s-j}\right)^2.
\]
As \(\kappa\to\infty\), one root tends to \(0\) and its multiplier tends to \(4\); the other \(2(d-1)\) roots tend in pairs to the simple zeros \(1,\ldots,d-1\), and their multipliers tend to \(+\infty\). Therefore, after increasing \(\kappa\) if necessary, every displayed three-cycle is hyperbolic with exactly one expanding multiplier and two zero multipliers: a saddle. Hyperbolicity and existence of the cycles persist on an open coefficient neighbourhood.

**5. Exact quadratic phase diagram.** For \(P_\kappa(s)=\kappa s(s-1)\), the equation is
\[
\kappa^2s(s-1)^2=1.
\]
The function \(s(s-1)^2\) has a unique positive local maximum \(4/27\) at \(s=1/3\), decreases to zero at \(s=1\), and strictly increases for \(s>1\). This proves the exact one/two/three root counts and the first threshold \(\kappa^2=27/4\). The multiplier is
\[
\Lambda(s)=4\left(\frac{2s-1}{s-1}\right)^2,
\qquad
\Lambda(s)-1=\frac{(3s-1)(5s-3)}{(s-1)^2}.
\]
The smallest root \(0<s<1/3\) and largest root \(s>1\) always have \(\Lambda>1\). The middle root in \((1/3,1)\) satisfies \(\Lambda<1\) precisely when \(1/3<s<3/5\). Since this root increases continuously with \(\kappa\), it crosses \(3/5\) at the exact parameter \(\kappa^2=[(3/5)(2/5)^2]^{-1}=125/12\). At \(\kappa^2=8\), it is \(s=1/2\), yielding \(\Lambda=0\). The derivative spectrum proves the stated local attracting/saddle types, and identifies the unit-multiplier boundaries without claiming their nonlinear classification.

## Verification
A standalone SymPy checker, `check_cycles.py`, reconstructs the Jacobian characteristic polynomial, polynomial conjugacy, the three-step multiplier, exact bifurcation factorizations, and strict rational sign witnesses for degrees \(1\) through \(11\). Run `python check_cycles.py` with SymPy installed. The general-degree root count, root simplicity, and large-\(\kappa\) saddle limit are proved above for all degrees; the finite checker is only supplementary verification.

## Relationship to prior work
Castañeda and Rebollo–Perdomo, arXiv:2209.06986v1, provide the conjugate recurrence in their equation (10), construct **at least one** three-cycle from their scalar equation (11), and calculate the transverse multiplier in the proof of Theorem 1.1. Those starting formulas and the nilpotent-Jacobian family are credited here. Their concluding remarks ask about uniqueness of the three-cycle. The new theorem instead determines the entire repeated-height stratum, its sharp degree-dependent multiplicity, an open saddle coexistence regime, and the exact quadratic saddle–sink transition thresholds. It does not claim uniqueness or a census of cycles with three distinct heights.

Chamberland's earlier study provides the nilpotent-Jacobian dynamical framework and a related sufficient condition for a three-cycle, but not the stated sharp repeated-height multiplicity and coefficient-space phase diagram. The established existence of cycles with all three heights distinct is logically separate from the repeated-height classification proved here.

## Limitations
The count \(2d-1\) is sharp **within the repeated-height stratum**, not an upper bound on all prime-three orbits. No bound is claimed for cycles with three distinct heights, or for arbitrary periods. The attracting statement is local; no global attraction basin is asserted. At unit multipliers the result supplies an exact linear classification only. These results have not undergone independent mathematical validation. Literature searches cannot exclude all unpublished or unindexed equivalents.

## References
1. Á. Castañeda and S. Rebollo–Perdomo, *Discrete and continuous dynamics of real 3-dimensional nilpotent polynomial vector fields*, arXiv:2209.06986v1 (first posted 15 September 2022), especially Theorem 1.1, equations (10)–(12), and concluding remarks. https://arxiv.org/abs/2209.06986
2. M. Chamberland, *Dynamics of Maps with Nilpotent Jacobians*, author's manuscript dated 17 May 2005, Theorem 3.1 and Sections 3–4; later published in *Journal of Difference Equations and Applications* 12 (2006), 49–56. https://chamberland.math.grinnell.edu/papers/nilpotent.pdf
