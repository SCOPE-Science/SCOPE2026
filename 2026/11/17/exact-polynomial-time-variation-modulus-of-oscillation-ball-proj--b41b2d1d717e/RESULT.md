# Exact polynomial-time variation modulus of oscillation-ball projection

## Finding

For every integer \(n\ge2\) and radius \(R>0\), let \(P_{n,R}\) be the Euclidean projector onto the bounded-oscillation set
\[
K_{n,R}=\{z\in\mathbb R^n:\max_i z_i-\min_i z_i\le R\},
\qquad V_n(z)=\sum_{i=1}^{n-1}|z_{i+1}-z_i|.
\]
The optimal **two-input** path-variation Lipschitz coefficient
\[
C_n=\sup_{V_n(x-y)>0}\frac{V_n(P_{n,R}x-P_{n,R}y)}{V_n(x-y)}
\]
is independent of \(R\), is attained by distinct finite inputs, and has the following exact integer-arithmetic formula, requiring \(O(n^3)\) arithmetic operations and no enumeration of active subsets.

For integers \(m\ge1\), \(0\le k\le m\), and \(z\in\{0,1\}\), define
\[
E_0(m,k)=\min\{m-1,2k,2(m-k)-1\},\qquad
E_1(m,k)=\min\{m-1,2(m-k),2k-1\}.
\]
Exclude infeasible cases \(E_0(m,m)\) and \(E_1(m,0)\). For \(a,b\ge1\) and \(z,w\in\{0,1\}\), put
\[
B_{z,w}(a,b)=\begin{cases}a+b&(z,w)=(0,0),\\a&(z,w)=(1,0),\\b&(z,w)=(0,1),\\0&(z,w)=(1,1).\end{cases}
\]
Then the exact modulus is
\[
\boxed{C_n=\max\!\left\{1,\ 
\max_{\substack{1\le t<n,\ 1\le a\le t,\ 1\le b\le n-t\\z,w\in\{0,1\}\ \mathrm{feasible}}}
\frac{bE_z(t,a)+aE_w(n-t,b)+B_{z,w}(a,b)}{a+b}\right\}.}
\]
For all dimensions,
\[
\boxed{\left\lfloor\frac n2\right\rfloor\le C_n\le 1+\left\lfloor\frac{2n}{3}\right\rfloor.}
\]
In particular, \(C_n=\Theta(n)\): range-constrained Euclidean projection can have linearly increasing variation sensitivity although it is nonexpansive in Euclidean norm. The first expansive dimension is \(n=4\). Exact values for dimensions \(2\) through \(16\) are respectively
\[
1,\ 1,\ 2,\ \frac52,\ 3,\ \frac{10}3,\ 4,\ \frac92,\ 5,\ \frac{27}5,\ 6,\ \frac{13}2,\ 7,\ \frac{52}7,\ 8.
\]

## Assumptions and scope

All observations are real, sample locations are a nonperiodic path of length \(n\), projection uses equally weighted Euclidean squared distance, and \(R>0\) is fixed for both inputs. Variation is a seminorm on vectors modulo constants; only input pairs with positive variation difference enter the ratio. The max in the displayed expression ranges over feasible integer indices and has finitely many terms. The statement does not assert a simpler closed form for every \(n\).

## Proof

**1. Projection chambers.** A vector lies in \(K_{n,R}\) precisely when all its coordinates fit inside some interval \([c,c+R]\). For each fixed \(c\), the least-squares fit clips every input coordinate to that interval. Hence minimizing the resulting one-variable convex piecewise-quadratic function gives the projector. If the input range is at most \(R\), the projection is the identity. Otherwise, in a strict clipping chamber let \(L\) and \(U\) denote coordinates clipped at the lower and upper endpoints, and \(S=L\cup U\); both \(L\) and \(U\) are nonempty. The derivative with respect to the input is the averaging projector \(A_S\): it replaces all coordinates in \(S\) by their arithmetic mean and leaves the other coordinates unchanged. Indeed, differentiating the first-order equation gives \(dc=|S|^{-1}\sum_{i\in S}dx_i\). There are finitely many polyhedral chambers; continuity and integration along line segments show that the global variation Lipschitz coefficient is at most the largest variation operator norm among these \(A_S\) and the identity.

**2. All active subsets are realized.** Given any proper or full subset \(S\) of size at least two and any partition \(S=L\sqcup U\) into nonempty parts, set the intended clipping endpoints to zero and one, let all coordinates outside \(S\) be one half, every lower coordinate be \(-|U|\), and every upper coordinate be \(1+|L|\). The first-order equation holds, and all clip statuses are strict. This realizes a full-dimensional chamber with derivative \(A_S\) when \(R=1\), and scaling realizes every \(R>0\). Thus the largest derivative norm equals the sharp global Lipschitz coefficient. A small nonzero perturbation inside the chamber attains the corresponding ratio, not just a limiting derivative.

**3. Reduction to a single jump.** Write \(h_t(i)=0\) for \(i\le t\) and \(h_t(i)=1\) for \(i>t\). Every \(v\in\mathbb R^n\) satisfies \(v=v_1\mathbf1+\sum_{t=1}^{n-1}(v_{t+1}-v_t)h_t\). Since \(A_S\) preserves constants, the triangle inequality implies \(\|A_S\|_{V\to V}=\max_t V_n(A_Sh_t)\). If \(S\) lies entirely on one side of the cut, this value is one. Otherwise let \(a=|S\cap[1,t]|\), \(b=|S\cap[t+1,n]|\), and \(s=a+b\). The image \(A_Sh_t\) equals \(b/s\) at selected coordinates, zero at unselected left coordinates, and one at unselected right coordinates.

**4. Exact binary-switch compression.** Let \(q_L\) and \(q_R\) count transitions between selected and unselected indices strictly inside the left and right pieces. Put \(z=1\) if the last left index is selected and \(w=1\) if the first right index is selected. The output variation is exactly
\[
V_n(A_Sh_t)=\frac{bq_L+aq_R+B_{z,w}(a,b)}{a+b}.
\]
For a binary word of length \(m\) with exactly \(k\) selected positions and specified last bit zero, the maximum number of adjacent switches is \(E_0(m,k)\). This follows from the three upper bounds: there are only \(m-1\) edges, every selected position can support at most two switches, and the unselected positions can support at most \(2(m-k)-1\) switches because the last position is unselected. Alternating the two symbols until the minority is exhausted, then grouping any surplus majority symbols, attains the minimum of the three bounds. Reversing zero and one gives \(E_1\). Reversal permits the same formulas when the **first** bit is fixed on the right side. The two sides can be optimized independently at fixed \(t,a,b,z,w\), giving exactly the displayed finite maximum. Its outer summation has \(\sum_{t=1}^{n-1}t(n-t)=O(n^3)\) pairs \((a,b)\), with only four endpoint statuses per pair.

**5. Growth, thresholds and attainment.** Every internal switch on the left can be charged to at most two selected left positions; similarly on the right. Consequently the internal variation is at most \(4ab/(a+b)\le a+b=s\). Charging switches instead to unselected endpoints gives at most \(2(n-s)\). The cross-cut jump is at most one. Thus \(C_n\le1+\max_{0\le s\le n}\min\{s,2(n-s)\}=1+\lfloor2n/3\rfloor\). For even \(n\ge4\), split the path into equal halves, select alternating positions on each half with the two cut-adjacent positions unselected and equal selection counts. Every internal edge then switches, the selected mean of \(h_t\) is one half, and the cross-cut jump is one. Therefore \(V(A_Sh_t)=n/2\). For odd \(n\ge5\), append an unselected right endpoint to the preceding even construction; variation cannot decrease, giving \(\lfloor n/2\rfloor\). For \(n=2\), the identity chamber gives the same lower bound. Substituting \(n=2,3,4\) in the exact finite formula gives \(1,1,2\), respectively. All maxima in the finite formula correspond to realized chambers by Step 2, so every \(C_n\) is attained by finite distinct input pairs.

## Verification

Run `python3 checker.py` from this package. The self-contained standard-library script independently enumerates all active subsets and single jumps through eleven sites, verifies the exact rational coefficient formula through sixteen sites, constructs strict clipping chambers and checks finite attaining input pairs using a separate exact scalar projection solver through twenty-one sites, and spot-checks the analytical growth inequalities through fifty-four sites. These computations corroborate the proof; the claims for arbitrary dimensions follow from the chamber and switch-count arguments, not extrapolation.

## Relationship to prior work

The projection/proximity theory of Combettes and Pesquet establishes Hilbert-space nonexpansivity, which does not imply nonexpansivity for the path-variation seminorm. Fadili and Peyré treat projection onto a **total-variation** ball; their feasible set uses a bound on the sum of adjacent differences rather than a bound on the global range. The present exact modulus concerns a distinct feasible set, with a different family of active averaging faces. Previously recorded finite-signal variation results for simplex projection, two-cell averaging and total-variation-ball projection do not provide this expression or the oscillation-ball attainment construction. This is a best-knowledge priority comparison, not a claim of exhaustive historical uniqueness.

## Limitations

The formula is an exact cubic-arithmetic computation rather than a simple closed expression in \(n\). The displayed linear upper and lower envelopes are proved, but neither is asserted to equal \(C_n\) for every dimension. Weighted Euclidean losses, cyclic variation, non-path graphs, and non-Euclidean projections are not covered. No independent mathematical validation is claimed.

## References

1. P. L. Combettes and J.-C. Pesquet, *Proximal Splitting Methods in Signal Processing*, arXiv:0912.3522, first publicly submitted 17 December 2009; see the projection and firm-nonexpansivity discussion in Section 2. https://arxiv.org/abs/0912.3522
2. J. M. Fadili and G. Peyré, *Total Variation Projection with First Order Schemes*, IEEE Transactions on Image Processing (2011), DOI:10.1109/TIP.2010.2072512, electronically published 2010. https://doi.org/10.1109/TIP.2010.2072512
