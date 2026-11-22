# A universal expanding Floquet multiplier for symmetry-broken two-cycles of coupled logistic maps

## Finding
For the two-site coupled logistic map
\[
F_{\mu,\gamma}(x,y)=\bigl(\mu x(1-x)+\gamma y,\;\mu y(1-y)+\gamma x\bigr),
\qquad \mu>0,\;\gamma\in\mathbb R,
\]
every primitive two-cycle with **both a nonconstant site average and a nonconstant site imbalance** has a positive real expanding Floquet multiplier greater than \(1\). In particular, none can be an attracting period-two orbit. The exact identity at such a cycle is
\[
\det\bigl(I-DF_{\mu,\gamma}^2\bigr)=-16MABC<0,
\]
where the quantities on the right are defined below.

## Assumptions and scope
All variables and parameters are real, and \(\mu>0\). Write the two distinct orbital points uniquely as
\[
P=(u+w+c+d,\;u-w+c-d),\qquad
Q=(u+w-c-d,\;u-w-c+d).
\]
Here \(u\) is the average of the four site-time coordinates, \(w\) is the time-averaged spatial imbalance, \(c\) is the temporal change of the spatial average, and \(d\) is the temporal change of the spatial imbalance. The asserted class has \(c\ne0\) and \(w\ne0\); the equations below then imply \(d\ne0\). Define
\[
M=\mu(1-2u),\qquad A=M-\gamma-1,\qquad B=M+\gamma+1,\qquad C=M-\gamma+1.
\]
No assumption that the full map preserves the population square is made. On any orbits lying in that square, the conclusion applies without alteration.

## Proof
The exact equalities \(F(P)=Q\) and \(F(Q)=P\), after taking the sums and differences in space and time, give
\[
\begin{aligned}
0&=(\mu+\gamma-1)u-\mu(u^2+w^2+c^2+d^2),\\
Aw&=2\mu cd,\\
Bc&=2\mu wd,\\
Cd&=2\mu wc.
\end{aligned}
\]
If \(c\ne0\) and \(w\ne0\), then \(d\ne0\) by the third equation. The second and fourth equations imply that none of \(A,B,C\) vanishes. Multiplying the last three equations pairwise and cancelling the nonzero factors gives
\[
w^2=\frac{BC}{4\mu^2},\qquad
c^2=\frac{AC}{4\mu^2},\qquad
d^2=\frac{AB}{4\mu^2}.
\]
Hence \(AB,AC,BC>0\), so \(A,B,C\) have one strict common sign. If all are positive then \(M>\max(\gamma+1,-\gamma-1)=|\gamma+1|\ge0\). If all are negative then \(M<-|\gamma+1|\le0\). In either case, \(MABC>0\).

The Jacobian at \((x,y)\) is
\[
DF(x,y)=\begin{pmatrix}\mu(1-2x)&\gamma\\ \gamma&\mu(1-2y)\end{pmatrix}.
\]
For the ordered return matrix \(K=DF(Q)DF(P)\), direct multiplication yields
\[
\begin{aligned}
\operatorname{tr} K&=2\bigl(M^2+\gamma^2+4\mu^2(w^2-c^2-d^2)\bigr),\\
\det\bigl(I-K\bigr)&=-16MABC.
\end{aligned}
\]
The determinant identity follows by expanding \(1-\operatorname{tr}K+\det DF(P)\det DF(Q)\) and using the three squared relations and \(cd=Aw/(2\mu)\). It is also independently checked as an exact polynomial identity by the included symbolic checker.

Since \(\det(I-K)<0\), the real monic characteristic polynomial \(p(t)=\det(tI-K)\) satisfies \(p(1)<0\). As \(p(t)\to+\infty\) for real \(t\to+\infty\), it has a real root strictly greater than \(1\), proving the claim. No assumption on the other Floquet multiplier is needed.

## Verification
The supplied `check.py` verifies symbolically both the four orbit equations and the return-matrix determinant identity under the orbit constraints, using rational polynomial arithmetic. Run `python check.py` with Python 3 and SymPy installed. The proof is independent of numerical enumeration.

## Relationship to prior work
Bosisio, Naimzada and Pireddu (2024) analyze the same additively coupled logistic map by the stretching-along-paths method to prove chaotic dynamics at suitable parameters; their inspected full article does not establish this global no-sink property for symmetry-broken primitive two-cycles. Yousefi, Maistrenko and Popovych (2000) introduced the same economic-map family and discuss stability regions of principal periodic cycles; its full text was not accessible for decisive comparison, so overlap with its detailed two-cycle classification remains a serious publication-priority risk. Earlier studies of coupled logistic maps often use diffusive, not additive, coupling; those models are not algebraically interchangeable here.

## Limitations
The theorem excludes cycles with vanishing temporal mean change \(c=0\), such as pure spatial-swapping orbits, and cycles of vanishing time-averaged imbalance \(w=0\), including synchronous orbits. It makes no claims about higher periods, other attractors, or exact historical priority against inaccessible older detailed classifications. The conclusion is an expanding **real multiplier**, not necessarily a saddle: the other multiplier may also be unstable.

## References
- A. Bosisio, A. Naimzada and M. Pireddu, *Proving chaos for a system of coupled logistic maps: A topological approach*, Chaos 34, 033112 (2024), DOI: 10.1063/5.0175789, https://doi.org/10.1063/5.0175789.
- S. Yousefi, Y. Maistrenko and S. Popovych, *Complex dynamics in a simple model of interdependent open economies*, Discrete Dynamics in Nature and Society 5, 161–177 (2000), DOI: 10.1155/S1026022600000509, https://doi.org/10.1155/S1026022600000509.
