# Three independent extreme scales in one-dimensional nearest-neighbor geometry

## Finding

Let \(X_1,\ldots,X_n\) be independent uniform points in \((0,1)\), with order statistics \(X_{(1)}<\cdots<X_{(n)}\). Write \(D_i=X_{(i+1)}-X_{(i)}\) for \(1\le i\le n-1\). Define \(A_n=\max_i D_i\), \(B_n\) as the largest directed nearest-neighbor edge length (the largest distance of any sampled point to its nearest distinct sampled point), and \(C_n\) as the largest length of an unordered **mutual** nearest-neighbor edge (each endpoint is the other's nearest point). Ties have probability zero. For all real \(x,y,z\),

\[
\lim_{n\to\infty}\Pr\left\{\begin{array}{l}
nA_n-\log(n-1)\le x,\\
2nB_n-\log(n-2)\le y,\\
3nC_n-\log((n-3)/3)\le z
\end{array}\right\}
=\exp\{-e^{-x}-e^{-y}-e^{-z}\}.
\]

Thus the three centered extremes converge jointly to **independent standard Gumbel laws**, while their uncentered leading scales are respectively \((\log n)/n\), \((\log n)/(2n)\), and \((\log n)/(3n)\). In particular, reciprocal-neighbor edges have a third, strictly shorter extremal scale not determined by the marginal extreme nearest-neighbor length.

## Assumptions and scope

All points are independent, continuously distributed, uniform on the *fixed* unit interval. The nearest-neighbor relation uses ordinary absolute distance, points at the two interval endpoints are not artificially inserted, and only actual interpoint gaps are eligible for \(A_n\) or \(C_n\). The asymptotic statement is for integer \(n\to\infty\), with \(n\ge5\); threshold variables are arbitrary fixed real numbers. It is a joint weak limit, not a finite-\(n\) independence statement or a theorem for nonuniform densities, higher dimensions, or ties.

## Proof

**1. Exact reduction to local spacing events.** Set \(m=n-1\). For any distinct positive \(d_1,\ldots,d_m\), the directed nearest neighbor of an interior point chooses the shorter of its two adjacent gaps; at either extreme sampled point the sole adjacent gap is chosen. Consequently,

\[
B_n=\max\left\{D_1,D_m,\min(D_i,D_{i+1}):1\le i<m\right\}.
\]

An interior edge between points \(i\) and \(i+1\), for \(2\le i\le m-1\), is mutual exactly when \(D_i<D_{i-1}\) and \(D_i<D_{i+1}\). The first edge is mutual exactly when \(D_1<D_2\), and the last exactly when \(D_m<D_{m-1}\). Therefore \(C_n\) is the maximum among these locally minimal spacings, including the two one-sided boundaries. At least one such edge exists, since the globally smallest gap is always reciprocal.

**2. Independent exponential representation and rare-event rates.** Let \(E_0,\ldots,E_n\) be independent unit-rate exponentials and \(S=\sum_{j=0}^n E_j\). The \(n+1\) unit-interval gaps, including the two outside the extreme sampled points, have the Dirichlet representation \((E_0/S,\ldots,E_n/S)\). Thus \((D_1,\ldots,D_m)\) has the same law as \((E_1/S,\ldots,E_m/S)\). All the comparisons defining reciprocity depend only on \(E_1,\ldots,E_m\).

For fixed \(x,y,z\) introduce the three thresholds

\[
u_1=\log(n-1)+x,\quad
u_2=\tfrac12(\log(n-2)+y),\quad
u_3=\tfrac13(\log((n-3)/3)+z).
\]

For sufficiently large \(n\) they are positive and satisfy \(u_1>u_2>u_3\). Form three collections of rare events:

\[
\begin{split}
\mathcal A_i&=\{E_i>u_1\},&&1\le i\le m,\\
\mathcal B_i&=\{E_i>u_2,E_{i+1}>u_2\},&&1\le i<m,\\
\mathcal C_i&=\{E_{i-1}>E_i>u_3,\ E_{i+1}>E_i\},&&2\le i\le m-1.
\end{split}
\]

The probabilities are, exactly,

\[
\Pr(\mathcal A_i)=e^{-u_1},\qquad
\Pr(\mathcal B_i)=e^{-2u_2},\qquad
\Pr(\mathcal C_i)=\int_{u_3}^{\infty}e^{-3t}\,dt=\tfrac13e^{-3u_3}.
\]

Hence the expected counts of \(\mathcal A\), \(\mathcal B\), \(\mathcal C\) are exactly \(e^{-x},e^{-y},e^{-z}\), respectively.

**3. A joint three-color Poisson limit.** Two events from these collections are independent when they use disjoint exponential coordinates. Each depends on at most three consecutive coordinates, so the overlap graph of event sites has uniformly bounded degree. Distinct overlapping sites have negligible simultaneous occurrence. Same-color overlaps satisfy

\[
\Pr(\mathcal B_i\cap\mathcal B_{i+1})\le e^{-3u_2}=O(n^{-3/2}),
\quad
\Pr(\mathcal C_i\cap\mathcal C_{i+1})=0,
\quad
\Pr(\mathcal C_i\cap\mathcal C_{i+2})\le e^{-5u_3}=O(n^{-5/3}).
\]

Distinct \(\mathcal A\) events use different coordinates. For mixed overlapping sites the following uniform bounds follow by listing the distinct coordinates required to exceed the appropriate threshold:

\[
\Pr(\mathcal A_i\cap\mathcal B_j)\le e^{-u_1-u_2}=O(n^{-3/2}),\quad
\Pr(\mathcal A_i\cap\mathcal C_j)\le e^{-u_1-2u_3}=O(n^{-5/3}),\quad
\Pr(\mathcal B_i\cap\mathcal C_j)\le e^{-2u_2-u_3}=O(n^{-4/3}).
\]

For the last estimate the two \(\mathcal B\) coordinates must exceed \(u_2\), while the three \(\mathcal C\) coordinates must exceed \(u_3\); at least one of the latter is distinct. If an event pair is disjoint, independence applies instead. For each fixed total order of a mixed factorial moment, terms whose event windows are all disjoint factor, and their sum converges to the corresponding product of limiting means. In the other terms, group windows into connected components of the overlap graph. Each component has at most a bounded number of positions given one anchor; a singleton contributes \(O(n^{-1})\), while a component with two or more events contributes at most \(O(n^{-4/3})\) by selecting one overlapping distinct pair. There are \(O(n)\) placements per component, and disjoint components are independent. Thus the total contribution from any pattern with a nonsingleton component is \(O(n^{-1/3})\). All joint factorial moments consequently converge to those of three independent Poisson variables with means \(e^{-x},e^{-y},e^{-z}\). Their joint distribution is determined by these moments, and the vector of event counts converges jointly to this independent-Poisson vector.

**4. End effects and denominator.** The events that a boundary directed nearest-neighbor length exceeds \(u_2\) have total probability at most \(2e^{-u_2}=O(n^{-1/2})\). The boundary reciprocity event has probability \(\Pr(E_1>u_3,E_2>E_1)=\tfrac12e^{-2u_3}=O(n^{-2/3})\), and similarly at the right boundary. Hence they do not change the limiting count of exceedances. The event that each of the three geometric maxima is below its respective threshold, in **exponential** coordinates, is equivalent up to an event of vanishing probability to all three Poisson counts being zero. This gives \(\exp(-e^{-x}-e^{-y}-e^{-z})\).

Finally \(S/n\to1\) in probability and \(S-n=O_{\Pr}(\sqrt n)\). All three maxima in exponential coordinates are bounded by \(\max_{1\le i\le m}E_i=O_{\Pr}(\log n)\). Multiplication by \(n/S\) changes each centered, fixed-coefficient maximum by \(O_{\Pr}((\log n)/\sqrt n)=o_{\Pr}(1)\). Applying the multivariate Slutsky theorem proves the joint assertion for the actual sample spacings. \(\square\)

## Verification

The independent checker `verify_extremes.py` reconstructs directed nearest neighbors for every ordering of \(3\) through \(7\) distinct internal gaps (sample sizes \(4\) through \(8\)), and checks agreement with all three spacing formulas. It also checks the single-event exponential integrals, finite overlapping-window implications, and a seeded finite-size Monte Carlo comparison against the three-Gumbel joint CDF. Run with `python verify_extremes.py` in an environment with NumPy and SciPy. The checker performs 142,730 finite combinatorial assertions and 10 numerical-integral comparisons; Monte Carlo is diagnostic only. The infinite-dimensional step is established by the proof above, not by enumeration or simulation.

## Relationship to prior work

Gupta and Iyer (arXiv:math/0604599, initially public 2006-04-27, primary MSC 60D05/60G70) study the *single* longest nearest-neighbor link for exponentially-tailed distributions in dimensions at least two, and discuss older nearest-neighbor extrema results. Bahadır and Ceyhan (arXiv:1605.01940, initially public 2016-05-06) fully analyze the *number* of reflexive and shared nearest-neighbor pairs for uniform points on a line, including their local-minimum encoding, finite count distribution, law of large numbers and CLT. Neither of those inspected analyses gives the three separate extremal scales, the maximum length of a reciprocal pair, or the joint independence law. General locally-dependent Poisson approximation supplies a method, but the explicit three-level windows, the third normalization, and the simultaneous overlap bounds are additional hypotheses and computations specific to this result. Marginal results for longest spacings and outgoing nearest-neighbor links are not asserted as new.

## Limitations

The leading-order one- and two-gap extreme laws are classical; the contribution assessed here is the mutual-edge extremal scale and the *joint* independence of all three centered extremes. No finite-sample independence, quantitative convergence rate, robustness under nonuniform densities, or higher-dimensional universality is proved. The theorem's priority has not been independently certified; a broader unlocated marked-extremes theorem might subsume the joint statement. Computational checks cannot exclude such historical coverage.

## References

1. B. Gupta and S. K. Iyer, *Criticality of the Exponential Rate of Decay for the Largest Nearest Neighbor Link in Random Geometric Graphs*, arXiv:math/0604599 (first version 2006-04-27), https://arxiv.org/abs/math/0604599.
2. S. Bahadır and E. Ceyhan, *On the Number of Reflexive and Shared Nearest Neighbor Pairs in One-Dimensional Uniform Data*, arXiv:1605.01940 (first version 2016-05-06), https://arxiv.org/abs/1605.01940.
3. M. D. Penrose, *A Strong Law for the Largest Nearest-Neighbour Link between Random Points*, Journal of the London Mathematical Society 60 (1999), 951–960, https://doi.org/10.1112/S0024610799008157.
4. H. Dette and N. Henze, *The Limit Distribution of the Largest Nearest-Neighbour Link in the Unit d-Cube*, Journal of Applied Probability (1989), https://doi.org/10.2307/3214317 (prior marginal extreme-value work; consult original publication details rather than web-posting dates).
