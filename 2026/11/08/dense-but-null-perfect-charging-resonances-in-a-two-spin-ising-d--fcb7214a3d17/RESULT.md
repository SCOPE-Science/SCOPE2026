# Dense but null perfect-charging resonances in a two-spin Ising–DM battery

## Finding

Fix a transverse charging strength \(\Omega>0\). In the *noiseless* two-spin Ising battery with positive Ising and Dzyaloshinskii–Moriya (DM) couplings \(J,D>0\), the couplings admitting **exact unit-probability charging** \(\lvert 00\rangle\to\lvert 11\rangle\) at some finite time form a countable, Lebesgue-null, **dense** subset of the full positive \((J,D)\)-quadrant.

More precisely, every perfect-charging parameter-time triple and only those triples arise from three *distinct odd integers* \(n_-<0<n_0<n_+\), subject to \(S_1>0\) and \(Q>0\), where
\[
S_1=n_-+n_0+n_+,\quad S_2=n_-n_0+n_-n_++n_0n_+,\quad S_3=n_-n_0n_+,
\]
\[
Q=\frac{S_1^3-4S_1S_2+8S_3}{16S_1},\qquad a=\frac{\Omega}{\sqrt Q},
\]
and
\[
\boxed{J=\frac{aS_1}{8},\quad D=a\sqrt{\frac{-S_3}{2S_1}},\quad t=\frac\pi a.}
\]
Thus a set of exact resonances is simultaneously dense and of measure zero; near-perfect charging is not the same as exact charging. When \(J=0\) and \(D>0\), perfect charging is impossible.

An explicit exact example is the odd spectrum \((-1,1,3)\), yielding
\[
\boxed{J=\frac{3\Omega}{2\sqrt5},\qquad D=2\Omega\sqrt{\frac25},\qquad t=\frac{\pi\sqrt5}{4\Omega}.}
\]
In particular, exact charging does not require vanishing DM coupling. The subfamily \((-1,2m+1,2m+3)\), \(m\ge1\), supplies perfect charging with unbounded \(D/\Omega\).

## Assumptions and scope

Set \(\hbar=1\) for time evolution, and use the computational basis \((\lvert00\rangle,\lvert10\rangle,\lvert01\rangle,\lvert11\rangle)\). The uniform-drive, two-site Ising specialization of the 2026 Ising/DM battery Hamiltonian has the Hermitian matrix
\[
H=\begin{pmatrix}
0&\Omega&\Omega&2J\\
\Omega&0&2(J+iD)&\Omega\\
\Omega&2(J-iD)&0&\Omega\\
2J&\Omega&\Omega&0
\end{pmatrix}.
\]
The initial pure state is \(\lvert00\rangle\). We call charging perfect at time \(t>0\) exactly when \(\bigl|\langle11|e^{-itH}|00\rangle\bigr|^2=1\). If the battery's reference energy Hamiltonian is \(-\omega_0(Z_1+Z_2)\), with \(\omega_0>0\) and \(\lvert11\rangle\) its unique upper-energy eigenstate, this coincides with attaining the maximal extractable energy of the pure battery. The result does not concern a nonzero random-telegraph-noise amplitude, nonunitary evolution, an anisotropic XY variant, or multi-spin batteries.

The assertion about all parameter-time triples allows redundant integer descriptions: multiplying all three odd integers by an odd positive integer leaves \((J,D)\) unchanged and produces an odd multiple of the transfer time. It is not a uniqueness statement for integer labels or for shortest time.

## Proof

**1. Exact three-mode reduction.** Define the normalized states
\[
\lvert p\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},\quad
\lvert m\rangle=\frac{|00\rangle-|11\rangle}{\sqrt2},\quad
\lvert s\rangle=\frac{|10\rangle+|01\rangle}{\sqrt2},\quad
\lvert a\rangle=\frac{|10\rangle-|01\rangle}{\sqrt2}.
\]
Direct multiplication gives \(H|m\rangle=-2J|m\rangle\). On the orthogonal span of \((p,s,a)\), subtracting the scalar reference eigenvalue \(-2J\) gives
\[
B=H_{\{p,s,a\}}+2JI
=\begin{pmatrix}4J&2\Omega&0\\2\Omega&4J&-2iD\\0&2iD&0\end{pmatrix}.
\]
Conjugating the last basis vector by a unit complex phase makes \(B\) a real symmetric tridiagonal Jacobi matrix with both off-diagonal magnitudes strictly positive. Therefore its three eigenvalues \(\beta_-<\beta_0<\beta_+\) are simple and every eigenvector has nonzero \(p\)-coordinate. To see the last assertion directly, an eigenvector with first coordinate zero must have second coordinate zero by the first row, and then third coordinate zero by the second row.

Since \(\det B=-16JD^2<0\) and \(\operatorname{tr}B=8J>0\), exactly one eigenvalue is negative and two are positive; none is zero. (Three negative roots would contradict the positive trace.)

**2. Perfect charging requires three odd spectral phases.** As \(|00\rangle=(|p\rangle+|m\rangle)/\sqrt2\) and \(|11\rangle=(|p\rangle-|m\rangle)/\sqrt2\), exact transfer at \(t>0\) holds if and only if \(e^{-itB}|p\rangle=-|p\rangle\), after removing the common factor \(e^{+2iJt}\). Every eigenmode of \(B\) occurs in \(p\), so this is equivalent to \(e^{-it\beta_j}=-1\) for all three eigenvalues. Thus
\[
\beta_j=a n_j,\qquad a=\frac\pi t>0,\qquad
n_-<0<n_0<n_+,\qquad n_j\in 2\mathbb Z+1.
\]
Conversely any spectrum of that form produces the transfer, because all three phases equal \(-1\).

**3. Exact inverse classification.** The characteristic polynomial, including all signs, is
\[
\det(zI-B)=z^3-8Jz^2+[16J^2-4(D^2+\Omega^2)]z+16JD^2.
\]
Equating its elementary symmetric coefficients with those of \(\prod_j(z-an_j)\) yields
\[
aS_1=8J,\quad a^2S_2=16J^2-4(D^2+\Omega^2),\quad
 a^3S_3=-16JD^2.
\]
Eliminate \(J,D\) from the last two equations using the first. The resulting identity is \(\Omega^2=a^2Q\), with \(Q\) as displayed. Therefore \(S_1,Q>0\) are necessary and the formulae in the Finding follow. Conversely, if the stated integers satisfy \(S_1,Q>0\), the reconstructed \(J,D,t\) are positive and all three coefficient identities hold. As both polynomials are monic, the eigenvalues of \(B\) are precisely \(an_j\), establishing sufficiency. This proves an exhaustive classification, not merely a set of sufficient couplings.

For \((n_-,n_0,n_+)=(-1,1,3)\), \(S_1=3\), \(S_2=-1\), \(S_3=-3\), and \(Q=5/16\), giving the explicit witness.

The family \((-1,2m+1,2m+3)\) has
\[
Q_m=\frac{3(4m+5)}{16(4m+3)},\qquad
\frac{D_m^2}{\Omega^2}=\frac{8(2m+1)(2m+3)}{3(4m+5)}.
\]
It is admissible for every integer \(m\ge1\), and the displayed ratio tends to infinity. In this family the transfer times converge to \(\pi\sqrt3/(4\Omega)\).

**4. Density without positive measure.** The collection of integer triples is countable, so its image under the displayed reconstruction is countable and has two-dimensional Lebesgue measure zero. To prove density fix any real couplings \(J,D>0\), let \(\beta_-<0<\beta_0<\beta_+\) be their eigenvalues, and for each sufficiently large positive integer \(k\) choose odd integers \(n_j(k)\) with \(\lvert n_j(k)-k\beta_j\rvert\le1\). They retain the strict signs and ordering. Write \(b_j(k)=n_j(k)/k\). Then \(b_j(k)\to\beta_j\).

The rational function \(Q\) is homogeneous of degree two in its three arguments and continuous wherever their sum is nonzero. From the actual matrix coefficients, \(Q(\beta_-,\beta_0,\beta_+)=\Omega^2>0\) and \(\sum_j\beta_j=8J>0\). Consequently, for all sufficiently large \(k\), the integer triples satisfy both admissibility inequalities. Their reconstructed scaling is
\[
a_k=\frac{\Omega}{\sqrt{Q(n(k))}}
=\frac1k\frac{\Omega}{\sqrt{Q(b(k))}}.
\]
Therefore \(a_k n_j(k)\to\beta_j\), and continuity of the formulas in Step 3 gives \(J_k\to J\) and \(D_k\to D\). Every point of the positive quadrant is thus the limit of exact resonances. This is a topological density statement, not uniform approximation in charging time; the constructed times typically grow with \(k\).

**5. Zero-Ising boundary.** If \(J=0\) and \(D>0\), the matrix \(B\) has a zero eigenvector with nonzero \(p\)-coordinate. Indeed, solving \(Bv=0\) gives \(v_s=0\) and \(\Omega v_p-iD v_a=0\), so \(v_p\ne0\) when \(D>0\). Thus \(e^{-itB}|p\rangle=-|p\rangle\) is impossible at any finite time, because the zero-eigenvalue component remains unchanged.

## Verification

The accompanying `verify.py` is a self-contained Python standard-library checker. It verifies exact rational identities for 29 members of the unbounded-DM family, tests the three elementary-symmetric spectral invariants, and independently evolves the full complex four-state Hamiltonian by scaling-and-squaring Taylor exponentiation for several arithmetic triples. It also implements an independent symmetric-Jacobi eigensolver and constructs approximate resonant couplings for five target points of the positive quadrant, comparing the reconstructed parameters as the odd-integer approximation scale increases. Run it with `python verify.py`; it prints the number of successful deterministic assertions and exits nonzero on failure.

These numerical and finite exact checks test the formulas but do not prove the statements for all integer triples or the whole positive quadrant; those rely on Steps 1–5.

## Relationship to prior work

Zhang et al. (2026), arXiv:2610.21928v1, introduce the driven two-spin Ising/DM model under local random-telegraph noise and provide the underlying Hamiltonian and numerical near-optimal ergotropy regions. The present theorem sets the noise amplitude to zero and classifies exact transfer at finite time, rather than the source's noise-assisted gain or approximate transient charging. The full mathematical statement above is not claimed to follow from a noisy dynamical theorem.

Zhang, Song and Wang (2024), arXiv:2406.16047, study the closely related two-spin Heisenberg/DM battery, including the Ising specialization, and report ergotropy and power behavior numerically. Its formulas supply prior background for the model and general charging dynamics; the exact three-odd-mode inverse classification and topologically dense measure-zero coupling set are not presented in the inspected text.

The generic rational-gap/phase-commensurability condition behind perfect quantum state transfer is established spectral methodology, not a novel principle. A related exact complete-graph result classifies perfect transfer using rational eigenvalue gaps and obtains a dense set of shifted on-site potentials; however, it fixes off-diagonal graph couplings and changes diagonal shifts, not the positive Ising/DM coupling pair in the present transverse two-spin charger. The Jacobi three-mode reduction and inverse parameter reconstruction need separate proofs here. The existing two-spin XY/DM thermal-entanglement classification concerns Gibbs concurrence rather than coherent perfect charging.

## Limitations

The theorem is exact only for unitary evolution in the specified 4-by-4 Ising/DM Hamiltonian, for fixed positive drive and strictly positive Ising and DM strengths. It does not establish exact charging with any nonzero random-telegraph noise, robustness to parameter errors, or a practical short-time optimum. Density in coupling space is compatible with arbitrarily large exact transfer times and with generic impossibility of exact transfer. The all-times parametrization is redundant, and no shortest-time classification is claimed. The relation between pure target-state transfer and a particular energy-storage convention requires the stated unique-highest-energy reference Hamiltonian.

Prior exact spectral-transfer theory could imply some statements after a specialized reduction not explicit in the inspected battery literature; publication-priority assessment remains qualified. 

## References

1. S.-Y. Zhang, M.-L. Song, H.-T. Dong, X.-K. Song, L. Ye, and D. Wang, “Synergistic charging of a quantum battery via Dzyaloshinskii-Moriya interaction and non-Markovian noise,” arXiv:2610.21928v1 (first public 2026-10-15), https://arxiv.org/abs/2610.21928.
2. X.-L. Zhang, X.-K. Song, and D. Wang, “Quantum battery in the Heisenberg spin chain models with Dzyaloshinskii-Moriya interaction,” arXiv:2406.16047v1 (first public 2024-06-23), https://arxiv.org/abs/2406.16047.
3. A. Casaccino, S. Lloyd, S. Mancini, and S. Severini, “Quantum state transfer through a qubit network with energy shifts and fluctuations,” arXiv:0904.4510 (2009), https://arxiv.org/abs/0904.4510.
4. R. J. Angeles-Canul et al., “On quantum perfect state transfer in weighted join graphs,” arXiv:0909.0431 (2009), https://arxiv.org/abs/0909.0431.
5. M. Bhattacharya, Y. Sabale, and P. Kumar, “Heisenberg spin chain models for realising quantum battery with the aid of Dzyaloshinskii Moriya interaction,” arXiv:2508.20529 (2025), https://arxiv.org/abs/2508.20529.
