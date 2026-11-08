# Sharp weak-loss relaxation exponent for corner-trapped prime tori

## Finding
Let \(d\ge2\) be fixed, and choose pairwise distinct odd primes \(p_1,\ldots,p_d\ge5\). Put \(G=C_{p_1}\square\cdots\square C_{p_d}\), let \(A\) be its unweighted adjacency, and let the trap set consist of the \(2^d\) vertex coordinates \(T=\{0,1\}^d\). For a real nonzero hopping constant \(J\) and a uniform absorption strength \(\kappa>0\), consider the non-Hermitian effective Hamiltonian \(H_\kappa=JA-i\kappa P_T\), where \(P_T\) projects onto coordinate basis vectors at trapped vertices.

All eigenvalues have strictly negative imaginary part for every \(\kappa>0\). Define the slowest amplitude-attenuation rate \(\delta(\kappa)=\min_{z\in\sigma(H_\kappa)}(-\operatorname{Im}z)\). The exact weak-loss coefficient is
\[
\lim_{\kappa\downarrow0}\frac{\delta(\kappa)}{\kappa}
=\mu_*(p_1,\ldots,p_d)
=\prod_{j=1}^{d}\frac{2-2\cos(\pi/p_j)}{p_j}.
\]
Equivalently, \(\delta(\kappa)=\kappa\mu_*+O(\kappa^2)\) for each fixed torus and fixed \(J\ne0\). For fixed dimension as every prime side length tends to infinity, \(\mu_*\sim\pi^{2d}\prod_jp_j^{-3}\). The corresponding optimal exponential rate for the squared norm of the propagator is twice the amplitude-attenuation rate, in the usual spectral-exponent sense.

The theorem concerns the quantitative decay bottleneck of a *known* minimal trapping/observing pattern. The fact that \(2^d\) appropriately chosen nodes suffice for observability, and that fewer do not, was established by Notarstefano and Parlangeli (2011); the threshold itself is not claimed as new.

## Assumptions and scope
All cycles are undirected nearest-neighbor graphs; \(C_p\) has vertex set \(\mathbb Z/p\mathbb Z\), with edges to the two adjacent residues. The indicated primes must be pairwise distinct, not merely odd, to exclude accidental energy coincidences in the sum Hamiltonian. The loss operator is a nonnegative diagonal projector with identical coefficient \(\kappa\) on precisely the corner set \(T\); arbitrary placement or heterogeneous loss strengths are not asserted. The limit is taken at fixed finite graph, and the large-side asymptotic is a subsequent limit for fixed dimension. For each fixed \(\kappa>0\), propagation is \(e^{-iH_\kappa t}\) in units with \(\hbar=1\).

A generic initial state has a nonzero component in the least-damped mode; no uniform claim is made that *every* initial state has that same individual late-time decay exponent. The result does not assert a uniform-in-size perturbation remainder in \(\kappa\).

## Proof
**1. Exact energy sectors.** Write \(\zeta_j=e^{2\pi i/p_j}\). The orthonormal Fourier characters of the torus are \(\phi_{\boldsymbol b}(\boldsymbol x)=N^{-1/2}\prod_j\zeta_j^{b_jx_j}\), where \(N=\prod_jp_j\). Their adjacency energies are \(E_{\boldsymbol b}=2J\sum_j\cos(2\pi b_j/p_j)\). Let \(a_j\in\{0,\ldots,(p_j-1)/2\}\), and group signed frequencies \(b_j\in\{a_j,-a_j\}\) (one choice if \(a_j=0\)). The corresponding energy-sector dimension is \(\prod_jm_j\), with \(m_j=1\) for \(a_j=0\) and \(m_j=2\) otherwise.

There are no other energy coincidences. Indeed, an equality of two sums of coordinate cosine values forces the difference in any single prime cyclotomic subfield to lie in its intersection with the compositum of all other prime cyclotomic fields, hence in \(\mathbb Q\). When both compared frequencies are nonzero, the algebraic trace of this rational difference is zero; it therefore vanishes. When exactly one is zero, its rational trace average has absolute value \(2p_j/(p_j-1)\), which is not an integer for \(p_j\ge5\), contradicting that a rational cyclotomic integer is an integer. Thus all unsigned frequencies coincide. The cyclotomic-field disjointness used here follows from coprime conductors.

**2. Trap compression.** Denote the orthogonal spectral projector for a sector by \(P_{\boldsymbol a}\). In its normalized Fourier basis, the positive matrix \(P_{\boldsymbol a}P_TP_{\boldsymbol a}\) restricted to the sector is exactly a tensor product \(B_{p_1,a_1}\otimes\cdots\otimes B_{p_d,a_d}\). For \(a=0\) the block is the scalar \(B_{p,0}=(2/p)\); for \(a>0\), with \(z=e^{2\pi ia/p}\), it is
\[
B_{p,a}=\frac1p\begin{pmatrix}2&1+\bar z^2\\1+z^2&2\end{pmatrix}.
\]
Its eigenvalues are \((2\pm2|\cos(2\pi a/p)|)/p\), both strictly positive for odd \(p\). Hence the full trap compression in every adjacency energy sector is positive definite. A real eigenvalue of \(H_\kappa\) would force the corresponding vector to have zero mass on all traps by the imaginary-part identity, making it an adjacency eigenvector in the kernel of this compression; contradiction. Thus all modes decay for each \(\kappa>0\).

**3. Sharp weak-loss coefficient.** Finite-dimensional analytic perturbation theory for the Hermitian matrix \(JA\) gives, at each unperturbed energy \(2J\sum_j\cos(2\pi a_j/p_j)\), the first-order imaginary shifts \(-\kappa b\), with \(b\) ranging over eigenvalues of the compressed trap matrix. As there are finitely many sectors and strictly positive \(b\), the coefficient of the *least* attenuation is the smallest of all these \(b\). A tensor product of positive matrices has smallest eigenvalue equal to the product of its smallest factor eigenvalues.

For each \(p\ge5\), among all unsigned cycle frequencies, the minimum block eigenvalue is uniquely attained at \(a=(p-1)/2\): its value is \((2-2\cos(\pi/p))/p\). The nonzero candidate \(a=1\) gives a larger value because \(\cos(\pi/p)>\cos(2\pi/p)\); intermediate nonzero frequencies have smaller absolute cosine, while the zero-frequency scalar \(2/p\) is larger. Taking the product over coordinates yields the stated formula, with a unique minimizing energy sector and eigenvector at first order. Finally, \(2-2\cos(\pi/p)=\pi^2/p^2+O(p^{-4})\), establishing the large-prime asymptotic.

## Verification
Run `python3 verify.py` with NumPy available. The script checks the full tensor Gram spectrum and the strict minimizing sector for \((5,7)\), \((5,11)\), \((7,11)\), and \((5,7,11)\), then independently diagonalizes the actual dissipative Hamiltonians for the first three cases at \(\kappa=0.08,0.04,0.02\). The numerically obtained ratios \(\delta(\kappa)/\kappa\) converge to the predicted exact coefficient. The first case has \(\mu_*(5,7)\approx0.0021615158009654\), and the three-dimensional case has \(\mu_*(5,7,11)\approx1.5919377742252\cdot10^{-5}\). The script tests finite examples only; its output is not substituted for the arbitrary-prime proof above.

## Relationship to prior work
Notarstefano and Parlangeli, *Observability and reachability of simple grid and torus graphs* (2011), especially Propositions 4.7–4.8, already show a sharp \(2^d\)-node observation threshold for suitable toroidal products, realized by a Cartesian cube of adjacent observations. Their theorem resolves the *existence* of a dark-free design; it does not state an exact weak-loss spectral width or its \(\prod_jp_j^{-3}\) deterioration. Krapivsky, Luck and Mallick (arXiv:1311.6298) examine continuous-time trapping, including finite one-dimensional rings and higher-dimensional disordered lattices, without the fixed higher-dimensional prime-torus corner-trap spectral-width calculation here. A publicly indexed result on sharp two-sensor Fourier frame bounds for cycles is relevant to the one-dimensional Gram factors; available summary material did not settle the tensor weak-loss result. Existing qualitative controllability results and standard perturbation theory are acknowledged as inputs, not claimed as new.

## Limitations
This is a sharp *weak-loss first-order* statement, not an exact finite-strength formula or a uniform bound when the side lengths diverge simultaneously with the weak-loss limit. Equal loss strengths and pairwise distinct odd-prime cycle lengths are essential to the presented statement/proof. Existing controllability results already imply qualitative full absorption for the chosen traps; only the quantitative sharp relaxation coefficient is proposed here as the additional finding. No independent scientific validation or complete historical priority certification has been performed. An indexed but full-text-inaccessible two-sensor frame result could imply parts of the Gram analysis, and unindexed earlier finite calculations cannot be excluded.

## References
1. G. Notarstefano and G. Parlangeli, *Observability and Reachability of Simple Grid and Torus Graphs*, 18th IFAC World Congress (2011), DOI: `10.3182/20110828-6-IT-1002.03618`; lawful proceedings text: https://skoge.folk.ntnu.no/prost/proceedings/ifac11-proceedings/data/html/papers/3618.pdf.
2. P. L. Krapivsky, J. M. Luck, and K. Mallick, *Survival of Classical and Quantum Particles in the Presence of Traps*, arXiv:1311.6298 (first submitted 2013-11-25), https://arxiv.org/abs/1311.6298.
3. *Sharp spectral-demixed two-sensor frame bounds on finite cycles*, publicly indexed 2026 mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-spectral-demixed-two-sensor-frame-bounds-on-finite-cycles--b03d8e4c7818. Only the indexed summary could be compared; its full text was not available in this examination.
