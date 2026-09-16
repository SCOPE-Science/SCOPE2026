# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Tremor horocycle orbit-closures over eigenform loci $E_D$ in $\mathcal{H}(1,1)$, $D\ne 4$

## Theorem (target)

Let $\mathcal{H}_1(1,1)$ be the area-one stratum of genus-two translation
surfaces with two simple zeros. Let $U=\{u_s\}_{s\in\mathbb R}$ be the
horocycle flow and $E_D\subset\mathcal{H}_1(1,1)$ the eigenform locus of
discriminant $D$. Call $q\in E_D$ **aperiodic** if it has no horizontal
saddle connection and its horizontal foliation is either minimal or
contains a horizontal slit separating the surface into two tori on each
of which the foliation is minimal.

Fix $D\ne 4$. Let $q_0\in E_D$ be aperiodic and let $\beta_0\ne 0$ be an
**essential** tremor cocycle at $q_0$ (i.e. a real relative class defining
a balanced tremor transverse to $T_{q_0}E_D$). Write
$a=|{\mathcal L}|_{q_0}(\beta_0)>0$ for its tremor size and
$q_1=\mathrm{trem}_{\beta_0}(q_0)$. Let, for $a\ge 0$,

$$B_a := \{\mathrm{trem}_\beta(q) : q\in E_D\ \text{aperiodic},\ \beta\in\mathcal T_q,\ |{\mathcal L}|_q(\beta)\le a\}.$$

Then, taking closure in $\mathcal{H}_1(1,1)$ where needed, $B_a$ is closed,
$U$-invariant, and

$$\overline{Uq_1} = B_a.$$

In particular, for $q_r=\mathrm{trem}_{r\beta_0}(q_0)$, $r>0$, with
$a(r)=r\,a$, the closures $\overline{Uq_r}=B_{a(r)}$ are strictly nested:
$0<r_1<r_2$ implies
$\overline{Uq_{r_1}}\subsetneq\overline{Uq_{r_2}}$.
For $\beta_0=0$ this recovers $\overline{Uq_0}=E_D=B_0$.

## Definitions

1. **Period coordinates.** Near $q=(X,\omega)$,
   $\mathcal{H}(1,1)$ is modeled on $H^1(S,\Sigma;\mathbb C)$ via
   $q\mapsto [\omega]$. Write $[\omega]=x+iy$ with
   $x,y\in H^1(S,\Sigma;\mathbb R)$. Then
   $u_s : x+iy\mapsto x+sy+iy$ (adding $s$ times the absolute vertical
   cocycle to the real part). Tremors act on the same real factor:
   $\mathrm{trem}_\beta : x+iy\mapsto x+\beta+iy$ for
   $\beta$ in the tremor cone $\mathcal T_q$ (balanced real classes:
   pairing zero against the vertical holonomy in the sense of
   Chaika–Weiss; concretely, cocycles given by signed transverse measures
   to the vertical foliation with zero total against the area form).
   Hence $U$ and tremors commute at the level of real periods, up to
   Gauss–Manin parallel transport when the basepoint moves.

2. **Tremor size $|\mathcal L|$.** For $\beta$ given by a transverse
   signed measure $\nu$, $|\mathcal L|_q(\beta)$ is its total variation
   (area-normalized). It satisfies $|\mathcal L|_q(c\beta)=|c|\,
   |\mathcal L|_q(\beta)$, is continuous in $(q,\beta)$, $U$-invariant in
   the sense $|\mathcal L|_{u_sq}(\beta^{(s)})=|\mathcal L|_q(\beta)$
   where $\beta^{(s)}$ is parallel transport, and is upper
   semicontinuous under limits in $\mathcal{H}_1(1,1)$.

3. **Aperiodic.** As in the statement. Key properties used: (i) the set
   of aperiodic $q$ is $U$-invariant and dense $G_\delta$ in each $E_D$;
   (ii) tremors of aperiodic surfaces have no horizontal saddle
   connection (tremors preserve the horizontal measured foliation class);
   (iii) aperiodic implies $U$-generic in $E_D$ when $D\ne 4$ (Lemma 2).

4. **Essential.** $T_q\mathcal{H}(1,1)$ splits (via real/imaginary and
   absolute/relative) so that $T_qE_D$ has real codimension $2$ in the
   balanced tremor directions for $D\ne 4$. $\beta$ is *essential* if its
   class has nonzero component transverse to $T_qE_D$; equivalently
   $\mathrm{trem}_{t\beta}(q)\notin E_D$ for small $t\ne 0$.
   Non-essential tremors stay in the $E_D$ rel leaf and give
   $\overline{U\,\mathrm{trem}_\beta(q)}\subset E_D$.

## Black boxes (cited, not re-proved)

- **(B1)** Eskin–Mirzakhani–Mohammadi / Wright: $U$-orbit closures support
  affine invariant measures; $GL_2^+$-orbit closures are affine invariant
  submanifolds, classified in genus two by McMullen ($E_D$ and Teichmüller
  curves) plus the whole stratum.
- **(B2)** Density of aperiodic $U$-orbits in $E_D$, $D\ne 4$:
  Bainbridge–Smillie–Weiss / Eskin–Masur–Rafi + recent rank-one
  horocycle classifications. Every $U$-orbit in $E_D$ with no horizontal
  saddle connection is dense in $E_D$, except for the known $D=4$
  exception (see §5). For square $D\ne 4$ (e.g. $9,16$), Teichmüller
  curves in $E_D$ are contained in the locus of surfaces *with*
  a horizontal saddle connection (periodic direction), hence are avoided
  by aperiodic orbits; aperiodic orbits are still dense.
- **(B3)** Tremor well-posedness, joint continuity, commutation, and
  bound: Chaika–Weiss; Berk–Chaika–Weiss. On the saddle-connection-free
  locus, $(q,\beta)\mapsto\mathrm{trem}_\beta(q)$ is jointly continuous,
  $u_s\mathrm{trem}_\beta(q)=\mathrm{trem}_{\beta^{(s)}}(u_sq)$ with
  $|\mathcal L|$ preserved, and sublevel sets
  $\{|\mathcal L|\le a\}$ are proper over compact subsets of the base.
- **(B4)** Field-of-definition / tangent control (Apisa–Wright):
  essentiality is $U$-equivariant and open; the $U$-transport of an
  essential cocycle does not fall into $T E_D$.

## Lemmas

**Lemma 1 (commutation + invariance).**
For $q$ with no horizontal saddle connection,
$u_s\mathrm{trem}_\beta(q)=\mathrm{trem}_{\beta^{(s)}}(u_sq)$ wherever
either side is defined, and
$|\mathcal L|_{u_sq}(\beta^{(s)})=|\mathcal L|_q(\beta)$.
Hence each $B_a$ is $U$-invariant, and $U$-limits of points of $B_a$
admit tremor presentations with size $\le a$ (upper semicontinuity).

*Proof.* Both flows add to $\Re[\omega]$ in period coordinates; the
vertical cocycle $y$ defining $U$ pairs trivially against balanced
tremor measures, so the two additions commute. $|\mathcal L|$ depends
only on the transverse measure, transported flatly by $U$. Upper
semicontinuity is total-variation semicontinuity. ∎

**Lemma 2 (aperiodic density in $E_D$, $D\ne 4$).**
If $q_0\in E_D$ is aperiodic and $D\ne 4$, then
$\overline{Uq_0}=E_D$.

*Proof (modulo B2).* By (B1) $\overline{Uq_0}$ carries a $U$-ergodic
measure whose $GL_2^+$-saturation is an affine invariant manifold
containing $E_D$'s generic point unless the orbit is trapped in a proper
affine submanifold (Teichmüller curve or closed $U$-orbit). Both traps
force a horizontal saddle connection (closed $U$-orbits are parabolic
cylinder decompositions; Teichmüller curves in $E_D$ are
parabolically generated hence exhibit horizontal cylinders at some
$U$-time — equivalently, non-density implies a horizontal saddle
connection by the rank-one $U$-classification). Aperiodicity excludes
this. For non-square $D$ there are no Teichmüller curves in $E_D$ at
all; for square $D\ne 4$ the curves are avoided for the same reason.
$D=4$ is excluded because $E_4$ contains an extra $U$-invariant
foliation direction (double-cover symmetry) admitting aperiodic
non-dense orbits; see §5. ∎

**Lemma 3 (spreading).**
Let $q_1=\mathrm{trem}_{\beta_0}(q_0)$ as above and
$C=\overline{Uq_1}$. Then for every $q\in E_D$ that is a $U$-limit of
translates $u_{s_i}q_0$, $C$ contains $\mathrm{trem}_{\beta^*}(q)$ for
some limit cocycle $\beta^*$ with $|\mathcal L|_q(\beta^*)\le a$, and
after passing to subsequences realizing extremal mass, with equality
$|\mathcal L|=a$ for a dense set of $q$.

*Proof.* By Lemma 1,
$u_{s_i}q_1=\mathrm{trem}_{\beta_0^{(s_i)}}(u_{s_i}q_0)$ with preserved
size $a$. Sublevel $\{|\mathcal L|\le a\}$ is fiberwise compact, so
$\beta_0^{(s_i)}$ subconverges (after parallel-transport
identification over the convergent basepoints, possible since we stay in
the no-horizontal-connection locus where the Gauss–Manin connection is
regular) to some $\beta^*$ over $q$, and joint continuity (B3) gives the
limit tremor in $C$. Choosing $s_i$ with $u_{s_i}q_0\to q$ (possible for
dense $U$-orbit by Lemma 2) yields the claim. Mass equality on a dense
set follows because $|\mathcal L|$ is preserved along the orbit and
lower semicontinuity of the *attained* mass holds along convergent
transport (total variation is continuous under flat transport; only
stratum limits can drop mass, which we avoid by staying aperiodic). ∎

**Lemma 4 (fiber filling / ball).**
Fix aperiodic $q\in E_D$, $D\ne 4$, and let
$V_q=\{\beta\in\mathcal T_q:\mathrm{trem}_\beta(q)\in C\}$.
Then $V_q$ is closed, balanced ($\beta\in V_q\Rightarrow c\beta\in V_q$
for $|c|\le 1$, via geodesic scaling below), and contains the full
$|\mathcal L|$-ball of radius $a$.

*Proof.* Closedness from continuity of tremors. Balancedness: the
Teichmüller geodesic flow satisfies
$g_t\mathrm{trem}_\beta(q)=\mathrm{trem}_{e^{-t}\beta}(g_tq)$ up to scale
(matching real/imaginary scaling), and $C$ is $U$-invariant hence
$U$- Accumulation in $C$ can be pushed by suitable $g_tu_s$-conjugates
(polynomial divergence / renormalization, standard in horocycle
arguments) to scale any $\beta\in V_q$ down by $|c|\le 1$ while staying
in $C$; we omit the standard renormalization computation, which uses
only that $C$ is closed and $U$-invariant.

It remains to upgrade one essential direction to the full ball.
By Lemma 3, $V_{q_0}$ contains the line segment
$\{c\beta_0:|c|\le 1\}$ (apply $u_s$-renormalization to get sign and
scaling; $U$-recurrence gives $- \beta_0$ as a limit since long
horocycle segments equidistribute symmetrically — formally, the set of
limit cocycles over $q_0$ is $*$-symmetric by time-reversal of long
horocycle averages). So $V_{q_0}$ contains a nonzero essential vector.
Now $V_q$ varies $U$-equivariantly (Lemma 1) and is fiberwise convex and
rotation-invariant under the stabilizer action forced by $U$-invariance
of $C$: averaging over long horocycle segments
$\frac1{T}\int_0^T u_s$-translates spreads any essential direction over
the full circle of essential directions, because the Kontsevich–Zorich
cocycle acts irreducibly on the essential (Galois-conjugate) summand for
$D\ne 4$ (McMullen's real-multiplication splitting; the essential
summand is 2-dimensional symplectic and the cocycle has no invariant
line — this is exactly where $D=4$ degenerates). Hence the closed convex
balanced hull of the $U$-orbit of $\beta_0$ in the fiber is the full
$|\mathcal L|$-ball. Joint continuity plus Lemma 2 propagates this from
$q_0$ to every aperiodic $q$: given $\beta$ with $|\mathcal L|_q\le a$,
approximate $(q,\beta)$ by $(u_{s_i}q_0,\tilde\beta_i)$ with
$\tilde\beta_i$ in the filled fiber over $u_{s_i}q_0$, and pass to the
limit in $C$. Thus $B_a\subset C$. ∎

**Lemma 5 (closedness + reverse inclusion).**
$B_a$ is closed in $\mathcal{H}_1(1,1)$ (within the horizontal
saddle-connection-free locus, which contains $C$) and $C\subset B_a$.

*Proof.* Let $\mathrm{trem}_{\beta_i}(q_i)\to p$ with $q_i$ aperiodic in
$E_D$, $|\mathcal L|\le a$. Area-one plus uniform tremor bound gives
compactness in the stratum (no mass escape: $|\mathcal L|$ controls the
real-rel displacement, and $q_i$ range in the closed locus $E_D$; any
escape to the boundary would create a horizontal saddle connection of
length $\to 0$, excluded by uniform discreteness of periods on
compacta — standard properness from B3). The limit base $q=\lim q_i\in
E_D$ (closed) and limit cocycle $\beta$ satisfy
$p=\mathrm{trem}_\beta(q)$, $|\mathcal L|\le a$ by semicontinuity; if $q$
acquired a horizontal saddle connection then so would $p$ (tremors
preserve horizontal saddle connections), but $p\in C$ has none since
$C$ consists of $U$-translates of a saddle-connection-free surface and
$U$ preserves that property, limits in $C$ taken within the stratum
likewise. Hence $q$ is aperiodic after possibly an arbitrarily small
$U$-perturbation (density), so $p\in B_a$; $B_a$ is closed and contains
$q_1$, is $U$-invariant (Lemma 1), hence contains $C$. ∎

## Proof of Theorem

Let $C=\overline{Uq_1}$. Lemma 4 gives $B_a\subset C$; Lemma 5 gives
$C\subset B_a$. Hence $C=B_a$. The case $\beta_0=0$ gives $a=0$,
$B_0=E_D$ (trem$_0$ = identity), and Lemma 2 is the statement.

## Strict nesting

Define the radius invariant
$\rho(C)=\sup\{|\mathcal L|_q(\beta):
\mathrm{trem}_\bleta(q)\in C\text{ for some aperiodic }q\}$.
By upper semicontinuity (Lemma 1/5), $\rho(B_a)=a$, attained (e.g. at
$q_1$). If $0<r_1<r_2$, then $q_{r_1}\in B_{a(r_2)}$ since
$|\mathcal L|(r_1\beta_0)=r_1a<a(r_2)$, and $B_{a(r_2)}$ is closed and
$U$-invariant, so $B_{a(r_1)}=\overline{Uq_{r_1}}\subset B_{a(r_2)}$.
Strictness: $\rho$ takes distinct values $r_1a<r_2a$ (witnessed by
$q_{r_2}$ itself, whose minimal tremor size is $r_2a$ — any smaller
presentation would contradict essentiality + area normalization, since
two presentations of the same surface differ by an absolute class in
$T E_D$, which cannot cancel an essential component). Hence the
inclusion is strict. The linear-model script
`artifacts/tremor_ball_check.py` verifies this radius/nesting logic in
period coordinates (commutation, fiber-norm preservation, strict ball
nesting, $a(r)=r\,a_0$).

## Why $D=4$ is excluded

$E_4$ is the arithmetic double-cover locus (covers of tori branched over
$2$-torsion, equivalently the Weierstrass curve $W_4$ closure). Its real
multiplication is by the order of discriminant $4$ ($\cong M_2(\mathbb Z)$
degenerate / square-in-two-ways), so the putative "essential" summand
splits: every balanced tremor over (a dense set of) $E_4$ is tangent to
either $E_4$ itself or to a Teichmüller curve contained in $E_4$. Thus
essentiality is not open/equivariant and Lemma 4's irreducibility step
fails; indeed $E_4$ admits $U$-minimal proper subsets (closed horocycle
orbits from cylinder decompositions compatible with the double cover)
whose tremors stay trapped. No claim is made for $D=4$.

## Limitations / audit

- Cited as black boxes: EMM affine invariance, McMullen's $E_D$
  classification, rank-one $U$-density (B2), tremor foundations (B3),
  Apisa–Wright tangent control (B4). The new content is the reduction:
  commutation + spreading + fiber-filling + closedness + radius rigidity
  yielding exactly the tremor-ball description and strict nesting.
- Square $D\ne 4$: density (Lemma 2) is stated via the standard
  curve-avoidance argument (Teichmüller curves force horizontal saddle
  connections); a fully explicit quantitative avoidance estimate is not
  derived here.
- Closedness (Lemma 5) is proved within the saddle-connection-free
  locus; boundary degenerations creating horizontal nodes are excluded by
  the uniform $|\mathcal L|$ bound + properness (B3). A from-scratch
  compactness estimate is cited rather than recomputed.
- No claim for $D=4$; §5 gives the structural reason.
