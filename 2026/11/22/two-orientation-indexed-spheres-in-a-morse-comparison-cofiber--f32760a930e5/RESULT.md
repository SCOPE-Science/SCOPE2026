# Two orientation-indexed spheres in a Morse comparison cofiber
## Finding
For every integer \(n\ge3\), let \(G_n\) be the simple graph obtained by attaching a two-edge pendant path \(v_0-u-w\) to the cycle \(C_n\), identifying the path's first vertex with the cycle vertex \(v_0\). Let \(\mathcal M(G_n)\subseteq\mathcal{GM}(G_n)\) be respectively the ordinary and generalized complexes of discrete Morse vector fields on the one-dimensional simplicial complex \(G_n\). The inclusion has homotopy cofiber
\[
\mathcal{GM}(G_n)/\mathcal M(G_n)\simeq S^n\vee S^n.
\]
In particular, the pair has integral relative homology
\[
H_j(\mathcal{GM}(G_n),\mathcal M(G_n);\mathbb Z)
\cong\begin{cases}\mathbb Z^2&j=n,\\0&j\ne n.\end{cases}
\]
The two primitive relative generators correspond to the two orientations of the unique graph cycle. Thus the inclusion fails to be a homotopy equivalence for every \(n\ge3\). By contrast, for a cycle with just one pendant edge the generalized Morse complex simplicially collapses onto the ordinary Morse complex, as established in the cited literature. The result is an infinite-family **map-level obstruction** rather than a classification of either absolute complex.

## Assumptions and scope
The graph has exactly the edges of the \(n\)-cycle together with \(v_0u\) and \(uw\), and no further edges. A primitive vector-field pair is a graph incidence \((v,e)\) with \(v\in e\), conventionally interpreted as the directed arrow from \(v\) to the opposite endpoint of \(e\). A face of \(\mathcal{GM}(G_n)\) is a set of primitive pairs with no repeated graph vertex and no repeated graph edge. A face belongs to \(\mathcal M(G_n)\) precisely if its directed arrows admit no nontrivial closed gradient path. For one-dimensional simple graphs, such a path is exactly a directed cycle. Homotopy cofiber means the quotient of the geometric realization of the first complex by its subcomplex; simplicial inclusions are cofibrations. Integral homology is with \(\mathbb Z\)-coefficients.

## Proof
Write \(K=\mathcal{GM}(G_n)\) and \(A=\mathcal M(G_n)\). The graph contains a unique undirected cycle, so there are exactly two minimal forbidden faces in \(K\): \(\sigma_+\) and \(\sigma_-\), each selecting one incidence from each of the \(n\) cycle edges with the arrows consistently directed around the cycle. Both have \(n\) vertices as simplices, hence dimension \(n-1\). No face of \(K\) can contain both of them, as their incidence sets use opposite endpoints of each cycle edge and therefore repeat graph edges.

A face containing either \(\sigma_+\) or \(\sigma_-\) already uses every cycle vertex and every cycle edge. It can contain no incidence \((v_0,v_0u)\). The only allowed additional primitive incidences are
\[
a=(u,v_0u),\qquad b=(u,uw),\qquad c=(w,uw).
\]
Of these three, \(a\) and \(c\) are compatible, but neither is compatible with \(b\). Therefore the link of either forbidden face in \(K\) is precisely the one-dimensional complex with a single edge \(ac\) and an isolated vertex \(b\). Denote this link by \(L\); it collapses to two isolated vertices and consequently satisfies \(|L|\simeq S^0\).

Every face in \(K\setminus A\) contains exactly one of the two forbidden faces. Hence the cofiber quotient decomposes along its basepoint into two copies of
\[
Q_n=|\Delta^{n-1}*L|\big/|\partial\Delta^{n-1}*L|.
\]
Here the boundary joins constitute precisely the part lying in \(A\). The standard cone–join quotient (equivalently, the relative augmented simplicial chain construction) identifies \(Q_n\) up to homotopy with the \(n\)-fold unreduced suspension of \(|L|\). Since \(|L|\simeq S^0\), it follows that \(Q_n\simeq S^n\), and the two disjoint forbidden-face classes yield the claimed wedge of two \(n\)-spheres.

For an independent integral calculation, the faces in \(K\setminus A\) associated to one orientation have cardinalities \(n,n+1,n+2\), with counts \(1,3,1\). Thus the relative cellular chain complex for that orientation has the form
\[
0\longrightarrow\mathbb Z\overset{d_{n+1}}\longrightarrow\mathbb Z^3
\overset{d_n}\longrightarrow\mathbb Z\longrightarrow0,
\]
with \(d_n\) having three coefficients of absolute value one and \(d_{n+1}\) two coefficients of absolute value one and one zero. The identity \(d_nd_{n+1}=0\) and the primitive images imply that the only nonzero relative homology is one copy of \(\mathbb Z\) in degree \(n\). The two orientation blocks have no relative differential between them, giving \(\mathbb Z^2\).

Since a homotopy equivalence between CW complexes with a cofibration inclusion would have contractible cofiber, the noncontractible wedge proves that \(\mathcal M(G_n)\to\mathcal{GM}(G_n)\) cannot be a homotopy equivalence.

## Verification
The fully standalone Python 3 program `verify_relative.py` enumerates compatible primitive incidences independently for both tail lengths one and two, for each \(3\le n\le10\). It identifies all forbidden faces by the two directed cycle orientations, verifies that the two blocks are disjoint and exhaustive, and computes signed integral relative boundary matrices directly from the simplex orientations. For a two-edge tail it checks the \((1,3,1)\) relative-face count, the chain identity, and primitive rank-one differentials. For a one-edge tail it checks the elementary cancellation pair. All 16 finite configurations pass; the complete recorded output is `verification_output.txt`. These finite checks are corroboration, not a substitute for the unrestricted local-link proof.

## Relationship to prior work
Donovan and Scoville (arXiv:2207.13780v1, first public 2022-07-27) establish equality of the homotopy types for a cycle with **one** leaf and explicitly give a collapse of the generalized Morse complex onto the ordinary Morse complex (Corollary 22). They ask how generalized Morse complexes may aid computations of ordinary Morse complexes, but do not compute the two-edge-tail relative cofiber.

An earlier published finite computation, *A two-edge tail separates generalized and ordinary Morse complexes of \(C_4\)* (published-finding corpus, 2026-10-11), proves that in the \(n=4\) case the two absolute homotopy types are respectively two and four three-spheres. That published finite separation is credited, **not** claimed as new. The present theorem computes the natural **map cofiber** and integral relative homology for every cycle length, including arbitrary \(n\), which are not implications of those two absolute homotopy types alone. Scoville and Zaremsky's higher-connectivity work (arXiv:2004.10481) introduces the same ordinary/generalized Morse framework but does not identify this explicit cofiber in the accessible material checked.

## Limitations
This does not determine the individual absolute homotopy types of \(\mathcal M(G_n)\) and \(\mathcal{GM}(G_n)\) for every \(n\), nor the full attaching map before quotienting. The result concerns exactly a two-edge pendant path on one otherwise bare cycle; more complicated attached trees have different links. The claims of originality are qualified by the possibility of unindexed equivalent cofiber computations and by limited access to the full text of some potentially related theses. No independent external audit has been performed.

## References
1. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1, publicly posted 2022-07-27; particularly Corollary 22 and the explicit single-leaf collapse. https://arxiv.org/abs/2207.13780
2. N. A. Scoville and M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481v1, publicly posted 2020-04-22. https://arxiv.org/abs/2004.10481
3. *A two-edge tail separates generalized and ordinary Morse complexes of \(C_4\)*, published-finding corpus, first published 2026-10-11. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-a-two-edge-tail-separates-generalized-and-ordinary-morse-complex--e8b31780ea89/RESULT.md
