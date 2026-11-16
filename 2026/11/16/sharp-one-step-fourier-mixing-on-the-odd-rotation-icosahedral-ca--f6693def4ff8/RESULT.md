# Sharp one-step Fourier mixing on the odd-rotation icosahedral Cayley network

## Finding
Let \(G=A_5\), of order 60, act on itself by right multiplication. Set
\[
S=\{s\in G:\operatorname{ord}(s)\in\{3,5\}\}.
\]
The 44-element set \(S\) contains all nontrivial odd-order rotations of the icosahedron; it excludes the identity and the 15 half-turns. Let \(\mathcal P\) be the set of **all** entrywise nonnegative doubly stochastic \(60\times60\) matrices supported on the directed edges \(g\to gs\), \(s\in S\), and let \(J=\mathbf1\mathbf1^*/60\). Then
\[
\min_{P\in\mathcal P}\|P-J\|_{2\to2}=\frac1{11}.
\]
The uniform admissible-edge walk \(P_*(g,h)=\mathbf1_{\{g^{-1}h\in S\}}/44\) is optimal. It is the **unique** minimizer among central-convolution walks; uniqueness over the entire set \(\mathcal P\) is not asserted. Its complete spectrum, with algebraic multiplicities, is
\[
1\ (1),\qquad \frac1{11}\ (18),\qquad-\frac1{44}\ (16),\qquad-\frac1{11}\ (25).
\]
Therefore \(\|P_*^k-J\|_{2\to2}=11^{-k}\) for every integer \(k\ge1\).

## Assumptions and scope
The norm is the Euclidean operator norm on \(\mathbb C^{60}\) restricted to the mean-zero subspace, equivalently \(\|P-J\|_{2\to2}\) for a doubly stochastic \(P\). The allowed transition set \(S\) consists exactly of the conjugacy classes of size 20 (3-cycles) and sizes 12 and 12 (the two 5-cycle classes). Holding and order-two transitions are forbidden. The optimization is over arbitrary nonreversible, nonhomogeneous doubly stochastic matrices respecting this support constraint. It is **not** an optimization of total-variation mixing time or a multistep product of distinct walks.

## Proof
**(1) Reduction to conjugacy-invariant convolution.** Both left translation \(g\mapsto ag\) and simultaneous conjugation \(g\mapsto aga^{-1}\) are permutations of the states preserving the allowed-edge relation; the latter is valid because \(S\) is a union of conjugacy classes. For any permutation matrix \(U\) from either symmetry family, \(UPU^{-1}\) is feasible, and \(UJU^{-1}=J\). The operator norm is convex and unitarily invariant, hence
\[
\left\|\frac1{|H|}\sum_{U\in H}UPU^{-1}-J\right\|_{2\to2}\le\|P-J\|_{2\to2}
\]
for each averaging symmetry group \(H\). Averaging first over left translations makes the transition matrix convolution by a probability measure on \(G\); averaging over conjugations makes this measure central. The resulting matrix remains doubly stochastic, supported on \(S\). Thus the unrestricted optimum is achieved in the central-convolution subclass, and every feasible matrix is bounded below by that subclass's optimum.

**(2) Central Fourier eigenvalues.** Write \(x,y,z\ge0\), \(x+y+z=1\), for total probability mass on the order-three class and the two order-five classes, respectively. By Schur's lemma, convolution by a class measure acts on an irreducible representation \(\rho\) of dimension \(d_\rho\) as the scalar \(\sum_C m_C\chi_\rho(C)/d_\rho\). The character table of \(A_5\) gives the four nontrivial irreducible dimensions \(3,3,4,5\) and, with \(\phi=(1+\sqrt5)/2\), \(\phi'=(1-\sqrt5)/2\), the exact values
\[
\lambda_3=\frac{\phi y+\phi' z}{3},\quad
\lambda_{3'}=\frac{\phi' y+\phi z}{3},\quad
\lambda_4=\frac{2x-1}{4},\quad
\lambda_5=-\frac{x}{5}.
\]
The trivial character has eigenvalue one. The regular representation contains each irreducible with multiplicity equal to its dimension, so its scalar eigenvalue occurs with multiplicity equal to the dimension squared.

**(3) Sharp lower bound and equality.** Since \(\phi+\phi'=1\) and \(y+z=1-x\),
\[
\lambda_3+\lambda_{3'}=\frac{1-x}{3},\qquad
\max\{|\lambda_3|,|\lambda_{3'}|\}\ge\frac{1-x}{6}.
\]
Together with \(|\lambda_5|=x/5\), this proves
\[
\|P-J\|_{2\to2}\ge
\max\left\{\frac{1-x}{6},\frac{x}{5}\right\}\ge\frac1{11}
\]
for every central convolution, hence for every feasible \(P\) by (1). Both affine functions meet at \(x=5/11\). For equality, the two three-dimensional scalar eigenvalues must each equal their positive average \(1/11\); because \(\phi-\phi'\ne0\), this forces \(y=z=3/11\). Conversely these masses give
\[
\lambda_3=\lambda_{3'}=\frac1{11},\qquad
\lambda_4=-\frac1{44},\qquad
\lambda_5=-\frac1{11}.
\]
No larger absolute nontrivial eigenvalue occurs. The class masses \((5,3,3)/11\) are precisely proportional to the class sizes \((20,12,12)\), giving equal individual transition probabilities \(1/44\). The equalities above prove uniqueness **among central measures**.

**(4) Multiplicities and powers.** The multiplicities are \(1,3^2+3^2=18,4^2=16,5^2=25\). Central convolution by the uniform \(S\)-measure is real symmetric because \(S=S^{-1}\); the restriction of \(P_*\) to constants is the identity, and its orthogonal complement has absolute spectral radius \(1/11\). Therefore its \(k\)-th power has sharp mean-zero norm \(11^{-k}\) for each \(k\ge1\).

## Verification
The standalone `verify_icosahedral_walk.py` enumerates all 60 even permutations of five symbols, verifies the 44-element generator set and the 15 excluded order-two permutations, constructs the exact integer adjacency matrix, and verifies the annihilating polynomial
\[
(A-44I)(A-4I)(A+I)(A+4I)=0.
\]
It checks the traces of \(I,A,A^2,A^3\), reconstructs the asserted exact adjacency multiplicities \((1,18,16,25)\), and checks the sharp rational mass balancing. All integer and rational checks use exact Python arithmetic. This finite-group certificate independently tests the numerical group-specialized steps, while the full-space optimality follows from the averaging and character argument above, not a finite grid search of stochastic matrices.

Run using `python3 verify_icosahedral_walk.py` with Python 3.10 or newer; no third-party dependencies.

## Relationship to prior work
Moreno and Velasco (first publicly available 2021-10-19) develop finite-group Fourier methods for mixing of random walks on homogeneous spaces, including Fourier spectral measures; the present proof uses that well-known representation-theoretic framework but proves a distinct **exact** one-step constrained optimization on all 60 vertices of a specific normal Cayley graph. Olesker-Taylor and Zanetti address the fastest-mixing problem for general graphs via geometric estimates and emphasize lazy reversible chains; the present no-holding conclusion is an exact norm minimum even among nonreversible doubly stochastic transitions. Earlier normal-Cayley spectral literature and the established \(A_5\) character table supply the basic group tools. No general claim of independent historical priority is made.

## Limitations
The bound concerns one-step mean-zero Euclidean contraction and the fixed allowed-edge set \(S\), not arbitrary symmetric-group moves, optimality over other support budgets, total-variation thresholds, adaptive-step strategies, or a global uniqueness claim beyond central convolutions. The standard symmetrization and character formulas are known; novelty is asserted only for the constrained exact optimum and its equality data, subject to possible coverage by earlier specialized Cayley-graph studies. A 2014 normal Cayley spectral paper was identifiable by title/abstract but not fully readable, leaving a residual historical-priority risk. Independent mathematical audit has not been performed.

## References
1. E. Moreno and M. Velasco, *On random walks and switched random walks on homogeneous spaces*, arXiv:2110.09908 (initial submission 2021-10-19), https://arxiv.org/abs/2110.09908.
2. S. Olesker-Taylor and L. Zanetti, *Geometric Bounds on the Fastest Mixing Markov Chain*, arXiv:2111.05816 (initial submission 2021-11-10); *Probability Theory and Related Fields* **188** (2024), 1017–1062, https://doi.org/10.1007/s00440-023-01257-x.
3. X. Liu and S. Zhou, *Eigenvalues of Cayley Graphs*, arXiv:1809.09829 (2018), https://arxiv.org/abs/1809.09829 (background survey).
4. *On the spectrum of Cayley graphs via character table*, 2014, https://doi.org/10.22061/JMNS.2014.477 (abstract examined; full text not obtained).
5. Character table of \(A_5\), ATLAS of Finite Group Representations, https://brauer.maths.qmul.ac.uk/Atlas/alt/A5/.
