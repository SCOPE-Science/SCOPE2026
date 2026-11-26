# Parity-sharp flux optimization of spectral separation in chiral quantum cycles

## Finding

For each integer \(n\ge3\), consider the Hermitian nearest-neighbor cycle Hamiltonian
\[
H_{n,\Phi}=e^{i\Phi/n}S+e^{-i\Phi/n}S^*,\qquad
(Su)_j=u_{j+1\pmod n},\qquad 0\le\Phi\le\pi.
\]
The total gauge-invariant flux is \(\Phi\). Its \(n\) Fourier energies are
\[
\lambda_k(\Phi)=2\cos\left(\frac{2\pi k+\Phi}{n}\right),\qquad 0\le k<n.
\]
Define the smallest **indexed** energy splitting (including zero at degeneracy) by
\[
g_n(\Phi)=\min_{0\le k<\ell<n}|\lambda_k(\Phi)-\lambda_\ell(\Phi)|.
\]
Write \(a=\pi/n\), \(\theta=\Phi/n\). The exact splitting is
\[
\boxed{g_n(\Phi)=\begin{cases}
4\sin a\min\{\sin\theta,\sin(a-\theta)\},&n\text{ odd},\\
4\min\{\sin(2a)\sin\theta,\sin a\sin(a-\theta)\},&n\text{ even}.
\end{cases}}
\]
For every size, the maximizer is **unique** in the full gauge/reflection fundamental interval \([0,\pi]\). For odd \(n\), it is
\[
\boxed{\Phi_n^*=\pi/2,\qquad g_n^*=4\sin(\pi/n)\sin(\pi/(2n)).}
\]
For even \(n\ge4\), it is
\[
\boxed{\Phi_n^*=n\arctan\!\left(\frac{\tan(\pi/n)}3\right),\quad
 g_n^*=\frac{8\sin^2(\pi/n)\cos(\pi/n)}{\sqrt{1+8\cos^2(\pi/n)}}.}
\]
Consequently the optimal total flux has a sharp parity split,
\[
\lim_{\substack{n\to\infty\\n\,\mathrm{odd}}}\Phi_n^*=\frac\pi2,
\qquad \lim_{\substack{n\to\infty\\n\,\mathrm{even}}}\Phi_n^*=\frac\pi3,
\]
and the optimal energy splittings obey
\[
\lim_{\substack{n\to\infty\\n\,\mathrm{odd}}}n^2g_n^*=2\pi^2,
\qquad\lim_{\substack{n\to\infty\\n\,\mathrm{even}}}n^2g_n^*=\frac{8\pi^2}{3}.
\]
Thus the even-size optimal worst-pair splitting has a \(4/3\) larger leading coefficient than the odd-size one.

## Assumptions and scope

The graph is an unweighted, loop-free cycle with \(n\ge3\) vertices and uniform hopping magnitude one. The parameter is the magnetic flux modulo \(2\pi\); complex conjugation identifies opposite fluxes for the spectral optimization. Hence \(0\le\Phi\le\pi\) is a complete fundamental range. No diagonal potential, disorder, losses, or interaction is present. Spectral splittings are between all different Fourier labels, not only different *values* after collapsing degeneracies.

The observable \(g_n\) is motivated by finite-time dephasing of coherent quantum walks. If the walker starts at any vertex and \(p_j(t)\) is its probability to occupy vertex \(j\), then for every \(0<\Phi<\pi\), every \(T>0\), and every vertex \(j\),
\[
\left|\frac1T\int_0^T p_j(t)\,dt-\frac1n\right|
\le\frac{2(n-1)}{nTg_n(\Phi)}.
\]
Thus the displayed unique flux maximizes the smallest energy splitting and minimizes the universal worst-pair denominator in this *particular* dephasing bound. It is **not asserted** to minimize actual total-variation mixing time or any finite-time transport objective.

## Proof

**1. Diagonalization and fundamental flux interval.** On a cyclic Fourier mode \(u_j=\exp(2\pi i k j/n)\), the shift contributes \(\exp(2\pi i k/n)\), so \(H_{n,\Phi}\) contributes the real eigenvalue stated above. Changing the total flux by \(2\pi\) merely relabels Fourier modes; replacing \(\Phi\) by \(-\Phi\) conjugates the Hamiltonian and preserves its spectrum. Therefore the interval \([0,\pi]\) suffices.

**2. Fold the eigenphases.** Fix \(0<\Phi<\pi\), so \(0<\theta<a\). Fold each angle into \([0,\pi]\) using \(\beta=\arccos(\cos((2\pi k+\Phi)/n))\). Since \(2\cos\beta\) decreases strictly on \([0,\pi]\), the smallest difference between distinct energies is achieved by neighboring entries of the increasing list of folded angles.

For **even** \(n=2m\), that sorted list is
\[
\theta,\quad 2ja-\theta,\;2ja+\theta\ (1\le j\le m-1),\quad\pi-\theta.
\]
Entries in parentheses are taken in increasing order of \(j\). Consecutive gaps inside a symmetric pair around \(2ja\) are exactly \(4\sin(2ja)\sin\theta\); consecutive gaps between successive pairs (including the two end gaps) are \(4\sin((2j+1)a)\sin(a-\theta)\) for \(0\le j\le m-1\). Since the minima of the respective sine factors are \(\sin(2a)\) and \(\sin a\), the even splitting formula follows. This includes the edge case \(n=4\) (one interior symmetric pair).

For **odd** \(n=2m+1\), the sorted list is
\[
\theta,\quad 2ja-\theta,\;2ja+\theta\ (1\le j\le m).
\]
The symmetric-pair gaps are \(4\sin(2ja)\sin\theta\), and all between-pair gaps are \(4\sin((2j+1)a)\sin(a-\theta)\), with \(0\le j<m\). The minimum of either sine coefficient is \(\sin a\), giving the odd formula. Both formulas extend continuously to the endpoints, where degeneracies force \(g_n(0)=g_n(\pi)=0\).

**3. Global unique maximizers.** Since \(0\le\theta\le a\le\pi/3\), \(\sin\theta\) is strictly increasing and \(\sin(a-\theta)\) strictly decreasing. Hence the minimum of the two positive increasing/decreasing branches has one and only one maximum, at their crossing. In the odd case the crossing is \(\theta=a/2\), yielding \(\Phi_n^*=\pi/2\). In the even case it solves
\[
\sin(2a)\sin\theta=\sin a\sin(a-\theta),
\qquad\tan\theta=\frac{\tan a}{3}.
\]
Substituting \(\sin\theta=\sin a/\sqrt{1+8\cos^2a}\) gives the even optimum and sharp value.

**4. Size limits.** Elementary small-angle limits give the displayed odd and even limits. For even \(n\), specifically, \(n\arctan(\tan(\pi/n)/3)=\pi/3+8\pi^3/(81n^2)+O(n^{-4})\), which distinguishes the optimal flux from exactly \(\pi/3\) at finite even size.

**5. Finite-time meaning.** A vertex-localized initial state decomposes uniformly into the Fourier eigenmodes. Expanding its time-dependent modulus squared gives one diagonal contribution \(1/n\) and \(n(n-1)\) ordered cross terms of coefficient magnitude \(1/n^2\). When \(0<\Phi<\pi\) all energies are simple by the strict splitting formulas. Each off-diagonal time integral satisfies
\[
\left|\frac1T\int_0^T e^{-it(\lambda_k-\lambda_\ell)}dt\right|
\le\frac{2}{T|\lambda_k-\lambda_\ell|}\le\frac{2}{Tg_n(\Phi)}.
\]
Triangle inequality yields the asserted bound. The infinite-time uniform Cesàro limit itself is a known consequence of simple Fourier spectrum; it is included only to motivate the new gap optimization.

## Verification

Run `python3 verify_gap.py` using Python 3 with no third-party dependencies. It checks 10,064 numerical assertions across all sizes \(3\le n\le69\), including the complete Fourier-pair minimum at sampled fluxes, the proposed optimum and strictness away from it, direct Hermitian-mode residuals, exactly integrated finite-time Cesàro probabilities for \(3\le n\le34\), and large-size asymptotic limits. The script prints `PASS: 10064 numerical checks ...` on success. These finite tests do not prove the infinite-family theorem; the preceding ordered-angle argument does.

## Relationship to prior work

Adamczak et al. (2007) derive Fourier spectra and average-mixing statements for real symmetric, undirected circulant adjacency Hamiltonians. Their nonuniformity proof relies on reversal symmetry of real edge weights and does not apply to a flux-threaded Hermitian cycle; the undirected flux-zero case is one boundary here.

Godsil (2011) studies average mixing of continuous quantum walks, including ordinary cycles. The implication from nondegenerate Fourier spectrum to uniform Cesàro averaging is therefore **not** proposed as a new discovery.

Frigerio et al. (2021) explicitly write the **same magnetic-cycle energy formula** and optimize short-time quantum-classical distance and transport. For odd cycles their observed resonant phase \(\theta=\pi/(2n)\) coincides with the odd optimizer above: that coincidence and the phase choice are prior work. Their Section IV does not identify the minimum over all pairwise energy separations, its even-cycle analytic optimum, or the parity-dependent sharp constants established here; those are the claimed new statements. Their even-size highlighted special phase \(\theta=\pi/n\) is the *degenerate* spectral boundary here, not the spectral-separation optimizer.

Levine et al. (2026) obtain uniform Cesàro mixing for suitable chiral circulants, establishing broader context for simple-spectrum mixing. This result is distinct from and is not claimed to be superseded by the spectral maximin theorem. The closest comparison is the pre-existing complete formula for energies in Frigerio et al.; novelty resides in its nontrivial global maximin optimization and the resulting parity law, not in diagonalizing the ring.

## Limitations

The universal dephasing estimate can be very loose and cannot certify optimal total-variation mixing time or transport fidelity. The theorem does not treat multiple bands, inhomogeneous edge weights, lattice defects, open systems, interacting walkers, or the stability of the optimizer under perturbations. It offers a closed spectral-gap benchmark, not a proof of physical speedup for all observables. Independent external validation and a comprehensive search of older flux-threaded tight-binding ring literature have not been performed.

## References

1. W. Adamczak, K. Andrew, L. Bergen, D. Ethier, P. Hernberg, J. Lin, C. Tamon, *Non-uniform mixing of quantum walk on cycles*, arXiv:0708.2096v1 (first public 2007-08-15), Sections 2 and 4. https://arxiv.org/abs/0708.2096
2. C. Godsil, *Average mixing of continuous quantum walks*, arXiv:1103.2578v1 (2011), including cycle applications. https://arxiv.org/abs/1103.2578
3. M. Frigerio, C. Benedetti, S. Olivares, M. G. A. Paris, *Quantum-classical distance as a tool to design optimal chiral quantum walk*, arXiv:2106.11685v1 (2021), Section IV and Eq. (26). https://arxiv.org/abs/2106.11685
4. L. Levine, J. J. Mesapam, B. Mustico, C. Tamon, G. Tucker, H. Zhan, *Uniform Mixing in Chiral Quantum Walks*, arXiv:2605.04414v1 (2026). https://arxiv.org/abs/2605.04414
