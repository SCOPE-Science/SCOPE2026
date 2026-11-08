# Unbounded minimal Ehrhart quasi-period in four-facet halfway-lattice parallelograms

## Finding
For each odd integer \(q\ge3\), set
\[
P_q=\{(x,y)\in\mathbb R^2: |x|\le\tfrac12,\ |x+qy|\le\tfrac12\}.
\]
Let \(L_q(t)=|tP_q\cap\mathbb Z^2|\) for integral \(t\ge0\). Define
\[
\delta_t=\begin{cases}1,&t\text{ even},\\0,&t\text{ odd},\end{cases}\quad
N_t=t+\delta_t,\quad r_t=N_t-q\lfloor N_t/q\rfloor\in\{0,\ldots,q-1\}.
\]
Then the exact Ehrhart quasi-polynomial is
\[
\boxed{L_q(t)=\frac{N_t^2+r_t(q-r_t)}q.}
\]
Its **minimal quasi-period is exactly \(2q\)**. Consequently four-facet centrally symmetric halfway-lattice polygons, with all facet normals primitive and no facet lattice points, exhibit arbitrarily large minimal Ehrhart quasi-periods.

## Assumptions and scope
Here a halfway-lattice supporting line means a line of equation \(\langle u,z\rangle=k+\tfrac12\), for a primitive integer normal \(u\) and an integer \(k\). The four supporting lines of \(P_q\) have primitive normals \(\pm(1,0)\) and \(\pm(1,q)\). The consecutive normal determinant has magnitude \(q>1\), so the polygon is not unimodular in the facet-normal sense. Its vertices are \((-\tfrac12,0)\), \((-\tfrac12,1/q)\), \((\tfrac12,-1/q)\), \((\tfrac12,0)\); its area is \(1/q\), and its minimal vertex denominator is \(2q\) for odd \(q\).

For a rational polytope, a quasi-period \(T\) means that \(L(t)\) agrees, for every nonnegative integer \(t\), with a polynomial depending only on \(t\bmod T\). The minimal quasi-period is the least positive such \(T\). The asserted formula includes \(t=0\), when the dilation consists of the origin.

## Proof
**Exact count.** Under the integer linear map \((x,y)\mapsto(u,v)=(x,x+qy)\), integer pairs map precisely to pairs \((u,v)\in\mathbb Z^2\) satisfying \(u\equiv v\pmod q\). The conditions \((x,y)\in tP_q\) become \(|u|,|v|\le t/2\). For integral \(t\ge0\), that interval contains \(N_t=t+\delta_t\) consecutive integers. Write \(N_t=qa+r\), \(0\le r<q\). Exactly \(r\) congruence classes occur \(a+1\) times, and the remaining \(q-r\) classes occur \(a\) times. Therefore
\[
L_q(t)=r(a+1)^2+(q-r)a^2
=\frac{(qa+r)^2+r(q-r)}q.
\]
The possible residue vectors \((\delta_t,r_t)\) depend only on \(t\bmod 2q\), so \(2q\) is a quasi-period.

**Minimality.** For a residue \(s\bmod2q\), its constituent polynomial is
\[
F_s(X)=\frac{(X+\delta_s)^2+r_s(q-r_s)}q,
\qquad r_s\equiv s+\delta_s\pmod q,\quad0\le r_s<q.
\]
Suppose \(T\) is any quasi-period, not necessarily assumed to divide \(2q\). Compare large nonnegative integers on any fixed class modulo \(\operatorname{lcm}(T,2q)\). Uniqueness of polynomial interpolation on infinitely many integers implies \(F_s=F_{s+T}\) for all \(s\bmod 2q\). The linear coefficient of \(F_s\) is \(2\delta_s/q\); thus \(T\) must be even. Choose \(s=q\), which is odd and has \(\delta_s=0\), \(r_s=0\). Since \(T\) is even, the residue \(s+T\) is also odd; equality of constant terms gives \(r_{s+T}(q-r_{s+T})=0\). With \(0\le r_{s+T}<q\), this forces \(r_{s+T}=0\), i.e. \(q\mid T\). Because \(q\) is odd, \(2q\mid T\). Since \(2q\) is a quasi-period, it is minimal.

**Geometry.** The map \((x,y)\mapsto(x,x+qy)\) has determinant \(q\), so \(P_q\) has area \(1/q\). Its primitive facet normals are as stated. Because its bounding-line values are half-integers, no lattice point lies on a facet; the origin is the only interior integer point (indeed \(|x|\le1/2\) forces \(x=0\) and \(|qy|\le1/2\) forces \(y=0\)).

## Verification
An independent finite verifier, `verify_halfway_period.py`, enumerates integer points directly in the two defining strips for \(q\in\{3,5,\ldots,27\}\) and \(0\le t\le93\), and checks the formula, giving 1,222 comparisons. It separately constructs the exact rational constituent coefficients for each such \(q\), checks that no proper divisor of \(2q\) is a constituent period, and tests the \(2q\) period. The universal claim is established by the preceding proof; finite checks do not establish it by themselves. Run `python3 verify_halfway_period.py` in the folder containing this document.

## Relationship to prior work
Chu and Karshon (2026) prove a Pick-type area theorem for **unimodular** halfway-lattice polygons, and discuss the role of the unimodularity assumption. The family here is systematically nonunimodular and asks a different arithmetic question: the full dilate-count quasi-polynomial and its **minimal period**. General Ehrhart theory supplies the bound dividing the vertex denominator \(2q\), but does not force this bound to be sharp. Work on quasi-period collapse and coefficient periods addresses broader rational-polygon classes; no exact covering theorem for this specified halfway-lattice family was identified in the inspected material. The result is not claimed as the first construction of arbitrarily long Ehrhart periods for general rational polygons.

## Limitations
The classification is for the explicit one-parameter family, restricted to odd \(q\ge3\). It does not classify all nonunimodular halfway-lattice polygons, show analogous behavior for every prescribed rational polygon, or address Ehrhart positivity beyond the stated formula. Historical novelty is provisional; earlier work using different equivalent descriptions may exist. The supporting computations are finite tests, and independent mathematical audit has not been performed.

## References
- C. Chu and Y. Karshon, *A Pick-type theorem for halfway-lattice polygons*, arXiv:2610.00696v1 (first public 2026-09-30), https://arxiv.org/abs/2610.00696.
- M. Bohnert, *Quasi-period collapse in half-integral polygons*, arXiv:2405.13404, https://arxiv.org/abs/2405.13404.
- T. B. McAllister and M. Moriarity, *Ehrhart quasi-period collapse in rational polygons*, arXiv:1509.03680, https://arxiv.org/abs/1509.03680.
