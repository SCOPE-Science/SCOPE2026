# Unattained sharp two-particle transport ceiling on balanced bicliques

## Finding

For every integer \(r\ge 3\), let two hard-core bosons undergo unit-amplitude adjacency hopping on \(K_{r,r}\), initially in a basis configuration with one particle on each shore. Write \(P_r(t)\) for the probability of finding both particles on the same shore at time \(t\). Then
\[
\sup_{t\ge0}P_r(t)=\frac{2r-1}{r^2},\qquad
P_r(t)<\frac{2r-1}{r^2}\quad\text{at every finite }t\ge0.
\]
In particular the same-shore upper envelope is sharp, but there is no first time of equality or finite-time maximizing configuration of the two phases. This concerns the aggregate probability from a *localized opposite-shore pair*, not perfect transfer between two collective same-shore states.

## Assumptions and scope

An orthonormal basis is indexed by the unordered two-element subsets of the vertices. The Hamiltonian \(H\) has matrix entry one for configurations related by one hop to a vacant site, and zero otherwise. Evolution is \(e^{-itH}\) with \(\hbar=1\). The measurement is the orthogonal projection onto all configurations contained in either shore, added together. The statement uses a fixed localized initial basis state, no detuning or collision loss, and all nonnegative real times. It does not assert sharpness on rectangular bicliques or bound the time needed to approach the supremum.

## Proof

**Return and layer probabilities.** The configuration graph is bipartite: one hop changes the class between mixed-shore and same-shore. Let \(J\) equal \(+1\) on mixed configurations and \(-1\) on same-shore configurations, and let \(x\) be the initial mixed basis state. Since \(JH=-HJ\) and \(Jx=x\), the same-shore probability satisfies
\[
1-2P_r(t)=\langle x,e^{itH}J e^{-itH}x\rangle
=\langle x,e^{2itH}x\rangle.
\]
The last expression is real because the odd return moments vanish. Thus the same-shore law is a direct parity consequence of the return amplitude. For a self-contained computation of the latter, more generally take shore sizes \(m,n\ge3\) and let \(B_s\) be the unsigned edge-by-vertex incidence matrix of the complete graph on \(s\) vertices. The mixed-to-same-shore block of \(H\) is
\[
W=\begin{pmatrix}B_m\otimes\mathbf 1_n^{\mathsf T}\\\mathbf 1_m^{\mathsf T}\otimes B_n\end{pmatrix}.
\]
Indeed a new same-shore pair must contain the token that stayed put. Since \(B_s^{\mathsf T}B_s=(s-2)I_s+J_s\), where \(J_s\) is the all-ones matrix, the squared frequencies of \(W^{\mathsf T}W\) on the constant–constant, standard–constant, constant–standard and standard–standard tensor factors are \(4mn-2m-2n\), \(n(m-2)\), \(m(n-2)\) and \(0\). Here a standard factor is the orthogonal complement of constants on that shore. The squared projection weights of a basis vector are \(1\), \(m-1\), \(n-1\) and \((m-1)(n-1)\), each divided by \(mn\). The mixed block of the even propagator is \(\cos(t\sqrt{W^{\mathsf T}W})\) by its power series; this also gives the usual paired positive and negative eigenvalues and a remaining zero band. At \(m=n=r\), the parity identity therefore reads
\[
P_r(t)=\frac{\sin^2(\omega_0t)+2(r-1)\sin^2(\omega_1t)}{r^2},\qquad
\omega_0=2\sqrt{r(r-1)},\quad\omega_1=\sqrt{r(r-2)}.
\]

**Balancing the phases.** Both sine squares would have to be one to reach the envelope. Their frequency ratio is \(2\sqrt{(r-1)/(r-2)}\). If it were rational, the coprime positive consecutive integers \(r-1,r-2\) would both be squares, which is impossible. Equality at positive finite time would force a ratio of odd integers, so it cannot occur. On the other hand, at times \(t_k=(\pi/2+k\pi)/\omega_1\) for nonnegative integers \(k\), the second term is exactly maximal. The first phase modulo \(\pi\) is an irrational rotation because its step divided by \(\pi\) is \(\omega_0/\omega_1\). Its density gives times with the first sine square arbitrarily close to one. This proves sharpness and nonattainment.

**Short-time comparison.** As a consequence of the same spectral weights, at \(t_r=\pi/(2r)\) one has \(rP_r(t_r)\to2\): the second frequency times \(t_r\) tends to \(\pi/2\), and the first term contributes at most \(1/r\) to \(rP_r\). For classical exclusion on the same configuration graph with unit directed-edge jump rates, the mixed-to-same and same-to-mixed rates are \(2(r-1)\) and \(2r\), so the classical same-shore probability equals \((r-1)(1-e^{-(4r-2)t})/(2r-1)\). At the same \(t_r\) its limit is \((1-e^{-2\pi})/2\). This comparison uses known rates and does not enter the supremum proof.

## Verification

The accompanying `verify_two_token.py` constructs the finite configuration graph by enumerating allowed moves, without using the incidence tensor calculation. Its documented scope is six exact integer characteristic-polynomial comparisons, 24 numerical same-shore probabilities, nine numerical classical probabilities and illustrations of the short-time limit. Reproducing these supporting calculations requires Python 3, NumPy, SciPy and SymPy. They do not verify the all-size arithmetic nonattainment or asymptotic time-density argument; those follow from the proof.

## Relationship to prior work

The exact biclique spectrum and mixed-basis return amplitude also appear in [*Flat-band confinement and collective pair transfer for hard-core bosons on complete bipartite networks*](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-flat-band-confinement-and-collective-pair-transfer-for-hard-core--9ab619828b2b/RESULT.md), dated 22 November 2026 UTC. The shared date alone does not establish priority. The parity identity above shows that the time-resolved same-shore law follows immediately from that return amplitude. Neither that law nor the spectrum is claimed as a distinct contribution here. The collective transfer calculation in that record uses just one positive frequency; its perfect-transfer statement does not maximize this two-frequency probability for a localized input. The distinction here is the all-size balanced-envelope extremum, including exclusion of any exact finite-time maximum and existence of arbitrarily close approaches.

The two-token Hamiltonian construction is classical symmetric-square theory (Audenaert, Godsil, Royle and Rudolph, [arXiv:math/0507251](https://arxiv.org/abs/math/0507251)); their strongly regular input theory applies to balanced full spectra in principle. Reyes, Dalfó and Fiol, *On the spectra and spectral radii of token graphs*, [DOI 10.1007/s40590-023-00583-3](https://doi.org/10.1007/s40590-023-00583-3), Corollary 4.3, give the balanced top frequency. Token-graph Laplacian spectra describe a different operator. The stationary mixed-shore component underlying the envelope is present in the collision-dark projector record `f8fb928d3537`, and the classical two-state comparison is already accessible from exclusion record `84ed4797c0f0`. The envelope inequality alone and the classical calculation are not treated as new. An equivalent unindexed extremum calculation may exist; these comparisons do not certify worldwide priority.
