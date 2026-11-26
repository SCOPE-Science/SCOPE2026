# Secure-guard spectra and exact relocation distances on the Pappus incidence graph

## Finding

For the 18-vertex Pappus incidence graph \(H\) specified below, the complete labelled secure-domination cardinality polynomial is
\[
\begin{aligned}
D_{\rm sec}(H;z)={}&1755z^8+13088z^9+24624z^{10}+24948z^{11}\\
&+16899z^{12}+8316z^{13}+3042z^{14}+816z^{15}\\
&+153z^{16}+18z^{17}+z^{18}.
\end{aligned}
\]
The total is \(93660\). The inclusion-minimal secure-domination cardinality polynomial is
\[
M_{\rm sec}(H;z)=1755z^8+3224z^9.
\]
In particular, the known minimum size is eight, and the only inclusion-minimal configurations that are not minimum have size nine. There are exactly \(3224\) of these. The contribution is the census across **all** subset sizes and the exact description of the nonminimum, inclusion-minimal part. Optimum-set orbits and relocation metrics below are benchmarks of the enumeration, not separate claims of originality.

## Assumptions and scope

Use point vertices \(P(x,y)\) and line vertices \(L(m,b)\), with \(x,y,m,b\in\mathbb F_3\). The only edges are \(P(x,y)L(m,b)\) for \(y=mx+b\). This is the Levi graph, not the nine-vertex point-collinearity graph [3]. The labels are distinguished in the polynomials.

Let \(N[v]\) be the closed neighborhood. A set \(S\) dominates if \(\bigcup_{v\in S}N[v]=V(H)\). It is secure dominating if it dominates and for every \(u\notin S\), some adjacent \(v\in S\) has \((S\setminus\{v\})\cup\{u\}\) dominating. A secure set is inclusion-minimal if no proper subset is secure.

## Proof by exhaustive enumeration

For a **dominating** set \(S\) and \(v\in S\), define \(\operatorname{priv}_{S}(v)=\{w:N[w]\cap S=\{v\}\}\). When \(v\) is removed, exactly these vertices lose their last selected closed neighbor. For adjacent \(v\in S\) and \(u\notin S\), the proposed swap dominates precisely when \(\operatorname{priv}_{S}(v)\subseteq N[u]\). The enumeration tests the same condition by computing the covering mask of the swapped set, not by assuming the swap is secure or that it can respond to later attacks.

Give \(P(x,y)\) label \(3x+y\) and \(L(m,b)\) label \(9+3m+b\). Visit the integers \(0\) through \(2^{18}-1\), viewing each as one selected mask. Let \(C_v\) be the closed-neighborhood mask of vertex \(v\). The cover of the empty mask is zero, and the cover of a nonempty mask \(s\) is the bitwise union of \(C_v\) and the cover of \(s\) with its least set bit \(v\) removed. This recurrence is exact by induction on the number of selected vertices. Discard every mask whose cover is not full. For each other mask and each unset position \(u\), visit every selected neighbor \(v\) of \(u\) until a swap with full cover is found; otherwise discard the mask. Count each surviving mask once in the bin for its number of set bits. Thus every subset is tested against exactly the secure predicate, which gives \(D_{\rm sec}\).

Adding vertices preserves security. Indeed, if \(S\subseteq T\) and \(u\notin T\), a defender \(v\in S\) for \(u\) in \(S\) also defends in \(T\): the new dominating set is a superset of the old one after the same swap. Consequently a secure set is inclusion-minimal exactly when every one-vertex deletion destroys security; a secure proper subset of \(S\) would also lie in a secure one-vertex deletion. Check membership in the accepted-mask list after every such deletion for each accepted mask. This supplies \(M_{\rm sec}\), including the exclusion of all sizes above nine.

## Optimum-class benchmarks

The size-eight class is also the all-singleton sector of the weight-eight weak Roman optima [5]. A weak Roman unit transfer from a singleton defender to an unoccupied vertex yields a function whose support is exactly the swapped set. Thus weak Roman feasibility for singleton functions is equivalent to secure domination of their supports. The companion record gives \(1755\) such optima and the full orbit split of one orbit of size \(27\), eight of size \(108\), and four of size \(216\). Its prior-work discussion also reports \(12798\) jump edges and \(4320\) slide edges for this sector. The two same-dated records do not establish the direction of precedence; the overlap in the statistic is exact.

The bundled enumeration reproduces these optimum-class counts. Two distinct optimum masks are joined by a jump exactly when their symmetric difference has size two; for a slide the two differing positions must be adjacent in \(H\). On these induced graphs (not the enlarged weighted-optimum graphs), breadth-first search from each optimum reaches all others. The jump eccentricities are all eight; in the slide graph \(1539\) are nine and \(216\) are ten. Thus the respective radius–diameter pairs are \((8,8)\) and \((9,10)\). These are reproducibility checks derived from the same optimum class, not the basis for distinguishing this census from [5].

For the orbit check, the maps \((x,y)\mapsto (ax+b,cx+dy+e)\) with \(a,d\ne0\) over \(\mathbb F_3\) induce \(108\) distinct point-preserving automorphisms. The incidence duality \(P(x,y)\leftrightarrow L(x,-y)\) gives another \(108\); the established order of the full group is \(216\) [4]. Applying these maps to optimum masks gives the indicated orbits.

## Verification

Run `python3 verify.py` to reproduce both polynomials and the optimum-class benchmarks, using Python 3 with no third-party packages. The program prints `PAPPUS_SECURE_VERIFY_OK` if its complete census and benchmarks agree with the recorded values. In a C++17 environment, `c++ -std=c++17 -O2 independent_check.cpp -o check && ./check` uses fresh vertex-wise domination tests for the swaps, rather than cached covering masks; it also checks every coefficient of both polynomials and the move metrics. Neither checker uses the claimed histograms to decide whether a subset is feasible.

## Relationship to prior work and limitations

An all-optimum census determines the coefficient at the optimum size and permits recovery of the optimum move graphs by direct restriction. It does not give the distribution of secure strict supersets and of larger inclusion-minimal sets. In [5] the displayed classification and transfer metrics cover weight-eight functions, so even allowing doubled vertices does not state the higher-weight secure census. For example, the \(3224\) inclusion-minimal nine-sets cannot be recovered as supersets of any eight-set in that census. The separate exhaustive tests in the present proof address that larger domain. Haythorpe and Newcombe [1] study the secure domination number on specified products and Möbius ladders. Křišťan and Svoboda [2] study token slides for ordinary dominating sets. Neither inspected statement supplies the higher-size secure spectra here. This comparison is not a claim of exhaustive historical priority.

The result is specific to this labelled graph. No finite-order spectrum for other graphs or parameterized family is asserted. Relocation moves are between feasible minima, not a model of indefinitely adaptive guard defense.

## References

1. M. Haythorpe and A. Newcombe, *The Secure Domination Number of Cartesian Products of Small Graphs with Paths and Cycles*, https://arxiv.org/abs/2103.01406.
2. J. M. Křišťan and J. Svoboda, *Shortest Dominating Set Reconfiguration under Token Sliding*, https://arxiv.org/abs/2307.10847.
3. K. Stokes, *Irreducibility of configurations*, Ars Mathematica Contemporanea 10 (2016), 169–181, §4.2, https://dlib.si/stream/URN%3ANBN%3ASI%3ADOC-OCBGMHAN/db7b0708-b365-4c1d-ad1e-eb6bd0f88a7b/PDF.
4. I. N. Kagno, *Desargues' and Pappus' graphs and their groups*, American Journal of Mathematics 69 (1947), 859–863, https://doi.org/10.2307/2371806; see also [Pappus Graph](https://mathworld.wolfram.com/PappusGraph.html).
5. *Mixed-guard weak Roman optima on the Pappus graph*, [Resultary record e85ac2992226](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-mixed-guard-weak-roman-optima-on-the-pappus-graph-twenty-symmetr--e85ac2992226), Finding and Relationship to prior work.
