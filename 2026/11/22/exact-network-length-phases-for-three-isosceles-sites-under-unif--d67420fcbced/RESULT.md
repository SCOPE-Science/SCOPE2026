# Exact network-length phases for three isosceles sites under uniform distance tolerance

## Finding

Let \(h>0\), and let the target set be the three planar sites
\[
M_h=\{(-1,0),(1,0),(0,h)\}.
\]
For every \(r\ge0\), define \(L_h(r)\) as the infimum of the one-dimensional Hausdorff length \(\mathcal H^1(\Sigma)\) over compact connected planar sets \(\Sigma\) satisfying \(\max_{v\in M_h}\operatorname{dist}(v,\Sigma)\le r\). This note gives an exact formula for \(L_h(r)\) and constructs a minimizer for every pair \((h,r)\).

Put
\[
c=1/\sqrt3,\qquad b=2/\sqrt3,\qquad
R(h)=\begin{cases}1,&0<h\le1,\\ (h^2+1)/(2h),&h>1.\end{cases}
\]
For \(r\ge R(h)\), \(L_h(r)=0\). For \(0\le r<R(h)\) set
\[
a_r=\sqrt{\max\{r^2-1,0\}},\qquad b_r=\max\{h-r,0\},\qquad
y_*=\min\{b_r,\max\{a_r,c\}\}.
\]
Then \(a_r\le b_r\) and
\[
\boxed{L_h(r)=(h-y_*-r)_++2\bigl(\sqrt{1+y_*^2}-r\bigr)_+,\qquad x_+=\max\{x,0\}.}
\]
In particular the formula reduces to the following **complete sharp phase portrait**, where adjacent formulas agree at the endpoints:

| Height domain | Radius interval below \(R(h)\) | Exact minimum length | A canonical minimizing shape |
| --- | --- | --- | --- |
| \(0<h\le c\) | \(0\le r\le h\) | \(2\sqrt{1+(h-r)^2}-2r\) | two arms meeting at the upper site's disk |
| \(0<h\le c\) | \(h\le r<1\) | \(2(1-r)\) | horizontal segment |
| \(c<h<1\) | \(0\le r\le h-c\) | \(h+\sqrt3-3r\) | three-arm, \(120^\circ\) tripod |
| \(c<h<1\) | \(h-c\le r\le h\) | \(2\sqrt{1+(h-r)^2}-2r\) | two arms |
| \(c<h<1\) | \(h\le r<1\) | \(2(1-r)\) | horizontal segment |
| \(1\le h<\sqrt3\) | \(0\le r\le h-c\) | \(h+\sqrt3-3r\) | three-arm tripod |
| \(1\le h<\sqrt3\) | \(h-c\le r<R(h)\) | \(2\sqrt{1+(h-r)^2}-2r\) | two arms |
| \(h=\sqrt3\) | \(0\le r<R(h)=b\) | \(h+\sqrt3-3r\) | tripod collapsing directly to a point |
| \(h>\sqrt3\) | \(0\le r\le b\) | \(h+\sqrt3-3r\) | tripod |
| \(h>\sqrt3\) | \(b\le r<R(h)\) | \(h-r-\sqrt{r^2-1}\) | vertical segment |

At the thresholds, arms of the canonical minimizer can have zero length. This is a classification of the **minimum length and one canonical optimal network**, not a claim that every optimal network is unique.

The phase boundaries at \(h=c\), \(h=1\), and \(h=\sqrt3\) are sharp. In particular, \(h=\sqrt3\) is the sole nondegenerate isosceles height at which a positive-length three-arm optimum collapses straight to a point without an intervening positive-length two-arm or one-segment regime.

## Assumptions and scope

The Euclidean metric and Euclidean one-dimensional Hausdorff length are used, with base half-width fixed to \(1\). All real \(h>0\) and all real \(r\ge0\) are covered. At \(r=0\) this is the ordinary three-terminal Steiner problem; for \(r>0\) it is the maximal-distance-minimizer problem. The finding is confined to the three-site isosceles family, not arbitrary compact sets or all triangles. The claimed source date is the first public posting of the motivating question, not an assertion about priority of the mathematical formulas.

## Proof

**1. Reduction from connected networks to a convex three-disk problem.** Write \(D_i=\overline B_r(v_i)\) for the three closed disks around the sites, and \(F(p)=\sum_{i=1}^3\operatorname{dist}(p,D_i)\). We first show
\[
L_h(r)=\min_{p\in\mathbb R^2}F(p).
\]
For an arbitrary admissible finite-length continuum \(\Sigma\), select \(z_i\in\Sigma\cap D_i\). The standard three-terminal Steiner-tree lower bound yields
\[
\mathcal H^1(\Sigma)\ge\min_{p\in\mathbb R^2}\sum_{i=1}^3\|p-z_i\|
\ge\min_p\sum_i\operatorname{dist}(p,D_i).
\]
Here the first inequality can be seen by retaining a minimal connected tree inside the finite-length continuum joining the three selected points: the tree consists of three (possibly degenerate) paths from a common junction, and each path is at least the Euclidean distance between its endpoints. The usual finite-terminal Steiner-tree characterization gives the same inequality. Conversely, choose a minimizer \(p\) of \(F\); it exists by continuity and coercivity. Project \(p\) to the nearest point \(z_i\in D_i\) and take the union of the three straight segments \([p,z_i]\). This connected network is admissible and has length at most \(F(p)\). The lower bound proves equality. Consequently the constructed union attains the minimum.

**2. Exact one-variable minimization.** The distance to a convex disk is convex, so \(F\) is convex. Reflection about the vertical axis preserves \(F\), hence an optimal junction may be chosen on that axis. Moving an axis point with height below \(0\) to \(0\), or one above \(h\) to \(h\), cannot increase any of the three distances. Thus
\[
L_h(r)=\min_{0\le y\le h}f(y),\qquad
f(y)=(h-y-r)_+ +2\bigl(\sqrt{1+y^2}-r\bigr)_+.
\]
For \(r<R(h)\), the interval \(I=[a_r,b_r]\) defined above is nonempty. On \([0,a_r)\), only the apex term is active and \(f\) decreases. On \((b_r,h]\), only the base terms are active and \(f\) increases. On \(I\), both types of terms are active, so
\[
f(y)=h-y+2\sqrt{1+y^2}-3r,
\qquad f'(y)=-1+\frac{2y}{\sqrt{1+y^2}}.
\]
Its unique free minimum is at \(c=1/\sqrt3\). Clamping this point to \(I\) produces \(y_*\) and the boxed formula.

**3. Collapse radius and exhaustive transition arithmetic.** The value vanishes if and only if the three disks have a common point. By horizontal reflection, the smallest enclosing disk of the three sites has a center on the vertical axis; minimizing \(\max\{\sqrt{1+y^2},|h-y|\}\) gives radius \(1\) for \(h\le1\), otherwise radius \((h^2+1)/(2h)\). This proves the exact \(R(h)\).

The regime with \(y_*=c\) requires both \(r\le h-c\) and \(r\le\sqrt{1+c^2}=2/\sqrt3\). It therefore ends at the smaller of those two bounds. The former is first precisely when \(h<\sqrt3\), producing an apex-contact two-arm phase. The latter is first precisely when \(h>\sqrt3\), producing a base-disk-intersection vertical segment phase. When \(h<1\) and \(r\ge h\), the apex disk contains the base midpoint; the optimal union is the horizontal segment of length \(2(1-r)\) until \(r=1\). Direct substitution yields every row of the table. All inequalities are strict in the interior of their indicated positive-length phases, so all thresholds are sharp.

**4. Explicit realization.** For \(r<R(h)\), take \(p_*=(0,y_*)\). For each of the three sites \(v_i\), let
\[
z_i=\begin{cases}p_*,&\|p_*-v_i\|\le r,\\v_i+\dfrac{r(p_*-v_i)}{\|p_*-v_i\|},&\|p_*-v_i\|>r.\end{cases}
\]
Then \(\Sigma_* = \bigcup_{i=1}^3[p_*,z_i]\) is a global minimizer by step 1. The three, two, or one nonzero segments are exactly the networks in the table. For \(r\ge R(h)\), any single common point of the three disks is a zero-length minimizer.

## Verification

Run `python3 verify_mdm.py` from the directory containing this file. The standalone script uses only the Python standard library and checks 644 specified/random height-radius cases against the independently evaluated clamped and branch formulas, plus 20 planar finite-grid comparisons. A separate exploratory differential-evolution stress test used 200 random height-radius pairs, agreeing to better than \(8\times10^{-11}\) in objective value. Neither finite test proves global minimality: that is established by the three-terminal reduction, convex symmetrization, and one-dimensional derivative argument above.

## Relationship to prior work

The classical Fermat–Torricelli/three-terminal Steiner theorem determines the \(r=0\) endpoint and underlies the network-to-disk reduction; neither is claimed as new. Teplitskaya's 2022 presentation explicitly illustrates a three-point tripod and another three-point segment as MDM examples; the **individual shapes are previously known**, not discoveries here. Basok–Cherkashin–Teplitskaya (2022, Observation 2.11 and Proposition 2.14) already establish the general finite-site Steiner-tree structure and the *small-radius trimmed tripod*; in the present isosceles geometry their proposition covers the initial three-arm branch whenever \(0<r<\min\{h-1/\sqrt3,2/\sqrt3\}\). Those reductions and this initial branch are prior art. Their result does not state the later two-arm, horizontal/vertical segment, and collapse regimes or their sharp two-parameter boundaries. Teplitskaya's 2026 length-optimization problem collection asks for explicit compact target geometries and likewise does not state this profile. A distinct published square four-site MDM result concerns four target points, not the full height-dependent three-site family. The asserted contribution here is the simultaneous exact all-radius length formula, the topology/order of branch loss, and the sharp height thresholds.

## Limitations

This is a deliberately restricted but natural three-site family; it is not an answer for arbitrary finite target sets or the circle/stadium cases of the motivating open-problem collection. It constructs a canonical minimizer without proving uniqueness of **all** minimizers. Prior qualitative three-point examples exist. Older literature on networks meeting neighborhoods of terminals may contain an equivalent formula under different terminology; novelty is best-knowledge pending independent literature audit. The numerical tests are supplementary only. No independent audit has been carried out.

## References

1. Y. Teplitskaya, *Open problems from the Length Optimization event at MDS 2026*, arXiv:2611.03403v1, publicly submitted 2026-11-02, §3, https://arxiv.org/html/2611.03403v1 .
2. M. Basok, D. Cherkashin and Y. Teplitskaya, *Inverse maximal and average distance minimizer problems*, arXiv:2212.01903, 2022, https://arxiv.org/abs/2212.01903 .
3. Y. Teplitskaya, *Maximal distance minimizers*, Benasque PDE meeting presentation, 2022-08-31, slides 8–10, https://www.benasque.org/2022pde/talks_contr/3110_Teplitskaya.pdf .
4. A. Gordeev and Y. Teplitskaya, *On regularity of maximal distance minimizers in Euclidean space*, arXiv:2207.13745, first submitted 2022-07-27, https://arxiv.org/abs/2207.13745 .
