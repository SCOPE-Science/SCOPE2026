# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — Finite nuclear dimension + UCT implies generalized tracial rank ≤ 1 without Q-stabilization

## Claim (TARGET)

Let $A$ be unital, simple, separable, non-elementary, nuclear with finite
nuclear dimension satisfying the UCT. Then $A$ has generalized tracial rank
at most one ($\mathrm{gTR}(A)\le 1$).

In particular the known fact that $A\otimes\mathbb Q$ has
$\mathrm{gTR}\le 1$ can be improved to $A$ itself, with no additional
hypotheses of finite decomposition rank, real rank zero, or torsion-free
$K_0$.

Non-elementary $+$ simple unital means $A$ is infinite-dimensional
(not a matrix algebra); the finite-dimensional case trivially has
$\mathrm{gTR}=0$ and is excluded only to make $\mathcal Z$-stability
non-vacuous.

## Definitions (for self-containment)

- Nuclear dimension $\dim_{\mathrm{nuc}}A\le n$: Winter–Zacharias
  completely-positive approximation through finite-dimensional algebras
  with $n+1$-coloured order-zero maps.
- UCT: Rosenberg–Schochet universal coefficient theorem for $KK$;
  the hypothesis needed for the Elliott–Gong–Lin–Niu classification.
- $\mathbb Q$: universal UHF algebra; $\mathcal Z$: Jiang–Su algebra.
- $\mathrm{gTR}(A)\le 1$ (Lin): $A$ is tracially approximated by the
  class $\mathcal C_1$ of $1$-dimensional noncommutative CW / Elliott–Thomsen
  building blocks. Precisely: for every finite ${\cal F}\subset A$,
  $\varepsilon>0$, nonzero $a\in A_+$, there are a nonzero orthogonal
  decomposition via a projection $p$ and a subalgebra $B\subset pAp$ with
  $B\in\mathcal C_1$ (finite direct sums of $C([0,1],M_n)$,
  dimension-drop intervals $I(k,m,n)$, $M_n$, $\mathbb C$) such that
  elements of ${\cal F}$ are $\varepsilon$-approximated by $B$ up to a
  small remainder $1-p\precsim a$ in Cuntz comparison. Unlike ordinary
  tracial rank $\le 1$, no real-rank-zero / projection-separation and no
  torsion-free $K_0$ restriction is built in: dimension-drop blocks carry
  torsion and have few projections by design.
- $\mathrm{gTR}\le 1$ is invariant under $*$-isomorphism and passes to
  unital inductive limits of algebras in $\mathcal C_1$ (tracial
  approximation property).

## Black-box theorems used (no re-proof claimed)

1. **Finite nuclear dimension $\Rightarrow$ $\mathcal Z$-stability**
   (Castillejos–Evington–Tikuisis–White–Winter, JEMS 2021):
   every separable simple unital nuclear non-elementary $C^*$-algebra with
   finite nuclear dimension is $\mathcal Z$-stable, $A\cong A\otimes\mathcal Z$.
   This removes the older need for finite decomposition rank,
   quasidiagonality, or strict comparison as an extra input.

2. **$\mathcal Z$-stable dichotomy** (Rørdam):
   a simple $\mathcal Z$-stable $C^*$-algebra is either stably finite or
   purely infinite.

3. **Purely infinite branch.** Kirchberg–Phillips classifies UCT Kirchberg
   algebras; Lin shows they have (ordinary) tracial rank zero, hence
   $\mathrm{gTR}\le 1$. Purely infinite simple unital algebras automatically
   have real rank zero (Zhang), so no extra RR0 hypothesis is ever needed
   on this branch.

4. **Stably finite classifiable branch**
   (Gong–Lin–Niu; Elliott–Gong–Lin–Niu classification + range):
   unital simple separable amenable $\mathcal Z$-stable UCT stably finite
   algebras are classified by the Elliott invariant and every such invariant
   is realized by a unital simple inductive limit of building blocks in
   $\mathcal C_1$ (Elliott–Thomsen / one-dimensional NCCW algebras,
   including dimension-drop intervals accommodating torsion $K$-theory).
   Such limits satisfy $\mathrm{gTR}\le 1$ by construction. Hence every
   algebra in this class is isomorphic to an algebra with $\mathrm{gTR}\le1$
   and therefore itself has $\mathrm{gTR}\le 1$.

## Proof

Let $A$ satisfy the hypotheses.

**Step 1 — $\mathcal Z$-stability.** By non-elementary simple unital,
$A$ is infinite-dimensional. By (1), $\dim_{\mathrm{nuc}}A<\infty$ gives
$A\cong A\otimes\mathcal Z$. Hence $A$ is in the classifiable class
(simple separable unital nuclear $\mathcal Z$-stable $+$ UCT).
The given fact that $A\otimes\mathbb Q$ has $\mathrm{gTR}\le 1$ is
consistent context but not used as an input; the argument below proves
the stronger statement for $A$ directly, avoiding circularity.

**Step 2 — Dichotomy.** By (2), $A$ is either stably finite or purely
infinite.

**Step 3 — Purely infinite case.** If $A$ is purely infinite, it is a
UCT Kirchberg algebra. By (3) it has tracial rank zero and in particular
$\mathrm{gTR}(A)\le 1$. Done.

**Step 4 — Stably finite case.** Suppose $A$ is stably finite. Then $A$
is a unital simple separable amenable $\mathcal Z$-stable UCT stably
finite algebra. By (4), there exists a model $B$, a unital simple
inductive limit of $\mathcal C_1$ building blocks with identical Elliott
invariant $\mathrm{Ell}(A)\cong\mathrm{Ell}(B)$, and classification gives
$A\cong B$. Since $B$ is (by range construction) tracially approximated
by $\mathcal C_1$, $\mathrm{gTR}(B)\le 1$. By isomorphism-invariance,
$\mathrm{gTR}(A)\le 1$.

**Step 5 — Why the three extra hypotheses are unnecessary.**
- *Finite decomposition rank:* only ever used as a proxy for
  $\mathcal Z$-stability; (1) supplies $\mathcal Z$-stability from finite
  nuclear dimension alone.
- *Real rank zero:* only needed for ordinary tracial rank; generalized
  tracial rank uses $1$-dimensional blocks with general trace simplices,
  so no RR0 / projection-richness is required. The purely infinite branch
  has RR0 automatically.
- *Torsion-free $K_0$:* dimension-drop interval blocks $I(k,m,n)$ realize
  arbitrary torsion in $K$-theory, and the range theorem covers all UCT
  invariants including torsion. Hence no torsion-free assumption is needed.

This covers all cases. Therefore $A$ itself has $\mathrm{gTR}\le 1$.
∎

## What is proved vs. assumed

- Proved locally: dichotomy split, reduction to the two classification
  branches, transfer of $\mathrm{gTR}\le 1$ across the classification
  isomorphism, and the explanation of why decomposition rank / RR0 /
  torsion-free drop out.
- Assumed as black boxes: CETWW $\mathcal Z$-stability, Rørdam dichotomy,
  Kirchberg–Phillips + Lin TR0, EGLN/GLN classification + range for
  $\mathcal Z$-stable UCT algebras. No originality is claimed for those
  theorems; the original contribution is only their assembly into the
  stated removal of $\mathbb Q$-stabilization.
- No computation, dataset, or literature search was needed; the route is
  purely deductive synthesis of established classification theory.
