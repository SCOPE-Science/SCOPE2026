# A sharp parity law for Lipschitz approximation of a twofold circle-cover average

## Finding
For the connected twofold metric circle covering \(q:Y\to X\), the least equal-weight \(m\)-composition approximation error of fiber averaging, measured on real Lipschitz test functions, is
\[
E_m=\min_{h_1,\ldots,h_m\in C(X,Y)}\left\|A_q-\frac1m\sum_{j=1}^m C_{h_j}\right\|_{\operatorname{Lip}(Y)/\mathbb R\to C(X)}
=\begin{cases}\frac1{2m},&m\text{ odd},\\ \frac1m,&m\text{ even}.\end{cases}
\]
Here the target operator annihilates constants, so the operator norm on the Lipschitz quotient is well-defined. All minima are attained by explicit piecewise-linear maps. In particular, the scaled error \(mE_m\) has distinct limits \(1/2\) and \(1\) along odd and even integers; the exact error is not monotone as a function of the prescribed number of equally weighted terms.

## Assumptions and scope
Use the quotient circles \(X=\mathbb R/\mathbb Z\) (circumference one) and \(Y=\mathbb R/(2\mathbb Z)\) (circumference two). Each is endowed with intrinsic geodesic distance; thus the two points in every fiber \(q^{-1}(x)=\{x,x+1\}\) have distance exactly one. Define
\[
A_qf(x)=\frac{f(x)+f(x+1)}2,\qquad C_hf=f\circ h.
\]
The domain \(\operatorname{Lip}(Y;\mathbb R)/\mathbb R\) is the real vector space of Lipschitz functions modulo constants, with norm \(\|f\|=\sup_{u\ne v}|f(u)-f(v)|/d_Y(u,v)\). Only the difference \(A_q-m^{-1}\sum_jC_{h_j}\) is viewed as an operator from this quotient; \(A_q\) and \(C_h\) separately need not descend to the quotient. The codomain is \(C(X;\mathbb R)\) with supremum norm. Each \(h_j\) is merely continuous, not required to be Lipschitz. Repetitions are allowed. The symbol \(m\) is an arbitrary positive integer; the number of terms is exactly \(m\), with every coefficient fixed to \(1/m\). No assertion is made for unrestricted convex weights or for general graph coverings.

## Proof
**1. Transport reduction.** For each \(x\in X\) and continuous tuple \(h=(h_j)\), write
\[
\mu_x=\tfrac12(\delta_x+\delta_{x+1}),\quad \nu_x=\tfrac1m\sum_{j=1}^m\delta_{h_j(x)}.
\]
Kantorovich--Rubinstein duality on compact metric spaces gives
\[
\left\|A_q-\tfrac1m\sum_j C_{h_j}\right\|=\max_{x\in X}W_1(\mu_x,\nu_x).
\]
The equality of the operator norm and the maximum follows by interchanging two suprema; continuity on the compact base yields the maximum. Translation by \(-x\) on \(Y\) reduces each fiber to the antipodal sites \(0\) and \(1\).

**2. Odd-number lower bound.** Write \(m=2k+1\). For any \(m\) destination points \(y_j\) in \(Y\), a transport coupling from \(\frac12(\delta_0+\delta_1)\) to \(m^{-1}\sum_j\delta_{y_j}\) sends \(t_j\in[0,1/m]\) of the first source's mass to destination \(j\), and the remaining \(1/m-t_j\) from the second. Necessarily \(\sum_jt_j=1/2\). The triangle inequality \(d_Y(0,y_j)+d_Y(1,y_j)\ge1\) gives
\[
 t_jd_Y(0,y_j)+(1/m-t_j)d_Y(1,y_j)
 \ge\min\{t_j,1/m-t_j\}.
\]
Since \(\sum_j mt_j=m/2\) is a half-integer, and the distance to the nearest integer is subadditive, \(\sum_j\min\{mt_j,1-mt_j\}\ge1/2\). Thus every coupling has cost at least \(1/(2m)\), at every base point.

**3. Even-number lower bound (topology).** Write \(m=2k\). At fixed \(x\), the two source masses \(1/2\) can be represented by \(k\) identical atoms of mass \(1/m\) at each fiber site. By the finite assignment principle (a linear transport problem with equal atom masses), an optimal \(W_1\) coupling can be chosen as a perfect matching between the \(m\) labeled destinations and this multiset of targets. Suppose \(W_1(\mu_x,\nu_x)<1/m\). Then the minimum total matching distance is less than one. Any two different assignments of destination labels to the two **fiber sites**, both of total distance less than one, must disagree at a minimum of two labels, because both assign exactly \(k\) labels to each site. For each disagreement the triangle inequality gives a sum of the two corresponding distances at least the fiber separation one. Summing over two disagreements, the two matching costs would add to at least two, contradicting their individual strict bounds below one. Hence the optimal assignment of each labeled destination to a fiber site is unique.

If a continuous tuple \(h_j\) had operator error strictly less than \(1/m\), the unique assignment would persist locally as \(x\) varies: in a local trivialization of the cover there are finitely many continuous matching-cost functions and a unique strict minimizer. Consequently, assigning to any fixed index \(j\) its optimally matched target would define a global continuous section \(a_j:X\to Y\) with \(q\circ a_j=\operatorname{id}_X\). Such a section cannot exist: on fundamental groups the map \(q\) multiplies degree by two, so \(2\deg(a_j)=1\) would be required. Thus the global error is at least \(1/m\). This argument uses strict inequality to prove the sharp weak bound; it does **not** assert a unique matching at the equality threshold.

**4. Attaining both bounds.** Parameterize \(X\) by \(t\in[0,1]\) with endpoints identified. Each map is written \(h_j(t)=t+r_j(t)\pmod2\), where the real piecewise-linear relative coordinate satisfies \(r_j(1)=r_j(0)-1\); therefore \(h_j(1)=h_j(0)\) modulo two and it defines a continuous circle map. All motion intervals may be chosen disjoint except for paired simultaneous motion described below.

For \(m=2k+1\), initially place \(k+1\) relative atoms at \(0\) and \(k\) at \(1\). Move them **one at a time**, in alternating order starting with a \(0\)-atom and ending with the last \(0\)-atom. Each moves by displacement \(-1\), traveling along the length-one geodesic to the opposite fiber site. At every intermediate point exactly \(k\) stationary atoms occupy each fiber site and one atom occupies a point \(y\) on a length-one geodesic between the sites. Transport \(k/m\) source mass at each site directly to the stationary atoms and the remaining \(1/(2m)\) from each site to \(y\). Its cost is
\[
\frac{d_Y(0,y)+d_Y(1,y)}{2m}=\frac1{2m}.
\]
This also covers \(m=1\). The pointwise lower bound in step 2 proves equality.

For \(m=2k\), start with \(k\) pairs, one atom at each of \(0,1\). Move the pairs one after another. In the active pair, both relative atoms make the same displacement \(-s\) with \(s\in[0,1]\), so their locations are \(-s,1-s\) modulo two. The remaining \(k-1\) pairs stay at their own fiber sites (including completed pairs, whose two positions are swapped). Match each moving atom with its initial fiber for \(s\le1/2\), or with the opposite fiber for \(s\ge1/2\). The resulting transport cost is at most
\[
\frac2m\min\{s,1-s\}\le\frac1m.
\]
At the midpoint of a moving pair the cost equals \(1/m\), consistent with step 3. At completion every relative atom has moved by exactly \(-1\), ensuring continuity across \(t=0\) and \(t=1\). The even bound is attained. These are explicit finite piecewise-linear constructions for every \(m\ge1\).

## Verification
A standalone Python 3 standard-library program, `check_wasserstein_double_cover.py`, implements the two constructions with exact rational arithmetic, calculates the two-source optimal transport cost by sorting the transportation linear program's reduced costs, checks endpoint closures and verifies the asserted sharp bound for every integer \(1\le m\le20\) over the grid of \(8\cdot17m+1\) equally spaced times. It reports `DOUBLE_COVER_W1_EXACT_RATIONAL_OK 28810`. This finite diagnostic is not the proof of the all-integer assertion; steps 1--4 above are the proof. Reproduce with `python3 check_wasserstein_double_cover.py`.

## Relationship to prior work
Duru, İlter and Bilgin (2026), Theorems 1.1--1.2, prove exact **total-variation / supremum-to-supremum operator** distances for connected graph-cover averaging. For degree two and equally weighted \(m\) terms their operator distance is \(2/m\) for both parities. This does not determine the present **geodesic Wasserstein-one / Lipschitz-to-supremum operator** distance: the metric-sensitive error is \(1/(2m)\) for odd \(m\) but \(1/m\) for even \(m\), so even its scaled-error convergence differs. Their construction permits arbitrary paths and controls missing mass, whereas the present argument uses the length of the two-sheet geodesic and a unique-matching section obstruction. Classical empirical Wasserstein quantization results concern pointwise measures without this global continuous-selection requirement. The present exact constants were not located in the checked literature; lack of a hit alone is not proof of priority.

## Limitations
The result assumes the intrinsic metric on a circle of circumference two and the connected twofold covering of a circle of circumference one. Changing the metric, using other covering graphs, replacing the test norm by a full bounded-Lipschitz norm, allowing unrestricted mixing weights or imposing a Lipschitz constant on each \(h_j\) may change the answer. The continuous maps constructed have finite but \(m\)-dependent slopes; no regularity-uniform approximation claim is made. No independent verification of the claimed novelty has been performed.

## References
1. H. Duru, S. İlter, A. Bilgin, *Sharp Norm Approximation of Covering Markov Operators*, arXiv:2610.35575v1, first posted 2026-10-26, Theorems 1.1--1.2, Sections 2--6, https://arxiv.org/abs/2610.35575 .
2. C. Sommerfeld and A. Munk, *Inference for Empirical Wasserstein Distances on Finite Spaces*, *Journal of the Royal Statistical Society: Series B* 80 (2018), 219--238, https://academic.oup.com/jrsssb/article/80/1/219/7048419 .
3. Kantorovich--Rubinstein duality and the Birkhoff--von Neumann assignment principle are used in their standard finite/compact metric forms; both reductions are explicit in the proof.
