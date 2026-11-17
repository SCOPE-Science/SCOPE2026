# Exact Euclidean inballs and complete facet-rank phases of generalized parking-function polytopes

## Finding
For every integer \(n\ge2\) and every positive integer vector \(\mathbf b=(b_1,\ldots,b_n)\), let \(\mathfrak X_n(\mathbf b)\) be the convex hull of the \(\mathbf b\)-parking functions in the standard Euclidean space \(\mathbb R^n\). Put
\[
S_j=\sum_{i=1}^j b_i,\qquad A_k=\sum_{j=n-k+1}^{n}(S_j-1),\qquad
r_k=\frac{A_k}{k+\sqrt{k}}\quad(1\le k\le n).
\]
Then the **largest Euclidean inscribed-ball radius** and its **unique center** are
\[
\boxed{\ r_{\mathrm{in}}(\mathfrak X_n(\mathbf b))=\min_{1\le k\le n}r_k,\qquad
c_{\mathrm{in}}=(1+r_{\mathrm{in}})\mathbf1.\ }
\]
Write \(\mathcal K=\{k:r_k=r_{\mathrm{in}}\}\). The ball touches all \(n\) lower-coordinate facets \(x_i=1\), and touches exactly the upper facets
\[
\sum_{i\in I}x_i=\sum_{j=n-|I|+1}^{n}S_j
\quad\text{for nonempty }I\subseteq[n]\text{ with }|I|\in\mathcal K.
\]
In particular, the exact number of supporting facets of its insphere is
\[
\boxed{n+\sum_{k\in\mathcal K}\binom{n}{k}.}
\]
If \(b_1=1\), the nominal \((n-1)\)-subset inequalities are redundant, but \(n-1\notin\mathcal K\), so this count is still correct.

**Every rank is an actual, robust metric phase.** For every \(n\ge2\) and \(k\in\{1,\ldots,n\}\), there exist positive integer parameters \(\mathbf b\) for which \(\mathcal K=\{k\}\). In fact those parameters can be chosen in an open region of the strictly increasing cumulative-sum parameter space. Thus, unlike the two-parameter subfamily \(\mathbf b=(a,b,b,\ldots,b)\), for which only ranks \(1\) and \(n\) can control the insphere, the fully general family realizes **each intermediate facet rank as the unique touching upper orbit**.

For a small explicit witness, take \(n=3\), \(\mathbf b=(69,1,31)\). Its three candidate radii are
\[
(r_1,r_2,r_3)=\left(50,\ \frac{169}{2+\sqrt2},\ \frac{237}{3+\sqrt3}\right),
\]
and the middle value is strictly the least. Its unique insphere therefore touches the three lower-coordinate facets and all three pair-sum facets, but no singleton upper facet or full-sum facet.

## Assumptions and scope
A \(\mathbf b\)-parking function is a positive integer vector whose nondecreasing rearrangement \(\beta'_1\le\cdots\le\beta'_n\) satisfies \(\beta'_j\le S_j\) for every \(j\). The body \(\mathfrak X_n(\mathbf b)\) is full-dimensional for \(n\ge2\). The norm and hyperplane distances are the ordinary, unscaled Euclidean ones in the stated coordinate realization, not an intrinsic metric after a nonorthogonal lattice equivalence.

The source's complete facet theorem (Bayer et al., Theorem 2.3(c)) states that the polytope is exactly
\[
\biggl\{x\in\mathbb R^n:x_i\ge1\ (1\le i\le n),\quad
\sum_{i\in I}x_i\le \sum_{j=n-|I|+1}^n S_j\ (\varnothing\ne I\subseteq[n])\biggr\}.
\]
It also specifies the sole redundant upper rank, \(n-1\), when \(b_1=1\). The proof below uses this full description as its sole non-elementary input.

## Proof
**1. Universal upper bound.** If a ball of radius \(\rho\ge0\) with center \(z\) is contained in the polytope, every lower facet gives \(z_i\ge1+\rho\). Every upper supporting hyperplane indexed by a set \(I\) of size \(k\) has outward normal \(\mathbf1_I\) of norm \(\sqrt{k}\), so it gives
\[
\sum_{i\in I}z_i+\rho\sqrt{k}\le\sum_{j=n-k+1}^{n}S_j.
\]
Consequently \(k(1+\rho)+\rho\sqrt{k}\le\sum_{j=n-k+1}^{n}S_j\), and thus \(\rho\le r_k\) for every rank \(k\). For the possibly redundant rank \(n-1\) this is still a valid inequality. It follows that \(\rho\le r_*:=\min_k r_k\).

**2. Attainment.** Set \(z_*=(1+r_*)\mathbf1\). The lower-coordinate distances to their supporting hyperplanes are exactly \(r_*\); the upper distances at rank \(k\) are
\[
\frac{\sum_{j=n-k+1}^n S_j-k(1+r_*)}{\sqrt{k}}\ge r_*
\]
because \(r_*\le r_k\). Therefore the radius-\(r_*\) ball about \(z_*\) lies inside every defining halfspace, hence inside the polytope. This proves the radius and center assertions.

**3. Uniqueness and exact contacts.** Choose any minimizing rank \(k\in\mathcal K\). Any radius-\(r_*\) center \(z\) satisfies \(z_i\ge1+r_*\), while every upper rank-\(k\) inequality forces
\[
\sum_{i\in I}z_i\le \sum_{j=n-k+1}^n S_j-r_*\sqrt{k}=k(1+r_*)
\]
for each \(k\)-element subset \(I\). The sum of \(k\) entries already bounded below by \(1+r_*\) each cannot be at most this value unless those entries all equal \(1+r_*\). Every coordinate lies in some \(k\)-subset, so \(z=z_*\). At this unique center, an upper rank-\(k\) support is tangent if and only if \(r_k=r_*\), and all rank-\(k\) subsets give distinct facets whenever that rank is minimizing. If \(b_1=1\), then \(S_1-1=0\) implies \(A_n=A_{n-1}\), while \(n+\sqrt n>n-1+\sqrt{n-1}\), hence \(r_n<r_{n-1}\). Thus the sole redundant rank is never active. This proves the contact-count formula.

**4. Realization of every upper rank.** Fix \(n\ge2\) and a target integer \(1\le k\le n\). Consider initially the positive nondecreasing real increment sequence
\[
w_0=\cdots=w_{n-2}=1,\qquad w_{n-1}=1+c,\qquad
c=\frac{k}{2\sqrt{k}+1}>0.
\]
These are the translated cumulative sums \(w_j=S_{j+1}-1\) in a limiting, not necessarily integral, realization. In this limit \(A_s=s+c\) for each \(1\le s\le n\), so the rank objective is
\[
g_c(s)=\frac{s+c}{s+\sqrt{s}}.
\]
Writing \(u=\sqrt{s}>0\), direct differentiation shows that the sign of \(d g_c(u^2)/du\) is the sign of
\[
u^2-c(2u+1).
\]
This expression has exactly one positive zero, at \(u=\sqrt{k}\), because \(c=k/(2\sqrt{k}+1)\); it is negative before and positive after that zero. Therefore \(g_c(s)\) has a **unique strict global minimum** at the real argument \(s=k\), and in particular a strict minimum over all integers \(s\in\{1,\ldots,n\}\).

The finite list of strict inequalities persists under sufficiently small perturbations of \((w_0,\ldots,w_{n-1})\). Perturb the repeated first \(n-1\) entries to be strictly increasing, keep the final jump positive, and approximate all entries by positive rationals while preserving these inequalities. A common positive integer scaling makes the resulting \(w_j\) integral and strictly increasing. Setting
\[
b_1=w_0+1,\qquad b_i=w_{i-1}-w_{i-2}\quad(2\le i\le n)
\]
then gives an honest positive integer vector with exactly \(\mathcal K=\{k\}\). The strict inequalities also show that the phase has an open neighborhood in the real cumulative-parameter space; integer realizations are produced by rational approximation followed by scaling. All rank phases are therefore genuine, not artifacts of ties or degenerations.

The displayed three-dimensional example follows by direct comparison of its three radical expressions.

## Verification
The bundled `verify.py` explicitly constructs the original defining-halfspace system (all subsets, not merely diagonal centers) and independently solves its Chebyshev linear program. It tests 121 parameter cases, including integer witnesses for every upper active rank in dimensions \(2\) through \(6\), ordinary two-parameter families, and the explicit three-dimensional example. It also confirms uniqueness numerically via recovered centers. The completed execution printed `ARBITRARY_PARKING_INBALL_CHECKS_PASSED trials=121 distinct_rank_phase_witnesses=20`.

Run `python -m pip install -r requirements.txt` followed by `python verify.py`. The code requires NumPy and SciPy, specified in `requirements.txt`. These finite numerical checks support, but do not replace, the analytic all-dimensional proof; the exact existence argument for integral parameters is in Step 4.

## Relationship to prior work
Bayer, Borgwardt, Chambers, Daugherty, Dawkins, Deligeorgaki, Liao, McAllister, Morrison, Nelson, and Vindas-Meléndez established the full arbitrary-positive-parameter vertex and facet description in arXiv:2403.07387 (Theorem 2.3). They also studied generalized-permutahedron representations, combinatorial types, and graph/circuit diameters, **not** the Euclidean inball or its contact ranks. That facet theorem is explicitly assumed above, rather than claimed anew.

Hanada, Lentfer, and Vindas-Meléndez treated \(\mathbf b=(a,b,b,\ldots,b)\) in arXiv:2212.06885. A subsequent published calculation determines the exact inball in that **two-parameter** subfamily and proves a two-phase law: only upper cardinalities \(1\) and \(n\) can be tangent. This is consistent with, but does not imply, the new arbitrary-parameter phase-realization assertion; in particular it cannot produce any intermediate unique active rank.

The later generalization of parking-function polytopes by Liu and Thawinrak (arXiv:2512.14199) addresses normal fans, face posets, and enumeration. Its inspected full-text sections do not state an inradius, Chebyshev-center, or tangent-orbit classification. Generic finite-halfspace Chebyshev linear programming supplies an algorithm to evaluate the inball, but neither an explicit all-parameter formula nor the existence of every rank phase without the present argument.

## Limitations
The novelty claim is **not** a new description of vertices or facets, not an algorithmic invention of Chebyshev linear programming, and not a new proof of the already established two-parameter endpoint phase law. It is the all-parameter exact metric formula, unique-center/contact classification, and in particular the all-rank realization theorem.

The result concerns the standard-coordinate Euclidean norm and \(n\ge2\), not lattice-invariant radii, John ellipsoids, general nonsymmetric polymatroids, or continuous-volume covariance. The finite checker has ordinary floating-point optimization tolerances and is not a formal proof; a hidden equivalent treatment of symmetric cardinality-polymatroid inballs could cover the formula, although the full rank-realization claim was not found in the inspected sources.

## References
1. Margaret M. Bayer et al., *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387, first public version 2024-03-12, Theorem 2.3; DOI 10.1007/s00454-025-00770-1.
2. Mitsuki Hanada, John Lentfer, and Andrés R. Vindas-Meléndez, *Generalized parking function polytopes*, arXiv:2212.06885, first public version 2022-12-13, Proposition 3.6; DOI 10.1007/s00026-023-00671-1.
3. Fu Liu and Warut Thawinrak, *Parking Function Polytopes*, arXiv:2512.14199, first public version 2025-12-16 (broader structural comparison).
4. *Generalized parking-function polytopes have a two-phase Euclidean inball*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-generalized-parking-function-polytopes-have-a-two-phase-euclidea--53d2c657716a/RESULT.md (two-parameter comparison only).
