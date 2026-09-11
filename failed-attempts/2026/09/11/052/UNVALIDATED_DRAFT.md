# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Primitive-point log BPS number m^P_{-K} = 10 for the smooth degree-2 del Pezzo pair, with the order-2 mixing obstruction

## Claim

Let $X = \mathrm{dP2}$ be the blowup of $\mathbf{P}^2$ at 7 general points and
$E \subset X$ a smooth anticanonical (elliptic) divisor. Let $\beta = -K_X$,
$w = \beta \cdot E = 2$. For a general pair $(X,E)$:

1. **Count.** At any $\beta$-primitive point $P \in E(\beta)$, the genus-0
   maximal-tangency log BPS number is
   $$m^P_{-K} = 10.$$
2. **Vanishing correction.** $\eta := \#\{\text{line classes } l : \beta\cdot l = 0\} = 0$.
3. **Mixing obstruction.** $w_{\mathrm{out}}(X) := \min_{\beta' \text{ effective}} E\cdot\beta' = 1 < 2 = w$.
   Hence any order-2 scattering-diagram coefficient for $(X,E)$ receives
   contributions from all effective classes with $E\cdot\beta' = 2$ (double
   covers of lines, conics, $-K_X$ itself) and cannot equal a single-class
   $N_{-K}$ term. The literal chamber equation
   $\log F_{\mathrm{out}} = N_{-K}\, z^{-2m_{\mathrm{out}}} + \text{higher}$
   is ill-posed at order 2 for this reason, independently of the missing
   toric degeneration.

## Proof

**Numerics.** $K_X^2 = 9 - 7 = 2$, so $w = (-K_X)\cdot E = K_X^2 = 2$.
Arithmetic genus
$p_a(\beta) = \beta(\beta+K_X)/2 + 1 = 0 + 1 = 1$.
Topological Euler number $e(X) = e(\mathbf{P}^2) + 7 = 3 + 7 = 10$.

**$\eta = 0$.** A line class $l$ satisfies $l^2 = -1$, $p_a(l) = 0$; by
adjunction $2p_a - 2 = l^2 + l\cdot K_X$, i.e. $-2 = -1 + l\cdot K_X$, so
$l\cdot K_X = -1$ and $(-K_X)\cdot l = 1 \ne 0$ for *every* line. Thus no
line is orthogonal to $\beta$ and $\eta = 0$. (No enumeration of the 56
lines is needed.)

**Applicability of the log BPS formula.** $\beta = -K_X$ is ample ($X$ is del
Pezzo), hence nef and big, so it contains an integral (indeed smooth) member
(Rocco, cf. Thm 4.7 as used in the source). Since $p_a(\beta) = 1$ and
$\beta \ne -K_{S_8}$ ($X = S_7$), case (2) of Theorem logcalc in
Choi–van Garrel–Katz–Takahashi (arXiv:1810.02377, Thm \ref{thm:logcalc})
applies at any $\beta$-primitive point:
$$m^P_\beta = e(X) - \eta = 10 - 0 = 10.$$
Existence of a $\beta$-primitive point for a general pair $(X,E)$ is their
Proposition \ref{prop:existence} ($\mathbf{Z}/w \times \mathbf{Z}/w$ has
elements of order $w = 2$); the target hypothesis (7 general points, smooth
$E$) is exactly generality. At a primitive point there are no multiple-cover
or reducible-image contributions, so $m^P_\beta$ is a finite weighted curve
count (their Props \ref{prop:logk3contr}(5), \ref{prop:finite}).

**Mixing.** Each line class satisfies $E\cdot l = (-K_X)\cdot l = 1$, so
$w_{\mathrm{out}} = 1$. The Gross–Siebert/Graefnitz wall-log formula
($\log f_{\mathrm{out}} = \sum (D\cdot\beta') N_{\beta'} x^{D\cdot\beta'}$)
sums over *all* classes; the $x^2$ coefficient therefore mixes double covers
of the lines, conics, and $-K_X$. A single-joint order-2 coefficient
($c = |\det(m_1,m_2)|$, $c = 1$ unimodular, via the always-resolvable
Kontsevich–Soibelman/Gross–Pandharipande–Siebert order-2 completion) cannot
be identified with the lone $N_{-K}$ term.

## Sharp boundary of what is (not) claimed

- The **total** invariant $N_{-K} = \sum_{P} N^P_{-K}$ (conjecturally
  $m^{\mathrm{tot}} = w^2 m^P = 40$) requires $P$-independence (Conjecture 1 /
  log-local principle), which Choi et al. prove only for multiples of line,
  conic, and $dh$ classes — *not* for $-K$ of $S_7$. We do **not** claim it.
- We do **not** claim any scattering computation for $(\mathrm{dP2},E)$: the
  Graefnitz toric degeneration does not exist in that form ($-K$ not very
  ample; no degree-2 Gorenstein toric model), and the order-2 joint analysis
  above shows the comparison itself would mix classes.
- The number $m^P_{-K} = 10$ for $S_7$ is not tabulated in the source (whose
  Theorem 1 covers only line/conic/$dh$ classes); it is a new explicit
  specialization with proof.

## Reproducibility

`python3 output/artifacts/verify_emergent.py` prints `EMERGENT_VERIFY_OK`
(exact integer checks of $K^2, w, p_a, e, \eta, m^P, w_{\mathrm{out}} < w$).
`python3 output/artifacts/check_dP2_numerics.py` and
`python3 output/artifacts/recovery_test.py` record the target-side numerics
and the failed bounded recovery (no degeneration object).

## References

- T. Graefnitz, *Tropical correspondence for smooth del Pezzo log Calabi–Yau
  pairs*, arXiv:2005.14018 (degree $\ge 3$ only; very-ample framework).
- J. Choi, M. van Garrel, S. Katz, N. Takahashi, *Log BPS numbers of log
  Calabi–Yau surfaces*, arXiv:1810.02377 (Thm logcalc, Def \ref{def:prim},
  Props existence/logk3contr/finite; Conjecture 1 for line/conic/$dh$).
- Gross–Pandharipande–Siebert / Gross–Siebert scattering completion (order-2
  KS commutator always resolvable).
