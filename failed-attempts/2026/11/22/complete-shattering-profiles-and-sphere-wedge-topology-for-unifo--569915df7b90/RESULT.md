# Complete shattering profiles and sphere-wedge topology for uniform independent sets of paths

## Finding
Fix integers \(n\ge1\) and \(1\le k\le\lceil n/2\rceil\). Let \(P_n\) be the simple path on vertices \([n]=\{1,\ldots,n\}\), and let \(\mathcal F_{n,k}\) be the Boolean membership concept class of all independent vertex sets of cardinality exactly \(k\). A query asks whether a given vertex belongs to the selected independent set. Put \(d=\min\{k,n-2k+1\}\), necessarily nonnegative. Then the complete shattered-support classification is
\[
S\subseteq[n]\text{ is shattered}\quad\Longleftrightarrow\quad S\text{ has no consecutive vertices and }|S|\le d.
\]
Consequently the entire shattering complex is the rank-\(d\) truncation of the path independence complex, and its exact face polynomial is
\[
\Phi_{n,k}(z)=\sum_{j=0}^{d}\binom{n-j+1}{j}z^j.
\]
The VC dimension \(d\) has appeared in related fixed-weight path/cycle research and is not presented here as independently new. The claimed contributions are the full characterization and all-degree polynomial, the minimax trace-completion lemma in the proof, and the following topological identification. If \(d\ge1\), the shattering complex is **pure shellable**, hence torsion-free, and
\[
|\Delta_{n,k}|\simeq\bigvee^{\beta(n,d)} S^{d-1},\qquad
\beta(n,d)=\sum_{j=0}^{d}(-1)^{d-j}\binom{n-j+1}{j}.
\]
Here a zero-fold wedge means a contractible complex; the formula includes \(d=1\), where the homotopy type is a wedge of \(n-1\) copies of \(S^0\). If \(d=0\), only the empty support is shattered; its generating polynomial is \(1\), and no assertion is made about the geometric realization of the void complex.

For instance, \((n,k,d)=(8,3,3)\) gives \(\Phi=1+8z+21z^2+20z^3\), and the complex is a wedge of six two-spheres. For \((n,k,d)=(11,4,4)\), \(\Phi=1+11z+45z^2+84z^3+70z^4\), and the complex is a wedge of 21 three-spheres.

## Assumptions and scope
All graphs are finite, simple, labeled paths. Independent means that no two selected vertices are adjacent. Concepts have **exactly** \(k\) selected vertices, not at most \(k\) and not necessarily maximal or dominating. A support \(S\) is shattered if for each binary assignment \(T\subseteq S\) some concept \(B\in\mathcal F_{n,k}\) satisfies \(B\cap S=T\). The empty support is shattered. The path independence complex \(\operatorname{Ind}(P_n)\) is the collection of all independent vertex sets of arbitrary sizes; its rank-\(d\) truncation contains faces with at most \(d\) vertices. The convention \(\binom ab=0\) for \(b>a\) is used.

## Proof
**1. Exact worst-case trace-completion capacity.** Let \(S\subseteq[n]\) be any independent set with \(s=|S|\). For each forced-positive trace \(T\subseteq S\), define
\[
M_S(T)=\max\{|I|: I\subseteq[n]\text{ independent and }I\cap S=T\}.
\]
The following is an exact minimax identity, valid also for an empty path:
\[
\boxed{\min_{T\subseteq S}M_S(T)=\left\lceil\frac{n-s}{2}\right\rceil.}
\]
For its lower bound, remove every vertex of \(S\) and every neighbor of a vertex in \(T\). The remaining induced graph \(H\) is a forest of paths with at least \(n-s-2|T|\) vertices, because \(P_n\) has maximum degree two. Being a path forest, \(H\) has a bipartition whose larger side has at least \(\lceil |V(H)|/2\rceil\) vertices, and that side is independent. Together with \(T\), it yields a compatible independent set of size at least \(|T|+\lceil(n-s-2|T|)/2\rceil=\lceil(n-s)/2\rceil\). Thus every \(M_S(T)\) is at least this bound.

For the matching upper bound, recursively choose one prescribed labeling of the support vertices so that every compatible independent set has size at most \(\lceil(n-s)/2\rceil\). The claim is immediate for paths of at most two vertices. For paths of length at least three, inspect their first vertex in the current interval. If it lies in \(S\), prescribe label zero and recurse on the remaining path, of length \(n-1\) with \(s-1\) support vertices; the maximum is at most \(\lceil(n-s)/2\rceil\) by induction. If the first two vertices are both outside \(S\), every independent set selects at most one of this pair; recurse after deleting the pair, giving maximum at most \(1+\lceil(n-2-s)/2\rceil=\lceil(n-s)/2\rceil\). In the final case, vertex one is outside \(S\) and vertex two is inside \(S\). Since \(S\) is independent, the third vertex (which exists in this case) is outside \(S\). Prescribe vertex two positive, thereby excluding vertices one and three, and recurse on the tail after vertex three, of length \(n-3\) with \(s-1\) support vertices. The maximum is at most \(1+\lceil((n-3)-(s-1))/2\rceil=\lceil(n-s)/2\rceil\). All possible cases are exhausted, proving the identity. The argument is constructive and does not rely on finite enumeration.

**2. Exact shattering test.** If \(S\) is shattered, its all-positive trace is realized, so it is independent and \(s\le k\). Also all traces must be extendible to an independent set of size \(k\); the minimax identity forces \(k\le\lceil(n-s)/2\rceil\). Conversely, if these inequalities hold, the minimax identity ensures \(M_S(T)\ge k\) for every \(T\subseteq S\). A compatible independent set of maximum size \(M_S(T)\) contains \(T\) and no other support vertex; deleting vertices outside \(T\) reduces its cardinality to \(k\), because \(k\ge s\ge|T|\), while retaining exactly the prescribed trace. Thus \(S\) is shattered. Since \(k\le\lceil(n-s)/2\rceil\) is equivalent for integer parameters to \(s\le n-2k+1\), the exact criterion is \(S\) independent and \(s\le d\). In particular \(\operatorname{VCdim}=d\), including the boundary \(d=0\).

**3. Enumerate every face.** A \(j\)-set \(1\le x_1<\cdots<x_j\le n\) is independent in the path exactly when \(x_{i+1}\ge x_i+2\). Subtracting \(0,1,\ldots,j-1\) from its ordered positions bijects such sets with ordinary \(j\)-subsets of \([n-j+1]\). Hence their count is \(\binom{n-j+1}{j}\); retaining precisely the ranks \(j\le d\) proves the complete polynomial.

**4. Purity of the truncation.** For \(d\ge1\), we have \(d\le k\) and \(d\le n-2k+1\); therefore \(3d\le2k+d\le n+1\). Every inclusion-maximal independent set of \(P_n\) is dominating. Since each selected vertex can dominate at most three vertices, every maximal independent set has size at least \(\lceil n/3\rceil\). The inequality \(3d\le n+1\) implies \(d\le\lceil n/3\rceil\). Hence every independent face of size less than \(d\) can be extended in \(\operatorname{Ind}(P_n)\) to a face of size \(d\). All maximal faces of the truncated complex have size \(d\): the truncation is pure.

**5. Homotopy and torsion.** A path is chordal. The established vertex-decomposability theorem for independence complexes of chordal graphs implies that \(\operatorname{Ind}(P_n)\) is (possibly nonpure) shellable. The established Björner–Wachs skeleton theorem asserts that every skeleton of a nonpure shellable simplicial complex remains shellable. Therefore the rank-\(d\) truncation is shellable, and the previous paragraph makes it pure of dimension \(d-1\). A finite pure shellable complex has homotopy type a wedge of spheres of its top dimension, and hence torsion-free reduced integral homology concentrated in that dimension. The alternating face count gives its reduced Euler characteristic:
\[
\widetilde\chi(\Delta_{n,k})=-\sum_{j=0}^{d}(-1)^j\binom{n-j+1}{j}=(-1)^{d-1}\beta(n,d).
\]
Comparing with the reduced Euler characteristic of a wedge of \((d-1)\)-spheres determines \(\beta(n,d)\) exactly. The proof covers every admissible \((n,k)\) and does not infer the infinite family from finite calculations.

## Verification
The standalone standard-library Python 3 file `verify.py` enumerates all independent \(k\)-subsets, directly builds the full trace family on **every** potential support for \(1\le n\le16\) (1,004,886 triple cases), and compares it against the structural criterion and coefficient formula. It separately checks the minimax completion identity on all 1,595 independent supports through 13 vertices. Finally it builds boundary matrices, checks homology ranks over \(\mathbb F_2\) and \(\mathbb F_3\) in 28 cases through 11 vertices, and matches the wedge multiplicities. The recorded output ends in `FIXED_WEIGHT_PATH_SHATTERING_PASS`. These finite tests are independent reproducibility evidence, not proofs of shellability or all-order quantifiers; the preceding induction and standard shellability theorems provide those proofs.

## Relationship to prior work
Chase and Freitag's 2018 work develops the shattering and model-theoretic framework, including finite-concept methods, but does not state this fixed-weight path support classification. The existing published-finding corpus study *Fixed-weight cyclic independent sets: a one-logarithm online boundary effect* explicitly reports the **path VC dimension** \(\min\{k,n-2k+1\}\), so that dimension is not claimed as new. Its available indexed summary emphasizes adaptive dimensions and the path/cycle online boundary; it does not expose the all-support classification, the entire face polynomial, or the homotopy decomposition here. A direct full-text comparison with that study could not be completed because its expected public repository resource returned not found, leaving a concrete overlap risk rather than establishing absence by title. The inspected minimum-independent-dominating-set theorem on paths concerns a different, smaller hypothesis family, and the whiskered-graph theorem concerns maximal independent sets with different membership constraints. Established shellability of chordal-graph independence complexes and skeleton preservation are used as prior mathematical results; the new step is identifying the **exact query-shattering complex** with a pure truncation and extracting its complete topological profile.

## Limitations
The size-\(k\) path VC dimension, binomial counts of arbitrary path-independent sets, and general shellability/skeleton theorems are known ingredients and are not independently novel. Historical priority of the new complete support/topology formulation is not certified; notably the related fixed-weight cyclic/path full text was not accessible. The homotopy conclusion uses a previously published general shellability theorem rather than constructing an explicit discrete Morse matching. For \(d=0\), only the empty face remains, and the paper deliberately makes no sphere-wedge claim. No independent external audit has been performed.

## References
1. H. Chase and J. Freitag, *Model theory and combinatorics of banned sequences*, arXiv:1801.07640, first public January 23, 2018, https://arxiv.org/abs/1801.07640.
2. R. Abdelmalek et al., *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, first public June 21, 2021, https://arxiv.org/abs/2106.10863.
3. A. Björner and M. Wachs, *Shellable nonpure complexes and posets. I*, Transactions of the AMS 348 (1996), 1299–1327; standard nonpure shelling and skeleton results.
4. *Fixed-weight cyclic independent sets: a one-logarithm online boundary effect*, published published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-fixed-weight-cyclic-independent-sets-a-one-logarithm-online-boun--253357213fec (full text unavailable at time of comparison; indexed description used only).
5. *A periodic shattering law for minimum independent dominating sets of paths*, published published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-periodic-shattering-law-for-minimum-independent-dominating-set--ab94895bb7a2 (full `RESULT.md` inspected).
6. *A flag-complex realization theorem for maximal-independent-set shattering on whiskered graphs*, published published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-flag-complex-realization-theorem-for-maximal-independent-set-s--0e9b40ed52ce (full `RESULT.md` inspected).
