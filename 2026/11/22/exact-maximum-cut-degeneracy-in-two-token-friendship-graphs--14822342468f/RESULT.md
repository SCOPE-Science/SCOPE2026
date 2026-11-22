# Exact maximum-cut degeneracy in two-token friendship graphs

## Finding
For every integer \(q\ge1\), let \(W_q\) consist of \(q\) triangles sharing a common vertex. Let \(H_q=F_2(W_q)\) be the unweighted two-token graph, and let \(N_q\) count *unordered* maximum cuts of \(H_q\), so that interchanging both cut sides does not create a second cut. Then
\[
N_q=\frac12\sum_{\substack{a,b,c\ge0\\a+b+c=q}}\frac{q!}{a!b!c!}\,4^c\,7^{\binom a2+\binom b2}\,2^{ab}\,5^{(a+b)c}\,6^{\binom c2}.
\]
The first values for \(q=1,2,3,4,5,6\) are respectively \(3,97,17239,17108945,96059118421,3084812337312399\). The stronger asymptotic description is
\[
\lim_{q\to\infty}\frac{N_q}{7^{\binom q2}}=1.
\]
Equivalently, with probability tending to one, a uniformly chosen maximum cut places every vertex \(\{o,a_i\},\{o,b_i\}\) on the same side, where \(o\) is the common hub of \(W_q\). The scalar maximum-cut value is \(\operatorname{MaxCut}(H_q)=2q(2q-1)\); this value follows from a known token-graph triangle argument and is not presented as new.

## Assumptions and scope
All graphs are finite, simple, undirected and unweighted. The vertices of \(W_q\) are \(o\) and two labelled leaves \(a_i,b_i\) for each \(1\le i\le q\), with precisely the edges \(oa_i,ob_i,a_ib_i\). A vertex of \(H_q\) is an unordered pair of distinct vertices of \(W_q\). Two such pairs are adjacent exactly when their symmetric difference is one of the specified edges. A cut is an unordered bipartition of all the labelled vertices of \(H_q\), with empty sides allowed; equivalently it is a binary coloring modulo simultaneous color reversal. There is no quotient by permutations of the parent triangles or their leaves. Every exponent and binomial coefficient in the formula is an ordinary nonnegative integer.

## Proof
**1. A saturated triangle partition of the edge set.** Each of the \(3q\) parent edges induces \((2q-1)\) edges of \(H_q\), one for each placement of the other token outside its two endpoints. For every parent triangle \(\{o,a_i,b_i\}\), these induced edges can be partitioned into exactly \(2q-1\) edge-disjoint triangles in \(H_q\): the triangle on \(\{o,a_i\},\{o,b_i\},\{a_i,b_i\}\), and one triangle on \(\{v,o\},\{v,a_i\},\{v,b_i\}\) for each vertex \(v\) outside that parent triangle. Each token edge belongs to precisely one of these triangles because its symmetric difference uniquely determines one of the three edges in one parent triangle, and its fixed token determines which lifted triangle to use. Thus the edge set is partitioned into \(q(2q-1)\) triangles.

Every cut misses at least one edge of each of these triangles, giving \(\operatorname{MaxCut}(H_q)\le 2q(2q-1)\). The parity lift of the parent coloring that assigns the hub one color and every leaf the other produces a cut crossing exactly two edges of each lifted triangle. Thus the bound is attained. A cut is maximum **if and only if** every lifted triangle is nonmonochromatic. This scalar upper/lower bound is an instance of the existing triangle-packing/parity-lift method; the classification and counting below are the additional conclusion.

**2. Independent constraints after the hub-token colors are fixed.** Choose two ordered cut colors \(0,1\). Write \(h_i=(h_{i0},h_{i1})\in\{00,01,10,11\}\), where \(h_{i0}\) colors \(\{o,a_i\}\) and \(h_{i1}\) colors \(\{o,b_i\}\). The remaining token vertices are of two kinds:

- The single within-petal vertex \(\{a_i,b_i\}\), whose color must make \((h_{i0},h_{i1},d_i)\) nonmonochromatic. There is exactly one possible color for \(h_i\in\{00,11\}\) and two possible colors for \(h_i\in\{01,10\}\).
- For every \(i<j\), four cross-petal token vertices \(\{a_{i,r},a_{j,s}\}\), indexed by \(r,s\in\{0,1\}\) with \(a_{i,0}=a_i\) and \(a_{i,1}=b_i\). Put their colors in a \(2\times2\) binary matrix \(X=(x_{rs})\). Exactly four lifted-triangle constraints involve these four variables: each row \(r\) obeys \(\operatorname{NAE}(h_{ir},x_{r0},x_{r1})\), and each column \(s\) obeys \(\operatorname{NAE}(h_{js},x_{0s},x_{1s})\). Here \(\operatorname{NAE}\) means that the three entries are not all equal.

No other lifted triangle couples different within-petal variables or different cross-petal matrices. For fixed \(h_1,\ldots,h_q\) all these local completions multiply independently. Counting the \(16\) binary matrices for each ordered pair \((h_i,h_j)\) gives
\[
M=\begin{pmatrix}7&5&5&2\\5&6&6&5\\5&6&6&5\\2&5&5&7\end{pmatrix}
\quad\text{in the state order }(00,01,10,11),
\]
and the within-petal weights are \(f=(1,2,2,1)\). Consequently the exact number of **ordered** optimal colorings is
\[
\sum_{h_1,\ldots,h_q\in\{00,01,10,11\}}
\prod_{i=1}^{q} f(h_i)\prod_{1\le i<j\le q}M(h_i,h_j).
\]
Combine the two mixed states \(01,10\): each mixed petal contributes a factor \(2\) for its orientation and a factor \(2\) for its within-petal choice, i.e., \(4\); pure \(00\) and \(11\) petals have weight \(1\). A pair of pure equal petals contributes \(7\), opposite pure petals \(2\), pure/mixed petals \(5\), and two mixed petals \(6\). Grouping by counts \((a,b,c)\) of \(00,11,\mathrm{mixed}\), there are \(q!/(a!b!c!)\) ways to place these types. This proves the displayed sum for ordered colorings. Simultaneous reversal has no fixed coloring (the token graph has vertices), so dividing by two counts unordered cuts as claimed.

**3. The asymptotic and concentration.** Divide the ordered count by \(7^{\binom q2}\). The two configurations in which every hub state is \(00\) or every hub state is \(11\) contribute exactly \(2\) in total. Every other term is nonnegative. We show their sum tends to zero. A three-type assignment with counts \((a,b,c)\) contributes at most
\[
4^c(2/7)^{ab}(5/7)^{(a+b)c}(6/7)^{\binom c2}.
\]
There are at most \(3^q\) three-type assignments, each with site weight at most \(4^q\). If \(c\ge q/3\), its contribution is at most \(12^q(6/7)^{\binom{\lceil q/3\rceil}{2}}\), which tends to zero. If \(c<q/3\) but both \(a\ge q/6\) and \(b\ge q/6\), the sum of this entire class is at most \(12^q(2/7)^{q^2/36}\), again tending to zero.

In every remaining nonconstant assignment one of the pure counts, say \(a\), exceeds \(q/2\), and the number \(d=q-a=b+c\) satisfies \(1\le d<q/2\). Every cross pair joining this majority pure type to one of the \(d\) exceptional petals contributes a factor at most \(5/7\) after normalization. There are at most \(\binom qd 2^d\) ways to select and type the exceptions, whose combined local site weight is at most \(4^d\). Other pair factors are at most one. Allowing both choices of pure majority, this class has total normalized weight at most
\[
2\sum_{d=1}^{\lfloor q/2\rfloor}\binom qd 8^d(5/7)^{d(q-d)}
\le 2\left(\bigl(1+8(5/7)^{q/2}\bigr)^q-1\right)\longrightarrow0.
\]
These classes exhaust all nonconstant assignments. The ordered count is thus \((2+o(1))7^{\binom q2}\), and the unordered count is \((1+o(1))7^{\binom q2}\). The same estimate shows that a uniformly selected maximizing coloring has all hub-token colors equal with probability tending to one.

## Verification
The standalone Python program `verify_formula.py` recomputes \(M\) by enumerating all binary \(2\times2\) matrices and checks the multinomial formula against an independent four-state sum for \(1\le q\le6\). The standalone C++17 program `verify_direct.cpp` constructs each token graph from its parent graph without using the formula and enumerates every unordered cut for \(1\le q\le3\). Both programs use exact integer arithmetic for all assertions. To rerun, execute `python3 verify_formula.py`, then `g++ -std=c++17 -O2 verify_direct.cpp -o verify_direct && ./verify_direct`. The proof above, not finite testing, covers every integer \(q\ge1\).

## Relationship to prior work
Apte, Parekh and Sud, *Conjectured Bounds for 2-Local Hamiltonians via Token Graphs*, first public June 3, 2025, motivate the study of token graph energy and frustrated configurations from spectral graph methods. Their spectral bounds neither enumerate maximum cuts nor imply the present result. Subsequently Alejandro-Soto et al., *Max-Cut on Token Graphs*, arXiv:2611.25153v1 (November 18, 2026), derive a parity-lift cut lower bound and a triangle-partition method; these **already imply the maximum-cut size** in the present family. Their work does not determine the number of optimal cuts or the optimal-configuration concentration for friendship graphs. The matrix \(M\), the multinomial degeneracy formula and its asymptotic are the newly established results here. Earlier double-vertex/token-graph literature defines and studies the objects, but an independently published equivalent optimum enumerator has not been ruled out exhaustively.

## Limitations
The exact formula is restricted to **unweighted** two-token graphs of friendship graphs; it does not apply to arbitrary token number, edge weights or general cactus graphs without further argument. The asymptotic concerns labeled token-graph vertices and only identifies the dominant hub-token color pattern; it does not classify automorphism orbits. Historical priority may require examination of older hard-to-access literature. These conclusions have been checked within this manuscript but not independently audited.

## References
1. A. Apte, O. Parekh and J. Sud, *Conjectured Bounds for 2-Local Hamiltonians via Token Graphs*, arXiv:2506.03441v1, first public 2025-06-03. https://arxiv.org/abs/2506.03441
2. J. A. Alejandro-Soto, P. T. Araujo, R. Fabila-Monroy, S. G. Gómez-Galicia, M. Hibat-Allah, M. M. R. Raj, M. A. Shamim and A. L. Trujillo-Negrete, *Max-Cut on Token Graphs*, arXiv:2611.25153v1, first publicly available 2026-11-18. https://arxiv.org/html/2611.25153v1
3. R. Fabila-Monroy et al., *Token graphs*, Graphs and Combinatorics 28 (2012), 365–380. DOI:10.1007/s00373-011-1055-9.
4. Deepalakshmi et al., *On the 2-token graph of a graph*, 2020. DOI:10.1016/j.akcej.2019.05.002 (full source not obtained for this comparison).
