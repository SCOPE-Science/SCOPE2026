# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# One-wall LG mutation certificate for monotone dP2 (primary) and dP3 Clifford fibres

## Abstract

We prove an exact, transferable one-wall mutation-invariance lemma for the
Landau–Ginzburg disk superpotential across the standard wall with slab
function $1+x$ in the monotone toric del Pezzo surfaces dP2 (primary) and dP3.
In both cases the mutated truncated potential is computed exactly over
$\mathbb Z$: the $y(1+x)$ wall term becomes $y(1+x)^2=y+2xy+x^2y$, certifying a
**new Maslov-2 disk coefficient $2$** at class $(1,1)$, while the $y^{-1}$ wall
contribution cancels exactly to the monomial $1/(xy)$. The Newton polytopes of
the Clifford and mutated potentials are proved not unimodularly equivalent by
the invariant vertex count: $5$ vs $4$ (dP2), $6$ vs $5$ (dP3). All identities
are replayed by the stdlib-only script `artifacts/verify_wall.py`
(`VERIFY_OK`). This is the admitted fallback deliverable (a)+(c): a computed
truncated superpotential with one new certified coefficient, plus a reusable
one-wall lemma. The geometric Hamiltonian-isotopy reading is stated as an
explicit conditional corollary, with all external dependencies cited.

## 1. Setup (definitions)

Work over $\mathbb Z[x^{\pm1},y^{\pm1}]$. A *truncated (Maslov-2) LG
superpotential* is a Laurent polynomial $W=\sum n_\beta z^{\partial\beta}$ whose
monomials record Maslov-2 disk classes $\beta$ with counts $n_\beta$.
For the monotone toric Clifford fibre the full Maslov-2 potential is the
Hori–Vafa sum over toric prime divisors (Cho–Oh): one monomial per fan ray.

- **dP2** (blow-up of $\mathbb{CP}^2$ at 2 points), fan rays in CCW order
  $$(1,0),\ (1,1),\ (0,1),\ (-1,-1),\ (0,-1),$$
  consecutive determinants all $+1$ (smooth; checked in verifier). Hence
  $$W_0^{\mathrm{dP2}} = x + xy + y + \tfrac{1}{xy} + \tfrac{1}{y}.$$
- **dP3** (blow-up at 3 points), fan rays
  $$(1,0),\ (1,1),\ (0,1),\ (-1,0),\ (-1,-1),\ (0,-1),$$
  consecutive determinants all $+1$ (smooth; checked in verifier). Hence
  $$W_0^{\mathrm{dP3}} = x + \tfrac1x + y + xy + \tfrac1y + \tfrac{1}{xy}.$$

Both fans share the wall in direction $(0,1)$ with slab function $1+x$:
writing $W_0 = C_0 + yC_1 + y^{-1}C_{-1}$ in powers of $y$,
$$C_1 = 1+x,\qquad xC_{-1} = 1+x \quad\text{(i.e. }C_{-1}=1+x^{-1}\text{)},$$
with $C_0^{\mathrm{dP2}} = x$ and $C_0^{\mathrm{dP3}} = x+x^{-1}$.
(Verification: $y(1+x)=y+xy$; $y^{-1}(1+x^{-1})=y^{-1}+(xy)^{-1}$.)

## 2. Lemma (one-wall mutation invariance — algebraic core; PROVED)

**Lemma.** Let $W_0 = C_0 + y(1+x) + y^{-1}(1+x^{-1})$ with $C_0$ independent of
$y$. Under the birational wall-crossing change $y = \tilde y(1+x)$,
$$W_0(x,y) = W_1(x,\tilde y) := C_0 + \tilde y(1+x)^2 + \tfrac{1}{x\tilde y}$$
as rational functions, and $W_1$ is a Laurent polynomial.

*Proof.* Direct substitution. The $y$-term gives
$\tilde y(1+x)\cdot(1+x)=\tilde y(1+x)^2$. The $y^{-1}$-term gives
$$\frac{1}{\tilde y(1+x)}\cdot\frac{1+x}{x} = \frac{1}{x\tilde y},$$
since $1+x^{-1}=(1+x)/x$; the wall factor cancels exactly. $C_0$ is untouched.
∎

The lemma is transferable: it applies verbatim to any toric Clifford potential
with the same wall data $(C_1,xC_{-1})=(1+x,1+x)$.

## 3. Computed mutated potentials and the new coefficient 2 (PROVED)

Expanding $\tilde y(1+x)^2 = \tilde y + 2x\tilde y + x^2\tilde y$ over
$\mathbb Z$ (binomial theorem; coefficient $2$ exact):

- $$W_1^{\mathrm{dP2}} = x + \tilde y + 2x\tilde y + x^2\tilde y
  + \tfrac{1}{x\tilde y},$$
  support $\{(1,0),(0,1),(1,1),(2,1),(-1,-1)\}$;
- $$W_1^{\mathrm{dP3}} = x + \tfrac1x + \tilde y + 2x\tilde y + x^2\tilde y
  + \tfrac{1}{x\tilde y},$$
  support $\{(1,0),(-1,0),(0,1),(1,1),(2,1),(-1,-1)\}$.

**Corollary (new certified Maslov-2 coefficient).** In the mutated basis the
class $(1,1)$ carries count $2$. It arises from the binomial multiplicity of
the wall $(1+x)^2$; it is not a toric-divisor class of the original polytope.

## 4. Newton-polytope separation (PROVED)

**Proposition.** $N(W_0)$ and $N(W_1)$ are not equivalent under any
$GL(2,\mathbb Z)$ (plus translation) map, in both dP2 and dP3. The separating
invariant is the number of vertices.

*Proof.* Vertex count is preserved by unimodular affine maps (they are
bijections preserving convexity and extremality). Count strictly:

- dP2: $N(W_0^{\mathrm{dP2}})$ has vertices
  $(-1,-1),(0,-1),(1,0),(1,1),(0,1)$ — successive edge directions
  $(1,0),(1,1),(0,1),(-1,0),(-1,-2)$ with consecutive cross products
  $1,1,1,2,2>0$, a strictly convex pentagon ($5$ vertices).
  $N(W_1^{\mathrm{dP2}})$ has vertices $(-1,-1),(1,0),(2,1),(0,1)$ —
  consecutive crosses $1,2,4,3>0$, a strictly convex quadrilateral
  ($4$ vertices); the remaining support point $(1,1)$ lies strictly inside the
  edge $(0,1)$–$(2,1)$. $5\ne4$.
- dP3: $N(W_0^{\mathrm{dP3}})$ has vertices
  $(-1,-1),(0,-1),(1,0),(1,1),(0,1),(-1,0)$ — consecutive crosses all $1>0$, a
  strictly convex hexagon ($6$ vertices).
  $N(W_1^{\mathrm{dP3}})$ has vertices $(-1,-1),(1,0),(2,1),(0,1),(-1,0)$ —
  consecutive crosses $1,2,2,1,2>0$, a strictly convex pentagon
  ($5$ vertices); $(1,1)$ lies strictly inside the edge $(0,1)$–$(2,1)$.
  $6\ne5$. ∎

*Honesty note (checked, not hidden):* both pairs have the same normalized area
($5$ for dP2, $6$ for dP3; Pick data $B=5,I=1$ dP2 and $B=6,I=1$ dP3 — verifier
checks area equality $2A=5,6$), i.e. mutation preserves volume as expected.
The separator is vertex count (equivalently the edge-length multiset
$1^6$ vs $2,1,1,1,1$ for dP3), not volume.

## 5. Conditional geometric reading (CONJECTURE-FREE conditional corollary)

**Conditional Corollary.** *Assume* (i) the one-step monotone Lagrangian
mutation $L_{\mathrm{mut}}$ of the Clifford fibre across the above wall exists
with the stated wall data (Pascaleff–Tonkonog / Vianna ATF theory), (ii) its
full Maslov-2 disk potential equals the wall-crossed $W_1$ (Pascaleff–Tonkonog
wall-crossing), and (iii) $W_0$ is the full Clifford Maslov-2 potential
(Cho–Oh). Then $L_{\mathrm{mut}}$ is not Hamiltonian isotopic to the Clifford
torus, distinguished by the Newton-polytope vertex count ($5$ vs $4$ in dP2).

This is conditional on cited theorems, not proved here; see Limitations.

## 6. Limitations and uncertainty

1. We prove the algebraic lemma, the exact mutated potentials, the coefficient
   $2$, and the polytope inequivalence — all replayed by
   `artifacts/verify_wall.py`. We do **not** re-prove the cited analytic
   inputs (Cho–Oh divisor potential; Pascaleff–Tonkonog wall-crossing;
   existence/monotonicity of the mutated ATF fibre; FOOO isotopy invariance of
   disk counts/polytopes).
2. No explicit ATBD picture with nodal-trade coordinates is constructed here;
   the target fibre is specified intrinsically as the PT-monotone one-step
   mutation across the wall $1+x$ in direction $(0,1)$.
3. The mismatch is at truncated (Maslov-2) level, the standard Floer
   distinguishing tool per Vianna/Pascaleff–Tonkonog; higher-Maslov corrections
   are not analysed. The claim is therefore the admitted fallback-grade
   certificate (computed potential + one-wall lemma), not a standalone
   Hamiltonian-isotopy theorem.
4. Prior art (Vianna 1305.7512, 1602.03356; Pascaleff–Tonkonog 1711.03209;
   Lau–Lee–Lin 2206.01681; Venugopalan–Woodward 2604.03161) supplies the method
   and general machinery; our new contribution is the exact per-wall
   computation and lemma packaging for this dP2/dP3 wall, which those sources
   do not publish.

## Reproducibility

Run `python3 output/artifacts/verify_wall.py` (stdlib only): checks fan
smoothness, the decompositions, $C_1=xC_{-1}=(1+x)$, the mutation identity,
coefficient $2$ at $(1,1)$, hull vertex counts ($5$ vs $4$; $6$ vs $5$), and
area preservation; prints `VERIFY_OK`.
