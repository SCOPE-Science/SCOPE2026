# Two incompatible escape clocks in a positive-feedback planar map

## Finding

Consider the real planar recurrence introduced in [1], with \(r=5/4\):
\[
F_{a,b,c}(x,y)=\bigl(x(a+b|y|),\,cx-r y\bigr).
\]
The following is one global-escape and resonant-growth theorem.

**Theorem.** Let \(b>0\), \(c\ne0\), and \(a>0\).

1. **Sharp escape chamber.** Every nonzero real initial point has an unbounded forward orbit if and only if \(a\ge1\). In fact, when \(a\ge1\) all nonzero orbits tend to infinity in norm; for \(x_0\ne0\), writing \(X_n=|x_n|\),
\[
X_{n+2}\ge a^2X_n+\frac{ab|c|}{r}X_n^2 \qquad(n\ge0).
\]
This two-step inequality is pointwise sharp for a prescribed \(x_n\). In this chamber, \(x_0\ne0\) implies \(\log X_n\ge C(\sqrt2)^n\) for all sufficiently large \(n\) and some orbit-dependent \(C>0\). The line \(x_0=0\), except for the origin, instead escapes at the exact rate \(|y_n|=r^n|y_0|\). The only invariant Borel probability measure on \(\mathbb R^2\) is the atom at the origin. When \(0<a<1\), two nonzero fixed points exist, so the boundary \(a=1\) is exact.

2. **Two sharp double-exponential clocks at resonance.** Specialize to \(a=r\) and \(b,c>0\). The cone
\[
\mathcal W=\{(x,y):x>0,\ 0\le y\le cx/r\}
\]
is forward invariant, its two boundary rays exchange under one iteration, and its interior is forward invariant. Put \(\phi=(1+\sqrt5)/2\). For every interior point there is a finite \(L=L(x_0,y_0)>0\) such that
\[
\lim_{n\to\infty}\frac{\log x_n}{\phi^n}=L.
\]
For an initial point on either boundary ray, let \(s=0\) for \(y_0=0\) and \(s=1\) for \(y_0=cx_0/r\), and put \(z_m=x_{2m+s}\). Then \(y_{2m+s}=0\) for all \(m\ge0\),
\[
z_{m+1}=r^2z_m+rbc z_m^2,
\qquad \lim_{m\to\infty}\frac{\log z_m}{2^m}=\Lambda>0.
\]
In particular, the interior grows on the \(\exp(L\phi^n)\) scale, while either boundary grows on the slower \(\exp(\Theta((\sqrt2)^n))\) scale. Both are escaping orbits for identical parameter values. The boundary family also demonstrates that the universal lower logarithmic growth base \(\sqrt2\) in part 1 cannot be increased uniformly over these parameters and initial conditions.

## Assumptions and scope

The phase space is all of \(\mathbb R^2\); trajectories are iterated forward at integer times \(n\ge0\). Parameters satisfy the displayed sign restrictions. The first part covers every initial state. The fine growth classification in part 2 concerns exactly the indicated forward-invariant cone and makes no claim about the detailed growth rates outside it. Constants \(C,L,\Lambda\) depend on the parameters and initial point. Statements about invariance are for Borel probability measures, not finite signed measures or nonprobability infinite measures.

## Proof

**Global two-step inequality.** When \(a\ge1\), \(b>0\), the first coordinate never changes sign if initially nonzero. From \(y_{n+1}+r y_n=cx_n\) and \(r>1\),
\[
|y_n|+|y_{n+1}|\ge\frac{|c|}{r}X_n.
\]
Therefore
\[
\begin{aligned}
X_{n+2}&=X_n(a+b|y_n|)(a+b|y_{n+1}|)\\
&\ge X_n\bigl(a^2+ab(|y_n|+|y_{n+1}|)\bigr)\\
&\ge a^2X_n+\frac{ab|c|}{r}X_n^2.
\end{aligned}
\]
Equality occurs at a given nonzero state with \(y_n=cx_n/r\), because then \(y_{n+1}=0\) and the first inequality's product term vanishes. Let \(q=ab|c|/r>0\). For each parity \(j\in\{0,1\}\), \(X_{2m+j}\) increases and must diverge: a hypothetical finite positive limit violates \(Z_{m+1}\ge Z_m+qZ_m^2\). Once \(qX_{2m+j}>1\), its logarithm obeys \(\log(qX_{2(m+1)+j})\ge2\log(qX_{2m+j})\). The two parities give the claimed \(\sqrt2\)-base lower bound with a positive common constant after a finite index. For \(x_0=0\), \(x_n=0\) and \(y_n=(-r)^n y_0\).

Thus every point except the origin escapes in norm. If \(\mu\) is invariant and \(f\) is continuous with compact support, dominated convergence applied to \(f\circ F^n\) gives \(\int f\,d\mu=\mu(\{0\})f(0)\), since every other orbit eventually leaves every compact set. Approximating the constant one by compactly supported functions forces \(\mu(\{0\})=1\). For \(0<a<1\), setting \(s_\pm=\pm(1-a)/b\) yields two distinct fixed points \(((1+r)s_\pm/c,s_\pm)\), proving sharpness.

**Resonant cone and exact boundary recurrence.** For \(a=r\), \(b,c>0\), if \((x,y)\in\mathcal W\) then \(x'=(r+by)x\ge rx>0\) and \(0\le y'=cx-ry\le cx\le cx'/r\). Strict inequalities persist in the interior. The rays \(y=0\) and \(y=cx/r\) map exactly into each other. Eliminating one step gives the identity, valid along every orbit inside the cone,
\[
y_{n+2}=(r^2+bc x_n)y_n.
\]
On a boundary ray the zero \(y\)-coordinate therefore returns at every second step, and a direct two-step computation gives
\[
z_{m+1}=r^2 z_m+rbc z_m^2.
\]
Set \(t_m=rbc z_m>0\). Then \(t_{m+1}=t_m^2+r^2t_m\); because \(r^2>1\), \(t_m\to\infty\). The logarithmic recurrence
\[
\frac{\log t_{m+1}}{2^{m+1}}=\frac{\log t_m}{2^m}+2^{-m-1}\log(1+r^2/t_m)
\]
shows convergence to a finite number (the increments have a summable upper bound). The limit is positive because at sufficiently large \(m\), \(\log t_m>0\) and all later increments are positive. Replacing \(\log t_m\) by \(\log z_m\) leaves the limit unchanged.

**Interior golden-ratio clock.** For an interior starting point, \(y_0,y_1>0\). The two-step identity implies that both parity subsequences of \(y_n\) grow at least geometrically by the factor \(r^2>1\); thus \(y_n\to\infty\). Since \(x_{n+1}/x_n=r+by_n\to\infty\), and \(0<y_n\le cx_{n-1}\) for \(n\ge1\),
\[
0<\frac{y_{n-1}}{x_{n-1}}\le\frac{c x_{n-2}}{x_{n-1}}=\frac{c}{r+b y_{n-2}}\longrightarrow0.
\]
Consequently \(y_n/(cx_{n-1})\to1\) and
\[
\frac{x_{n+1}}{bc x_nx_{n-1}}\longrightarrow1.
\]
Write \(u_n=\log(bc x_n)\). For all sufficiently large indices,
\[
u_{n+1}=u_n+u_{n-1}+\varepsilon_n,
\qquad \varepsilon_n=\log\frac{r+by_n}{bc x_{n-1}}\longrightarrow0.
\]
The standard Fibonacci Green-function formula for a forced second-order recurrence expresses \(u_n\) as a homogeneous Fibonacci combination plus a convolution of the bounded \(\varepsilon_j\) with Fibonacci numbers. Dividing by \(\phi^n\), the convolution converges absolutely (its coefficients decay geometrically in \(j\)); hence \(\lim u_n/\phi^n=L\) exists and is finite. For positivity, the preceding ratio tends to one, so eventually \(x_{n+1}\ge(bc/2)x_nx_{n-1}\). Thus \(v_n=\log((bc/2)x_n)\) obeys \(v_{n+1}\ge v_n+v_{n-1}\). Both \(v_n,v_{n+1}\) are positive for sufficiently large \(n\) because \(x_n\to\infty\), and Fibonacci comparison gives \(v_n\ge K\phi^n\) for large \(n\) with \(K>0\). Therefore \(L>0\). This proves both clocks and their separation.

## Verification

The accompanying file `verification/escape_clock_check.py` uses exact rational arithmetic, not floating-point orbit plots. It verifies the universal two-step inequality for 400 deterministic sign-varied parameter/initial-state cases and the resonant two-step identity, cone invariance, and alternating boundary recurrence in 72 further checks. All 472 tests passed. The infinite-time assertions instead follow from the foregoing analytic estimates and Fibonacci recurrence argument; finite tests are not substitutes for those proofs.

## Relationship to prior work

Zhou, Li, Lu, Lei and Zhao [1] introduced exactly this map, found its fixed points, and studied numerical bifurcations, amplitude control, symmetric attractors and circuit implementation (their equation (1) and sections 2–6). Their nonzero fixed-point condition already identifies a sign-dependent parameter boundary, but does not imply the global all-orbit escape inequality, the unique stationary probability, or the distinct golden-ratio and square-root-two orbit clocks proved here. Figure 10(b) in [1] also labels a bounded-looking orbit diagram with \(a=2.35\), \(b=1\), \(c=-1\); the printed recurrence instead forces \(|x_{n+1}|\ge2.35|x_n|\) whenever \(x_n\ne0\). Thus the illustration and the literal map would require reconciliation, without implying knowledge of the authors' numerical implementation. General work on canonical heights and dynamical degrees for algebraic maps [2] does not by itself classify the two boundary rays of this nonsmooth real map or identify its global sharp escape condition. Comparisons with published orbit-growth and escape classifications for other families likewise do not imply this model-specific theorem.

## Limitations

The results are confined to positive feedback \(b>0\); the chaotic examples emphasized in [1] often use \(b<0\). No attractors or bifurcations are classified for the negative-feedback chamber. The fine growth assertion is limited to \(\mathcal W\) at \(a=r\) with \(c>0\); no claim of uniqueness of possible escape exponents outside that cone is made. Originality is assessed against searched, accessible literature and records, not an exhaustive mathematical bibliography. No independent proof audit has been conducted.

## References

[1] X. Zhou, C. Li, X. Lu, T. Lei and Y. Zhao, *A 2D Hyperchaotic Map: Amplitude Control, Coexisting Symmetrical Attractors and Circuit Implementation*, Symmetry **13** (2021), 1047, published 2021-06-10. https://doi.org/10.3390/sym13061047 . Full text: https://pdfs.semanticscholar.org/672a/71704179de6ae9d20d731f1fc0bd17a1a82e.pdf .

[2] J. H. Silverman, *Dynamical degree, arithmetic entropy, and canonical heights for dominant rational self-maps of projective space*, Ergodic Theory Dynam. Systems **34** (2014), 647–678, published online 2012-11-29. https://doi.org/10.1017/etds.2012.144 .
