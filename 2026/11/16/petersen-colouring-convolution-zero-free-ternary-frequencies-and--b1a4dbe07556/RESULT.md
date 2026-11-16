# Petersen colouring convolution: zero-free ternary frequencies and a six-vertex four-colour resonance

## Finding

Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph, with vertices the ten two-element subsets of \(\{1,2,3,4,5\}\) in lexicographic order, and edges joining disjoint pairs. For \(q=3\), colour with \(H_3=\mathbb Z/3\mathbb Z\); for \(q=4\), colour with \(H_4=\mathbb F_2^2\). Let \(A_q\subseteq H_q^{V(P)}\) denote the proper vertex colourings and let \(T_q\) be unnormalised convolution by \(\mathbf1_{A_q}\) on the corresponding finite abelian group. Define the unnormalised character multiplier
\[
W_q(u)=\sum_{c\in A_q}\chi_u(c),
\quad
\chi_u(c)=\prod_{v\in V(P)}\chi_{u_v}(c_v).
\]
A frequency is *balanced* when \(\sum_vu_v=0\) in the relevant colour group.

**Ternary versus binary-four palette transition.** The exact results are
\[
\begin{array}{c|r|r|r|r}
q&|A_q|&\#\{u:W_q(u)=0\}&\operatorname{rank}T_q&\min_{W_q(u)\ne0}|W_q(u)|\\ \hline
3&120&39\,366&19\,683&3\\
4&12\,960&801\,222&247\,354&16
\end{array}
\]
For \(q=3\), the zeros are *exactly* the \(39\,366\) unbalanced frequencies, so every balanced frequency is recoverable. For \(q=4\), there are \(786\,432\) forced unbalanced zeros and an additional \(14\,790\) balanced zeros. In the four-colour case every nonzero signed multiplier is divisible by \(16\), there are exactly \(83\) distinct signed multiplier levels, and the complete level-multiplicity table appears in `SPECTRUM_Q4.csv`.

A balanced four-colour frequency vanishes only if it has at least **six nonzero vertex coordinates**. The exact numbers of extra balanced zeros at vertex support degrees \(6,7,8,9,10\) are respectively
\[
1110,\quad2880,\quad3420,\quad5040,\quad2340.
\]
An explicit smallest-degree zero is the vertex-frequency vector with entries \(2\) on vertices \(12,13,14,15\), entries \(1\) on \(23,24\), and \(0\) at the other four vertices, writing the two binary coordinates of \(H_4\) as the labels \(0,1,2,3\). Its signed sum has \(6480\) positive and \(6480\) negative contributions.

The sharp Hilbert-space inverse norms on the convolution ranges are \(1/3\) and \(1/16\), respectively; the positive-spectrum condition numbers are \(40\) and \(810\). If \(R_4=\operatorname{ran}(T_4)\), then the optimal endpoint projection norm over **all** real or complex linear projections onto this range is
\[
\boxed{\Lambda_1(R_4)=\Lambda_\infty(R_4)=\frac{5\,453\,971}{65\,536}.}
\]
For the ternary range the corresponding endpoint projection constant is exactly \(1\).

## Assumptions and scope

The graph is fixed, finite and simple, with labelled vertices \(12,13,14,15,23,24,25,34,35,45\). Each vertex receives any of the stated group elements, subject solely to unequal colours across edges. Each character is evaluated using the standard additive pairing: \(\exp(2\pi i ab/3)\) for \(H_3\), and \((-1)^{a_1b_1+a_2b_2}\) for \(H_4\), where four-colour labels are \(a_1+2a_2\). Rank is over \(\mathbb C\) (and equals the real rank). Inverse norms are for the restriction of the unnormalised operator to its range in counting-measure \(\ell^2\). Endpoint projection norms concern the fixed range as a subspace of counting-measure \(\ell^1\) or \(\ell^\infty\). No assertion is made for larger palettes, graph extensions, or arbitrary changes to the colouring encoding.

## Proof

1. **Colour counting and global shifts.** Checking all colour words against the fifteen disjoint-pair edges gives exactly \(120\) ternary and \(12\,960\) four-colour proper words, agreeing with the classical Petersen chromatic-polynomial evaluation. Simultaneous translation of every colour leaves properness unchanged, so multiplying a colour word by such a shift proves \(W_q(u)=0\) for every unbalanced \(u\). The balanced sectors have cardinality \(3^9=19\,683\) and \(4^9=262\,144\).

2. **Analytic ternary zero-free proof.** Every proper ternary colouring uses all three colours, and the \(120\) colourings split into exactly \(20\) orbits under permutations of the three colour names. Since all permutations of \(\mathbb F_3\) are affine, on a balanced frequency each six-colouring orbit contributes either \(6\), when its phase is zero, or \(-3\), when its phase is nonzero. If \(a\) of the twenty orbits have zero phase, then
\[
W_3(u)=6a-3(20-a)=9a-60\ne0,
\]
since \(20\) is not divisible by three. An explicit balanced frequency with labels \(2,2,1,0,1,0,0,0,0,0\) in the specified vertex order has multiplier \(3\), establishing the minimum. The maximum is \(120\) at frequency zero.

3. **Exhaustive four-colour multiplier certificate.** `check.cpp` enumerates the \(4^{10}=1\,048\,576\) words independently from the graph adjacency test, builds the proper-colouring indicator, and applies the exact integer, twenty-stage Walsh–Hadamard transform. It checks all entries against translation symmetry, counts the zeros by vertex-support degree, validates all \(83\) signed levels against `SPECTRUM_Q4.csv`, and checks the exact Parseval identity
\[
\sum_u W_4(u)^2=4^{10}|A_4|.
\]
As an independent frequency-side computation, it constructs the action of the Petersen automorphism group \(S_5\) and the six invertible linear colour maps \(\operatorname{GL}(2,2)\), partitions all \(262\,144\) balanced frequencies into precisely \(513\) orbits, directly recomputes each orbit-representative character sum from all \(12\,960\) proper colourings, and checks the agreement of every orbit with the full transform. This proves the reported nullity, minimum positive magnitude, support-degree counts and signed-multiplier table by finite exhaustive integer arithmetic. In particular, the displayed weight-six witness has exactly \(6480\) terms of each sign. The maximum multiplier magnitude is \(12\,960\) at frequency zero.

4. **Sharp projection norm.** Write \(M=4^{10}\), and \(s(u)=\mathbf1_{\{W_4(u)\ne0\}}\). The translation-equivariant Fourier projection onto \(R_4\) has kernel
\[
K(x)=M^{-1}\sum_u s(u)\chi_u(x).
\]
The checker applies a second exact integer Walsh transform to \(s\) and verifies
\[
\sum_x\left|\sum_u s(u)\chi_u(x)\right|=87\,263\,536.
\]
Thus its \(\ell^1\)- and \(\ell^\infty\)-operator norms both equal \(87\,263\,536/1\,048\,576=5\,453\,971/65\,536\). To prove optimality among all projections, average any linear projection onto the translation-invariant range over all translations. The resulting translation-equivariant projection has no choice but to be the Fourier multiplier \(s\); averaging cannot increase the norm. The ternary range, having precisely the balanced Fourier support, is the space of functions invariant under diagonal colour shifts and admits contractive averaging.

## Verification

The companion files are `check.cpp` (standard C++17 with no external libraries) and `SPECTRUM_Q4.csv` (the complete 83-level signed-multiplier table). To independently reproduce all computations in their directory, run `c++ -O2 -std=c++17 check.cpp -o check` followed by `./check`. The code uses only exact integer operations. Its Kneser-label graph construction, complete frequency-side Walsh transform, direct checks on all symmetry orbits, and independent ternary cyclotomic transform are inspectable. The final checker emits `THREE_COLOR_PASS` and `FOUR_COLOR_PASS`. Arithmetic assertions verify the numerical claims without floating-point thresholds. The infinite-dimensional generalization of any finite result is not asserted.

## Relationship to prior work

The classical Petersen chromatic polynomial already gives the counts \(120\) and \(12\,960\), and partition counts \(20\) and \(520\); these are prior facts, not new enumerations. Goodall's work develops finite-group Fourier transforms and their graphical uses, while Tarsi relates graph-polynomial coefficients and weighted proper colourings. A previously known general four-colour congruence implies the divisibility by \(16\) here, so that congruence is not claimed as new. The additional claims are the exact **Petersen-specific signed spectrum**, its \(14\,790\) additional balanced zeros, the six-vertex onset, the sharp recoverable multiplier gap, and the unrestricted endpoint projection constant. Published work on one-coordinate Fourier sampling for graph-colouring ensembles, and on recolouring dynamics, concerns different operators and does not by itself give these full-cube values.

## Limitations

This is a finite computation with a mathematically exhaustive certificate, not an all-graph or large-palette theorem. The ternary zero-free part has a short algebraic explanation and is not presented as a generally new principle. The four-colour divisibility is independently known in greater generality. The exhaustive certificate, not an external formal prover, establishes the graph-specific arithmetic assertions. Complete historical priority beyond the examined primary sources and mathematical records remains unverified. A 2006 Goodall preprint is identifiable, but its precise first public day was not established; the stated first-public motivating date refers to the precisely dated 2008 arXiv text. There is no independent mathematical audit.

## References

- A. Goodall, *Graph polynomials and Tutte-Grothendieck invariants: an application of elementary finite Fourier analysis*, arXiv:0806.4848v1 (first submitted 2008-06-30), https://arxiv.org/abs/0806.4848.
- A. Goodall, *Fourier Analysis on Finite Abelian Groups: Some Graphical Applications*, preprint, https://iuuk.mff.cuni.cz/~andrew/dwajgApr06.pdf (precise initial public day unverified).
- P. J. Cameron, *Counting colourings of graphs*, 2012-04-12, https://cameroncounts.wordpress.com/2012/04/12/counting-colourings-of-graphs/.
- M. Tarsi, *The graph polynomial and the number of proper vertex coloring*, Annales de l'Institut Fourier 49 (1999), 1089–1093, https://doi.org/10.5802/aif.1707.
