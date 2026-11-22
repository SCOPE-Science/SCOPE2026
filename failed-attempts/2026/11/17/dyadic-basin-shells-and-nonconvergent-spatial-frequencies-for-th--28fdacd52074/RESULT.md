# Dyadic basin shells and nonconvergent spatial frequencies for the equilateral farthest-projection map

## Finding
Let \(V_0,V_1,V_2\) be the counterclockwise vertices of a unit equilateral triangle, with indices interpreted modulo three. On the union of its three **complete supporting lines** \(\ell_i=\{V_i+t(V_{i+1}-V_i):t\in\mathbb R\}\), apply the farthest-orthogonal-projection map: at a point on one supporting line, orthogonally project onto the more distant of the other two supporting lines, and fix the point if their distances tie. The definition at vertices is unambiguous.

The complete recurrent set is exactly **three fixed side midpoints and two attracting primitive three-cycles**:
\[
\Gamma_{-}=\{V_i+\tfrac13(V_{i+1}-V_i):i=0,1,2\},\qquad
\Gamma_{+}=\{V_i+\tfrac23(V_{i+1}-V_i):i=0,1,2\}.
\]
Every initial point outside the explicit countable set of fixed-point preimages converges to one of these cycles, at exact factor \(1/2\) per step after a finite entry time. The countable exceptional set is, in side coordinates, precisely
\[
E=\{\tfrac12\}\cup\{2^k,1-2^k:k=0,1,2,\ldots\};
\]
its points reach a fixed midpoint in finite time. There are **no other periodic points** or recurrent points.

The two attracting basins have a striking exact description on each outward ray \(t>1\): convergence to \(\Gamma_+\) occurs precisely for
\[
t\in B_+:=\bigcup_{j\ge1}(2^{2j-1},2^{2j}),
\]
and convergence to \(\Gamma_-\) occurs on the complementary open dyadic shells \(\bigcup_{j\ge0}(2^{2j},2^{2j+1})\); the dyadic endpoints belong to \(E\). Thus, with \(D(R)=\operatorname{length}(B_+\cap[1,R])/(R-1)\),
\[
D(4^j)=\frac23\quad(j\ge1),\qquad
\lim_{j\to\infty}D(2\cdot4^j)=\frac13,
\qquad\liminf_{R\to\infty}D(R)=\frac13,\quad\limsup_{R\to\infty}D(R)=\frac23.
\]
In particular, **neither orientation basin has an asymptotic arclength density along an outward supporting-line ray**, despite universal convergence to a cycle or fixed point.

The exact time to first enter the open triangle-edge interval \(0<t<1\), for generic initial \(t>1\), is \(N(t)=n\) precisely when \(2^{n-1}<t<2^n\). Consequently, if \(t\) is uniformly distributed on \((1,2^m)\), then
\[
\Pr(N(t)=n)=\frac{2^{n-1}}{2^m-1},\qquad n=1,\ldots,m.
\]
Equivalently, the slack \(m-N(t)\) converges in law to the geometric distribution with mass \(2^{-r-1}\) at every \(r\in\{0,1,2,\ldots\}\).

## Assumptions and scope
All three lines are infinite; this is **not** a dynamics clipped to the boundary of the triangle. The triangle is equilateral and is normalized to side length one (any similar triangle has identical side-coordinate dynamics). The coordinate \(t\) uses the oriented segment from \(V_i\) to \(V_{i+1}\). At each vertex the farthest projection is independent of which incident line is taken as the source. Side midpoints are fixed under the original tie-as-fixed convention. An attracting cycle means distance to its three-point orbit tends to zero; it does not assert finite-time arrival at the orbit itself. The arclength-density claim concerns a **one-sided ray** \(t>1\), not a symmetric interval of the supporting line.

## Proof
**1. Exact geometric reduction.** Let \(d_i=V_{i+1}-V_i\) be the unit side vectors. They satisfy \(d_i\cdot d_{i+1}=-1/2\). For \(x=V_i+td_i\), the distances to the other supporting lines are \((\sqrt3/2)|t|\) (line sharing \(V_i\)) and \((\sqrt3/2)|1-t|\) (line sharing \(V_{i+1}\)). The farther line is the latter precisely when \(t<1/2\). Projection along unit directions, using the displayed dot product, gives the exact one-step rule
\[
(i,t)\longmapsto
\begin{cases}
(i+1,(1-t)/2),&t<1/2,\\
(i,t),&t=1/2,\\
(i-1,1-t/2),&t>1/2.
\end{cases}
\]
At \(t=0\) or \(1\), either incident-line representation produces the same point: the midpoint of the opposite side. Thus the formula is a valid representation of the original single-valued map; the two representations of a vertex yield the same image.

**2. Contractive interior and all cycles.** Put \(s=t-1/2\). For \(s\ne0\), the new side coordinate obeys
\[
s'= -\frac{s}{2}+\frac{\operatorname{sgn}(s)}4.
\]
When \(0<|s|<1/2\), the sign is preserved, and the corresponding fixed coordinate is \(s_*=\operatorname{sgn}(s)/6\). The exact identity \(s_{k}-s_*=(-1/2)^k(s_0-s_*)\) holds while the orbit remains in the interior; the chosen side index increments by one at every step when \(s<0\) and decrements by one when \(s>0\). Hence interior points converge to the indicated primitive three-cycles, with exact coordinate contraction factor \(1/2\) per step. The three midpoints \(s=0\) are fixed. Since each such open half-edge is forward invariant, no other periodic orbit lies within the triangle edges.

**3. Global finite entry and exceptional set.** For \(|s|>1/2\), the sign flips and \(|s'|=(|s|-1/2)/2\). Therefore, as long as the coordinate remains exterior,
\[
|s_k|+1/2=2^{-k}(|s_0|+1/2).
\]
For \(t>1\) this initial quantity is \(t\), and for \(t<0\) it is \(1-t\). Except when that quantity is a power of two, the first strict entrance into \(|s|<1/2\) occurs after
\[
N(t)=\left\lceil\log_2\max(t,1-t)\right\rceil
\]
steps for exterior \(t\). If the quantity equals \(2^k\), the orbit instead lands at a vertex and then at a fixed midpoint. Together with the midpoint itself, these are exactly the side-coordinate exceptions \(E\). Interior points have \(N(t)=0\). In the exterior the sign flips exactly \(N(t)\) times, so initial \(t>1\) selects \(\Gamma_+\) for even \(N(t)\), and \(\Gamma_-\) for odd \(N(t)\). All points have consequently been classified. A nonconstant recurrent or periodic point cannot lie in a strict basin trajectory because its forward iterates approach one of the finite cycles without returning arbitrarily close to its initial point; the recurrent set is precisely the five displayed invariant components (three fixed points and two cycles).

**4. Dyadic shells and exact basin frequency.** For generic \(t>1\), the first-entry criterion is \(2^{n-1}<t<2^n\) for \(N(t)=n\). Even \(n=2j\) yields precisely \(B_+\), and odd \(n=2j+1\) gives the complementary shells. Their lengths are \(2^{n-1}\). Consequently,
\[
\operatorname{length}(B_+\cap[1,4^j])=
\sum_{r=1}^j(4^r-2\cdot4^{r-1})=\frac{2(4^j-1)}3.
\]
Division by \(4^j-1\) gives \(D(4^j)=2/3\). Up to the next endpoint \(2\cdot4^j\) no additional \(B_+\) points appear, so \(D(2\cdot4^j)=2(4^j-1)/[3(2\cdot4^j-1)]\to1/3\). Within a positive shell \(D\) increases monotonically with \(R\); within a negative shell it decreases. Thus the two subsequential limits are also the global \(\liminf\) and \(\limsup\). Their inequality proves the absence of a spatial basin density, and the complementary basin has corresponding lower and upper densities \(1/3\) and \(2/3\).

**5. Capture-time distribution.** On \((1,2^m)\), the event \(N(t)=n\) has exact Lebesgue measure \(2^n-2^{n-1}=2^{n-1}\), giving the displayed probability. For each fixed \(r\ge0\),
\[
\Pr(m-N(t)=r)=\frac{2^{m-r-1}}{2^m-1}\longrightarrow2^{-r-1}.
\]
These limits sum to one, so they determine the asserted probability-law convergence. No stochastic dynamics are assumed: the randomness is solely the uniform initial position.

## Verification
The standalone standard-library program `verify.py` uses exact `fractions.Fraction` arithmetic to check the affine map and its capture predictions on 50,050 rational starting-coordinate presentations, including negative and remote coordinates, all fixed-point preimages on the grid, and both periodic orbits. It checks the finite dyadic cumulative-length identity for fifteen scales and the capture-time probability normalization for twenty-one scales. Run `python3 verify.py`; the three success lines are `EXACT_RATIONAL_CAPTURE_AND_ORIENTATION_OK 50050`, `EXACT_DYADIC_BASIN_MEASURES_OK`, and `EXACT_CAPTURE_TIME_DISTRIBUTION_OK`. The finite test does not certify the infinite assertions; those follow from the exact inequalities and geometric series above.

## Relationship to prior work
Everett introduced the farthest-projection map, established qualitative convergence to periodic or fixed behavior, and discussed geometry-dependent periods and boundary-restricted isosceles bifurcations. The original paper does not determine the **global equilateral basin partition on full supporting lines**, its dyadic capture law, or the nonexistence of one-sided basin densities. A separately published exact classification of primitive three-cycles for arbitrary triangles already implies that the equilateral geometry has precisely two primitive three-cycles; this is acknowledged, not claimed as new. That classification expressly leaves basins and higher-period dynamics outside its scope. The present result proves a **complete global recurrent-set and basin description**, and exact arclength statistics. Everett's later angle-rule sequence study provides general convergence criteria for a broader class of maps, but not these quantitative farthest-rule basin identities. Classical piecewise-contraction theory concerns general convergence mechanisms, not this explicit dyadic one-sided-basin frequency anomaly.

## Limitations
The complete classification is specific to equilateral triangles and the original farthest-orthogonal-projection rule with ties fixed. It does not establish persistence of the exact dyadic pattern for unequal sides, nor describe a symmetric-interval basin density (which can behave differently), or a randomly perturbed map. This is an analytical calculation for infinite supporting lines; bounded-triangle behavior is a strict subcase. There is no claim of independent verification or of absolute publication priority beyond the inspected sources.

## References
1. Samuel Everett, *A Piecewise Contractive Map on Triangles*, *Journal of Dynamical Systems and Geometric Theories* **18**(2), 183–192; DOI `10.1080/1726037X.2020.1847765`; publisher-confirmed online publication **2021-01-07**. Complete open publisher PDF at `https://tarupublications.com/journals/jdsgt/volume/18/issue/2/a-piecewise-contractive-map-on-triangles/pdf` (Definition 2.1, Sections 3–4). Author preprint arXiv `2408.16019v1` appeared later.
2. *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map*, published-finding corpus, `2026/10/11/SCOPE-exact-two-orientation-classification-of-primitive-three-cycles-f--2944d54e59d8`, `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-two-orientation-classification-of-primitive-three-cycles-f--2944d54e59d8` (RESULT.md, Sections Finding, Proof, Limitations).
3. Samuel Everett, *A geometric dynamical system with relation to polygonal billiards*, arXiv `2112.02207` (2021), especially the farthest-line piecewise-rule definition and Section 5.
4. E. Catsigeras, P. Guiraud, A. Meyroneinc and E. Ugalde, *On the asymptotic properties of piecewise contracting maps*, *Dynamical Systems* **31**(2), 107–135 (2016), preprint accessible via ResearchGate.
