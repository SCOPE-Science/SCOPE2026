# Half-gap resonances in uniformly coupled quantum-walk bilayers

## Finding

Let \(A\) be an arbitrary real symmetric \(n\times n\) matrix, with \(n\ge 1\), and let its distinct eigenvalues be \(\Lambda\), with real orthogonal spectral projectors \(E_\lambda\). For a uniform interlayer coupling \(g\ge0\), consider
\[
H_g=A\otimes I_2+gI_n\otimes X,\qquad X=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
For a real symmetric Hamiltonian \(H\), write \(\widehat M(H)\) for the infinite-time Cesàro average of its instantaneous transition-probability matrices. Define
\[
C(A)=\sum_{\lambda\in\Lambda}E_\lambda\circ E_\lambda,
\quad B_0(A)=C(A),\quad
B_\delta(A)=\sum_{\substack{\lambda,\mu\in\Lambda\\\lambda<\mu,\ \mu-\lambda=\delta}}E_\lambda\circ E_\mu\quad(\delta>0),
\]
where \(\circ\) is entrywise multiplication; an empty sum is zero. Put \(P_\pm=(I_2\pm X)/2\).

**Theorem (exact bilayer resonance law).** For every \(n\ge1\), every real symmetric \(A\), and every \(g\ge0\),
\[
\boxed{\widehat M(H_g)=C(A)\otimes P_++B_{2g}(A)\otimes P_-.}
\]
Consequently,
\[
\boxed{\operatorname{rank}\widehat M(H_g)=\operatorname{rank}C(A)+\operatorname{rank}B_{2g}(A).}
\]
For every \(g>0\), the matrix \(B_{2g}(A)\) is positive semidefinite and annihilates the all-ones vector. Thus all positive-coupling resonances are confined to the finite set of half-gaps
\[
\mathcal G(A)=\{(\mu-\lambda)/2:\lambda,\mu\in\Lambda,\lambda<\mu\}.
\]
Outside this set, the rank is exactly \(\operatorname{rank}C(A)\); at any half-gap, its increase is the nonnegative integer \(\operatorname{rank}B_{2g}(A)\le n-1\). In particular, \(\widehat M(H_g)\) is never positive definite for \(g>0\). For disconnected layers (\(g=0\)), its rank is \(2\operatorname{rank}C(A)\).

**Sharp natural family.** If \(A\) is the ordinary adjacency matrix of the complete graph \(K_m\), with \(m\ge3\), then the full-rank profile of the \(2m\)-vertex weighted bilayer is
\[
\boxed{\operatorname{rank}\widehat M(H_g)=\begin{cases}2m,&g=0,\\ 2m-1,&g=m/2,\\ m,&g>0\text{ and }g\ne m/2.\end{cases}}
\]
Thus the positive rung strength \(g=m/2\) restores \(m-1\) average-mixing directions that are absent for every other positive strength. The example \(m=3\) has ranks \(6,5,3\) in the three respective regimes.

## Assumptions and scope

The fixed basis labels \(n\) vertices in each of two layers, ordered as vertex then layer. The single-layer Hamiltonian \(A\) may have repeated eigenvalues, may include real edge weights and on-site potentials, and need not be a graph adjacency matrix. No commensurability or rationality of its spectrum is assumed. The layer-coupling strength \(g\) is uniform and nonnegative; changing its sign is a diagonal basis gauge for this two-layer setting, so restricting to \(g\ge0\) loses no rank phenomena for real couplings. No other interlayer edges or unequal-layer potentials are included.

We use the continuous-time quantum-walk convention \(U_H(t)=\exp(itH)\), and
\[
\widehat M(H)=\lim_{T\to\infty}\frac1T\int_0^T\bigl(U_H(t)\circ\overline{U_H(t)}\bigr)\,dt.
\]
All limits exist in finite dimensions. A rank jump at a half-gap is allowed to be zero when all associated entrywise spectral products vanish; no positivity of a jump is asserted without checking its \(B_\delta\) matrix.

## Proof

**1. Factor the propagator and mixing matrix.** The two tensor summands in \(H_g\) commute, so
\[
U_{H_g}(t)=U_A(t)\otimes \bigl(\cos(gt)I_2+i\sin(gt)X\bigr).
\]
Let \(M_A(t)=U_A(t)\circ\overline{U_A(t)}\). Since the layer propagator has squared moduli \(\cos^2(gt)\) on the diagonal and \(\sin^2(gt)\) off the diagonal,
\[
U_{gX}(t)\circ\overline{U_{gX}(t)}=P_++\cos(2gt)P_-.
\]
The entrywise tensor-product rule therefore yields the exact time-dependent identity
\[
M_{H_g}(t)=M_A(t)\otimes P_++\cos(2gt)M_A(t)\otimes P_-.
\]

**2. Average the two Fourier channels.** The spectral theorem gives
\[
M_A(t)=\sum_{\lambda,\mu\in\Lambda}e^{it(\lambda-\mu)}(E_\lambda\circ E_\mu).
\]
The Cesàro average of \(e^{i\omega t}\) is one when \(\omega=0\) and zero otherwise. Hence the time average of \(M_A(t)\) is \(C(A)\). For \(g>0\), the average of \(\cos(2gt)e^{it(\lambda-\mu)}\) is \(1/2\) when \(\lambda-\mu=2g\) or \(\lambda-\mu=-2g\), and zero otherwise. The symmetric ordered pairs give \(B_{2g}(A)\). At \(g=0\), the cosine equals one and this channel averages to \(C(A)=B_0(A)\). Substitution proves the matrix identity including the boundary \(g=0\).

**3. Read off rank and nonresonant bounds.** The orthogonal rank-one projectors \(P_+\) and \(P_-\) have orthogonal ranges. Conjugating the layer coordinate by an orthogonal matrix that diagonalizes \(X\) makes the displayed matrix block diagonal, with blocks \(C(A)\) and \(B_{2g}(A)\). Their ranks add.

Each orthogonal spectral projector is positive semidefinite. By the Schur product theorem, every term \(E_\lambda\circ E_\mu\) is positive semidefinite, and therefore so is \(B_{\delta}(A)\). For \(\lambda\ne\mu\), the \(i\)-th row sum of the entrywise product is
\[
\sum_j (E_\lambda)_{ij}(E_\mu)_{ij}=(E_\lambda E_\mu)_{ii}=0,
\]
because the projectors are symmetric and orthogonal. Thus \(B_\delta(A)\mathbf1_n=0\) for \(\delta>0\), proving \(\operatorname{rank}B_\delta\le n-1\). Moreover, \(C(A)\) is doubly stochastic, hence \(C(A)\mathbf1_n=\mathbf1_n\); the opposite-layer constant vector \(\mathbf1_n\otimes(1,-1)^\mathsf T\) is therefore always in the kernel of \(\widehat M(H_g)\) for every \(g>0\). If \(2g\) is not a difference of eigenvalues, the defining sum for \(B_{2g}\) is empty. At \(g=0\), both blocks equal \(C(A)\), giving twice its rank.

**4. Complete-graph bilayer.** For \(A=A(K_m)=J_m-I_m\), the two spectral projectors are \(E_{m-1}=J_m/m\) and \(E_{-1}=I_m-J_m/m\). Direct entrywise multiplication yields
\[
C(A)=\left(1-\frac2m\right)I_m+\frac{2}{m^2}J_m,
\qquad
B_m(A)=\frac1m I_m-\frac1{m^2}J_m.
\]
For \(m\ge3\), the first is positive definite: its eigenvalues are \(1\) on the all-ones direction and \(1-2/m>0\) on its orthogonal complement. The second has eigenvalue zero on the all-ones vector and eigenvalue \(1/m\) with multiplicity \(m-1\), so its rank is \(m-1\). The only positive eigenvalue gap of \(A\) is \(m\); therefore \(B_{2g}=B_m\) only when \(g=m/2\). The general theorem gives the claimed three exact rank regimes.

## Verification

The accompanying self-contained Python 3 script `verify.py` independently constructs exact rational spectral projectors, expands the \(2n\)-dimensional bilayer Hamiltonian by grouping coincident joint energies, and then compares the resulting sum of projector Schur squares with the closed tensor formula entry by entry. It also checks ranks by exact Gaussian elimination. Run `python3 verify.py` from the directory containing this file and the script.

A completed run yielded `VERIFY_OK exact_profiles= 42 resonant_profiles= 14 matrix_entries= 2520`. Cases include complete graphs of orders two and three, cycles of orders four and six, and real weighted symmetric matrices with rational entries and prescribed integer spectra. Tested couplings include zero, resonances and nonresonances. These finite checks are independent corroboration, not a proof of the unrestricted theorem.

## Relationship to prior work

The established spectral-projector formula for the average mixing matrix and its Gram interpretation appear in Coutinho–Godsil–Guo–Zhan (2017). Coutinho and collaborators (2022) give exact methods for mixing matrices in the quantum-walk setting, and this 2022 source motivates the present question. Baptista–Coutinho–Marques (2023), Section 5, state the instantaneous Cartesian-product mixing identity and study the **trace** of generalized average mixing for Cartesian products; their Proposition 5 also gives a Fourier formula for single-walk sampling averages. The present result specializes these broad spectral tools to tunable uniform interlayer couplings and isolates the full **matrix-valued half-gap selector**, its rank, positive-semidefinite jump structure, a universal kernel mode, and a sharp complete-graph family. These statements are not asserted to be logically independent of the cited general formulas; the explicit rank classification is the contribution assessed here.

## Limitations

The theorem concerns identical layers and spatially uniform real interlayer coupling. Nonuniform rung weights, different layer Hamiltonians and complex non-gaugeable interlayer phases are not covered. The rank formula uses exact eigenvalue-gap equality; approximate gaps at finite averaging times require separate analysis. An eigenvalue gap need not produce a positive rank increment if its entrywise spectral products vanish. The literature comparison may miss a general result that explicitly extracts the same rank consequences from the known Fourier and Cartesian-product identities. Independent external validation has not been performed.

## References

1. G. Coutinho, C. Godsil, K. Guo and H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591v1 (2017), https://arxiv.org/abs/1709.03591 . Especially Sections 1, 3 and 5.
2. G. Coutinho, P. Ferreira Baptista, C. Godsil, T. J. Spier and R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first public 2022-08-18), https://arxiv.org/abs/2208.08971 . Primary MSC 81P68.
3. P. Baptista, G. Coutinho and V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1 (2023), https://arxiv.org/abs/2308.16378 . Especially Proposition 5 and Section 5, Theorem 17.
