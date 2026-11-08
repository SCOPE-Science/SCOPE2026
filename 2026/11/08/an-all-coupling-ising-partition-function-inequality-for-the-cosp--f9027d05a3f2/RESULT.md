# An all-coupling Ising partition-function inequality for the cospectral rook and Shrikhande graphs

## Finding
Let \(R=K_4\square K_4\) be the rook graph and \(S\) the Shrikhande graph, on the same vertex set \(V=(\mathbb Z/4\mathbb Z)^2\). Both have strongly regular parameters \((16,6,2,2)\) and adjacency eigenvalues \(6,2,-2\) of respective multiplicities \(1,6,9\). In spite of this cospectrality, their complete zero-field Ising partition functions admit the strict comparison
\[
\boxed{P_R(q)-P_S(q)=16q^{12}(q^2-1)^8(3q^4+2q^2+1)}.
\]
Here \(P_G(q)=\sum_{\sigma\in\{-1,+1\}^{V}}q^{c_G(\sigma)}\), and \(c_G(\sigma)\) is the number of edges whose endpoint spins disagree. Consequently, for every nonzero real \(K\),
\[
\boxed{Z_R(K)>Z_S(K)},\qquad
 Z_G(K)=\sum_\sigma\exp\!\left(K\sum_{uv\in E(G)}\sigma_u\sigma_v\right).
\]
At \(K=0\) there is equality. This holds for either sign of \(K\), ferromagnetic and antiferromagnetic.

The high-temperature even-subgraph expansion has identical coefficients through degree seven and differs first at degree eight by exactly \(96\). Both graphs have maximum cut \(32\), while the numbers of spin configurations achieving that cut are \(90\) for \(R\) and \(42\) for \(S\).

## Assumptions and scope
All statements concern **classical**, uniform-coupling, zero-external-field, finite sixteen-spin systems. Vertices are pairs \((x,y)\) with residues modulo four. Rook edges join distinct vertices sharing \(x\) or \(y\). Shrikhande edges join pairs whose difference lies in \(\{\pm(1,0),\pm(0,1),\pm(1,1)\}\); every unordered edge is counted once. The dimensionless coupling \(K\) may be any real number. The physical Hamiltonian convention is \(H_G=-J\sum_{uv\in E(G)}\sigma_u\sigma_v\), with \(K=\beta J\), where \(\beta>0\); hence either sign of \(J\) is included.

## Proof
**1. Exact cut enumerators by a finite identity.** Encode four horizontal rows by \(a_0,a_1,a_2,a_3\in\{0,\ldots,15\}\), and write \(a_j\in\{0,1\}\) for its bit at position \(j\) (the bit notation is local to the row). Define
\[
\begin{aligned}
 u(a)&=\sum_{j=0}^3 [a_j\ne a_{j+1\pmod 4}],\\
 v(a)&=\sum_{0\le j<k<4}[a_j\ne a_k],\\
 d(a,b)&=\sum_{j=0}^3\bigl([a_j\ne b_j]+[a_j\ne b_{j+1\pmod4}]\bigr),\\
 e(a,b)&=\sum_{j=0}^3[a_j\ne b_j].
\end{aligned}
\]
Square brackets are indicators. Directly from the edge definitions, the number of cut edges for the Shrikhande and rook graphs, respectively, is
\[
\begin{aligned}
 c_S(a_0,a_1,a_2,a_3)&=\sum_{i=0}^3u(a_i)+\sum_{i=0}^3d(a_i,a_{i+1\pmod4}),\\
 c_R(a_0,a_1,a_2,a_3)&=\sum_{i=0}^3v(a_i)+\sum_{0\le i<j<4}e(a_i,a_j).
\end{aligned}
\]
These equations are a 16-state-per-row finite arithmetic expression for every coefficient \(h_G(c)=[q^c]P_G(q)\). Evaluating their complete \(16^4=65{,}536\) terms using integer arithmetic yields the table below; coefficients at unlisted cut sizes vanish. It is a complete enumeration, not a sample.

| \(c\) | \(h_R(c)\) | \(h_S(c)\) |
|---:|---:|---:|
| 0 | 2 | 2 |
| 6 | 32 | 32 |
| 10 | 96 | 96 |
| 12 | 224 | 208 |
| 14 | 288 | 384 |
| 16 | 1428 | 1188 |
| 18 | 2624 | 3008 |
| 20 | 8064 | 7392 |
| 22 | 10464 | 11808 |
| 24 | 15632 | 13616 |
| 26 | 12384 | 14304 |
| 28 | 11424 | 10320 |
| 30 | 2784 | 3136 |
| 32 | 90 | 42 |

Both columns sum to \(2^{16}\). Subtracting columns gives the coefficient sequence, at exponents \(12,14,\ldots,32\),
\[
(16,-96,240,-384,672,-1344,2016,-1920,1104,-352,48),
\]
which, by direct multiplication, is exactly the displayed factored polynomial difference. Thus this is an exact integer proof of the polynomial identity.

**2. Strict Ising inequality.** Because each graph has 48 edges, \(\sum_{uv\in E(G)}\sigma_u\sigma_v=48-2c_G(\sigma)\), and therefore
\[
Z_G(K)=e^{48K}P_G(e^{-2K}).
\]
For any finite nonzero real \(K\), the substitution \(q=e^{-2K}\) satisfies \(q>0\) and \(q\ne1\). Each factor in \(16q^{12}(q^2-1)^8(3q^4+2q^2+1)\) is strictly positive. At \(K=0\), \(q=1\) and both partition functions equal \(2^{16}\). These are the full quantifiers and boundary cases for the inequality.

**3. First graph-sensitive high-temperature term.** Expanding every edge factor \(e^{K\sigma_u\sigma_v}=\cosh K\,(1+\sigma_u\sigma_v\tanh K)\) and summing over all spins yields
\[
Z_G(K)=2^{16}(\cosh K)^{48}\sum_{j=0}^{48}a_j(G)(\tanh K)^j,
\]
where \(a_j(G)\) counts edge subsets with exactly \(j\) edges and even degree at every vertex. The exact binomial transform from the cut table is
\[
a_j(G)=2^{-16}\sum_{c=0}^{48}h_G(c)
\sum_{\ell=\max(0,j-48+c)}^{\min(j,c)}
(-1)^\ell\binom c\ell\binom{48-c}{j-\ell}.
\]
For both graphs the coefficients for degrees \(0\) through \(7\) are \((1,0,0,32,60,288,1696,5568)\); degree eight gives \(a_8(R)=19602\) and \(a_8(S)=19506\), a first difference of \(96\). The expansion statement follows exactly, including the antiferromagnetic sign of \(\tanh K\), since degree eight is even.

**4. Antiferromagnetic ground states.** The last nonzero table row is \(c=32\). For positive \(J\) in the antiferromagnetic convention \(H_G^{\mathrm{AF}}=J\sum_{uv}\sigma_u\sigma_v\), the ground energy is \(J(48-2\cdot32)=-16J\), and exactly \(90\) rook configurations and \(42\) Shrikhande configurations attain it.

## Verification
Two standalone source programs are included. `verify_rowstates.py` implements the complete four-row algebraic sums just defined, checks the full polynomial factorization coefficient-by-coefficient and independently recomputes the even-subgraph coefficients using the displayed binomial transform. It prints `VERIFY_ROWS_OK row_patterns=65536 each factorization_exact=1 first_difference_order=8 coefficient=96`.

`verify_gray.cpp` constructs both graphs by their edge definitions, verifies all 16 degrees and common-neighbor counts, then visits all \(2^{16}\) configurations per graph using Gray-code incremental edge cuts. It checks every difference coefficient and the maximum-cut counts and prints `VERIFY_GRAY_OK configurations_per_graph=65536 maxcut=32`. Neither program relies on a previous numerical result or any unavailable data file. To replay in a directory containing the two included source files:

```sh
python3 verify_rowstates.py
c++ -std=c++17 -O2 verify_gray.cpp -o verify_gray
./verify_gray
```

## Relationship to prior work
Wu and Hu (arXiv:cond-mat/0204217, first public 2002-04-10), in their complete article (not just its abstract), give exact partition functions for finite periodic square and plane-triangular lattice Ising models. Their triangular-torus model specializes to the Shrikhande-side graph, so computing that individual partition function in principle is **not** the novelty claimed here. Their article does not formulate the rook-versus-Shrikhande comparison, the factored difference, its strictly positive sign for both signs of coupling, or the first discrepancy at high-temperature order eight. Mosseri (arXiv:1409.0147) gives a broad Hadamard framework for arbitrary-graph Ising spectra and partition functions, which applies to both graphs but likewise is not the displayed comparison identity. The graph catalogue identifies the cospectral strongly regular pair and its common spectral parameters, not an Ising equality. The proposed contribution is exactly the comparison identity and its consequences, not a new general partition-function algorithm or an individual triangular-lattice solution.

## Limitations
The theorem is an exact finite-graph statement, not a thermodynamic-limit phase transition, a nonzero-field result, a quenched-disorder result or an efficient calculation for larger graph families. Its proof uses a complete exact finite enumeration rather than a conceptual graph-theoretic closed-form construction of the cut polynomials. Although primary sources and related mathematical records have been compared, an equivalent identity in unindexed Tutte-polynomial, coding-theory, or Ising-enumerator tables cannot be categorically excluded. No independent scientific audit has been performed.

## References
1. M.-C. Wu and C.-K. Hu, *Exact partition functions of the Ising model on M×N planar lattices with periodic-aperiodic boundary conditions*, arXiv:cond-mat/0204217 (first public 2002-04-10), https://arxiv.org/abs/cond-mat/0204217 . In particular, the full preprint, sections 1–3 and equation (1).
2. R. Mosseri, *Ising-like models on arbitrary graphs: the Hadamard way*, arXiv:1409.0147 (first public 2014-08-30), https://arxiv.org/abs/1409.0147 ; *Phys. Rev. E* **91**, 012142 (2015). Complete author-posted manuscript, sections II–V and appendices.
3. A. E. Brouwer, *Shrikhande* graph catalogue, https://jaanos.github.io/tables/graphs/Shrikhande.html (graph parameters, spectral data and relationship to the rook graph).
