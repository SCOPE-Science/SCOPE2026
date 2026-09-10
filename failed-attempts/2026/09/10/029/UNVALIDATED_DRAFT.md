# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Critical truncation and sparse-large-entry control for Pareto-4.5 Wigner edges

## 1. Ensemble and result

Let `x` be standardized symmetric Pareto with exponent `alpha = 9/2`:
`|x| = Y`, `S*x` with `S` Rademacher independent, `P(Y > t) = (x_m/t)^{9/2}`,
`t >= x_m`, where `E[Y^2] = (9/5) x_m^2 = 1`, i.e. `x_m^2 = 5/9`,
`x_m = sqrt(5)/3 = 0.7453559925`. Tail constant `c0 = x_m^{9/2} = 0.2664629696`.
Then `E[x] = 0`, `E[x^2] = 1`, `E[x^4] = 25/9`, and `s^4 P(|x| >= s) -> 0`
(Lee-Yin universal regime, qualitative only). Consider `M = N^2` i.i.d. copies
`x_i` (the rescaled Wigner entries `sqrt(N) H_{ij}`).

**Critical truncation.** `T* = N^{34/81}`. Bad entries `B = #{i : |x_i| > T*}`.
Window `w = N^{-5/9}`.

**Theorem (sparse-large-entry control).**
With `Y_i = x_i^2 1_{|x_i|>T*}`, `Z_i = |x_i| 1_{|x_i|>T*}`:

- (T1) `P(B > 3 N^{1/9}) <= N^{-1}` for all `N >= 2`.
- (T2) `P((1/N^2) sum Y_i > N^{-5/9}) <= N^{-1}` for all `N >= 22`.
- (T3) `P((1/N^{3/2}) sum Z_i > N^{-5/9}) <= N^{-1}` for all `N >= 4`.

**Proposition (criticality).** `tau* = 34/81` is the unique minimal truncation
exponent such that (a) the bad-entry count is `<= O(N^{1/9})` (the number of
edge eigenvalue spacings `N^{-2/3}` that fit in the window `N^{-5/9}`), while
(b) both bad-mass scales sit below the window. The count constraint binds:
`34/81 > 24.4/81 > 18/81` (first-order mass, quadratic mass). See Section 4.

**Remark (sharpness of method).** Second moments do not suffice for (T2):
the `m = 2` majorant gives `2.628 N^{-80/81}`, missing `N^{-1}` by `N^{1/81}`;
third moments are necessary and sufficient here. Verified numerically.

## 2. Tail integrals (Lemma)

For `k != 9/2`, `E[|x|^k 1_{|x|>T}] = C_k T^{k-9/2}` with
`C_k = 4.5 c0/|k-4.5|`, `T >= x_m`, by direct integration of
`f_{|x|}(t) = 4.5 x_m^{9/2} t^{-11/2}`:
`int_T^inf t^k f(t) dt = 4.5 x_m^{9/2} T^{k-9/2}/|k-9/2|`.
Needed: `E[Y]=1.8c0 T^{-5/2}=0.47963335 T^{-5/2}`,
`E[Y^2]=9c0 T^{-1/2}=2.39816673 T^{-1/2}`,
`E[Y^3]=3c0 T^{3/2}=0.79938891 T^{3/2}`,
`E[Z]=(9/7)c0 T^{-7/2}=0.34259525 T^{-7/2}`, `E[Z^3]=3c0 T^{-3/2}`.
Per-entry exceedance `p = P(|x|>T*) = c0 T*^{-9/2} = c0 N^{-17/9}`.

## 3. Proofs

**(T1).** `B ~ Binomial(M, p)`, `mu = E[B] = c0 N^{1/9}`.
Chernoff: `P(B >= (1+d)mu) <= (e^d/(1+d)^{1+d})^mu` (from
`E[e^{tB}] = (1-p+pe^t)^M <= e^{mu(e^t-1)}`, optimize `t`).
Take `(1+d)mu = 3N^{1/9}`, i.e. `1+d = 3/c0 = 11.258600`.
Bound `= exp(-K1 N^{1/9})`, `K1 = c0((1+d)\ln(1+d)-d) = 4.529860`.
`K1 y - 9\ln y >= 2.821 > 0` for all `y = N^{1/9} >= 2^{1/9}`
(minimum at `y = 9/K1 = 1.9868`, in domain), so the bound is `<= N^{-1}`.

**(T2).** `E[(sum Y_i)^3] = M E[Y^3] + 3M(M-1)E[Y^2]E[Y] + M(M-1)(M-2)E[Y]^3`
`<= (0.79938891 + 3.45064449 + 0.11033440) N^{231/81} = 4.360450 N^{231/81}`
(using `T*^{-5/2}=N^{-85/81}`, `T*^{-1/2}=N^{-17/81}`, `T*^{3/2}=N^{51/81}`:
terms scale as `N^{213/81}, N^{222/81}, N^{231/81}`, dominated by the last).
Markov: `P((1/N^2)sum Y > w) <= 4.360450 N^{231/81}/(N^2 w)^3`
`= 4.360450 N^{-120/81} <= N^{-1}` iff `N^{39/81} >= 4.360450`, i.e. `N >= 22`
(`21^{39/81} = 4.331 < 4.360450 <= 22^{39/81} = 4.428`).

**(T3).** Same expansion for `Z`:
`E[(sum Z)^3] <= (0.79938891 + 0.49290000 + 0.04021000) N^{129/81}`
`= 1.332560 N^{129/81}` (terms `N^{111/81}, N^{120/81}, N^{129/81}`).
`P((1/N^{3/2})sum Z > w) <= 1.332560 N^{129/81}/(N^{3/2}w)^3`
`= 1.332560 N^{-100.5/81} <= N^{-1}` iff `N^{19.5/81} >= 1.332560`,
i.e. `N >= 4` (`3^{19.5/81} = 1.3028 < 1.332560 <= 4^{19.5/81} = 1.3962`).

## 4. Criticality computation

Bad-count scale `N^{2-4.5 tau} <= N^{1/9}` iff `tau >= (2-1/9)/4.5 = 34/81`.
Quadratic-mass mean scale `T^{-5/2} = N^{-2.5 tau} <= N^{-5/9}` iff
`tau >= (5/9)/2.5 = 2/9 = 18/81`. First-order-mass mean scale
`N^{1/2}T^{-7/2} <= N^{-5/9}` iff `tau >= (1/2+5/9)/3.5 = 19/63 = 24.4/81`.
Hence `34/81 > 19/63 > 2/9`: the interlacing-count constraint binds, and
`tau* = 34/81` is the minimal truncation exponent satisfying all three;
any smaller `tau` breaks the count, any larger one needlessly fattens the
truncated support (`Q = N^tau`) for the downstream local law.

## 5. Route-obstruction ledger (context for the target TW rate)

For the full `N^{-1/18}` Kolmogorov target with coincidence truncation
`tau = 37/81`: entrywise 4th-order Lindeberg remainder
`E_comp <= M5(T) D5/(120 N^{1/2})`, `M5(T) <= 2.3982 T^{1/2}`, forces
`s
...[truncated 1790 chars]