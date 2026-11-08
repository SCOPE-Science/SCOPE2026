# Twelve-step resonance and exact orbit census for mixed Hamming waves

## Finding

Let \(d\geq3\), let \(q_1,\ldots,q_d\geq2\) be integers, and suppose at least one \(q_i\) is even and at least one is odd. On the Cartesian product of cliques
\[
G=K_{q_1}\square\cdots\square K_{q_d},
\]
let \(A\) be its ordinary (loopless) adjacency matrix over a field \(\mathbb F_Q\) of order \(Q=2^f\), \(f\geq1\). The reversible nearest-neighbor wave on ordered pairs of vertex configurations is
\[
T(u,v)=(Au+v,u).
\]
Every state is periodic from time zero, and the permutation \(T\) has **exact order twelve**. Every one of the six possible least periods \(1,2,3,4,6,12\) occurs, and there are no other periods.

The following closed census holds, including for unequal alphabet sizes. Partition the coordinate indices into odd and even sets \(O\) and \(E\), and define
\[
U=\prod_{i\in O}q_i,\quad P=\prod_{i\in O}(q_i-2),\quad
V=\prod_{i\in E}q_i,\quad C=\prod_{i\in E}(q_i-2),
\]
\[
h_0=\frac{U+(-1)^dP}{2},\qquad
h_1=\frac{U-(-1)^dP}{2},\qquad
z_a=\frac{h_a(V+C)}{2}\quad(a=0,1).
\]
All these census exponents are nonnegative integers. For \(t=1,2,3,4,6,12\), the exact number \(F(t)=|\operatorname{Fix}(T^t)|\) of **labelled two-row states** fixed by \(t\) updates is
\[
\begin{array}{c|cccccc}
t&1&2&3&4&6&12\\ \hline
F(t)&Q^{z_0}&Q^{2z_0}&Q^{z_0+2z_1}&Q^{2h_0V}&Q^{2z_0+2h_1V}&Q^{2UV}.
\end{array}
\]
For all other positive \(t\), \(F(t)=F(\gcd(t,12))\). The number of **distinct temporal cycles** of least period \(m\mid12\) is
\[
P_m=\frac1m\sum_{r\mid m}\mu(m/r)F(r),
\]
where \(\mu\) is the number-theoretic Möbius function. In particular, the primitive twelve-cycle orbit population is
\[
P_{12}=\frac{Q^{2UV}-Q^{2z_0+2h_1V}-Q^{2h_0V}+Q^{2z_0}}{12}>0.
\]
For the smallest three-coordinate mixed example \(G=K_2\square K_2\square K_3\) and \(Q=2\), the six fixed populations at \(t=1,2,3,4,6,12\) are \(4,16,1024,256,1048576,16777216\); there are exactly \(1310700\) primitive twelve-cycle orbits.

## Assumptions and scope

Graphs are simple and labelled by their coordinate tuples. Adjacency sums exclude the vertex itself. The alphabet sizes \(q_i\) count graph vertices; the field size \(Q\), always a power of two, counts local wave values and need not equal any \(q_i\). A two-row state consists of two independent elements of \(\mathbb F_Q^{V(G)}\). No quotient by spatial automorphisms, translations, or exchange of the two rows is taken. The assumptions on mixed coordinate parity are essential for the *exact twelve* conclusion; the fixed-count algebra also describes the homogeneous-parity boundary, where some periods disappear.

## Proof

**1. Cartesian adjacency decomposition.** Write \(J_q\) for the \(q\times q\) all-ones matrix. The adjacency matrix of \(K_q\) in characteristic two is \(J_q+I_q\). Thus, on \(\bigotimes_i\mathbb F_Q^{q_i}\),
\[
A=(d\bmod2)I+\sum_{i=1}^d J_{q_i}^{(i)},
\]
where each superscript means action in the indicated tensor coordinate only.

**2. Odd-coordinate primary spaces.** For every odd \(q\), \(J_q^2=J_q\), and \(\mathbb F_Q^q\) is the direct sum of the one-dimensional \(J_q\)-eigenspace of eigenvalue one and the \((q-1)\)-dimensional zero-eigenspace. The tensor decomposition over the odd coordinates gives \(h_a\) blocks on which the scalar contribution to \(A\) is \(a\in\{0,1\}\). Indeed, choosing the eigenvalue-one space in a subset \(S\subseteq O\) has multiplicity \(\prod_{i\in O\setminus S}(q_i-1)\) and scalar \(d+|S|\pmod2\). Taking even/odd subsets by \(\prod_{i\in O}((q_i-1)+x)\) at \(x=\pm1\) yields the claimed \(h_0,h_1\). Both are strictly positive because \(O\ne\varnothing\) and every odd \(q_i\ge3\).

**3. Even-coordinate square-zero rank.** For every even \(q\), \(J_q^2=0\), \(\operatorname{rank}J_q=1\), and a basis puts it into one nilpotent length-two block plus \(q-2\) zero blocks. On the tensor product of all even-coordinate spaces, let \(N\) be the sum of their \(J\)-operators. Then \(N^2=0\). Tensor summands consisting solely of the zero blocks form a \(C\)-dimensional subspace where \(N=0\). On every other tensor summand there is a two-block tensor factor; contracting along that factor gives \(HN+NH=I\), because the other factors commute and the field has characteristic two. Hence that summand is acyclic for the square-zero operator \(N\), and its rank is half its dimension. Therefore
\[
\operatorname{rank}N=\frac{V-C}{2},\qquad
\dim\ker N=\frac{V+C}{2}.
\]
Consequently the adjacency space splits into \(A=N\) on a summand of dimension \(h_0V\), and \(A=I+N\) on a summand of dimension \(h_1V\). The respective kernel dimensions of \(N\) are \(z_0,z_1\).

**4. Two reversible clocks.** For an \(A\)-invariant subspace of dimension \(s\), the wave matrix is \(T_A=\left(\begin{smallmatrix}A&I\\I&0\end{smallmatrix}\right)\). It is invertible and obeys \(T_A^2=A T_A+I\), where \(A\) acts diagonally on the two-row space. On the \(A=N\) summand, \(N^2=0\) gives \(T_A^4=I\). Directly, \(\ker(T_A-I)\) has dimension \(\dim\ker N\), and \(\ker(T_A^2-I)\) has dimension \(2\dim\ker N\). On the \(A=I+N\) summand, \(A^2=I\) gives \(T_A^3=\operatorname{diag}(A,A)\) and \(T_A^6=I\). Here \(T_A-I\) is invertible, as a fixed pair would have equal rows and satisfy \(Ax=0\), which forces \(x=0\). Thus the fixed dimension at three steps is \(2\dim\ker N\), and at six steps it is \(2s\). These facts, together with direct-sum multiplicativity, give all six displayed \(F(t)\).

**5. Sharpness and orbit inversion.** Since \(E\ne\varnothing\), the rank \((V-C)/2\) is positive. The \(a=0\) sector therefore supports a genuine order-four state; the \(a=1\) sector supports order-three and order-six states. Their direct-sum combinations realize order twelve; the same sectors realize periods one, two, three, four and six separately. There are no periods outside the divisors of twelve because \(T^{12}=I\). Möbius inversion on \(F(t)=\sum_{m\mid t}mP_m\) yields the orbit formulas. This is an all-parameter proof; finite checks are corroborative only.

## Verification

The standalone `check_matrices.py` constructs adjacency matrices directly from coordinate tuples, forms the two-row wave over \(\mathbb F_2\), computes ranks of \(T^t-I\) for all six divisors \(t\mid12\), and compares the resulting fixed populations against the theorem on nineteen graph families (up to thirty-six graph vertices). The independent `check_bruteforce.py` performs direct state transitions without matrix-rank calls and classifies every one of 266,576 two-row states across five small Cartesian products, including the mixed \(K_2\square K_3\). Their captured stdout files are included. Invoke with `python3 check_matrices.py` and `python3 check_bruteforce.py` from the directory containing the scripts. Only binary fields were tested computationally; the argument establishes every \(\mathbb F_{2^f}\).

## Relationship to prior work

Second-order reversible update construction is classical: Vlasov (2013, arXiv:1311.4297, Section 3 and Section 6.1) explicitly gives the same two-time-level XOR mechanism for binary local cellular rules. Cartesian products of complete graphs as Hamming graphs are standard (Klavžar–Peterin, 2005). The novel assertion assessed here is the *mixed-arity Cartesian-clique adjacency decomposition, exact all-parameter wave fixed-point/orbit census and universal sharp twelve-step resonance* for dimensions at least three. The ordinary real Hamming adjacency eigenspaces analyzed by Valyuzhenich (2020) do not determine the characteristic-two nilpotent Jordan ranks: reducing an eigenbasis modulo two is invalid when a coordinate size is even. Earlier special wave classifications on other graph families or diameter-two graphs do not directly furnish the mixed-arity, diameter-at-least-three census.

## Limitations

This counts temporal cycles with individual vertices labelled and does not classify spatial-symmetry quotient cycles. It assumes characteristic two, the specific unweighted adjacency rule, and both odd and even coordinate sizes. The all-even or all-odd boundary is not claimed to have exact order twelve. Direct computation is finite and does not constitute a proof for all coordinate sizes. The originality comparison is evidence-based rather than a guarantee against unindexed or inaccessible antecedents.

## References

1. S. Klavžar and I. Peterin, “Characterizing subgraphs of Hamming graphs,” *Journal of Graph Theory* 49 (2005), 302–312. DOI: 10.1002/jgt.20084. First available publication date verified as 2005-04-08.
2. A. Yu. Vlasov, “On generalization of reversible second-order cellular automata,” arXiv:1311.4297 (first posted 2013-11-18), Sections 3 and 6.1. https://arxiv.org/abs/1311.4297.
3. T. Toffoli and N. Margolus, “Invertible cellular automata: a review,” *Physica D* 45 (1990), 229–253, DOI: 10.1016/0167-2789(90)90185-R. Background on reversible automata, not a source for the present orbit census.
4. A. Valyuzhenich, “Eigenfunctions and minimum 1-perfect bitrades in the Hamming graph,” arXiv:2003.01571 (2020), Sections 1–2 and eigenfunction/support classifications. https://arxiv.org/abs/2003.01571.
