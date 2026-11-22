# An integer-slice obstruction and the missing three-ball phase for taxicab square tori

## Finding
Let \(T=\mathbb R^2/\mathbb Z^2\) carry the quotient taxicab metric
\[d_1(p,q)=\min_{m\in\mathbb Z}|p_1-q_1+m|+\min_{n\in\mathbb Z}|p_2-q_2+n|.\]
Write \(N(r)\) for the minimum number of closed intrinsic radius-\(r\) balls covering \(T\). For every \(0<r<1/2\),
\[N(r)\ge\left\lceil\frac{\lceil1/r\rceil}{2r}\right\rceil.\]
In particular \(N(r)\ge4\) for every \(r<1/2\), whereas \(N(1/2)=2\). Hence the optimal covering radii using two and three freely placed centers coincide, both equalling \(1/2\); *no radius has covering number three*. More precisely \(N(r)=1\) for \(r\ge1\), \(N(r)=2\) for \(1/2\le r<1\), and \(N(r)\ge4\) below \(1/2\). An infinite equality family is
\[N(1/(2n))=2n^2\qquad(n\in\mathbb Z_{\ge1}).\]
For radii just below \(1/2\), the integer-slice obstruction is strictly stronger than the elementary area bound \(N(r)\ge\lceil1/(2r^2)\rceil\).

## Assumptions and scope
The torus is the *unit-period square quotient*, not a torus embedded in three-dimensional space. All centers may be arbitrary points of \(T\). The metric is the intrinsic sum of two circle geodesic distances; balls are closed. There are no lattice-center restrictions. The formula supplies a lower bound at arbitrary radii and exact answers only at the stated radii and in the one-, two-, and three-center regimes; it does not claim a complete covering function for every radius.

## Proof
Set \(u=x+y\) and \(v=x-y\) on the universal cover. The period lattice becomes \(\Lambda=\langle(1,1),(1,-1)\rangle\). The identity \(|x|+|y|=\max\{|x+y|,|x-y|\}\) converts the lift of each intrinsic radius-\(r\) ball to congruent axis-aligned closed squares of side \(2r\) in \((u,v)\)-coordinates. The projection \((u,v)\mapsto v\pmod1\) has circle fibers of \(u\)-length \(2\): \((2,0)\in\Lambda\), and no shorter nonzero horizontal period lies in \(\Lambda\).

Fix \(0<r<1/2\). The \(v\)-projection of each projected ball is a closed arc of length \(2r<1\). On almost every fiber \(v=t\pmod1\), each ball intersects the fiber either in nothing or in a *single* circular interval of \(u\)-length exactly \(2r\). Indeed, the possible vertical lifts differ by integers, and an interval of vertical length \(2r<1\) meets at most one such lift, except at a null set of endpoint values. If \(A(t)\) balls are active on that fiber, the length \(2\) of the fiber requires \(2rA(t)\ge2\). As \(A(t)\) is integral, \(A(t)\ge\lceil1/r\rceil\) for almost all \(t\). Integrating over the unit-period \(v\)-circle, and observing that each of the \(N\) balls is active on an arc of measure exactly \(2r\), gives
\[2rN=\int_0^1 A(t)\,dt\ge\lceil1/r\rceil.\]
Taking the outer ceiling proves the announced bound. Since \(r<1/2\), one has \(\lceil1/r\rceil\ge3\) and \(2r<1\), whence \(N(r)\ge4\).

For the constructive equality family put \(r=1/(2n)\) and \(L_r=\mathbb Z(r,r)+\mathbb Z(r,-r)\). The closed diamonds \(c+\{(x,y):|x|+|y|\le r\}\), \(c\in L_r\), form a face-to-face tiling of \(\mathbb R^2\), since the diamond is a fundamental parallelogram for the displayed generators. The vectors \((1,0)\) and \((0,1)\) lie in \(L_r\) for integral \(n\), so the tiling descends to the unit torus. The lattice covolume is \(2r^2=1/(2n^2)\), hence the quotient has exactly \(2n^2\) distinct centers and covers \(T\). Conversely, each radius-\(r\) torus ball has area at most \(2r^2\), so area one requires at least \(1/(2r^2)=2n^2\) balls. This proves equality for all \(n\ge1\) without using the strict-range slice bound at \(n=1\).

The torus diameter under \(d_1\) equals \(1\), so one ball covers exactly when \(r\ge1\). At \(r=1/2\) the tiling with \(n=1\) uses two balls. At smaller radii the slice lower bound forces at least four; at \(r\ge1/2\) two suffice by monotonicity. Thus no covering number is ever three, and the minimum radii for two or three centers are both \(1/2\).

## Verification
The included `checker.py` enumerates the distinct rational torus centers of the constructive lattices and checks a finite \((4n)\)-by-\((4n)\) grid of test points for each \(n=1,\ldots,6\). It also checks the exact formula for the center counts and the lower-bound arithmetic. The run passed 1,456 finite grid tests. The infinite claims are established by the preceding proof, not by sampling.

## Relationship to prior work
Kai Cieliebak and Milan Cieliebak, *Covering numbers of metric spaces*, arXiv:2611.15599v1 (first publicly available November 11, 2026), introduce the general product-covering conjecture for the sum metric and prove high-dimensional infinitesimal results. The present claim instead identifies the exact missing three-center phase and an all-radius integer-slice obstruction for a specific low-dimensional product of two length-one circles. General parallelogram tilings, elementary measure bounds, and covering-number definitions are standard prior inputs. Published Euclidean two-disk flat-torus covering theorems concern a different norm and do not directly determine the present taxicab three-center question.

## Limitations
No classification of four-center optimizers or exact formula for \(N(r)\) between the resonant radii is claimed. Historical novelty is based on targeted searches and accessible comparisons, not an exhaustive priority certification. The proof uses the special square metric and does not assert analogous behavior for arbitrary skew tori, higher products, or Euclidean geodesic disks.

## References
- K. Cieliebak and M. Cieliebak, *Covering numbers of metric spaces*, arXiv:2611.15599v1, https://arxiv.org/html/2611.15599v1 (2026-11-11).
- AMS Mathematics Subject Classification 2020, code 52C17 (packing and covering in discrete geometry).
