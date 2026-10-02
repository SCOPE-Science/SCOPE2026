# Certified divisorial beta values for smooth rank-3 degree-14 Fano threefolds

## Context

K-stability of smooth Fano threefolds (105 Mori–Mukai families) is the open
classification program after Chen–Donaldson–Sun and Blum–Xu, feeding K-moduli
compactifications, Sarkisov rigidity, and Kähler–Einstein existence.
Belousov–Loginov (arXiv:2403.03700, v3, June 2026) proved that every
**general** smooth Fano threefold of Picard rank 3 and degree 14 is K-stable
under an explicit generality condition $(\star)$ on multiple fibres of the
conic bundle $\pi$ (A1 singularities along $C$ in the containing $F_2$
fibre), and stated they expect all such threefolds to be K-stable but are
"unable to prove this at the moment." The complementary special
(non-$(\star)$) stratum is therefore explicitly left open. The result below
is the strongest verifiable fragment (the pre-registered fallback (a)):
exact divisorial beta-invariants valid uniformly over that stratum, with a
documented obstruction for the remaining full K-verdict.

## Definitions

Let $X$ be a smooth Fano threefold of Picard rank 3 with $(-K_X)^3 = 14$,
realised as in Belousov–Loginov §3: $D \simeq \mathbf{P}^1\times\mathbf{P}^1$
with $\mathcal{O}_D(D)=\mathcal{O}(-1,-1)$; $F_1, F_2$ general fibres of the
del Pezzo fibrations $\pi_1, \pi_2$ (degrees 6 and 3);
$-K_X \sim D + F_1 + 2F_2$;
$\overline{\mathrm{Eff}}(X)=\langle D,F_1,F_2\rangle$ (Matsuki + erratum);
uniform intersection numbers
$D^3=2$, $D^2{\cdot}F_1=-2$, $D^2{\cdot}F_2=-1$,
$D{\cdot}F_1{\cdot}F_2=2$, $F_i$-pure triple products zero.
For a prime divisor $E$ over $X$,
$S_X(E)=\frac{1}{(-K_X)^3}\int_0^{\tau(E)}\mathrm{vol}(-K_X-uE)\,du$,
$\beta_X(E)=A_X(E)-S_X(E)$ with $A_X=1$ for smooth prime divisors.

## Result (partial theorem)

Let $X$ be as above (hence in particular any smooth member of the special
stratum excluded by condition $(\star)$). Then:

1. $S_X(F_1) = 45/112$ and $\beta_X(F_1) = 67/112 > 0$ (**new certified value**).
2. $S_X(D) = 17/28$ and $\beta_X(D) = 11/28 > 0$ (**new certified value**).
3. $S_X(F_2) = 45/56$, $\beta_X(F_2)=11/56 > 0$ (reproduction of
   Belousov–Loginov Prop 5.2; not claimed as new).
4. For $P \in D$ with $Z \subset D$ a $(1,0)$-divisor through $P$,
   $S(W^{D,Z}_{\bullet,\bullet};Z)=S(W^{D,Z}_{\bullet,\bullet,\bullet};P)=45/56$
   (reproduction of Belousov–Loginov Lemma 6.1; not claimed as new), hence
   $\delta_P(X) \ge 56/45 > 1$.

Items 1–2 are the original contribution. Items 3–4 are independently
re-verified consistency checks with explicit non-originality labels.

## Proof / evidence

Uniform volume law from the intersection table: for $c,a,b\in\mathbf{Q}$,
$(cD+aF_1+bF_2)^3 = 2c^3-6c^2a-3c^2b+12cab$; at $(1,1,2)$,
$(-K_X)^3 = 2-6-6+24 = 14$.

$F_1$ (from BL Prop 5.1 Zariski data): $-K_X-uF_1$ ample for $0\le u<1/2$
(dots $1$, $1-2u$, $2$ on $L_1,L_2,C$);
for $1/2\le u\le 1$, $P(u)=(2-2u)D+(1-u)F_1+2F_2$, $N(u)=(2u-1)D$.
Volumes $14-18u$ on $[0,1/2]$ (integral $19/4$) and $-8t^3+24t^2$,
$t=1-u$, on $[1/2,1]$ (integral $7/8$); tau-endpoint volume at $u=1$ is 0.
$S_{F_1}=(19/4+7/8)/14=45/112$, $\beta=67/112$.

$D$: $-K_X-uD=(1-u)D+F_1+2F_2$ has dots $1+u$ on $L_{1,2}$ and $2-2u$ on $C$,
hence nef on $[0,1]$ with $N(u)=0$. $D,F_1,F_2$ are an $N^1(X)$ basis
($(D,F_1,F_2)\times(L_1,L_2,C)$ matrix determinant $-4\ne 0$) generating the
simplicial $\overline{\mathrm{Eff}}(X)$, so $u>1$ is not pseudo-effective:
$\tau(D)=1$. Volume $2t^3-12t^2+24t$, $t=1-u$, integrates to $17/2$;
$S_D=(17/2)/14=17/28$, $\beta=11/28$.

$F_2$ and the $D$-flag are replayed from BL Props 5.2/Lemma 6.1 with the same
volume law, yielding $45/56$ in each case (flag: $R=(u-v+1,u+1)$,
$R^2=2(u-v+1)(u+1)$, $\frac{3}{14}\int_0^1(u+1)^3du=45/56$ twice since $N=0$).
The stdlib-only script `artifacts/verify_beta.py` replays every integral and
identity with exact `Fractions` arithmetic (`VERIFY_OK`); no floating point,
no external packages.

## Limitations

Full K-(poly)stability of the special stratum is NOT proved. The remaining
obstruction is the $W^{F_2,C}$ volume function for worse-than-$A_1$
multiple fibres ($A_3$/$D_m$ along $C$), which BL Lemma 7.1 does not cover;
BL §§6–7 give $\delta\ge 1$ (not $>1$) at nodal $F_1\cap F_2$ points. No
destabilizing valuation ($\beta<0$) and no equivariant degeneration were
found. The $D$-flag bound applies only to points on $D$. Zariski/Mori/Eff
inputs are imported from Belousov–Loginov §3/§5 and Matsuki (+erratum),
checked here for kink consistency and endpoint vanishing but not re-derived
from defining equations.

## Reproducibility

Run `python3 artifacts/verify_beta.py` (Python 3 stdlib only); expect
`VERIFY_OK` with $S(F_1)=45/112$, $S(D)=17/28$, $S(F_2)=45/56$, flag
$45/56$ twice.

## References

- G. Belousov, K. Loginov, K-stability of Fano threefolds of rank 3 and
  degree 14, arXiv:2403.03700 v3 (Jun 2026), §§3–8.
- H. Abban, Z. Zhuang, K-stability of Fano varieties via admissible flags,
  arXiv:2003.13788 (method; no stratum verdict).
- C. Araujo et al., The Calabi problem for Fano threefolds (flag-formula
  source for Props 4.2–4.4).
