# Three-cumulant inversion and a sharp realizability region for thermal telegraph confinement

## Finding

For a symmetric two-state run-and-tumble particle in a harmonic trap with known relaxation rate, the three nonzero consecutive even stationary position cumulants of orders two, four, and six determine **all three unknown physical parameters**: the propulsion speed, the tumbling rate, and the thermal diffusivity. The exact image of the parameter-to-cumulant map is characterized by two sharp inequalities. The first two cumulants never provide locally unique identification when thermal diffusivity is positive.

Write \(K_2,K_4,K_6\) for stationary cumulants; set
\[
R=\frac{K_6^2}{(-K_4)^3},\qquad u=\frac{3R}{800},\qquad
q=\frac{1-8u+\sqrt{1-8u}}{2u}.
\]
The *necessary and sufficient* realizability conditions for strictly positive speed, tumbling rate, and thermal diffusivity are
\[
K_2>0,\qquad K_4<0,\qquad K_6>0,\qquad 0<R<32,
\]
\[
K_2>\sqrt{\frac{(-K_4)(q+2)}6}.
\]
Under these conditions the unique reconstruction is
\[
\lambda=\frac a2(q-1),\quad
v=a\left[q\sqrt{\frac{(-K_4)(q+2)}6}\right]^{1/2},\quad
D=a\left[K_2-\sqrt{\frac{(-K_4)(q+2)}6}\right].
\]
Here \(a>0\) denotes the known harmonic relaxation. If \(D=0\) is permitted, replace the final strict inequality by equality or greater-than, keeping \(\lambda,v>0\). The ratio has a sharp open range \((0,32)\), independent of the thermal diffusivity and speed.

## Assumptions and scope

Let \(a>0\) be known. Consider the stationary one-dimensional process
\[
dX_t=(-aX_t+v S_t)\,dt+\sqrt{2D}\,dB_t,
\]
where \(v>0\) and \(\lambda>0\) are unknown, \(D>0\) is an unknown translational diffusivity, \(B\) is independent standard Brownian motion, and \(S\in\{-1,+1\}\) flips sign at Poisson rate \(\lambda\), independently of \(B\). The two heading states have equal long-run probability. Statements concern **exact population cumulants** of the unique stationary position law, not finite-sample inference. When the stationary system starts in its equilibrium distribution, symmetry gives zero odd cumulants. Position is observed, heading is not. No inertial effect or state-dependent trap is included.

The stationary solution exists uniquely in distribution because the driven linear equation has a pullback stochastic convolution from the infinite past with exponentially integrable coefficients. The propulsion contribution is bounded by \(v/a\), and the Brownian contribution is an independent Gaussian of variance \(D/a\). The full position law has finite moments of all orders.

## Proof

**Step 1: two independent stationary contributions.** With a stationary two-sided heading chain and independent Brownian motion, the stable linear response gives
\[
X_t=v\int_{-\infty}^t e^{-a(t-s)}S_s\,ds+
\sqrt{2D}\int_{-\infty}^t e^{-a(t-s)}\,dB_s.
\]
The second term is centered Gaussian of variance \(D/a\), independent of the first. Set \(c=v/a\) and \(b=\lambda/a\). The dimensionless athermal variable \(Z=(a/v)X^{\mathrm{active}}\) has density proportional to \((1-z^2)^{b-1}\) on \((-1,1)\). This known beta law follows alternatively from the stationarity equations for the two heading-resolved densities, or from the two-state generator below. In particular,
\[
\mathbb E Z^2=\frac1{2b+1},\quad
\mathbb E Z^4=\frac3{(2b+1)(2b+3)},\quad
\mathbb E Z^6=\frac{15}{(2b+1)(2b+3)(2b+5)}.
\]
For an independently Gaussian-smeared variable, all cumulants of orders four and higher are unchanged; the second cumulant gains \(D/a\).

**Step 2: cumulant formulas, including their normalization.** Put \(q=1+2b>1\). From the three beta moments and the cumulant identities
\(K_4=m_4-3m_2^2\) and
\(K_6=m_6-15m_4m_2+30m_2^3\), one obtains
\[
K_2=\frac Da+\frac{c^2}{q},\qquad
K_4=-\frac{6c^4}{q^2(q+2)},\qquad
K_6=\frac{240c^6}{q^3(q+2)(q+4)}.
\]
The independent calculation using the joint Markov generator is as follows. With \(m_n=\mathbb E X^n\) and \(h_n=\mathbb E[SX^n]\), stationarity gives for each positive integer \(n\)
\[
0=-na m_n+nv h_{n-1}+Dn(n-1)m_{n-2},
\]
\[
0=-(na+2\lambda)h_n+nv m_{n-1}+Dn(n-1)h_{n-2}.
\]
Using \(m_0=1,h_0=0\), these equations determine the even moments through degree six exactly and reproduce the displayed cumulants. This supplies a direct independent check of the parameterization and factors.

**Step 3: a sharp and invertible ratio.** Cancellation of the unknown scale \(c\) and Gaussian variance yields
\[
R=\frac{800}{3}\frac{q+2}{(q+4)^2}.
\]
Its derivative is
\[
\frac{dR}{dq}=-\frac{800q}{3(q+4)^3}<0\qquad(q>1).
\]
As \(q\downarrow1\), \(R\uparrow32\); as \(q\to\infty\), \(R\downarrow0\). Neither endpoint is attained with \(\lambda>0\) finite. The map \(q\mapsto R\) is therefore a bijection from \((1,\infty)\) to \((0,32)\). Rearranging \(u(q+4)^2=q+2\) gives the stated positive-branch root. Its second algebraic root is negative on the admissible interval: indeed, \(1-8u-\sqrt{1-8u}<0\) for \(0<u<3/25\), since \(0<1-8u<1\).

**Step 4: sharp parameter reconstruction and sufficiency.** The fourth-cumulant formula gives
\[
\frac{c^2}{q}=\sqrt{\frac{(-K_4)(q+2)}6}.
\]
Therefore the displayed reconstruction is forced, and \(D>0\) is equivalent to the final strict inequality. Conversely, any real cumulant triple meeting the stated inequalities gives \(q>1\), \(v>0\), \(\lambda>0\), and \(D>0\) by those formulas. Substitution into the three cumulant expressions recovers the input triple exactly, proving sufficiency, uniqueness, and the entire feasible region. Boundary equality corresponds precisely to vanishing thermal diffusivity.

**Step 5: failure of two-cumulant identification.** Take any interior parameter triple with \(D>0\). Hold \(K_2,K_4\) fixed and vary \(q\) in a sufficiently small open neighborhood of its true value while keeping \(q>1\). For each nearby \(q\), the same displayed fourth-cumulant formula defines a positive \(c(q)\), and the second-cumulant formula defines \(D(q)=a[K_2-c(q)^2/q]\). Continuity preserves \(D(q)>0\). These are distinct \(\lambda(q)=a(q-1)/2\) yet they produce the identical first two even cumulants. Thus the sixth is the first even cumulant in this ordered hierarchy that restores structural identification without separate calibration of the speed or thermal level.

## Verification

Run `python check_exact.py` with Python 3 and SymPy. The checker assembles the stationary joint-generator recursion through degree six, independently evaluates the three cumulants and their ratio, verifies the ratio derivative and sharp endpoints, and reconstructs the exact rational witness \((a,\lambda,v,D)=(2,3,6,4)\). Its cumulants are
\[
(K_2,K_4,K_6)=\left(\frac{17}{4},-\frac{81}{16},\frac{3645}{64}\right),\qquad R=25,
\]
with inverse \(q=4\) and restored original physical parameters. The proof is algebraic for the full positive parameter domain; finite checks are diagnostics, not a substitute for the sign, monotonicity, and sufficiency arguments.

## Relationship to prior work

Sevilla and Meléndez Mora (2026) prove the exact stationary convolution and derive general forward moment formulas for the **same physical model**, including the second and fourth moments. Guéneau, Majumdar and Schehr (2026) independently provide the stationary distributions and Gaussian-smearing framework for harmonically confined run-and-tumble systems, also including one dimension. Those results imply the forward cumulant formulas after straightforward algebra, and **no novelty is claimed for the stationary distribution, Gaussian convolution, or individual moments/cumulants**. The asserted extension is the exact inverse map of three cumulants, a necessary-and-sufficient semialgebraic/one-radical realizability test, and proof that the lower two cumulants have a continuum of ambiguities with all three physical parameters unknown.

Sun, Ye and Podgornik (arXiv:2409.00578) treat a *different three-state* finite-tumble model with a genuine resting state and forward moments. Other published inverse-moment classifications for that three-state model recover **two internal rates with separately known speed and no thermal Brownian component**; they do not give the stated two-state, three-unknown thermal inverse map. The structural similarity is a significant priority comparison, not evidence of identical parameter models. An unindexed application of classical beta-mixture inverse theory could in principle encompass this exact characterization; independent priority verification remains open.

## Limitations

Only exact stationary population cumulants are treated. The result assumes known trap relaxation \(a\); if \(a\) is unknown, one-time position laws determine dimensionless ratios rather than absolute kinetic time scales. Numerical conditioning worsens when \(R\downarrow0\) (rapid heading switches), and the inverse does not quantify finite-sample error. The result does not cover biased headings, non-Poisson tumbles, unknown instrumental non-Gaussian noise, random propulsion speeds, finite tumble pauses, or spatial dimension greater than one. It makes no claim of an independent scientific audit or publication priority.

## References

1. F. J. Sevilla and J. A. Meléndez Mora, *Nonequilibrium statistics of harmonically trapped run-and-tumble particles: An exact convolution approach*, arXiv:2608.21781, first posted 2026-08-22. https://arxiv.org/abs/2608.21781
2. M. Guéneau, S. N. Majumdar, and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436, first posted 2026-02-09. https://arxiv.org/abs/2602.08436
3. A. Sun, F. Ye, and R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578, first posted 2024-09-01. https://arxiv.org/abs/2409.00578
4. F. J. Sevilla, A. V. Arzola, and E. P. Cital, *Stationary superstatistics distributions of trapped run-and-tumble particles*, Phys. Rev. E 99, 012145 (2019). https://doi.org/10.1103/PhysRevE.99.012145
