# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# 3-subharmonic instability of the even bright soliton on the m=3/4 cnoidal background

## Result (TARGET route; NUMERICAL, non-rigorous finding)
Let `u_cn(x)=1.5*cn^2(x;m=3/4)` (minimal period `L=2K(3/4)=4.3130312950`,
travelling with speed `c=2` under KdV `u_t+u_xxx+6uu_x=0`) and let `u_b(x)`
be the even bright one-soliton on this background from the Bertola-Jenkins-Tovbis
nodal-degeneration formula (genus-2 curve pinched at the midpoint of the finite
gap, Kay-Moses determinant, zero phase shift) at `t=0`, namely the N=1 hot
soliton with Abel parameter `beta1=1/4`, `beta1*=3/4`:

- `G(x) = th3(delta+x/L-A)/(th1(delta)*th3(x/L-A)) * C0 * e^{-3x}`,
  `delta=2*beta1-1=-1/2`, `A=(beta1-beta1*)/2=-1/4`, `C0=th1(-1/2)`,
  `L=2K`, theta functions at `tau=i*K(1/4)/K(3/4)=0.7817i`;
- `u_b(x) = 2 d^2/dx^2 log[(1+G(x))*th3(x/L-A)] + <u_cn>`,
  `<u_cn>=0.6235981733183054`, even, `G(0)=1`, `G>0` everywhere.

The function satisfies: `u_b(-x)=u_b(x)` to 4.2e-15 (analytic theta-series
derivatives), value-continuous on the 3L ring `P=3L=12.9390938850` (value seam
1.1e-15) but only C0 there (derivative jump ~2 from the BJT background phase
shift; see Disclosures), bright hump `u_b(0)=max=3.62543820` versus background
max 1.5, minimum 0.00127.

For perturbations of period P (Floquet exponent mu=0), the linearized KdV
operator `Lambda = -D^3-6*D*M_{u_b}` shows a real eigenvalue pair

- `lambda = +-0.402037` with empirical spread `+-3e-6` from M/N Cauchy ladders
  (imaginary parts < 2e-13 at the finest resolution),

i.e. a convergence-estimated NUMERICAL (explicitly non-rigorous) off-axis
(real, hence non-imaginary) unstable eigenvalue `+0.402037`. At mu=0 all
remaining ring eigenvalues lie on the imaginary axis (max |Re| of rest < 1.6e-11
at N=60). The 3-subharmonic spectrum is therefore, on the numerical evidence,
NOT confined to the imaginary axis. This is NOT an interval certificate and NOT
a rigorous enclosure: see Disclosures.

## Evidence
1. **Background control.** Hill discriminant of `-d^2/dx^2-u_cn` over L gives
   bands `[-0.75,-0.5]`, `[0.25,inf)`, finite gap `(-0.5,0.25)` with midpoint
   `-0.125` (multipliers `{-2.942,-0.340}`). The 3L-Hill spectrum of the bare
   background in the c=2 frame is purely imaginary (N-ladder max|Re| 7e-02 at
   N=10 collapsing to 3.4e-06 at N=40, mu=0 Jordan-block artifact; <=1e-11 at
   all other Bloch phases). Hence the real pair is created by the soliton.
2. **Construction.** BJT Theorem 1.1 (arXiv:2210.01350, eqs. (1.16)-(1.19)),
   N=1, hot branch `beta1=1/4` (midpoint of `(0,1/2)`), `x0=x1(0)=0`. Evenness
   follows the identity `H(x)/H(-x)=1` with `H=(1+G)T e^{3x/2}`, verified
   numerically to 4.2e-15; `G(0)=1` (`th3` values coincide at 0 by symmetry).
3. **Convergence ladder** (`output/artifacts/spectrum_evidence.json`):
   (M,N)=(2048,25): 0.40203374; (4096,25): 0.40203525; (8192,25): 0.40203562;
   (4096,40): 0.40203668; (8192,40): 0.40203706; (8192,60): 0.40203719.
   M- and N-doubling shifts are <=1.4e-6 and shrinking; rest-of-spectrum
   max|Re| stays at 1e-11..1e-12 level throughout. Reported value `+-0.402037`
   with empirical spread `+-3e-6` (about twice the largest observed doubling
   shift); this spread is a convergence heuristic, not a validated bound.
4. **Seam-mollification control** (`output/artifacts/seam_mollification.json`,
   M=8192, N=40, Gaussian mollifier on the periodic extension, kernel full
   widths 0.076/0.303/1.213 in x): pair moves 0.402037 -> 0.402086 ->
   0.402869 -> 0.414675 while the rest stays on-axis (<=6e-12). Narrow
   mollification barely moves the pair, so it is a soliton mode rather than a
   kink artifact; heavy smoothing (width ~1.2, comparable to the background
   wavelength) shifts it by ~3%, as expected when the background itself is
   altered.
5. **Bloch-phase scan** (`output/artifacts/bloch_scan.json`, M=8192, N=30):
   mu=0: +-0.402037 (rest on-axis); mu=0.03: +-0.390109+0.016282i plus further
   off-axis modes (rest 0.242); mu=0.06: +-0.348457+0.033862i (rest 0.243);
   mu=0.09: +-0.269626+0.047204i (rest on-axis); mu=0.12: +-0.121740+0.052960i
   (rest on-axis); mu=0.15: no off-axis pair (all |Re| <= 4.6e-12);
   mu=0.18: +-0.177545+1.828672i (rest on-axis); mu=0.21: +-0.223252+2.000713i
   (rest on-axis); mu=k0/2 (zone edge): +-0.064305+2.201271i. The instability
   is present at most exponents but not all (mu=0.15 is clean at this
   resolution); the target's "one Floquet exponent" is satisfied already at
   mu=0. Note the scan also shows additional off-axis modes at mu=0.03 and
   mu=0.06, so confinement fails there by a wider margin.
6. **Reproducibility.** `output/artifacts/ub_profile.dat` (x, u_b on 8193-point
   ring grid); theta series `q=e^{-pi*0.78170096}=0.08579573`, 161 Fourier
   modes, termwise analytic derivatives; Hill matrices exact Toeplitz FFT.

## Disclosures (uncertainties and limits of this finding)
- **No rigorous certificate.** The `+-3e-6` spread is an empirical Cauchy-ladder
  heuristic, NOT an interval-arithmetic enclosure. The eigenvalue is highly
  non-normal (left/right eigenvector overlap gives condition number ~3e13), so
  Bauer-Fike-type a posteriori bounds are vacuous (crude tail-Frobenius bounds
  are O(1)). A fully rigorous enclosure would need further machinery (e.g.
  validated Evans-function shooting or a validated symmetrizer) beyond this pass.
- **C0 ring profile.** The 3L profile is value-continuous but only C0 at the
  seam point (first-derivative jump ~2 inherited from the BJT background phase
  shift), so Hill convergence is algebraic rather than spectral; the ladder
  accounts for this empirically and the mollification control bounds its effect.
- **Snapshot dynamics.** The computation is in the lab frame about the t=0
  snapshot (the BJT wave is not stationary: background at rest plus soliton
  moving at group velocity V). No convective-versus-absolute dynamical
  interpretation of the moving hump is established here.
- Earlier in this session a transcription error (extra -A shift in the Kay-Moses
  numerator) produced a spurious "no-go" (asymmetry); it was found, corrected,
  and the corrected formula verified even to 1e-15. The WORKLOG records both.
  The prior `output/target_exit_request.json` (REQUEST_TARGET_EXIT) is thereby
  superseded by this TARGET-route result and retained only as audit history.
