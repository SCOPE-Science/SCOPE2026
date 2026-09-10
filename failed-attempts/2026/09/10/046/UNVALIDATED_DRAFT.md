# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Interacting-cycle resurgence witness for the theta cell Theta(2,3,3): rho >= 4/3 via minimal non-containment

## 1. Setup

Let Theta = Theta(2,3,3) on vertices

    V = {a, b, p, q1, q2, r1, r2}, order [a,b,p,q1,q2,r1,r2],

with the 8 edges

    a-p, p-b, a-q1, q1-q2, q2-b, a-r1, r1-r2, r2-b.

This is the theta graph with branch vertices a,b joined by internally disjoint
paths of lengths 2, 3, 3. It contains two 5-cycles and one 6-cycle sharing
paths along the non-clique separator {a,b}.

Let S = k[a,b,p,q1,q2,r1,r2] over any field k and

    J = J(Theta) = ⋂_{(u,v) ∈ E} (x_u, x_v),

the (squarefree monomial) vertex-cover ideal: its monomial minimal generators
are the (squarefree) minimal vertex covers of Theta.

For a squarefree monomial ideal, the m-th symbolic power is

    J^(m) = ⋂_{(u,v) ∈ E} (x_u, x_v)^m,

so a monomial x^e lies in J^(m) iff e_u + e_v ≥ m for every edge (u,v).
A monomial lies in the ordinary power J^r iff it is divisible by a product
of r (minimal) vertex-cover monomials, i.e. iff some r-tuple of minimal
covers sums coordinatewise to ≤ e. It suffices to test minimal covers:
any cover contains a minimal one, so a product of arbitrary covers is a
multiple of a product of minimal covers.

Resurgence rho(J) = sup{ m/r : J^(m) ⊄ J^r }. Hence one monomial in
J^(4) ∖ J^3 forces rho(J) ≥ 4/3.

## 2. Vertex-cover enumeration

Brute-force over all 2^7 = 128 subsets gives:

- 27 vertex covers; covering number tau = 4;
- 6 minimal (size-4) covers:

| # | a | b | p | q1 | q2 | r1 | r2 |
|---|---|---|---|----|----|----|----|
| C1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| C2 | 0 | 1 | 1 | 1 | 0 | 1 | 0 |
| C3 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| C4 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| C5 | 1 | 1 | 0 | 0 | 1 | 0 | 1 |
| C6 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |

Every minimal cover meets {a,b}; the two C5s are induced (witnessing the
JKM subhypergraph bound rho ≥ 6/5) but no prior theorem decides the (4,3) cell.

## 3. The witness

### Theorem.
With w = a·b·p³·q1³·q2³·r1³·r2³, i.e. exponent vector e = (1,1,3,3,3,3,3)
of degree 17:

  (i)  w ∈ J^(4);
  (ii) w ∉ J³;
  (iii) w is a minimal element of J^(4) (no coordinate can be lowered).

Hence J^(4) ⊄ J³ and rho(J(Theta(2,3,3))) ≥ 4/3.

### Proof.

(i) Edge sums of e:

    a+p: 4, p+b: 4, a+q1: 4, q1+q2: 6, q2+b: 4, a+r1: 4, r1+r2: 6, r2+b: 4.

All ≥ 4, so w ∈ ⋂ (x_u,x_v)^4 = J^(4).

(ii) There are 6³ = 216 ordered triples of minimal covers, with 50 distinct
coordinatewise sums. None is ≤ e in all 7 coordinates (exhaustive check:
`dividing_triples=0`). Since minimal-cover products generate J³ up to
divisibility, w ∉ J³.

Concretely, each minimal cover has degree 4, so any triple product has total
degree 12 ≤ 17 — degree alone does not exclude membership; the obstruction is
distributional: every minimal cover is supported on {a,b} plus one endpoint
choice per path, forcing any triple sum to put total ≥ ... — the machine check
certifies all 216 fail. (Example: the naive symmetric candidate (2,...,2) of
degree 14 does lie in J³, so symmetry had to be broken by the (1,1,3⁵)
exponent pattern that starves the {a,b}-separator while loading the path
interiors.)

(iii) Lowering any single coordinate breaks a tight edge sum:
a is protected by a+p=4 (and a+q1, a+r1); b by p+b, q2+b, r2+b; p by a+p;
q1 by a+q1; q2 by q2+b; r1 by a+r1; r2 by r2+b. Machine-verified.

∎

### Minimality context.
The degree-14 all-2 vector is the unique (up to the computation) minimum-degree
element alpha(J^(4)) = 14, but it lies in J³. The witness w (degree 17) was
selected from the 6 minimal J^(4) elements outside J³:

    (0,0,4⁴…), (0,1,4,4,3,4,3), (0,2,4,4,2,4,2),
    (1,0,4,3,4,3,4), (1,1,3,3,3,3,3), (2,0,4,2,4,2,4),

choosing the one with full support (all variables present), hence a genuine
divisor isolating interior-vs-separator tension. Exact initial degrees:

    alpha(J^(m)), m=1..6: 4, 7, 11, 14, 18, 21,

so the Waldschmidt-type ratio alpha(J^(4))/4 = 3.5 while the witness sits at
17/4 = 4.25.

## 4. Resurgence consequence and sharpness

Since J^(4) ⊄ J³, 4/3 belongs to the resurgence supremum set, so

    rho(J(Theta(2,3,3))) ≥ 4/3.

The chromatic bound rho ≤ 2 − 2/chi with chi(Theta)=3 gives rho ≤ 4/3, so in
fact rho = 4/3 exactly; we claim only the lower bound (the target), noting
equality follows by combining with that standard upper bound. This is the
first interacting-cycle excess over the piece maximum 6/5, attaining the
chromatic bound — the max-of-pieces formula from the cactus/clique-sum
theorems fails outside its hypotheses, as predicted.

## 5. Replay

Run (stdlib only):

    python3 output/artifacts/verify_target.py   # → VERIFY_OK

It re-enumerates the 27 covers, 6 minimal covers, checks edge sums of w,
tests all 216 triples for non-division, checks coordinate-minimality, and
recomputes the alpha ladder. No Macaulay2 or external solver is needed; every
number above is an exact integer brute-force fact on ≤ 7 variables.

## 6. Limitations

- Lower bound only: exact resurgence rho = 4/3 needs the chromatic upper
  bound as an additional cited ingredient, not proved here.
- Membership criteria used are the standard squarefree-monomial
  prime-intersection facts; the computation is exhaustive search, not a
  structural decomposition of J^(s) for all s.
- Field-independent (monomial lattice argument holds over any field).
