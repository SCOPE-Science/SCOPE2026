# Four-sample vertex-count tomography of Euclidean triangles

## Finding
Let \(T\) be any nondegenerate Euclidean triangle with side lengths \(a,b,c\), perimeter \(P\), and \(p_1=a/P\), \(p_2=b/P\), \(p_3=c/P\). Sample four boundary points independently and uniformly by physical arclength, and let \(V_4\) be the number of extreme points of their convex hull. Write \(h_j=\Pr(V_4=j)\) for \(j\in\{2,3,4\}\). Then
\[
\begin{aligned}
h_2&=\sum_{i=1}^3 p_i^4,\\
h_3&=4\sum_{i=1}^3p_i^3(1-p_i),\\
h_4&=1-4\sum_{i=1}^3p_i^3+3\sum_{i=1}^3p_i^4
=6(p_1p_2+p_1p_3+p_2p_3)^2.
\end{aligned}
\]
**The full distribution of \(V_4\) determines \(T\) up to similarity, and four is the smallest sample size for which the hull-vertex-count distribution does so for every triangle.** An explicit inversion is
\[
 e_2=\sqrt{h_4/6},\qquad
 e_3=\frac{h_2-1+4e_2-2e_2^2}{4},
\]
where the three normalized side lengths are the three roots of
\[
 z^3-z^2+e_2z-e_3=0.
\]
In particular, the sharp universal range of the convex-quadrilateral probability is
\[
 \frac38<h_4\leq\frac23.
\]
The upper endpoint occurs exactly for an equilateral triangle; the lower bound is approached by triangles whose normalized side lengths tend to \((1/2,1/2,0)\), and is not attained by a nondegenerate triangle.

The image of the entire three-valued law is also explicit. Given \(h_2,h_3,h_4\geq0\) with sum one, define \(e_2,e_3\) as above and
\[
 \Delta=e_2^2-4e_2^3-4e_3+18e_2e_3-27e_3^2.
\]
The law comes from a nondegenerate Euclidean triangle **if and only if**
\[
 e_2>0,\qquad e_3>0,\qquad \Delta\geq0,\qquad
 \frac{e_2}{2}-e_3-\frac18>0.
\]
Equal roots are allowed and describe isosceles triangles.

## Assumptions and scope
All four points are iid on the entire boundary under normalized length measure, not uniform in the interior, and no vertices are sampled with positive probability. The hull of collinear sampled points is interpreted as the segment with its two endpoints as extreme points; this occurs precisely when all four points fall on one parent side. The triangle is nondegenerate: \(p_i>0\), \(\sum_i p_i=1\), \(p_i<1/2\). Similarity, rather than congruence, is the identifiable relation because all observables are invariant under common rescaling.

## Proof
**1. Reduction to side occupancies.** The supporting line of any original side is a supporting line for the random hull. If exactly \(k\geq1\) sampled points lie in the relative interior of that side, then the first and last in side order are extreme points of the sampled hull, except for the obvious single-point convention at \(k=1\). No point strictly between these extremes can be extreme. Therefore for any number of sampled points at least two, with edge occupancies \(K_i\), almost surely
\[
 V_N=\sum_{i=1}^3\min\{2,K_i\}.
\]
The \((K_1,K_2,K_3)\) vector is multinomial with probabilities \((p_1,p_2,p_3)\). The only patterns yielding \(V_4=2\) have all four samples on one side; they have total probability \(s_4=\sum_i p_i^4\). The only patterns yielding \(V_4=3\) have exactly three on one side and one elsewhere; their total probability is \(4\sum_i p_i^3(1-p_i)=4(s_3-s_4)\). Otherwise \(V_4=4\). This proves the three probability formulas up to the last symmetric-polynomial identity.

**2. The symmetric identity.** Let \(e_2=\sum_{i<j}p_ip_j\) and \(e_3=p_1p_2p_3\). Newton's identities with \(p_1+p_2+p_3=1\) yield
\[
 s_3=1-3e_2+3e_3,\qquad
 s_4=1-4e_2+2e_2^2+4e_3.
\]
Consequently \(h_4=1-4s_3+3s_4=6e_2^2\). Since \(e_2>0\), its positive square root is uniquely selected; the formula for \(h_2=s_4\) then determines \(e_3\). Vieta's theorem gives the characteristic cubic, and therefore the unordered length proportions uniquely. Euclidean side-side-side similarity finishes identification.

**3. Exact feasibility.** For a monic cubic \(f(z)=z^3-z^2+e_2z-e_3\), the discriminant \(\Delta\) is nonnegative exactly when all three roots are real, counting multiplicity. When \(e_2,e_3>0\), the roots are nonzero and cannot consist of two negative and one positive root: writing the negatives as \(-u,-v\) with \(u,v>0\), and the positive root as \(1+u+v\), would give \(e_2=uv-(u+v)(1+u+v)<0\). Thus all three roots are positive. As their sum is one, at most one root exceeds \(1/2\). The additional strict condition \(f(1/2)=e_2/2-e_3-1/8>0\) excludes both a root equal to \(1/2\) and a unique root greater than \(1/2\). It is therefore equivalent to all three strict triangle inequalities. Conversely, every nondegenerate triangle has three positive roots below \(1/2\), a nonnegative cubic discriminant, and \(f(1/2)>0\). Their Newton sums reproduce \(h_2,h_4\), hence also \(h_3=1-h_2-h_4\), proving sufficiency.

**4. Sharp range.** Since \(0<p_i<1/2\) and \(\sum_i p_i=1\), \(\sum_i p_i^2<1/2\). The Cauchy inequality gives \(\sum_i p_i^2\geq1/3\), equality exactly for the equal triple. Hence
\[
 \frac14<e_2=\frac{1-\sum_i p_i^2}{2}\leq\frac13,
\]
and \(3/8<h_4=6e_2^2\leq2/3\). Both endpoints are sharp in the stated sense.

**5. Minimality.** For three sampled boundary points, the hull has two vertices exactly when all three points occupy one parent side. Thus \(\Pr(V_3=2)=s_3\), and \(\Pr(V_3=3)=1-s_3\). The two noncongruent normalized isosceles triangles
\[
 (16/61,16/61,29/61),\quad(25/61,25/61,11/61)
\]
both satisfy the strict triangle inequalities and have
\[
 s_3=32581/226981.
\]
They therefore have identical \(V_3\)-laws (and necessarily identical laws for sample sizes one and two) but different \(V_4\)-laws: their \(h_4\) values are respectively \(8411136/13845841\) and \(8283750/13845841\). No sample size below four can identify all triangle shapes from the vertex-count law.

## Verification
The self-contained program `verify.py` enumerates the \(3^4=81\) labeled four-point side-occupancy patterns using exact rational arithmetic for five triangle shapes, checks both symmetric-polynomial identities and the inverse, and verifies the rational minimality pair. It separately samples continuous boundary locations, computes convex hulls by an independent monotone-chain routine, and compares all three probabilities over 180,000 four-point trials. `python verify.py` prints `VERIFY_OK exact_occupancy_shapes=5 continuous_hull_trials=180000 nonidentifiability_pair=1`. The finite tests are checks, not a substitute for the all-triangle proof.

## Relationship to prior work
The facet-wise interpretation of boundary random-polytope vertices and the broader random-polytope context are established in Reitzner, Schütt and Werner (first public arXiv version 2019). That geometric reduction is used as background, not claimed as new. The new mathematical claim is the **single-four-sample exact inverse law, its complete feasibility criterion and minimality**. Har-Peled's 2011 work and Efron's classical expected-hull work concern points sampled from the **interior** of convex bodies; those are different input distributions. Sylvester's familiar four-point convexity probability for interior-uniform triangle points is always \(2/3\), whereas the present perimeter-uniform value varies with shape and equals \(2/3\) only for an equilateral triangle. The existence of general occupancy arguments does not by itself state the resulting one-experiment reconstruction or the sharp feasible image.

## Limitations
The laws are exact population probabilities. Statistical confidence intervals for recovering side lengths from finite repetitions and stability near isosceles or degenerate shapes are not established. The convex polygon formula for edge occupancy is elementary background; no claim is made here that a single four-point vertex-count law reconstructs arbitrary polygons. Historical priority beyond accessible records is provisional, particularly given the elementary occupancy mechanism and the possibility of earlier unpublished inverse observations.

## References
- S. Har-Peled, *On the Expected Complexity of Random Convex Hulls*, arXiv:1111.5340 (first public version 2011-11-22), https://arxiv.org/abs/1111.5340 (interior-uniform comparison).
- M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first public version 2019-11-14), https://arxiv.org/abs/1911.05917 (facet-wise boundary sampling and asymptotics).
- B. Efron, *The convex hull of a random set of points*, Biometrika 52 (1965), 331–343, https://doi.org/10.1093/biomet/52.3-4.331 (classical random-hull context; original report also dated January 1965 without a verified day).
- E. W. Weisstein, *Sylvester's Four-Point Problem*, MathWorld, https://mathworld.wolfram.com/SylvestersFour-PointProblem.html (interior sampling model, not a source of the present inverse claim).
