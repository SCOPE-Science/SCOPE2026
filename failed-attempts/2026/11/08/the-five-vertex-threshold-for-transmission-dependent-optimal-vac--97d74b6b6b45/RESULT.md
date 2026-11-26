# The five-vertex threshold for transmission-dependent optimal vaccination

## Finding

For every finite connected simple undirected graph \(G\) on \(2\le n\le 5\) vertices, remove one perfectly vaccinated vertex \(v\). Each edge remaining in \(G-v\) independently transmits with probability \(p\in(0,1)\), and the single initial infected vertex is drawn uniformly from the \(n-1\) unvaccinated vertices. Let \(R_{G,v}(p)\) be the expected final outbreak size (including the initial case). We minimize \(R_{G,v}(p)\) over vertices \(v\).

**Theorem (complete first-order classification).** For every connected graph with \(2\le n\le4\), and for 19 of the 21 connected graph isomorphism classes with \(n=5\), there is one vertex that is optimal for every \(p\in(0,1)\). Exactly two five-vertex isomorphism classes lack such a transmissibility-independent optimum. In each, the set of optimal vertices changes precisely at \(p=1/4\), and the optimizer sets in the following table are exhaustive for \(0<p<1\).

| Class | Edges (vertices \(0,1,2,3,4\)) | \(0<p<1/4\) | \(p=1/4\) | \(1/4<p<1\) |
|---|---|---|---|---|
| A | \(01,13,14,23,24,34\) | \(\{3,4\}\) | \(\{1,3,4\}\) | \(\{1\}\) |
| B | \(02,03,04,12,13,14,24\) | \(\{2,4\}\) | \(\{0,1,2,4\}\) | \(\{0,1\}\) |

Every vertex in the changing optimizer classes has an unchanging degree: the switch is caused exclusively by the transmissibility-dependent geometry of contagion paths. In both classes the competing vertices have degree three, so degree-only ranking cannot distinguish them.

## Assumptions and scope

Graphs are simple, unweighted, undirected, connected and considered up to relabeling. Only \(2\le n\le5\) is classified. Exactly one vertex is completely removed before infection; no vaccine failures, additional initial infections or node heterogeneities occur. Independently open edges represent transmissible contacts; conditional on an open-edge realization, the outbreak from a seed is its open component. This is the Reed–Frost / independent-bond-percolation final-size formulation, **not** the weighted synchronous SIR updating rule in the motivating 2023 vaccination paper. The seed is uniform among the remaining \(n-1\) vertices after vaccination, and all expectations include the seed. Endpoints \(p=0,1\) are excluded from the optimizer-set table, since additional ties can occur there.

## Proof

**1. Exact finite polynomial objective.** Write \(H=G-v\), \(N=n-1\), and \(m=|E(H)|\). For each \(F\subseteq E(H)\), let \(\mathcal C(F)\) be the components of \((V(H),F)\). Averaging the number of infected individuals over a uniformly random seed gives

\[
R_{G,v}(p)=\frac1N\sum_{F\subseteq E(H)}\left(\sum_{C\in\mathcal C(F)}|C|^2\right)p^{|F|}(1-p)^{m-|F|}.
\]

Indeed a component of size \(s\) is selected with probability \(s/N\), and then contributes \(s\) infections. Thus \(P_{G,v}(p):=N R_{G,v}(p)\) has **integer polynomial coefficients**, constructible by finite edge-subset enumeration. Independently, \(P_{G,v}=\sum_{a,b\in V(H)}\Pr_p(a\leftrightarrow b)\), counting ordered vertex pairs; this gives a separate exact implementation check.

**2. The two changing classes.** In class A, label vertices as in the edge table. Directly expanding the preceding polynomial gives

\[
\begin{aligned}
R_{A,3}-R_{A,1}&=\tfrac12 p^2(4p-1),\\
R_{A,3}-R_{A,2}&=\tfrac12 p(p-1)(2p^2+4p+1)<0,\\
R_{A,3}-R_{A,0}&=\tfrac12 p(p-1)\bigl(2+8p+7p^2(1-p)\bigr)<0,\\
R_{A,4}&=R_{A,3}.
\end{aligned}
\]

These identities prove every optimizer assertion for class A, including strictness except at the stated crossing. In class B the exact identities are

\[
\begin{aligned}
R_{B,2}-R_{B,0}&=\tfrac12 p^2(1-p)(4p-1),\\
R_{B,3}-R_{B,2}&=\tfrac12 p(1-p)^2(7p^2+6p+1)>0,\\
R_{B,4}&=R_{B,2},\quad R_{B,1}=R_{B,0}.
\end{aligned}
\]

They likewise establish the exhaustive class B optimizer sets on the open transmissibility interval.

**3. Exhaustive classification and positivity certificate.** Enumerate all labeled graphs on each size \(n=2,3,4,5\) via the \(2^{\binom n2}\) edge masks, discard disconnected graphs, and identify labelings via all vertex permutations. The resulting numbers of connected isomorphism classes are, respectively, \(1,2,6,21\). For each of the 28 classes other than A and B, the standalone verifier explicitly finds a vertex \(w\) for which all polynomials \(P_{G,v}(p)-P_{G,w}(p)\) have a **nonnegative-coefficient certificate**: for any such polynomial \(Q(p)=\sum_{k=0}^{d}a_kp^k\), every coefficient of

\[
(1+t)^d Q\!\left(\frac{t}{1+t}\right)
=\sum_{j=0}^{d}\left(\sum_{k=0}^{j}a_k\binom{d-k}{j-k}\right)t^j
\]

is nonnegative. Since \(t=p/(1-p)>0\), this proves \(P_{G,w}(p)\le P_{G,v}(p)\) simultaneously for every vertex \(v\) and every \(0<p<1\). The supplied `verify.py` (standard-library Python, no external data) contains all enumeration, canonical-labeling, polynomial and certificate operations, and asserts that the **only** classes for which no permanent witness is so certified are precisely the two explicit A/B adjacency lists. Because the preceding identities prove A/B really lack a permanent optimizer, the exhaustive classification follows. This is complete finite enumeration, not random sampling or numerical root finding.

## Verification

Run `python3 verify.py` with Python 3. The checker enumerates every labeled graph up to five vertices, canonically reduces them to isomorphism types, enumerates every possible open-edge subset, and performs every comparison using integer arithmetic. It verifies 127 nonnegative-coefficient inequality certificates, compares the component-square objective with an independently implemented ordered-pair connectivity objective for 147 vertex cases (including repeated direct checks of A/B), and proves the two special factor identities by exact coefficient equality. Expected output: class counts \(1,2,6,21\), exactly two exceptional five-vertex classes, the exact \(1/4\) crossing in both, and all checks passed. The verification code supplies constructive, replayable detail for the finite certificate used in Step 3.

## Relationship to prior work

Chatterjee and Zehmakan (2023, arXiv:2305.16458) motivate rigorous study of network-based vaccine placement and contrast degree- and centrality-based heuristics under their different, weighted discrete-time epidemic process. Their Sections III–IV, VI–VIII formulate the optimization and compare heuristics; they do not provide this bond-percolation one-vaccine complete classification. Morone et al. (2016) formulate collective immunization and optimal percolation and develop scalable approximate methods, emphasizing giant-component fragmentation and network-scale threshold behavior. Neither general methodology states or implies the exact first size, the two isomorphism classes, or the shared rational crossover under the present uniform-seed expected-outbreak objective. The polynomial/cluster-size identity is standard and is used, not claimed as novel.

## Limitations

The result applies only to the exactly specified homogeneous bond-percolation epidemic model, connected simple graphs of at most five vertices and a single perfect vaccine. The chosen source model has different infection/recovery dynamics. The graph classification is finite, though exhaustive; it does not establish behavior for larger graphs or other vaccination objectives. The literature search and database comparison do not rule out an unindexed equivalent result; independent external review remains outstanding.

## References

1. S. Chatterjee and A. N. Zehmakan, *Effective Vaccination Strategies in Network-based SIR Model*, arXiv:2305.16458v1 (first public 2023-05-25). https://arxiv.org/abs/2305.16458
2. F. Morone, B. Min, L. Bo, R. Mari and H. A. Makse, *Collective Influence Algorithm to find influencers via optimal percolation in massively large social media*, Scientific Reports **6**, 30062 (2016). https://doi.org/10.1038/srep30062
3. *A comparison of node vaccination strategies to halt SIR epidemic spreading in real-world complex networks*, Scientific Reports **12**, 21355 (2022). https://doi.org/10.1038/s41598-022-24652-1
