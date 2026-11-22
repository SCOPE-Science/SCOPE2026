# Parity-dependent activation thresholds for budgeted probabilistic firebreaks on a path

## Finding

Consider a path with \(n\ge2\) equal-value fuel patches. Edge \(i\), joining patches \(i\) and \(i+1\), transmits an ignition independently with probability \(q_i=e^{-g_i}\), where the nonnegative protection investment \(g_i\) obeys \(\sum_{i=1}^{n-1}g_i=B>0\). One initial ignition occurs at a uniformly chosen patch; fire then propagates through every transmitting edge. The goal is to minimize the expected number of burned patches. There is a **unique optimal investment vector** for every \(n\) and \(B\), and its first diversification threshold depends sharply on path parity:

- For \(n=2m\), \(m\ge2\), the sole protected edge is the central edge \(m\), receiving the whole budget, **if and only if**
  \[
  0<B\le B_{2m}^{\mathrm{first}}=\log\!\left(\frac{m}{m-1}\right).
  \]
  Above this threshold, that central-only allocation is strictly suboptimal.
- For \(n=2m+1\), \(m\ge2\), the sole protected edges are the two central edges \(m,m+1\), each receiving \(B/2\), **if and only if**
  \[
  0<B\le B_{2m+1}^{\mathrm{first}}=2\log\!\left(\frac{m}{m-1}\right).
  \]
  Above this threshold, their equal two-edge allocation is strictly suboptimal.

The endpoint cases are \(n=2\), where the only edge receives the budget for all \(B>0\), and \(n=3\), where the two edges always receive \(B/2\). At either finite threshold the stated center allocation is still the **unique** global optimum. For a matched value of \(m\), the odd-path threshold is exactly twice the even-path threshold; the respective large-\(m\) scales are \(1/m\) and \(2/m\).

The four-patch case admits a complete continuation: its unique optimum is \((0,B,0)\) through \(B=\log 2\); for \(B>\log 2\), it is \((x,B-2x,x)\), where the unique \(x\in(0,B/2)\) solves
\[
 e^B=e^{3x}+e^{2x}.
\]

## Assumptions and scope

Patches are the vertices \(1,\ldots,n\) of the undirected path; the \(n-1\) edges are its only routes for fire spread. One patch is chosen uniformly as the ignition point, independently of all edge outcomes. Every edge is independently open to transmission with probability \(e^{-g_i}\), and every patch in the ignition's open-edge connected component burns. The protection variables are real, nonnegative, of equal unit cost, and have a fixed total budget \(B\). The exponential probability law is an **assumed dimensionless model**, not a calibrated law linking physical firebreak width to field failure probability. There is no direct protection of individual patches, wind-driven leapfrogging, or secondary ignition outside the connected component.

Index edges starting at \(1\). Put
\[
 F(g)=\sum_{1\le i<j\le n}\exp\!\left(-\sum_{k=i}^{j-1}g_k\right).
\]
The optimality statements are about exact global minimizers on \(\{g_i\ge0:\sum g_i=B\}\), not stationary points of an unconstrained problem.

## Proof

**Expected loss and strict convexity.** For distinct patches \(i<j\), connectivity requires every intervening edge to transmit. Independence gives
\[
 \Pr(i\leftrightarrow j)=\exp\!\left(-\sum_{k=i}^{j-1}g_k\right).
\]
For the size \(L\) of the uniformly rooted component, counting ordered connected pairs gives
\[
 \mathbb E L=\frac1n\sum_{i,j=1}^{n}\Pr(i\leftrightarrow j)=1+\frac2nF(g).
\]
Thus the loss minimizer minimizes \(F\). For every nonzero vector \(v\in\mathbb R^{n-1}\), its directional second derivative is
\[
 D^2F(g)[v,v]=\sum_{i<j}e^{-\sum_{k=i}^{j-1}g_k}\left(\sum_{k=i}^{j-1}v_k\right)^2>0.
\]
Indeed, the length-one intervals already contribute \(\sum_k e^{-g_k}v_k^2>0\). Hence \(F\) is strictly convex; the nonempty compact budget simplex has one global optimum. Reflection of the path leaves \(F\) invariant and consequently fixes this unique optimum.

**First-order certificate.** Write \(G_k=\partial F/\partial g_k\). Direct differentiation yields
\[
 G_k=-\sum_{i\le k<j}\exp\!\left(-\sum_{a=i}^{j-1}g_a\right).
\]
For a proposed budget-simplex minimizer, the necessary and sufficient first-order convex optimality conditions are: all positively funded edges have the same \(G_k\), and all zero-funded edges have \(G_k\) at least this value. Sufficiency follows by the supporting-hyperplane inequality and strict convexity; necessity follows by transferring an infinitesimal budget from a positive edge to an arbitrary other edge.

**Even number of patches.** Let \(n=2m\), \(m\ge2\), place budget \(B\) on edge \(m\), and let \(q=e^{-B}\). The central derivative is \(G_m=-m^2q\). At edge \(k\), for \(1\le k<m\), count \(k(m-k)\) within-left pairs and \(km\) across-center pairs to get
\[
 G_k=-k(m-k)-kmq,\qquad G_k-G_m=(m-k)(mq-k).
\]
All right-side derivatives are mirrors of left-side derivatives. Hence every inactive derivative is at least \(G_m\) exactly when \(mq\ge m-1\), since \(k\le m-1\) and the strongest condition is \(k=m-1\). This is equivalent to \(B\le\log(m/(m-1))\). Below or at the threshold strict convexity certifies the unique global optimum; above it, transferring some protection from the center to either neighboring edge strictly decreases loss, so center-only allocation is not optimal.

**Odd number of patches.** Let \(n=2m+1\), \(m\ge2\), place \(B/2\) on each of edges \(m,m+1\) and set \(q=e^{-B/2}\). Their derivatives coincide by reflection and equal \(-m(q+mq^2)\). At left edge \(1\le k<m\), count \(k(m-k)\) left-internal pairs, \(k\) central-crossing pairs with one attenuated edge, and \(km\) fully crossing pairs with two attenuated edges. This gives
\[
 G_k=-k(m-k+q+mq^2),\quad G_k-G_m=(m-k)(q+mq^2-k).
\]
Reflected edges yield identical comparisons. All inactive gradients meet the certificate precisely when \(q+mq^2\ge m-1\). The factorization
\[
 q+mq^2-(m-1)=(q+1)(mq-(m-1))
\]
reduces it to \(q\ge(m-1)/m\), equivalently \(B\le2\log(m/(m-1))\). Strict convexity again establishes uniqueness even at equality and strict failure of the proposed support beyond the threshold. For \(n=3\), reflection and uniqueness force an equal split for every budget; \(n=2\) has only one decision variable.

**Four-patch continuation.** Reflection and uniqueness imply the optimizer on \(n=4\) has form \((x,B-2x,x)\) for \(0\le x\le B/2\). Its pair sum is
\[
 F(x)=2e^{-x}+e^{-B+2x}+2e^{-B+x}+e^{-B}.
\]
Its derivative at \(0\) has the sign of \(2-e^B\), and at \(B/2\) it is strictly positive: \(F'(B/2)=2>0\). Its second derivative is strictly positive. Consequently for \(B\le\log2\), \(x=0\) is uniquely minimizing; for \(B>\log2\), one unique interior critical point minimizes. Solving \(F'(x)=0\) yields the displayed strictly increasing equation, and necessarily \(B-2x>0\).

**Large-size threshold comparison.** The identity \(\log(m/(m-1))=-\log(1-1/m)=1/m+O(m^{-2})\) gives both stated asymptotics. No post-threshold support classification is claimed for general \(n\ge5\).

## Verification

The standalone `check_firebreak.py` uses Python 3 standard library and reports `PASS 6952 finite/exact checks`. It independently enumerates bond-outcome probabilities with exact fractions for paths through eight vertices; checks exact rational derivative identities and active/inactive comparisons for the even and odd families through \(m=12\); checks the four-patch continuation on multiple budgets against dense one-variable grids; and evaluates positive directional Hessian forms on test vectors. These finite checks are supplementary; all-\(n\) proof is the exact pair-counting and convexity argument above. Run `python3 check_firebreak.py` in the package directory.

## Relationship to prior work

Finney (2001) analyzes geometric placement of fuel-treatment patterns to change fire spread under prescribed fire shapes and directions, rather than a uniformly rooted independent-bond path with continuous protection investments. Wei, Rideout and Kirsch (2008) optimize discrete landscape fuel-treatment decisions in a spatial stochastic loss model. Demange and collaborators (2021) develop graph-theoretic firebreak location with combinatorial edge or vertex removal. These are important motivations and general optimization frameworks, but their inspected formulations do not directly state the parity-dependent continuous-allocation threshold proved here. The related published mathematical result “Exact staircase of optimal two-firebreak gaps on a uniformly ignited cycle” treats **two completely blocked edges on a cycle and independent ignitions at every vertex**, optimizing integer gap length, not continuously distributed transmission suppression along a rooted path. In a single-root uniform-transmission tree epidemic, comparable models optimize a single perfect cut or seed location, also without the present continuous budget. Full coverage of all historical sources is not certified; the precise comparison is model- and implication-specific.

## Limitations

The model is a mathematical benchmark, not a field-calibrated wildfire intervention strategy. Its predicted cutoffs depend on a single uniform ignition, exact path topology, equal patch value, independent transmissions, the exponential response assumption, absence of fire jumping, and a linear homogeneous budget. Altering any of these can change the optimizing support. The theorem establishes only the *first* activation threshold for arbitrary path size and one full four-patch continuation, not all subsequent activation thresholds for larger paths. Computational checks are finite and do not establish infinite-range statements or historical priority. Independent scientific validation has not been performed.

## References

1. M. A. Finney (2001). “Design of Regular Landscape Fuel Treatment Patterns for Modifying Fire Growth and Behavior.” *Forest Science* 47(2):219–228. DOI: 10.1093/forestscience/47.2.219. Lawful full text: https://www.fs.usda.gov/rm/pubs/rmrs_gtr292/2001_finney.pdf. Published May 1, 2001.
2. Y. Wei, D. Rideout and A. Kirsch (2008). “An Optimization Model for Locating Fuel Treatments Across a Landscape to Reduce Expected Fire Losses.” *Canadian Journal of Forest Research* 38:868–877. DOI: 10.1139/X07-162.
3. M. Demange and collaborators (2021). “A graph theoretical approach to the firebreak locating problem.” arXiv:2103.10115. https://arxiv.org/abs/2103.10115.
4. M. A. Finney, J. D. Cohen, I. C. Grenfell and K. M. Yedinak (2010). “An examination of fire spread thresholds in discontinuous fuel beds.” DOI: 10.1071/WF07177. Lawful full text: https://research.fs.usda.gov/download/treesearch/35608.pdf.
5. “Exact staircase of optimal two-firebreak gaps on a uniformly ignited cycle” (2026), openly available mathematical manuscript, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-staircase-of-optimal-two-firebreak-gaps-on-a-uniformly-ign--20549d04bba2.
