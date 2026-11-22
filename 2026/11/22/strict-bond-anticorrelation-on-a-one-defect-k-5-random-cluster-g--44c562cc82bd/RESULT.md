# Strict bond anticorrelation on a one-defect \(K_5\) random-cluster graph

## Finding
Let \(G=K_5\), with a distinguished bond \(d=\{0,1\}\). Every other bond has positive edge activity \(v\), and \(d\) has arbitrary independent activity \(w>0\). Under the Fortuin–Kasteleyn random-cluster law of cluster weight \(0<q<1\), **every pair of distinct edge-occupation indicators is strictly negatively correlated**, for every \(v,w>0\). In particular, the conclusion holds on both sides of the equal-bond line \(v=w\), including the small-activity region excluded by known complete-graph sufficient conditions.

For distinct bonds \(e,f\), with activities \(x_e,x_f\in\{v,w\}\), there is an explicitly certified strictly positive polynomial expression \(P_{ef}(q,v,w)\) such that
\[
\operatorname{Cov}(X_e,X_f)=-\frac{x_ex_fq^2(1-q)P_{ef}(q,v,w)}{Z(q,v,w)^2}<0.
\]
Here \(P_{ef}\) has integer coefficients, possibly including two negative coefficients in one symmetry type, but is positive on the entire indicated parameter domain. All coefficient tables are in `CERTIFICATE.json`.

## Assumptions and scope
Set \(V=\{0,1,2,3,4\}\), with edges ordered lexicographically as \((01,02,03,04,12,13,14,23,24,34)\). For a subset \(A\subseteq E\), write \(k(A)\) for the number of connected components of \((V,A)\), including isolated vertices, and \(h(A)=\mathbf1_{\{01\in A\}}\). Define
\[
Z(q,v,w)=\sum_{A\subseteq E}q^{k(A)}v^{|A|-h(A)}w^{h(A)},\qquad
\mathbb P(A)=\frac{q^{k(A)}v^{|A|-h(A)}w^{h(A)}}{Z(q,v,w)}.
\]
All assertions quantify over \(0<q<1\), \(v>0\), \(w>0\) and all \(\binom{10}{2}=45\) unordered distinct edge pairs. The claim does not extend to arbitrary independently varying activities on the other nine bonds, to other graphs, or to the endpoint \(q=1\) where independent bonds have zero covariance.

## Proof
**1. Four-cell Rayleigh differences.** Fix different edges \(e,f\). Split each edge configuration into its two marked occupation bits \((i,j)\in\{0,1\}^2\). Let
\[
Z_{ij}=\sum_{A:\,X_e=i,\,X_f=j}q^{k(A)}\prod_{g\in A\setminus\{e,f\}}x_g,
\]
where the marked activities have been stripped from the summands. Direct expansion of the multiaffine partition function gives
\[
\operatorname{Cov}(X_e,X_f)=-\frac{x_ex_f}{Z^2}(Z_{10}Z_{01}-Z_{00}Z_{11}).
\]
For each marked pair, the four sums have at most \(2^8\) contributing configurations each, and together they enumerate all \(2^{10}=1024\) edge subsets. Consequently, the following polynomial identities can be checked by exact integer coefficient arithmetic, not by sampling parameter values.

**2. Orbit reduction and factor certificate.** The automorphisms preserving the distinguished edge form \(S_2\times S_3\), acting on the two endpoints of \(d\) and the other three vertices. The 45 distinct edge pairs split into eight orbits represented by edge-index pairs
\[
(0,1),(0,7),(1,2),(1,4),(1,5),(1,7),(1,9),(7,8),
\]
with respective orbit sizes \(6,3,6,3,6,12,6,3\). Exhaustively expanding the four cells and dividing by \(q^2(1-q)\) gives the exact integer polynomial identity
\[
Z_{10}Z_{01}-Z_{00}Z_{11}=q^2(1-q)P_{ef}(q,v,w)
\]
for every representative. The eight quotient polynomials have respectively \(32,28,82,82,76,82,68,78\) nonzero terms, stored as triples of exponents plus an integer coefficient in `CERTIFICATE.json`. `verify.py` recomputes the entire certificate from the 1024 subsets and checks multiplication back to the original Rayleigh differences.

**3. Positivity.** For seven of the eight orbit types, every coefficient of \(P_{ef}\) is nonnegative and at least one is strictly positive. For the sole exceptional orbit \((1,5)\), corresponding to disjoint ordinary bonds \(02\) and \(13\), all coefficients of positive powers of \(q\) are nonnegative. Its \(q^0\) coefficient \(P_0\) satisfies the exact identity
\[
P_0(v,w)=25v^4(v-w)^2+v^5(84v^2-20vw+96w^2)+R(v,w),
\]
where the remainder \(R\) is a sum of 14 monomials with strictly positive integer coefficients. It is the remainder obtained by subtracting these two displayed terms from the \(q^0\) entries of the certificate; the exact 14 entries are reproducibly checked by `verify.py`. The quadratic \(84v^2-20vw+96w^2\) is strictly positive for \(v,w>0\), since its discriminant is \(400-4\cdot84\cdot96<0\). Thus \(P_0(v,w)>0\), and so \(P_{1,5}(q,v,w)>0\) for all positive \(q,v,w\). Every orbit therefore has \(P_{ef}(q,v,w)>0\). Since \(x_e,x_f,q,Z\) and \(1-q\) are positive on the specified domain, the covariance is strictly negative, proving the theorem.

## Verification
The package includes `verify.py` and `CERTIFICATE.json` (Python 3 standard library only). Run `python verify.py` alongside `CERTIFICATE.json` to regenerate the full polynomial coefficient certificates and confirm their exact agreement with the stored tables; the verifier checks all eight orbits, all 45 pair positions by orbit completeness, the exceptional positive-square decomposition, and the polynomial factorization. It additionally performs 540 exact-rational covariance comparisons on a twelve-point parameter grid covering all 45 pairs. The successful run printed `K5_RANDOM_CLUSTER_CERTIFICATE_PASSED edge_pair_orbits=8 edge_pairs=45 coefficient_counts=32,28,82,82,76,82,68,78 exact_covariance_comparisons=540`. The finite graph is exhausted exactly; no finite parameter grid is used as a substitute for the global polynomial positivity proof.

## Relationship to prior work
Grimmett and Winkler (2003) studied negative association for uniform forests and connected subgraphs, motivating the edge-dependence question. Semple and Welsh (2005) established matroidal negative-correlation closure properties, including a class based on \(K_4\), and noted the difficulty of weighted computations even on \(K_5\); their result concerns the independent/spanning ensembles, not this full \(q\)-random-cluster interval. Çiçeksiz and Ravichandran (2026) prove negative edge correlation on complete graphs when all edge weights are at least \(2\), and, for a common weight, when that weight is at least \(1\). Neither sufficient condition covers arbitrary \(v,w>0\), in particular \(v\ll1\) and \(w\ne v\). Zhao and Zhou (2026) establish all-weight \(Z\)-Rayleigh correlation for matroids of rank or corank at most three. The cycle matroid of \(K_5\) has rank four and corank six, and hence lies outside their hypothesis. Published exact certificates on the five-vertex wheel and the complete bipartite \(K_{3,3}\) concern different graphs and specializations. This comparison concerns logical implication, not titles or merely different numbers.

## Limitations
The result proves pairwise edge anticorrelation only, not full negative association or the analogous claim on all graphs. Eight finite exact polynomial certificates, with an explicit positivity decomposition for the exceptional orbit, prove the parameter-uniform statement; the polynomial tables themselves are necessary to reproduce the computations. Historical priority is provisional because searches and source inspections are bounded, and a broader unexamined specialization could subsume the claim. No external independent scientific audit has been performed.

## References
1. G. Grimmett and S. Winkler, *Negative association in uniform forests and connected graphs* (first public 2003-02-17), https://arxiv.org/abs/math/0302185.
2. C. Semple and D. Welsh, *Negative correlation in graphs and matroids* (2005 preprint), https://ir.canterbury.ac.nz/bitstreams/7d5d8de7-9541-4d93-b990-be18fbed62e0/download.
3. R. A. Çiçeksiz and M. Ravichandran, *Negative Correlations for Forests and the \(q<1\) Random Cluster Model* (first public 2026-09-30), https://arxiv.org/abs/2610.00549.
4. Q. Zhao and X. Zhou, *Every rank-three matroid is Z-Rayleigh* (first public 2026-11-11), https://arxiv.org/abs/2611.15512.
5. Tang and Zhang, *Pairwise correlation bounds for the random-cluster model with cluster weight at most one* (2026), https://arxiv.org/abs/2611.11993.
