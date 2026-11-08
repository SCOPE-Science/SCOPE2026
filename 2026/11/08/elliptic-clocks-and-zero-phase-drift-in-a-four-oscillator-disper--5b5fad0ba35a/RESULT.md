# Elliptic clocks and zero phase drift in a four-oscillator dispersive ring

## Finding
Consider the four-site nearest-neighbor phase oscillator ring at the quadrature phase lag. Its **complete original-time orbit classification** is elementary after an exact reduction, but is not supplied by the cited primary lattice and oscillator-ring studies.

For a nondegenerate conserved opposite-pair phase coordinate \(s\) and a normalized conserved energy \(h\) with \(0<|h|<2\), each relative-phase trajectory is a simple closed curve. Every **full four-phase trajectory** above that curve is also periodic, with *no accumulated common rotation* and with exact minimal period
\[
T(s,h)=\frac{2}{|\sin s|}\,\mathbf K\!\left(\sqrt{1-\frac{h^2}{4}}\right),\qquad
\mathbf K(k)=\int_0^{\pi/2}\frac{du}{\sqrt{1-k^2\sin^2u}}.
\]
For fixed \(\sin s\ne0\), this period strictly decreases as \(|h|\) increases. Its two sharp limits are
\[
\lim_{|h|\to2^-}T(s,h)=\frac{\pi}{|\sin s|},\qquad
T(s,h)=\frac{2}{|\sin s|}\log\frac8{|h|}+o(1)
\quad(|h|\to0).
\]
The only full-phase trajectories that are not equilibria or periodic orbits are the lifts of the nonstationary heteroclinic separatrices at \(h=0\) on nondegenerate leaves. In particular, the four-site endpoint has no aperiodic recurrent motion, despite the conservative dynamics and possible nontrivial dynamics in larger lattices.

## Assumptions and scope
The phase variables \(\theta_j\in\mathbb R/(2\pi\mathbb Z)\), with cyclic indices \(j=1,2,3,4\), obey
\[
\dot\theta_j=\sin\!\left(\theta_{j-1}-\theta_j+\frac\pi2\right)
+\sin\!\left(\theta_{j+1}-\theta_j+\frac\pi2\right)
=\cos(\theta_{j-1}-\theta_j)+\cos(\theta_{j+1}-\theta_j).
\]
All coupling coefficients have been normalized to one; nonzero common coefficients rescale time. There are no heterogeneous natural frequencies. Choose real lifts \(\psi_j=\theta_{j+1}-\theta_j\) satisfying \(\sum_{j=1}^4\psi_j=0\), and define
\[
s=\frac{\psi_1+\psi_3}{2},\quad
x=\frac{\psi_1-\psi_3}{2},\quad
y=\pi+\frac{\psi_2-\psi_4}{2},\quad
h=\cos x+\cos y.
\]
These coordinates have periodic identifications; an allowed change of lifts may replace \((s,x,y)\) by \((s+\pi,x+\pi,y+\pi)\), and thus change \(h\) to \(-h\). The claimed periods depend only on \(|\sin s|\) and \(|h|\), and are unambiguously defined on the original phase torus.

For \(\sin s\ne0\), the reduced critical levels are: a center at each \(h=2\) and \(h=-2\); two saddles at \(h=0\); and four connecting heteroclinic arcs on \(h=0\). There is a single periodic oval per regular level \(0<|h|<2\). On the degenerate leaves \(\sin s=0\), every relative-phase configuration is stationary and the original four phases execute a common rigid rotation (possibly of zero frequency). At the reduced centers and saddles, the four phases likewise execute a rigid rotation (possibly stationary). Thus every nonseparatrix initial condition gives a periodic or stationary full-phase trajectory. This is an assertion about the complete four-site system, not about general ring sizes or nonquadrature phase shifts.

## Proof
**1. Exact reduction and integrals.** Direct subtraction of consecutive oscillator equations gives the four cyclic equations
\[
\dot\psi_j=\cos\psi_{j+1}-\cos\psi_{j-1}.
\]
The identities
\[
(\psi_1,\psi_2,\psi_3,\psi_4)
=(s+x,-s+y-\pi,s-x,-s-y+\pi)
\]
then yield
\[
\dot s=0,\qquad\dot x=-\Omega\sin y,\qquad
\dot y=\Omega\sin x,\qquad \Omega=2\sin s.
\]
The reduced energy \(h=\cos x+\cos y\) is constant; the original conserved Hamiltonian is \(H=\sum_j\sin\psi_j=2\sin s\,h\). Existence of the alternating-sum and Hamiltonian conservation laws for the general dispersive lattice is prior knowledge, not a claimed new discovery here.

**2. Exact phase portrait.** For \(\Omega\ne0\), the reduced system is a two-dimensional Hamiltonian flow on the \((x,y)\)-torus. Its critical points solve \(\sin x=\sin y=0\); their energy values are \(2\), \(-2\), and \(0\). The noncritical level \(h\in(0,2)\) is the sole oval surrounding \((0,0)\); the level \(h\in(-2,0)\) is the sole oval surrounding \((\pi,\pi)\). The zero level is the union of the two circles \(y=\pi+x\) and \(y=\pi-x\) modulo \(2\pi\), intersecting in precisely two saddles, with four heteroclinic arcs. This also classifies all possible relative recurrence.

**3. Exact *minimal* period.** First take \(0<h<2\) and write \(u=(x+y)/2\), \(v=(x-y)/2\). Then \(h=2\cos u\cos v\) and
\[
\dot v=-\Omega\sin u\cos v,
\quad |\dot v|=|\Omega|\sqrt{\cos^2v-h^2/4}.
\]
The turning points of \(v\) are \(\pm\arccos(h/2)\). A full circuit traverses each of the four congruent quarter-arcs exactly once. Hence, with \(k=\sqrt{1-h^2/4}\),
\[
T=\frac4{|\Omega|}\int_0^{\arccos(h/2)}
\frac{dv}{\sqrt{\cos^2v-h^2/4}}
=\frac4{|\Omega|}\int_0^{\pi/2}\frac{dt}{\sqrt{1-k^2\sin^2t}}.
\]
The last equality follows from \(\sin v=k\sin t\). Because the regular energy set is a single simple closed orbit and the vector field never vanishes on it, this circuit time is its minimal positive period. Translation \((x,y)\mapsto(x+\pi,y+\pi)\) converts negative to positive energy and reverses time, leaving the period unchanged.

**4. Vanishing *full-phase* holonomy.** Put \(\chi=(\theta_1+\theta_2+\theta_3+\theta_4)/4\). Summing the original differential equations gives
\[
\dot\chi=\frac12\sum_{j=1}^4\cos\psi_j
=\cos s\,(\cos x-\cos y).
\]
The involution \(R(x,y)=(y,x)\) reverses the reduced vector field and preserves each single regular energy oval. The observable \(\cos x-\cos y\) changes sign under \(R\). Uniform time measure on a periodic oval is invariant under this reversal; therefore its integral over one minimal period is exactly zero. Thus \(\chi(T)-\chi(0)=0\). Since the oval is contractible, the real lifted \(\psi_j\) also return without winding; consequently each \(\theta_j(T)=\theta_j(0)\pmod{2\pi}\). No smaller full-system period is possible because its projection has minimal period \(T\).

**5. Singular limits and remaining trajectories.** The standard elliptic-integral limits \(\mathbf K(0)=\pi/2\) and \(\mathbf K(k)=\log(4/\sqrt{1-k^2})+o(1)\) as \(k\to1^-\) give the two stated limits, including the exact constant \(8\) in the separatrix logarithm. Since \(\mathbf K(k)\) is strictly increasing in \(k\in(0,1)\), the period strictly decreases with \(|h|\). For \(\sin s=0\), the reduced vector field vanishes identically; for \(h=\pm2\) or at either saddle, the reduced state is fixed. In all these cases \(\dot\chi\) is constant, so the original system is a rigid rotation, hence periodic or stationary. Nonstationary heteroclinic orbits have distinct limiting reduced saddles and cannot be periodic. This exhausts the full phase space.

## Verification
The accompanying `verify_phase4.py` performs five symbolic trigonometric-identity checks and numerically integrates the **original four-phase equations** as well as the phase-difference equations for 70 combinations of the conserved coordinates, including both signs of energy and coupling direction. Each numerically observed full-phase return agrees with the claimed exact minimal period. Additional finite checks compare the monotonicity and two asymptotic formulas. Run with `python verify_phase4.py` using Python 3 with SymPy, NumPy, and SciPy. These finite calculations support but do not prove the global results; the preceding algebra, level-set topology, and symmetry arguments do.

## Relationship to prior work
Yan, Ozawa, Kori and Sato (arXiv:2603.02135, first version March 2, 2026; revised July 9, 2026) study the same nearest-neighbor phase-shift ring, emphasizing basin geometry and transient scaling for \(\alpha<\pi/2\), while identifying the conservative boundary. They do not present this exact four-site phase portrait, elliptic minimal period, or full-phase no-drift conclusion.

Rosenau and Pikovsky (2005) explicitly derive the cosine-difference lattice and document its alternating-sum and sine-sum conservation laws, which imply integrability on the four-site reduction. Their analysis instead concerns compactons, waves, and the continuum approximation. Pikovsky (2026) independently treats conservative oscillator-network Hamiltonian structure but not this period and phase-holonomy formula. Thus conserved quantities and the existence of a conservative limit are acknowledged prior facts; the precise complete minimal-period/phase-holonomy classification is the claim compared for originality. The closely related Pikovsky–Rosenau (2006) continuation could be inspected only via its public abstract, leaving residual historical-priority risk.

## Limitations
This theorem applies to exactly four *identical*, equally weighted nearest-neighbor oscillators at the conservative phase shift \(\alpha=\pi/2\). It does not establish integrability for larger rings, perturbative persistence of periodicity at \(\alpha<\pi/2\), or the behavior of the basin riddling discussed in the source paper. It classifies full trajectories only modulo the natural \(2\pi\) phase periodicity. The logarithmic asymptotic holds for fixed \(s\) with \(\sin s\ne0\), not uniformly as \(s\) approaches a frozen leaf. Historical priority needs independent examination of any inaccessible overlapping prior studies; no independent scientific audit has been performed.

## References
1. J. Yan, A. Ozawa, H. Kori, Y. Sato, *Basin Riddling in Coupled Phase Oscillators*, arXiv:2603.02135v1 (March 2, 2026); *Basin Metamorphosis in Coupled Phase Oscillators*, arXiv:2603.02135v2 (July 9, 2026). https://arxiv.org/html/2603.02135v2
2. P. Rosenau, A. Pikovsky, *Phase Compactons in Chains of Dispersively Coupled Oscillators*, Physical Review Letters **94** (2005), 174102, doi:10.1103/PhysRevLett.94.174102.
3. A. Pikovsky, *Conservative dynamics in phase oscillator networks*, Journal of Physics: Complexity **7** (2026), 025008, doi:10.1088/2632-072X/ae669b; arXiv:2603.25431.
4. A. Pikovsky, P. Rosenau, *Phase compactons*, Physica D **218** (2006), 56–69, doi:10.1016/j.physd.2006.04.015 (abstract available; full text not inspected).
