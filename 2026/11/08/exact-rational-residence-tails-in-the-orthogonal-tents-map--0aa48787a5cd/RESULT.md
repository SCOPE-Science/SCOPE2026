# Exact rational residence tails in the orthogonal tents map

## Finding

The orthogonal tents map of the two-torus has an **exact rational survival law** inside a distinguished parabolic Jacobian branch. Let \(\mathbb T^2=(\mathbb R/\mathbb Z)^2\), \(h(t)=2\min(\{t\},1-\{t\})\), and
\[
H=G\circ F,\qquad F(x,y)=(\{x+h(y)\},y),\qquad G(u,v)=(u,\{v+h(u)\}),
\]
where \(\{t\}\) denotes the fractional part. Define the upper-left branch
\[
A_3=\bigl\{(x,y)\in[0,1)^2:y\ge\tfrac12,\ \{x-2y\}<\tfrac12\bigr\},
\]
and for each integer \(n\ge1\) define the initial survivor region
\[
S_n=\bigl\{z\in A_3:H^j(z)\in A_3\ \text{for every }0\le j<n\bigr\}.
\]
Writing \(\mu\) for normalized torus Lebesgue area, the exact values are
\[
\boxed{\mu(S_1)=\tfrac14,\quad \mu(S_2)=\tfrac1{12},\quad
\mu(S_{2m})=\frac{2m-1}{4(4m-3)(4m-1)}\quad(m\ge2).}
\]
For **all** integers \(n\to\infty\), including odd times,
\[
\boxed{\lim_{n\to\infty}n\mu(S_n)=\tfrac1{16}.}
\]
If \(Z\) is uniform in \(A_3\) and \(\tau=\inf\{j\ge1:H^j(Z)\notin A_3\}\), then \(\Pr(\tau<\infty)=1\) but
\[
\boxed{\lim_{n\to\infty}n\Pr(\tau>n)=\tfrac14,\qquad \mathbb E[\tau]=\infty.}
\]
The exact finite-time law and its coefficient quantify the intermittent residence near parabolic period-two segments. They do **not** assert an exact constant for correlations of general observables.

## Assumptions and scope

The map is defined modulo one on the unit torus, and its values on branch boundaries can be chosen by the displayed half-open convention. These boundaries and all iterated preimages relevant to a fixed finite survival test have zero Lebesgue area, so no area formula depends on a different boundary convention. Every quantifier above is for the single symmetric orthogonal tents map (both tent slopes equal to \(\pm2\)), not a parameter neighborhood. A survivor at time \(n\) means membership at indices \(0,1,\ldots,n-1\), not at index \(n\). The first-exit time has values in the positive integers or infinity. All measures are two-dimensional normalized Lebesgue area.

## Proof

**1. A parabolic two-step coordinate.**  Inside \(A_3\), the horizontal shear uses slope \(-2\) and the vertical shear uses slope \(+2\), hence
\[
(x',y')=(\{x-2y\},\{y+2x'\}),\qquad
DH|_{A_3}=\begin{pmatrix}1&-2\\2&-3\end{pmatrix}.
\]
Write \(d=\{x-y\}\). Whenever the current point belongs to \(A_3\), the next difference is \(d'\equiv-d\pmod1\) and \(x'\equiv-x+2d\pmod1\). Consequently, as long as the itinerary stays inside \(A_3\), its even-indexed first coordinates satisfy
\[
x_{2k}\equiv x_0-4kd\pmod1,\qquad d_{2k}=d.
\]
The change from \((x,y)\) to \((x,d)\) preserves normalized torus area.

**2. All admissible two-step pairs.**  Let \(E_d\) be the circular subset of \(x\in[0,1)\) for which both \((x,\{x-d\})\) and its first image lie in \(A_3\). Apart from boundary points of zero area, the four conditions are
\[
\{x-d\}\ge\tfrac12,\quad \{-x+2d\}<\tfrac12,\quad
\{-x+3d\}\ge\tfrac12,\quad \{x-4d\}<\tfrac12.
\]
Equivalently these are the intersection, modulo one, of four semicircular intervals whose respective left endpoints and lengths are
\[
(d+\tfrac12,\tfrac12),\quad(2d+\tfrac12,\tfrac12),\quad
(3d,\tfrac12),\quad(4d,\tfrac12).
\]
(The last two intervals are right-oriented; the other two follow from reversing the fractional-part inequalities.) Unfolding those four intervals at their endpoints gives precisely the following single circular interval \(E_d\) for each \(d\) range:
\[
\begin{array}{c|c|c}
\text{range of }d& E_d\text{ as an oriented circular interval}&e(d)=|E_d|\\\hline
0<d<\tfrac14 &[\tfrac12+2d,\tfrac12+3d]&d\\
\tfrac14<d<\tfrac13 &[4d-1,d]&1-3d\\
\tfrac13<d<\tfrac23 &\varnothing&0\\
\tfrac23<d<\tfrac34 &[d-\tfrac12,4d-\tfrac52]&3d-2\\
\tfrac34<d<1 &[3d-2,2d-1]&1-d
\end{array}
\]
An interval in this table is understood modulo one, so an interval with a right endpoint greater than one wraps across zero. For completeness, the elementary unfolding can be checked directly by starting with \([d+\tfrac12,d+1]\cap[2d+\tfrac12,2d+1]\) modulo one and cutting it with \([3d,3d+\tfrac12]\) and \([4d,4d+\tfrac12]\); the only changes in endpoint order are at \(d=\tfrac14,\tfrac13,\tfrac23,\tfrac34\). In particular \(0\le e(d)\le\tfrac14\) everywhere. Integrating the two pairs of triangular profiles yields
\[
\mu(S_2)=\int_0^1e(d)\,\mathrm dd
=2\left(\tfrac1{32}+\tfrac1{96}\right)=\tfrac1{12}.
\]

**3. Every long pairwise survivor.** For an integer \(m\ge2\), survival for \(2m\) consecutive visits is equivalent to
\[
x_0-4kd\pmod1\ \in E_d,\qquad k=0,1,\ldots,m-1.
\]
Because \(E_d\) is one circular arc of length at most \(\tfrac14\), two consecutive members of that orbit can belong to it only if the circle distance from \(4d\) to the nearest integer is at most \(e(d)\). Thus \(d\) must lie within \(\tfrac1{16}\) of some multiple of \(\tfrac14\). The neighborhoods of \(0\) and \(1\) give \(e(d)=\min(d,1-d)\), strictly smaller than the corresponding shift length \(4\min(d,1-d)\); the neighborhood of \(\tfrac12\) has empty \(E_d\). Therefore all positive-area survivors have \(d\) near \(\tfrac14\) or \(\tfrac34\), where the signed lift of the two-step rotation is \(-4(d-d_0)\) for the relevant center \(d_0\). The circular arc cannot wrap under this signed lift while all visits stay in it, so its \(m\)-fold overlap has length
\[
\bigl[e(d)-4(m-1)|d-d_0|\bigr]_+,\qquad [t]_+=\max(0,t).
\]
At \(d=\tfrac14-\varepsilon\) and \(d=\tfrac34+\varepsilon\), this length is \([\tfrac14-(4m-3)\varepsilon]_+\). At \(d=\tfrac14+\varepsilon\) and \(d=\tfrac34-\varepsilon\), it is \([\tfrac14-(4m-1)\varepsilon]_+\). Each supporting \(\varepsilon\)-interval lies strictly inside the neighborhood where that formula was derived. Since
\[
\int_0^\infty [\tfrac14-a\varepsilon]_+\,\mathrm d\varepsilon=\frac1{32a}\qquad(a>0),
\]
adding the four contributions proves, for every integer \(m\ge2\),
\[
\mu(S_{2m})=2\left(\frac1{32(4m-3)}+\frac1{32(4m-1)}\right)
=\frac{2m-1}{4(4m-3)(4m-1)}.
\]

**4. All-time tail and infinite conditional mean.**  We have \(S_{n+1}\subseteq S_n\) and the even-time formula gives \(2m\mu(S_{2m})\to\tfrac1{16}\). Squeezing \(\mu(S_{2m+1})\) between consecutive even-time values gives \(n\mu(S_n)\to\tfrac1{16}\) for all integer times. Since \(F\) preserves Lebesgue area and its target square \([0,\tfrac12)\times[\tfrac12,1)\) has area \(\tfrac14\), \(\mu(A_3)=\tfrac14\). Hence for a uniform initial point in \(A_3\), \(\Pr(\tau>n)=4\mu(S_{n+1})\sim1/(4n)\). This tends to zero, proving almost-sure exit; the tail-sum identity for a positive integer-valued random variable gives \(\mathbb E[\tau]=\sum_{n\ge0}\Pr(\tau>n)=\infty\).

## Verification

A standalone exact-rational checker is included as `verify_orthogonal_tent.py`. It reconstructs the four-inequality pair test and compares it with the five-row circular-interval table at 18,224 nonboundary rational pairs, checks up to six consecutive even-time pairs, and verifies the four-triangle integration identities for \(2\le m\le29\). Its reported result is:

`ORTHOGONAL_TENTS_EXACT_PAIR_INTERVALS_AND_SURVIVORS_OK grid= 18224`

`ORTHOGONAL_TENTS_EXACT_SURVIVOR_AREA_OK m=2..29 S4= 3/140  S6= 5/396`

These are finite consistency and arithmetic checks, not a replacement for the all-integer proof above. The proof's interval decomposition and integration are independent of floating-point approximations.

## Relationship to prior work

Myers Hill, Sturman and Wilson, *Loss of Exponential Mixing in a Non-Monotonic Toral Map* (first arXiv posting 15 March 2023; arXiv:2303.08515, Sections 1, 3, 6, 7) define this map and its parabolic branch decomposition, show that almost every point eventually leaves a parabolic branch, and prove an \(O(n^{-1})\) correlation bound. They describe polygonal escape cells and triangular wedges but do not state the present complete exact even-time **initial-branch** area formula or its leading coefficient. Their return-to-induced-base cells \(M_m\) are distinct objects from the unconditioned full-branch survivor \(S_n\) here; the two should not be conflated.

The earlier *Exponential mixing by orthogonal non-monotonic shears* (Physica D 434, 2022) treats open parameter regimes and explicitly identifies exceptional cusp behavior. *A Family of Non-Monotonic Toral Mixing Maps* (Journal of Nonlinear Science 32, 2022) studies a related family of shears. Neither inspected result gives a complete survival distribution for this cusp branch. Related exact escape laws on other maps have different domains, branch geometries, and claims.

## Limitations

The formula applies only to the specific parabolic branch \(A_3\) of the symmetric orthogonal tents map, not to return times to an induced tower base or to arbitrary perturbations. Odd-time survivor **areas** are controlled asymptotically by monotonicity; no exact odd-time formula is asserted. The infinite conditional mean is for the branch first-exit time, not an infinite mean correlation time or a general limit theorem. Direct search cannot rule out every unpublished or unindexed equivalent calculation. No independent audit has been performed.

## References

1. J. Myers Hill, R. Sturman, M. C. T. Wilson, *Loss of Exponential Mixing in a Non-Monotonic Toral Map*, arXiv:2303.08515 (first public version dated 2023-03-15; v2 dated 2023-12-14), especially Sections 1, 3, 6, 7 and the Appendix. https://arxiv.org/abs/2303.08515
2. J. Myers Hill, R. Sturman, M. C. T. Wilson, *Exponential mixing by orthogonal non-monotonic shears*, Physica D 434 (2022), 133224, DOI:10.1016/j.physd.2022.133224.
3. J. Myers Hill, R. Sturman, M. C. T. Wilson, *A Family of Non-Monotonic Toral Mixing Maps*, Journal of Nonlinear Science 32 (2022), article 31, DOI:10.1007/s00332-022-09790-0.
