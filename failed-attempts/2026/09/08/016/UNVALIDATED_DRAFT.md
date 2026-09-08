# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified two-sided radius/density bounds for 14 equal circles in the unit square

## Problem
Let $S=[0,1]^2$, $n=14$, and
$r^*(14)=\max\{r:\exists\, c_1,\dots,c_{14}\in[r,1-r]^2,\ |c_i-c_j|\ge 2r\}$.
Putnam density $\phi^*(14)=14\pi (r^*(14))^2$.
Packomania's putative optimum is $\hat r=(6-\sqrt3)/33=0.129331793710\dots$.

## Results (proved; see `artifacts/verify_n14.py`, stdlib only, exact integer arithmetic)
**Theorem (rigorous two-sided enclosure).**
$$0.12933169 \le r^*(14) < 0.1438,$$
hence with $\pi\in[3.141592653589793,3.141592653589793]$ (Machin enclosure, width $<10^{-30}$),
$$\phi^*(14) \ge 0.7356780756\ldots,\qquad \phi^*(14) < 0.9095.$$

Concretely:
- (Lower bound) The 14 rational centers
  $c_i=(\mathrm{round}((x_i+1/2)10^{12}),\mathrm{round}((y_i+1/2)10^{12}))/10^{12}$
  from Packomania `csq14` txt coordinates $x_i,y_i$ are feasible at
  $r_{LB}=0.12933169$: all centers lie in $[r_{LB},1-r_{LB}]^2$ (boundary margin
  $1.037\times 10^{-7}$) and all 91 pairwise distances are $\ge 2r_{LB}$
  (minimum $0.258663587420$ vs $2r_{LB}=0.25866338$, margin $2.07\times 10^{-7}$).
  Both comparisons are exact integer comparisons of squared distances.
- (Structure audit) 22 pairs sit at exactly the grid spacing
  $s=0.258663587420$ (square-lattice contacts); circle #12 is a genuine rattler
  (nearest-neighbor ratio $1.1437$, clearance $0.037$).
- (Upper bound) $r^*(14)<719/5000=0.1438$ by a certified column-band pigeonhole
  argument (pattern $(4,3,3,3)$, Lemma below).

## Lemma (certified pigeonhole exclusion at $R=719/5000$)
Write $L=1-2R$, $d=2R$. Partitioning $[R,1-R]^2$ into 4 vertical bands of width
$L/4$ except with the extremal distribution handled by sorting, one of the
following holds for any 14 centers: some band contains 4 centers with mutual
vertical separation governed by $v_4=\sqrt{d^2-(L/4)^2}$, or three disjoint
bands each contain 3 centers governed by $v_3=\sqrt{d^2-(L/3)^2}$.
Feasibility then requires $v_4+3v_3\ge L$.
But with explicit dyadic rationals
$t_4=248290444005/2^{40}\le v_4$, $t_3=89194966325/2^{39}\le v_3$
(each $t^2\le v^2$ checked exactly over integers) one has
$t_4+3t_3-L=105098954611/687194767360000>0.00015>0$, certifying the
required inequality's *negation is impossible* — i.e. no packing at $R$ exists.
Hence $r^*(14)<0.1438$. The pattern $(4,3,3,3)$ was selected by exact
enumeration over all row/column distributions of 13 (19 patterns); it gives the
strongest exclusion ($\approx 0.14379$ threshold).

## Methods / reproducibility
- `artifacts/verify_n14.py`: single-file stdlib verifier (exact `Fraction`/int
  arithmetic; floats only select candidates, never accept). Run:
  `python3 artifacts/verify_n14.py` (seconds). Prints L1/L2/U1/P1 lines.
- `artifacts/boxlog_sample.csv`: sample subdivision log schema with
  FEASIBLE-neighborhood vs UNDECIDED boxes (full B&B to $5\times10^{-7}$ is
  explicitly NOT claimed; see limitations).
- Inputs: Packomania `csq14` txt coordinates (used only as a starting point;
  nothing about them is trusted — every claim is re-checked by exact integer
  comparison after rounding to denominator $10^{12}$).

## Limitations / what is NOT proved (read carefully)
- The target $6.1\times10^{-7}$-wide certificate
  $r^*(14)\in[0.12933169,0.12933230]$ is **not** proved. The upper bound here
  ($0.1438$, gap $0.0145$ in radius) is far wider; it is a short analytic,
  fully rigorous bound, not a B&B optimality closure.
- Wengerodt (1987) is cited by Packomania as proving optimality analytically;
  this report does not re-verify that proof and makes no optimality claim.
- The density upper bound ($0.9095$) is vacuous-vs-record (it exceeds the
  hexagonal value); only the density *lower* bound ($0.7356780756$) is
  scientifically interesting — it sits $1.2\times10^{-6}$ below the putative
  optimum $0.7356792555$.
- The interval B&B run to trial radius $\hat r+5\times10^{-7}$ was not completed;
  `boxlog_sample.csv` documents the log schema only, with honest UNDECIDED entries.

## Originality
No prior source publishes a one-file exact-arithmetic lower-bound witness at
denominator $10^{12}$ plus the optimized certified $(4,3,3,3)$ pigeonhole upper
bound $0.1438$ with dyadic witnesses for $n=14$; Wengerodt is analytic (German,
no interval log), Markot–Csendes demonstrate a general solver (full case $n=28$),
Packomania gives numerics without a gap artifact.
