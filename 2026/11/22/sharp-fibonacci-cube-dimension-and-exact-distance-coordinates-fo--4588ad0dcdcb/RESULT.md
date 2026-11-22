# Sharp Fibonacci-cube dimension and exact distance coordinates for even-alphabet generalized Pell graphs

## Finding
For every integer \(n\ge1\) and every even integer \(k\ge4\), the generalized Pell graph \(\Pi_{n,k}\) of Iršič, Klavžar, and Tan embeds **isometrically** as an induced subgraph of the Fibonacci cube \(\Gamma_{kn-1}\). No isometric embedding into a smaller-dimensional Fibonacci cube exists. Thus its minimum isometric Fibonacci-cube dimension equals exactly \(kn-1\). This improves the published \((2k-2)n-1\)-coordinate construction by \((k-2)n\) coordinates for this parameter family and gives a partial answer to the explicit optimal-embedding question raised in that work.

More precisely, each vertex \(x\) has uniquely determined site levels \(h_i(x)\in\{0,\ldots,k-1\}\) and dimer indicators \(D_i(x)\in\{0,1\}\), defined below. For all vertices \(x,y\), their graph distance is
\[
d_{\Pi_{n,k}}(x,y)=\sum_{i=1}^{n}\left|h_i(x)-h_i(y)\right|+\sum_{i=1}^{n-1}\left|D_i(x)-D_i(y)\right|.
\]
These coordinates yield an explicit shortest-path procedure and a \(kn-1\)-bit Fibonacci labeling in time \(O(kn)\).

## Assumptions and scope
The generalized Pell graph \(\Pi_{n,k}\) has as vertices all length-\(n\) words over \(\{0,1,\ldots,k\}\) in which each maximal run of symbol \(k\) has even length. Equivalently, vertices have a unique left-to-right parsing into single-site monomers with levels \(0,\ldots,k-1\) and two-site dimers \(kk\). Its undirected edges are exactly the valid moves: replace one monomer level \(j\) by \(j+1\) (or conversely), \(0\le j\le k-2\); or replace an adjacent pair of maximal-level monomers \((k-1)(k-1)\) by a dimer \(kk\) (or conversely), keeping a valid word. Distinct symbols \(k\) always occur as part of dimers.

For each site \(i\in\{1,\ldots,n\}\), define \(h_i(x)=x_i\) if \(x_i<k\), and \(h_i(x)=k-1\) if \(x_i=k\). For each \(i\in\{1,\ldots,n-1\}\), let \(D_i(x)=1\) if a dimer in the canonical left-to-right parsing starts at \(i\), and \(D_i(x)=0\) otherwise. Consecutive occupied dimer-start locations are impossible. The theorem includes \(n=1\); the outer restriction to even \(k\ge4\) concerns the Fibonacci embedding only. The distance identity itself holds for every integer \(k\ge2\).

## Proof
**1. Distance and shortest paths.** Every monomer-level move changes exactly one level by one and leaves all dimer indicators unchanged. Every dimer move toggles exactly one dimer indicator and leaves every effective level unchanged. Hence the stated sum is a lower bound on path length. For the reverse inequality, first dissolve precisely the dimers in \(x\) that are absent from \(y\); this can be done independently, because they are disjoint, and it does not change any effective level. Retain the dimers common to \(x\) and \(y\). At all other sites, change each monomer level monotonically from its current value to \(h_i(y)\); these are independent admissible single-site operations. In particular, every site designated for a new target dimer now has level \(k-1\). Finally create precisely the target dimers absent from \(x\). The target dimers are pairwise disjoint and do not overlap retained dimers, so these operations are all legal. This path has exactly the displayed lower-bound length, proving the identity.

**2. An isometric hypercube.** Form \(n(k-1)\) threshold bits \(b_{i,j}(x)={\bf1}[h_i(x)\ge j]\) for \(1\le j\le k-1\), and append \(n-1\) dimer bits \(D_i(x)\). For integer-valued levels, Hamming distance between threshold sequences equals absolute level difference. Step 1 therefore proves this map to the binary hypercube \(Q_{kn-1}\) is distance preserving, and in particular injective. Every edge changes one bit; conversely, pairs of encoded vertices at Hamming distance one are adjacent by the distance equality. Thus the image is induced and isometric.

**3. Reorder and complement for even alphabets.** Write \(k=2r\) with \(r\ge2\). At each site \(i\), define low bits \(\ell_{i,j}={\bf1}[h_i<j]\) for \(1\le j\le r\), and high bits \(u_{i,j}={\bf1}[h_i\ge j]\) for \(r+1\le j\le2r-1\). Form a site block by alternating them:
\[
B_i=(\ell_{i,1},u_{i,r+1},\ell_{i,2},u_{i,r+2},\ldots,\ell_{i,r-1},u_{i,2r-1},\ell_{i,r}).
\]
Concatenate \(B_1,D_1,B_2,D_2,\ldots,D_{n-1},B_n\). The total length is \(n(2r-1)+(n-1)=kn-1\). Within each block every adjacent pair consists of one low and one high bit. Both cannot equal one, because \(h_i<j\le r\) and \(h_i\ge r+1\) are incompatible. At block boundaries a one in \(D_i\) implies \(h_i=h_{i+1}=k-1\), so the ending and starting low bits equal zero. Consequently no two adjacent bits in the full output equal one. The output lies in \(\Gamma_{kn-1}\). The reordered low bits are complements of the original low thresholds; complementing or permuting coordinates does not alter pairwise Hamming distances, so the map is still isometric and induced.

**4. Sharp lower bound.** The hypercube in Step 2 uses \(M=kn-1\) coordinate directions, and all are essential for isometric encoding. For each site \(i\) and each threshold \(j\), the all-zero monomer word with site \(i\) changed between \(j-1\) and \(j\) supplies a graph edge toggling just that threshold coordinate. For each adjacent-site location \(i\), the all-\((k-1)\) word and the word obtained by replacing the pair starting at \(i\) by \(kk\) supply a graph edge toggling only \(D_i\). These edges belong to \(M\) different Djoković–Winkler metric edge classes: two edges with different directions in any isometric hypercube labeling are distinguished by the relation
\[
d(a,c)+d(b,d)=d(a,d)+d(b,c),
\]
whereas two edges with the same direction give inequality between the two cross-sums (with endpoints ordered consistently). This relation depends only on the source graph metric, so any other isometric hypercube labeling must allocate distinct coordinates to these \(M\) edge classes. Every Fibonacci cube \(\Gamma_m\) is itself isometrically embedded in \(Q_m\): coordinate flips from either vertex to the coordinatewise intersection, followed by flips to the other, never create consecutive ones. Thus an isometric embedding of \(\Pi_{n,k}\) into \(\Gamma_m\) requires \(m\ge kn-1\), which Step 3 attains.

## Verification
The standalone `verify.py` enumerates legal generalized Pell strings using their monomer–dimer recursion, independently constructs legal graph edges, produces the indicated Fibonacci words, and checks every pair's graph distance against Hamming distance. It also checks all \(kn-1\) coordinate directions occur on graph edges. Exhaustive parameter cases include \(k=4\), \(1\le n\le4\); \(k=6\), \(1\le n\le3\); and \(k=8\), \(1\le n\le2\), alongside the \(k=2\) base case. In particular, the \(n=4,k=4\) case has 305 vertices, and the \(n=3,k=6\) case has 228 vertices. Run `python3 verify.py`. These finite checks are consistency tests; the proof above establishes the unbounded theorem.

## Relationship to prior work
Iršič, Klavžar, and Tan introduced \(\Pi_{n,k}\), proved that these graphs are median, and gave a Fibonacci-cube subgraph embedding of length \((2k-2)n-1\) (Proposition 5.8). Their Problem 5.10 asks whether this dimension can be reduced. Their result does not give the length-\(kn-1\) isometric embedding or its sharp minimality. Došlić and Podrug studied *metallic cubes*, another generalization with the same vertex and edge counts but different adjacency and diameter; their results cannot directly supply an embedding for the present graphs. Munarini's earlier Pell-graph work concerns the \(k=2\) specialization, excluded from the improved-dimension claim. Cabello, Eppstein, and Klavžar's general Fibonacci-dimension theorem (2011) characterizes isometric Fibonacci embeddings through coordinating paths in a semicube graph; it does not evaluate those paths for generalized Pell graphs, which were introduced later. The alternating coordinate construction here supplies an explicit one-path certificate in their framework. The present result settles the optimum **only for even alphabets**; no claim is made about odd \(k\), nor about optimal embeddings without distance preservation.

## Limitations
Optimality is among **isometric** Fibonacci-cube embeddings. An abstract subgraph embedding not preserving distance could use fewer dimensions; that separate optimization is unresolved here. While finite verification confirms small cases, it is not a substitute for the all-parameter proof. Comprehensive historical priority across unindexed presentations or unpublished results is not guaranteed. The theorem assumes the exact generalized Pell transition rule above; transferring it to differently defined metallic-cube families would require a separate proof.

## References
1. V. Iršič, S. Klavžar, and E. Tan, *Generalized Pell graphs*, arXiv:2307.13317, first posted 25 July 2023, https://arxiv.org/abs/2307.13317 (especially Proposition 5.8 and Problem 5.10).
2. T. Došlić and L. Podrug, *Metallic cubes*, arXiv:2307.14054, first posted 26 July 2023, https://arxiv.org/abs/2307.14054.
3. E. Munarini, *Pell graphs*, Discrete Mathematics 342 (2019), 2415–2428, https://doi.org/10.1016/j.disc.2019.05.008.
4. S. Cabello, D. Eppstein, and S. Klavžar, *The Fibonacci Dimension of a Graph*, Electronic Journal of Combinatorics 18 (2011), #P55, https://doi.org/10.37236/542.
