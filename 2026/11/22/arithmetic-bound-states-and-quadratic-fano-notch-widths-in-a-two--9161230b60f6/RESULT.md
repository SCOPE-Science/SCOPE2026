# Arithmetic bound states and quadratic Fano-notch widths in a two-arm quantum stub

## Finding
Attach a branching finite pendant to one site of an otherwise uniform one-dimensional tight-binding lead. The pendant consists of a root and two paths with \(m,n\ge1\) vertices. A weak uniform onsite shift on one arm splits every common arm eigenfrequency into two **perfect-transmission energies**, separated by one **zero-transmission notch** whose half-width is quadratic in that shift. Both the count of these features and their sharp width constants are explicit in the arm lengths.

Set \(d=\gcd(m+1,n+1)\). At zero detuning there are exactly \(d-1\) compact eigenstates embedded in the lead band, at
\[
E_s=2\cos\theta_s,\qquad \theta_s=\frac{\pi s}{d},\quad 1\le s<d.
\]
Each energy is a perfect-transmission energy. For every fixed \(s\), at all sufficiently small \(\delta>0\) there is one and only one fully reflecting energy \(E_{*,s}(\delta)\) between the two exactly transparent energies \(E_s\) and \(E_s+\delta\). It has expansion
\[
E_{*,s}(\delta)=E_s+\frac{n+1}{m+n+2}\delta+O_{m,n,s}(\delta^2).
\]
Let \(E_{-,s}(\delta)<E_{*,s}(\delta)<E_{+,s}(\delta)\) be the two local energies of transmission probability \(1/2\). Then
\[
E_{*,s}-E_{-,s}\sim E_{+,s}-E_{*,s}\sim\Gamma_{m,n,s}\delta^2,\qquad
\Gamma_{m,n,s}=\frac{(m+1)^2(n+1)^2}{4(m+n+2)^3\sin^3(\pi s/d)}.
\]
For every fixed real \(x\), the reflection probability in the scaling window satisfies
\[
\mathcal R_\delta\big(E_{*,s}(\delta)+\Gamma_{m,n,s}\delta^2x\big)\longrightarrow\frac{1}{1+x^2}.
\]
The two-arm graph with \(m=n=1\) is the smallest illustration: \(E_s=0\), the notch center is \(\delta/2+O(\delta^2)\), and the half-width is asymptotic to \(\delta^2/16\).

## Assumptions and scope
On \(\ell^2(\mathbb Z)\), use nearest-neighbor hopping amplitude \(+1\) and no onsite potentials. Attach a separate root vertex \(r\) to lead vertex \(0\) with hopping \(+1\). Attach two disjoint paths of \(m\) and \(n\) vertices to \(r\), again using hopping \(+1\); the endpoints adjacent to the root have path coordinate \(1\). Every vertex in the second path carries onsite potential \(\delta\), and every other vertex carries onsite potential \(0\). All couplings are real and conservative; there are no losses, interactions, or additional leads. Incoming plane waves have energy \(E=2\cos k\), where \(0<k<\pi\) and \(-2<E<2\). Transmittance \(\mathcal T=|t|^2\) and reflectance \(\mathcal R=1-\mathcal T\) refer to this single propagating channel. Both arm lengths are fixed before taking \(\delta\downarrow0\).

Write \(U_j\) for the Chebyshev polynomial of the second kind, with \(U_{-1}=0\), \(U_0=1\). Define the rational endpoint resolvent of a path by
\[
G_j(E)=\frac{U_{j-1}(E/2)}{U_j(E/2)},\qquad H(E,\delta)=E-G_m(E)-G_n(E-\delta).
\]
At energies away from the finite-path eigenvalues, the exact transmission is
\[
\mathcal T_\delta(E)=\frac{(4-E^2)H(E,\delta)^2}{1+(4-E^2)H(E,\delta)^2}.
\]
Its continuous physical scattering limit at a simple pole of \(H\) is \(1\). At \(\delta=0\), coincident poles are treated by the same limit; an independent embedded compact eigenvector may coexist with the scattering solution.

## Proof
**1. Finite resolvents and scattering.** The characteristic polynomial \(P_j(E)\) of a length-\(j\) path satisfies \(P_0=1\), \(P_1=E\), \(P_j=EP_{j-1}-P_{j-2}\); thus \(P_j=U_j(E/2)\). Cramer's rule gives the endpoint Green function \(G_j=P_{j-1}/P_j\). Eliminating the two arms in the eigenvalue equation at the side root yields root response \(r=\psi_0/H(E,\delta)\). Eliminating that root yields the effective lead-site potential \(V_{\mathrm{eff}}=H^{-1}\). Matching the left and right lead plane waves across a point potential gives \(\mathcal T=4\sin^2 k/[4\sin^2 k+V_{\mathrm{eff}}^2]\), which is the displayed exact formula.

**2. Compact eigenstates and the arithmetic criterion.** An embedded square-summable state has zero wavefunction on the uniform lead. The lead equation at vertex \(0\) then forces the side-root amplitude to vanish. Each nonzero arm amplitude consequently solves a Dirichlet path eigenproblem. A single arm cannot support such a state alone: its endpoint eigenvector component is nonzero, and the root equation requires the two endpoint amplitudes to cancel. The two arm spectra are \(2\cos(\pi j/(m+1))\) and \(2\cos(\pi k/(n+1))\); equality is equivalent to \(j/(m+1)=k/(n+1)=s/d\), with \(1\le s<d\). At each common eigenvalue the endpoint-cancellation equation cuts the two-dimensional common eigenspace to one dimension. Thus there are exactly \(d-1\) compact bound states and no others. The common energy produces a pole in each \(G_j\), both with positive residue, and hence \(\mathcal T_0(E_s)=1\) by the limiting scattering formula.

**3. A unique zero between two exact transparency points.** The spectral decomposition of the path resolvent is
\[
G_j(E)=\sum_{k=1}^j\frac{a_{j,k}}{E-2\cos(\pi k/(j+1))},\qquad a_{j,k}=\frac{2\sin^2(\pi k/(j+1))}{j+1}>0.
\]
Fix a common energy \(E_s\). For sufficiently small positive \(\delta\), no other arm eigenvalue lies in \((E_s,E_s+\delta)\). The simple poles at its endpoints make \(\mathcal T_\delta(E_s)=\mathcal T_\delta(E_s+\delta)=1\). On the intervening open interval \(H\) is differentiable, and
\[
\frac{\partial H}{\partial E}=1- G_m'(E)-G_n'(E-\delta)=1+\sum\frac{a_{m,k}}{(E-\lambda_{m,k})^2}+\sum\frac{a_{n,k}}{(E-\delta-\lambda_{n,k})^2}>0.
\]
Furthermore \(H(E,\delta)\) tends to \(-\infty\) at the left endpoint and \(+\infty\) at the right endpoint. It therefore has exactly one zero there. Since \(H=0\) makes the effective point potential infinite, transmission vanishes exactly at that unique zero.

**4. Notch position and sharp linewidth.** The two positive endpoint residues at \(E_s\) are
\[
a=\frac{2\sin^2\theta_s}{m+1},\qquad b=\frac{2\sin^2\theta_s}{n+1}.
\]
Uniformly when \(E-E_s\) is a fixed nonendpoint fraction of \(\delta\),
\[
H(E,\delta)=E-\frac{a}{E-E_s}-\frac{b}{E-E_s-\delta}+O(1).
\]
The unique root therefore has \(E_{*,s}-E_s=a\delta/(a+b)+O(\delta^2)\), giving the stated length ratio. Direct differentiation at the root gives
\[
H'(E_{*,s},\delta)=\frac{(a+b)^3}{ab\,\delta^2}+O(\delta^{-1}).
\]
Its inverse slope divided by the waveguide velocity factor \(\sqrt{4-E_s^2}=2\sin\theta_s\) is the half-height scale
\[
\frac{ab}{2\sin\theta_s\,(a+b)^3}\delta^2=\Gamma_{m,n,s}\delta^2.
\]
Since \(H'\) is of order \(\delta^{-2}\) throughout this interval whereas the derivative of \((4-E^2)^{-1/2}\) remains bounded, the two equations \(H=\pm(4-E^2)^{-1/2}\) have exactly one solution each for small enough \(\delta\). A Taylor expansion on the \(\delta^2\)-scale gives \(H(E_{*,s}+\Gamma\delta^2 x,\delta)\to x/(2\sin\theta_s)\); substitution into the exact transmission formula proves the universal Lorentzian reflection limit.

## Verification
A standalone exact-and-numerical script is embedded as `verify.py`. It confirms 24 exact rational path-resolvent identities against independently inverted finite path matrices; eight polynomial-gcd degree checks; 28 complete complex scattering solutions obtained directly from boundary matching on the full pendant (independent of the reduced scattering formula), with probability conservation; and 16 notch-position and half-width asymptotic tests for varied nonidentical and identical arm lengths. Execution output is `ALL_CHECKS_PASSED exact_resolvents=24 gcd_bics=8 direct_scattering=28 width_asymptotics=16`. The general theorem rests on the symbolic argument above, not on finite tests. Reproduce with `python verify.py` using Python 3, SymPy, NumPy and SciPy.

## Relationship to prior work
Fano interference and zeroes of transmission on quantum wires with one side-attached finite or quasiperiodic chain are established in Chakrabarti (2006); his finite-chain decimation is an important precursor, not the two-arm-root arithmetic or its linewidth formula. The unified scattering formalism of Gorbatsevich and Shubin (2017) treats arbitrary Hermitian devices and BICs, but its general determinant criteria do not state the present exact greatest-common-divisor count, length-ratio displacement, or explicit linewidth coefficient. Petráček and Kuzmiak (2022) study two **direct** single-site attachments to the propagating wire, where the side energies are transmission **zeroes** rather than the transmission **ones** created here by the additional root. Kuo, Chen and Chen (2016) analyze different common-cavity quantum-dot networks, supporting the broader Fano mechanism but not the all-size two-path arithmetic. Existing finite-spider dark-mode counts and compact Fano-mode leakage laws concern different observables or geometries; their overlap is at the BIC mechanism and quadratic scaling, not this complete explicit scattering-window classification.

## Limitations
The bound-state count, zero positions, and linewidth constants assume exactly unit hopping, a single common root, two path arms, and an onsite detuning uniform across one whole arm. The asymptotic estimates are pointwise for fixed lengths and fixed common-mode index; no uniform-in-size estimate is asserted. Nonzero absorption generally prevents exact unit transmission and perfect reflection. The mechanism of symmetry-protected BICs, Fano resonances, and generic quadratic leakage is previously known: only the specified arithmetic and exact coefficient classification is assessed as a candidate new specialization. Earlier equivalent or stronger work outside the inspected literature remains a priority risk; no external independent audit is implied.

## References
1. A. Chakrabarti, *Electronic transmission in a model quantum wire with side-coupled quasiperiodic chains: Fano resonance and related issues*, arXiv:cond-mat/0609082 (first submitted 2006-09-05), https://arxiv.org/abs/cond-mat/0609082 .
2. A. A. Gorbatsevich and N. M. Shubin, *Unified theory of resonances and bound states in the continuum in Hermitian tight-binding models*, arXiv:1707.05531 (2017), https://arxiv.org/abs/1707.05531 .
3. J. Petráček and V. Kuzmiak, *Bound states in the continuum in waveguide arrays within a symmetry classification scheme*, *Optics Express* **30**, 35712–35724 (2022), https://doi.org/10.1364/OE.464599 .
4. P.-C. Kuo, G.-Y. Chen and Y.-N. Chen, *Scattering of nanowire surface plasmons coupled to quantum dots with azimuthal angle difference*, *Scientific Reports* **6**, 37766 (2016), https://doi.org/10.1038/srep37766 .
