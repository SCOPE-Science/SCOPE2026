# Exact singular spectrum and optimal two-parity dephasing budget for Fourier-type quantum channels

## Finding

Let \(d\geq2\) be an integer and let \(U\in\mathbb C^{d\times d}\) be unitary with **both** of the following properties:

1. \(|U_{jk}|^2=1/d\) for every \(j,k\) (\(U\) is complex Hadamard).
2. \(U^2\) is a monomial unitary: a product of a diagonal unitary and a permutation matrix.

For each \(p\in[0,1]\), define the quantum channel
\[
\mathcal L_p(X)=(1-p)UXU^\dagger+p\,\mathcal P(UXU^\dagger),\qquad
\mathcal P(X)=\sum_{j=0}^{d-1}|j\rangle\langle j|X|j\rangle\langle j|.
\]
For any integer \(t\geq1\), take arbitrary, potentially different \(p_1,\ldots,p_t\in[0,1]\), put \(\mathcal T_t=\mathcal L_{p_t}\circ\cdots\circ\mathcal L_{p_1}\), and define
\[
Q_{\mathrm o}=\prod_{\substack{1\leq k\leq t\\k\ \mathrm{odd}}}(1-p_k),\qquad
Q_{\mathrm e}=\prod_{\substack{1\leq k\leq t\\k\ \mathrm{even}}}(1-p_k).
\]
An empty product is one. The complete multiset of singular values of \(\mathcal T_t\), restricted to trace-zero operators with the Hilbert--Schmidt norm, is exactly
\[
\underbrace{Q_{\mathrm o},\ldots,Q_{\mathrm o}}_{d-1},\quad
\underbrace{Q_{\mathrm e},\ldots,Q_{\mathrm e}}_{d-1},\quad
\underbrace{Q_{\mathrm o}Q_{\mathrm e},\ldots,Q_{\mathrm o}Q_{\mathrm e}}_{(d-1)^2}.
\]
These entries include zeros and repeated values with their multiplicities. Consequently, writing \(\Delta(X)=\operatorname{tr}(X)I/d\),
\[
\boxed{\left\|\mathcal T_t-\Delta\right\|_{2\to2,\,\operatorname{tr}=0}
=\max\{Q_{\mathrm o},Q_{\mathrm e}\}.}
\]
The bound is *attained by the normalized Hilbert--Schmidt displacement of some genuine density matrix from \(I/d\)*; it is not merely a formal bound on non-Hermitian matrices.

Moreover, for every \(t\geq2\) and every fixed total dephasing budget \(B\in[0,t]\),
\[
\boxed{\min_{\substack{0\leq p_k\leq1\\\sum_{k=1}^tp_k=B}}
\left\|\mathcal T_t-\Delta\right\|_{2\to2,\,\operatorname{tr}=0}
=\max\{0,1-B/2\}.}
\]
If \(0<B<2\), **all** optimal schedules consist of exactly two nonzero dephasing probabilities, each \(B/2\), one on an odd-indexed step and the other on an even-indexed step. At \(B=2\), exactly one full dephasing step in each parity group is optimal. If \(2<B\leq t\), a schedule is optimal if and only if it includes at least one full dephasing step of each parity. With \(B=0\), the zero schedule is the only choice. In particular, increasing the number of allowed steps never improves the optimal worst-case error once both parities are available.

For constant \(p_k=p\), the exact contraction is \((1-p)^{\lfloor t/2\rfloor}\). Two full dephasing steps give the completely depolarizing channel, \(\mathcal T_2=\Delta\), in *any* finite dimension in this unitary class. For a single step, the worst-case contraction is one even if \(p_1=1\).

## Assumptions and scope

The Hilbert--Schmidt norm is \(\|X\|_2=(\operatorname{tr}(X^\dagger X))^{1/2}\), and the induced norm is taken on the complex linear space \(\{X:\operatorname{tr}X=0\}\). All conclusions are finite-dimensional for every integer \(d\geq2\), every positive integer \(t\), and all admissible parameters. The cost \(B=\sum p_k\) is the total *per-step projective-dephasing probability*; it is not an energetic or continuous-time dissipation budget.

The normalized discrete Fourier transform \(U_{jk}=d^{-1/2}\exp(2\pi i jk/d)\) satisfies the hypotheses because its square permutes the labels by inversion. Tensor Walsh--Hadamard transforms also satisfy them. The theorem does not assume a particular graph or a local coined-walk realization; it gives a fully specified unitary-and-pinching instance of the coherent/classical interpolation framework.

## Proof

Write \(V(X)=UXU^\dagger\) and \(\mathcal K_p=(1-p)\mathrm{Id}+p\mathcal P\), so that \(\mathcal L_p=\mathcal K_p V\). The map \(V\) is unitary on Hilbert--Schmidt operator space. Both \(\mathcal P\) and \(\mathcal R=V\mathcal P V^{-1}\) are orthogonal projections there. They project onto the two maximal diagonal algebras defined by the standard basis and the \(U\)-rotated basis.

Complex Hadamardness gives \(\mathcal P\mathcal R=\mathcal R\mathcal P=\Delta\). Indeed, \(\mathcal R(X)=U\operatorname{diag}(U^\dagger XU)U^\dagger\), and taking its diagonal replaces each entry by \(\frac1d\sum_j(U^\dagger XU)_{jj}=\operatorname{tr}(X)/d\). Reversing the roles of the bases gives the other identity. Thus the trace-zero parts of the two diagonal algebras are orthogonal, and \(\mathcal P\) and \(\mathcal R\) commute.

Because \(U^2\) is monomial, conjugation by \(U^2\) preserves the standard diagonal algebra. Hence \(V^2\mathcal P V^{-2}=\mathcal P\), so \(V^{2j}\mathcal P V^{-2j}=\mathcal P\) and \(V^{2j+1}\mathcal P V^{-(2j+1)}=\mathcal R\) for every nonnegative integer \(j\).

Move the unitary conjugations in \(\mathcal T_t\) to the right:
\[
\mathcal T_t=
\left[\prod_{j=0}^{t-1}
\left((1-p_{t-j})\mathrm{Id}+p_{t-j}V^j\mathcal P V^{-j}\right)\right]V^t.
\]
All bracketed factors commute, as each is a polynomial in the commuting projections \(\mathcal P,\mathcal R\). They act diagonally on the orthogonal decomposition
\[
\mathcal B(\mathbb C^d)=
\mathbb CI\ \oplus\ \mathcal P_0\ \oplus\ \mathcal R_0\ \oplus\ \mathcal K,
\]
where \(\mathcal P_0=\operatorname{Ran}(\mathcal P)\cap\ker\Delta\), \(\mathcal R_0=\operatorname{Ran}(\mathcal R)\cap\ker\Delta\), and \(\mathcal K=(\mathbb CI\oplus\mathcal P_0\oplus\mathcal R_0)^\perp\). Their dimensions are \(1,d-1,d-1,(d-1)^2\), respectively. The product acts as one on \(\mathbb CI\), as \(Q_{\mathrm o}\) and \(Q_{\mathrm e}\) in some order on \(\mathcal P_0\) and \(\mathcal R_0\), and as \(Q_{\mathrm o}Q_{\mathrm e}\) on \(\mathcal K\). Right multiplication by the unitary superoperator \(V^t\) leaves all singular values unchanged. This proves the full singular-value formula and the induced norm.

Sharpness for physical density matrices follows because both \(\mathcal P_0\) and \(\mathcal R_0\) contain nonzero Hermitian traceless operators. Take a Hermitian unit-Hilbert--Schmidt vector \(H\) in whichever one corresponds to the larger scalar. For sufficiently small \(\varepsilon>0\), \(\rho=I/d+\varepsilon V^{-t}(H)\) is a positive density matrix, because unitary conjugation preserves Hermiticity and positivity at small perturbation; the ratio \(\|\mathcal T_t(\rho)-I/d\|_2/\|\rho-I/d\|_2\) equals the induced norm exactly.

For the budget problem let \(B_{\mathrm o}=\sum_{k\ \mathrm{odd}}p_k\) and \(B_{\mathrm e}=\sum_{k\ \mathrm{even}}p_k\). The elementary product inequality \(\prod_j(1-p_j)\geq1-\sum_jp_j\) implies
\[
\max\{Q_{\mathrm o},Q_{\mathrm e}\}\geq
\max\{1-B_{\mathrm o},1-B_{\mathrm e}\}
=1-\min\{B_{\mathrm o},B_{\mathrm e}\}\geq1-B/2.
\]
There is also the lower bound zero. For \(B\leq2\), placing probabilities \(B/2\) on one odd and one even step gives equality. For \(B\geq2\), a full-dephasing step in each parity group makes both products zero, and the remaining budget can be distributed among the other steps (when feasible). For \(0<B<2\), equality requires \(B_{\mathrm o}=B_{\mathrm e}=B/2<1\) and equality in both product inequalities. The latter is possible exactly when there is at most one nonzero probability within each parity group: in the induction \((1-a)(1-b)=1-a-b+ab\), two positive entries force a strict excess. This proves the complete optimizer classification. The cases \(B=0\), \(B=2\), and \(B>2\) follow by inspecting when a product of factors in \([0,1]\) vanishes.

## Verification

The accompanying standalone `check.py` directly constructs the matrix representation of the composed channels on the \(d^2\)-dimensional operator space, computes its singular values after subtracting the depolarizing projection, and compares the entire multiset with the theoretical factors for several discrete Fourier and Walsh--Hadamard examples, including full and zero dephasing, alternating nonuniform strengths, and an exact two-pulse budget example. A separate small-grid calculation checks the stated budget optimum numerically. The script checks independent matrix products rather than reusing the algebraic proof, and its numerical checks do not substitute for the proof above. It requires Python 3 and NumPy.

## Relationship to prior work

Higuchi, Segawa, Shiratori and Yoshino (2026) formulate convex interpolations of unitary quantum walks with pinched correlated/classical walks and prove general spectral-annulus and absorption-space results. Their spectral bounds do not specify an exact singular multiset for arbitrary nonstationary dephasing probabilities or optimize their sum. The present result is about a Fourier-type global unitary benchmark, not a claim to extend their graph-specific absorption characterizations.

Basile, de Leon, Fonseca, Leyvraz and Pineda (2023/2024) develop Weyl-diagonal and component-erasing quantum channels, covering the algebraic components used in finite-dimensional dephasing. Their analysis of Weyl-diagonal maps and semigroups is not itself the stated nonstationary product and fixed-cost minimax theorem. The fact that two complete measurements in mutually unbiased bases erase state information is a familiar consequence of complementary projective measurements, **not claimed here as an independent new principle**. The additional result concerns the full singular spectrum for partial steps and the exact minimax allocation across any number of steps.

Burgarth, Chiribella, Giovannetti, Perinotti and Yuasa (2012/2013) give general criteria for ergodicity and mixing of quantum channels, but not this quantitative, dimension-independent schedule optimization. These earlier results motivate the model and the question of sharp quantitative mixing; no statement that the present theorem was formally proved in a previously published source is made.

## Limitations

The exact singular multiset and resource optimum concern Hilbert--Schmidt mixing, not trace norm, diamond norm, entropy or physical work cost. The complex-Hadamard and monomial-square hypotheses are structural: general unitary channels need not have the alternating two-algebra decomposition, so the result is not asserted for arbitrary graph quantum walks or arbitrary Hadamard matrices whose square is not monomial. The two-full-measurement special case is already part of the wider complementary-measurement picture. An earlier specialized analysis of variable-strength Fourier dephasing might also imply the sharp budget theorem; the literature comparison cannot rule out all unindexed or inaccessible papers. No independent external validation is claimed.

## References

1. Y. Higuchi, E. Segawa, H. Shiratori and S. Yoshino, *Interpolating walk between discrete-time quantum walk and its intrinsic random walk on graph*, first public 25 September 2026, arXiv:2609.30931. https://arxiv.org/abs/2609.30931
2. T. Basile, J. A. de Leon, A. Fonseca, F. Leyvraz and C. Pineda, *Weyl channels for multipartite systems*, first public 17 October 2023, arXiv:2310.10947; Phys. Rev. A 109 (2024), 032607. https://arxiv.org/abs/2310.10947
3. D. Burgarth, G. Chiribella, V. Giovannetti, P. Perinotti and K. Yuasa, *Ergodic and Mixing Quantum Channels in Finite Dimensions*, first public 20 October 2012, arXiv:1210.5625; New J. Phys. 15 (2013), 073045. https://arxiv.org/abs/1210.5625
4. A. Kalev and G. Gour, *Mutually unbiased measurements in finite dimensions*, New J. Phys. 16 (2014), 053038. https://doi.org/10.1088/1367-2630/16/5/053038
