# One optimum orbit and six real zeros for the Petersen class-domination partition polynomial

## Finding

Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph, whose vertices are the ten two-element subsets of \([5]\), adjacent precisely when disjoint. A *class-domination coloring* (CD-coloring) is a partition of \(V(P)\) into nonempty independent classes, each contained in the **open** neighborhood of at least one vertex. We count **unlabeled color classes**, so globally renaming colors does not produce a new partition. Let \(c_k\) denote the number of these partitions with exactly \(k\) classes and define \(C_P(z)=\sum_{k=0}^{10}c_kz^k\).

Then
\[
\boxed{C_P(z)=30z^4+604z^5+1575z^6+1130z^7+295z^8+30z^9+z^{10}.}
\]
In particular, \(\chi_{cd}(P)=4\) and there are exactly \(30\) optimal four-class partitions. Each optimum has class sizes \((3,3,2,2)\); every optimum arises from two disjoint Petersen vertices, by using both corresponding open neighborhoods as triple classes and partitioning the four remaining vertices into one of two possible pairs of doubleton classes. The \(30\) optima form a single orbit under the natural \(S_5\) action on the vertices of \(P\).

Moreover, the polynomial \(C_P(z)/z^4\), of degree six, has six **distinct strictly negative real zeros**. Thus \(C_P(z)\) itself is real-rooted (with the root zero of multiplicity four), and its nonzero coefficient sequence is strictly log-concave.

## Assumptions and scope

The graph is the simple ten-vertex Petersen graph; \(N_P(v)\) means an open neighborhood, excluding \(v\). A class is valid exactly when it is contained in some \(N_P(v)\). The term *partition* always counts unordered, nonempty classes, not assignments of named colors. The rank polynomial counts all valid partitions, including those with nonminimal class counts. Root statements concern the ordinary indeterminate \(z\) over \(\mathbb R\).

## Proof

**1. Allowed classes.** Every open neighborhood has three vertices, and in \(P\) it is independent (the graph has no triangles). Singletons are admissible. Two vertices can belong to a common class if and only if they are nonadjacent in \(P\). Under the Kneser representation this means that their two-subsets intersect, so admissible doubletons are exactly edges of the triangular graph \(T_5=L(K_5)=\overline P\). Every admissible triple is one full open neighborhood \(N_P(v)\), and there are precisely ten distinct such triples. There are no larger classes.

**2. How triple classes meet.** Two open neighborhoods \(N_P(u),N_P(v)\) are disjoint if and only if \(u,v\) are adjacent in \(P\), i.e. their two-subsets of \([5]\) are disjoint. Indeed, the neighborhoods are the three edges in the complementary three-sets, and their intersection is an edge if the center two-subsets meet, and empty if those centers are disjoint. Hence there are exactly \(15\) unordered pairs of disjoint triple classes, and no three pairwise disjoint triple classes (\([5]\) contains at most two disjoint two-subsets).

**3. Matching decomposition and exact coefficients.** For a finite graph \(H\), write \(M_H(t)=\sum_jm_j(H)t^j\), where \(m_j(H)\) counts \(j\)-edge matchings. Once triple classes have been selected, the remaining doubleton classes form a matching in the induced subgraph of \(T_5\) on the unused vertices. The remaining vertices are singletons. Because the triples have distinct neighborhood centers, this decomposition is bijective; no partition is counted twice.

With no triple class the matching polynomial is \(M_{T_5}(t)\). With one triple class, each of the ten choices has the same residual graph \(T_5-N_P(v)\) on seven vertices. With two triple classes there are fifteen choices, and the residual four vertices induce \(C_4\) in \(T_5\). Exact matching-polynomial coefficients are:

| Residual graph | \(m_0\) | \(m_1\) | \(m_2\) | \(m_3\) | \(m_4\) | \(m_5\) |
|---|---:|---:|---:|---:|---:|---:|
| \(T_5\) | 1 | 30 | 285 | 980 | 1020 | 144 |
| \(T_5-N_P(v)\) | 1 | 15 | 54 | 40 | — | — |
| \(C_4\) | 1 | 4 | 2 | — | — | — |

All numbers follow from the terminating vertex-deletion recurrence
\[
M_H(t)=M_{H-u}(t)+t\sum_{w\in N_H(u)}M_{H-\{u,w\}}(t),\qquad M_{\varnothing}(t)=1.
\]
The first two rows can be reproduced with the fully specified ten-vertex bit-mask recurrence in `verify_matching.py`, and checked independently against unrestricted set-partition enumeration in `verify_partitions.py`. The latter visits all \(115975\) partitions of a ten-element set, directly applying the open-neighborhood definition.

A matching of size \(j\) with \(r\) triple classes and leftover singletons gives \(10-2r-j\) classes. Thus, with \(t=z^{-1}\),
\[
C_P(z)=z^{10}M_{T_5}(t)+10z^8M_{T_5-N_P(v)}(t)+15z^6M_{C_4}(t).
\]
Substituting the coefficient table gives the stated polynomial and no terms below degree four.

**4. Optimum structure and symmetry.** Four classes must cover ten vertices with class sizes at most three. The only numerical possibilities are \((3,3,3,1)\) and \((3,3,2,2)\). The former is impossible since three disjoint neighborhoods cannot occur. In the latter, the two triple centers are disjoint two-subsets \(a,b\) of \([5]\), giving \(15\) choices. The four remaining Petersen vertices are exactly the four cross-edges between the two pairs \(a,b\), and they induce a four-cycle in \(T_5\). Its two perfect matchings yield the two admissible doubleton pairings. Hence there are \(15\cdot2=30\) optima. The symmetric group on \([5]\) is transitive on unordered disjoint pairs of two-subsets, and the stabilizer interchanges the two pairings, proving there is one orbit.

**5. Exact real-root certificate.** Put
\[
q(z)=C_P(z)/z^4=30+604z+1575z^2+1130z^3+295z^4+30z^5+z^6.
\]
Direct exact rational evaluation gives opposite signs at the ends of each of the six disjoint intervals
\[
(-15,-14),\ (-9,-8),\ (-5,-4),\ (-2,-3/2),\ (-1,-1/2),\ (-1/10,0).
\]
The exact endpoint evaluations, from left to right, are respectively \((75345,-72910)\), \((-6135,4862)\), \((1385,-610)\), \((-94,8385/64)\), \((137,-127/64)\), and \((-15750799/1000000,30)\). By the intermediate value theorem each interval contains a distinct negative root. Because \(q\) has degree six, these are all its roots and all are simple. Strict log-concavity of the positive coefficient sequence follows from Newton's inequalities.

## Verification

Run `python3 verify_matching.py` and `python3 verify_partitions.py` from the extracted artifact directory. Their deterministic expected standard outputs are in `verification_matching.txt` and `verification_partitions.txt`. The matching program computes all coefficient rows by an explicit deletion recurrence, constructs the optima and tests the full \(120\)-element underlying-point symmetry action, and evaluates the six root sign changes with rational arithmetic. The second program uses a separate adjacency representation and visits every one of the \(115975\) unrestricted set partitions, checking the common-neighbor condition for every block. No numerical root approximations or probabilistic inference are required.

## Relationship to prior work

Antony, Chandran, Gayen, Gosavi, and Jacob's 2023 preprint studies CD-coloring, total domination, and separated clusters and includes the known equality of the CD-chromatic and total-domination numbers for triangle-free graphs. The present four-class minimum is compatible with that general scalar relation; the complete coefficient polynomial, single-orbit optimum classification, and six-real-zero certificate are stronger enumerative statements not supplied by the inspected material. Krithika, Rai, Saurabh, and Tale's earlier exact algorithm addresses minimization on general graphs, rather than this explicit partition census. Zhou, Zhao, Ma, and Xu study a **strictly different** domination coloring requiring every vertex also to dominate a class, and report five colors for the Petersen graph under that stricter definition; this does not contradict the four-color CD result. Comparisons with other published research records returned differently constrained Petersen coloring, domination, and geometric counts rather than a claim implying this enumerator.

## Limitations

This is a finite classification for the ten-vertex Petersen graph, not an all-order formula for generalized Petersen graphs. All graphs and color classes are labelled at vertex level, but color class names are quotient out. The six-root result is for this one polynomial; it does not assert general real-rootedness of CD-coloring partition polynomials. Historical priority depends on the accessible and indexed literature, and no independent formal or expert mathematical audit has been performed.

## References

1. D. Antony, L. S. Chandran, A. Gayen, S. Gosavi, D. Jacob, *Total Domination, Separated-Cluster, CD-Coloring: Algorithms and Hardness*, first public arXiv submission 2023-07-22, arXiv:2307.12073, https://arxiv.org/pdf/2307.12073.
2. R. Krithika, A. Rai, S. Saurabh, P. Tale, *Parameterized and Exact Algorithms for Class Domination Coloring*, https://web.iitd.ac.in/~raiashutosh/Papers/Conference/cd-col.pdf (accessible author-hosted text); also arXiv:2203.09106.
3. Y. Zhou, D. Zhao, M. Ma, J. Xu, *Domination Coloring of Graphs*, Mathematics 10 (2022), article 998, https://doi.org/10.3390/math10060998 (different, stricter parameter).
