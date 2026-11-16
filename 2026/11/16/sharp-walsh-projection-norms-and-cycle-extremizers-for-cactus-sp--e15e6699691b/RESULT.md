# Sharp Walsh projection norms and cycle extremizers for cactus spanning trees

## Finding
Let \(G\) be a finite, connected, simple cactus graph: every edge belongs to at most one simple cycle. Let \(b\) be its number of bridges, and let its simple cycle lengths be \(\ell_1,\ldots,\ell_r\), each at least three. Put \(E=E(G)\), \(H=\mathbb F_2^E\), and let \(A_G\subset H\) be the edge-incidence vectors of its spanning trees. All claims include trees (\(r=0\)), and the one-vertex graph, with empty products equal to one.

The unnormalized Walsh transform of \(1_{A_G}\), at any \(x\in H\), is exactly
\[
\widehat{1_{A_G}}(x)=\left(\prod_{e\text{ bridge}}s_e\right)
\prod_{j=1}^r\left[\left(\prod_{e\in C_j}s_e\right)
\left(\sum_{e\in C_j}s_e\right)\right],\qquad s_e=(-1)^{x_e}.
\]
Consequently convolution by \(1_{A_G}\) is invertible on \(\ell^2(H)\) if and only if **every cycle of \(G\) has odd length**. Its exact rank in all cases is
\[
2^b\prod_{j=1}^r\left(2^{\ell_j}-\mathbf1_{2\mid\ell_j}{\ell_j\choose\ell_j/2}\right).
\]
If all cycles are odd, the smallest absolute Fourier multiplier is exactly one, the largest is \(\prod_j\ell_j\), and hence
\[
\|C_G^{-1}\|_{2\to2}=1,\qquad \kappa_2(C_G)=\prod_{j=1}^r\ell_j,
\]
where \(C_Gf=1_{A_G}*f\) uses unnormalized convolution. More generally, if there are \(e\) even cycles, the smallest **nonzero** absolute multiplier is exactly \(2^e\).

For the Fourier projection \(P_{A_G}\) retaining precisely the frequencies in \(A_G\), its two sharp endpoint norms coincide:
\[
\boxed{\ \|P_{A_G}\|_{1\to1}=\|P_{A_G}\|_{\infty\to\infty}
=\prod_{j=1}^r\alpha_{\lfloor(\ell_j-1)/2\rfloor},\quad
\alpha_m=\frac{(2m+1){2m\choose m}}{4^m}.\ }
\]
This depends **only** on the cycle lengths, not on the cactus block tree or bridge locations.

There is also an exact sharp extremal law. For every cactus on \(N\ge1\) vertices, let \(K=\lfloor(N-1)/2\rfloor\). Then
\[
\boxed{\ \|P_{A_G}\|_{1\to1}\le (3/2)^K.\ }
\]
For \(K\ge1\), equality holds **precisely** when the cycles consist of \(K\) triangles, with no bridges if \(N\) is odd, and either one bridge or replacement of exactly one triangle by a quadrilateral if \(N\) is even. All such cactus block arrangements attain equality. For \(N=1,2\), the only connected cacti are trees and the norm is one.

More generally, for a prescribed feasible cycle count \(1\le r\le K\), put \(a=\lfloor K/r\rfloor\), \(u=K-ra\). The maximum endpoint projection norm is
\[
\boxed{\ \alpha_a^{r-u}\alpha_{a+1}^{u}.\ }
\]
It is attained exactly when the effective half-lengths \(\lfloor(\ell_j-1)/2\rfloor\) differ by at most one and sum to \(K\). Equivalently the cycles have odd lengths \(2a+1\) or \(2a+3\) in counts \(r-u\) and \(u\); if \(N\) is even, there is exactly one spare edge, either a bridge or an increment by one of the length of exactly one cycle. The maximum is independent of the attachment topology.

## Assumptions and scope
All graphs are undirected, connected, and simple. A cactus has edge-disjoint simple cycles but may have cycles intersecting in cut vertices. Walsh characters use the standard coordinate pairing on \(\mathbb F_2^E\). The norm on the finite group is unchanged by whether counting measure or normalized counting measure is used consistently for input and output. Convolution \(C_G\) is unnormalized, whereas Fourier projection \(P_{A_G}\) uses the normalized inverse Fourier transform. The extremal statements concern only connected simple cacti, not arbitrary graphs with overlapping cycles.

## Proof
**Cactus decomposition.** Removing any single edge from each simple cycle and retaining every bridge yields a spanning tree; conversely a spanning tree must retain every bridge and omit exactly one edge from each simple cycle. To see necessity, deleting at least one cycle edge is required for acyclicity; deleting two edges from one cycle disconnects the two resulting arcs because a cactus has no other path between those arcs avoiding that cycle. The block tree then forces the remaining choices independently. Thus every spanning tree corresponds bijectively to a choice of one omitted edge per cycle.

**Fourier factorization.** At a frequency \(x\), multiply the signs \(s_e=(-1)^{x_e}\) over every edge in each spanning tree. Bridges contribute \(\prod_{e\text{ bridge}}s_e\). In a cycle \(C\), omission of edge \(f\) contributes \(\prod_{e\in C,\,e\ne f}s_e=(\prod_{e\in C}s_e)s_f\). Summing independently over omitted edges gives the displayed transform, with no omitted factors.

**Rank, parity, and the spectral gap.** For a cycle of length \(\ell\), \(\sum_{e\in C}s_e=\ell-2k\), where \(k\) is the number of negative signs. It vanishes if and only if \(\ell\) is even and \(k=\ell/2\); exactly \({\ell\choose\ell/2}\) of the \(2^\ell\) signings do so. Multiplication of the independent per-cycle and bridge counts proves the rank. A signed sum of odd length has smallest absolute value one; a nonzero signed sum of even length has smallest absolute value two. All these minima can be attained independently. Every cycle has maximum signed-sum modulus \(\ell\), simultaneously attained at the zero character. Diagonalization of finite abelian convolution by Walsh characters proves the claimed invertibility, exact smallest nonzero modulus, inverse norm, and condition number.

**Endpoint projection norm.** The projection kernel at \(x\) is \(2^{-|E|}\widehat{1_{A_G}}(x)\). Every convolution row is a translate of this kernel, hence the sharp \(\ell^1\) and \(\ell^\infty\) operator norms are both its absolute row sum. Averaging the factorized absolute transform over independent uniformly random signs gives
\[
\|P_{A_G}\|=\prod_{j=1}^r 2^{-\ell_j}\sum_{k=0}^{\ell_j}{\ell_j\choose k}|\ell_j-2k|.
\]
The binomial identity obtained by splitting at \(k=\ell/2\) and telescoping \((\ell-2k){\ell\choose k}=\ell[{\ell-1\choose k}-{\ell-1\choose k-1}]\) is
\[
2^{-(2m+1)}\sum_{k=0}^{2m+1}{2m+1\choose k}|2m+1-2k|
=2^{-(2m+2)}\sum_{k=0}^{2m+2}{2m+2\choose k}|2m+2-2k|
=\alpha_m.
\]
This proves the exact endpoint formula including the parity plateau.

**Sharp extremal laws.** For each cycle set \(m_j=\lfloor(\ell_j-1)/2\rfloor\ge1\). Its use of vertices in the block tree is \(\ell_j-1\ge2m_j\). With \(b\) bridges, the cactus identity \(N-1=b+\sum_j(\ell_j-1)\) gives \(\sum_jm_j\le K\). A direct factorial calculation yields \(\alpha_1=3/2\) and
\[
\frac{\alpha_{m+1}}{\alpha_m}=\frac{2m+3}{2m+2}\quad(m\ge1).
\]
These ratios are greater than one and strictly decreasing, with every ratio strictly below \(3/2\). Therefore \(\alpha_m\le(3/2)^m\), equality if and only if \(m=1\). Combining with \(\sum m_j\le K\) proves the global sharp bound and its stated equality family by accounting for the total edge/vertex budget. For prescribed \(r\), strict increase requires \(\sum m_j=K\). If two effective lengths differ by at least two, moving one unit from the longer to the shorter strictly raises the product by the decreasing-ratio property. Hence precisely the balanced effective lengths \(a,a+1\) maximize the product. The spare vertex budget is zero for odd \(N\) and one for even \(N\), giving the exact equality descriptions.

## Verification
The standalone `check_cactus_fourier.py` independently enumerates spanning trees by cycle-free union-find tests, calculates complete Boolean Walsh transforms by a butterfly algorithm, and compares each coefficient with the product expression. It checks bridge and multi-cycle examples, operator ranks, the endpoint norm, and minimal positive spectral magnitude. It also exhaustively compares the sharp extremal bound against 5,739 integer cycle configurations up to 24 vertices and verifies the binomial plateau through cycle length 79. Run `python3 check_cactus_fourier.py`. An exact successful execution prints `CACTUS_FOURIER_ALL_EXACT_CHECKS_PASS`, plus 5,648 exact Fourier frequencies tested. The finite checks supplement, but do not replace, the all-dimensional proof.

## Relationship to prior work
The weighted matrix-tree theorem gives signed spanning-tree evaluations as weighted Laplacian cofactors, and the classical cactus block decomposition gives independent choices of omitted cycle edges. Zaslavsky's signed-graph matrix survey, Ghorbani's work on spanning-tree parity and graph eigenvalues, and Klee–Stamps' weighted tree enumeration establish related matrix and enumeration tools, but not the exact Walsh-convolution rank, Fourier-projection endpoint norm, or the optimal triangle-packing extremal law. A published result on real edge-Walsh projection constants for unicyclic graphs concerns projections **onto a linear span of edge coordinate characters**, not the Fourier projection **onto spanning-tree incidence frequencies** treated here; the former does not imply the latter. Other cactus transportation-space projection constants likewise act on a different Banach space. The factorization argument is elementary; novelty is claimed for this combined harmonic characterization and sharp extremal law, not for tree-block decomposition or binomial identities themselves.

## Limitations
The claims are restricted to connected simple cactus graphs and the specific edge-incidence spanning-tree frequency set. No assertion is made for arbitrary graphs with overlapping cycles, other graph classes, or nonbinary characters. The sharp extrema are among cacti on a fixed vertex count (and, in the refined statement, a fixed cycle count). Historical priority has not been exhaustively established, and independent mathematical validation has not been performed. The cited classical ingredients are not claimed as original.

## References
- E. Ghorbani, *Spanning trees and even integer eigenvalues of graphs*, arXiv:1201.3221, first submitted 16 January 2012. https://arxiv.org/abs/1201.3221
- T. Zaslavsky, *Matrices in the Theory of Signed Simple Graphs*, arXiv:1303.3083, first submitted 13 March 2013. https://arxiv.org/abs/1303.3083
- S. Klee and M. T. Stamps, *Linear algebraic techniques for weighted spanning tree enumeration*, arXiv:1903.03575, first submitted 27 February 2019. https://arxiv.org/abs/1903.03575
- published-finding corpus record `2026/10/18/SCOPE-an-exact-cycle-parity-law-for-walsh-projection-constants-of-unic--4465ca2f751a` (distinct edge-Walsh projection problem; available summary only).
- published-finding corpus record `2026/10/11/SCOPE-sharp-coordinate-projection-norms-for-edge-bases-of-cactus-trans--b98930fbc1cd` (distinct transportation-space coordinate projection; available summary only).
