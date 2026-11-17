# Exact Fourier stability windows and re-entrant transverse modes in the ideal-storage lattice

## Finding
For the spatially coupled logistic ideal-storage map, the entire Fourier-mode local stability region of the positive homogeneous fixed point has a closed form. Write \(r=(1+e^{b-5c})^{-1}\), \(d=5c(1-r)\). At mode symbol \(a=1-p+p\mu\), strict stability holds exactly when
\[
-\frac1d-\frac r{2-r}<a<\frac{d^{-1}-r}{1-r}.
\]
In particular, coupling cannot create a linear instability of a locally exponentially attracting homogeneous equilibrium: all diffusion strengths are stable when \(d<1\). For \(d>1\), the homogeneous mode is unstable for every coupling strength, yet a transverse stripe mode can regain and then lose stability as coupling increases. The exact example \(r=1/4\), \(d=3\), and \(\mu=-1/2\) has stability window \(16/27<p<62/63\).

## Assumptions and scope
Let \(H,W\ge4\) be integers; sites are indexed modulo \(H,W\). Each site carries \(S_i>0\) and \(0<R_i<1\). At each synchronous discrete step,
\[
S_i^+=S_i(1-R_i)+c,\qquad
R_i^+=\frac1{1+\exp(b-5S_i\bar R_i)},\qquad
\bar R_i=(1-p)R_i+\frac p8\sum_{j\sim i}R_j,
\]
where \(j\sim i\) ranges over eight distinct Moore neighbors, \(c>0\), \(b\in\mathbb R\), and \(0\le p\le1\). A mode is called strictly stable if both eigenvalues of its linearized two-dimensional Fourier block have modulus strictly below one. For a nonhyperbolic parameter boundary, no claim about nonlinear attraction is made.

## Proof
**1. Unique homogeneous equilibrium.** The first fixed-point equation gives \(S_*r=c\). The second therefore gives \(r=(1+e^{b-5c})^{-1}\) uniquely and \(S_*=c/r\). Put \(d=5c(1-r)>0\).

**2. Exact Fourier blocks.** The eight-neighbor averaging operator has symbol
\[
\mu_{jk}=\frac{(1+2\cos(2\pi j/H))(1+2\cos(2\pi k/W))-1}8,
\qquad 0\le j<H,\;0\le k<W.
\]
Because each factor \(1+2\cos\) belongs to \([-1,3]\), all symbols lie in \([-1/2,1]\); \(\mu_{00}=1\) and all other symbols are less than one. With \(a=1-p+p\mu_{jk}\), direct differentiation of the *simultaneous* update at the fixed point gives
\[
J_a=\begin{pmatrix}1-r&-c/r\\5r^2(1-r)&da\end{pmatrix},\qquad
T_a=1-r+da,\quad D_a=d\bigl(r+(1-r)a\bigr).
\]

**3. Sharp stability inequalities.** For a real quadratic multiplier polynomial \(z^2-T_a z+D_a\), the strict Schur criterion is \(1-D_a>0\), \(1-T_a+D_a>0\), and \(1+T_a+D_a>0\). Here
\[
1-T_a+D_a=r\bigl(1+d(1-a)\bigr)>0
\]
for every physical \(a\le1\). The other two conditions are exactly
\[
a<\frac{d^{-1}-r}{1-r},\qquad
 a>-\frac1d-\frac r{2-r}.
\]
This proves the if-and-only-if statement for each Fourier mode. The two bounds may be reversed for very large \(d\); then no mode satisfies them.

**4. No stable-homogeneous-state diffusion instability.** If \(d<1\), the upper bound exceeds \(1\). The lower bound is less than \(-1\), whereas \(a\ge-1/2\). Every Fourier block is strictly stable for all \(p\). If \(d>1\), the uniform block has \(a=1\) for all \(p\) and violates \(1-D_a>0\) since \(D_1=d\); hence the full equilibrium is linearly unstable. At \(d=1\), the uniform block has \(D_1=1\) and \(T_1=2-r\in(1,2)\), hence a conjugate unit-circle multiplier pair. If \(p>0\), every nonuniform mode has \(a<1\) and \(a\ge-1/2\); it satisfies both strict inequalities.

**5. Genuine transverse re-entrance.** Choose \(r=1/4\), \(d=3\), equivalently \(c=4/5\), \(b=4+\log3\). For an even-height torus, the stripe mode \((j,k)=(H/2,0)\) has \(\mu=-1/2\) and \(a=1-3p/2\). Its strict bounds simplify to \(-10/21<a<1/9\), or
\[
\frac{16}{27}<p<\frac{62}{63}.
\]
At smaller \(p\) the mode violates \(1-D_a>0\), while at larger \(p\) it violates \(1+T_a+D_a>0\), passing a negative-unit-multiplier boundary (the other multiplier is \(9/28\)). The entry threshold has determinant \(1\) and trace \(13/12\), while the exit has eigenvalues \(-1\) and \(9/28\). Throughout, the full equilibrium has its unstable uniform block. This is *mode-specific* stabilization and destabilization, not stabilization of the full equilibrium.

## Verification
Run `python verify_modes.py` using Python 3 (standard library only). It tests 29,804 modal eigenvalue/Schur comparisons over four sizes and multiple physical parameters, the exact rational stripe boundaries, and centered finite-difference derivatives of the nonlinear cell map against four independent Fourier blocks. Expected output: `VERIFY_OK mode_samples=29804 finite_difference_modes=4 exact_window=(16/27,62/63)`. The proof above, rather than the finite tests, establishes the universal claim.

## Relationship to prior work
Hordijk (2026) numerically documents spontaneous spirals in the coupled lattice, using isolated-oscillator bifurcation diagrams, but does not provide this full lattice Fourier-mode stability criterion. Dress, Hordijk, Lin and Serocka (2010) introduced the Moore-coupled model and examined spatial patterns; their eight-page primary article contains the coupling formula and simulations, but no Fourier-mode spectrum in the spatial-analysis section. Dress and Lin (2011) derived stability and Neimark–Sacker behavior for the **uncoupled** two-dimensional storage map, so its fixed-point Schur condition is acknowledged as prior, not claimed new. The asserted contribution is the *coupled lattice* all-mode classification together with the exact re-entrant stripe window. General use of Fourier decomposition and the Schur test is standard.

## Limitations
The statements are about local linear multipliers (and local exponential attraction when all multipliers have modulus below one). They do not prove existence, stability, or destruction of spirals, identify global attractors, or classify nonlinear dynamics exactly at the neutral boundaries. Re-entrant stability belongs to a transverse Fourier block while the full homogeneous state remains unstable. The lattice has periodic boundaries and at least four sites per direction. Historical priority against unlocated specialized work on this exact lattice remains provisional.

## References
1. W. Hordijk, *Spontaneous Spirals in Spatial Systems*, arXiv:2610.38710v1 (2026), https://arxiv.org/html/2610.38710v1; first publicly posted 2026-10-28 UTC.
2. A. Dress, W. Hordijk, W. Lin and P. Serocka, *The Ideal Storage Cellular Automaton Model*, Dagstuhl Seminar Proceedings 10231 (2010), DOI:10.4230/DagSemProc.10231.8, https://drops.dagstuhl.de/storage/16dagstuhl-seminar-proceedings/dsp-vol10231/DagSemProc.10231.8/DagSemProc.10231.8.pdf.
3. A. Dress and W. Lin, *Dynamics of a Discrete-Time Model of an “Ideal-Storage” System Describing Hetero-Catalytic Processes on Metal Surfaces*, International Journal of Bifurcation and Chaos 21 (2011), 1331–1339, DOI:10.1142/S0218127411029197, https://www.researchgate.net/publication/220272976_DYNAMICS_OF_A_DISCRETE-TIME_MODEL_OF_AN_IDEAL-STORAGE_SYSTEM_DESCRIBING_HETERO-CATALYTIC_PROCESSES_ON_METAL_SURFACES.
