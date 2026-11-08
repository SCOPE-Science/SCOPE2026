# Minimal geodesic-transversal spectra of cycles and a re-entrant purity exception

## Finding
For the labelled simple cycle \(C_n\), \(n\ge3\), a *geodesic transversal* is a set of vertices intersecting every maximal graph-shortest path. Let \(M_n(z)=\sum_S z^{|S|}\), summed over inclusion-minimal geodesic transversals \(S\). Set \(L=\lfloor n/2\rfloor\), \(r=\lceil n/2\rceil-2\), and \(\delta=3r-n\), and define
\[
 b_n=\begin{cases}n,&n\text{ odd},\\3n/2,&n\text{ even},\end{cases}
 \qquad
 c_n=\begin{cases}\dfrac n3\binom{\delta+2}{2},&\delta\ge0,\\0,&\delta<0.\end{cases}
\]
Then, exactly and for all \(n\ge3\),
\[
\boxed{M_n(z)=b_nz^2+c_nz^3.}
\]
Every inclusion-minimal geodesic transversal has cardinality two or three. The two-element minimal transversals are precisely unordered pairs whose two cyclic distances are both at most \(L+1\). The three-element minimal transversals are precisely unordered triples whose three successive positive cyclic gaps are all at most \(r\). No other minimal transversals exist.

The upper inclusion-minimal geodesic-transversal number equals three exactly for \(n=9\) or \(n\ge11\), and equals two otherwise. In particular the hypergraph-independent-set complex formed by subsets of \(V(C_n)\) that contain no entire maximal geodesic is pure exactly for \(3\le n\le8\) and \(n=10\): non-purity begins at nine vertices, disappears at ten, and persists from eleven onward. The three-element coefficient is asymptotic to \(n^3/24\), while the two-element coefficient is linear in \(n\).

## Assumptions and scope
The graph is a labelled, undirected, loop-free cycle of length \(n\ge3\), with vertices \(0,1,\ldots,n-1\) interpreted modulo \(n\). A geodesic is a shortest path between its endpoints; *maximal* means not properly contained as a path in another geodesic. Inclusion-minimal means minimal under removal of any selected vertex, not minimum cardinality. Two vertex sets are counted as distinct when their labelled subsets differ; rotations and reflections are **not** identified. The convention \(c_n=0\) for \(\delta<0\) is part of the formula, not an extension of the binomial coefficient to negative upper indices.

## Proof
**Maximal geodesics.** Write \(L=\lfloor n/2\rfloor\). In a cycle every shortest path is a consecutive cyclic arc of length at most \(L\). Every arc of length strictly less than \(L\) extends to a longer shortest arc (including when \(n=3\)); every arc of length \(L\) is unextendible. Thus the maximal geodesics are exactly the \(n\) cyclic blocks of \(L+1\) consecutive vertices. This remains true for even \(n\), when antipodal vertices have two distinct shortest paths.

**Cyclic-gap criterion.** A nonempty set \(S\) of cardinality \(k\) has clockwise-ordered selected vertices \(s_1,\ldots,s_k\); write \(d_i\ge1\) for the number of cycle edges clockwise from \(s_i\) to \(s_{i+1}\), with cyclic indices and \(\sum_i d_i=n\). A maximal geodesic misses \(S\) precisely when one of the gaps contains at least \(L+1\) consecutive unselected vertices. Each gap contains \(d_i-1\) such vertices. Therefore
\[
 S\text{ is a transversal}\quad\Longleftrightarrow\quad d_i\le L+1\text{ for all }i.
\]
Deleting \(s_i\) merges the two neighbouring unselected runs and \(s_i\), making a run of \(d_{i-1}+d_i-1\) unselected vertices. Therefore the deletion destroys the hitting property exactly when \(d_{i-1}+d_i-1\ge L+1\). Inclusion-minimality is accordingly **equivalent**, with no extra assumptions, to both systems
\[
 d_i\le L+1,\qquad d_{i-1}+d_i\ge L+2\qquad(1\le i\le k).
\]
The empty set is not a transversal. A singleton cannot be a transversal since its unique gap has size \(n>L+1\) for \(n\ge3\).

**Only two or three points.** Summing the second system over all \(i\) gives \(2n\ge k(L+2)\). Since \(4(L+2)>2n\) for every \(n\ge3\), one has \(k\le3\). Thus \(k\in\{2,3\}\).

**Two points.** For \(k=2\), the deletion inequality is automatic: each sum equals \(n\ge L+2\). If one clockwise gap equals \(d\), the other equals \(n-d\). Feasibility is
\[
 n-L-1\le d\le L+1.
\]
For \(n=2m\) the three allowed values are \(m-1,m,m+1\), producing \(3n/2\) distinct unordered pairs (there are \(n\) choices of starting vertex, each pair counted twice). For \(n=2m+1\) the allowed values are \(m,m+1\), producing \(n\) unordered pairs. Hence the coefficient \(b_n\).

**Three points.** For \(k=3\), the deletion inequality for each pair of neighbouring gaps says \(n-d_j\ge L+2\) for the complementary third gap; equivalently
\[
 1\le d_1,d_2,d_3\le r=n-L-2=\lceil n/2\rceil-2,
 \qquad d_1+d_2+d_3=n.
\]
Here \(r\le L+1\), so these inequalities automatically imply transversal feasibility. A triple is counted three times by choosing a distinguished selected starting vertex, and for each starting vertex the three ordered gaps uniquely determine the triple. Thus its number is
\[
 c_n=\frac n3[x^n](x+x^2+\cdots+x^r)^3.
\]
If \(3r<n\), there are no triples. Otherwise set \(e_i=r-d_i\ge0\); their sum is \(\delta=3r-n\). For even \(n=2m\), \(r=m-2\) and \(\delta=m-6\); for odd \(n=2m+1\), \(r=m-1\) and \(\delta=m-4\). When \(\delta\ge0\) it is strictly less than \(r\), so the upper bounds \(e_i\le r-1\) are automatic. Stars-and-bars gives \(\binom{\delta+2}{2}\) ordered triples, proving the claimed exact coefficient.

**Spectrum and purity.** A three-point inclusion-minimal transversal exists if and only if \(\delta\ge0\). This occurs for odd \(n\ge9\) and even \(n\ge12\), precisely \(n=9\) or \(n\ge11\). Two-point inclusion-minimal transversals exist for every \(n\ge3\). The independence complex of the cyclic-block hypergraph has facets exactly the complements of inclusion-minimal transversals, of sizes \(n-2\) and (when they exist) \(n-3\). This proves the purity classification. The formulas for \(c_n\) have cubic leading term \(n^3/24\) along both parities, proving the asymptotic comparison.

## Verification
The accompanying standard-library Python program `verify.py` independently enumerates all shortest paths of each cycle of order \(3\) through \(18\), retains the maximal shortest paths, tests each of the \(524280\) vertex subsets against the original hitting and deletion definitions, and compares the individual sets with the cyclic-gap classification and all polynomial coefficients. It reports `VERIFY_OK`. The computation is corroboration only; the preceding proof treats all integers \(n\ge3\).

## Relationship to prior work
Manuel, Brešar and Klavžar introduced geodesic transversals and investigated algorithmic and structural aspects. Peterin and Semanišin independently introduced the equivalent *maximal shortest paths cover* and explicitly proved \(\operatorname{gt}(C_n)=2\) for cycles (Proposition 2.2(ii) of their 2021 preprint). That scalar minimum and the identification of length-\(L\) maximal cycle geodesics are **prior knowledge**, not claimed as new here. The finding refines them by determining **every inclusion-minimal set**, its exact cardinality distribution, the cubic/linear dichotomy, and the re-entrant purity exception.

Elbassioni and Rauf gave a general incremental enumeration algorithm for minimal hitting sets of circular-arc hypergraphs and showed that such hypergraphs are 2-exact. Our cyclic-block hypergraph is a special circular-arc hypergraph, and that generic algorithm is acknowledged. The 2-exact bound does not itself state this sharp two/three-element global classification, labelled coefficients, or the exceptional purity pattern. The \(n=4\) case can also be recovered from a separate ladder-graph calculation, so it is not claimed as an isolated new case.

## Limitations
No new assertion is made about minimum transversal size, known to be two for cycles. The theorem concerns labelled undirected cycles, and does not classify larger graph families or provide a general circular-arc hypergraph enumeration formula. It is proved mathematically and corroborated finitely; independent mathematical audit and an exhaustive publication-priority determination have not been performed. A different terminology or unindexed enumeration may already imply this specialization.

## References
1. P. Manuel, B. Brešar and S. Klavžar, *The geodesic-transversal problem*, arXiv:2101.08042v1, first publicly posted 20 January 2021; later *Applied Mathematics and Computation* 413, 126621 (2022). https://arxiv.org/abs/2101.08042
2. I. Peterin and G. Semanišin, *On the Maximal Shortest Paths Cover Number*, *Mathematics* 9 (2021), 1592. https://doi.org/10.3390/math9141592 ; author's preprint https://mp.feri.um.si/osebne/peterin/clanki/MSCP1.pdf
3. K. Elbassioni and I. Rauf, *Polynomial-time dualization of r-exact hypergraphs with applications in geometry*, *Discrete Mathematics* 310 (2010), 2356–2363. https://doi.org/10.1016/j.disc.2010.05.017
