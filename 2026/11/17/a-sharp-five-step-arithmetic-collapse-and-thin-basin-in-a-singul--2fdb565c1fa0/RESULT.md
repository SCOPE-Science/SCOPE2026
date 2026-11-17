# A sharp five-step arithmetic collapse and thin basin in a singular four-partition map

## Finding
Consider the integral planar absolute-value map
\[
T(x,y)=(|x|-y-1,\ x+|y|-1),\qquad (x,y)\in\mathbb Z^2.
\]
It has precisely two primitive periodic orbits among integer points:
\[
C_s=\{(-1,-1),(1,-1),(1,1),(-1,1)\},\qquad
C_\ell=\{(1,-3),(3,3),(-1,5),(-5,3)\}.
\]
Every integer point enters one of these two four-cycles in at most five iterations, and five is the **smallest universal bound**. Exactly the following lattice points are eventually captured by \(C_s\):
\[
\begin{split}
S={}&\{(x,y):x\le-2,\ y\in\{-x-1,-x\}\}\\
&\cup\{(x,y):x=-1,\ y\le1\}\\
&\cup\{(x,y):x=0,\ y\in\{-2,-1,0\}\}\\
&\cup\{(x,y):x=1,\ y\ge-1\}\\
&\cup\{(x,y):x\ge2,\ y=x-2\},
\end{split}
\]
where all coordinates in this display are integers. The complement \(\mathbb Z^2\setminus S\) is precisely the basin of \(C_\ell\). For every integer \(N\ge2\),
\[
\#(S\cap([-N,N]^2\cap\mathbb Z^2))=5N+4.
\]
Thus the smaller orbit's basin has asymptotic lattice density zero, despite being an infinite union of rays and half-lines. In particular no other integer periodic orbit exists.

## Assumptions and scope
The map is the specialization \(a=-1,c=1\) of the four-quadrant system \(T_{a,c}(x,y)=(|x|+ay-1,x+c|y|-1)\). Only **integer initial conditions** are claimed. We do not claim that every real orbit is eventually periodic. The full two-parameter map and its period-four bifurcations appear in [1]; the case considered here is a singular boundary \(c=-a\), not a generic invertible branch regime.

## Proof
**1. Two invariant cycles and the lattice image.** Direct substitution shows that the points of \(C_s\) appear in the displayed cyclic order. Likewise \(C_\ell\) appears in the displayed cyclic order. For \((x,y)\in\mathbb Z^2\), let \((X,Y)=T(x,y)\) and put
\[
p=(X+Y+2)/2=\max(x,0)+\max(-y,0),\qquad
q=(X-Y)/2=\max(-x,0)-\max(y,0).
\]
Both are integers and \(p\ge0\). Conversely \((X,Y)=(p+q-1,p-q-1)\). Therefore every orbit, after its first iteration, belongs to the invariant arithmetic cone \(\{(p+q-1,p-q-1):p\in\mathbb Z_{\ge0},q\in\mathbb Z\}\).

**2. A complete finite-depth case analysis.** Conjugate the map on that cone to \(R(p,q)\). For \(p\ge2\), the following mutually exhaustive and boundary-compatible cases follow by substituting the signs of \(p+q-1\) and \(p-q-1\):

* If \(q\le1-p\), then \(R(p,q)=(0,2-2p)\), followed by \((0,2)\).
* If \(q\ge p-1\), then \(R(p,q)=(2q,0)\). The case \((p,q)=(2,1)\) enters \((2,0)\); all other such cases have \(q\ge2\) and proceed via \((2q-1,1-2q)\) and \((0,4-4q)\) to \((0,2)\).
* If \(2-p\le q\le p-2\) and \(q\le0\), then \(R(p,q)=(p+q-1,q-p+1)\), and the following iterate is \((0,4-2p-2q)\). This is \((0,0)\) precisely for \(q=2-p\); otherwise it reaches \((0,2)\) in one further step.
* If \(2-p\le q\le p-2\) and \(q\ge1\), then two consecutive iterations give \((2q-1,3-2p)\), followed by \((0,4-4q)\). For \(q=1\) this is \((0,0)\); for \(q\ge2\) the next image is \((0,2)\).

For \(p=0\), the cases \(q\le-1\), \(q=0\), \(q=1\), and \(q\ge2\) go respectively to \((0,2)\), \((1,1)\), \((2,0)\), and \((2q,0)\). For \(p=1\), the cases \(q\le0\), \(q=1\), and \(q\ge2\) go respectively to \((0,0)\), \((2,0)\), and \((2q,0)\). The already discussed paths from \((2q,0)\) complete these cases. In each case, after at most four iterations of \(R\) one is in one of the following two invariant sets:
\[
E_s=\{(0,0),(1,1),(2,0),(1,-1)\},\qquad
E_\ell=\{(0,2),(4,0),(3,-3),(0,-4)\}.
\]
These are precisely \(C_s,C_\ell\) in the conjugate coordinates. Together with the first iteration of the original map, this gives the universal five-step assertion.

**3. Exact basin decision.** The same exhaustive cases show that a cone state enters \(E_s\) if and only if
\[
(p=0\text{ and }q\in\{0,1\})\quad\text{or}\quad
(p=1\text{ and }q\le1)\quad\text{or}\quad
(p\ge2\text{ and }q\in\{1,2-p\}).
\]
Apply this criterion to the first-image coordinates \(p=\max(x,0)+\max(-y,0)\), \(q=\max(-x,0)-\max(y,0)\), separately in the four closed quadrants. The equivalent conditions in the original integer plane are exactly the five pieces defining \(S\) above. The five pieces are mutually disjoint since they occupy respectively \(x\le-2,x=-1,x=0,x=1,x\ge2\). For \(N\ge2\), their square counts are respectively \(2(N-1)\), \(N+2\), \(3\), \(N+2\), and \(N-1\), giving \(5N+4\). Its ratio to \((2N+1)^2\) tends to zero.

**4. Sharpness and periodic census.** The exact trajectory
\[
(-3,0)\mapsto(2,-4)\mapsto(5,5)\mapsto(-1,9)\mapsto(-9,7)\mapsto(1,-3)
\]
first meets the two cycles at its fifth iterate, proving sharpness. Any integer periodic point must belong to the invariant periodic core because all points enter it in five steps, and each core cycle has least period four by direct substitution.

## Verification
A standalone Python checker (`verify.py`) uses exact integer arithmetic. It checks the two four-cycle identities, the four-step conjugated collapse and correct basin classification at 20,301 cone states, the global five-step capture and the formula \(5N+4\) at five square sizes, and the sharpness witness. Expected output: `VERIFY_OK period_cycles=2 transformed_cases=20301 square_counts=5 sharpness=1`. These finite checks are **corroboration only**. The exhaustive symbolic case partition above proves the assertions for every integer input.

## Relationship to prior work
The underlying continuous-state four-quadrant map, its fixed points and low-period bifurcations are treated in [1]. This theorem instead classifies **all lattice orbits** on the singular line \(c=-a\) at the canonical integral parameter \((-1,1)\); it is not a claim about generic real-plane attractors. Related literature on distinct absolute-value maps gives finite-time collapse or eventually periodic real trajectories [2]; their maps have different second-coordinate signs/parameters, and those theorems do not imply the present lattice-capture statement. The full historical-priority search is not conclusive.

## Limitations
The theorem is about integer initial conditions and exactly one natural integer parameter. It neither classifies real nonlattice trajectories nor nearby nonintegral parameters. The five-step uniform bound is for entry into one of the eight core **states**, not for reaching a designated point in a cycle. Finite checker runs are not proofs or independent certification. Historical priority remains provisional, including because the full text of some earlier related journal literature could not be inspected.

## References
[1] W. Tikjha, *Multistability and Bifurcation Phenomena in a Four-Partitions Piecewise Linear Map*, arXiv:2607.13519v1, first publicly posted 2026-07-15, https://arxiv.org/abs/2607.13519.

[2] J. Cima, A. Gasull, V. Mañosa and F. Mañosas, work on eventual periodicity of a different absolute-value planar map, https://arxiv.org/abs/2507.05881 (related model; not a source of the present theorem).

[3] Tikjha and collaborators, related four-quadrant bifurcation literature, *Chaos, Solitons & Fractals* (2020), doi:10.1016/j.chaos.2020.109813 (full text not inspected).
