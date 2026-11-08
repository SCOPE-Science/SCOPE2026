# Four-state ladder character-degree transfer over finite fields

## Finding

Let \(q\) be any prime power, \(n\ge3\), and \(L_n=P_n\mathbin{\square}K_2\) the ladder graph with \(2n\) vertices and \(3n-2\) edges. For a labeling \(w\in\mathbb F_q^{E(L_n)}\), let \(B(w)\) be the alternating weighted adjacency matrix. Write
\[
A_{n,q}(z)=\sum_w z^{n-\operatorname{rank}(B(w))/2}.
\]
Define a row vector \(u\), a matrix \(M\), and a column vector \(v\) over \(\mathbb Z[q,z]\) by
\[
u=(0,\ q-1,\ q(q-1),\ z),
\]
\[
M=\begin{pmatrix}
q^2(q-1)&0&q^2z&0\\
q(q-1)&0&q^2(q-1)+qz&0\\
0&q(q-1)&q^2(q-1)&qz\\
0&q-1&q(q-1)&q^2(q-1)+z
\end{pmatrix},
\]
\[
v=\begin{pmatrix}q^2z\\q^2-q+qz\\q^2-q+qz\\q^2-1+z\end{pmatrix}.
\]
**Theorem.** For every prime power \(q\) and every integer \(n\ge3\),
\[
\boxed{A_{n,q}(z)=uM^{n-2}v.}
\]
Every coefficient \([z^j]A_{n,q}(z)\) counts precisely the edge labelings whose alternating rank is \(2(n-j)\); thus all such counts are polynomials in the field size. For odd \(q\), the graphical class-two group \(G_{L_n}(\mathbb F_q)\) has exactly
\[
\boxed{\operatorname{ch}(L_n,r;q)=q^{2n-2r}[z^{n-r}]uM^{n-2}v}
\]
ordinary irreducible complex characters of degree \(q^r\), for every \(0\le r\le n\). For all other degrees, the multiplicity is zero. These statements also hold algebraically for the boundary case \(n=2\), where the graph is a single four-cycle; this already simpler case is not part of the new contribution.

## Assumptions and scope

The ladder \(L_n\) has vertex set \(\{a_i,b_i:1\le i\le n\}\), rung edges \(a_ib_i\), and rail edges \(a_ia_{i+1},b_ib_{i+1}\). Its edge labels are arbitrary, including zero; no field-characteristic restriction is imposed on the alternating-rank theorem. The group-character statement requires odd characteristic. The graphical group may be defined on \(V\oplus Z\), with \(V=\mathbb F_q^{2n}\), \(Z=\mathbb F_q^{3n-2}\), and product \((x,c)(y,d)=(x+y,c+d+\tfrac12[x,y])\), the bracket having independent central basis vectors for the graph edges.

The transfer states are ordered \(0,H,X,F\), where \(0\) means the zero subspace of \(\mathbb F_q^2\), \(H=\langle(1,0)\rangle\), \(X\) combines the vertical line \(\langle(0,1)\rangle\) and every non-coordinate line, and \(F=\mathbb F_q^2\). The aggregation into \(X\) is legitimate because those lines have identical total transition weights to each of these four state classes.

## Proof

**Step 1: bipartite reduction.** Color \(a_i\) and \(b_i\) by opposite parities according to \(i\); after ordering the two color classes, the alternating adjacency matrix is congruent via a permutation to
\[
\begin{pmatrix}0&T\\-T^{\mathsf T}&0\end{pmatrix},
\]
where \(T\) is an arbitrary \(n\)-by-\(n\) tridiagonal matrix. The diagonal entries correspond to rungs, and its upper and lower diagonals to the two rails. Every free matrix entry is an independently labeled edge, giving a bijection between the \(q^{3n-2}\) edge labelings and all such tridiagonal matrices. Hence \(\operatorname{rank}B=2\operatorname{rank}T\) and \(A_{n,q}(z)=\sum_Tz^{\dim\ker T}\).

**Step 2: boundary propagation.** Write the equations \(T x=0\) as
\[
\alpha_i x_{i-1}+\beta_i x_i+\gamma_i x_{i+1}=0
\quad(1\le i\le n),
\]
with \(x_0=0\), \(\alpha_1=0\), \(\gamma_n=0\), and independent free coefficients in all positions not forced to zero. Introduce a free dummy variable \(x_{n+1}\). Immediately before imposing row \(i\), let \(K_i\subseteq\mathbb F_q^i\) be the solution space of rows \(1,\ldots,i-1\); its last-coordinate-pair image is \(S_i\subseteq\mathbb F_q^2\). For \(i=1\), use the pair \((x_0,x_1)=(0,x_1)\) and \(S_1=\langle(0,1)\rangle\).

When row \(i\) is imposed after adjoining the free variable \(x_{i+1}\), let \(\epsilon_i\in\{0,1\}\) be the rank of the linear functional \((u,v,w)\mapsto \alpha_i u+\beta_i v+\gamma_iw\) on \(S_i\times\mathbb F_q\). Then
\[
\dim K_{i+1}-\dim K_i=1-\epsilon_i.
\]
The next boundary image is precisely
\[
S_{i+1}=\{(v,w):\exists u\text{ with }(u,v)\in S_i,\ \alpha_iu+\beta_iv+\gamma_iw=0\}.
\]
Since \(\gamma_n=0\), the final dummy variable is independent, and \(\dim K_{n+1}=\dim\ker T+1\). As \(\dim K_1=1\), the monomial weight \(\prod_{i=1}^nz^{1-\epsilon_i}\) is exactly \(z^{\dim\ker T}\).

**Step 3: transition enumeration.** For interior rows all three coefficients range over \(\mathbb F_q\). Distinguish the five actual types \(0,H,V,O,F\), with \(V=\langle(0,1)\rangle\) and \(O=\langle(1,\lambda)\rangle\), \(\lambda\ne0\). States \(V\) and \(O\) have identical outgoing class-weight totals: replacing \(\alpha_i+\lambda\beta_i\) by a uniformly distributed coefficient reduces their equations to the same two-variable case. Their transitions to \(H,V,O,F\) have weights \(q(q-1),q(q-1),q(q-1)^2,qz\), respectively.

For \(S_i=0\), the only possibilities are \(S_{i+1}=0\) if \(\gamma_i\ne0\) (weight \(q^2(q-1)\)) and \(S_{i+1}=V\) if \(\gamma_i=0\) (weight \(q^2z\)). For \(S_i=H\), the equation is \(\alpha_iu+\gamma_iw=0\): when \(\alpha_i=0,\gamma_i\ne0\), the new image is \(0\), with weight \(q(q-1)\); otherwise it is \(V\), with combined weight \(q^2(q-1)+qz\). For \(S_i=F\), when \(\alpha_i\ne0\) the new image is \(F\), giving \(q^2(q-1)\) choices; if \(\alpha_i=0,\beta_i=\gamma_i=0\), it is \(F\) with weight \(z\); otherwise it is the line \(\beta_iv+\gamma_iw=0\), with \(q-1\) choices for \(H\), \(q-1\) for \(V\), and \((q-1)^2\) for \(O\). Aggregating \(V,O\) into \(X\) yields exactly the displayed \(4\)-by-\(4\) transition matrix \(M\).

For the first row, \(\alpha_1=0\) and the pair \((x_1,x_2)\) lies in the kernel of \(\beta_1x_1+\gamma_1x_2\); these \(q^2\) possibilities give weights \(q-1\) for \(H\), \(q(q-1)\) for \(X\), and \(z\) for \(F\), namely \(u\). For the terminal row, \(\gamma_n=0\), so if \(S_n\) has dimension \(s\) there are \(q^{2-s}\) pairs \((\alpha_n,\beta_n)\) that vanish on it (weight \(z\)) and \(q^2-q^{2-s}\) others (weight \(1\)). Thus the terminal weights are \(q^{2-s}z+q^2-q^{2-s}\) for \(s=0,1,1,2\), giving \(v\). There are precisely \(n-2\) interior rows, proving the first displayed boxed formula.

**Step 4: character multiplicities.** For odd \(q\), fix a central character of \(G_{L_n}(\mathbb F_q)\), equivalently a functional \(\lambda\in Z^*\). Its commutator pairing on \(V\) is \(B(\lambda)\). If its alternating rank is \(2r\), its radical has size \(q^{2n-2r}\). The corresponding twisted complex group algebra has \(q^{2n-2r}\) simple blocks, each a full matrix algebra of degree \(q^r\). Indeed, its center has one dimension for each radical element and its total dimension is \(q^{2n}\), while all simple degrees are \(q^r\) by the nondegenerate alternating quotient. Summing over all \(\lambda\) of rank \(2r\) gives the second boxed formula.

## Verification

Running `python3 checks/verify_ladder.py` independently constructs all tridiagonal matrices over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\) in the packaged test sizes and computes ranks by Gaussian elimination. In a separate test it constructs the actual \(2n\)-by-\(2n\) skew adjacency matrices directly from ladder edges. The complete log is `checks/verification_output.txt`, with last line `LADDER_CHARACTER_RANK_TRANSFER_PASS`. Samples include the nullity populations \((32,74,21,1)\) for \(n=3,q=2\), \((1080,1020,86,1)\) for \(n=3,q=3\), and \((176,544,270,33,1)\) for \(n=4,q=2\). Every tested entry matches the transfer. The separate character degree-square checksum equals \(q^{5n-2}\) for the tested odd fields.

For all \(n\), the total number of labelings is \(A_{n,q}(1)=q^{3n-2}\). The constant coefficient of \(A_{n,q}\), counting nonsingular tridiagonal matrices, agrees with the two-step recurrence \(a_n=q^2(q-1)a_{n-1}+q^3(q-1)^2a_{n-2}\), whose evaluation was independently checked for sample prime powers and dimensions through \(n=15\). This nonsingular specialization was already known and is not part of the claimed novelty.

## Relationship to prior work

The graphical Lie-algebra construction and isomorphism theory are established in Mainkar's 2010 preprint. Lewis–Liu–Morales–Panova–Sam–Zhang (2010 preprint, 2011 publication) introduce rank enumeration with arbitrary support restrictions but do not supply a ladder-specific rank polynomial or the four-state transfer. Rossmann (2022, Section 1.6, Question 1.10) explicitly poses enumeration of ordinary irreducible characters by degree for graphical groups and reduces it to alternating weighted adjacency ranks. His known family results include paths, rather than the ladder family considered here. Jitman–Sricharoen (2024, Section 3, Theorems 3.1–3.4) fully enumerate tridiagonal matrices by determinant, determining the full-rank coefficient, not the entire lower-rank distribution. This theorem gives that missing rank refinement and, via the graph correspondence, every ladder character-degree multiplicity.

For \(n\ge3\), ladder graphs are not trees, single cycles, cones, or vertex-bouquets of cycles. Their rank spectrum is not implied by the tree, cycle, cone, or rooted-vertex-amalgamation formulas by a direct specialization. The lower-dimensional \(n=2\) cycle case, and the full-rank coefficient, are explicitly treated as established boundary information.

## Limitations

The character statement is restricted to odd characteristic. The rank transfer counts labeled edge weights, not automorphism orbits; it does not enumerate individual conjugacy classes, higher-width strip graphs, or the scheme structures of rank loci. The four-state method does not assert a classification of all sparse-matrix patterns. Historical-priority search is necessarily nonexhaustive; an unidentified general pathwidth or zero-pattern rank-transfer theorem may imply the result. Independent mathematical audit has not been performed.

## References

- Meera G. Mainkar, *A short note on 2-step nilpotent Lie algebras associated with graphs*, arXiv:1010.4005 (first public preprint 2010-10-19). https://arxiv.org/abs/1010.4005
- J. B. Lewis, R. I. Liu, A. H. Morales, G. Panova, S. V. Sam, Y. X Zhang, *Matrices with restricted entries and \(q\)-analogues of permutations*, arXiv:1011.4539 (first public preprint 2010-11-20). https://arxiv.org/abs/1011.4539
- Tobias Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, *Bull. Lond. Math. Soc.* 54 (2022), 1923–1943, doi:10.1112/blms.12665. https://doi.org/10.1112/blms.12665
- Somphong Jitman and Yosita Sricharoen, *Determinants of tridiagonal matrices over some commutative finite chain rings*, *Special Matrices* 12 (2024), article 20230114, doi:10.1515/spma-2023-0114. https://doi.org/10.1515/spma-2023-0114
