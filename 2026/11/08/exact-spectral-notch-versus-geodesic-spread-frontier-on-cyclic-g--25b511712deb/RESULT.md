# Exact spectral-notch versus geodesic-spread frontier on cyclic groups

## Finding

For every integer \(N\ge3\), the complete sharp tradeoff between a nonnegative mass distribution's first cyclic Fourier coefficient and its squared graph-distance spread is a piecewise-affine curve. Its breakpoints are the sampled cosines, and its minimizers have mass on at most two adjacent graph-distance shells, with an explicit one-parameter family of possible asymmetries.

Write \(G=\mathbb Z/N\mathbb Z\) and let \(\mu:G\to[0,1]\) satisfy \(\sum_{j\in G}\mu(j)=1\). Define
\[
 z(\mu)=\sum_{j\in G}\mu(j)e^{2\pi i j/N},\qquad
 d_N(j,a)=\min\{(j-a)\bmod N,(a-j)\bmod N\},
\]
\[
 V_N(\mu)=\min_{a\in G}\sum_{j\in G}\mu(j)d_N(j,a)^2.
\]
For \(0\le\rho\le1\), set
\[
 F_N(\rho)=\min\{V_N(\mu):\mu\ge0,\ \sum_j\mu(j)=1,\ |z(\mu)|\le\rho\}.
\]
Let \(c_j=\cos(2\pi j/N)\) for \(0\le j\le\lfloor N/2\rfloor\). Select an index \(k\) with \(0\le k<\lfloor N/2\rfloor\) and \(c_k\ge\rho\ge c_{k+1}\). At a breakpoint either adjacent admissible choice yields the same value. Set
\[
 W_k=\frac{\rho-c_{k+1}}{c_k-c_{k+1}},\qquad
 W_{k+1}=\frac{c_k-\rho}{c_k-c_{k+1}}.
\]
Then the exact optimum is
\[
 \boxed{F_N(\rho)=W_k k^2+W_{k+1}(k+1)^2.}
\]
In particular, the profile is continuous, strictly decreasing, and piecewise affine, with genuine corners at every sampled \(c_j\in(0,1)\).

Every minimizer is obtained as follows. Choose a center \(a\in G\). Assign total mass \(W_k\) to the shell \(d_N(j,a)=k\) and mass \(W_{k+1}\) to the shell \(d_N(j,a)=k+1\), with no other mass. Within these shells, require the sine-balance condition
\[
 \sum_{j\in G}\mu(j)\sin(2\pi(j-a)/N)=0.
\]
Here a zero-radius shell is the singleton \(a\), and a shell of radius \(N/2\), when present, is also a singleton. These conditions are necessary and sufficient; in particular the two signs at each nonsingleton radius need not have equal weights. Reflection-symmetric minimizers always exist. On a non-breakpoint segment with both radii positive, the allowable asymmetries form a compact interval and its endpoints use at most three sites. At a breakpoint only one radius carries mass, equally split between its two signs when they are distinct.

The zero-notch case has a sharp arithmetic quantization effect:
\[
 F_N(0)\ge N^2/16,
\]
with equality exactly when \(4\mid N\). In the other even congruence class, the precise gap is
\[
 \boxed{F_N(0)=N^2/16+1/4\quad\text{if }N\equiv2\pmod4.}
\]
For odd \(N\), the displayed general cosine-interpolation formula gives the exact strictly positive gap. As \(N\to\infty\) with \(N\equiv1\) or \(3\pmod4\), this gap tends to \(3/16\).

A quantitative **exact defect identity** accompanies the optimum. For an admissible \(k\), put
\[
 \beta=\frac{(k+1)^2-k^2}{c_{k+1}-c_k}<0,\qquad
 \alpha=k^2-\beta c_k,\qquad
 H(j)=d_N(j,0)^2-\alpha-\beta\cos(2\pi j/N).
\]
For every probability measure with \(|z(\mu)|\le\rho\) and every center \(a\in G\),
\[
 \boxed{
 \sum_j\mu(j)d_N(j,a)^2-F_N(\rho)
 =\sum_j\mu(j)H(j-a)+(-\beta)\bigl(\rho-\operatorname{Re}(e^{-2\pi ia/N}z(\mu))\bigr).
 }
\]
Both terms on the right are nonnegative, and \(H(j)=0\) exactly for the two indicated distance shells. Consequently, if the left side is at most \(\varepsilon\) and the complement of these shells is nonempty, its mass is at most \(\varepsilon/\gamma\), where \(\gamma=\min\{H(j):d_N(j,0)\notin\{k,k+1\}\}>0\). Also \(\rho-\operatorname{Re}(e^{-2\pi ia/N}z(\mu))\le\varepsilon/(-\beta)\).

## Assumptions and scope

Only finite cyclic groups \(N\ge3\), nonnegative real weights of total mass one, the first character \(j\mapsto e^{2\pi i j/N}\), graph distance on the unit-edge cycle, and centers restricted to the vertices are considered. No rationality, exact support-size condition, or equal-weight condition is imposed. The phase of the first Fourier coefficient is unrestricted; the hypothesis is its modulus bound. The statement does not concern arbitrary complex signed weights, other Fourier characters, or continuous centers between vertices.

## Proof

**1. Convex support certificate.** For \(0\le j\le\lfloor N/2\rfloor\) let \(\theta_j=2\pi j/N\in[0,\pi]\). Since \(d_N(j,0)=j\) at these radial representatives, the pairs \((c_j,j^2)\) lie on the graph
\[
 f(x)=\frac{N^2}{4\pi^2}(\arccos x)^2,\quad -1\le x\le1.
\]
Writing \(t=\arccos x\in(0,\pi)\), we have
\[
 \frac{d^2}{dx^2}(\arccos x)^2
 =\frac{2(\sin t-t\cos t)}{\sin^3 t}>0,
\]
because the numerator's derivative with respect to \(t\) is \(t\sin t>0\) and it vanishes at zero. The function is strictly convex (including its continuous endpoint extensions).

Choose consecutive radial nodes \(c_k\ge\rho\ge c_{k+1}\). The affine function \(\ell(x)=\alpha+\beta x\) joining \((c_k,k^2)\) and \((c_{k+1},(k+1)^2)\) has negative slope \(\beta\). By strict convexity, its extension lies strictly below \(f\) at every other sampled cosine, since no grid cosine lies strictly between those two nodes. Therefore \(H(j)\ge0\) on the whole cycle, and equality occurs precisely for radii \(k,k+1\).

**2. Lower bound and equality.** For any \(a\in G\), Fourier translation gives
\[
 \sum_j\mu(j)\cos(2\pi(j-a)/N)
 =\operatorname{Re}(e^{-2\pi ia/N}z(\mu))\le |z(\mu)|\le\rho.
\]
Summing the affine certificate and using \(\beta<0\) yields
\[
 \sum_j\mu(j)d_N(j,a)^2
 \ge\alpha+\beta\operatorname{Re}(e^{-2\pi ia/N}z(\mu))
 \ge\alpha+\beta\rho
 =W_k k^2+W_{k+1}(k+1)^2.
\]
This holds at every center and hence for their minimum. To attain the bound, place \(W_k/2\) at each sign of radius \(k\), and \(W_{k+1}/2\) at each sign of radius \(k+1\); on singleton shells put the unsplit total mass. The cosine moment is \(\rho\), the sine moment is zero, and the squared spread around the chosen center equals the bound. The lower bound already proved for all centers then guarantees that this is the intrinsic minimum.

Equality requires the support certificate to vanish and the rotated Fourier coefficient to have real part exactly \(\rho\). Under the modulus condition this means the rotated coefficient equals the real number \(\rho\). Its cosine equation fixes the two radial totals uniquely as \(W_k,W_{k+1}\); its imaginary part is precisely the asserted sine balance. Conversely those conditions imply equality. On an interior segment with two nonsingleton shells, writing the signed imbalances as \(\delta_k,\delta_{k+1}\), sine balance is the single real equation \(\delta_k\sin\theta_k+\delta_{k+1}\sin\theta_{k+1}=0\) with \(|\delta_j|\le W_j\), hence a compact interval of solutions, whose endpoints eliminate one of the four signed masses. At grid breakpoints one shell has zero total mass, leaving the stated symmetric solution.

**3. Exact deficit and arithmetic effects.** Inserting and subtracting the affine certificate proves the defect identity term by term. The nonnegative slack gives the displayed localization bound and phase/cosine deficiency estimate. For \(\rho=0\), convexity also implies the continuous bound \(N^2/16\), with equality only if the quarter-turn angle is sampled, equivalently \(4\mid N\). If \(N=4m+2\), the bracketing radii are \(m,m+1\) with opposite cosines and equal masses, giving \((m^2+(m+1)^2)/2=N^2/16+1/4\). If \(N\) is odd, strict convexity gives a strict inequality. For \(N=4m+1\) or \(4m+3\), write the quarter-grid offset as \(\delta=1/4\) or \(3/4\), respectively. Taylor expansion of the chord interpolation of \(f\) at the origin, using \(f''(0)=N^2/(2\pi^2)\) and adjacent cosine gaps of order \(1/N\), yields \(F_N(0)-N^2/16\to\delta(1-\delta)=3/16\). This completes the proof.

## Verification

`CHECK.py` uses only the Python standard library. Run `python3 CHECK.py` to reproduce 39,300 deterministic assertions. They cover all orders \(3\le N\le52\), 35 attenuation targets per order, exact dual certificates, explicit minimizers, arithmetic zero-notch identities, and randomized distributions with checks at every possible center. The numerical checks are finite corroboration, not an exhaustive or infinite proof. The strict-convexity argument above supplies the global certificate for all \(N\) and \(\rho\).

## Relationship to prior work

Tan and Zhang [1] study nonnegative cyclotomic multiples and vanishing initial Fourier moments. Their Lemma 2.1 and Proposition 5.1 give support-arc and near-extremal-diameter bounds, not the minimum quadratic graph spread under a bounded single Fourier coefficient. In particular, their Remark 3.3 distinguishes a single Fourier zero for arbitrary positive real coefficients from full cyclotomic divisibility. Our measures need only one approximately vanishing Fourier coefficient; the sharp invariant, full attenuation profile and equality family differ from their results.

Peherstorfer [2] classifies positive trigonometric quadrature formulas through moment matching and orthogonal polynomials. The present calculation instead minimizes a specific metric cost over all positive weights on a *fixed cyclic grid*, under an inequality on the first moment, and determines its entire sharp frontier. Coeurjolly and Le Bihan [3] distinguish intrinsic geodesic variance and extrinsic first trigonometric moment for parametric circular distributions; their analysis does not contain the stated unrestricted finite-grid optimization. These works provide context, not independent novelty certification.

## Limitations

The convexity method is special to a radial quadratic cost and a single first-harmonic magnitude constraint. It does not give an identical frontier for several simultaneous vanished Fourier modes, complex signed measures, or a continuous choice of centers. The result does not determine a lower bound for each individual Fourier coefficient at arbitrary character order. Earlier unlocated formulations under discrete circular-statistics or moment-optimization terminology remain a publication-priority risk; no independent audit has been performed.

## References

[1] Hu Tan and Ying Zhang, *Sharp Diameter Bounds for Nonnegative Cyclotomic Multiples*, arXiv:2609.07646 (first public September 7, 2026), especially Sections 2, 3 and 5.

[2] Franz Peherstorfer, *Positive trigonometric Quadrature Formulas and quadrature on the unit circle*, arXiv:1001.2451 (first public January 14, 2010), especially Sections 1–2.

[3] Jean-François Coeurjolly and Nicolas Le Bihan, *Geodesic Normal distribution on the circle*, arXiv:1012.4361 (first public December 20, 2010), especially Sections 2–3.
