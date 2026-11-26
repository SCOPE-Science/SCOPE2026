# Independent mathematical audit

## correctness

PASS

On the unit circle the derivative measure of real BV data has zero total mass; each Jordan part has mass V/2. With K_t=−tG_t′, the multiplier of K_t applied to Df is exactly that of I−R_t. Normalize a coupling of the Jordan parts to a probability and take the mean of the corresponding translate chords of K_t in L². The norm is at most their maximum M; equality forces zero Hilbert-space variance since all chord norms are at most M. Equal nonzero maximizing chords yield equal ordered differences of point masses: nonzero Fourier modes agree by injectivity of K_t on these modes and the zero mode agrees by total mass zero. The equality support is therefore one ordered pair, giving exactly the stated arcs up to constants and scaling. The kernel G_t has derivative jump −1/t and solves the homogeneous equation off zero; H_t=G_t*G_t has H_t″=∂_tG_t. The squared arc residual is 2t²[H_t″(s)−H_t″(0)], divided by four for V²; the differentiated expression and its integral from s=0 agree with the frozen formula. Its sign on the open half-circle is that of h(z)+2−h(a), where h(u)=u coth u strictly increases from 1. This gives a unique shorter optimum and includes the critical semicircle. In the small-time limit z=a−2+o(1), and the normalized bracket tends to 1+e^(−2). Near criticality h(z)=1+z²/3+O(z⁴) and a_c h′(a_c)=a_c²−6, yielding the stated square-root coefficient. Replay: RESULT.md proof §§1–4 and its positive Fourier-tail bound; the finite verifier was inspected, not executed. Scope is real circular BV and a single unit-circle constant-coefficient step.

## originality

PASS

The coupling-to-arcs mechanism is shared by other circular smoothing results. The distinguishable contribution is the explicit all-time resolvent maximization, its complete equality lengths, and the critical transition and coefficients; the inspected bounds for other operators do not furnish these.

## value

PASS

This is a precise deterministic benchmark for a common implicit diffusion step on discontinuous data. It identifies where the worst pair of jumps is located, shows a finite-time transition that a norm bound alone misses, and quantifies both the small-time interaction and the approach to the semicircle. The result does not generalize by assertion to other boundaries or multiple steps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
