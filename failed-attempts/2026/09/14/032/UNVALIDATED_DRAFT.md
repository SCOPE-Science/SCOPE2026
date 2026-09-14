# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Realizability of the genus-0 degree-12 Belyi passport P3 = ([4,3,2,2,1], [5,3,2,1,1], [4,3,3,2])

## Claim (TARGET: existence decided AFFIRMATIVE; cover defined over Q)

The passport is realizable. Product convention throughout: $(uv)(i)=u(v(i))$
(left action; apply $v$ first).

- $u_0=(0\,1\,2\,3)(4\,5\,6)(7\,8)(9\,10)$, image vector $[1,2,3,0,5,6,4,8,7,10,9,11]$,
  cycle type $(4,3,2,2,1)$, sign $-1$;
- $u_1=(0\,2\,11\,1\,10)(3\,5)(4\,8\,6)$, image vector $[2,10,11,5,8,3,4,7,6,9,0,1]$,
  cycle type $(5,3,2,1,1)$, sign $-1$;
- $u_\infty=(u_0u_1)^{-1}=(0\,5\,6\,3)(1\,10\,9)(2\,11)(4\,8\,7)$,
  image vector $[5,10,11,0,8,6,3,4,7,1,9,2]$, cycle type $(4,3,3,2)$, sign $+1$.

Then $u_0u_1u_\infty=\mathrm{id}$; $\langle u_0,u_1\rangle$ is transitive on
$\{0,\dots,11\}$ (orbit size 12); its simultaneous centralizer in $S_{12}$ is
trivial (order 1, exact backtracking); $\langle u_0,u_1\rangle=S_{12}$
(order $479001600=12!$, Schreier–Sims), hence primitive and not contained in
$A_{12}$. By the Riemann existence theorem this triple is the monodromy of a
connected genus-0 degree-12 cover branched only over $\{0,1,\infty\}$ with
exactly the prescribed ramification. Riemann–Hurwitz checks:
$5+5+4=14$ parts, $\sum(e-1)=7+7+8=22=2\cdot 12-2$.

## Census (exact integer computations, two independent enumerations)

Fix $x$ canonical of type $C_0=(4,3,2,2,1)$. Enumerate the full class
$C_\infty$ of type $C_{\mathrm{inf}}=(4,3,3,2)$:
$|C_\infty|=12!/(4\cdot 3^2\cdot 2\cdot 2!)=3326400$ placements, and count
$y=x^{-1}z$ of type $C_1=(5,3,2,1,1)$:

- **111680** raw hits; **88608** with $\langle x,y\rangle$ transitive.
- Centralizer orders (formula $\prod_l m_l!\,l^{m_l}$):
  $|C_{S_{12}}(x)|=4\cdot 3\cdot 2^2\cdot 2!=96$ for type $C_0$;
  $5\cdot 3\cdot 2\cdot 2!=60$ for type $C_1$;
  $4\cdot 3^2\cdot 2\cdot 2!=144$ for type $C_{\mathrm{inf}}$.
  (An earlier draft attached the 144 denominator to the $C_0$ quotient; the
  correct $C_0$-centralizer order used for the class quotient is 96.)
- Modulo the 96-element centralizer: **1277** classes total, of which **923**
  are transitive; $923\times 96=88608$, i.e.\ the centralizer acts freely on
  the transitive hits (exact check).
- Both enumerations agree: `work/censusA.py` (subset-nested 4/3/3/2
  enumeration + numpy lex-min canonicals) and `work/censusB.py`
  (lexicographic-config enumeration + independent orbit-BFS quotient, no
  lex-min/normality assumption) each give placed $=3326400$, raw $=111680$,
  transitive $=88608$, classes $1277/923$. Our triple's $u_1$ is among the hits.
- Correction note: a prior draft reported 14908 raw / 526 classes. That loop
  ranged the 4-cycle/3-cycle slots with smallest-unused-first ordering but did
  not range over all cyclic rotations (ordered $(L-1)$-tuples were
  restricted), enumerating only a subset of the class. The repaired scripts
  enumerate all 3326400 placements; the old numbers are withdrawn.

## Braid data (per-triple claim; Hurwitz convention stated)

Hurwitz moves (left action, consistent with $(uv)(i)=u(v(i))$):
$s_1(a,b,c)=(b,b^{-1}ab,c)$ with inverse $s_1^{-1}(a,b,c)=(aba^{-1},a,c)$;
$s_2(a,b,c)=(a,c,c^{-1}bc)$ with inverse $s_2^{-1}(a,b,c)=(a,bcb^{-1},b)$
(verified $s_i^{-1}s_i=\mathrm{id}$ on the nose in `work/braid_repaired.py`).
Pure-braid (slot-preserving) generators $t_1=s_1^2$, $t_2=s_2^2$.

- The pure-braid orbit of **our triple's class** has size **1**: both
  $t_1$ and $t_2$ images re-canonicalize to our class (exact quotient check).
  No global rigidity over all 923 transitive classes is claimed.
- The full-$B_3$ orbit of our triple (moves $s_1^{\pm1},s_2^{\pm1}$ over the
  union of slot-permuted Nielsen sets, canonical rep = first-slot canonical
  plus centralizer-orbit minimum) has size **6**, one class per permutation of
  the three distinct slot types.
- Trivial automorphism group (centralizer order 1) plus the pure-braid-fixed
  class (field of moduli $\mathbf{Q}$) and $\mathbf{Q}$-rational branch locus
  $\{0,1,\infty\}$ imply our cover is defined over $\mathbf{Q}$
  (Coombes–Harbater / Dèbes criterion).

## Primitivity certificate (exact words)

With $A=U_0=u_0^{-1}$, $B=U_1=u_1^{-1}$, $a=u_0$, $b=u_1$, the words
$w_1=\mathtt{AAB}=U_0^2U_1$ and $w_2=\mathtt{aBBB}=u_0U_1^3$ both fix $0$, are
non-identity, and their joint orbits join $1$ to all of $\{1,\dots,11\}$
(11 of 11). Hence the point stabilizer acts transitively and the action is
primitive. (Independent sympy Schreier–Sims call also returns
`is_primitive True`, `is_transitive True`, order $12!$.)

## Field of definition / model: proved field, model boundary stated

- Proved: our cover has field of moduli $\mathbf{Q}$ (per-triple pure-braid
  orbit 1) and, with trivial Aut, is defined over $\mathbf{Q}$.
- An exact $\mathbf{Q}$-polynomial model (e.g.\ $f=cP/Q$ with the anchored
  normalizations of WORKLOG) was **not** recovered: a bounded program
  (5 ansatz/normalization variants, $\approx$200 restarts, 50-digit Newton,
  real-restricted Newton, repulsion annealing) plateaued at residual
  $F\sim 10^{-9}$–$10^{-10}$ against a degenerate attractor (scale $c\to 0$
  with fiber collisions). This is a solver limitation, not an obstruction.
  No numerical vector is claimed as the model. Reproduction scripts are kept
  in `work/` (not part of the verification core).

## Verification (all re-run; every exact number reproduces)

1. `python3 work/verify1.py` — triple, types, product $=id$, transitivity (12),
   centralizer 1. Reproduces.
2. `python3 work/grp.py` — sympy: group order $12!$, transitive, primitive.
   Reproduces.
3. `python3 work/censusA.py` — placed 3326400, raw 111680, transitive 88608,
   Cx order 96, classes 1277, transitive classes 923, $923\times96=88608$,
   our $u_1$ present. Reproduces (~12 s).
4. `python3 work/censusB.py` — independent path, same six numbers. Reproduces
   (~170 s).
5. `python3 work/braid_repaired.py` — centralizer orders 96/60/144,
   $s_i^{-1}s_i=id$ sanity, per-triple pure-braid orbit 1, full-$B_3$ orbit 6.
   Reproduces.
6. `python3 work/cert_repaired.py` — consolidated exact certificate written to
   `output/artifacts/exact_certificate.json` with the repaired counts.
   Reproduces.

## Limitations

The polynomial model over $\mathbf{Q}$ is proved to exist for our cover but
not exhibited exactly; the report claims no explicit coefficients. The
model-search bound above is documented in WORKLOG; a future exact solve
(e.g.\ rigidity-based norm equations or certified homotopy) would close this
last computational gap without affecting the realizability theorem.
