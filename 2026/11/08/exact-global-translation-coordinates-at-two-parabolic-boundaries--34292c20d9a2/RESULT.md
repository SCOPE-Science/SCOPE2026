# Exact global translation coordinates at two parabolic boundaries of a piecewise symplectic plane map

## Finding
For each \(b\in\{0,1\}\), the homogeneous area-preserving plane map \(F_b\) below has an explicit global action–time normal form outside one fixed ray. In coordinates \((J,t)\), the map is precisely \((J,t)\mapsto(J,t+1)\); its phase portrait, invariant foliation, exact first-entry time and asymptotic transport velocity can therefore be read off without solving an itinerary recurrence.

Set \(R=\{(u,u):u\ge0\}\), and for \((x,y)\notin R\) set
\[
c_0(x,y)=\max\{|x-y|,-x-y\},\qquad
c_1(x,y)=\max\{|x-y|,-x,-y\}.
\]
Each height is strictly positive on the complement of \(R\), vanishes exactly on \(R\), and is constant on trajectories of its respective map. Define \(\Phi_b:(0,\infty)\times\mathbb R\to\mathbb R^2\setminus R\) by
\[
\Phi_0(c,t)=\begin{cases}
(-ct,c(1-t)), &t\le1,\\
(c(t-2),c(1-t)), &1\le t\le2,\\
(c(t-2),c(t-3)), &t\ge2;
\end{cases}
\]
\[
\Phi_1(c,t)=\begin{cases}
(-ct,c(1-t)), &t\le1,\\
(-c,c(1-t)), &1\le t\le2,\\
(c(t-3),-c), &2\le t\le3,\\
(c(t-3),c(t-4)), &t\ge3.
\end{cases}
\]
These are homeomorphisms, with exact global conjugacies
\[
F_b\circ\Phi_b(c,t)=\Phi_b(c,t+1),\qquad b\in\{0,1\}.
\]
On the open smooth pieces of either chart,
\[
\Phi_b^*(dx\wedge dy)=c\,dc\wedge dt=dJ\wedge dt,\qquad J=c^2/2.
\]
The equality describes a piecewise canonical transformation, not a globally smooth symplectomorphism across the chart seams.

Every nonfixed point \(z\) has unbounded forward and backward orbits, no nontrivial periodic points, and the **same limiting position-per-elapsed-time vector** in the two time directions:
\[
\lim_{k\to+\infty}\frac{F_b^k(z)}k=
\lim_{k\to+\infty}\frac{F_b^{-k}(z)}k
=(c_b(z),c_b(z)).
\]
Here both limits divide by positive elapsed time \(k\), whether iterating forward or backward. Writing \(t_b(z)\) for its unique chart-time coordinate, the least nonnegative iterate entering the outgoing shear cone \(\{x\ge y\ge0\}\) is exactly
\[
N_b(z)=\max\{0,\lceil3+b-t_b(z)\rceil\}.
\]

## Assumptions and scope
For the two integer parameters \(b=0\) and \(b=1\), consider
\[
F_b(x,y)=\begin{cases}
(2x-y,x),&x\ge0,\\
(bx-y,x),&x<0.
\end{cases}
\]
The expressions agree on \(x=0\). We work on the entire real plane, for every real initial condition and every positive or negative integer iterate. No compactness, smoothness at the switching line, genericity, or measure-theoretic exceptional-set qualification is assumed. Exact first-entry times use the inclusive inequalities \(x\ge y\ge0\). The source's rotation-number classification alone does not provide these coordinates.

## Proof
**Fixed ray and positivity.** The fixed-point equation has \(y=x\). For \(x\ge0\), the first component gives \(2x-y=x\), automatically. For \(x<0\), the first component gives \((b-2)x=0\), impossible since \(b\in\{0,1\}\). Thus the fixed set is exactly \(R\). Each of the displayed maxima is nonnegative, and vanishes only if \(x=y\ge0\). This proves positivity of the height outside \(R\).

**Exhaustive foliation.** Fix \(c>0\). For \(b=0\), the equation \(c_0(x,y)=c\) is the union of the incoming ray \(y-x=c\) up to \((-c,0)\), the lower-left segment \(x+y=-c\) from \((-c,0)\) to \((0,-c)\), and the outgoing ray \(x-y=c\) from \((0,-c)\) onward. For \(b=1\), it is the incoming ray \(y-x=c\) ending at \((-c,0)\), the segment \(x=-c\) ending at \((-c,-c)\), the segment \(y=-c\) ending at \((0,-c)\), and the outgoing ray \(x-y=c\). The displayed formulae traverse each contour once, from incoming to outgoing, and the pieces meet with matching endpoints. Every point off \(R\) lies on exactly one of these contours with exactly one \(t\). The inverse is continuous on each interior piece and agrees on seams, giving a global homeomorphism. In particular \(c_b(\Phi_b(c,t))=c\).

**Time-one identity.** For \(b=0\), partition the time coordinate into \(({-\infty},0]\), \([0,1]\), \([1,2]\), \([2,\infty)\). Under the first piece, \(x\ge0\), so the right branch maps \((-ct,c(1-t))\) to \((-c(t+1),-ct)=\Phi_0(c,t+1)\). Under the second piece, \(x\le0\), so the left branch maps that point to \((c(t-1),-ct)=\Phi_0(c,t+1)\). The third piece maps \((c(t-2),c(1-t))\) to \((c(t-1),c(t-2))=\Phi_0(c,t+1)\). On the fourth piece, right-branch shear maps \((c(t-2),c(t-3))\) to \((c(t-1),c(t-2))=\Phi_0(c,t+1)\).

For \(b=1\), use the five time intervals \(({-\infty},0]\), \([0,1]\), \([1,2]\), \([2,3]\), \([3,\infty)\). The corresponding images are, respectively, \((-c(t+1),-ct)\), \((-c,-ct)\), \((c(t-2),-c)\), \((c(t-2),c(t-3))\), and \((c(t-2),c(t-3))\). Comparing with the next interval of the defining formula gives \(F_1(\Phi_1(c,t))=\Phi_1(c,t+1)\) in every case. At boundaries, branch agreement gives the same identity. Invertibility of \(F_b\), or the displayed homeomorphism, extends the identity to every signed iterate.

**Area.** In variables ordered as \((c,t)\), the Jacobian of every affine-in-\(t\) branch equals \(c\). For instance the incoming branch has columns \((-t,1-t)\) and \((-c,-c)\), whose determinant is \(c\). On the remaining horizontal, vertical, diagonal and outgoing pieces, direct differentiation also gives \(c\). Since \(d(c^2/2)=c\,dc\), this proves the stated area form almost everywhere, including its precise limitation at seams. Each branch matrix of \(F_b\) itself has determinant one.

**Global consequences.** Both maps fix \(R\). On its complement, translation \(t\mapsto t+n\) has no periodic points. As \(t+n\to+\infty\), the outgoing formula is \(\Phi_b(c,t+n)=c(t+n-2-b,t+n-3-b)\). As \(t+n\to-\infty\), the incoming formula is \(\Phi_b(c,t+n)=c(-(t+n),1-(t+n))\). Dividing by positive elapsed time \(k\) proves the two drift limits, and shows escape in both directions. Finally, \(\Phi_b(c,t)\in\{x\ge y\ge0\}\) if and only if \(t\ge3+b\): neither the incoming ray nor any intermediate leg belongs to this cone, while the outgoing leg enters it at this exact time threshold. Integer translation yields the ceiling formula for \(N_b\). This exhausts all initial states and parameter values claimed.

## Verification
The accompanying standalone Python 3 script `checker.py` uses exact fractions, not floating-point numerics. It tests \(\Phi_b\), the independent map formula, invariants, inverse coordinates, four subsequent iterates, exact cone-entry thresholds, and Jacobian determinants for both parameters, a family of positive rational heights and a time grid crossing all seams. It produced **34,659 passing exact-rational assertions**. This finite check supports, but does not establish, the universal theorem; the proof above establishes the all-real, all-integer conclusions.

## Relationship to prior work
The two-zone homogeneous plane map is classical; its definition and broad dynamics are not new. Lagarias and Rains [1] prove that its induced circle map has rotation number zero whenever the right-branch trace is at least two, and their sequel [2] studies invariant circles. Garcia-Morato and collaborators [3] investigate resonance regions and the trace-two transition. Roberts, Saito and Vivaldi [4] study critical curves and symbolic itineraries in the same map family. The present result fixes two natural integer parameters on that parabolic trace-two boundary and gives exact global *plane-level* transport coordinates, a canonical area identity, the entire orbit portrait, sharp entry times, and an explicit speed at every initial state. Knowing the common zero circle rotation number, or the existence of a fixed ray, does not by itself yield these quantitative formulas. No general claim about all real left-branch traces is made.

## Limitations
This result covers exactly \(b\in\{0,1\}\) with right-branch coefficient \(2\); it does not classify the remaining real parameter space. The canonical coordinates are globally continuous and piecewise smooth but not globally differentiable at seams or defined on the fixed ray. The original circle rotation-zero classification is prior knowledge, not a novelty claim. No independent audit has been performed. A differently parameterized classical construction could potentially imply the same explicit normal forms; priority beyond the inspected literature is not established.

## References
[1] J. C. Lagarias and E. Rains, *Dynamics of a family of piecewise-linear area-preserving plane maps I: Rational rotation numbers*, arXiv:math/0301294, https://arxiv.org/abs/math/0301294.

[2] J. C. Lagarias and E. Rains, *Dynamics of a family of piecewise-linear area-preserving plane maps II: Invariant circles*, arXiv:math/0303007, https://arxiv.org/abs/math/0303007.

[3] L. B. Garcia-Morato et al., *Bifurcation patterns in homogeneous area-preserving piecewise-linear maps*, open-access manuscript, https://upcommons.upc.edu/server/api/core/bitstreams/4dd8bcd7-56f6-4ce1-84c8-e367b5535f6b/content.

[4] J. A. G. Roberts, A. Saito and F. Vivaldi, *Critical curves of a piecewise linear map*, arXiv:2104.07197v1 (first public submission 2021-04-15), https://arxiv.org/abs/2104.07197.
