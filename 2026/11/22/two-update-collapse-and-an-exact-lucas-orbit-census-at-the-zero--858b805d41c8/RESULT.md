# Two-update collapse and an exact Lucas orbit census at the zero-field edge of a separable automaton

## Finding

**Theorem.** Fix integers \(H,W\geq4\). On the binary periodic \(H\)-by-\(W\) lattice consider the normalized rank-one separable-field update defined below, with identical closed birth and survival intervals \(\mathcal S=\mathcal B=[0,\varepsilon]\), where
\[
0\leq\varepsilon<\frac{1}{9HW}.
\]
Every configuration is periodic by its **second update**. The empty configuration is the unique fixed point; every other periodic configuration belongs to a primitive two-cycle consisting entirely of full-row stripes or entirely of full-column stripes. The two-update bound is attained for every \(H,W\geq4\).

Write \(L_0=2\), \(L_1=1\), and \(L_{n+2}=L_{n+1}+L_n\) (Lucas numbers), and define the integer
\[
C_n=L_n+2\cos\!\left(\frac{n\pi}{3}\right)-2 \quad(n\geq4).
\]
Then the **exact** number of primitive two-cycles is
\[
\boxed{N_2(H,W)=\frac{C_H+C_W}{2}},
\]
and the numbers of periodic configurations of periods one and two are respectively \(1\) and \(C_H+C_W\). These are all the primitive periods. In particular, the complete recurrent-state count is \(1+C_H+C_W\), with no computation over the \(2^{HW}\) global states required.

## Assumptions and scope

For a configuration \(X\in\{0,1\}^{\mathbb Z/H\mathbb Z\times\mathbb Z/W\mathbb Z}\), define row and column occupancies
\[
r_j(X)=\sum_i X_{j,i},\qquad c_i(X)=\sum_j X_{j,i},
\]
and blurred profiles
\[
R_j=r_{j-1}+r_j+r_{j+1},\qquad C_i=c_{i-1}+c_i+c_{i+1},
\]
with cyclic subscripts. The raw field is \(n_{j,i}=R_jC_i\), its maximum is \(n_{\max}=\max_{j,i}n_{j,i}\), and for nonempty \(X\) the normalized field is \(q_{j,i}=n_{j,i}/n_{\max}\). When \(X\) is empty, it stays empty. Otherwise the next cell is alive exactly when its normalized field lies in \([0,\varepsilon]\), independently of its present value (because the birth and survival intervals coincide). All comparisons and products here are exact real/integer arithmetic, not floating-point approximations.

The theorem includes \(\varepsilon=0\) and a strictly positive-width interval uniform across all configurations on each fixed torus. It is not a claim for larger threshold widths, unequal birth/survival windows, nonperiodic boundaries, or nonstandard empty-state conventions. It is a finite-system dynamical result under MSC2020 \(37B15\).

## Proof

**1. Exact reduction to zero-field masks.** For nonempty \(X\), some row and column occupancies are positive, so \(n_{\max}>0\). Since \(R_j\) and \(C_i\) are integers bounded by \(3W\) and \(3H\), every positive normalized field satisfies
\[
q_{j,i}\geq\frac1{(3W)(3H)}=\frac1{9HW}>\varepsilon.
\]
Consequently, the selected positions are *precisely* those with \(R_jC_i=0\). Set \(A(X)=\{j:R_j(X)=0\}\) and \(B(X)=\{i:C_i(X)=0\}\). The first update has the exact factorized form
\[
F(X)=\big(A(X)\times\mathbb Z/W\mathbb Z\big)
\cup\big(\mathbb Z/H\mathbb Z\times B(X)\big).\tag{1}
\]
When both masks are empty, \(F(X)\) is empty. When both are nonempty, \(F(X)\) contains at least one fully occupied row and at least one fully occupied column, so **all** its row and column occupancies, and hence all its blurred profiles, are positive. Therefore \(F^2(X)\) is empty.

**2. Stripe dynamics and the two-update bound.** If exactly one mask is nonempty, say \(A(X)\ne\varnothing\), then \(F(X)\) is the full-row stripe configuration associated with \(A(X)\). (The column case is identical.) On a cyclic set \(\mathbb Z/n\mathbb Z\) define
\[
D_n(A)=A+\{-1,0,1\},\quad
T_n(A)=(\mathbb Z/n\mathbb Z)\setminus D_n(A),\quad
E_n(B)=\{j:\{j-1,j,j+1\}\subseteq B\}.
\]
For a nonempty row-stripe set \(A\), its next state is the stripe set \(T_H(A)\), or the absorbing empty state if \(T_H(A)=\varnothing\). The elementary complement identity gives \(T_n^2=E_nD_n\). Moreover, for all \(A\),
\[
A\subseteq E_nD_n(A),\qquad D_nE_n(B)\subseteq B.
\]
Putting \(B=D_n(A)\) and applying \(D_n\) to the first inclusion shows \(D_nE_nD_n(A)=D_n(A)\). Hence
\[
\boxed{T_n^3=T_n}.\tag{2}
\]
Once a trajectory has become a nonempty stripe, either its next state is empty, or its *next* stripe is already on a two-cycle by (2). Combined with (1), this proves \(F^4(X)=F^2(X)\) for every initial \(X\), which is exactly periodicity from update two. No nonempty stripe is fixed, since \(A\cap T_n(A)=\varnothing\); and (1) rules out any nonstripe nonempty periodic state.

The bound is sharp: from a configuration with one occupied cell, both \(A(X)\) and \(B(X)\) are nonempty whenever \(H,W\geq4\). Its first image is a nonempty union of full rows and full columns, whereas its second image is empty. The starting configuration first enters a periodic orbit at update two.

**3. Exact classification of recurrent stripes.** From (2), a proper nonempty stripe set \(A\) is recurrent precisely when \(T_n^2(A)=A\) and \(T_n(A)\ne\varnothing\). The closing operator \(E_nD_n\) fills exactly the maximal complementary zero-runs of lengths one or two in a cyclic binary indicator (it preserves any gap of length at least three). Therefore the eligible sets are *exactly* the nonempty, nonfull cyclic binary words in which each maximal zero-run has length at least three. For such sets \(T_n(A)\) is again eligible and \(T_n^2(A)=A\). The involution \(T_n\) on this family has no fixed point because \(A\cap T_n(A)=\varnothing\), so the number of primitive stripe cycles in that orientation is half the number of eligible sets.

**4. Finite-state census.** A cyclic word with no zero-run of length one or two can be read by the four-state automaton whose states record that the current position is a one, the first zero of a run, the second zero, or a subsequent zero. Its adjacency matrix (rows are source states) is
\[
M=\begin{pmatrix}
1&1&0&0\\0&0&1&0\\0&0&0&1\\1&0&0&1
\end{pmatrix}.
\]
Each admissible cyclic binary word has exactly one compatible cyclic state assignment; this includes the all-zero and all-one words. Thus, for \(n\geq4\), the number of eligible nonempty proper words is
\[
C_n=\operatorname{tr}(M^n)-2.
\]
Direct determinant expansion gives
\[
\det(\lambda I-M)=(\lambda^2-\lambda-1)(\lambda^2-\lambda+1).
\]
The first factor's roots yield the Lucas trace \(L_n\); the second factor's roots \(e^{\pm i\pi/3}\) yield \(2\cos(n\pi/3)\). Hence the stated closed form for \(C_n\).

There are \(C_H\) nonempty periodic row-stripe states and \(C_W\) nonempty periodic column-stripe states. The two orientations cannot overlap except at the empty or full lattice, neither of which is in these two families. Division by two counts primitive two-cycles, and the empty state gives the unique fixed point. This completes the proof.

## Verification

The accompanying dependency-free Python checker implements the *original integer-valued row/column update*, not only the stripe reduction. It exhaustively checks all configurations on the \(4\)-by-\(4\) and \(4\)-by-\(5\) tori, verifies that \(F^4=F^2\), and compares the periodic-state census to the Lucas formula. It also exhaustively verifies \(T_n^3=T_n\), the stripe eligibility description, and the transfer-matrix count for every ring length \(4\leq n\leq13\). The exhaustive grids contain respectively \(65{,}536\) and \(1{,}048{,}576\) configurations. The all-size claims are proved by Steps 1--4; these finite checks do not substitute for those arguments. Execute `python3 checker.py` from the extracted package.

## Relationship to prior work

Shi and Huang [1], first public June 8, 2026, introduced this normalized separable-field model and investigated its phase diagram, cycle regimes, and long transients numerically. The present theorem concerns the mathematically natural **zero-field selection edge** with coincident birth/survival intervals; it gives an all-configuration, all-torus exact dynamical classification and orbit census, rather than another numerical parameter scan.

The closest separately indexed analysis of this model [2] treats the **opposite maximum-field edge** with intervals near \(1\), where states become rectangles rather than the row/column stripe *unions* of (1). Its theorem cannot imply this zero-field classification. Standard dilation/erosion adjunctions and the idempotence of morphological closing [3] are known; Step 2 explicitly uses rather than claims those identities. The specific interaction of the two normalized row-column masks, the resulting uniform two-update bound, and the Lucas-number count for this finite-grid dynamical model are the assertions tested for prior coverage. The literature comparison is not a proof of historical uniqueness.

## Limitations

The model is global rather than a finite-neighborhood shift-space cellular automaton on an infinite lattice. The bound on \(\varepsilon\) is sufficient to select precisely zero-field sites; it is **not asserted to be the largest possible uniform interval**. The periodic-state count does not specify every attraction-basin size or the exact first-entry shell counts. Long-time behavior for windows extending beyond this zero-field range, and for differing survival/birth intervals, is not determined here. The proof depends on the source's convention that the all-zero lattice is absorbing. The source-preprint's complete PDF was not independently retrieved for full-text priority inspection; the original model equations and accessible descriptions were inspected, leaving an acknowledged historical-priority risk.

## References

[1] X. Shi and M. Huang, *Dynamics in a Low-Rank Separable Field Cellular Automaton*, arXiv:2606.08983, first public 2026-06-08. https://arxiv.org/abs/2606.08983 . The precise update appears in section 2.1.

[2] *A sharp near-max selection window and a global two-cycle cutoff for a separable-field automaton*, public research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-near-max-selection-window-and-a-global-two-cycle-cutoff--cc868950d182 . Distinct maximum-field endpoint.

[3] Standard mathematical morphology: dilation-erosion adjunction and idempotent closing. https://en.wikipedia.org/wiki/Mathematical_morphology . Used as background, not claimed as a discovery.
