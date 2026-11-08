# Sharp fixed-negativity correlation-ergotropy frontiers for pure two-qutrit batteries

## Finding
For two identical three-level cells with single-cell Hamiltonian \(h=\omega\operatorname{diag}(0,1,2)\), \(\omega>0\), fix any pure bipartite state and its *natural-logarithm* logarithmic negativity \(\mathcal N\in[0,\log3]\). Put \(s=e^{\mathcal N/2}\), \(D(s)=\sqrt{6-2s^2}\), and
\[
z_*(s)=\frac12\left(s-\frac{\sqrt{4-s^2}}{\sqrt3}\right),\qquad
B_+(s)=(s-z_*)\sqrt{2-s^2+2sz_*-3z_*^2},
\]
\[
B_-(s)=\begin{cases}
\dfrac{1+s\sqrt{2-s^2}}2,&1\le s\le\sqrt2,\\[5pt]
\dfrac{sD(s)}3-\dfrac{D(s)^2}{12},&\sqrt2\le s\le\sqrt3.
\end{cases}
\]
The exact possible interval of correlation ergotropy \(\mathcal W_{\mathrm{corr}}\), the collective ergotropy minus the sum of optimal local ergotropies, is
\[
\boxed{2\omega(1-B_+(s))\ \le\ \mathcal W_{\mathrm{corr}}\ \le\ 2\omega(1-B_-(s)).}
\]
Every value in this closed interval is achieved by a pure state of the prescribed logarithmic negativity. The lower-energy frontier has a unique unordered Schmidt spectrum, of full rank with three distinct weights for \(0<\mathcal N<\log3\). The upper-energy frontier has Schmidt rank two for \(0<\mathcal N<\log2\), and full rank with the **two largest** Schmidt weights equal for \(\log2<\mathcal N<\log3\). Its change of extremizer at \(\mathcal N=\log2\) is sharp. At the endpoint \(\mathcal N=0\), the spectrum is \((1,0,0)\); at \(\mathcal N=\log3\), it is \((1/3,1/3,1/3)\). At both endpoints the interval collapses.

## Assumptions and scope
Write the eigenvalues of either one-cell reduced state, in decreasing order, as \(p_0\ge p_1\ge p_2\ge0\), with \(\sum p_j=1\). Every pure two-qutrit state is permitted: its Schmidt bases need not be energy bases. The total noninteracting Hamiltonian is \(H=h\otimes I+I\otimes h\); there is no restriction to a particular charging trajectory, circuit, or interaction Hamiltonian. All work extraction uses arbitrary global or individual-cell unitaries; no heat bath, catalyst, or coherence restriction is included. The logarithmic negativity uses the natural logarithm of the trace norm of the partial transpose:
\[
\mathcal N=\log\|(|\psi\rangle\langle\psi|)^{T_A}\|_1
=2\log\left(\sqrt{p_0}+\sqrt{p_1}+\sqrt{p_2}\right).
\]
The established pure-state passive-energy identity gives
\[
\mathcal W_{\mathrm{corr}}=2\omega(p_1+2p_2)=2\omega(1-p_0+p_2).
\]
The identity itself is prior work, not a new part of the claim. The new assertion is its complete sharp constrained range and equality/rank classification at **fixed** logarithmic negativity.

## Proof
**1. One-coordinate reduction.** Set \(q_j=\sqrt{p_j}\) and \(z=q_1\). The constraints become \(q_0\ge z\ge q_2\ge0\), \(q_0+z+q_2=s\), and \(q_0^2+z^2+q_2^2=1\). Solving the last two equalities gives
\[
q_0=\frac{s-z+\sqrt{A(z)}}2,\quad
q_2=\frac{s-z-\sqrt{A(z)}}2,\quad
A(z)=2-s^2+2sz-3z^2.
\]
For \(s\in[1,\sqrt3]\), the allowed \(z\) form exactly the closed interval
\[
z_{\rm lo}=\frac{2s-D(s)}6,\qquad
z_{\rm hi}=\begin{cases}
\dfrac{s-\sqrt{2-s^2}}2,&1\le s\le\sqrt2,\\[5pt]
\dfrac{2s+D(s)}6,&\sqrt2\le s\le\sqrt3.
\end{cases}
\]
Indeed the lower endpoint has \(q_1=q_2\); for \(s\le\sqrt2\) the upper endpoint has \(q_2=0\), whereas for \(s\ge\sqrt2\) it has \(q_0=q_1\). No other boundaries are possible under the sorted nonnegative constraints. Conversely the displayed formulas give an admissible ordered triple at every point of this interval.

**2. Unique maximum of the outer spectral spread.** Define \(B(z)=p_0-p_2\). By the preceding formulas,
\[
B(z)=(s-z)\sqrt{A(z)},\qquad
B'(z)=\frac{2(3z^2-3sz+s^2-1)}{\sqrt{A(z)}}.
\]
For \(1<s<\sqrt3\), the derivative polynomial has roots
\[
z_{\pm}=\frac{s}{2}\pm\frac{\sqrt{4-s^2}}{2\sqrt3}.
\]
Only \(z_-=z_*\) is feasible. At the lower endpoint the polynomial equals \((s^2+sD(s)-3)/6>0\), while at the upper endpoint it is \((1-s^2)/2<0\) for \(s\le\sqrt2\) and \((s^2-sD(s)-3)/6<0\) for \(s\ge\sqrt2\). The strict signs and positive leading coefficient show that \(B\) increases to \(z_*\) then decreases. Hence the unique largest spread is \(B_+(s)\), giving the unique smallest ergotropy. The maximizing Schmidt roots \(q_0,q_1,q_2\) are strictly ordered and strictly positive for every \(1<s<\sqrt3\).

**3. Exact minimum of the spread and the rank transition.** Since \(B\) has a single interior maximum, its minimum occurs at an interval endpoint. At \(z_{\rm lo}\) (two smallest roots equal) the spread is
\[
B_{\rm lo}=\frac{sD(s)}3+\frac{D(s)^2}{12}.
\]
For \(\sqrt2\le s\le\sqrt3\), the upper endpoint instead has \(q_0=q_1=(2s+D(s))/6\), \(q_2=(s-D(s))/3\), with spread
\[
B_{\rm hi}=\frac{sD(s)}3-\frac{D(s)^2}{12}.
\]
Thus \(B_{\rm lo}-B_{\rm hi}=D(s)^2/6>0\) in the interior. For \(1<s<\sqrt2\), the upper endpoint has \(q_2=0\) and spread \(B_{\rm hi}=[1+s\sqrt{2-s^2}]/2\). With \(t=\sqrt{2-s^2}\), the difference is
\[
B_{\rm lo}-B_{\rm hi}=\frac{s}{6}\left(2\sqrt{2(1+t^2)}-s-3t\right)>0.
\]
Indeed the two positive quantities in parentheses satisfy
\[
8(1+t^2)-(s+3t)^2=6(1-st)\ge0,
\]
with strict inequality for \(1<s<\sqrt2\), since \(s^2t^2=1-(1-t^2)^2<1\). This proves \(B_-(s)=B_{\rm hi}\) in both regimes and identifies the unique maximizing-ergotropy Schmidt spectrum. The upper extremizer is rank two until \(s=\sqrt2\), then has two equal largest roots. Both formula branches join continuously at \(s=\sqrt2\), where \(q_0=q_1=1/\sqrt2\), \(q_2=0\). The square-root term on the lower-\(s\) branch has an infinite one-sided slope, while the upper-\(s\) branch has a finite slope; consequently the upper ergotropy frontier has a cusp at \(\mathcal N=\log2\).

**4. Endpoints and attainability of the full interval.** At \(s=1\), the only spectrum is \((1,0,0)\), and at \(s=\sqrt3\) it is \((1/3,1/3,1/3)\). The feasible \(z\)-set is a connected compact interval, and \(B(z)\) is continuous. Its image is therefore every number between its proven minimum and maximum, establishing attainability without any dynamics assumption. Each admissible spectrum is realized by \(\sum_jq_j|jj\rangle\), followed if desired by arbitrary local unitaries.

## Verification
The supplied standalone program `verify_frontier.py` independently constructs random local-unitary rotations of pure two-qutrit states and evaluates global work, local passive work, and the trace norm of the full \(9\times9\) partial transpose. On a deterministic grid it checks the exact interval, the equality triples, the rank transition and the one-dimensional feasible-domain parametrization. The executed program reported **72,109 passing assertions**. Finite tests do not establish the continuum theorem; the proof is analytic and relies on the derivative and endpoint comparisons above. The program uses Python 3 and NumPy, and can be run as `python3 verify_frontier.py`.

## Relationship to prior work
Hajizade, Ameri and Askari (2026, arXiv:2610.05592, Sec. III.2) proved the all-pure-state formula \(\mathcal W_{\mathrm{corr}}=2\sum p_ke_k\), specialized it to two equally spaced qutrits, and mapped the locked-energy fraction across the Schmidt simplex. Their separate plots discuss correlation ergotropy versus logarithmic negativity along a particular charger trajectory. Neither the formula nor the simplex plot is claimed new. The full-text study does not give extremal work at **fixed negativity**, equality spectra, the Schmidt-rank transition at \(\log2\), or the strict interior three-distinct-root optimizer derived here.

Alimuddin, Guha and Parashar (2019/2020, arXiv:1912.09780) developed passive-state energy as an entanglement monotone and related it to Schmidt vectors and work; it does not provide the present constrained fixed-negativity qutrit envelopes. Yang et al. (2024, arXiv:2406.13319) relate ergotropic gaps to multipartite entanglement geometry and SLOCC classes rather than this two-qutrit negativity-level frontier. Shi et al. (2022, arXiv:2205.11080) establish relationships among coherence, entanglement and extractable work in battery models, without the sharp two-qutrit constrained spectral calculation. These literature distinctions are by mathematical content, not matching titles.

## Limitations
The result is restricted to *pure* states of two identical qutrits with equally spaced noninteracting local energies and unrestricted unitary work extraction. Mixed states can have nonzero correlation ergotropy at zero negativity and are outside the theorem. These sharp extremal states need not be reachable by any specified charger at a prescribed time or energy; fixed stored energy is not imposed. The source exact ergotropy formula already determines work at each individual spectrum, and the novelty is a new constrained global classification built on that identity, not a new formula for individual spectra. The restricted primary-source search cannot exclude all unpublished or unindexed derivations; external independent publication-priority review remains outstanding.

## References
1. H. Hajizade, V. Ameri, and A. Askari, *Erasure of entanglement-locked energy in multi-cell quantum batteries through decoherence* (first publicly posted 2026-10-04), arXiv:2610.05592, https://arxiv.org/abs/2610.05592, especially Sec. III.2 and Eqs. (8), (12).
2. M. Alimuddin, T. Guha, and P. Parashar, *Independence of work and entropy for equal energetic finite quantum systems: Passive state energy as an entanglement quantifier* (2019), arXiv:1912.09780, https://arxiv.org/abs/1912.09780.
3. X. Yang, Y.-H. Yang, S.-M. Fei, and M.-X. Luo, *Multiparticle entanglement classification with ergotropic gap* (2024), arXiv:2406.13319, https://arxiv.org/abs/2406.13319.
4. H.-L. Shi, S. Ding, Q.-K. Wan, X.-H. Wang, and W.-L. Yang, *Entanglement, Coherence, and Extractable Work in Quantum Batteries* (2022), arXiv:2205.11080, https://arxiv.org/abs/2205.11080.
