# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified minimal non-monomial witness: SL(2,3) of order 24

## Claim (proved here)
Let $G$ be the group of $2\times2$ determinant-one matrices over $\mathbf{F}_3$
($SL(2,3)$), presented by
$$P=\langle x,y,t\mid x^4=t^3=1,\ x^2=y^2,\ y^{-1}xy=x^{-1},\
txt^{-1}=y,\ tyt^{-1}=xy\rangle.$$
Then:
1. $|G|=24$; $G$ has 7 conjugacy classes of sizes $[1,1,4,4,4,4,6]$.
2. $G\cong Q_8\rtimes C_3$ with Sylow $Q_8$ the commutator subgroup; $|G^{ab}|=3$.
3. The irreducible degrees are exactly $\{1,1,1,2,2,2,3\}$.
4. Every degree-2 irreducible is non-monomial: no linear character of any
   subgroup induces it. Hence $G$ is not an M-group.
5. Minimality context (quoted background, not proved here): every group of
   order $<24$ is monomial, so 24 is the smallest order admitting failure.

## Proof (machine-checked; replay: `python3 output/artifacts/VERIFY.py`)

**Model.** $G=\{M\in M_2(\mathbf F_3):\det M=1\}$, $24$ matrices listed
explicitly. All $576$ products lie in the set, inverses $A^{-1}=\mathrm{adj}(A)$
($\det=1$) verified, unique identity. (Artifact `sl23_struct.json`.)

**Presentation.** With $x=(0,1,2,0)$, $y=(1,1,1,2)$, $t=(0,1,2,2)$ (entries mod 3
row-major), all six relations hold exactly in the matrix model, including the
cyclic leg $t(xy)t^{-1}=x$; $\langle x,y,t\rangle$ is all 24 matrices.
Conversely every word in $P$ reduces to $x^ay^bt^c$: $t^{\pm1}$ moves right past
$Q_8$-words via $tx=yt$, $ty=(xy)t$ (and inverse forms from the same relations:
conjugating $txt^{-1}=y$ by $t^{-1}$ gives $t^{-1}yt=x$, conjugating
$tyt^{-1}=xy$ gives $t^{-1}(xy)t=y$, whence $t^{-1}xt=yx^{-1}=xy$ by the $Q_8$
relation $xy=yx^{-1}$; the third leg $t(xy)t^{-1}=y(xy)=x$ is itself a
consequence),
$Q_8$-words collapse via the quaternion relations to 8 normal forms, and
$t^3=1$ caps the exponent. Hence $|P|\le 24$, and since $P$ maps onto the
24-element matrix group, $P$ presents $G$. (Artifacts `sl23_present.json`,
`sl23_normal.json`.)

**Classes.** Orbit BFS under conjugation: 7 classes, sizes
$[1,1,4,4,4,4,6]$, sum 24; rep orders $[1,2,6,3,6,3,4]$.
Centralizer sizes $[24,24,6,6,6,6,4]$. (Artifacts `sl23_classes.json`,
`sl23_classalg.json`.)

**Subgroups (complete).** Starting from $\{1\}$ and closing under adjoining one
generator until fixed point (every subgroup arises this way), $G$ has exactly
15 subgroups with orders $[1,2,3{\times}4,4{\times}3,6{\times}4,8,24]$.
In particular **no subgroup has order 12** (no index-2 subgroup).
(Artifact `sl23_subgroups.json`.)

**Derived subgroup.** The 8 distinct commutators close to an order-8 subgroup
equal element-wise to $Q_8=\{g:g^4=1\}$ (order distribution $1,2,4^6$:
quaternion). Hence $G'=Q_8$, $|G^{ab}|=24/8=3$ (cyclic), so exactly 3 linear
characters. (Artifact `sl23_abel.json`.) The order-3 subgroup
$\langle t^2\rangle$ meets $Q_8$ trivially and $t$ acts nontrivially
($tqt^{-1}\ne q$), so $G=Q_8\rtimes C_3$.

**A 3-dimensional irreducible.** $G$ has 4 Sylow-3 subgroups; conjugation gives
a permutation character $\pi$; $\chi=\pi-1$ takes values
$(3,3,0,0,0,0,-1)$ on the 7 classes (in size-sorted order) and
$\langle\chi,\chi\rangle=\frac1{24}\sum|C|\chi(C)^2=24/24=1$,
so $\chi$ is irreducible of degree 3 (it factors through $G/Q_8$-free
$A_4$-quotient action; the central involution acts trivially).

**Degrees.** 7 classes $\Rightarrow$ 7 irreducibles. Three are linear, one has
degree 3; the remaining three have degrees $\ge2$ (not linear) with squares
summing to $24-3\cdot1-9=12$, forcing degrees $\{2,2,2\}$. So the degree
multiset is $\{1,1,1,2,2,2,3\}$ — no explicit $2$-dimensional character values
needed.

**Non-monomiality.** A monomial irreducible of degree $d$ is induced from a
linear character of a subgroup of index $d$. Degree 2 would require a subgroup
of order $12$; the complete census shows none exists. Hence all three
degree-2 irreducibles are non-monomial, and $G$ is not an M-group. ∎

## What is NOT claimed
- The full 15-group order-24 M-group dichotomy (target claim) is **not**
  proved here: only the SL(2,3) extremal witness (the admission fallback) is
  certified. Per-group verdicts for the other 14 groups, Dixon–Schneider
  reconstructions, and degree multisets beyond SL(2,3) were not completed.
- Minimality of order 24 (all smaller groups monomial) is standard background
  (Taketa line), quoted not proved.
- No explicit degree-2 character values and no per-subgroup induction
  scalar-product sweep were needed: the index-2-subgroup counting argument
  subsumes them.

## Replay
`python3 output/artifacts/VERIFY.py` re-derives everything (order, closure,
classes, subgroup census, commutator$=Q_8$, $\chi_3$ norm 1, presentation) and
writes `output/artifacts/VERIFY_result.json`. Pure Python + stdlib (numpy only
used for an environment check). Step scripts `sl23_base/subgroups/abel/struct/
present/normal/classalg.py` with JSON logs in `output/artifacts/`.
