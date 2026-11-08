# A two-point distance histogram determines every finite metric star

## Finding
Let \(S\) be a compact metric star: \(k\) closed intervals of strictly positive lengths \(a_1,\ldots,a_k\) are glued at one common endpoint and equipped with the intrinsic path metric and normalized arclength measure. Independently draw two points from this measure, and write \(D\) for their geodesic distance. The full probability law of \(D\) determines the metric isometry class of \(S\), without prior knowledge of \(k\), for every finite \(k\ge 1\). Specifically, if \(k\ge3\), it uniquely recovers \(k\) and the unordered multiset of all arm lengths. For \(k=1\) and \(k=2\) the graph is an interval, and its total length is recovered, but any artificial degree-two subdivision remains undetectable (as required by isometry).

For \(k\ge3\) the reconstruction is exact and finite: recover total arclength \(L\) and branch valence \(k\) from the value and right derivative of the density at zero; then recover the arm lengths recursively from the smallest atoms of its distributional second derivative. This remains valid with repeated lengths and with exact collisions between one arm length and a sum of others.

## Assumptions and scope
An arm of length \(a_i>0\) consists of all points with radial coordinate \(u\in[0,a_i]\). For points on a common arm, their distance is \(|u-v|\); on distinct arms their distance is \(u+v\). The measure of any measurable arm segment is its length divided by \(L=\sum_i a_i\). Points at the common vertex have measure zero. The law records distances in physical units, not normalized by diameter, and is assumed known exactly.

Put \(x_+=\max\{x,0\}\). A continuous version of the density of \(D\), for \(t\ge0\), is
\[
 f(t)=\frac{2}{L^2}\left[\sum_{i=1}^k(a_i-t)_+
 +\sum_{1\le i<j\le k}\bigl(t_+-(t-a_i)_+-(t-a_j)_++(t-a_i-a_j)_+\bigr)\right]. \tag{1}
\]
This formula is also valid for \(k=1,2\), taking an empty sum as zero. In particular \(f\) is continuous, compactly supported and piecewise affine; the value \(f(0)\) and right derivative \(f'_+(0)\) are unambiguously determined by the probability law.

## Proof
**1. The exact density.** For points on one arm \(i\), the unnormalized density of \(|u-v|\), where \(u,v\in[0,a_i]\), is \(2(a_i-t)_+\). For an unordered pair of distinct arms \(i<j\), ordered point sampling contributes twice the unnormalized density of the sum \(u+v\). Convolution of the two interval indicators gives
\[
 ({\mathbf{1}}_{[0,a_i]}*{\mathbf{1}}_{[0,a_j]})(t)
 =t_+-(t-a_i)_+-(t-a_j)_++(t-a_i-a_j)_+.
\]
Divide the resulting ordered-pair measure by \(L^2\) to obtain (1). Every pair of points belongs to exactly one of these cases, so the density has total integral one; there is no atom at zero or elsewhere.

**2. The arclength and valence are visible at the origin.** From (1), because all arms are positive,
\[
 f(0)=\frac{2}{L},\qquad
 f'_+(0)=\frac{k(k-3)}{L^2}.\tag{2}
\]
Thus \(L=2/f(0)\) is determined. For integer \(k\ge3\), the function \(k\mapsto k(k-3)\) is strictly increasing, beginning at zero. For \(k=1,2\), the derivative equals \(-2/L^2\), and the glued space is isometric to an interval of length \(L\). In particular, the two-point distance histogram distinguishes the genuine branch point case \(k\ge3\) from intervals and also determines the valence when branching occurs.

**3. The signed kink measure.** Work with distributional derivatives on the open half-line \((0,\infty)\), excluding the boundary \(t=0\). Differentiating (1) twice shows that the finite signed atomic measure
\[
 \nu:=\frac{L^2}{2}f''
 =-(k-2)\sum_{i=1}^k\delta_{a_i}
   +\sum_{1\le i<j\le k}\delta_{a_i+a_j}.\tag{3}
\]
Here \(\delta_s\) denotes unit point mass at \(s\). The measure \(\nu\) is recovered exactly from the law. Some negative and positive masses in (3) can cancel at colliding locations, so simply reading all visible negative breakpoints is not a valid inversion.

**4. A collision-safe greedy inversion.** Suppose a submultiset \(R\) of the arm lengths has already been recovered, with distinct copies counted separately. Define
\[
 \nu_R=\nu+(k-2)\sum_{a\in R}\delta_a
                    -\sum_{\{a,b\}\subset R}\delta_{a+b},\tag{4}
\]
where the second sum ranges over unordered pairs of *copies* in \(R\). It follows from (3) that
\[
 \nu_R=-(k-2)\sum_{a\notin R}\delta_a
          +\sum_{\{i,j\}:\ \text{at least one index not in }R}\delta_{a_i+a_j}.
\]
If any unrecovered arm exists, let \(b>0\) be its smallest length, and let \(q\) be its multiplicity among the unrecovered arms. Every positive pair-sum atom remaining in the second sum lies strictly to the right of \(b\), since every pair containing an unrecovered arm has sum greater than that arm's positive length. Thus \(b\) is the least point in the support of \(\nu_R\), and its mass is exactly \(-(k-2)q\). As \(k-2>0\), both \(b\) and \(q\) are recovered; append those \(q\) copies to \(R\) and repeat. After at most \(k\) iterations this yields every length, with no generic-position assumption. In particular, even resonance events \(a_h=a_i+a_j\) cannot spoil the recursion. The resulting multiset determines the metric star up to isometry.

**5. The interval boundary case.** A star with one or two arms is metrically an interval of length \(L\). Its pair-distance density is \(2(L-t)_+/L^2\), independent of the position of an artificial degree-two vertex. The law therefore determines precisely the isometry class even in these cases. This proves the theorem for all finite stars.

## Verification
Execute `python3 check_star.py` with Python 3 and only the standard library. It constructs (3) using exact rational arithmetic, applies the collision-safe inversion (4), and checks exact normalization of the piecewise-linear density and its kink masses. It includes repeated-length and arm/pair-sum resonance cases, 77 exact inverse cases, 230 independent kink checks, interval subdivision equivalence, and 140,000 independently sampled point pairs as a probabilistic check on the derived mean distance. Finite tests support but do not replace the proof of all positive real arm lengths.

For reference, integrating distances over edge cuts independently of (1) gives
\[
 \mathbb E[D]=\frac1{L^2}\sum_{i=1}^k\left(La_i^2-\frac23a_i^3\right).
\]
The verifier uses this separate identity to check the simulation. No finite-sample stability estimate, noisy inversion, or algorithm for general metric trees is claimed.

## Relationship to prior work
Goldsborough, Rautu and Römer (2014) compute leaf-to-leaf distance statistics for ordered regular discrete trees. Their observations concern vertices/leaves and do not provide uniform-arclength pair-distance inversion on a continuous metric star. Mémoli and Needham (2018) study global and local distance distributions as inverse invariants: their Section 4 constructs nonisomorphic general metric trees with equal local distance information, while their injectivity theorem for local distributions assumes a continuous measure-preserving identification. Neither statement implies the present theorem for the *single global pair-distance law* of an arbitrary-length star. Baptista, Kennedy and Mugnolo (2023/2024) analyze mean distance on compact metric graphs and explicitly compute the mean for equilateral stars; one scalar mean is weaker than the full density and does not imply arbitrary-length reconstruction. Work on separated two-particle configuration persistence of metric stars concerns homotopy and persistence barcodes of a filtered configuration space, not the pushforward of product arclength by geodesic distance; its formulas involving arm lengths and pair sums do not, by themselves, establish the histogram inverse implication.

## Limitations
The conclusion is conditional on the observed space belonging to the finite metric-star family. General metric graphs and trees can be nonisomorphic while sharing distance distributions. The law must be given in absolute length units and exactly; density values and distributional derivative atoms are ill-conditioned under measurement noise, and no statistical stability theorem is proved. The arclength weighting is essential: arbitrary sampling weights can change the kink coefficients and hence the inversion. Historical priority beyond the identified literature and database searches is not independently certified.

## References
1. A. M. Goldsborough, S. A. Rautu, R. A. Römer, *Leaf-to-leaf distances and their moments in finite and infinite ordered m-ary tree graphs*, arXiv:1406.4079v1 (first public 2014-06-16), https://arxiv.org/abs/1406.4079.
2. F. Mémoli and T. Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646 (first public 2018-10-23), especially Section 4, https://arxiv.org/html/1810.09646v5.
3. L. N. Baptista, J. B. Kennedy, D. Mugnolo, *Mean distance on metric graphs*, arXiv:2312.04952 (first public 2023-12-08), subsequently *Journal of Geometric Analysis* 34 (2024), article 137, https://link.springer.com/article/10.1007/s12220-024-01574-0.
4. W. Li and M. Özaydın, *Persistent Combinatorial Model of the Restricted Second Configuration Space of Metric Star Graphs*, arXiv:2603.00914v1 (first public 2026-03-01), especially Sections 1, 3 and 4, https://arxiv.org/html/2603.00914v1.
