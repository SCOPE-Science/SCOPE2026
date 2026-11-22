# A power-of-two classification of majority equilibria on square rook graphs

## Finding
For every integer \(n\ge2\), let \(R_n=K_n\square K_n\) be the square rook graph, with one vertex at each cell of an \(n\)-by-\(n\) board and an edge between distinct cells in the same row or column. Under synchronous binary majority of the *open* neighborhood, with incumbent-state retention upon a tie, **all fixed configurations are Ferrers matrices up to independent permutations of rows and columns**. The exact number of fixed-configuration equivalence classes under \(S_n\times S_n\), acting by independent row and column permutations, is
\[
\boxed{U_n=2^n.}
\]
The equivalence group does **not** include exchanging the row and column coordinates; the larger full graph automorphism group is not being counted here.

The assertion admits a complete structural and labelled enumeration. Let \(\lambda=(\lambda_1,\ldots,\lambda_n)\) be a weakly decreasing sequence of integers satisfying \(n\ge\lambda_1\ge\cdots\ge\lambda_n\ge0\). Let \(m_r(\lambda)\) count the rows of length \(r\), and let \(\lambda'\) denote the conjugate partition, padded with zeroes to \(n\) entries. Define \(\mathcal F_n\) as the set of such partitions satisfying the majority corner inequalities below. The number of labelled fixed configurations is exactly
\[
\boxed{N_n=(n!)^2\sum_{\lambda\in\mathcal F_n}
\frac{1}{\displaystyle\prod_{r=0}^{n}m_r(\lambda)!\prod_{s=0}^{n}m_s(\lambda')!}.}
\]
The values of \(N_n\) for \(n=2,3,4,5,6,7,8,9,10\) are respectively \(6,32,302,4512,97248,2851858,109223374,5294338160,316828964816\). The value \(302\) at order four was previously determined in a finite rook-graph census and is not claimed as new.

## Assumptions and scope
There are no loops. An update of cell \((i,j)\) uses the \(2n-2\) other cells in the same row or column. A strict majority replaces its bit; if exactly \(n-1\) neighbors have bit one, the incumbent bit remains. Every row and column position is labelled. A *fixed configuration* satisfies \(F_n(x)=x\) at time zero. No assertion about two-cycles or transient durations is made.

A Ferrers matrix of shape \(\lambda\) has bit one at \((i,j)\) exactly when \(1\le j\le\lambda_i\). For \(1\le\ell\le n-1\), set \(a_\ell=\#\{i:\lambda_i>\ell\}\) and \(b_\ell=\#\{i:\lambda_i=\ell\}\). The necessary and sufficient conditions defining \(\lambda\in\mathcal F_n\) are, for **each** positive proper row length \(\ell\) that actually occurs,
\[
\ell+a_\ell\le n-1,
\qquad
\ell+a_\ell+b_\ell\ge n+1.
\]
The boundary lengths zero and \(n\) impose no further conditions.

## Proof
**1. Row/column majority inequalities.** Write \(r_i=\sum_jx_{ij}\) and \(c_j=\sum_ix_{ij}\). The number of one-neighbors of cell \((i,j)\) is \(r_i+c_j-2x_{ij}\). Because the degree equals \(2n-2\), the fixed-state condition is exactly
\[
 x_{ij}=1\implies r_i+c_j\ge n+1,
 \qquad x_{ij}=0\implies r_i+c_j\le n-1.
\]
Indeed, a one persists if its one-neighbor count is at least \(n-1\), whereas a zero persists if its one-neighbor count is at most \(n-1\). These two implications cover both strict votes and ties.

**2. Nested supports and Ferrers rigidity.** If rows \(i,k\) have \(r_i\ge r_k\), it is impossible to have \(x_{ij}=0\) and \(x_{kj}=1\) in any column \(j\): the first cell gives \(r_i+c_j\le n-1\), the second gives \(r_k+c_j\ge n+1\), contradicting \(r_i\ge r_k\). Therefore row-one supports are nested in decreasing row-degree order. Rows of equal degree have identical supports, and the columns can then be arranged by their sums so that the matrix is the unique Ferrers form of a partition \(\lambda\). Conversely every independent-row/column orbit has exactly one Ferrers form, since its sorted row-length partition uniquely specifies all Ferrers entries.

**3. Corner test.** In the rows with proper positive length \(\ell\), the rightmost one is in column \(\ell\), with column sum \(a_\ell+b_\ell\); the leftmost zero is in column \(\ell+1\), with column sum \(a_\ell\). The implications in step 1 require respectively \(\ell+a_\ell+b_\ell\ge n+1\) and \(\ell+a_\ell\le n-1\). These suffice for the entire row because column sums decrease from left to right. Every all-one row has \(r_i=n\) and at least one one-neighbor sum \(n-1\); every all-zero row has \(r_i=0\) and at most \(n-1\) one-neighbors. Thus these boundary rows always remain fixed. The displayed corner test is necessary and sufficient.

**4. A two-to-one extension recursion.** Denote the stable Ferrers shapes by \(\mathcal F_n\), including the trivial \(\mathcal F_1=\{(0),(1)\}\). For \(\mu\in\mathcal F_{n-1}\), define the length-\(n\) shape
\[
 E(\mu)=(e(\mu_1),\ldots,e(\mu_{n-1}),0),
 \qquad e(t)=\begin{cases}t+1,&t>0,\\0,&t=0.\end{cases}
\]
For each proper positive length \(t\) of \(\mu\), the extension changes \(t\) to \(t+1\), increases the board order by one, and keeps both group counts \(a_t,b_t\) unchanged. Hence the two corner inequalities remain identical. An old full row becomes a new full row. It follows that \(E(\mu)\in\mathcal F_n\), and its final row is zero.

Conversely, suppose \(\lambda\in\mathcal F_n\) has a zero last row. No length-one row can occur: such a row would require \(1+a_1+b_1\ge n+1\), but a zero row implies \(a_1+b_1\le n-1\), a contradiction. Delete one last zero and replace each remaining positive length \(t\) with \(t-1\). The result is a valid partition of order \(n-1\), because the corner inequalities are the same after reversing the above simultaneous shifts; full rows and zero rows remain boundary cases. Thus \(E\) is a bijection from \(\mathcal F_{n-1}\) onto those elements of \(\mathcal F_n\) with a zero last row.

Define \(C(\lambda)=(n-\lambda_n,\ldots,n-\lambda_1)\), the Ferrers shape after exchanging zeros and ones and reordering rows, and let \(\lambda'\) mean transpose. Complementing a binary configuration preserves the majority rule with incumbent tie retention, and transposing the board is a graph automorphism; both operations preserve fixed configurations. Therefore \(J(\lambda)=(C(\lambda))'\) maps \(\mathcal F_n\) bijectively to itself. It is an involution, since complement and transposition commute as operations on the Ferrers diagrams of an \(n\)-square. Its last row is positive exactly when the complement shape \(C(\lambda)\) has a row of length \(n\), which is equivalent to \(\lambda_n=0\). Thus \(J\) bijects the zero-last-row and positive-last-row halves of \(\mathcal F_n\). Consequently \(|\mathcal F_n|=2|\mathcal F_{n-1}|\), and with the base \(|\mathcal F_1|=2\) we obtain \(|\mathcal F_n|=2^n\).

**5. Labelled orbit sizes.** A Ferrers shape has \(m_r(\lambda)\) indistinguishable rows of each length \(r\), and \(m_s(\lambda')\) indistinguishable columns of each height \(s\). Any row or column permutation stabilizing the matrix must preserve these equal-support groups, and any permutation within each such group does stabilize it. The stabilizer in \(S_n\times S_n\) therefore has order \(\prod_rm_r(\lambda)!\prod_sm_s(\lambda')!\). Orbit-stabilizer gives precisely the displayed labelled count \(N_n\); distinct Ferrers shapes give disjoint labelled orbits.

## Verification
The standalone Python 3 program `code/verify_rook.py` implements the extension and involution independently from the local-neighbor update and checks every generated shape for the exact corner inequalities. It enumerates all Ferrers partitions independently for \(n\le8\) and confirms that its stable set matches the recursively generated set. It also calculates the orbit-stabilizer labelled sums for all \(n\le10\). Separately it directly updates every one of the \(16+512+65,536=66,064\) bit matrices for \(n=2,3,4\), without relying on row/column-sum update formulas, and verifies the Ferrers-and-shape characterization and counts exactly. A further 20,000 seeded random configurations at \(n=5\) also agree; these nonexhaustive tests are not used as proof of the all-size theorem. Run from the extracted package root: `python3 code/verify_rook.py`. Its recorded outputs appear in `outputs/verification.json`.

## Relationship to prior work
The Goles–Olivos result on generalized threshold dynamics establishes eventual period at most two but does not enumerate fixed configurations. Benjamini et al. (2014, arXiv:1405.2486) study majority dynamics on broader graph classes without a Ferrers classification or square-rook orbit count. A previously published exact comparison of the Shrikhande and \(4\times4\) rook graph reports \(302\) fixed states for the rook graph, consistent with this result but restricted to that one order. The published three-row rook-graph majority analysis concerns \(K_3\square K_n\), not the all-size diagonal family \(K_n\square K_n\). The terminology *two-color majority C-coloring* gives an equivalent fixed-point formulation: the 2026 paper on majority C-colorings of Cartesian products determines the **maximum number of colors**, rather than the enumeration of all binary majority-fixed configurations. Its same-object coverage is acknowledged but does not imply the \(2^n\) class census or the Ferrers structural theorem.

## Limitations
The count \(2^n\) uses independent row/column symmetry \(S_n\times S_n\); it is not the count modulo the larger group that also transposes the board, and it is not the labelled count. The theorem applies only to the binary strict-majority-with-tie-retention fixed states of square rook graphs, not rectangular boards, other tie conventions, oscillatory attractors, or attraction basins. Although the proof is self-contained and the computations were reproduced, no independent mathematical audit has been performed. Accessible source inspections and searches do not rule out an unindexed equivalent enumeration or a stronger general theorem.

## References
1. E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* 30 (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, “Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs,” arXiv:1405.2486, first submitted 2014-05-11. https://arxiv.org/abs/1405.2486
3. “Binary majority clocks distinguish the Shrikhande and rook graphs,” published mathematical result, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-binary-majority-clocks-distinguish-the-shrikhande-and-rook-graph--de29d0d819a4
4. “Sharp parity-dependent majority relaxation on three-row rook graphs,” published mathematical result, 2026-11-01. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-parity-dependent-majority-relaxation-on-three-row-rook-gra--3349c8eefe09
5. C. Bujtás, M. Dettlaff, H. Furmańczyk, A. Laskowska and Z. Tuza, “Majority C-coloring in Cartesian products,” arXiv:2608.27669, first submitted 2026-08-27. https://arxiv.org/abs/2608.27669
