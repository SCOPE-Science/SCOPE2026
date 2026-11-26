# Integral critical group of the Kummer node–trope Levi graph

## Finding

For every smooth complex genus-two curve, consider the sixteen ordinary double points (nodes) and sixteen trope planes on its singular Jacobian Kummer quartic. Let \(\Gamma\) denote their **bipartite incidence graph**, with a node joined to a trope exactly when the node lies on that plane. Then

\[
K(\Gamma)\cong (\mathbb Z/2\mathbb Z)^4\oplus\mathbb Z/4\mathbb Z\oplus(\mathbb Z/16\mathbb Z)^4\oplus(\mathbb Z/32\mathbb Z)^9\oplus\mathbb Z/96\mathbb Z.
\]

The group has order \(3\cdot2^{72}\), exponent \(96\), and nineteen nontrivial cyclic invariant factors. The spectrum of the combinatorial Laplacian is \(0^{(1)},4^{(15)},8^{(15)},12^{(1)}\). The incidence graph has cycle rank \(96-32+1=65\).

## Assumptions and scope

The underlying curve is smooth of genus two over an algebraically closed field of characteristic zero (in particular, over \(\mathbb C\)), with its standard principal polarization. Its singular quartic Kummer image has exactly sixteen nodes and sixteen tropes, forming the classical Kummer \((16_6)\)-configuration. This is a statement about the **abstract integral graph Jacobian** (also called the critical or sandpile group), not about the Jacobian of the genus-two curve, the Picard lattice, or a Kummer-surface discriminant group.

For any connected graph with \(v\) vertices and Laplacian \(L\), choose a vertex \(s\), delete its row and column, and define \(K(\Gamma)=\operatorname{coker}L_s\). The finite isomorphism type is independent of \(s\).

## Proof

1. **The geometric incidence matrix.** The classical Kummer configuration is the distinguished \(2\)-\((16,6,2)\) biplane. It has an explicit model with nodes indexed by \((i,j)\in\{0,1,2,3\}^2\), and a trope indexed by \((a,b)\) containing the six nodes in the same row or column, excluding \((a,b)\). Thus, for lexicographically ordered pairs, the integer matrix is

   \[
   N_{(i,j),(a,b)}=\mathbf1_{(i=a,\ j\ne b)}+\mathbf1_{(i\ne a,\ j=b)}.
   \]

   Every row and column has sum six, and distinct rows meet in exactly two ones; hence \(NN^{\mathsf T}=4I_{16}+2J_{16}\). This identifies the graph without choosing equations or moduli parameters of a particular Kummer quartic.

2. **Laplacian and determinant.** The graph Laplacian in node–trope order is the integer block matrix

   \[
   L=\begin{pmatrix}6I_{16}&-N\\-N^{\mathsf T}&6I_{16}\end{pmatrix}.
   \]

   Since \(NN^{\mathsf T}\) has eigenvalues \(36\) once and \(4\) fifteen times, the singular values of \(N\) are \(6\) once and \(2\) fifteen times. Consequently \(L\) has eigenvalues \(0,12,4^{(15)},8^{(15)}\). The sole zero eigenvalue proves connectivity. Kirchhoff's matrix-tree theorem gives the exact spanning-tree count

   \[
   \det L_s=\frac{12\cdot4^{15}\cdot8^{15}}{32}=3\cdot2^{72}.
   \]

3. **Exact integral invariant factors.** Integer Smith diagonalization of the displayed \(31\times31\) cofactor yields twelve unit factors, four \(2\)'s, one \(4\), four \(16\)'s, nine \(32\)'s, and one \(96\). To provide independently checkable exact arithmetic, `verify_kummer.py` constructs \(L_s\) from the six-incidence rule and performs invertible elementary row and column elimination over the rings \(\mathbb Z/2^e\mathbb Z\) and \(\mathbb Z/3^e\mathbb Z\). It gives the complete local valuation multisets

   \[
   \begin{array}{c|c}
   p&\text{local Smith valuations, including units}\\\hline
   2&0^{(12)},1^{(4)},2^{(1)},4^{(4)},5^{(10)}\\
   3&0^{(30)},1^{(1)}
   \end{array}.
   \]

   The exponent bounds are below the tested precision; therefore these are exact, not lower bounds or floating-point estimates. The determinant from step 2 shows no prime other than \(2\) or \(3\) can occur. Hence the \(2\)-primary group is \((\mathbb Z/2)^4\oplus\mathbb Z/4\oplus(\mathbb Z/16)^4\oplus(\mathbb Z/32)^{10}\), and the \(3\)-primary group is \(\mathbb Z/3\). Combining one \(\mathbb Z/32\) with \(\mathbb Z/3\) gives \(\mathbb Z/96\) as asserted.

## Verification

Run `python3 verify_kummer.py` using Python 3 and no third-party dependencies. The program checks the incidence design axioms, the exact \(31\times31\) cofactor determinant with fraction-free integer elimination, and the local Smith valuations using modular elementary operations. It repeats them for four different deleted vertices and two modular precisions at each relevant prime. Successful output is `KUMMER_BIPLANE_CRITICAL_GROUP_VERIFIED_OK`.

A separate symbolic exact Smith computation with integer matrices gave the same diagonal and group; the attached program uses a different algorithm. Exact integer calculations prove the displayed finite matrix result; this is not an extrapolation from sampled Kummer quartics.

## Relationship to prior work

The sixteen nodes, sixteen tropes and their classical incidence geometry are longstanding, described explicitly by Kumar (arXiv:math/0701669, §4.2). The graph is also known as the folded six-cube. Those facts are premises, **not** novel claims. Gao–Marx-Kuo–McDonald–Yuen (arXiv:1912.06919, Proposition 2.12) provide the mod-two Laplacian rank for the broader family of folded cubes. In the present dimension their formula yields rank twelve, agreeing with nineteen nontrivial \(2\)-primary invariant factors, but does not supply the full exponents or the \(3\)-primary factor.

Previous computations of the integer node–trope **incidence-matrix cokernel** are different: that cokernel is presented by a \(16\times16\) matrix \(N\), whereas the graph Jacobian here is presented by a \(31\times31\) **reduced graph Laplacian**. One does not identify these two quotient groups. The spectral and spanning-tree data alone do not determine the integral invariant factors.

## Limitations

This is the exact graph-critical-group invariant of the canonical complex Kummer configuration. It neither determines the Picard discriminant group of a K3 resolution nor states a new theorem about a geometric genus-two Jacobian. The complete mathematical literature has not been exhaustively indexed; an older graph-specific Smith calculation is a residual priority risk. The local Smith certificate uses modular elimination at finite precision, made mathematically decisive by the exact nonzero pivot valuation and determinant checks. Independent mathematical review has not been performed.

## References

- A. Kumar, *K3 surfaces associated with curves of genus two*, arXiv:math/0701669 (first public version 2007-01-24), §4.2. https://arxiv.org/abs/math/0701669
- J. Gao, J. Marx-Kuo, V. McDonald, C. H. Yuen, *Sandpile Groups of Cayley Graphs of \(\mathbb F_2^r\)*, arXiv:1912.06919 (2019), Proposition 2.12. https://arxiv.org/abs/1912.06919
- A. E. Brouwer, A. M. Cohen, A. Neumaier, *Distance-Regular Graphs* (1989), §9.2D (folded six-cube construction).
- H. S. M. Coxeter, *Self-Dual Configurations and Regular Graphs*, *Bull. Amer. Math. Soc.* **56** (1950), 413–455.
