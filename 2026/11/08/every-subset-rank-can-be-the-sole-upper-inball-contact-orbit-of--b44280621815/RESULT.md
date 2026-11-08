# Every subset rank can be the sole upper inball-contact orbit of a generalized parking-function polytope

## Finding

Let \(n\ge2\) and \(\mathbf b=(b_1,\ldots,b_n)\in\mathbb Z_{>0}^{n}\). Put
\[
S_j=\sum_{i=1}^{j}b_i,\qquad H_k=\sum_{j=n-k+1}^{n}S_j\quad(1\le k\le n).
\]
Let \(P(\mathbf b)\subset\mathbb R^n\) be the convex hull of the integer vectors \(x\) with positive coordinates for which, writing \(x'_1\le\cdots\le x'_n\) for the nondecreasing rearrangement, \(x'_j\le S_j\) for all \(j\).

**Theorem (exact inball and all possible contact ranks).** In the standard Euclidean coordinate metric, set
\[
r_*(\mathbf b)=\min_{1\le k\le n}\frac{H_k-k}{k+\sqrt{k}},\qquad K(\mathbf b)=\left\{k:\frac{H_k-k}{k+\sqrt{k}}=r_*(\mathbf b)\right\}.
\]
Then \(r_*\) is the inradius of \(P(\mathbf b)\) and its **unique** incenter is \(c_*=(1+r_*)\mathbf1\). The insphere is tangent to each of the \(n\) facets \(x_i=1\), and precisely to the subset-sum facets
\[
\sum_{i\in I}x_i=H_{|I|}\quad\text{with}\quad |I|\in K(\mathbf b).
\]
Consequently the number of tangent facets is exactly
\[
n+\sum_{k\in K(\mathbf b)}\binom nk.
\]
For every prescribed \(n\ge2\) and \(1\le k\le n\) there is a positive-integer \(\mathbf b\) with \(b_1>1\) for which \(K(\mathbf b)=\{k\}\). Hence every upper-facet cardinality can uniquely control an inball; taking \(k=\lfloor n/2\rfloor\) gives exponentially many simultaneous contacts while the combinatorial type remains unchanged.

For example, with \(n=8\) and \(\mathbf b=(1001,1,1,1,1,1,1,500)\), one has \(H_2=2514\),
\[
r_*=\frac{2512}{2+\sqrt2}=735.747765659\ldots,\qquad K(\mathbf b)=\{2\}.
\]
Exactly \(8+\binom82=36\) facets touch the maximum inscribed ball.

## Assumptions and scope

All parameters are strictly positive integers, \(n\ge2\), and lengths are measured in the full ambient space \(\mathbb R^n\). The polytope is full-dimensional for this range. The case \(n=1=b_1\) is a point and is excluded. We use the exact complete inequality description of \(P(\mathbf b)\) from Bayer et al. [1], Theorem 2.3(c):
\[
x_i\ge1\ (i\in[n]),\qquad \sum_{i\in I}x_i\le H_{|I|}\quad(\varnothing\ne I\subseteq[n]).
\]
When \(b_1=1\), inequalities with \(|I|=n-1\) are redundant; the displayed full system still defines the same polytope.

## Proof

**Step 1 (Euclidean supporting distances).** At a diagonal point \(c=t\mathbf1\), the signed inward distance from the coordinate plane \(x_i=1\) is \(t-1\). For an upper plane indexed by a \(k\)-element set, the unit normal is \(\mathbf1_I/\sqrt k\), and the signed inward distance equals \((H_k-kt)/\sqrt k\). For an arbitrary center \(c\) and radius \(r\), the closed Euclidean ball \(c+rB_2^n\) lies in the polytope exactly when all these signed distances are at least \(r\).

**Step 2 (optimal radius and existence).** Given any feasible inscribed ball, permuting its center by every coordinate permutation preserves its radius and feasibility. Averaging the centers preserves all the linear containment inequalities, hence some optimal ball is centered at \(t\mathbf1\). Its radius must satisfy
\[
r\le t-1,\qquad kt+\sqrt k\,r\le H_k\quad(1\le k\le n).
\]
Eliminating \(t\ge1+r\) gives \(r(k+\sqrt k)\le H_k-k\). Therefore \(r\le r_*\). Conversely, the diagonal point \(c_*=(1+r_*)\mathbf1\) satisfies the lower bounds with equality and all the upper ball-containment bounds by the defining minimum; hence the radius \(r_*\) is attained. Every numerator \(H_k-k\) is positive for \(n\ge2\).

**Step 3 (uniqueness and exact tangencies).** Let \(c\) be any center of an inscribed ball of radius \(r_*\). Lower-coordinate containment forces \(c_i\ge1+r_*\) for every \(i\). Choose any minimizing \(k\) from the nonempty set \(K(\mathbf b)\). Every \(k\)-subset \(I\) satisfies
\[
\sum_{i\in I}c_i\le H_k-r_*\sqrt k=k(1+r_*).
\]
All summands are at least \(1+r_*\), so each is equal to this value. Every index belongs to a \(k\)-subset, hence \(c=c_*\). A lower-coordinate facet is tangent, and an upper \(k\)-subset plane is tangent precisely when its distance equals \(r_*\), equivalently \(k\in K(\mathbf b)\). The orthogonal foot is on the contained ball and thus on the polytope, so these are genuine facet contacts, not merely equalities for an external plane. If \(b_1=1\), then \(H_{n-1}=H_n-1\), implying \((H_{n-1}-(n-1))/(n-1+\sqrt{n-1})>(H_n-n)/(n+\sqrt n)\); thus no redundant size-\(n-1\) plane can be a contact. The facet count follows from Theorem 2.3(c) of [1].

**Step 4 (every facet rank occurs, even with fixed combinatorics).** Fix \(n\). Consider the functions
\[
f_k(\theta)=\frac{k+\theta}{k+\sqrt k}=v(t_k)+\theta u(t_k),\qquad t_k=\sqrt k,
\]
where \(u(t)=1/[t(t+1)]\) and \(v(t)=t/(t+1)\). As \(t\) increases, \(u(t)\) strictly decreases while \(v(t)\) strictly increases. Furthermore
\[
\frac{dv}{du}=-\frac{t^2}{2t+1},
\]
which increases strictly as \(u\) increases, proving that \(v\) is strictly convex as a function of \(u\). Hence the adjacent crossover values
\[
\theta_j=\frac{v(t_{j+1})-v(t_j)}{u(t_j)-u(t_{j+1})}\quad(1\le j<n)
\]
are positive and strictly increasing. For \(2\le k<n\), every choice \(\theta_{k-1}<\theta<\theta_k\) makes \(f_k(\theta)\) the unique minimum among \(f_1,\ldots,f_n\). For \(k=1\) choose \(0<\theta<\theta_1\); for \(k=n\) choose \(\theta>\theta_{n-1}\).

For large positive integer \(M\), take
\[
\mathbf b^{(M)}=(M+1,\underbrace{1,\ldots,1}_{n-2\text{ entries}},\max\{1,\lfloor M\theta\rfloor\}).
\]
For each fixed \(j\), the exact partial-sum calculation yields
\[
\frac{H_j(\mathbf b^{(M)})-j}{M}\longrightarrow j+\theta,
\]
so the ratios defining \(r_*/M\) converge to \(f_j(\theta)\). There are finitely many \(j\), and the chosen minimum is strict, so it persists for all sufficiently large \(M\). Thus \(K(\mathbf b^{(M)})=\{k\}\). The first parameter is \(M+1>1\); by [1], Corollary 3.14, all these polytopes are combinatorially equivalent to the stellohedron. This proves both realizability and the asserted contact-count phenomenon.

## Verification

Run `python general_parking_inball_checker.py` with Python, NumPy, and SciPy. The checker independently solves the Euclidean Chebyshev-center linear program over every subset-sum inequality for 150 seeded instances in dimensions 2 through 7, verifies the explicit eight-dimensional rank-two example, and constructs 104 instances realizing all individual facet ranks through dimension 14. Its successful marker is `GENERAL_PARKING_INBALL_CHECKS_PASSED`. These finite checks are illustrative only; Steps 1–4 provide the proof for all parameters.

## Relationship to prior work

Bayer, Borgwardt, Chambers, Daugherty, Dawkins, Deligeorgaki, Liao, McAllister, Morrison, Nelson, and Vindas-Meléndez [1] establish the full facet description and the two possible combinatorial types; these are explicit premises, not new claims. Hanada, Lentfer, and Vindas-Meléndez [2] study the restricted two-parameter family. The metric inball for that restricted family has also been treated separately in a published research record [5]. The present finding covers arbitrary positive-integer vectors and shows a qualitative behavior absent from the two-parameter theorem: every intermediate upper-facet cardinality can uniquely control the inball while the combinatorial type remains fixed. Liu and Thawinrak [3] develop normal fans and Ehrhart structure for a still broader class; Hill et al. [4] develop lattice-slice and Ehrhart properties. Their inspected results do not supply the metric formula or the all-ranks contact realization.

## Limitations

This statement concerns standard Euclidean distances in the original coordinates, not distances after a nonorthogonal affine equivalence. It does not classify *which combinations* of several upper-facet ranks can tie in one instance, nor study inball volumes or general real, nonstrict parameter sequences. The comparison with prior literature leaves a residual risk of an equivalent earlier formulation through symmetric polymatroid Chebyshev centers; historical priority awaits independent verification.

## References

[1] M. M. Bayer et al., *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387 (first posted 2024-03-12), Theorem 2.3 and Corollary 3.14. https://arxiv.org/abs/2403.07387

[2] M. Hanada, J. Lentfer, A. R. Vindas-Meléndez, *Generalized parking function polytopes*, arXiv:2212.06885 (first posted 2022-12-13). https://arxiv.org/abs/2212.06885

[3] F. Liu, W. Thawinrak, *Parking Function Polytopes*, arXiv:2512.14199 (first posted 2025-12-16). https://arxiv.org/abs/2512.14199

[4] C. Hill, A. Luo, V. Trinh, A. R. Vindas-Meléndez, *Lattice slices, Ehrhart polynomials, and magic positivity of generalized parking-function polytopes*, arXiv:2607.15503 (first posted 2026-07-16). https://arxiv.org/abs/2607.15503

[5] *Generalized parking-function polytopes have a two-phase Euclidean inball*, published research finding (2026-10-11), identifier `53d2c657716a`, concerning only the two-parameter family.
