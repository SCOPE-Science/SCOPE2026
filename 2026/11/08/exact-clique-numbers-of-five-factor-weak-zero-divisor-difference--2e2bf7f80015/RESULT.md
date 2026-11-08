# Exact clique numbers of five-factor weak zero-divisor difference graphs

## Finding
Let \(R=\prod_{i=1}^{5}\mathbb F_{q_i}\), with arbitrary finite-field orders \(q_i\ge2\), and let \(\mathcal D(R)=W\Gamma(R)-\Gamma(R)\) be the weak zero-divisor difference graph, with isolated vertices deleted. Set \(a_i=q_i-1\), and relabel the factors so that \(a_1\ge a_2\ge a_3\ge a_4\ge a_5\). Define
\[
T=\sum_{1\le i<j<k\le5}a_ia_ja_k,\quad B=5+T,\quad
\Delta_{ij}=a_i a_j-\prod_{k\notin\{i,j\}}a_k,
\]
and
\[
U=4+a_1\left(1+\sum_{j=2}^{5}a_j+\sum_{2\le j<k\le5}a_ja_k\right).
\]
Then the exact clique number is the maximum of **seven explicit quantities**:
\[
\boxed{\begin{aligned}
\omega(\mathcal D(R))=\max\{&U,\ B,\ B+\Delta_{12},\ B+\Delta_{12}+\Delta_{13},\\
&B+\Delta_{12}+\Delta_{13}+\Delta_{14},\\
&B+\Delta_{12}+\Delta_{13}+\Delta_{14}+\Delta_{15},\\
&B+\Delta_{12}+\Delta_{13}+\Delta_{23}\}.\end{aligned}}
\]
Equivalently, **without ordering the factors**, put
\[
U_i=4+a_i\left(1+\sum_{j\ne i}a_j+
\sum_{\substack{j<k\\j,k\ne i}}a_ja_k\right),
\]
\[
S_i=\sum_{j\ne i}(\Delta_{\min(i,j),\max(i,j)})_+,
\qquad C_{ijk}=(\Delta_{ij})_++(\Delta_{ik})_++(\Delta_{jk})_+
\]
for \(i<j<k\), where \((x)_+=\max\{0,x\}\). Then
\[
\omega(\mathcal D(R))=\max\left\{\max_i U_i,
5+T+\max\left(0,\max_i S_i,\max_{i<j<k}C_{ijk}\right)\right\}.
\]
Both expressions hold for every tuple of prime-power field orders, including tied orders and factors isomorphic to \(\mathbb F_2\).

## Assumptions and scope
The zero-divisor graph \(\Gamma(R)\) has all nonzero zero divisors as vertices, with distinct vertices joined when their product is zero. The weak graph \(W\Gamma(R)\) joins distinct \(x,y\) if nonzero \(r\in\operatorname{Ann}(x)\), \(s\in\operatorname{Ann}(y)\) satisfy \(rs=0\). The difference graph retains the weak edges not present in \(\Gamma(R)\), and deletes isolated vertices. There are exactly five direct factors, each a finite field. No assumptions on their characteristics or relative sizes are imposed.

For a nonempty proper subset \(A\subsetneq[5]\), let \(X_A\) be the set of elements with exactly the coordinates in \(A\) nonzero. Its size is \(w(A)=\prod_{i\in A}a_i\). All \(X_A\) occur, and \(w(A)>0\). For two distinct classes \(X_A,X_B\), there are all possible difference-graph edges between the classes exactly when \(A\cap B\ne\varnothing\). A class \(X_A\) induces a clique for \(|A|\le3\), and an independent set for \(|A|=4\). These are the support-decomposition properties established by Wani; they also follow directly from the annihilator definition.

## Proof
**1. Reduction to intersecting support families.** Given a graph clique, replace its set of represented support classes by a family \(\mathcal F\) of nonempty proper subsets of \([5]\). Its distinct members must intersect pairwise. A class of size at most three may contribute all \(w(A)\) vertices, whereas a class of size four may contribute at most one. Conversely, any intersecting \(\mathcal F\), taking all possible class vertices for smaller supports and one for each support of size four, produces a clique. Thus the clique number equals the maximum weighted size of an intersecting support family, with weight \(w(A)\) for \(|A|\le3\) and weight \(1\) for \(|A|=4\).

**2. Families containing a singleton.** If \(\{i\}\in\mathcal F\), every member contains \(i\). All positive-weight supports containing \(i\) may be included simultaneously. They comprise one singleton, four pairs, six triples, and four four-element supports. Their total weight is exactly \(U_i\). Therefore the optimal singleton-containing clique has weight \(\max_i U_i\).

**3. Families without singleton supports.** Every four-element support intersects every support of size two or more. It may therefore be included, contributing exactly \(5\) in total. Every pair of three-element supports intersects, so all triples can be included except those forbidden by chosen two-element supports. A two-element support \(P\) is disjoint from exactly one three-element support, namely its complement \(P^c\); it is compatible with all other triples. Distinct two-element supports must themselves intersect. Hence, if \(\mathcal P\subseteq\binom{[5]}{2}\) is any pairwise-intersecting family of pairs, the best total weight with this exact pair layer is
\[
5+T+\sum_{P\in\mathcal P}\bigl(w(P)-w(P^c)\bigr)
=5+T+\sum_{\{i,j\}\in\mathcal P}\Delta_{ij}.
\]
A family of pairwise-intersecting edges of the complete graph on five vertices is contained either in a star (all pairs contain one common coordinate) or in a triangle. Indeed, after any two distinct intersecting edges \(\{a,b\}\), \(\{a,c\}\), a third edge meeting both must either contain \(a\) or equal \(\{b,c\}\). If the latter occurs, every edge meeting all three edges lies among those of this triangle. If it does not occur, all edges share \(a\). This also handles families of at most two edges. Within any fixed star or triangle, one may choose each positive-gain edge separately and omit each nonpositive-gain edge. The resulting optimum is exactly the unordered positive-part formula stated above.

**4. Seven candidates when the field orders are sorted.** If \(a_i\ge a_j\), replacing the pair \(\{j,k\}\) by \(\{i,k\}\) for distinct \(i,j,k\) cannot decrease its gain: writing \(d=\prod_{\ell\notin\{i,j,k\}}a_\ell\), the difference of gains is \((a_i-a_j)(a_k+d)\ge0\). The same coordinate replacement cannot decrease a singleton-star total. Thus the largest singleton star is the one centered at \(1\), the largest pair-star gain is centered at \(1\), and the largest triangle gain is achieved on coordinates \(1,2,3\). Since \(\Delta_{12}\ge\Delta_{13}\ge\Delta_{14}\ge\Delta_{15}\) and \(\Delta_{12}\ge\Delta_{13}\ge\Delta_{23}\), the maximum positive-gain subset of the best star is one of its five initial segments, while for the best triangle it is one of \(\varnothing\), \(\{12\}\), \(\{12,13\}\), and \(\{12,13,23\}\). Removing repeated cases gives the six non-singleton candidates shown in the box. Together with \(U\), these are the seven claimed expressions. They are all realized by the corresponding support families, so the bounds are equalities.

## Verification
The standard-library Python program `verify.py` constructs the 30-vertex intersection graph of nonempty proper supports and enumerates every maximal clique by a bitmask Bron--Kerbosch procedure, independently of the case analysis. It weighs a four-element support by one and all smaller supports by the size of its field-element class. For 39 heterogeneous parameter tuples, it compares this independent maximum with both formulas. All 81 maximal support families are enumerated each time. It also tests the annihilator-witness definition of the graph directly against the support-class criterion for all unordered vertex pairs in four products of prime fields. The program prints `VERIFY_OK`; run `python3 verify.py` from the directory containing the file. `verification_output.txt` contains its actual output. No external packages are needed.

For \((q_1,\ldots,q_5)=(11,11,11,2,2)\), the formula gives \(1905\), agreeing with the previously published finite example. Finite checks are corroboration; the proof covers all field orders by the support-family argument.

## Relationship to prior work
Wani, *The Weak Zero-Divisor Difference Graph of a Finite Commutative Ring* (arXiv:2607.17677, first publicly posted 20 July 2026), establishes the exact support adjacency and internal-class structure used in Step 1. That paper determines clique numbers for three and four field factors, gives general upper/lower bounds, evaluates the five-factor example above as \(1905\), and poses Question 6.11 asking for a general exact formula for at least five factors. It also proves existence of a shifted extremal family but does not give the five-factor case classification. The theorem here supplies that first unresolved five-factor case uniformly over all field sizes. It does not claim to resolve six or more factors. The weakly zero-divisor graph introduced by Nikmehr, Azadi, and Nikandish (2021), and the ordinary zero-divisor graph, are different graph constructions; their known invariants do not state this difference-graph formula.

## Limitations
Only the clique number is determined, not the chromatic number. The result is restricted to products of precisely five finite fields; nilpotents, arbitrary finite reduced rings with at least six factors, and noncommutative rings are outside the proof. The seven candidates describe the optimum weight and supply attaining support configurations; they do not classify every maximum clique when gains vanish or field orders tie. It remains possible that an older result on weighted intersecting Boolean families implies the formula without using this graph's terminology. Independent mathematical and historical-priority auditing has not been performed.

## References
1. B. A. Wani, *The Weak Zero-Divisor Difference Graph of a Finite Commutative Ring*, arXiv:2607.17677 (first public version 2026-07-20), https://arxiv.org/abs/2607.17677, especially Sections 3, 6, and 8 and Question 6.11.
2. M. J. Nikmehr, A. Azadi, R. Nikandish, *The weakly zero-divisor graph of a commutative ring*, Revista de la Unión Matemática Argentina (2021), https://doi.org/10.33044/revuma.1677.
3. MSC2020 classification: 13A70, general commutative ring theory and combinatorics (zero-divisor graphs, annihilating-ideal graphs, etc.).
