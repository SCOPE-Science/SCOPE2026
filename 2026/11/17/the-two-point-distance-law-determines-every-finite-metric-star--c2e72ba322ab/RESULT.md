# The two-point distance law determines every finite metric star

## Finding

Let \(T\) be a finite **metric star**: \(m\geq 3\) closed intervals of arbitrary strictly positive lengths \(\ell_1,\ldots,\ell_m\), with exactly one endpoint of each interval identified at a common hub, equipped with its intrinsic shortest-path metric. Put \(L=\sum_i\ell_i\), and independently choose \(X,Y\) from normalized arclength measure on \(T\). Let \(S(t)=\Pr\{d(X,Y)>t\}\) for \(t\geq0\).

**Reconstruction theorem.** The single real-valued function \(S\) uniquely determines \(m\), \(L\), and the multiset \(\{\ell_1,\ldots,\ell_m\}\), hence the metric star up to isometry. No prior knowledge of \(m\) or \(L\) is needed. An exact recovery procedure is given below, including repeated lengths and complete cancellations of observable derivative jumps. The conclusion is about the **population law** and does not assert statistically stable finite-sample recovery.

The sharp exceptional boundary is an interval: stars with one or two arms are isometric to an interval of total length \(L\), and the position of the nominal two-arm junction is undetectable (and geometrically inessential).

## Assumptions and scope

All arms have finite strictly positive real lengths. Sampling is independent and uniform relative to the one-dimensional arclength measure, normalized by total arclength \(L\). The distance is the intrinsic geodesic distance, not ambient Euclidean distance. Degree-two subdivisions are ignored as isometrically redundant; \(m\) is the degree of the unique branch point when \(m\geq3\). Equality of distance laws means equality as exact probability distributions on \([0,\infty)\). The result covers ties and additive resonances, with no generic-position assumption.

Write \(r_+=\max\{r,0\}\). For all \(t\geq0\), define

\[
K_t(a,b)=ab-\tfrac12\bigl(t^2-(t-a)_+^2-(t-b)_+^2+(t-a-b)_+^2\bigr).
\]

Then the complete tail formula is

\[
L^2S(t)=\sum_{i=1}^{m}(\ell_i-t)_+^2+2\sum_{1\leq i<j\leq m}K_t(\ell_i,\ell_j).
\tag{1}
\]

In particular, throughout \(0<t<\min_i\ell_i\),

\[
S(t)=1-\frac{2t}{L}+\frac{m(3-m)t^2}{2L^2}.
\tag{2}
\]

Thus \(L=-2/S'(0+)\). Given \(L\), the initial second derivative recovers \(m\) as the unique integer \(m\geq3\) satisfying \(L^2S''(0+)=m(3-m)\), since this expression is strictly decreasing over those integers.

## Proof

**1. Exact distance law.** Identify arm \(i\) with \([0,\ell_i]\), distance zero at the hub. If both points lie on that arm at coordinates \(x,y\), their distance is \(|x-y|\); the set of pairs with distance above \(t\) has area \((\ell_i-t)_+^2\). If they lie on distinct arms \(i,j\), their distance is \(x+y\). The area of the complementary set \(\{(x,y):0\leq x\leq\ell_i,0\leq y\leq\ell_j,x+y\leq t\}\) is

\[
\tfrac12\bigl(t^2-(t-\ell_i)_+^2-(t-\ell_j)_+^2+(t-\ell_i-\ell_j)_+^2\bigr),
\]

by inclusion-exclusion in the positive quadrant. Accounting for both orders of distinct arms and dividing by \(L^2\) yields (1). For \(0<t<\min_i\ell_i\), expand each positive-part term to obtain (2). This proves recovery of \(L\) and \(m\).

**2. The finite signed jump spectrum.** Formula (1) makes \(S\) continuously differentiable and piecewise quadratic, with finitely many breakpoints. At all positive \(t\) outside its breakpoints,

\[
L^2S''(t)=m(3-m)
 +2(m-2)\#\{i:\ell_i<t\}
 -2\#\{\{i,j\}:i<j,\ \ell_i+\ell_j<t\}.
\tag{3}
\]

Here a breakpoint may have a zero net jump because two kinds of terms cancel. Define the observable finite signed atomic measure

\[
\nu=\frac{L^2}{2}\sum_{s>0}
\bigl(S''(s+)-S''(s-)\bigr)\,\delta_s.
\]

All one-sided derivatives are defined using the constant quadratic pieces, so this is an exact distributional derivative even at a cancellation point. Equation (3) gives the decisive identity

\[
\boxed{\nu=(m-2)\sum_{i=1}^{m}\delta_{\ell_i}
 -\sum_{1\leq i<j\leq m}\delta_{\ell_i+\ell_j}.}
\tag{4}
\]

**3. Injectivity, including ties and cancellations.** Suppose two positive \(m\)-multisets \(A,B\) produce the same \(S\). Steps 1 and 2 imply the same \(L,m,\nu\). If \(A\ne B\), let \(s>0\) be the least value whose multiplicity differs in \(A\) and \(B\). Every pair of strictly positive lengths summing to \(s\) consists of two lengths strictly smaller than \(s\). Those lower-length multiplicities agree by minimality of \(s\), so the multiplicities of pair sums equal to \(s\) also agree. Equation (4) then gives

\[
\nu_A(\{s\})-\nu_B(\{s\})
 =(m-2)\bigl(\operatorname{mult}_A(s)-\operatorname{mult}_B(s)\bigr)\ne0,
\]

because \(m\geq3\). This contradicts equality of \(\nu\). Therefore the arm-length multisets coincide, which determines the intrinsic metric star up to isometry.

**4. Constructive recovery.** Process candidate values \(s>0\) in increasing order, maintaining all previously reconstructed arm lengths with multiplicities. The candidate set consists of all visible atoms of \(\nu\) together with pair sums of arms already reconstructed; it is updated after each step. At \(s\), let \(c_s\) count pairs of already recovered arms summing to \(s\), counting distinct occurrences. The multiplicity of an arm of length \(s\) is exactly

\[
\boxed{a_s=\frac{\nu(\{s\})+c_s}{m-2}.}
\tag{5}
\]

It is a nonnegative integer. Newly recovered copies of \(s\) are added and processing continues until \(m\) arms have been found. No unknown pair can sum to \(s\), since both its summands would be smaller than \(s\). Every hidden arm length with zero observed net jump must coincide with a pair sum of earlier recovered arms and is therefore still considered. Because there are only finitely many arms and pair sums, the algorithm terminates. For instance, arms \((1,1,2)\) have \(\nu=2\delta_1-2\delta_3\); the arm at length \(2\) is invisible in the signed spectrum, but is recovered from the pair sum \(1+1\).

**5. Exceptional degree-two boundary.** A star with \(m=1\) or \(m=2\) is isometric to a closed interval of length \(L\). Its two-point geodesic tail is \((1-t/L)_+^2\), independent of the chosen subdivision of that interval. Such representations cannot be recovered as labeled arms; their metric spaces are nonetheless determined up to isometry. The theorem claims reconstructibility of the branching geometry precisely for \(m\geq3\).

## Verification

The accompanying standard-library checker `check_star_inverse.py` evaluates (1) with exact rational arithmetic, extracts the signed spectrum using (4), and independently reconstructs all arm lengths using (5). It covers 808 exact test multisets of three through ten arms, including repeated lengths and the cancellation example \((1,1,2)\), then compares the tail formula with direct finite-grid integration of geodesic distance predicates. The reported successful marker is `STAR_GEODESIC_DISTANCE_INVERSE_EXACT_OK 808`.

Run locally using `python check_star_inverse.py` (Python 3.9 or later). The finite-grid comparisons are consistency tests, not substitutes for the all-real-length argument in the proof. No external dependencies, precomputed artifacts, or remote services are required.

## Relationship to prior work

Vershik's matrix-distribution reconstruction framework (arXiv:math/0205086, first public 2002-05-08) uses full infinite matrices of random distances to determine metric-measure spaces. The result here uses only the **one-dimensional law of a single random pair distance**, a much smaller invariant, and proves it is complete within the metric-star class. Chazal and Sun (arXiv:1305.1172, first public 2013-05-06) reconstruct graph-like metric spaces from sampled metric data, also requiring substantially richer input. Baptista, Kennedy and Mugnolo (DOI 10.1007/s12220-024-01574-0, 2024), §4 Example 4.1, explicitly compute the mean distance of **equal-arm** stars, rather than the full distance distribution or uniqueness of arbitrary arm lengths. Gaspers and Lau (arXiv:1811.03836, 2018) study a combinatorial distance histogram for vertex pairs in discrete trees, not continuous uniform-arclength sampling. Dahl (DOI 10.1002/net.20202, 2007) concerns majorization of fixed-vertex distance vectors on trees, not this two-point inverse law.

A related public result titled *Exact persistence of two unordered separated particles on metric stars* studies homological persistence of configuration spaces. Its publicly searchable abstract concerns barcodes determined by arm lengths and pair sums; those invariants are not the scalar **volume distribution** of a random geodesic distance, and their inverse claims do not directly supply the present injectivity assertion. The full record was not accessible for decisive full-text comparison.

## Limitations

The theorem makes no claim that two-point distance laws distinguish arbitrary metric trees or metric graphs; that question lies outside its scope. It gives exact population-law identifiability, not robustness under noisy estimated distributions. Differentiating a measured empirical distribution three times is generally unstable. The underlying tail formula can be obtained by elementary integration; the new candidate is the full reconstruction statement including exact cancellation handling. A broader unpublished or inaccessible inverse theorem might subsume the result; literature priority is provisional. No independent audit has been performed.

## References

1. A. Vershik, *Random and universal metric spaces*, arXiv:math/0205086, publicly submitted 2002-05-08, https://arxiv.org/abs/math/0205086.
2. F. Chazal and J. Sun, *Gromov-Hausdorff Approximation of Metric Spaces with Linear Structure*, arXiv:1305.1172, first public 2013-05-06, https://arxiv.org/abs/1305.1172.
3. L. N. Baptista, J. B. Kennedy and D. Mugnolo, *Mean Distance on Metric Graphs*, J. Geom. Anal. 34 (2024), 137, https://doi.org/10.1007/s12220-024-01574-0.
4. S. Gaspers and J. Lau, *Minimizing and Computing the Inverse Geodesic Length on Trees*, arXiv:1811.03836, first public 2018-11-09, https://arxiv.org/abs/1811.03836.
5. G. Dahl, *Majorization and distances in trees*, Networks 50 (2007), 251–257, first online 2007-09-04, https://doi.org/10.1002/net.20202.
