# Perfect-square dark trapping under Hamming-shell capture in quantum hypercubes

## Finding

A continuous-time quantum excitation launched from a corner of a hypercube can permanently evade a uniform set of absorbers covering **every** vertex at distance two. This happens exactly in perfect-square dimensions, despite the exponentially many monitored vertices. For a hypercube of dimension \(d\ge2\), capture strength \(\gamma>0\), and initially localized excitation, the eventual unabsorbed probability is

\[
S_{d,2}=\begin{cases}
2^{1-d}\binom{d}{(d+\sqrt d)/2},&d\text{ is a perfect square},\\
0,&d\text{ is not a perfect square}.
\end{cases}
\]

For example, the surviving fractions in dimensions \(4,9,16\) are respectively \(1/2\), \(21/64\), and \(1001/4096\). This phenomenon is independent of the positive capture strength. The exact extension to any single monitored Hamming shell, and a two-shell design that removes every dark component, follow below.

## Assumptions and scope

Let \(d\in\mathbb Z\), \(d\ge2\). Vertices of the unweighted hypercube \(Q_d\) are strings \(x\in\{0,1\}^d\), and edges join strings differing in exactly one bit. Write \(|x|\) for Hamming weight, \(A\) for the real adjacency matrix, and

\[
\Pi_r=\sum_{|x|=r}|x\rangle\langle x|,\qquad
H_{d,r,\gamma}=A-i\gamma\Pi_r
\]

for a chosen radius \(0\le r\le d\) and \(\gamma>0\). Evolution is the no-jump, norm-decreasing excitation \(|\psi(t)\rangle=e^{-itH_{d,r,\gamma}}|0^d\rangle\). The survival observable is \(S_{d,r}=\lim_{t\to\infty}\|\psi(t)\|^2\); absorbed probability is \(1-S_{d,r}\). This convention uses the imaginary potential \(-i\gamma\Pi_r\); consequently the instantaneous norm loss is \(2\gamma\langle\psi,\Pi_r\psi\rangle\). The initial state is a **single corner**, not the spatially uniform distribution.

The binary Krawtchouk polynomials in the normalization used here are

\[
K_r(k;d)=\sum_{j=0}^{r}(-1)^j\binom{k}{j}\binom{d-k}{r-j},
\]

where every out-of-range binomial coefficient equals zero. The general exact law is

\[
\boxed{S_{d,r}=2^{-d}\sum_{k=0}^{d}\binom{d}{k}\mathbf1_{\{K_r(k;d)=0\}}.}
\]

For two monitored shells, replace the imaginary potential with \(-i(\gamma_1\Pi_1+\gamma_2\Pi_2)\), where both rates are strictly positive.

## Proof

**1. A closed radial sector.** For \(0\le j\le d\), define the normalized equal-weight shell vector

\[
|j\rangle_R=\binom{d}{j}^{-1/2}\sum_{|x|=j}|x\rangle.
\]

The radial space \(\mathcal R=\operatorname{span}\{|j\rangle_R:0\le j\le d\}\) contains the initial corner and is invariant under both \(A\) and \(\Pi_r\). Direct edge counting gives the tridiagonal restriction

\[
\langle j+1|A|j\rangle_R=\sqrt{(j+1)(d-j)},\qquad0\le j<d,
\]

with zero diagonal. The shell capture restricts to the rank-one projector \(|r\rangle_R\langle r|\). Consequently, the full \(2^d\)-vertex evolution from a corner is exactly represented by the \((d+1)\)-dimensional dissipative radial matrix.

**2. Its simple spectral resolution.** For every subset \(T\subseteq\{1,\dots,d\}\), let

\[
|\chi_T\rangle=2^{-d/2}\sum_{x\in\{0,1\}^d}(-1)^{\sum_{j\in T}x_j}|x\rangle.
\]

These Walsh characters form an orthonormal eigenbasis of \(A\) and satisfy \(A|\chi_T\rangle=(d-2|T|)|\chi_T\rangle\). For \(0\le k\le d\), the normalized permutation-invariant vector

\[
|\phi_k\rangle=\binom{d}{k}^{-1/2}\sum_{|T|=k}|\chi_T\rangle
\]

lies in \(\mathcal R\) and has eigenvalue \(d-2k\). These \(d+1\) eigenvalues are distinct, so the \(|\phi_k\rangle\) form an orthonormal basis of \(\mathcal R\). Counting signs on a shell yields

\[
{}_R\langle r|\phi_k\rangle
=\sqrt{\frac{\binom{d}{k}}{2^d\binom{d}{r}}}\,K_r(k;d),
\qquad
\langle\phi_k|0^d\rangle=\sqrt{\frac{\binom dk}{2^d}}.
\]

Thus the spectral vector \(|\phi_k\rangle\) is completely invisible to every absorber in shell \(r\) exactly when \(K_r(k;d)=0\).

**3. Exact long-time survival.** On \(\mathcal R\), let \(H=A-i\gamma\Pi_r\). If \(Hz=\lambda z\) for a nonzero vector \(z\), then

\[
\operatorname{Im}\lambda
=-\gamma\frac{\|\Pi_r z\|^2}{\|z\|^2}\le0.
\]

Equality is possible precisely for vectors with \(\Pi_r z=0\) that are eigenvectors of \(A\). Because the radial eigenvalues are simple, these vectors are exactly the \(|\phi_k\rangle\) for which \(K_r(k;d)=0\). Their span \(\mathcal D\) is reducing for \(H\): each such vector is simultaneously an eigenvector of \(H\) and its adjoint. Every eigenvalue on the invariant orthogonal complement has strictly negative imaginary part. Finite-dimensional matrix-exponential theory then implies decay to zero on that complement (possibly with a polynomial prefactor, still exponentially bounded). Consequently,

\[
\lim_{t\to\infty}\|e^{-itH}|0^d\rangle\|^2
=\|P_{\mathcal D}|0^d\rangle\|^2
=2^{-d}\sum_{K_r(k;d)=0}\binom dk.
\]

This proves the general law and its independence of \(\gamma>0\), without assuming that the full hypercube lacks nonradial dark states. Such states, if present, are orthogonal to the radial initial condition and therefore irrelevant to this claim.

**4. The square-dimension resonance.** Elementary evaluation of the quadratic Krawtchouk polynomial gives

\[
K_2(k;d)=\tfrac12\big((d-2k)^2-d\big).
\]

For integral \(d\ge2\) and \(0\le k\le d\), this vanishes exactly when \(d=m^2\) is an integer square and \(k=(d\pm m)/2\). Both integers exist because \(d\) and \(m\) have the same parity; both lie in the allowed range and are distinct. Binomial symmetry gives the displayed exact survival fraction. The local central binomial estimate at a one-standard-deviation offset, obtained from Stirling's formula, gives along square dimensions

\[
2^{1-d}\binom{d}{(d+\sqrt d)/2}
=\sqrt{\frac{8}{\pi e d}}\big(1+O(d^{-1/2})\big).
\]

**5. Two-shell completeness.** For first-shell monitoring, \(K_1(k;d)=d-2k\), whereas \(K_2(k;d)=\frac12((d-2k)^2-d)\). They cannot vanish together when \(d\ge2\): the first equation forces the second value to be \(-d/2\ne0\). For positive \(\gamma_1,\gamma_2\), the imaginary part of any radial eigenvalue is \(-[\gamma_1\|\Pi_1z\|^2+\gamma_2\|\Pi_2z\|^2]/\|z\|^2\). A nondecaying eigenvector must be invisible to both shells; none exists, hence the corner-start survival tends to zero.

## Verification

Run the included standalone Python program with `python verify.py` in an environment with `numpy` and `scipy`. It independently enumerates Krawtchouk zeros in all dimensions from 2 through 300, diagonalizes radial adjacency matrices, compares radial and full-hypercube non-Hermitian semigroups, and verifies square-dimension weights. It produced 1,130 passing diagnostic groups. These tests are reproducibility checks, not substitutes for the proof for arbitrary dimension. The explicitly compared square dimensions \(4,9,16\) give exactly \(1/2,21/64,1001/4096\).

## Relationship to prior work

Earlier studies introduce absorption for quantum walks on hypercubes and exploit symmetry reductions. In particular, Yamasaki–Kobayashi–Imai (2002) analyze **coined discrete-time** hypercube absorption; Novo and collaborators (2015) prove the invariant-subspace method for continuous-time transport and analyze the hypercube with a **single target vertex**; Makmal and collaborators (2015) analyze dark states of **coined walks on embedded hypercubes**. Razzoli–Paris–Bordone (2020/2021) examine single-site transport efficiency on other graph structures. Manzano–Chuang–Cao (2016) study uniform-lattice flux rather than spatially complete coherent capture on a Hamming shell.

The present calculation combines the radial Walsh eigenspectrum with a **whole-shell imaginary potential** to obtain an exact all-radius Krawtchouk-zero survival law, a perfect-square exception at radius two, and a positive two-shell elimination rule. These are not asserted by the cited single-vertex, coined-walk, or flux results. The spectral-subspace principle and Krawtchouk formulas themselves are established tools, not claimed as new.

## Limitations

The Hamiltonian uses unweighted adjacency hopping, uniform positive capture rates on each monitored shell, and a vertex-localized initial state at a corner. The statement is about asymptotic no-jump norm survival, not finite-time hitting statistics or noisy density-matrix dynamics. Nonradial dark eigenspaces of the full Hamiltonian are not classified. The large-dimension formula is restricted to square integers. Priority beyond the inspected literature cannot be certified, and no independent scientific audit has been performed.

## References

1. T. Yamasaki, H. Kobayashi and H. Imai, *Analysis of Absorbing Times of Quantum Walks*, arXiv:quant-ph/0205045, first public 2002-05-09; Phys. Rev. A 68, 012302 (2003). https://arxiv.org/abs/quant-ph/0205045
2. L. Novo, S. Chakraborty, M. Mohseni, H. Neven and Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, Scientific Reports 5, 13304 (2015). https://doi.org/10.1038/srep13304
3. A. Makmal, M. Tiersch, C. Ganahl and H. J. Briegel, *Quantum walks on embedded hypercubes: Nonsymmetric and nonlocal cases*, arXiv:1510.08388 (2015). https://arxiv.org/abs/1510.08388
4. L. Razzoli, M. G. A. Paris and P. Bordone, *Transport Efficiency of Continuous-Time Quantum Walks on Graphs*, Entropy 23, 85 (2021), first preprint arXiv:2011.13794 (2020). https://doi.org/10.3390/e23010085
5. D. Manzano, C. Chuang and J. Cao, *Quantum transport in d-dimensional lattices*, New Journal of Physics 18, 043044 (2016). https://doi.org/10.1088/1367-2630/18/4/043044
