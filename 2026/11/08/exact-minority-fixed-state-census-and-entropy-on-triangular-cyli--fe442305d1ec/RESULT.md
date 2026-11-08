# Exact minority fixed-state census and entropy on triangular cylinders

## Finding
For every integer \(n\ge3\), let \(G_n=C_n\square K_3\), with three labelled vertices in each of \(n\) cyclic columns. In synchronous binary open-neighborhood **minority** dynamics, each vertex takes the less frequent neighbor opinion, retaining its own opinion if the four neighbors split equally. Let \(U_n\) denote the number of labelled configurations fixed after one update.

Define
\[
p(X)=X^3-3X^2-3X+2,\qquad q(X)=X^4+X^3+4X^2-3X+3,
\]
and let \(S_f(n)\) be the sum of the \(n\)-th powers of the complex roots of \(f\), with algebraic multiplicity. Then the following exact formula holds for every \(n\ge3\):
\[
\boxed{U_n=2^n+3(-1)^n+9\mathbf 1_{3\mid n}+S_p(n)+2S_q(n).}
\]
The initial counts \(U_3,\ldots,U_{10}\) are \(102,188,510,2918,9240,30836,124374,448208\).

Let \(\lambda\) be the unique root of \(p\) in \((3,4)\); numerically \(\lambda\approx3.66907908828229\). The remaining characteristic roots have modulus strictly smaller than \(3\). Therefore
\[
\boxed{U_n=\lambda^n+O(3^n),\qquad
\lim_{n\to\infty}\frac{\log U_n}{3n}=\frac{\log\lambda}{3}\approx0.433313566985.}
\]
Equivalently, the fraction of the \(2^{3n}\) binary configurations that are fixed is asymptotic to \((\lambda/8)^n\).

## Assumptions and scope
Vertices are \((i,j)\) for \(i\in\mathbb Z/n\mathbb Z\) and \(j\in\{0,1,2\}\). Vertex \((i,j)\) is adjacent to \((i-1,j),(i+1,j)\) and the other two vertices of column \(i\). For \(n\ge3\), these four neighbors are distinct and the graph is simple, connected, and four-regular. There is no self-voting except tie retention. This theorem counts fixed configurations at time zero, not transient states, period-two states, or global energy minimizers.

## Proof
A configuration is fixed exactly when each vertex has at least two neighbors of the opposite color. Indeed, a vertex whose own color occurs among its four neighbors at most twice either is the strict neighbor minority or retains its color at a tie; if its own color occurs at least three times, it must change. Thus fixed configurations are precisely the unfriendly binary partitions (single-spin stable states for the uniform antiferromagnetic Ising interaction with zero-field ties allowed).

Encode each column by its three-bit integer \(b\in\{0,\ldots,7\}\). For three consecutive columns \((a,b,c)\) and rail \(j\in\{0,1,2\}\), let \(b_j\) be the \(j\)-th bit and define the number of 1-neighbors of the central vertex as
\[
 t_j(a,b,c)=a_j+c_j+\operatorname{popcount}(b)-b_j.
\]
The central column is fixed precisely when, for every \(j\), \(b_j=1\) implies \(t_j\le2\), and \(b_j=0\) implies \(t_j\ge2\).

Index a \(64\times64\) zero-one integer matrix \(T\) by ordered column pairs \((a,b)\), and set \(T_{(a,b),(b',c)}=1\) if \(b'=b\) and all three preceding inequalities hold; set every other entry to zero. Each closed walk of length \(n\) in this pair-state graph corresponds bijectively to one assignment of all \(n\) cyclic columns obeying the fixed-point condition, with the vertices and positions labelled. Consequently, \(U_n=\operatorname{tr}(T^n)\), valid for every \(n\ge3\), without boundary correction.

Exact integer evaluation of this explicitly defined finite matrix gives
\[
\det(XI-T)=X^{40}(X-2)(X-1)^3(X+1)^3(X^2+X+1)^3p(X)q(X)^2.
\]
This finite polynomial identity is independently reconstructible by the complete standalone \(\texttt{verify\_transfer.py}\) program. It is not an approximation or an extrapolation from initial terms. For \(n\ge1\), the trace is the sum of the \(n\)-th powers of all eigenvalues with multiplicity, whether or not the matrix is diagonalizable. Since the two roots of \(X^2+X+1\) have power sum \(2\) when \(3\mid n\) and \(-1\) otherwise, substituting the characteristic factorization yields the displayed exact formula.

The cubic \(p\) has roots in \((-2,-1)\), \((0,1)\), and \((3,4)\), by sign changes at the six listed endpoints. Since its degree is three these are all its roots, and the last one, \(\lambda\), is its unique root of modulus greater than \(3\). On \(|z|=3\), one has \(|z^4|=81>27+36+9+3\), so Rouché's theorem applied to \(q(z)=z^4+(z^3+4z^2-3z+3)\) puts all four roots of \(q\) strictly inside \(|z|<3\). Every other characteristic root has modulus at most two, apart from those of \(q\) which are strictly inside three. Hence \(U_n=\lambda^n+O(3^n)\). Taking logarithms of this positive count proves the entropy and fraction formulas.

## Verification
The standalone reproducibility files \(\texttt{verify\_transfer.py}\) and \(\texttt{verify\_direct.py}\) contain all data and use only Python 3 (with SymPy for the exact characteristic polynomial). The symbolic program reconstructs every matrix entry from the stated inequalities, computes the characteristic polynomial by exact integer arithmetic, compares it coefficientwise with the displayed factorization, and independently checks trace values through \(n=14\). It finds exactly \(218\) unit entries in the transfer matrix.

The direct program separately reconstructs the four-neighbor graph, applies the original synchronous minority update to each labelled binary configuration, and exhaustively checks all \(2^{3n}\) configurations for each \(3\le n\le7\). This covers \(2{,}396{,}672\) configurations and gives counts \(102,188,510,2918,9240\), agreeing with the exact formula. Finite enumeration is corroboration only; the all-size theorem follows from the matrix identity and spectral argument.

## Relationship to prior work
Wacław and Burda (2008) develop a field-theoretic approximation for averages of single-spin-stable states under random Gaussian Ising couplings on various graph families, including ladders. Their paper does not compute the exact fixed-state population on the present all-negative, four-regular triangular cylindrical family. Jen (1988) supplies the general transfer-matrix paradigm for periodic one-dimensional automata; the finite spectral identity, characteristic factors, and growth constant reported here require an additional specific calculation and are not explicitly given by that paradigm. Turau (2023) proves fixed-state counting results for trees, not for the nonbipartite cyclic graph family studied here. The connection to unfriendly partitions is a known general equivalence, not claimed as a new theorem.

## Limitations
No assertion is made about dynamics outside the fixed-point locus, global maximum cuts, higher-width triangular cylinders, or disordered couplings. The exact spectral formula is verified algebraically and by small-instance exhaustive simulation, but has not undergone independent scientific audit. Unindexed earlier computations or an inaccessible broader catalogue of local antiferromagnetic metastable states could contain an equivalent expression; the novelty assessment is qualified accordingly.

## References
1. B. Wacław and Z. Burda, *Counting metastable states of Ising spin glasses on arbitrary graphs*, arXiv:0801.1224v1 (first public arXiv posting 2008-01-08), https://arxiv.org/abs/0801.1224 .
2. E. Jen, *Cylindrical cellular automata*, Communications in Mathematical Physics **118** (1988), 569–590, https://doi.org/10.1007/BF01221109 .
3. V. Turau, *Counting Problems in Trees, with Applications to Fixed Points of Cellular Automata*, arXiv:2312.13769v1 (2023), https://arxiv.org/abs/2312.13769 .
