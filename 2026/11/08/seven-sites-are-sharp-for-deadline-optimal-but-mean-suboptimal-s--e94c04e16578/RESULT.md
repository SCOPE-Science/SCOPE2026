# Seven sites are sharp for deadline-optimal but mean-suboptimal SI surveillance on trees

## Finding

For a finite unweighted tree, begin a continuous-time susceptible–infected (SI) epidemic at one uniformly selected vertex. Each infected–susceptible edge independently transmits at rate one; no vertex recovers. Monitor exactly one fixed vertex perfectly and continuously, and write \(T_v\) for the time until that vertex first becomes infected, including \(T_v=0\) when it is the initial seed.

**Sharp cutoff.** On **every** tree with at most six vertices, every vertex minimizing the positive-deadline miss probability \(\Pr(T_v>t)\), for every fixed \(t>0\), also minimizes the mean \(\mathbb E[T_v]\). At seven vertices this assertion is false. On the seven-vertex broom
\[
E=\{\{0,1\},\{1,2\},\{2,3\},\{3,4\},\{0,5\},\{0,6\}\},
\]
the unique mean-optimal sentinel is vertex \(1\). For positive deadlines, the *unique* miss-probability-optimal sentinel is vertex \(0\) when \(0<t<t_*\), vertex \(1\) when \(t>t_*\), and exactly the pair \(\{0,1\}\) tie at
\[
t_* =\frac{\sqrt{33}-3}{2}=1.372281323\ldots.
\]
The mean values at these two sites are \(\mathbb E[T_0]=12/7\) and \(\mathbb E[T_1]=11/7\). Consequently, under the stated assumptions seven is the minimum tree order for a uniquely deadline-optimal sentinel to be strictly suboptimal in mean time.

## Assumptions and scope

A tree here is finite, simple, connected, undirected and unweighted. Every directed infected-to-susceptible edge has homogeneous exponential transmission rate one. All transmissions are independent; infection is permanent. The initial infected vertex is sampled uniformly from the vertex set and is independent of the transmission clocks. One perfect, continuously monitored vertex is chosen before the outbreak. No other intervention or transmission cutoff is assumed. The deadline is a fixed strictly positive real number, and the result concerns every tree order from one through six plus the explicit seven-vertex witness. No universality for cyclic graphs, heterogeneous rates, recovery or multiple sentinels is claimed.

## Proof

**First-passage identity.** For vertices \(u,v\) on a tree, the unique simple path from \(u\) to \(v\) has length \(d(u,v)\). With initial infection at \(u\), every successive path edge is crossed after an independent exponential waiting time of rate one. There is no alternate route in a tree. Therefore \(T_v\), conditional on seed \(u\), is the sum of \(d(u,v)\) independent unit exponentials, with the empty sum equal to zero. In particular,
\[
\mathbb E[T_v]=\frac1n\sum_{u\in V}d(u,v),\qquad
\Pr(T_v>t)=\frac{e^{-t}}n P_v(t),
\]
where
\[
P_v(t)=\sum_{u\ne v}\sum_{j=0}^{d(u,v)-1}\frac{t^j}{j!}
=\sum_{j=0}^{n-2}c_j(v)\frac{t^j}{j!},\qquad
c_j(v)=\bigl|\{u\in V:d(u,v)>j\}\bigr|.
\]
The equality includes the initially monitored case via \(T_v=0\). Mean-optimal vertices are precisely graph medians, i.e. minimizers of the total distance \(\sum_u d(u,v)\).

**Exhaustive lower bound through six vertices.** The accompanying dependency-free program `verify.py` generates all labeled trees of orders \(1\) through \(6\), using the inverse Prüfer encoding for orders at least two. Every labeled tree on \(n\ge2\) vertices has a unique Prüfer sequence of length \(n-2\) over the \(n\) vertex labels: repeatedly delete the smallest labeled leaf and record its neighbor; the stated decoder reverses that procedure. Thus enumerating all \(n^{n-2}\) sequences is exhaustive, not random sampling. The counts per order are \(1,1,3,16,125,1296\), a total of \(1442\) labeled trees including the one-vertex case.

For **each** enumerated tree, the program determines graph distances by breadth-first search, obtains all medians from exact integer distance sums, and verifies this stronger finite certificate: for every nonmedian \(w\), there is a median \(m\) with \(c_j(m)\le c_j(w)\) for all \(j\), and strict inequality for at least one \(j\). Since all \(t^j/j!\) are nonnegative and all are strictly positive for \(t>0\), it follows that \(P_m(t)<P_w(t)\) at every positive deadline. Hence no nonmedian can be deadline-optimal on a tree of at most six vertices. This exhausts exactly the finite range asserted; it does not extrapolate a finite check to arbitrary tree size.

**Seven-vertex witness and complete phase diagram.** On the stated broom, the total-distance sums for vertices \(0,1,2,3,4,5,6\) are
\[
(12,11,12,15,20,17,17),
\]
so vertex \(1\) alone minimizes the mean. The miss-polynomial coefficients in the basis \(t^j/j!\), for \(j=0,\ldots,5\), are
\[
\begin{array}{c|rrrrrr}
v&c_0&c_1&c_2&c_3&c_4&c_5\\\hline
0&6&3&2&1&0&0\\
1&6&4&1&0&0&0\\
2&6&4&2&0&0&0\\
3&6&4&3&2&0&0\\
4&6&5&4&3&2&0\\
5,6&6&5&3&2&1&0
\end{array}.
\]
Every vertex \(v\in\{2,3,4,5,6\}\) is coefficientwise strictly dominated by vertex \(1\), so none minimizes miss probability at any positive deadline. For the only remaining candidates,
\[
P_0(t)-P_1(t)=-t+\frac{t^2}{2}+\frac{t^3}{6}
=\frac{t}{6}(t^2+3t-6).
\]
For \(t>0\), the quadratic has exactly one zero, \(t_*=(\sqrt{33}-3)/2\); it is negative before and positive after that zero. The claimed two optimal phases and unique tie follow. This is the required seven-vertex counterexample, completing sharpness.

## Verification

Run `python3 verify.py` using only the Python standard library. The first component checks all \(1442\) labeled trees through six vertices with exact integer coefficients, including the required strict component. The second checks the exact broom distance vectors and polynomial coefficients. A separately derived subset-state continuous-time Markov chain, with 128 possible infected subsets and rational Laplace parameters \(s\in\{1,2,3\}\), is solved by backward recursion and agrees with the distance-based Laplace expression for all seven monitored vertices (21 exact comparisons). These finite Laplace comparisons independently check the stochastic model implementation; the analytic first-passage identity, not those sampled transforms, proves the all-deadline result.

## Relationship to prior work

Leskovec et al. (2007) establish a general outbreak-sensor placement framework, including detection-delay objectives, but do not give this exact homogeneous SI-tree deadline classification. Bhamidi, van der Hofstad and Komjathy (arXiv:1401.0914, first public version January 5, 2014) analyze epidemic spread through first-passage percolation on sparse random graphs and provide the earlier epidemic-process motivation. Brandes and Hildenbrand (2014) study distinctions among classical vertex-centrality measures; degree and closeness are related to the limiting and mean criteria here, but a centrality comparison alone does not state the full stochastic deadline order or the transition \(t_*\). Holme (2017) gives exact small-graph comparisons for SIR epidemic node importance, including mean sentinel detection, under different recovery and objective assumptions. The new claim is strictly the minimal-order finite-tree all-deadline theorem, together with the full exact seven-site phase diagram. Historical priority remains provisional; one especially relevant centrality note was accessible only through its bibliographic material and abstract.

## Limitations

The result is confined to homogeneous unit-rate SI transmission, uniform one-site seeding, one continuously observed perfect sentinel, and trees. For every positive homogeneous rate \(\beta\), the time variable simply rescales to \(\beta t\); no heterogeneous-rate conclusion is asserted. The lower-bound proof is a complete finite Prüfer enumeration, not a structural classification of arbitrarily large trees. The computed exact identities do not empirically validate a particular real surveillance network. Uninspected full texts could affect historical originality, and independent verification is not claimed.

## References

1. Leskovec, J., Krause, A., Guestrin, C., Faloutsos, C., VanBriesen, J., and Glance, N. (2007), *Cost-effective outbreak detection in networks*, ACM KDD. https://doi.org/10.1145/1281192.1281239 ; lawful extended technical report https://www-cs.stanford.edu/~jure/pubs/detect-techRept.pdf
2. Bhamidi, S., van der Hofstad, R., and Komjathy, J. (2014 preprint), *The front of the epidemic spread and first passage percolation*, arXiv:1401.0914v1, first posted 2014-01-05. https://arxiv.org/abs/1401.0914
3. Brandes, U., and Hildenbrand, J. (2014), *Smallest graphs with distinct singleton centers*, *Network Science* 2(3), 416–418. https://doi.org/10.1017/nws.2014.25
4. Holme, P. (2017), *Three faces of node importance in network epidemiology: Exact results for small graphs*, arXiv:1708.06456. https://arxiv.org/abs/1708.06456
