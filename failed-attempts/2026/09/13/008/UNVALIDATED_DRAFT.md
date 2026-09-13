# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# PPV Galois group of the cubic oscillator Y'' = (x^3 + t) Y

## Setting
Let `C` be algebraically closed of characteristic 0, `K0` a
`d/dt`-differentially closed field containing `C(t)`, `K = K0(x)` with
`d/dx(x)=1`, `(d/dt)(x)=0`, and `r = x^3 + t in K`.
Consider `D(Y) = Y'' - rY = 0`, i.e. the system `Y' = A Y` with
`A = [[0,1],[r,0]]`, traceless, so every PPV group lands in SL2.
Goal: run the bounded Arreche-Dreyfus computation and exhibit the defining
`t`-differential equations of the PPV group.

## Theorem
The (unparameterized) Picard-Vessiot group of `Y''=(x^3+t)Y` over `K` is the
full group `SL2`, and the parameterized Picard-Vessiot (PPV) Galois group
(with parameter derivation `d/dt`) is the full constant group `SL2`:
it is defined by `det = 1` alone, with no nontrivial `d/dt`-differential
equation on the matrix entries. In particular a generic solution (and the
natural fundamental matrix) is hypertranscendent in `t` in the sense of
Hardouin-Minchenko-Ovchinnikov: no nonzero `K`-coefficient `d/dt`-polynomial
relation holds among a fundamental solution matrix and its `t`-derivatives.
The Arreche `Pi'`-reduction is vacuous here (`D = {0}`), and the unipotent
radical is `0`.

## Proof, step 1: classical PV group is SL2 (Kovacic cases 1-3 excluded)

Kovacic's theorem for `Y''=rY` ([Kov86], cf. [vdPS03] section 4.3,
[Dreyfus, arXiv:1110.1053] Thm 2.10, [Arreche, arXiv:1208.2226] Thm 3.2):
the PV group is reducible/dihedral/finite/SL2 according as the Riccati
equation `R(u) := u' + u^2 - r = 0` is solvable in `K` / in an irreducible
quadratic extension / in `Kbar` with all roots giving finite group / never.
We exclude the first three.

### Case 1: no Riccati solution in K.
Suppose `u in K = K0(x)` satisfies `u'+u^2 = x^3+t`; `r` is a polynomial,
hence has no finite poles.

Residue lemma. If `u` has a pole at `c in K0bar` of order `m >= 1` with
principal part `a/(x-c)^m`, then `u'` contributes `-m a/(x-c)^{m+1}` while
`u^2` contributes `a^2/(x-c)^{2m}`. If `m >= 2`, `u^2` dominates with order
`2m > m+1`, impossible against pole-free `r`. Hence `m = 1`, and the polar
part of `u'+u^2` is `(a^2-a)/(x-c)^2` (verified symbolically in the artifact).
Vanishing forces `a = 1`. So every finite pole of `u` is simple of residue 1.

Write partial fractions `u = P + sum_{i=1}^s 1/(x-c_i)` with polynomial
`P in K0bar[x]` (multiple poles reduce to this since all residues are 1).
Then `u' + u^2 = P' + 2P sum_i 1/(x-c_i) + (sum_i 1/(x-c_i))'`
`+ (sum_i 1/(x-c_i))^2 + P^2`. The cross terms are proper rational with at
most simple poles, while `(sum)' + (sum)^2 = sum_{i<j} 2/((x-c_i)(x-c_j))`
is proper. Since `r` is a polynomial, all proper polar parts must cancel,
and comparing polynomial parts gives `P' + P^2 + E = r` with `E` a constant
(the `x^{-1}` and `x^{-2}` coefficients at infinity force `s = 0` below;
in any case): if `deg P = d >= 1`, `deg(P'+P^2) = 2d` with leading
coefficient `f^2 != 0`; `2d = 3` is impossible over integers; and
`d = 0` gives bounded LHS against cubic `r`. The infinity check makes this
watertight: `u` rational implies `u = O(x^k)`; `u'+u^2` has degree `2k`
(if `k >= 1`), degree `k-1` (if `k <= 0` with `k != 0`... in all cases even
or `<= 0`), never the odd degree 3 of `r` with leading coefficient 1.
Concretely: constant `u` gives constant `u^2`; `deg P >= 1` gives even
degree `2d`; proper part is bounded at infinity. None equals `x^3+t`.
Hence no `u in K` exists. (Checked: `2d != 3` for all `0 <= d <= 6` and in
general; leading-term algebra confirmed by the artifact.)

### Case 2: no Riccati solution in any irreducible quadratic extension.
Suppose `u` satisfies `R(u)=0` in some quadratic `F = K(u)` with `u not in K`.
Let `v` be the Galois conjugate root, `s = u+v in K` (trace),
`d_ = u-v` with `Delta := d_^2 in K` (discriminant). From
`u'+u^2 = r = v'+v^2`, subtracting gives `d_' + s d_ = 0`, i.e.
`Delta' + 2 s Delta = 0`, so `s = -Delta'/(2 Delta)`.
Adding gives `s' + (s^2+Delta)/2 = 2r`, i.e. `Delta = 4r - 2s' - s^2`.

Since `r` is a polynomial, any finite pole of `s` must come from poles of
`u` or `v`, each of which (by the residue computation applied in `F`, where
`r` is still pole-free) is simple of residue 1, so a priori a pole of `s`
has order `m >= 1` and residue `a in {1, 2}`. But
`s = -Delta'/(2 Delta)` is (minus one half) a logarithmic derivative, hence
has only simple poles: `m >= 2` is excluded outright (if `Delta` has a
zero/pole of order `e` at `c`, `s` has at most a simple pole of residue
`-e/2`; in particular a `Delta` pole of order `P` gives `s`-residue `+P/2`).

Exclude residue `a = 2`: if `s ~ 2/(x-c)` then `s' ~ -2/(x-c)^2` and
`s^2 ~ 4/(x-c)^2`, so the double poles cancel,
`-2s' - s^2 ~ (4 - 4)/(x-c)^2 = 0` (i.e. `2a - a^2 = 0` for `a = 2`), and
`Delta = 4r - 2s' - s^2` has valuation at least `-1` at `c` (at worst a
simple pole; artifact valuation check). But at a point where `Delta` has
valuation `e >= -1`, `s = -Delta'/(2Delta)` has residue `-e/2`: namely
`+1/2` if `e = -1`, `0` if `Delta` is regular nonzero, `-e/2 <= -1/2` if
`e >= 1` — never `+2`. Contradiction. Hence every finite pole of `s` is
simple of residue 1.

Write `s = P + sum_{i=1}^N 1/(x-c_i)` with polynomial `P`. Since
`Delta'/Delta -> 0` at infinity (logarithmic derivative of a rational
function), `s = -Delta'/(2Delta)` vanishes at infinity, so `P = 0`; i.e.
`s = sum_{i=1}^N 1/(x-c_i)` (with `s = 0` when `N = 0`).

Then `Delta = 4r - 2s' - s^2 = Q/prod_{i=1}^N (x-c_i)^2` with `Q` polynomial:
indeed `(sum)' + (sum)^2` put over `prod (x-c_i)^2` is proper, while
`4r = 4(x^3+t)` contributes degree `3 + 2N` with leading coefficient 4, so
`deg Q = 3 + 2N >= 3` (including `N = 0`, where `Q = 4(x^3+t)` has degree 3).
Logarithmic differentiation gives
`Delta'/Delta = Q'/Q - sum_{i=1}^N 2/(x-c_i)`, which must equal
`-2s = -sum_{i=1}^N 2/(x-c_i)`, forcing `Q'/Q = 0`, i.e. `Q` constant —
impossible since `deg Q >= 3`. Hence no such `s` exists, so no Riccati
solution in any irreducible quadratic extension.

### Case 3: group is not finite.
Finite PV group implies every solution is algebraic over `K`, hence every
singularity (including infinity) is regular singular. Under `z = 1/x`,
`d/dx = -z^2 d/dz`, `d^2/dx^2 = z^4 D_zz + 2z^3 D_z`, so the equation becomes
`Yz'' + (2/z) Yz' - (z^{-7} + t z^{-4}) Yz = 0`: the coefficient of `Yz`
has a pole of order 7 > 2 at `z = 0` (artifact check: `(-t z^3-1)/z^7`).
Thus infinity is an irregular singularity, and not all solutions are
algebraic. So the group is infinite, not finite.

Conclusion of step 1: the classical PV group is the full `SL2(K0)`.

## Proof, step 2: PPV group is the full constant SL2 (telescoping equation)
With one parameter, Dreyfus Prop 2.8 / Arreche Thm 3.3 ([arXiv:1110.1053]
Prop 2.8, [arXiv:1208.2226] Thm 3.3, eq. (3.3)): when the classical group is
SL2, the PPV group is conjugate to `SL2(M^D)` where `D` is the space of
parameter derivations `d'` for which
`b'''/2 - 2 r b' - r' b = -d'(r)` is solvable in `M(z)`, here `M = K0`.
With `r = x^3+t`, `d' = d/dt` (the only parameter direction up to scale),
`d'(r) = 1`, and with the factor-2 normalization this is
`L[b] := b''' - 4 r b' - 2 r' b = -2`, i.e.
`b''' - 4(x^3+t) b' - 6x^2 b = -2`, sought in `K0(x)`.

Lemma (no rational solution). Let `b in K0(x)` satisfy `L[b] = -2`.
(i) `b` has no finite pole: at a pole `c` of order `m >= 1`,
`b'''` has pole order `m+3` with coefficient `-(m)(m+1)(m+2) != 0`,
while `4rb'`, `6x^2b` have orders `m+1`, `m`; the `b'''/2` term strictly
dominates, so `L[b]` has a pole of order `m+3 >= 4` (artifact valuations:
orders exactly 4,5,6 for `m = 1,2,3`), contradicting the constant RHS.
(ii) `b` is not a non-polynomial rational function; so `b in K0[x]`.
For a monomial `f x^nu` (`f != 0`), `L[f x^nu]` has exact degree `nu+2`
with leading coefficient `-(4nu+6) f != 0` (artifact: verified for
`nu = 0..6`; algebra: `b'''` contributes degree `nu-3`, `-4x^3 b'`
contributes `-4nu f x^{nu+2}`, `-6x^2 b` contributes `-6 f x^{nu+2}`;
sum `-(4nu+6) f x^{nu+2} != 0`). Hence `deg L[b] = deg(b)+2 >= 2` for every
nonzero polynomial `b`, and `L[0] = 0`; neither equals the nonzero constant
`-2`. Contradiction. So no `b in K0(x)` solves the equation.

Therefore `D = {0}`, and the PPV group is conjugate over SL2 to
`SL2(K0^{D}) = SL2(K0)`: the full constant group SL2, defined by the single
algebraic equation `det = 1` and no nontrivial `d/dt`-differential equation.
The Arreche `Pi -> Pi'` reduction is vacuous (reductive quotient already
`Pi`-constant: it is the whole simple group SL2; unipotent radical 0), and
no creative-telescoping operator beyond `L` above is needed.

## Consequence (hypertranscendence)
By the PPV Galois correspondence ([Cassidy-Singer]), absence of any nonzero
`d/dt`-differential polynomial vanishing on the PPV group is equivalent to
`d/dt`-differential transcendence of the generic solution: with `K0`
`d/dt`-differentially closed, the PPV ring is a domain whose fraction field
has `d/dt`-differential transcendence degree `dim_{d/dt}(SL2) = 3`
(parameters of a fundamental matrix modulo `det = 1`); no nonzero
`t`-differential relation over `K` holds. Either disjunct of the target is
thus decided in favor of the first: full constant SL2, hypertranscendent
family, with defining equations exhibited (`det - 1 = 0` only).

## What was computed vs. cited
- Recomputed from scratch with symbolic checks: Riccati residue lemma,
  degree/parity obstructions, quadratic-trace log-derivative sign (`+P/2`),
  residue-2 cancellation (`2a-a^2=0`, `Delta` valuation `>= -1`),
  partial-fraction/degree count (`deg Q = 3+2N`, `Q'/Q != 0`),
  `z = 1/x` irregularity (pole order 7), and the full `L[b]` degree
  (`nu+2`, lc `-(4nu+6)f`) and pole-amplification (`m -> m+3`) analysis.
- Used as black-box classification/oracle (not re-proved): Kovacic's
  four-case theorem; Dreyfus Prop 2.8 / Arreche Thm 3.3 reduction of the
  Zariski-dense case to the single equation `L[b] = -2 d'(r)`; Sit-Cassidy
  classification of Zariski-dense differential-algebraic subgroups of SL2;
  PPV Galois correspondence linking "no defining `d/dt`-equation" to
  hypertranscendence. References: Kovacic [JSC 1986]; van der Put-Singer
  [GTLDE, Ch. 4]; Dreyfus [arXiv:1110.1053] Prop 2.8/Thm 2.10;
  Arreche [arXiv:1208.2226] Thm 3.3 and [Adv. Appl. Math. 2014];
  Cassidy-Singer [IRMA 2007]; Sit [Amer. J. Math. 1975].

## Limitations / scope notes
- The base `d/dx`-constant field is taken `d/dt`-differentially closed
  (standard PPV hypothesis); the computation itself uses only `C(tbar)(x)`.
- The statement is generic in `t` (over the differentially closed constant
  field); no claim is made about specializations `t = t0 in C` (whose
  unparameterized PV group is likewise SL2 by the same Kovacic argument
  with `t0` constant, but that is a separate specialization statement).
- Hypertranscendence is the differential-algebraic consequence via the PPV
  correspondence; analytic incarnations (actual meromorphic fundamental
  matrices, Stokes data) are not addressed.
