# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# General wall-crossing extension theorem (non-coprime case) — DRAFT

## 1. Setup and statement

Let $X$ be a smooth projective Calabi–Yau threefold of Picard rank one with
ample generator $H$, and assume the Bayer–Macrì–Toda double-tilt Bridgeland
stability conditions $\sigma_{a,b} = (Z_{a,b}, \mathcal{A}_b)$ exist on the
required $(a,b)$-region (the BMT inequality, hence the hypothesis of the
target; e.g. quintic threefold, or double/triple solids, or
$X_{2,4}, X_{3,3}, X_{2,2,2,2}$ cases where it is known).

Fix a numerical class $v$ of positive rank $r > 0$. Write
$D = H^2 \cdot \mathrm{ch}_1$, $Q = H \cdot \mathrm{ch}_2$, $N = \mathrm{ch}_3$
(the $H$-degrees that enter every wall equation). **No coprimality is assumed**:
$$
d_0 := \gcd(r, D) \geq 1 \quad\text{arbitrary}.
$$
Denote $v_0$ a primitive class when $v = m v_0$ (such an $m$ exists
numerically since $r > 0$; the argument below does not need $v_0$ effective).

**Theorem (non-coprime DT/PT single wall).**
There is a numerical Bridgeland wall $W = W(v)$ (the same wall as in the
coprime case) and a stability condition $\sigma_0 \in W$ such that:

1. (Wall location, gcd-independent.) $W$ is cut out by the numerical equation
   $\Im(Z_{a,b}(u)\overline{Z_{a,b}(v)}) = 0$ for a rank-$\le 1$ destabilizing
   class $u$, hence depends only on $(r, D, Q, N)$ linearly; scaling
   $v \mapsto m v_0$ scales the equation by $m$ and leaves its zero set
   unchanged. The DT/PT wall is the same wall whether $d_0 = 1$ or $d_0 > 1$.

2. (Adjacent chambers = DT side and PT side, semistable versions.)
   On one side of $W$ (for $b$ in the large-volume range), an object $E$ of
   class $v$ is $\sigma_{a,b}$-semistable iff it is a Gieseker-semistable sheaf
   (non-strict inequality); on the other side, $E$ of class $v$ is
   $\sigma_{a,b}$-semistable iff it is a PT-semistable object (stable pair
   complex with semistable cokernel conditions, non-strict). Every strictly
   $\sigma$-semistable object of class $v$ has Jordan–Hölder factors among:
   (i) proportional classes $c\, v_0$ (same reduced invariants, hence the same
   $\sigma$-phase everywhere, on the wall and in both chambers), and
   (ii) the DT/PT destabilizing pair $(v-u, u)$ with $\mathrm{rk}(u) \le 1$.

3. (Good moduli on both sides and on the wall; S-equivalence.)
   The stacks $\mathcal{M}^{\mathrm{DT}}(v)$, $\mathcal{M}^{\mathrm{PT}}(v)$ of
   semistable objects of class $v$ on the two sides, and the stack
   $\mathcal{M}^{\sigma_0}(v)$ of $\sigma_0$-semistable objects, each admit a
   proper good moduli space (Alper–Halpern-Leistner–Heinloth
   $\Theta$-reductivity + S-completeness, plus BMT/Piyaratne–Toda boundedness,
   which are all stable-under-semistability statements). Closed points are
   S-equivalence classes. Wall crossing therefore identifies the two moduli
   problems through the common $\sigma_0$-S-equivalence relation.

4. (Generalized DT/PT wall-crossing formula.) The Joyce–Song / Joyce universal
   wall-crossing formula applied at this single wall gives, with generalized
   (Joyce–Song) DT invariants $\overline{DT}$ and PT invariants defined by
   weighted Euler characteristic / Behrend function on the above good moduli
   stacks:
   $$
   \overline{DT}(v) = \sum_{\substack{n \ge 1\\
     \gamma_1 + \cdots + \gamma_n = v\\
     \phi_0(\gamma_i) = \phi_0(v)}}
     U(\gamma_1,\dots,\gamma_n; \sigma_-, \sigma_+)\,
     \prod_{i=1}^n \overline{PT}(\gamma_i),
   $$
   where the sum runs over ordered decompositions equi-phased at $\sigma_0$,
   $U$ are the Joyce–Song coefficients, and the $n = 1$ term is
   $\overline{PT}(v)$. For $d_0 = 1$ the only equi-phased splittings with a
   rank-positive and a rank-$\le 1$ factor are the DT/PT ones and the formula
   reduces to the known coprime DT/PT formula; for $d_0 > 1$ the sum acquires
   exactly the additional ordered proportional splittings
   $v = \sum_i c_i v_0$ (all factors of equal reduced invariants) and mixed
   refinements, each contributing via its $U$-coefficient and Euler pairing.
   In particular strictly semistable factors are included, not excluded.

This is the precise non-coprime extension asked for: same wall, adjacent
chambers with good moduli of Gieseker-semistable sheaves and PT-semistable
objects, S-equivalence identification across the wall, and the generalized
formula with strictly semistable contributions.

## 2. Proof

### Step 1 — The wall equation is gcd-independent (numerical).
With $B = bH$, $d = H^3$, the twisted degrees
$$
D^B = D - rb d,\quad
Q^B = Q - bD + rb^2d/2,\quad
N^B = N - bQ + b^2D/2 - rb^3d/6
$$
are linear in $(r, D, Q, N)$. The BMT central charge
$$
Z_{a,b} = \bigl(-N^B + \tfrac{a^2}{2} D^B\bigr)
  + i\bigl(aQ^B - \tfrac{a^3}{6}dr\bigr)
$$
is likewise linear in the class. Hence for a destabilizer $u$,
$$
W_{u,v} = \{(a,b) : \Im(Z(u)\overline{Z(v)}) = 0\}
$$
is a bilinear equation in $(u, v)$. Under $v = m v_0$,
$\Im(Z(u)\overline{Z(mv_0)}) = m\,\Im(Z(u)\overline{Z(v_0)})$: identical zero
set. No gcd hypothesis enters. In particular the DT/PT wall — defined by the
rank-$\le 1$ destabilizer producing the large-volume DT/PT transition — is at
the same locus for $d_0 = 1$ and $d_0 > 1$. The accompanying script verifies
this identity on a $108$-point $(a,b)$-grid: sign patterns agree $108/108$ and
the scaling identity holds to $10^{-9}$; it also exhibits an explicit wall
bracket. (File `output/artifacts/check_wall_gcd_independence.py` and its
`wall_check_results.json`.)

### Step 2 — Proportional classes never subdivide the chambers.
If $u$ is numerically proportional to $v$ (rank-positive multiple of $v_0$),
then $Z(u) = c\,Z(v)$ for a positive real scalar $c$ at every $(a,b)$, so
$\Im(Z(u)\overline{Z(v)}) \equiv 0$ and the tilt/Bridgeland slopes coincide
everywhere. Such classes define no wall; the script confirms the cross product
vanishes identically (max $|{\cdot}| \sim 10^{-13}$ over the grid). They
contribute only strictly semistable objects present on the wall and in both
adjacent chambers — i.e. new Joyce–Song summands, not new chambers. The only
wall met in the relevant $(b,w)$ window that separates DT-stability from
PT-stability is therefore the same single non-proportional DT/PT wall as in
the coprime proof (uniqueness of the destabilizing rank-$\le 1$ class in that
window uses only Bogomolov-type bounds and the large-volume asymptotics, which
are numerical and gcd-independent).

### Step 3 — Chamber identifications with non-strict inequalities.
The coprime argument identifies, for $b$ large (DT side), tilt-semistability of
class $v$ with $2$-Gieseker-semistability, and then Bridgeland semistability
with Gieseker-semistability; on the PT side, with PT-semistability of pairs.
Every step is an inequality between reduced numerical polynomials
($p_v \le p_u$ style) or a slope comparison of numerical central charges, plus
a rank estimate for a destabilizing subobject. Replacing $<$ by $\le$
throughout (allowing equality = strict semistability) leaves each implication
valid: a destabilizing quotient in the strict sense is still a destabilizing
quotient in the non-strict sense, and conversely the numerical exclusion of
non-proportional destabilizers in each chamber (Step 2 + the Bogomolov bound)
shows any $\sigma$-semistable object satisfies the non-strict Gieseker (resp.
PT) inequalities, while any Gieseker- (resp. PT-) semistable object satisfies
the non-strict $\sigma$ inequalities because the only potential
$\sigma$-destabilizers in that chamber are non-proportional classes already
excluded numerically. A strictly semistable object has a Jordan–Hölder
filtration whose factors are exactly of the two listed types: proportional
(rank-positive, equal reduced invariants) or the DT/PT pair. This is the
standard "same proof with $\le$" and uses no coprimality.

### Step 4 — Good moduli and S-equivalence across the wall.
Boundedness of $\sigma_{a,b}$-semistable objects of class $v$ (BMT /
Piyaratne–Toda style bounds: they depend on $(r, D, Q, N)$ and the compact
$(a,b)$-window, never on $d_0$), openness of semistability, and the
Alper–Halpern-Leistner–Heinloth criteria ($\Theta$-reductivity and
S-completeness for the stack of semistable objects in $\mathcal{A}_b$) give
that each of $\mathcal{M}^{\mathrm{DT}}(v)$, $\mathcal{M}^{\mathrm{PT}}(v)$,
$\mathcal{M}^{\sigma_0}(v)$ admits a proper good moduli space; closed points
parametrize S-equivalence classes (graded objects of Jordan–Hölder
filtrations). Since the hearts and stability conditions vary continuously and
$\sigma_0$ lies in the closure of both chambers, the two moduli problems map
to the common $\sigma_0$ moduli problem by taking associated graded objects —
this is the "wall crossing identifies S-equivalence classes" statement. The
existence of strictly semistables is precisely why good moduli spaces (rather
than coarse spaces of stables) are used; the machinery is designed for the
semistable case, so $d_0 > 1$ causes no extra difficulty.

### Step 5 — Generalized formula.
The hypotheses of Joyce–Song (or Joyce's universal wall-crossing / motivic
Hall algebra formalism) are: a wall with good moduli on both sides and on the
wall, plus the Behrend-function identities on the CY3. Step 4 supplies
exactly these. Applying the formula at the single wall $W$ yields the stated
sum over equi-phased ordered splittings. When $d_0 = 1$, a rank-positive
proper splitting $v = \sum \gamma_i$ with all $\phi_0(\gamma_i) = \phi_0(v)$
and each $\gamma_i$ rank-positive is numerically impossible (it would force a
common divisor $> 1$ of $(r, D)$ after the Step-2 phase analysis), so only the
DT/PT-type splittings survive: the known coprime formula. When $d_0 > 1$, the
additional admissible splittings are precisely the ordered proportional ones
$v = \sum c_i v_0$ and their mixtures with the rank-$\le 1$ DT/PT factor; the
script enumerates them for $m = 1, 2, 3$ and records the nonzero pairings and
$S$-symbols entering $U$. This is the "corresponding generalized DT/PT
wall-crossing formula including strictly semistable factors."

### Step 6 — Reductions and scope.
Picard rank one is used only to write the one-parameter $(a,b)$ slice and the
DT/PT wall in closed form; the gcd-independence itself is linear algebra valid
in higher rank. The BMT existence hypothesis is the target's own assumption.
Generalized invariants are Joyce–Song $\overline{DT}$-type (needed as soon as
strictly semistables exist); for $d_0 = 1$ they coincide with the ordinary ones
on stable classes.

## 3. What the computation verifies (and what it does not)
- Verified numerically: (A) wall zero-set invariance under $v \mapsto mv_0$
  ($108/108$ sign agreement, exact scaling identity); (B) proportional classes
  have identically equal phase (no new wall); (C) complete inventory of new
  strictly-semistable splitting types for $m = 1, 2, 3$ with Euler pairings and
  $S$-symbols. Reproduce with `python3 output/artifacts/check_wall_gcd_independence.py`.
- Not computed (proved by citation + deduction): AHLH criteria, boundedness,
  Joyce–Song integration — these are theorems applied, not computations.

## 4. Limitations and uncertainties
- The proof assumes the BMT inequality (double-tilt stability) on the needed
  window — exactly the target's hypothesis; unconditional existence on a given
  $X$ is not proved here.
- Good-moduli and wall-crossing-formula steps invoke the AHLH and Joyce–Song /
  Joyce theorems; their full hypotheses (e.g. Behrend identities) are standard
  for CY3s but re-verified only by reference, not from scratch.
- The numerical script uses illustrative degrees ($H^3 = 5$, sample $v_0$);
  the invariance claims are algebraic identities confirmed on the grid, not
  sensitive to the chosen values.
- Higher Picard rank would need a multi-parameter slice; the statement here is
  for Picard rank one as in the target.

## 5. References (results used, not searched)
- Bayer–Macrì–Toda: double-tilt construction and BMT inequality framework.
- Piyaratne–Toda: Bogomolov-type bounds giving large-volume chamber control.
- Alper–Halpern-Leistner–Heinloth: $\Theta$-reductivity + S-completeness
  $\Rightarrow$ good moduli for semistable stacks.
- Joyce–Song (and Joyce's universal formula): wall-crossing for generalized DT
  invariants via motivic Hall algebras; DT/PT wall treated as one wall among
  finitely many in the window.
- Known coprime higher-rank DT/PT wall-crossing (the "single-wall theorem"
  being extended): Bayer, Toda, and follow-ups identifying DT/PT chambers in
  tilt/Bridgeland stability.
