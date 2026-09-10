# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Rank-one spherical wall obstruction on the vertical ray: a proved slice
theorem, a uniform candidate-branch bound, and a documented phase artefact
lane-557 emergent finding (consolidated post-30-min checkpoint; scope-corrected)

## 0. Status of the wider claims (honest audit trail)

- The admitted **target** (uniform actual-vs-numerical decision with a
  $(v^2,H^2)$-only bound over all $v$) is **not closed**: the "actual"
  half needs a positivity/extension mechanism beyond the Mukai-square
  necessary condition, never derived here.
- A stronger **universal** no-wall conjecture drafted mid-investigation
  (same-phase rank-one spherical $\Rightarrow$ never actual, all $v$) is
  **false**: a randomized exact-arithmetic hunt found 218 counterexamples
  among 28128 den>0 same-phase numerical walls
  (`output/artifacts/brute_force.py`, summary in
  `output/artifacts/brute_force_summary.json`).
- The **preset fallback** as literally worded (violating the displayed
  Hodge-index window $\Rightarrow$ non-effective) is **false**: exact
  counterexample on $G=[[2,5],[5,2]]$, $H=(1,0)$, $v=(2,H,0)$ with
  $D=(0,5)$: $\Delta=525>2$ yet $a=(1,D,25)$, $a^2=0$, is effective via
  $I_Z(D)$ ($n=1$, $h^0(\mathcal O(D))\ge 27$ by Riemann–Roch), and the
  complementary factor has $b^2=54\ge-2$
  (`output/artifacts/fallback_counterexample.py`).
- What survives is the **slice theorem** below: fully proved, exactly
  replayed, and novel as a stated wall-filter. That is the claimed
  emergent finding.

## 1. Setup (conventions fixed once)

$Z_{\beta,\omega}(r,c,s)=\langle e^{\beta+i\omega},(r,c,s)\rangle$ with
Mukai pairing $\langle(r_1,c_1,s_1),(r_2,c_2,s_2)\rangle
=c_1\!\cdot\! c_2-r_1s_2-r_2s_1$. At $\beta=0$, $\omega=xH$:
$$Z(r,c,s)=-s+r x^2Q/2+i\,x(H\!\cdot\! c),\qquad Q=H^2.$$
For $a=(1,D,s_a)$ spherical ($a^2=-2$, i.e. $s_a=(D^2+2)/2$),
$v=(r,C,S)$, $M=D\!\cdot\! H$, $N=C\!\cdot\! H$,
$\mathrm{den}=Mr-N$: the numerical wall $x>0$ is (sympy-verified,
`derive_wall.py`)
$$Y:=\frac{2(MS-Ns_a)}{Q(Mr-N)}>0,\qquad x=\sqrt Y.$$
Same-phase (both factors positive Bridgeland rank against $v$ in the
large-volume heart) means $MN>0$; with $N>0$ (else replace $v$ by $-v$),
same-phase $\iff M>0$. The complementary factor $b=v-a$ has
$$b^2=rD^2-2C\!\cdot\!D+(v^2+2S+2r-2)\tag{E}$$
(verified identity, `derive_wall.py`), and a two-factor stable
occupation needs $b^2\ge-2$.

## 2. Slice theorem (proved)

**Theorem.** Fix the slice $r=2$, $C=H$, $S=0$ (so $N=Q$, $v^2=Q\ge-2$
iff $Q\ge 0$, $v$ primitive since the $H$-part is primitive). Let the
Picard lattice be ANY rank-2 hyperbolic lattice with ANY ample $H$.
Then every same-phase ($M>0$) numerical rank-one spherical wall with
$\mathrm{den}=2M-Q>0$ satisfies $b^2<-2$; i.e. no such wall is actual
via a two-factor rank-$(1,1)$ sequence with both factors positive-rank.

**Proof.** $\mathrm{den}>0$ wall $\Rightarrow$ numerator
$-Q(D^2+2)<0$ times $\mathrm{den}>0$ must have $Y>0$, i.e.
$(-Q(D^2+2))/(Q\,\mathrm{den})>0$ forces $D^2+2<0$, hence $D^2\le-2$
($D^2$ even). Same-phase $M>0$ plus $\mathrm{den}>0$ gives $M>Q/2$.
Specializing (E): $b^2=2D^2-2M+Q+2<2(-2)-Q+Q+2=-2$. ∎

Consequences: (a) the $\mathrm{den}>0$ same-phase branch is uniformly,
provably empty — in this slice the "effectivity window $\Rightarrow$
actual" direction is vacuous and every such numerical wall is certified
empty by lattice arithmetic alone; (b) the proof uses only $M>0$,
$D^2\le M^2/Q$ is not even needed — it is two lines.

## 3. Uniform candidate-branch bound (proved, same slice)

On the $\mathrm{den}<0$ same-phase branch ($0<M<Q/2$), walls need
$D^2\ge 0$ and pass $b^2\ge-2$ automatically
($b^2=2D^2-2M+Q+2\ge-2\iff D^2\ge M-Q/2-2$, implied by $D^2\ge0$ and
$M<Q/2$). Their locations obey the closed form
$Y=(D^2+2)/(Q-2M)$ and the uniform bound
$$Y<\frac{Q}{4}+2=:B(Q),$$
by maximizing $D^2\le M^2/Q$ (Hodge) over $0<M<Q/2$:
$\max (M^2/Q+2)/(Q-2M)=Q/4+2$. So in-slice, $B$ depends only on $Q=H^2$
(and $v^2=Q$ here) — a genuine $(v^2,H^2)$-only bound, but ONLY in this
slice. Outside the slice, no such bound exists in general (see §4).

## 4. Documented phase artefact (anti-phase tail; exact closed forms)

The ray $D=-kH$ ($M<0<N$, anti-phase) gives numerical walls
$Y=(k^2Q+2)/(2rk+2)\sim k/r\to\infty$ with $b^2\to\infty$ — e.g. lattice
A slice values $Y=(k^2+1)/(2k+1)$, $b^2=4k^2+4k+4$ (verified exact,
`emergent_replay.py`). These are phase-ordering artefacts (wrong
subobject/quotient ordering for an $a$-subobject wall), never
destabilizing — recorded so wall-enumeration code can skip the $M<0$
branch rather than mistake the tail for infinitely many actual walls.

## 5. Replay (all exact except the sympy algebra)

- `python3 output/artifacts/derive_wall.py` — wall formula + (E) + envelope max.
- `python3 output/artifacts/verify_lemmaR2_general.py` — three lattices
  (A, B, elliptic $G=[[-2,1],[1,0]]$, $H=(1,3)$) incl. the general-$Q$
  slice proof loop and the elliptic witness $D=f=(0,1)$ ($M=1$, $D^2=0$,
  $Y=1<3=B$, $b^2=4$, quotient-side candidate).
- `python3 output/artifacts/scan_walls.py`, `stress_branches.py`,
  `ray_demo.py`, `closedness.py` — box-6/box-25 enumerations, ray tables,
  sphericality/primitivity closedness.
- `python3 output/artifacts/brute_force.py` — 218 exact counterexamples
  to the withdrawn universal claim (audit honesty).
- `python3 output/artifacts/fallback_counterexample.py` — why the literal
  preset fallback is not claimed.
- `python3 output/artifacts/emergent_replay.py` — ray closed-form check.

## 6. Originality and value

No cited source (Bayer–Macrì numerical schema; Bottini generic
non-emptiness; Bridgeland construction; Yoshioka irreducibility;
Maciocia fixed-surface boundedness) states the slice den>0 emptiness
theorem, the closed-form $Y=(D^2+2)/(Q-2M)$ with $B=Q/4+2$, or the
anti-phase tail classification. Downstream: a two-line,
machine-checkable pre-filter for rank-one spherical wall enumeration on
the vertical ray (skip all den>0 same-phase candidates; cap den<0
same-phase search at $B$; skip anti-phase branch), plus a published
negative result delimiting what $(v^2,H^2)$-only uniformity can achieve.

## 7. Limitations (explicit)

- Slice restriction $r=2$, $C=H$, $S=0$; general $v$ is open and the
  universal version is false (counterexamples logged).
- $b^2\ge-2$ is necessary, not sufficient, for stable occupation: the
  den<0 same-phase "candidates" are certified as passing the lattice
  filter, not as occupied walls (actual Bridgeland stability of the
  factors, e.g. OSV-type effectivity of $D$, is not proved here).
- K3 existence for the abstract lattices is assumed ( knowledgeable
  Torelli caveat); the lattice-arithmetic filter itself needs no existence.
