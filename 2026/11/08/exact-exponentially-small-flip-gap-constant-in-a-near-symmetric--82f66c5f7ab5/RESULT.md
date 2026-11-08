# Exact exponentially small flip-gap constant in a near-symmetric replicator map

## Finding

**Theorem (sharp beyond-all-orders boundary layer).** Let
\[
 f_{a,b}(t)=\frac{t}{t+(1-t)\exp(a(t-b))},\qquad 0\le t\le1,
\]
with \(a>0\) and \(b=(1-d)/2\), where \(d>0\) is sufficiently small. Write \(a_f(d)\) for the unique coupling at which the nontrivial period-two orbit has multiplier \(-1\). Its existence and uniqueness for sufficiently small \(d\) are established in [3]. Introduce the explicit rational comparison coupling
\[
 a_{\mathrm{rat}}(d)=\frac{2}{d(1-d)}.
\]
Let \(x_f(d)\) denote the smaller point of that two-cycle at \(a=a_f(d)\), and let \(\Lambda_{\mathrm{rat}}(d)\) denote its multiplier at \(a=a_{\mathrm{rat}}(d)\). Then
\[
\boxed{\lim_{d\downarrow0}d^2 e^{1/d}\left(a_f(d)-\frac{2}{d(1-d)}\right)=4,}
\]
\[
\boxed{\lim_{d\downarrow0}\frac{d e^{1/d}}{1-d}\,x_f(d)=1,\qquad
\lim_{d\downarrow0}\frac{d e^{1/d}}{4}\bigl(1+\Lambda_{\mathrm{rat}}(d)\bigr)=1.}
\]
In particular the rational comparison coupling lies *strictly inside the attracting region* for all sufficiently small \(d>0\), and the distance to the neutral flip boundary is exactly \(4d^{-2}e^{-1/d}(1+o(1))\). These claims concern only the distinguished period-two orbit and its multiplier.

For \(b=(1+d)/2\), reflection \(t\mapsto1-t\) gives identical coupling and multiplier limits, with \(x_f(d)\) replaced by the distance of the larger orbit point from \(1\).

## Assumptions and scope

All limits are taken along real \(d>0\) tending to zero. The asymptotic \(o(1)\) refers to that limit; no explicit finite upper bound on admissible \(d\) is claimed. For each sufficiently small \(d\), the nontrivial period-two orbit exists for \(a>2/[b(1-b)]\). The points of this orbit have the form \(x=b-u\), \(y=b+u\), with \(u\in(0,b)\). The multiplier means \(f'_{a,b}(x)f'_{a,b}(y)\). The comparison coupling grows as \(2/d\); it is not the fixed-point flip threshold \(2/[b(1-b)]\), which remains bounded near \(d=0\).

## Proof

**1. Cycle coordinates and known uniqueness of the neutral crossing.** Put \(h(t)=\log((1-t)/t)\) and \(q(t)=t(1-t)\). The exact identity
\[
 h(f_{a,b}(t))-h(t)=a(t-b)
\]
implies that a two-cycle \(x<y\) satisfies \(x+y=2b=1-d\). For \(x=b-u\), \(y=b+u\), the cycle equation is equivalent to
\[
 a=\frac{h(b-u)-h(b+u)}u
 =\frac2u\left(\operatorname{artanh}\frac{u}{b}+
 \operatorname{artanh}\frac{u}{1-b}\right).
\]
The positive-term power series of \(\operatorname{artanh}(s)/s\) shows that this expression increases strictly from \(2/[b(1-b)]\) to infinity, giving one two-cycle for every larger \(a\). Differentiating the original map around the cycle gives
\[
 \Lambda(a,d)=\bigl(1-aq(x)\bigr)\bigl(1-aq(y)\bigr).
\]
The existing theorem [3, Proof, Steps 3–6] proves that for small enough \(d>0\), this multiplier crosses \(-1\) *once*, transversely, at \(a_f(d)\), and establishes the coarse, uniform estimate
\[
 a_f(d)=\frac{2}{d(1-d)}
 +O\!\left(d^{-2}e^{-1/(10d)}\right).
\]
This previously established existence/uniqueness and error estimate are used here as a lemma; they are not new claims. In particular, writing \(\Delta(d)=a_f(d)-a_{\mathrm{rat}}(d)\), one has \(\Delta(d)=o(1)\).

**2. Exponentially small cycle coordinate at the crossing.** Since \(y=1-d-x\), the first cycle equation gives the exact positive identity
\[
 x=\frac{(1-x)(1-d-x)}{d+x}\exp\!\left[-a\left(\frac{1-d}{2}-x\right)\right]. \tag{1}
\]
At \(a=a_f(d)\), the prior uniform endpoint estimate in [3, Step 3] gives \(x_f\le\exp[-1/(10d)]\) for small \(d\). Hence \(x_f=o(d)\). Also,
\[
 a_f(d)\left(\frac{1-d}{2}-x_f\right)
 =\left(\frac{2}{d(1-d)}+o(1)\right)\frac{1-d}{2}
  -a_f(d)x_f
 =\frac1d+o(1),
\]
since \(a_f(d)=O(d^{-1})\) and \(x_f=o(d)\). Equation (1) therefore yields
\[
 x_f(d)=\frac{1-d}{d}e^{-1/d}(1+o(1)). \tag{2}
\]
The same argument holds at \(a=a_{\mathrm{rat}}(d)\): its small-cycle coordinate \(x_{\mathrm{rat}}\) is bounded by the same estimate in [3, Step 3], so
\[
 x_{\mathrm{rat}}(d)=\frac{1-d}{d}e^{-1/d}(1+o(1)). \tag{3}
\]

**3. Extracting the first nonvanishing stability displacement.** For either of the two parameters and its corresponding small orbit coordinate \(x\),
\[
 q(x)=x-x^2,\quad
 q(y)=d(1-d)+(1-2d)x-x^2.
\]
Let \(a=a_{\mathrm{rat}}+\Delta\), with \(\Delta=o(1)\) and \(x=o(d)\). Insert these expressions into the exact multiplier identity, and use \(a_{\mathrm{rat}}d(1-d)=2\). Elementary multiplication gives
\[
 1+\Lambda=-d(1-d)\Delta+\frac{4x}{1-d}+o(x). \tag{4}
\]
The error \(o(x)\) is uniform for the two relevant parameter choices: all omitted terms are bounded by constants times \(x^2/d^2\), \(|\Delta|x\), and \(\Delta^2dx\); their ratio to \(x\) tends to zero because the endpoint estimate gives \(x=o(d^m)\) for every fixed positive integer \(m\), while \(\Delta=o(1)\). There is no parameter-only quadratic remainder: the exact multiplier is linear in \(a\) when \(x=0\), as \(q(x)=0\).

At \(a=a_f\), the defining condition is \(\Lambda=-1\). Equations (2) and (4) give
\[
 \Delta(d)=\frac{4x_f(d)}{d(1-d)^2}(1+o(1))
 =\frac{4}{d^2(1-d)}e^{-1/d}(1+o(1)).
\]
Because \(1-d\to1\), this proves the first boxed limit and its strict positive sign. At the rational comparison parameter \(\Delta=0\), (3)–(4) yield
\[
 1+\Lambda_{\mathrm{rat}}(d)
 =\frac{4x_{\mathrm{rat}}(d)}{1-d}(1+o(1))
 =\frac4d e^{-1/d}(1+o(1)),
\]
proving the remaining limit. The known strict inequality \(\Lambda<1\) for every nontrivial cycle [3, Step 2], together with \(\Lambda_{\mathrm{rat}}>-1\), proves local hyperbolic attraction at the comparison parameter. Reflection proves the assertion for \(b>1/2\).

## Verification

The standalone `verify.py` uses only the Python standard library. It checks 132 exact rational multiplier identities and six high-precision decimal cycle and flip-point computations, including the normalized exponentially small gap, boundary-point coordinate, and multiplier margin. Run `python3 verify.py`; its final line is `VERIFY_OK rational_multiplier_identites=132 high_precision_parameters=6`. These are finite checks, not a substitute for the uniform asymptotic argument in the proof. Critical published ingredients are the unique transverse crossing and coarse endpoint bounds of [3]; all new leading constants follow from equations (1)–(4).

## Relationship to prior work

Kryzhevich, Zhang, and Chmara [1] established the two-cycle dynamics, including the exceptional symmetric case and qualitative asymmetric loss of stability. Kryzhevich and Zhang [2] analyzed the same map in a more general shift-map setting. The sigmoid-conjugate recurrence is also treated in [4, Sections 3–4], which proves period-two existence/uniqueness and describes numerical bifurcations, not the sharp exponential asymptotics. Most closely, [3] already proved that for small \(\delta=|b-1/2|\) the period-two multiplier has exactly one neutral crossing and that its coupling is \(1/[\delta(1-2\delta)]+O(\delta^{-2}e^{-1/(20\delta)})\). That original theorem covers both uniqueness and every finite algebraic-order asymptotic term. **Those results are not new here.** Its error estimate does not imply the actual exponential rate, the coefficient of its first nonzero beyond-all-orders term, the direction of the gap, or the corresponding normalized multiplier margin. The present theorem identifies precisely these missing scales by resolving the exponentially tiny orbit endpoint. Bibliographic and database searches of these formulations found no covering identity for the three joint limits.

## Limitations

This is a sharp asymptotic near the symmetry point, not a global formula for all asymmetries. It concerns local linear stability of one distinguished two-cycle, not the existence or type of a period-four branch or the global attractor census. The leading coefficient is proved using the uniqueness and coarse bounds from [3]; removing those published hypotheses is not part of the claim. The result is a mathematically nonperturbative refinement of a known boundary, not a new boundary's existence theorem. Independent external validation and exhaustive publication-priority adjudication have not been performed.

## References

1. S. Kryzhevich, Y. Zhang, M. Chmara, *Bifurcations and invariant sets for a family of replicator maps from evolutionary games*, arXiv:2412.16379v1, first public 2024-12-20, https://arxiv.org/abs/2412.16379.
2. S. Kryzhevich and Y. Zhang, *Shift maps and statistical invariants for some dynamical systems*, arXiv:2603.20685v1, first public 2026-03-21, https://arxiv.org/abs/2603.20685.
3. *Singular symmetry-breaking threshold for the period-two orbit of a replicator map*, published October 11, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-singular-symmetry-breaking-threshold-for-the-period-two-orbit-of--fdee730ba349/RESULT.md.
4. S. Kryzhevich, V. Avrutin, G. Söderbacka, *Bistability in a one-dimensional model of a two-predators-one-prey population dynamics system*, arXiv:2108.06739v3, https://arxiv.org/abs/2108.06739.
