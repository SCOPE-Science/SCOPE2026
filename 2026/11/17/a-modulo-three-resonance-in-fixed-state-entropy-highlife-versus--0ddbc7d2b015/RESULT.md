# A modulo-three resonance in fixed-state entropy: HighLife versus Life

## Finding

Let \(H_n\) and \(L_n\) count the labelled fixed configurations, respectively, of the synchronous HighLife rule B36/S23 and Conway Life B3/S23 on the Moore-neighborhood torus \(\mathbb Z_3\times\mathbb Z_n\), for each integer \(n\ge3\). No spatial rotations or reflections are identified.

Define the two integer polynomials
\[
\begin{aligned}
p_H(z)&=z^{10}-z^9-15z^7+6z^6-9z^5+72z^4-63z^3-162z+162,\\
p_L(z)&=z^{10}-z^9-z^8-14z^7+6z^6+63z^4-63z^3-81z+243.
\end{aligned}
\]
Let \(R_H\) and \(R_L\) be their multisets of ten complex roots, counted with algebraic multiplicities. Then, for every \(n\ge3\),
\[
\begin{aligned}
H_n&=3^{n+1}\mathbf1_{3\mid n}+\sum_{\alpha\in R_H}\alpha^n,\\
L_n&=3^{n+1}\mathbf1_{3\mid n}+\sum_{\beta\in R_L}\beta^n.
\end{aligned}
\]

The respective positive dominant roots \(\rho_H,\rho_L\) satisfy rigorously
\[
2.65923<\rho_H<2.65924<2.70363<\rho_L<2.70364<3.
\]
Consequently, despite the inclusion of every HighLife fixed configuration among the Life fixed configurations,
\[
\lim_{k\to\infty}\frac{H_{3k}}{L_{3k}}=1,
\qquad
\lim_{k\to\infty}\frac{H_{3k+r}}{L_{3k+r}}=0\quad(r=1,2),
\]
and more precisely \(H_n/L_n\sim(\rho_H/\rho_L)^n\) along either nonzero residue class modulo three. The absolute difference still grows as \(L_n-H_n\sim\rho_L^n\) along every sequence of integers \(n\to\infty\).

## Assumptions and scope

Rows and columns are indexed modulo three and modulo \(n\), respectively. Every site has eight distinct Moore neighbors when \(n\ge3\), including the case \(n=3\). Both rules retain a live cell precisely with two or three live neighbors. Life births a dead cell at exactly three live neighbors; HighLife births at exactly three or six. A fixed configuration is an entire binary configuration unchanged by one synchronous update. All sites are distinguished, and configurations are not divided by translation, rotation, reflection, or complementation.

## Proof

Encode each column by a three-bit integer \(b\in\{0,\ldots,7\}\), with \(|b|\) its number of one-bits and \(b_r\) its bit in row \(r\). For three successive columns \(a,b,c\), the live-neighbor count at the central site's row \(r\) is exactly
\[
N_r(a,b,c)=|a|+|b|+|c|-b_r.
\]
Construct the finite directed graph \(G_Q\) with sixty-four vertices \((a,b)\) and an edge \((a,b)\to(b,c)\) exactly when all three central sites remain unchanged under rule \(Q\). Equivalently, for every row \(r\), require \(N_r\in\{2,3\}\) when \(b_r=1\), and \(N_r\notin B_Q\) when \(b_r=0\), where \(B_H=\{3,6\}\) and \(B_L=\{3\}\). A cyclic sequence of \(n\) columns gives a unique length-\(n\) closed walk in this graph, including sequences with shorter spatial period. Therefore the labelled fixed-state count equals \(\operatorname{tr}(A_Q^n)\), with \(A_Q\) the zero-one adjacency matrix.

Enumerating all \(8^3=512\) column triples by those explicitly stated Boolean conditions yields \(155\) edges for HighLife and \(156\) for Life. Their cyclic strongly connected components have exactly the same vertex sets, of sizes \(30\) and \(27\); seven other vertices do not lie on any directed cycle. The two rules differ only by the edge \((7,0)\to(0,7)\), which is allowed by Life but not HighLife, because an empty central column between two full columns has six live neighbors at every site. Both size-thirty components contain the loop \((0,0)\to(0,0)\) and are strongly connected, hence their adjacency matrices \(B_H,B_L\) are primitive nonnegative matrices.

The common size-twenty-seven component consists of adjacent column pairs whose weights belong to \(\{(1,1),(1,2),(2,1)\}\). A cyclic configuration in this component has column-weight pattern \(1,1,2\) repeated (up to one of three phases), with each individual column having three independent mask choices. All three-column windows have total weight four, so each live site has three live neighbors and each dead site has four, making these configurations fixed under both rules. Thus this component contributes exactly \(3^{n+1}\mathbf1_{3\mid n}\) closed walks. Its exact characteristic polynomial is \(z^{24}(z^3-27)\).

The size-thirty adjacency matrices have characteristic polynomials \(z^{20}p_H(z)\) and \(z^{20}p_L(z)\), respectively. This assertion is a finite exact-integer calculation: enumerate the stated \(512\) triples, find their strongly connected components and use Newton identities on the first thirty traces to obtain every characteristic coefficient. Complete executable source is supplied in `transfer_check.py`; it requires only the Python standard library and tests the coefficients against their displayed values. Adding the traces of the two cyclic components proves both exact formulas for every \(n\), with no extrapolation from a finite range of circumferences.

By primitivity, the size-thirty components have positive simple Perron eigenvalues and all their other eigenvalues have strictly smaller modulus. The directed graph inclusion is strict on this same strongly connected vertex set, so Perron-Frobenius strict monotonicity gives \(\rho_H<\rho_L\). For each component, take \(v=B^{50}\mathbf1\), a strictly positive integer vector, and verify the exact componentwise bounds \(265923v<100000B_Hv<265924v\) and \(270363v<100000B_Lv<270364v\), respectively. The Collatz-Wielandt inequalities give the stated rational spectral intervals without reliance on floating-point eigenvalue computation.

The common twenty-seven-vertex contribution dominates along multiples of three because \(\rho_L<3\). Along the other two residue classes it vanishes identically; Perron-Frobenius asymptotics give \(H_n\sim\rho_H^n\) and \(L_n\sim\rho_L^n\). On every residue class, subtracting the common contribution gives \(L_n-H_n\sim\rho_L^n\). These observations establish all limits.

## Verification

Two independently structured reproducibility programs accompany the result. `transfer_check.py` enumerates column triples, computes cyclic strongly connected components, verifies exact characteristic polynomials by Newton identities, and proves rational Perron bounds with positive integer vectors. Run it with `python3 transfer_check.py`. `direct_check.cpp` independently evolves all \(2^{3n}\) labelled configurations for each \(3\le n\le7\) and counts fixed configurations under both actual update rules. Compile using `g++ -O3 -std=c++17 direct_check.cpp -o direct_check` and execute `./direct_check`. Both programs were executed from the supplied standalone source files; their recorded stdout is included as text outputs.

Selected exact counts are \((H_n,L_n)=(127,127),(37,39),(91,121),(2539,2595),(1009,1177)\) at circumferences \(n=3,4,5,6,7\), respectively. The transfer certificate also computes all counts through \(n=15\). Independent direct enumeration confirms, but is not the all-circumference proof; that proof rests on the complete finite graph and exact spectra.

## Relationship to prior work

HighLife and its extra six-neighbor birth, replicators, and classical still-life examples were described by David I. Bell in 1994 and surveyed in Eppstein's 2009 preprint. The author-hosted Bell archive was located but its compressed full text could not be retrieved in this inspection. Eppstein's full open preprint discusses the distinction between the two update rules and engineered patterns, not a transfer-matrix enumeration on periodic three-row strips. McIntosh's *Life's Still Lifes* applies de Bruijn methods to Conway Life; accessible bibliographic descriptions do not establish a HighLife comparison. The Conway Life three-row fixed-state spectrum and its divisibility-by-three phase are already established comparison data and are not claimed as separately new. The transfer method and inclusion of HighLife still lifes among Life still lifes are established principles. The contribution here is the exact HighLife spectrum and its newly established contrast with the known Life spectrum, including an arithmetic separation caused by a single deleted transition.

## Limitations

The result concerns fixed configurations only, not transient basins or nontrivial temporal periods; the width is exactly three, and narrow-strip periodic boundary conditions must not be confused with fixed finite patches in the infinite plane. The two dominant-root intervals are rigorous, but the simple-decimal approximations do not themselves prove the theorem. Historical priority remains uncertain for older unindexed catalogues and for the full Bell archive and McIntosh chapter, neither of which was available for complete full-text comparison. The reproducibility checks are computational self-checks rather than independent external mathematical validation.

## References

- D. I. Bell, *HighLife — An Interesting Variant of Life* (original 1994 public discussion, May 7 Usenet posting), author-hosted archive listed at https://www.tip.net.au/~dbell/ ; full compressed text not inspected.
- D. Eppstein, *Growth and Decay in Life-Like Cellular Automata*, first arXiv posting November 15, 2009, https://arxiv.org/abs/0911.2890 ; readable complete manuscript at https://ar5iv.labs.arxiv.org/html/0911.2890 .
- D. Eppstein, *Replicators: B36/S23 (HighLife)*, https://ics.uci.edu/~eppstein/ca/replicators/b36s23.html .
- H. V. McIntosh, *Life's Still Lifes*, in *Game of Life Cellular Automata* (2010), pp. 35–50; bibliographic record at https://dblp.org/rec/books/daglib/p/McIntosh10a ; full chapter not inspected.
