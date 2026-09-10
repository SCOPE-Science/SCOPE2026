# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Sharpness floor for the universal thin-shell constant: C* ≥ 8, so the target constant 8 is exactly optimal if valid

## 1. Scope and covering priors (conceded)

Let $X$ range over all isotropic log-concave random vectors in
$\mathbb{R}^n$ ($n \geq 1$): $\mathbb{E}X = 0$,
$\mathrm{Cov}(X) = \mathrm{Id}$, law absolutely continuous with a
log-concave density (or the subspace version).

Covering priors, both conceded in full:

- Klartag–Lehec arXiv:2507.15495, Theorem 1.1:
  $\mathrm{Var}(|X|^2) \leq Cn$ with $C$ universal **unspecified**;
  tightness noted only via Gaussian ($C = 2$) and cube ($C = 4/5$).
- Klartag–Lehec GAFA 2025 (slicing resolution): Guan bound
  $\mathbb{E}\,\mathrm{Tr}[A_t^2] \leq Cn$ with $C$ unspecified and only
  an "absurdly large" extractable explicit constant.

Neither states any explicit single-digit constant. The admitted target was
$\mathrm{Var}(|X|^2) \leq 8n$ via constant-tracked parallel coupling; the
revealed fallback was
$\mathbb{E}\,\mathrm{Tr}[A_t^2] \leq 8n$ uniformly in $t \geq 0$.
**Neither is claimed here** (see §4 for the quantified reason).

## 2. Main result (emergent finding)

Let

$$C^* := \sup_{n \geq 1}\ \sup_{X\ \mathrm{isotropic\ log-concave\ in\ }
\mathbb{R}^n}\ \frac{\mathrm{Var}(|X|^2)}{n} \in (0,\infty]$$

be the optimal universal thin-shell constant (the $O(n)$ order itself is
the conceded Klartag–Lehec theorem).

**Proposition (certified sharpness floor).** $C^* \geq 8$. Explicitly, for
every $n \geq 1$ there exists an isotropic log-concave $X$ in
$\mathbb{R}^n$ with

$$\mathrm{Var}(|X|^2) = 8n\quad\text{exactly}.$$

**Corollary.** The admitted target constant $8$, if the upper bound
$\mathrm{Var}(|X|^2) \leq 8n$ holds, is exactly sharp and cannot be
lowered — already at $n = 1$, and hence universally. In particular the
Gaussian value $2$ is **not** the governing floor; the true floor is at
least $4\times$ larger, correcting the "above the Gaussian floor 2"
framing of the admission to "at the exponential floor 8".

## 3. Proof (self-contained; machine-checked arithmetic)

Fix $n \geq 1$. Let $Y_1,\dots,Y_n \overset{iid}{\sim} \mathrm{Exp}(1)$
(rate 1) and put $X_i = Y_i - 1$, $X = (X_1,\dots,X_n)$.

**Step 1 — 1D moments (exact integers).**
For $Y \sim \mathrm{Exp}(1)$, $\mathbb{E}[Y^m] = m!$. By binomial expansion,

$$\mathbb{E}[X_1^4] = \mathbb{E}[(Y-1)^4]
= \sum_{j=0}^{4}\binom{4}{j}(-1)^{4-j}j!
= 24 - 24 + 12 - 4 + 1 = 9,$$

$$\mathbb{E}[X_1] = 1 - 1 = 0,\qquad
\mathbb{E}[X_1^2] = 2 - 2 + 1 = 1.$$

Hence $\mathrm{Var}(X_1) = 1$ and, since $(\mathbb{E}X_1^2)^2 = 1$,

$$\mathrm{Var}(X_1^2) = \mathbb{E}[X_1^4] - (\mathbb{E}X_1^2)^2
= 9 - 1 = 8.$$

All identities are exact integer arithmetic, replayed by
`output/artifacts/verify_sharpness.py` (PASS).

**Step 2 — isotropy.** The $X_i$ are i.i.d. with mean $0$ and variance $1$,
so $\mathbb{E}X = 0$ and $\mathrm{Cov}(X) = \mathrm{Id}$.

**Step 3 — log-concavity.** $X_1$ has density
$f(x) = e^{-(x+1)}\mathbf{1}_{\{x \geq -1\}}$: support $[-1,\infty)$ is
convex and $\log f(x) = -(x+1)$ is affine, hence concave, on it. The joint
density of $X$ is $\exp(-\sum_i(x_i+1))$ on the convex set
$[-1,\infty)^n$ with linear (hence concave) log-density; i.e. a
tensor product of log-concave laws, log-concave by inspection
(no citation needed beyond the definition).

**Step 4 — variance.** $|X|^2 = \sum_i X_i^2$ with independent summands, so

$$\mathrm{Var}(|X|^2) = \sum_{i=1}^{n}\mathrm{Var}(X_i^2) = 8n.$$

Thus $C^* \geq 8$. ∎

*Sanity checks* (same script): Gaussian $\mathrm{Var}(Z^2) = 3-1 = 2$;
cube 1D uniform gives $9/5-1 = 4/5$; both reproduce the covering paper's
tightness examples, confirming the arithmetic pipeline.

## 4. Why the target / fallback upper bounds are NOT claimed (quantified obstruction)

Re-running Klartag–Lehec §§5–6 with bookkeeping: Corollary 6.1 with the
as-written exponent $\alpha = 1/8$ forces, via
$x_0 = 2^{1/\alpha}(\log(n/k))^{1/\alpha}$,

$$\mathbb{E}\tau_k^{-2} \leq 2^{16}(\log(n/k))^{16} + C',$$

i.e. $\beta = 16$ with $C_2 \geq 2^{16} = 65536$ already from the $x_0^2$
term. Theorem 6.2 then sums $(1+\log(n/k))^{16}$ over $k$ and multiplies
by $e^6$; Bochner (5) multiplies by $4$. The normalized sum converges to
the exact integer

$$I_{16} := \int_0^1 (1-\log u)^{16}\,du
= \sum_{j=0}^{16}\binom{16}{j}j! = 56874039553217,$$

certified by exact integer arithmetic in
`output/artifacts/verify_factorial_blowup.py`. Consequently the
as-written chain certifies at best a final constant

$$\geq 4\cdot e^6\cdot 65536\cdot I_{16}
\approx 6.01\times 10^{21} \gg 8,$$

a gap of $\sim 7.5\times 10^{20}$ even before pinning $C_1, C_3$.
No alternative short route to $\mathrm{Var} \leq 8n$ or to the uniform
Guan certificate $\mathbb{E}\,\mathrm{Tr}[A_t^2] \leq 8n$ was found in the
hour; the fallback needs the same §§5 machinery. Both upper bounds are
therefore explicitly **not** claimed. The obstruction script (PASS)
documents this floor.

## 5. Constant table (all numbers replayable)

| Quantity | Value | Source |
|---|---|---|
| $\mathbb{E}[(Y-1)^4]$, $Y\sim\mathrm{Exp}(1)$ | $9$ exact | binomial + $m!$ |
| $\mathrm{Var}(X_1^2)$ (shifted exp.) | $8$ exact | $9-1$ |
| $\mathrm{Var}(\|X\|^2)$ witness | $8n$ exact | independence |
| Gaussian / cube 1D values | $2$ / $4/5$ | $3-1$ / $9/5-1$ |
| $I_{16}$ | $56874039553217$ exact | $\sum_j\binom{16}{j}j!$ |
| $C_2$ floor ($\alpha=1/8$) | $65536 = 2^{16}$ | $x_0^2$ term |
| As-written chain final-constant floor | $\geq 6.01\times10^{21}$ | $4e^6C_2I_{16}$ |

## 6. Reproducibility log

- `output/artifacts/verify_sharpness.py` — exact-integer witness check +
  Gaussian/cube sanity. Run: `python3 output/artifacts/verify_sharpness.py`. PASS.
- `output/artifacts/verify_factorial_blowup.py` — exact $I_{16}$, finite-$n$
  sums, chain floor. Run: `python3 output/artifacts/verify_factorial_blowup.py`. PASS.
- Full KL paper §§2–6 fetched and line-checked (Bochner (5), Cor 4.5,
  Prop 4.6, Lemmas 5.2–5.5, Prop 5.1 recursion with $C_2 = 8C_1+2$,
  Cor 6.1 $\beta = 16$, Thm 6.2 $e^6$ factor) to anchor the obstruction.
- No subagents used. Only stdlib Python.

## 7. Limitations, conjecture boundary, and originality honesty

- Proved: $C^* \geq 8$ (lower bound, all $n$). **Not** proved: $C^* \leq 8$
  (the target upper bound) or 1D maximality $\mathbb{E}Z^4 \leq 9$ for all
  isotropic log-concave $Z$; the latter was scanned only within the
  two-piece exponential subfamily (kurtosis $\uparrow 9$ from below) and is
  stated as numerical evidence, not a theorem.
- Originality (not overclaimed): the derivation is elementary; independent
  rediscovery by experts is possible. The claim is to the auditable
  certificate, not to depth. At triage level, the covering paper records
  only Gaussian/cube tightness values and the admission union search
  returned no source stating an $8$-floor or any single-digit explicit
  constant; to that checked extent the $8$-floor observation is unrecorded.
  Its value is as a sharpness benchmark: it makes $8$ a forced (not tuned)
  threshold and tells all future constant-tracking that aiming below $8$ is
  futile.
- No new literature search beyond the admitted checked sources plus the
  full fetch of arXiv:2507.15495 is claimed.

## References (covering priors)

- B. Klartag, J. Lehec, *Thin-shell bounds via parallel coupling*,
  arXiv:2507.15495 (2025). Thm 1.1 ($VCn$, $C$ unspecified), §§2–6 chain used for §4.
- B. Klartag, J. Lehec, *Affirmative resolution of Bourgain's slicing
  problem using Guan's bound*, GAFA 2025, DOI 10.1007/s00039-025-00718-w.
  Guan lemma $E\mathrm{Tr}[A_t^2]\le Cn$, "absurdly large" extractable constant.
