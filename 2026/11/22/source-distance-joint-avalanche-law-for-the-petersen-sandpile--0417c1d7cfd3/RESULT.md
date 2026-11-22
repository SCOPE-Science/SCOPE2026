# Source-distance joint avalanche law for the Petersen sandpile

## Finding

Consider the undirected Abelian sandpile on the Petersen graph \(P=KG(5,2)\), with one fixed sink \(s\). Every nonsink vertex has degree three, and a stable configuration has height in \(\{0,1,2\}\). Let \(\mathcal R\) be its recurrent stable configurations with the uniform stationary measure. For each nonsink source \(v\), add one grain, stabilize, and denote by \(M\) the *total number of individual topplings*, including repeats, and by \(L\) the total grains dissipated into \(s\).

There are exactly \(|\mathcal R|=2000\) recurrent configurations. Define the unnormalized bivariate generating polynomial
\[
 A_d(z,w)=\sum_{c\in\mathcal R}z^{M(c,v)}w^{L(c,v)},\qquad d=\operatorname{dist}_P(s,v)\in\{1,2\}.
\]
By the automorphism group of \(P\), this depends on the source only through \(d\). The **complete joint coefficients** of both polynomials are given in the accompanying `JOINT_COUNTS.csv`; there are 14 nonzero pairs \((M,L)\) for \(d=1\) and 30 for \(d=2\). In particular, the two mass marginals are exactly
\[
\begin{aligned}
 A_1(z,1)={}&800+240z+144z^2+105z^3+72z^4+78z^5\\
 &+72z^6+105z^7+144z^8+240z^9,\\
 A_2(z,1)={}&878+77z+72z^2+105z^3+82z^4+112z^5\\
 &+79z^6+108z^7+121z^8+46z^9+107z^{10}\\
 &+48z^{11}+63z^{12}+20z^{13}+25z^{14}+8z^{15}\\
 &+17z^{16}+14z^{17}+2z^{18}+10z^{19}+6z^{24}.
\end{aligned}
\]
The dissipated-grain marginals are
\[
\begin{aligned}
 A_1(1,w)&=800+640w+320w^2+240w^3,\\
 A_2(1,w)&=955+436w+375w^2+157w^3+48w^4+23w^5+6w^6.
\end{aligned}
\]
For sources adjacent to the sink, every site topples at most once, the nine positive mass coefficients are palindromic, and the sharp maximum is \(M=9\), achieved in exactly 240 recurrent states. For sources at distance two, the sharp maximum is \(M=24\), achieved in exactly six recurrent states, always with \(L=6\); the four values \(M=20,21,22,23\) never occur. Thus a change in the source's distance from the sink increases the worst-case total activity from 9 to 24, although both sources lie in a ten-vertex cubic graph. Finally
\[
\mathbb E[M\mid d=1]=3,\qquad\mathbb E[M\mid d=2]=4,
\qquad \mathbb E[L\mid d]=1\quad(d=1,2).
\]
All counts are exact, not sampling estimates.

## Assumptions and scope

Vertices are the ten unordered two-subsets of \(\{0,1,2,3,4\}\), adjacent precisely when disjoint. Choose the sink \(s=\{0,1\}\). Each non-sink toppling removes three grains from its vertex and sends one along each incident edge, with grains sent to \(s\) lost. The sink never topples. At each stationary addition choose any fixed source \(v\ne s\); the stationary distribution is uniform on recurrent stable heights. Sources adjacent to \(s\) are precisely the three two-subsets of \(\{2,3,4\}\); the other six nonsink sources have distance two. The graph is connected and topplings terminate. All stated distributions are conditional on the fixed source class, not on a uniformly random source or on nonzero avalanches.

## Proof

**1. Source orbits.** The permutations of the five underlying labels preserving the pair \(\{0,1\}\) transitively permute the three vertices at distance one and the six vertices at distance two. They preserve the sink, recurrence, the addition dynamics, \(M\) and \(L\); therefore only two fixed-source computations are necessary.

**2. Recurrent-state count and exact characterization.** The Petersen graph has strongly regular parameters \((10,3,0,1)\). Its adjacency matrix satisfies \(A^2+A-2I=J\), so the nontrivial eigenvalues are \(1\) with multiplicity five and \(-2\) with multiplicity four. Kirchhoff's matrix-tree theorem gives
\[
 \tau(P)=\frac{2^5 5^4}{10}=2000.
\]
Dhar's sandpile-group theorem identifies the number of recurrent configurations with this spanning-tree count. Moreover, for the vector \(b\) of edges from each nonsink vertex to \(s\), a stable configuration \(c\) is recurrent exactly when stabilizing \(c+b\) topples each nonsink vertex exactly once. Equivalently, there is no nonempty subset \(U\) of nonsink vertices for which every \(i\in U\) has \(c_i<\deg_U(i)\). Both equivalent recurrence tests are used independently in the verifiers.

**3. Exhaustive joint polynomial certificate.** Every stable configuration is one of exactly \(3^9=19683\) integer vectors. The complete procedure is finite: enumerate all vectors, retain exactly those satisfying the burning criterion, then add one grain at a representative source in each distance class, perform legal topplings until all heights are at most two, and record \((M,L)\). The first verifier constructs \(KG(5,2)\) from disjoint two-subsets and topples one unstable vertex at a time. The second constructs the isomorphic generalized Petersen graph \(GP(5,2)\), identifies recurrence by successive deletion of vertices from every forbidden candidate set, and topples all currently unstable vertices in parallel. Both independently return the same 2000 recurrent states and the 44 exact joint coefficient records in `JOINT_COUNTS.csv`. The displayed marginals are the literal sums of these records; the finite enumeration certifies the absence of other pairs as well as the positive counts. Each routine uses integer arithmetic only and terminates on this connected graph with a sink.

**4. Sharp maxima without statistical extrapolation.** Stabilization is monotone in the initial configuration's heights: a componentwise larger initial stable configuration cannot produce fewer topplings at any vertex after the same addition. Thus the all-two configuration bounds every avalanche odometer from above; it is itself recurrent by the burning criterion. For a source adjacent to \(s\), its avalanche topples each of the nine nonsink vertices once, leaving stable heights. For a source at distance two, its avalanche topples each of the three sink-neighbors twice and each of the six distance-two vertices three times. One can check these vectors by direct legal parallel relaxation from the all-two configuration, as in either verifier. Therefore these are the sharp maxima \(9\) and \(24\). The exact counts of maximizers and the missing intermediate values follow from the complete joint coefficient certificate.

**5. Mean activity and dissipation checks.** Dhar's Green-function identity says that the expected firing vector is the column of the inverse reduced Laplacian corresponding to the source. By symmetry, the solution to the reduced Poisson problem \(\Delta u=\mathbf1\) has values \(u_1\) and \(u_2\) on the near and far shells. They obey \(3u_1-2u_2=1\) and \(u_2-u_1=1\), hence \((u_1,u_2)=(3,4)\). Conservation in the uniform stationary recurrent measure gives unit mean sink dissipation for either source. These agree independently with the polynomial derivatives at \((z,w)=(1,1)\).

## Verification

Run `python verify_kneser.py` and `python verify_prism.py` from the directory containing `JOINT_COUNTS.csv`. Each is a complete Python-standard-library verifier; no external scientific package or network access is needed. Both verify all 44 joint coefficients, exactly 2000 recurrent configurations, conservation on every trial, and the maximum total toppling count in each source class. The complete fixed graph is defined in each program, not loaded from a prior calculation. The first uses the Kneser construction plus sequential stabilization; the second uses the generalized Petersen construction plus forbidden-subconfiguration recurrence and simultaneous stabilization. For each source the coefficients sum to 2000, their dissipation-weighted sum is 2000, and their mass-weighted sums are 6000 and 8000 respectively.

## Relationship to prior work

Dhar established the general Abelian sandpile model, uniform recurrent stationary measure and inverse-Laplacian mean-toppling law. Austin, Chambers, Funke, García Puente and Keough developed multivariate avalanche polynomials and exact classifications for trees, cycles, wheels and complete graphs, but their inspected text does not state the two-source, joint toppling/dissipation coefficients on the Petersen graph. Generic sandpile software can in principle enumerate the data; its availability is not an explicit prior determination of the numerical distribution. Other finite-graph results, including a source-distance-resolved icosahedral sandpile calculation and a \(K_{2,n}\) avalanche law, concern different graph families and do not imply the displayed 44 Petersen-specific coefficients. The 240 system-spanning, sink-neighbor-driven events are consistent with previously known general full-avalanche identities and are not independently claimed as new. The contribution is the *complete joint source-distance census and its sharp exceptional tail* on this canonical cubic nonplanar graph.

## Limitations

This is an exact finite-graph statement, not an infinite-volume scaling theorem or a claim of universal critical exponents. The positive mass-coefficient palindrome is a finite identity; no universal palindromicity theorem is asserted. The proof uses a finite exhaustive arithmetic certificate for the full joint distribution and analytic arguments for recurrence count, source orbits, maxima and means. Exact historical priority has not been independently certified; an unlocated explicit Petersen table, including one generated by software, would alter the originality assessment. Neither simulations nor finite partial searches are used as proofs of infinite claims.

## References

1. D. Dhar, "Self-organized critical state of sandpile automaton models," *Physical Review Letters* **64** (1990), 1613–1616, https://doi.org/10.1103/PhysRevLett.64.1613 . First publicly dated 1990-04-02.
2. D. Austin, M. Chambers, R. Funke, L. D. García Puente, L. Keough, "The Avalanche Polynomial of a Graph," arXiv:1605.02713, first public version 2016-05-09, https://arxiv.org/abs/1605.02713 .
3. SageMath, *Sandpiles* reference, `Sandpile(graphs.PetersenGraph(),1)` example and `avalanche_polynomial` method, https://doc.sagemath.org/html/en/reference/dynamics/sage/sandpiles/sandpile.html .
