# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified pole-free tube for homogeneous Painlevé-II on [4.9, 5] via a validated Airy box and a Picard contraction

## Claim
For homogeneous Painlevé-II $w'' = 2w^3 + xw$ ($\alpha=0$) on the real line,
with $x_0 = 5$ and $h = 1/10$:

1. **Validated Airy far-field box.** With $\zeta=(2/3)x^{3/2}$,
   $p(x) = e^{-\zeta}/(2\sqrt{\pi}\,x^{1/4})$,
   $p_2(x) = x^{1/4}e^{-\zeta}/(2\sqrt{\pi})$, $u_1=5/72$, $u_2=385/10368$,
   $v_2=-(13/11)u_2$:
   $$\mathrm{Ai}(5) \in P\cdot(1+R_1),\quad R_1\in[-u_1/\zeta,\,0],$$
   $$\mathrm{Ai}'(5) \in -P_2\cdot(1+7/(72\zeta)+S_2),\quad
     S_2\in[v_2/\zeta^2,\,0],$$
   where the prefactor intervals $P\ni p(5)$, $P_2\ni p_2(5)$ are the rigorous
   rational intervals computed in `farfield_tube.py` (square roots via verified
   `isqrt`, $\pi$ via the Machin formula with alternating-series remainder,
   $e^{-\zeta}$ via Taylor order 40 with Lagrange remainder, valid since the
   enclosed $\zeta(5)\subset(7,8)$). Numerically
   $$\mathrm{Ai}(5)\in[1.08279777\times10^{-4},\,1.09298103\times10^{-4}],$$
   $$\mathrm{Ai}'(5)\in[-2.47585848\times10^{-4},\,-2.47392790\times10^{-4}].$$
   Authority: DLMF §9.7(iii) — for real $x>0$, the $n$th error term of (9.7.5)
   is bounded by the first neglected term with the stated sign whenever the
   following term has opposite sign ($n\ge 0$ for Ai, $n\ge 1$ for Ai');
   the required Leibniz decrease at $x=5$ is verified by exact rational
   inequalities ($u_1\zeta\ge u_2$ and $(13/11)u_2\zeta\ge(19/17)u_3$,
   asserted in the script).
2. **Pole-free tube.** Let $M_0=1/5000$, $M_1=1/2000$,
   $B_2 = 2M_0^3+5M_0 = 62500001/62500000000$.
   For **every** Cauchy datum $(w(5),w'(5))$ in the above Airy box, the PII
   initial-value problem has a unique $C^2$ solution on the whole closed
   segment $[4.9,5]$, satisfying $|w|\le M_0$, $|w'|\le M_1$ there; in
   particular it is pole-free on $[4.9,5]$. The solution at $x=4.9$ lies in
   the box expanded by the logged remainders $r_w = hM_1 = 1/20000 = 5\times
   10^{-5}$ and $r_v = hB_2 = 62500001/625000000000 \approx 1.000000002\times
   10^{-4}$ about the datum box.
3. **Proof (Banach/Picard).** On the box, $|2w^3+xw|\le B_2$ for $x\le 5$ and
   the vector field $(v,\,2w^3+xw)$ is Lipschitz with constant
   $L = 6M_0^2+5 = 62500003/12500000$. The script verifies the self-mapping
   inequalities (datum box expanded by $hM_1$, resp. $hB_2$, stays inside
   $[-M_0,M_0]\times[-M_1,M_1]$) and the contraction $hL = 0.500000024 < 1$
   by exact rational arithmetic. Hence the Picard map is a contraction of the
   closed ball of $C^1$ paths on $[5-h,5]$ staying in the box, giving existence,
   uniqueness, and the tube.
4. **Replay.** `remainder_log.json` archives every rational endpoint
   ($\zeta$, Ai(5), Ai'(5), $M_0$, $M_1$, $B_2$, remainders, contraction
   constant, series coefficients, $\pi$ enclosure, check list).
   `verify.py` (stdlib only) replays all inequalities from the committed
   rationals, recomputes the full rigorous chain from scratch, confirms the
   recomputed boxes are subsets of the committed boxes, and cross-checks that
   the boxes contain the 80-digit reference values
   ($\mathrm{Ai}(5)=1.08334428\ldots\times10^{-4}$,
   $\mathrm{Ai}'(5)=-2.47413890\ldots\times10^{-4}$); it prints `VERIFY_OK`.

## Scope and limitations
- This is preset-fallback clause (a) only: a single-ray pole-free tube with
  remainder logs. It does **not** prove Hastings–McLeod membership of the
  trapped solutions, **not** extract any Stokes-multiplier interval, and
  **not** extend toward any maximal tritronquee sector angle.
- The tube is local ($h=1/10$); the contraction margin $hL\approx 0.5$ allows
  modest extension, not attempted here.
- "Airy-type far-field box" means the DLMF-enclosed Airy values above; the
  further claim that the Hastings–McLeod solution's datum lies in this box is
  **not** established (that would require the decaying-solution fixed-point
  argument on $[5,\infty)$, left open).
- All rigor is in exact rational (`Fraction`) interval arithmetic with outward
  rounding; no floating-point step is part of the proof (floats appear only as
  display and in the non-proven reference cross-check).

## Prior work (separation)
Huang–Xu–Zhang (1410.3338) prove Hastings–McLeod pole-free sectors by hand-built
quasi-solutions with no validated-numerics tube or replay logs; Bertola–Cafasso
(1101.3997) is analytic Riemann–Hilbert for noncommutative PII; Cleri–Dunne
(2002.06270) is formal trans-series; Dai–Xu–Zhang (1908.01532) is analytic
Stokes-parametrised integrals; Costin–Huang–Tanveer (1209.1009) is P-I. None
records or mechanically implies this machine-checkable tube; the interval
enclosure layer is the new contribution.
