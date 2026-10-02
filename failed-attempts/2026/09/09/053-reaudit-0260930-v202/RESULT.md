# Certified Maynard–Tao extremal sieve ratio for one fixed k=32 weight cell

## Context

After Zhang–Maynard–Tao–Polymath, bounded prime gaps are governed by the
collision between the Maynard–Tao sieve ratio $M_k$ and the level of
distribution $\\theta$. Maynard (arXiv:1311.4600, Prop. 4.2) shows that for an
admissible $k$-tuple, with $M_k = \\sup_F \\sum_m J_k^{(m)}(F)/I_k(F)$,

$$r_k = \\lceil \\theta M_k/2 \\rceil$$

primes are guaranteed infinitely often in the tuple. Hence at the
unconditional Bombieri–Vinogradov level $\\theta=1/2$ one needs $M>4$ for
$\\geq 2$ primes (DHL[k,2]) and $M>8$ for $\\geq 3$ primes (DHL[k,3]);
at full Elliott–Halberstam $\\theta \\approx 1$ one needs $M>2$ for
$\\geq 2$ primes and $M>4$ for $\\geq 3$ primes.
A fixed restricted weight cell either pushes $M$ past a threshold or its
extremal ratio is a certified no-go lemma locating the sieve-side
obstruction. This record is the pre-registered optimality-barrier outcome
in sharp corrected form.

## Definitions

- Fix $k=32$ and the simplex
  $R = \\{x_i \\geq 0,\\ \\sum_{i=1}^{32} x_i \\leq 1\\}$.
- Fix the documented 8-dimensional weight cell
  $$V = \\mathrm{span}\\{1,s,s^2,\\dots,s^6,x_1\\}, \\quad
    s = x_1+\\cdots+x_{32}$$
  (symmetric polynomials of total degree $\\leq 6$ plus one asymmetric
  simplex-cell direction $x_1$).
- Maynard functionals ($\\tau=1$):
  $$I(F) = \\int_R F^2, \\quad
    J(F) = \\sum_{i=1}^{32} J_i(F), \\quad
    J_i(F) = \\int \\left(\\int F\\,dx_i\\right)^2, \\quad
    M(F) = J(F)/I(F).$$
- Scaled exact Gram matrices: $A = 31!\\,I$, $B = 31!\\,J_{\\mathrm{sum}}$
  on the 8-basis above.

## Result

The exact cell maximum satisfies

$$7553888936545658/2485078816758705 \\leq
  \\max_{0\\neq F \\in V} M(F) \\leq 61/20 = 3.05,$$

i.e. $\\max_V M \\in [3.0396\\dots, 3.05]$ ($3.03969793\\dots$ lower end).

Prime-count readings via Maynard Prop. 4.2 ($r_k=\\lceil\\theta M_k/2\\rceil$):

- (a) No weight in $V$ yields unconditional DHL[32,2] (needs $M>4$ at
  $\\theta=1/2$) or DHL[32,3] (needs $M>8$); $3.05<4$.
- (b) No weight in $V$ yields even conditional triple-prime:
  $\\geq 3$ primes needs $M>4$ even at $\\theta\\approx 1$; $3.05<4$.
  A sharp $m=2$ barrier holding including EH.
- (c) $V$ does yield $\\geq 2$ primes conditionally once
  $\\theta>2/M\\approx 0.658$ (using $M\\geq 3.0397$), e.g. under a
  partial EH/GEH hypothesis above 0.658.

No unconditional prime-count corollary is claimed; the ratio interval
itself is the auditable finding.

Admissibility witness only: the 32-tuple $H$ in artifacts/tuple.json
(diameter 200, normalized to min 0) misses a residue class mod $p$ for
every $p\\leq 32$ (witnesses logged; machine-checked). Tuple minimality
is disclaimed; no diameter-based prime record is claimed.

## Proof / evidence

1. Exact Gram matrices $A,B$ computed in exact rational arithmetic from
   Dirichlet simplex integrals $\\int_{\\mathrm{simp}_d} S^a(1-S)^b$ via
   binomial expansion and iterated $(t,u)$ rest-moments
   $\\int t^{t_{pow}}(t+u)^a(1-t-u)^b$ (exact Beta values).
   Entries stored in artifacts/gram_final.json.
2. Lower bound: rational coefficient vector $c$ in
   artifacts/ratio_bound.json gives
   $M(c)=7553888936545658/2485078816758705\\approx 3.03970$ by exact
   Fraction evaluation (denominator $>0$ checked).
3. Upper bound: for $U=61/20$, $U\\cdot A-B$ is positive definite by
   exact rational LDL (all 8 pivots $>0$, logged in ratio_bound.json),
   hence $M(F)\\leq U$ for all $0\\neq F\\in V$.
4. Independent replay: artifacts/verify.py (stdlib only) rebuilds both
   Gram matrices from its own formulas, replays the LDL pivots,
   re-evaluates $M(c)$, re-checks admissibility: prints VERIFY_OK.
   Auditor re-execution confirmed VERIFY_OK; hand derivation of every
   Gram block (A via $S$-density/symmetry/Dirichlet moments; B via
   $\\Phi$ integrals and rest moments) matches; $A$ positive-definiteness
   independently confirmed; float generalized-eigenvalue max $\\approx
   3.044$ lies inside the certified interval.

## Limitations

- Barrier $U=3.05$ binds only the documented 8-dimensional slice $V$,
  not the full degree-$\\leq 6$ symmetric space; nothing is claimed
  about weights outside $V$.
- Ratio interval is the finding, so threshold-normalization disputes
  cannot void it; prime readings follow from Maynard Prop. 4.2.
- No unconditional DHL corollary; no conditional triple from $V$ even
  under EH; only conditional $\\geq 2$-prime reading above
  $\\theta\\approx 0.658$.
- Diameter-200 tuple is solely an admissibility witness ($p\\leq 32$);
  minimality disclaimed.
- Two real bugs caught and fixed during the work (sym-sym $J$ expansion
  conflating $S^a$ with $(1-S)^a$; a 29!/30! factorial slip in the
  rest-moment) remain disclosed in the draft.

## Reproducibility

Run `python3 verify.py` in artifacts/ (stdlib only). Expected:

```
Gram matrices: independent rebuild MATCHES
L = 7553888936545658/2485078816758705 = 3.0396979305462093
U = 61/20 PSD pivots all >0 OK
Admissibility p<=32 OK; diameter = 200
VERIFY_OK
```

## References

- J. Maynard, Small gaps between primes, arXiv:1311.4600.
- D. H. J. Polymath (Polymath 8b), Variants of the Selberg sieve, and
  bounded intervals containing many primes, arXiv:1407.4897.
- D. H. J. Polymath, New equidistribution estimates of Zhang type,
  arXiv:1402.0811.
