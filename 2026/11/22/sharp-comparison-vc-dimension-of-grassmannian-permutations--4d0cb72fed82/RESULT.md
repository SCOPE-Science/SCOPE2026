# Sharp comparison VC dimension of Grassmannian permutations

## Finding
Let \(\mathcal G_n\) be the set of permutations \(\pi\) of \([n]\) having at most one descent. For every pair of positions \(1\le i<j\le n\), ask the Boolean inversion query \(q_{ij}(\pi)=[\pi(i)>\pi(j)]\). The complete comparison concept class on the \(\binom n2\) possible queries satisfies, for every integer \(n\ge2\),
\[
\operatorname{VCdim}(\mathcal G_n)=\left\lfloor\frac{n+1}{2}\right\rfloor.
\]
This is a dimension theorem, **not** a claim that all supports with at most that many queries are shattered. Every shattered query support is necessarily a matching, or a matching with one additional edge meeting one of its edges, in the graph on the position labels; the latter necessary condition is not sufficient. For \(n=6\), an explicit complete adaptive comparison tree of depth five shows
\[
\operatorname{VCdim}(\mathcal G_6)=3,\qquad \operatorname{Ldim}(\mathcal G_6)=5.
\]
This is the first two-unit static/adaptive gap in this sequence: the exact dimensions through \(n=6\) are given in the verification table below.

## Assumptions and scope
A descent of a permutation is an index \(i<n\) with \(\pi(i)>\pi(i+1)\). All permutations here are written in one-line notation. A support is a set of distinct unordered position pairs \(\{i,j\}\), represented uniquely with \(i<j\). Its trace is the vector of inversion-query responses, with one coordinate for each pair. A support is VC-shattered when all its binary traces occur. The Littlestone dimension is the maximum depth of a complete binary decision tree, where each internal node asks one position-pair inversion query and every root-to-leaf answer path is consistent with a permutation in the class. The empty support is shattered. No sampling, random hypothesis, or asymptotic approximation is involved.

## Proof
**Lemma 1 (hereditary obstruction).** The class of at-most-one-descent permutations is closed under standardizing any subsequence selected by a subset of positions: removing positions cannot create a second descent. Therefore a query support on \(m\) distinct positions shattered at a larger order would also be shattered by at-most-one-descent permutations on those \(m\) positions, after order-preserving relabeling of the chosen positions.

**Lemma 2 (two finite local obstructions).** On four positions, no three-query support is shattered; on six positions, no four-query support is shattered. Both statements follow by an exhaustive finite, reproducible enumeration: enumerate every permutation of the indicated order with at most one descent, every subset of three or four comparison queries, respectively, and test whether all \(2^3\) or \(2^4\) answer vectors occur. The independent implementations `verify.py` and `verify.cpp` enumerate all such support sizes by extending only already-shattered supports. In the four-position case the full polynomial is \(1+6z+10z^2\), and in the six-position case it is \(1+15z+70z^2+41z^3\); consequently the respective degree-three and degree-four coefficients are zero. Each search is genuinely exhaustive because any shattered support has all its subsets shattered, and every candidate extension is evaluated against all concepts. Finite exhaustive enumeration proves these *finite* lemmas, which are subsequently applied to arbitrary orders by Lemma 1.

**Universal upper bound.** Let \(S\) be a shattered support of \(k\) position-pair queries, viewed as a simple graph on the positions appearing in \(S\). A vertex of degree at least three would yield three incident edges supported on four vertices, contradicting Lemmas 1–2. Two distinct vertices of degree at least two are also impossible: if they share an edge, three of their incident edges yield a three-edge path on at most four vertices (or a triangle, also on at most four vertices); if they do not share an edge, choose two incident edges at each vertex, giving four distinct edges on at most six vertices. Both cases contradict Lemmas 1–2. Thus every positive-degree vertex has degree one, except possibly one vertex of degree two. The handshaking identity then gives at least \(2k-1\) distinct supporting positions. As there are only \(n\) positions, \(k\le\lfloor(n+1)/2\rfloor\).

**Construction attaining the bound.** Let \(k\ge2\) and initially \(n=2k-1\). Consider the \(k\)-query support
\[
S_k=\{(1,k),(1,k+1)\}\cup\{(i,k+i):2\le i\le k-1\}.
\]
We realize all \(2^k\) inversion labels by producing a total order of the **positions by their desired permutation values**, then assigning values \(1,2,\ldots,2k-1\) in that total order. Let \(a,b\in\{0,1\}\) be desired inversion labels on \((1,k)\) and \((1,k+1)\), respectively.

When \((a,b)\) is \((0,0)\), \((1,0)\), or \((1,1)\), sort the first group of positions by increasing desired value as, respectively, \((1,k,k+1)\), \((k,1,k+1)\), or \((k,k+1,1)\). For each \(i=2,\ldots,k-1\) append one more group consisting of positions \(i,k+i\): put \(k+i\) first if its desired inversion label is one, and put \(i\) first otherwise. All these groups are concatenated in the stated order. The resulting assigned permutation is increasing on the first \(k-1\) positions and separately increasing on the final \(k\) positions, so has at most one descent, and it realizes all labels.

When \((a,b)=(0,1)\), put positions \((k+1,1)\) first, then for each \(i=2,\ldots,k-1\) append \((i,k+i)\) or \((k+i,i)\) as determined by its desired inversion label, and finally append position \(k\). The resulting permutation is increasing on positions \(1,\ldots,k\) and separately increasing on positions \(k+1,\ldots,2k-1\), realizes zero on the first query (same initial increasing run), one on the second, and all other requested labels. Thus \(S_k\) is shattered. For every \(n>2k-1\), append new, larger values to these permutations at the right, preserving the traces and the one-descent property. For \(k=1\) and \(n\ge2\), the identity and a transposition of adjacent entries give both responses to query \((1,2)\). This proves equality for all \(n\ge2\).

**Adaptive six-position separation.** The finite class \(\mathcal G_6\) has \(2^6-6=58\) distinct permutations, so a depth-six binary tree would need at least \(64\) different concepts, which is impossible. The accompanying `tree_n6.txt` lists \(31\) internal comparison questions, one for every binary path of length less than five, and \(32\) distinct witness permutations at the leaves. For every leaf, all five successive answers match the stated permutation and it has at most one descent. `check_tree.cpp` validates every branch, all leaves and their consistency. Therefore its Littlestone dimension is exactly five. The verified static dimension is three by the universal formula, so the gap is two. Exhaustive checks of orders two through five rule out an earlier gap of size two.

## Verification
The standalone Python program `verify.py` enumerates all distinct permutations through eight positions via the one-descent test, computes each shattered support polynomial by independent trace masks, and computes the full Littlestone recursion with memoization. The independent C++17 program `verify.cpp` instead generates the same class from all subsets \(A\subseteq[n]\), taking the increasing listing of \(A\) followed by the increasing listing of its complement, deduplicates the resulting permutations, and computes support traces directly. Both cover all support sizes via hereditary extension. The third program, `check_tree.cpp`, independently validates the explicit depth-five certificate. To run:

```
python3 verify.py
c++ -std=c++17 -O2 verify.cpp -o verify_cpp && ./verify_cpp
c++ -std=c++17 -O2 check_tree.cpp -o check_tree_cpp && ./check_tree_cpp tree_n6.txt
```

The exact finite values are:

| \(n\) | Number of concepts | Shattering polynomial coefficients, starting at degree zero | VC dimension | Littlestone dimension |
|---:|---:|---|---:|---:|
| 2 | 2 | 1, 1 | 1 | 1 |
| 3 | 5 | 1, 3, 2 | 2 | 2 |
| 4 | 12 | 1, 6, 10 | 2 | 3 |
| 5 | 27 | 1, 10, 30, 6 | 3 | 4 |
| 6 | 58 | 1, 15, 70, 41 | 3 | 5 |
| 7 | 121 | 1, 21, 140, 161, 10 | 4 | 6 |
| 8 | 248 | 1, 28, 252, 476, 89 | 4 | 7 |

For \(n\ge9\), no corresponding complete shattering-polynomial or Littlestone-dimension formula is asserted. The all-order VC result is justified by the proof, not by extrapolating this table.

## Relationship to prior work
Gil and Tomasko (arXiv:2112.03338, first public 2021-12-06) explicitly develop Grassmannian (at-most-one-descent) permutations, their enumeration \(2^n-n\), pattern avoidance, Dyck-path interpretations and parity restrictions. This provides the canonical object and count, not the comparison-query dimension. Menon and Singh (arXiv:2212.13794, 2022-12-28) study pattern-avoidance refinements by binary words and Dyck paths rather than shattering of positional comparisons. The broader finite-concept literature studies Littlestone dimension and VC-dimension generally. Related published results on unrestricted permutation comparisons, single-peaked preferences and fixed-layer decreasing permutations concern distinct concept classes: in particular unrestricted orders allow far more permutations, while the single-peaked comparison support family has a different two-query shattering profile. There is no implication supplying the present uniform exact formula from the inspected statements.

## Limitations
The local obstruction proof relies on reproducible **exhaustive finite** checks at orders four and six, not on an independently formalized proof assistant. The combinatorial reduction from those small orders to all \(n\) is proved above. No formula for Littlestone dimension at arbitrary \(n\), no complete structural criterion for all shattered supports, and no new enumeration of Grassmannian permutations is claimed. Earlier unindexed or unavailable comparisons could affect historical priority. This result has not had an independent mathematical audit.

## References
1. J. B. Gil and J. A. Tomasko, *Restricted Grassmannian permutations*, arXiv:2112.03338 (first public 2021-12-06), Enumerative Combinatorics and Applications 2 (2022), S4PP6, https://arxiv.org/html/2112.03338v2 .
2. K. Menon and A. Singh, *Dyck paths, binary words, and Grassmannian permutations avoiding an increasing pattern*, arXiv:2212.13794 (first public 2022-12-28), https://arxiv.org/abs/2212.13794 .
3. P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, arXiv:2211.01443 (first public 2022-11-02), https://arxiv.org/abs/2211.01443 .
