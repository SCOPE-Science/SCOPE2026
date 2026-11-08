# Complete three-color Potts field diagram on the truncated tetrahedron

## Finding
Place three labeled colors \(\{0,1,2\}\) on the twelve vertices of the truncated-tetrahedral graph \(T\), with antiferromagnetic coupling \(J>0\) and a real color-selective field \(h\) favoring color zero. Write \(x=h/J\), \(k(\sigma)=|\{v:\sigma_v=0\}|\), and \(e(\sigma)=|\{uv\in E(T):\sigma_u=\sigma_v\}|\). Then
\[
\mathcal H_{J,h}(\sigma)/J=e(\sigma)-xk(\sigma),
\qquad
E_0(h)/J=\min\{4,-4x,2-6x,6-8x,18-12x\}.
\]
The **only** critical fields are \(h/J=-1,1,2,3\). The open-field ground-state color-zero populations \(k\) and degeneracies \(g\), respectively, are

| Field range | \(k\) | \(g\) |
|---|---:|---:|
| \(x<-1\) | 0 | 24 |
| \(-1<x<1\) | 4 | 120 |
| \(1<x<2\) | 6 | 384 |
| \(2<x<3\) | 8 | 480 |
| \(x>3\) | 12 | 1 |

At critical fields \(x=-1,1,2,3\), the complete lists of ground-state populations and total degeneracies are, respectively, \((\{0,1,2,3,4\},1320)\), \((\{4,5,6\},984)\), \((\{6,7,8\},1824)\), and \((\{8,9,10,11,12\},1273)\). Configurations in the listed populations are ground states **if and only if** they attain the sectorwise minimum interaction energy in the table below; no others are.

## Assumptions and scope
The graph \(T\) has vertices \((i,j)\), where \(i,j\in\{0,1,2,3\}\), \(i\ne j\). Its edges are (a) all pairs \((i,j),(i,k)\) of different vertices with the same first coordinate, and (b) the six reverse pairs \((i,j),(j,i)\), \(i<j\). These are exactly twelve triangle edges and six intertriangle edges. There are no other edges or interactions, no thermal fluctuations, and each assignment of the three labeled colors is counted once. The field \(h\) may be any real number. The claim concerns this **finite** twelve-site cluster, not a thermodynamic phase transition.

## Proof
The proof is an exhaustive exact finite contraction, independently realized in two different encodings. There are exactly \(3^{12}=531441\) assignments. For every integer \(k\) with \(0\le k\le12\), define \(m_k=\min_{k(\sigma)=k} e(\sigma)\) and let \(a_k\) count assignments attaining this minimum. The following complete sector minima and multiplicities are obtained by the explicit deterministic algorithms in `verify_enum.cpp` and `verify_blocks.py`, which implement the exact finite sum described next:

| \(k\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(m_k\) | 4 | 3 | 2 | 1 | 0 | 1 | 2 | 4 | 6 | 9 | 12 | 15 | 18 |
| \(a_k\) | 24 | 192 | 504 | 480 | 120 | 480 | 384 | 960 | 480 | 576 | 192 | 24 | 1 |

For a transparent finite mathematical identity behind the contraction, write a coloring as four triple-valued functions \(s_i:\{0,1,2,3\}\setminus\{i\}\to\{0,1,2\}\). Define the local triangle penalty \(c_i=\sum_{j<\ell,\,j,\ell\ne i}\mathbf1_{s_i(j)=s_i(\ell)}\). Then exactly
\[
e(\sigma)=\sum_{i=0}^3c_i+\sum_{0\le i<j\le3}\mathbf1_{s_i(j)=s_j(i)},\quad
k(\sigma)=\sum_{i=0}^3\sum_{j\ne i}\mathbf1_{s_i(j)=0}.
\]
There are \(3^3=27\) local states on each triangle, hence the coefficient of \(u^kz^e\) in the **finite** polynomial
\[
P(u,z)=\sum_{s_0,s_1,s_2,s_3}u^{k(s)}z^{e(s)}
\]
is the exact number of assignments with that \((k,e)\), with precisely \(27^4=531441\) terms. The Python checker contracts these four local state spaces and obtains the table directly. The separate C++ checker uses all twelve base-three digits instead, constructs edges from the ordered-pair adjacency rule, and obtains the same sector minimum table without using the triangle-local formula. Both sum all configurations, not a sample.

The five points \((k,m_k)=(0,4),(4,0),(6,2),(8,6),(12,18)\) are the successive vertices of the lower convex hull of the thirteen sector points; its edge slopes are \(-1,1,2,3\). Every intermediate sector lies on or above its corresponding segment. This is verified by integer cross-multiplication on the displayed thirteen-entry table and checked in `verify_blocks.py`. Consequently the minimum of \(m_k-xk\) over all sectors is exactly the minimum of the five affine functions stated in the finding, **for every real \(x\)**. At a vertex-supporting field only the indicated vertices are minimizing; at a segment slope all sector points lying on that segment are minimizing. Adding their \(a_k\) produces the stated field and coexistence multiplicities. The same exact enumeration gives zero interaction energy and 120 proper three-colorings at zero field.

## Verification
Run `c++ -O2 -std=c++17 verify_enum.cpp -o verify_enum && ./verify_enum` and `python3 verify_blocks.py` from the extracted package directory. The checks independently establish the complete sector minima and multiplicities, the sum \(3^{12}\), convex-hull support, and all four critical-field degeneracies. The C++ program prints `ALL_ASSERTIONS_PASSED`, and the Python program prints `BLOCK_CONTRACTION_PASSED`. The tests enumerate finite spaces completely, so they suffice to certify this finite claim; they make no assertion about larger graphs.

## Relationship to prior work
Coffey and Trugman [1] motivated the truncated tetrahedron as a twelve-site antiferromagnetic spin cluster and investigated its classical-vector and spin-\(1/2\) Heisenberg interactions. Their Hamiltonian and its continuous-spin metamagnetic behavior are not this discrete three-color Potts model. Strečka, Karľová, and Madaras [2] derived magnetization plateaux for Ising spins on five *Platonic* solids; their binary-spin setting and graph list do not determine these Potts counts on an Archimedean solid. Shrock and Tsai [3] considered the three-state antiferromagnetic Potts model on the *honeycomb lattice* at zero field and related its entropy to proper colorings, but not this finite cluster or its color-selective field. Known facts that the truncated-tetrahedral graph is three-colorable and has twelve vertices do not by themselves determine the entire bivariate field-sector spectrum.

The graph is the line graph of the once-subdivided \(K_4\). Its root graph has four degree-three and six degree-two vertices, so statements requiring a *cubic* root graph do not directly apply. No generality beyond the specified finite cluster or independence from all unindexed historical tables is asserted.

## Limitations
The exact result applies to uniform antiferromagnetic equality penalties, three labeled Potts colors, one color-selective field, and the specified finite graph. It does not cover two inequivalent physical exchange strengths, finite-temperature thermodynamics, quantum spins, or macroscopic phase transitions. Unknown alternate-name or tabulated Potts field-sector counts could affect historical priority; prior-art inspection is not an independent audit. The full microcanonical polynomial is generated by the checkers but is not separately tabulated in this note.

## References
1. D. Coffey and S. A. Trugman, *Correlations for the S=1/2 Antiferromagnet on a Truncated Tetrahedron*, arXiv:cond-mat/9206011v1, first public 1992-06-26. https://arxiv.org/abs/cond-mat/9206011
2. J. Strečka, K. Karľová, and T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra*, arXiv:1502.04449v1, first public 2015-02-16. https://arxiv.org/html/1502.04449v1
3. R. Shrock and S.-H. Tsai, *Ground State Entropy and the \(q=3\) Potts Antiferromagnet on the Honeycomb Lattice*, arXiv:cond-mat/9608095, first public 1996-08-21. https://arxiv.org/abs/cond-mat/9608095
