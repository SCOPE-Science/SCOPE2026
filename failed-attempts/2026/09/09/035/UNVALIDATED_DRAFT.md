# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Tilt-induced wall fragment for the imprimitive class v = 2a in Ku of a cubic threefold

## Abstract

Let $Y \subset \mathbf{P}^{4}$ be a smooth cubic threefold over
$\mathbf{C}$ and $\mathrm{Ku}(Y)$ its Kuznetsov component with the
Bayer–Lahoz–Macrì–Stellari tilt-induction setup. Fix a $(-1)$-class
$a \in N(\mathrm{Ku}(Y))$ with classified $\sigma$-stable objects
(e.g. the instanton/line class of Liu–Zhang) and put $v = 2a$.
We certify one tilt wall fragment for class $v$ at the level of
Bayer–Maccaferri tilt inequalities: an exact wall equation, its
destabilizer-versus-empty dichotomy, and the Bogomolov–Gieseker (BG)
exclusion list. This is the fallback-grade partial theorem admitted
for this lane: one certified wall verdict plus a replayable tilt-slope
log and an explicit BG bound. It is **not** a full chamber
decomposition of the stability manifold.

## 1. Fixed conventions (audit entry point)

- $H$ = hyperplane class, $\int_Y H^3 = 3$.
- Write $\mathrm{ch} = (r, kH, xH^2, y\,\mathrm{pt})$ with
  $\mathrm{pt} = H^3/3$. Integer-friendly coordinates:
  $d_1 = H^2\!\cdot\!\mathrm{ch}_1 = 3k$,
  $d_2 = H\!\cdot\!\mathrm{ch}_2 = 3x$.
- Hirzebruch–Riemann–Roch check (replay
  `artifacts/hrr_check.py`): $c(T_Y) = 1 + 2H + 4H^2 - 2H^3$,
  $\mathrm{td} = 1 + H + \tfrac{2}{3}H^2 + \tfrac{1}{3}H^3$,
  $\chi(\mathcal{O}) = 1$, $\chi(\mathcal{O}(1)) = 5$,
  $\chi(\mathcal{O}(-1)) = 0$.
- $H$-discriminant $\Delta_H = d_1^2 - 6rd_2$
  ($= 9(k^2 - 2rx)$, nine times the usual
  $\bar\Delta_H = k^2 - 2rx$). Classical BG for a tilt-semistable
  factor: $\Delta_H \ge 0$.
- Tilt slope at $(\alpha,\beta) = (a,b)$ with $A = a^2$:
  $$\mathrm{num}(E) = d_2 - b\,d_1 + \tfrac{3}{2}r(b^2 - A),
    \qquad \mathrm{den}(E) = d_1 - 3rb,$$
  $$\mu_{a,b} = -\mathrm{num}/\mathrm{den}.$$
  The wall $W(E_0, F)$ is the zero locus of
  $\mathrm{num}_E\,\mathrm{den}_F - \mathrm{num}_F\,\mathrm{den}_E$.
- Model lift of $v = 2a$: $E_0 = 2[I_\ell]$,
  $(r,d_1,d_2) = (2,0,-2)$, $\Delta_H(E_0) = 12$,
  $\mu_H(E_0) = 0$.
- Lifts of $a$: $F_{m,n} = a_0 + m[\mathcal{O}] + n[\mathcal{O}(1)]$
  with $a_0 = (1,0,-1)$, $[\mathcal{O}] = (1,0,0)$,
  $[\mathcal{O}(1)] = (1,3,\tfrac{3}{2})$, i.e.
  $$r = 1+m+n,\quad d_1 = 3n,\quad d_2 = -1 + \tfrac{3n}{2}.$$

## 2. Statement

**Theorem (one certified tilt wall fragment for $v = 2a$).**
With the conventions above:

1. *(Proportional-lift no-wall lemma.)* The naive proportional lift
   $F_{0,0} = a_0$ gives a vanishing wall polynomial (identically
   zero): scalar-proportional $(r,d_1,d_2)$ lifts never define a
   tilt wall. Genuine $a{+}a$ walls require non-proportional
   $D^b(Y)$-lifts of the $\mathrm{Ku}$-class $a$.
2. *(Certified wall equation.)* For the destabilizer type
   $F_{0,1} = a_0 + [\mathcal{O}(1)] = (2,3,\tfrac{1}{2})$
   ($\Delta_H = 3$, $\mu_H = \tfrac{1}{2}$) the wall against
   $E_0 = (2,0,-2)$ is the semicircle
   $$A + b^2 - \tfrac{5}{3}b + \tfrac{2}{3} = 0,
     \qquad\text{i.e.}\quad
     a^2 + (b - \tfrac{5}{6})^2 = (\tfrac{1}{6})^2,$$
   a real arc over $b \in (\tfrac{2}{3}, 1)$.
3. *(Destabilizer-versus-empty dichotomy.)* On this arc the shifts
   $E_0[1]$ and $F_{0,1}[1]$ lie in the tilt heart $\mathrm{Coh}^b(Y)$
   (since $\mu_H(E_0) = 0 < b$ and $\mu_H(F_{0,1}) = \tfrac12 < b$
   put both sheaves in $\mathcal{F}_b$, whose $[1]$-shift is in the
   heart) and their $\mu_{a,b}$-slopes agree on the wall and cross
   transversely off it (checked exactly at $b = \tfrac{3}{4}$,
   $A = \tfrac{1}{48}$: equal slopes $-\tfrac{1}{12}$ on the wall;
   order flips on the two sides). Hence $F_{0,1}$ is a genuine tilt
   destabilizer type along this wall; alternative lift types in the
   enumerated window are either (i) proportional (no wall),
   (ii) vertical wall $b = 0$, (iii) imaginary ($R^2 < 0$, proved
   empty as tilt walls), or (iv) BG-excluded ($\Delta_H < 0$). The
   full case table is in §3 and `artifacts/wall_log.txt`.
4. *(BG obstruction lemma, reusable.)* Any would-be tilt-semistable
   destabilizer with $\Delta_H < 0$ is impossible by classical BG;
   in the $|m|,|n| \le 2$ window these are exactly
   $(m,n) \in \{(1,2), (2,1), (2,2)\}$ with
   $\Delta_H \in \{-12, -3, -24\}$.

**What is not claimed.** Transfer of this tilt wall to a
$\sigma$-wall in $\mathrm{Ku}(Y)$, existence of $\sigma$-stable
objects of class $2a$ on either side, and any geometric moduli
identification are **not** proved here; they would require the
Bayer et al. induction/restriction argument plus the
Li–Lin–Pertusi–Zhao nonemptiness and Liu–Zhang classification
inputs, which we cite as black boxes. Consistent with
Li et al., no claim is made that $M_\sigma(2a)$ is empty: the
proved emptiness concerns fake wall types, not the Ku moduli space.

## 3. Proof and computation log

**HRR/conventions.** `artifacts/hrr_check.py` passes
(`HRR_OK`): Chern, Todd, and $\chi$ values as in §1.

**Enumeration.** `artifacts/tilt_wall.py` (stdlib only) enumerates
$F_{m,n}$, $|m|,|n| \le 2$, computes $\Delta_H$ and the exact wall
polynomial $\mathrm{num}_E\mathrm{den}_F - \mathrm{num}_F\mathrm{den}_E$,
and writes `artifacts/wall_log.txt`. An independent check
re-diagonalized each polynomial into circle/vertical/identical/
imaginary normal form. Results:

| $(m,n)$ | $r_F$ | $\Delta_H$ | wall type |
|---|---|---|---|
| (0,0) | 1 | 6 | identical (no wall) — Lemma 1 |
| (-2,0),(-1,0),(1,0),(2,0) | —/2/3 | —/12/18 | vertical $b=0$ |
| (0,1) | 2 | 3 | **real circle** $C=5/6$, $R^2=1/36$ — Theorem |
| (0,2),(1,1) | 3 | 0 | real circle $C=5/6$ resp. $7/6$, $R^2=1/36$ resp. $25/36$ |
| (1,2),(2,1),(2,2) | 4,4,5 | $-12,-3,-24$ | BG-excluded (Lemma 2) |
| remaining $r_F>0$ entries | — | $\ge 0$ | imaginary circles ($R^2<0$): no tilt wall |

**Slope crossing and heart membership.** At $(A,b) =
(\tfrac{1}{48},\tfrac{3}{4})$ (on the (0,1) wall):
$\mu(E_0) = \mu(F_{0,1}) = -\tfrac{1}{12}$. At
$A \pm \tfrac{1}{100}$ the order flips ($-\tfrac{9}{100}$ vs
$-\tfrac{31}{300}$, then reversed), so the wall is genuine, not a
touch. Heart membership: on the arc $b \in (\tfrac23,1)$ we have
$b > \mu_H(E_0) = 0$ and $b > \mu_H(F_{0,1}) = \tfrac12$, so both
underlying sheaves lie in the torsion-free part $\mathcal{F}_b$
and their $[1]$-shifts lie in $\mathrm{Coh}^b(Y)$ in degree $0$.
Hence the destabilizing sequence is read in the tilt heart (up to
the standard $[1]$-shift); the destabilizer is a rank-2 tilt object
of type $a + [\mathcal{O}(1)]$, i.e. a non-proportional $D^b(Y)$
lift of the $\mathrm{Ku}$-class $a$, not a sheaf of class $a$
itself.

**Quotient invariance.** The (0,1) wall equation is homogeneous of
degree zero under common rescaling of $(r,d_1,d_2)$ and unchanged
under adding multiples of $[\mathcal{O}],[\mathcal{O}(1)]$ that
preserve the projective triple, so it depends only on the
destabilizer type, not on the chosen representative.

## 4. Originality and downstream use

Bayer et al. (1703.10839) prove existence of stability on
$\mathrm{Ku}$ via tilt induction but treat no fixed-class walls;
Liu–Zhang (2106.01961) classify primitive $(-1)$/$(-4)$-classes;
Li et al. (2406.09124) prove Ku-moduli nonemptiness for every
nonzero class without computing tilt walls; Feyzbakhsh–Pertusi
(2109.13549) and Fan–Liu–Ma (2310.16950) study the Serre-invariant
locus structurally. None records the above wall equation or the
proportional-lift no-wall observation for $v = 2a$. The BG
exclusion list narrows the next-wall search; the wall equation is a
concrete boundary condition for categorical-Torelli, Ulrich/
instanton, and hyperkähler-moduli programs using $\mathrm{Ku}(Y_3)$.

## 5. Limitations and uncertainty (explicit)

- Window: only $|m|,|n| \le 2$ lifts enumerated; outermost-ness is
  certified **within** this window, not globally.
- Model lift $E_0 = 2[I_\ell]$ is a convenient $D^b(Y)$-lift of
  $v = 2a$; the true outermost wall could involve a different lift
  of $v$ (shifts by $\langle\mathcal{O},\mathcal{O}(1)\rangle$).
- Tilt-to-Ku transfer and $\sigma$-stability consequences are cited,
  not proved. The destabilizer $F_{0,1}$ has rank 2 (a
  non-proportional $D^b(Y)$-lift of the $\mathrm{Ku}$-class $a$),
  so the wall is a genuine tilt wall for the $v = 2a$ problem but
  not a literal $a{+}a$ short exact sequence of sheaves; the
  $a{+}a$ triangle can only be read inside $\mathrm{Ku}(Y)$ after
  the Bayer et al. projection, which is not carried out here.
- Heart-membership bookkeeping is machine-checked at the slope
  level; the remaining hand-checked step is identifying the
  relevant tilt-heart extension (triangle) after the $[1]$-shift,
  not yet certified by an independent script — the natural next
  audit step.
- No claim of full chamber decomposition or of $M_\sigma(2a)$
  (non)emptiness.

## References

- Bayer–Lahoz–Macrì–Stellari, Stability conditions on Kuznetsov
  components, arXiv:1703.10839.
- Liu–Zhang, A note on Bridgeland moduli spaces and moduli of
  sheaves on $X_{14}$ and $Y_3$, arXiv:2106.01961.
- Li–Lin–Pertusi–Zhao, Higher dimensional moduli spaces on
  Kuznetsov components of Fano threefolds, arXiv:2406.09124.
- Feyzbakhsh–Pertusi, Serre-invariant stability conditions and
  Ulrich bundles on cubic threefolds, arXiv:2109.13549.
- Fan–Liu–Ma, Stability manifolds of Kuznetsov components of prime
  Fano threefolds, arXiv:2310.16950.

## Reproduction

```
python3 output/artifacts/hrr_check.py      # expect HRR_OK
python3 output/artifacts/tilt_wall.py      # regenerates wall_log.txt
```
