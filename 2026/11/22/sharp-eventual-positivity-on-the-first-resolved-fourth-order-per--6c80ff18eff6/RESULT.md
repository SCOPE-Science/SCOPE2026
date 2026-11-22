# Sharp eventual positivity on the first resolved fourth-order periodic heat grid

## Finding

For the standard centered five-point fourth-order spatial discretization of one-dimensional heat flow on a periodic grid of five nodes, exact semidiscrete evolution has a **single, sharp positivity-restoration time**, with no later sign reentry. A nonnegative point mass initially creates negative values at precisely its two cyclic distance-two neighbors, although the generator is symmetric negative semidefinite and mass preserving.

Let \(S\) be the cyclic shift on five coordinate positions, let \(I\) be the identity, and put
\[
D=S+S^{-1}-2I,\qquad Q=D-\frac1{12}D^2
=-\frac52I+\frac43(S+S^{-1})-\frac1{12}(S^2+S^{-2}).
\]
The matrix \(Q\) is the dimensionless classical fourth-order five-point central-difference Laplacian on the five-node periodic grid, the **smallest periodic grid with five distinct stencil positions**. Let \(E(t)=e^{tQ}\) for dimensionless time \(t\ge0\), and define
\[
\varphi=\frac{1+\sqrt5}{2},\quad
\alpha=\frac{75-17\sqrt5}{24},\quad
\beta=\frac{75+17\sqrt5}{24}.
\]
There is a unique \(T>0\) solving
\[
\boxed{1-\varphi e^{-\alpha T}+\varphi^{-1}e^{-\beta T}=0.}
\]
Its value is \(T=0.1030787110077426622381848633844554940\ldots\). For every real \(t>0\), the entries of \(E(t)\) obey the following complete sign law:

* **\(0<t<T\):** exactly ten entries are strictly negative, namely the two cyclic distance-two entries in each of the five rows; all other fifteen entries are strictly positive.
* **\(t=T\):** exactly those ten entries are zero, and the other fifteen are strictly positive.
* **\(t>T\):** every entry is strictly positive.

At \(t=0\) the propagator is the identity. Thus its exact entrywise-nonnegativity times are \(\{0\}\cup[T,\infty)\). In physical units with diffusivity \(\kappa>0\) and mesh spacing \(h>0\), the restoration time is \(Th^2/\kappa\).

## Assumptions and scope

The model has exactly five equally spaced *periodic* nodes, no boundary closure, constant positive diffusivity and the classical five-point central-difference stencil. The five shift positions \(0,\pm1,\pm2\) are distinct modulo five; for smaller periodic meshes the stencil aliases. The time integrator is **exact**: the object is the semidiscrete matrix exponential, not forward Euler, backward Euler or a Runge--Kutta approximation. “Entrywise nonnegative” means that **every** nonnegative nodal vector remains nonnegative under that propagator at that particular time. All signs and thresholds refer to exact real arithmetic.

The stability property is independent of the entrywise signs: \(Q\mathbf1=0\), the spectrum of \(Q\) is nonpositive, and \(\|E(t)\|_2\le1\) for every \(t\ge0\). Row sums of \(E(t)\) are exactly one.

## Proof

**1. Spectral resolution.** The cyclic shift diagonalizes in the five-point discrete Fourier basis, where \(D\) has eigenvalue \(-4\sin^2(\pi k/5)\) in frequency \(k=0,1,2,3,4\). Substituting into \(Q=D-D^2/12\), one obtains
\[
\operatorname{spec}(Q)=\{0,-\alpha,-\alpha,-\beta,-\beta\},
\]
with \(\alpha,\beta\) as stated and \(0<\alpha<\beta\). Thus the exact Fourier inversion yields, with indices interpreted modulo five, precisely three distinct entries in each row:
\[
E_{j,j}(t)=\frac15\left(1+2e^{-\alpha t}+2e^{-\beta t}\right),
\]
\[
E_{j,j\pm1}(t)=\frac15\left(1+\varphi^{-1}e^{-\alpha t}-\varphi e^{-\beta t}\right),
\]
\[
E_{j,j\pm2}(t)=\frac15\left(1-\varphi e^{-\alpha t}+\varphi^{-1}e^{-\beta t}\right).
\]
For example, the Fourier cosine values \(2\cos(2\pi/5)=\varphi^{-1}\) and \(2\cos(4\pi/5)=-\varphi\) give the first-neighbor and second-neighbor coefficients and show that each frequency pair contributes multiplicity two.

**2. Diagonal and nearest-neighbor signs.** The diagonal formula is positive for every \(t\ge0\). For \(t>0\), let \(u=e^{-\alpha t}\), \(v=e^{-\beta t}\). Since \(0<v<u<1\) and \(\varphi-\varphi^{-1}=1\),
\[
5E_{j,j\pm1}(t)=1+\varphi^{-1}u-\varphi v
=(1-u)+\varphi(u-v)>0.
\]

**3. Exact number of second-neighbor sign changes.** Put
\[
F(t)=5E_{j,j\pm2}(t)=1-\varphi e^{-\alpha t}+\varphi^{-1}e^{-\beta t}.
\]
The initial value is \(F(0)=1-\varphi+\varphi^{-1}=0\), and differentiation gives
\[
F'(t)=\varphi\alpha e^{-\alpha t}-\varphi^{-1}\beta e^{-\beta t}.
\]
The exact stencil coefficient \(Q_{j,j\pm2}=-1/12\) implies \(F'(0)=5Q_{j,j\pm2}=-5/12<0\). Since \(\beta>\alpha\), the ratio of the positive terms in \(F'(t)\) increases strictly with \(t\). Consequently \(F'\) has exactly one zero, at
\[
t_{\min}=\frac{\log\left(\beta/(\varphi^2\alpha)\right)}{\beta-\alpha}>0.
\]
It is negative before this point and positive afterward. Hence \(F\) decreases from zero to a strictly negative minimum, then increases strictly to \(\lim_{t\to\infty}F(t)=1\). By continuity and strict monotonicity after its minimum, it has one and only one positive zero \(T>t_{\min}\), with \(F<0\) on \((0,T)\) and \(F>0\) on \((T,\infty)\).

**4. All entries and sharpness.** Each row contains one diagonal entry, two distance-one entries, and two distance-two entries. Steps 2--3 therefore give exactly ten negative entries before \(T\), exactly ten zero entries at \(T\), and strict positivity after \(T\), proving the full sign law. Taking the initial unit point mass at any grid node exhibits the failure of positivity for every \(0<t<T\). As \(Q\) is symmetric with spectrum in \(( -\infty,0]\), its semigroup is Euclidean nonexpansive, and the zero-mode projector ensures row sums one. Neither property prevents the transient negative entries.

## Verification

The standalone script `artifacts/verify_five_cycle.py` uses exact symbolic arithmetic to reconstruct the five-by-five stencil, its eigenvalues, its spectral projectors and all three Fourier formulas. It also checks the exact derivative identity \(F'(0)=-5/12\). At 70-digit precision, it compares direct matrix exponentials against the independently assembled spectral resolution over 220 positive times, checks mass conservation and entrywise sign patterns, and computes \(t_{\min}=0.048778362704582189316052668514211104\ldots\) and \(T\) to high precision. The run returned **7,260 successful numerical comparisons** plus the exact symbolic assertions. The complete all-time sign assertion does **not** follow from sampled matrix exponentials; it is proved analytically in Step 3.

Reproduce with `python artifacts/verify_five_cycle.py` after installing the packages specified in `requirements.txt`. The console output of the actual run is retained at `artifacts/checks.txt`.

## Relationship to prior work

The classical centered fourth-order stencil itself is standard. Hu and Zhang [1] develop positivity-preserving finite difference schemes obtained from Gauss--Lobatto finite elements; the fourth-order spatial operator and fully discrete positivity conditions analyzed there differ from this classical circulant signed generator and its **exact semidiscrete** propagator.

Chen and collaborators [2, Section VI] establish broad connections between signed Laplacian spectra and eventual exponential positivity. Their general finite-dimensional eventual-positivity principle predicts eventual recovery when the zero eigenvalue is simple, but does not give this exact five-node restoration time, the unique crossing, or the complete ten-entry sign census.

An existing analysis of negative outer couplings in symmetric finite-range diffusion [4] studies **the same classical five-point stencil**. It proves infinite-lattice sign oscillation for all positive times and eventual finite-periodic positivity, with a quantitative large-cycle delay and a nonsharp upper bound on recovery time. Its full statement expressly does not claim **a sharp finite-cycle recovery time**. The exact first unaliased five-node classification here is a distinct finite-size answer, not a new assertion of qualitative eventual positivity. A separate backward-Euler resolvent positivity classification [5] also involves the same stencil but a different operator, \((I-tQ)^{-1}\) rather than \(e^{tQ}\); neither its infinite-grid lower-step threshold nor its rational kernel signs imply the exponential-time threshold here.

Cross and Zhang [3, Section 2.2] discuss classical high-order discrete elliptic stencils and inverse positivity, which is distinct from time-by-time entrywise positivity of a matrix exponential. The Fourier method and eventual-positivity concepts are not claimed to be new. The contribution assessed here is the **exact, sharp first-resolved-grid sign and restoration classification**. Earlier finite-difference work may contain this concrete small-grid calculation under another description; the accessible sources do not establish a statement covering it.

## Limitations

The result is exact for a **five-node periodic mesh only**. It neither gives the sharp restoration time for other mesh sizes nor an optimal physical continuum recovery scale. It does not extend to nonperiodic boundaries, variable coefficients, higher spatial dimensions, or full time integrators without additional work. The threshold and signs are invariant under cyclic permutation, and at its root some entries are zero rather than strictly positive. This is a narrow motivated boundary benchmark, not a general theorem about every high-order spatial discretization. An older equivalent specialization could still exist; independent historical-priority validation has not been performed.

## References

1. J. Hu and X. Zhang, *Positivity-preserving and energy-dissipative finite difference schemes for the Fokker--Planck and Keller--Segel equations*, arXiv:2103.16790, first made public 2021-03-31, especially Sections 2 and 3.5, https://arxiv.org/html/2103.16790v2 .
2. W. Chen et al., *On Spectral Properties of Signed Laplacians with Connections to Eventual Positivity*, arXiv:2009.03581, first made public 2020-09-08, especially Section VI, https://arxiv.org/html/2009.03581v1 .
3. L. J. Cross and X. Zhang, *On the monotonicity of Q3 spectral element method for Laplacian*, arXiv:2010.07282, first made public 2020-10-14, especially Section 2.2, https://arxiv.org/html/2010.07282v3 .
4. *Negative outer jumps force persistent lattice sign oscillation and a linear cycle-positivity delay*, research record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-negative-outer-jumps-force-persistent-lattice-sign-oscillation-a--904e3c4eba47 .
5. *One third is the sharp positivity-recovery threshold for backward Euler on the classical fourth-order heat stencil*, research record, 2026-10-12, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-one-third-is-the-sharp-positivity-recovery-threshold-for-backwar--f6b8d51838a7 .
