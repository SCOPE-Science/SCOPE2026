# Certified low-order diagonal rational filters for |x| on [-1,1]

## Context

Best uniform rational approximation of the kink $f(x)=|x|$ on $[-1,1]$
is the Newman–Stahl root-exponential regime
($O(\exp(-C\sqrt n))$, Stahl rate $\exp(-\pi\sqrt n)$).
High-type floating tables (Varga–Carpenter–Ruttan to $(50,50)$;
Chebfun type $(80,80)$ in ~21.5 s) give no certified low-type constants.
Low orders $n\le 4$ are the practical filter window (evaluation cost
restricts degree) for Zolotarev-type sign/absolute-value rational filters
in matrix functions and polar factors, and for AAA-Lawson /
differential-correction benchmarks.

## Definitions

- $\|\cdot\|=\sup_{[-1,1]}$.
- $R_{n,n}=\min_{\mathrm{type}(n,n)}\|f-r\|$.
- Even rational $r(x)=R(x^2)$ satisfies
  $\|f-r\|_{C[-1,1]}=\|\sqrt{\cdot}-R\|_{C[0,1]}$ with $t=|x|$, $y=t^2$.
- $r_{22}(x)=P_{11}(x^2)/Q_{11}(x^2)$,
  $P_{11}(y)=0.0437+3.1915y$, $Q_{11}(y)=1+2.383y$ (exact type $(2,2)$).
- $r_{44}(x)=P_{22}(x^2)/Q_{22}(x^2)$,
  $P_{22}(y)=0.00851+16.739y+139.54y^2$,
  $Q_{22}(y)=1+81.671y+74.958y^2$ (exact type $(4,4)$).
- $r_{33}:=r_{22}$ viewed as type $(3,3)$ (zero-padding; valid since
  type $(2,2)\subset$ type $(3,3)$).
- All denominator coefficients are nonnegative, so $Q\ge 1$ on
  $y\ge 0$: pole-freedom by inspection.

## Result

Two-sided sup-norm error intervals for the exhibited filters:

- (a) $\||x|-r_{22}\|\in[0.04367,\,0.04370]$.
- (b) $\||x|-r_{33}\|\in[0.04367,\,0.04370]$ (same rational, padded).
- (c) $\||x|-r_{44}\|\in[0.00847,\,0.00852]$.

Hence $R_{2,2}\le 0.04370$, $R_{3,3}\le 0.04370$, $R_{4,4}\le 0.00852$,
with near-optimality factors of the exhibited filters
$L_{22}/U_{22}=0.99931\ldots$, $L_{44}/U_{44}=0.99413\ldots$.

Rational-over-polynomial separation at matched max-degree 3:
the best uniform degree-$\le 3$ polynomial error for $|x|$ on $[-1,1]$
is exactly $1/8$ (attained by $p^\star(x)=x^2+1/8$ with errors
$-1/8,+1/8,-1/8,+1/8,-1/8$ at $-1,-1/2,0,1/2,1$, hence optimal by
Chebyshev alternation), so
$U_{33}=0.0437<0.125=E_3^{\mathrm{poly}}(|x|)$,
separation factor $0.125/0.0437=2.860\ldots$.

Newman comparison at $n=2$: Newman's explicit degree-2 construction
$N_2(x)=x(P(x)-P(-x))/(P(x)+P(-x))$,
$P(x)=\prod_{k=1}^{2}(x+e^{-k/\sqrt2})$, satisfies
$\||x|-N_2\|\ge e(1)\ge 0.332085\ldots$ (proved by $\sqrt2$ bracketing
plus monotone Taylor bounds), so the $r_{22}$ cap $0.0437$ is at most
$13.2\%$ of Newman's error — a $7.6\times$ rigorous improvement
($7.84\times$ against the float value $0.342617$).

## Proof / evidence

Upper bounds (exact Sturm sign certificates).
With $t=|x|$, $e(t)=t-P(t^2)/Q(t^2)$, $Q>0$:
$|e|\le U$ iff $G_1(t)=tQ(t^2)-P(t^2)-UQ(t^2)\le 0$ and
$G_2(t)=tQ(t^2)-P(t^2)+UQ(t^2)\ge 0$ on $[0,1]$
(degrees $\le 5$ for $r_{22}$, $\le 9$ for $r_{44}$,
exact `Fraction` coefficients).
Each $G$ has the required endpoint sign and exactly zero Sturm roots
in $(0,1)$:

- $r_{22}$, $U=0.0437$: $G_1(0)=-0.0874$, $G_1(1)=-3.71\times10^{-5}$,
  0 roots; $G_2(0)=0$, $G_2(1)=0.2956371$, 0 roots.
- $r_{44}$, $U=0.00852$: $G_1(0)=-0.01703$, $G_1(1)=-0.00150908$,
  0 roots; $G_2(0)=10^{-5}$, $G_2(1)=2.68448908$, 0 roots.

Zero interior roots plus endpoint signs force the inequalities by
continuity (the endpoint-zero case $G_2(0)=0$ with $G_2(1)>0$ still
forces $G_2\ge 0$).

Lower bounds (pointwise evaluation, a fortiori de la Vallée Poussin):
$\|e\|\ge\min_i|e(\xi_i)|$ over any alternating-sign node set.
Exact `Fraction` evaluations:

- $r_{22}$ at $t\in\{0,19/100,81/125,1\}$: errors
  $-0.0437$, $+0.04367468$, $-0.04369350$, $+0.04368903$
  (4 alternating signs), so $\|e\|\ge 0.04367$.
- $r_{44}$ at $t\in\{0,19/500,37/250,39718/100000,77803/100000,1\}$:
  errors $-0.00851$, $+0.00851034$, $-0.00850557$, $+0.00848148$,
  $-0.00847328$, $+0.00851043$ (6 alternating signs),
  so $\|e\|\ge 0.00847$.

Candidates were found by Lawson IRLS + Nelder–Mead polish in $y=x^2$;
no floating-point optimization output enters the proof — every number
is re-proved from the printed decimals alone by the stdlib-only verifier.

## Limitations

- Upper bounds only for the integer minimax values $R_{n,n}$;
  exact minimax values are NOT determined (only pinned within $L/U$
  of the exhibited rationals).
- No full ($\ge 2n+2$-point certified extremal) alternation-optimality
  proof for the minimax values themselves; the 4- and 6-point
  alternating node sets certify near-optimality of the exhibited
  filters, not exact optimality of $R_{n,n}$.
- $r_{33}$ inherits $r_{22}$'s interval via padding; no genuinely
  degree-3 rational was optimized.
- Newman comparison is at $n=2$ only (matched degree with $r_{22}$);
  no claim against higher-$n$ Newman interpolants or Stahl asymptotics.
- Discovery used floating-point heuristics; only the final decimals
  plus exact certificates constitute the result.

## Reproducibility

Run `python3 output/artifacts/verify_all.py` (Python 3 stdlib only;
exact `fractions.Fraction` arithmetic; also writes
`output/artifacts/result_numbers.json`). It asserts: Sturm endpoint
signs and zero root counts for $G_1/G_2$ of $r_{22}$ and $r_{44}$;
nonnegative denominators; strict sign alternation and $|e|\ge L$ at
the listed nodes; the Taylor-monotonicity side conditions and
$e(1)\ge 0.332$ for Newman $n=2$; and prints the separation factor.
Expected output ends with `ALL CHECKS PASSED`.

## References

- Chebfun Example — RationalAbsx: rational approximation of abs(x)
  with minimax. https://www.chebfun.org/examples/approx/RationalAbsx.html
- Chebfun Example — BestApprox: best approximation with the REMEZ
  command. https://www.chebfun.org/examples/approx/BestApprox.html
- DLMF §3.11(iii) Minimax Rational Approximations.
  https://dlmf.nist.gov/3.11
- Chebfun Guide Chapter 4 — Chebfun and Approximation Theory.
  https://www.chebfun.org/docs/guide/guide04.html
