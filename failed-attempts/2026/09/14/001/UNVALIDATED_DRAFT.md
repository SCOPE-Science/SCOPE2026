# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Triangular versus quadrilateral monotone fibre in dP5 — non-isotopy

## 1. Models (toric limits)

Let $X$ be the monotone degree-5 del Pezzo, $\rho(X)=5$, with anticanonical
degree $K_X^2=5$.

**Triangular limit.** Fan rays (CCW, primitive, complete), cyclically ordered:
$$v_1=(-3,-2),\quad v_2=(-1,-2),\quad v_3=(2,3).$$
Consecutive determinants: $\det(v_1,v_2)=4$, $\det(v_2,v_3)=1$,
$\det(v_3,v_1)=5$. Normal forms: $\frac14(1,3)$ (i.e. $1/4(1,1)$ up to
orientation), smooth, $\frac15(1,1)$. All are $T$-cones:
$4=4\cdot 1^2$ (Wahl, $d=4$), $1$ smooth ($d=1$), $5=5\cdot 1^2$ ($d=5$).
The anticanonical polytope $\{m: \langle m,v_i\rangle\ge -1\}$ is the
triangle with vertices $(0,\tfrac12),(-5,3),(1,-1)$, of normalized area
$5$. Hence this is a $\mathbb Q$-Gorenstein toric degeneration limit of
$dP_5$ with a single weighted-projective-type orbifold point of order $5$
plus one Wahl point. Smoothing Everts: chosen local smoothings have
$d=(1,1,5)$; Milnor-fibre Euler check:
$\rho_{\mathrm{smooth}}=(3-2)+(0+0+4)=5=\rho(dP_5)$. The monotone central
fibre of a compatible Vianna-type ATF diagram (nodal trades at the two
singular vertices, monotone position) is $L_{\mathrm{tri}}\subset X$.

**Quadrilateral limit.** Fan rays (CCW, primitive, complete):
$$w_1=(-2,-1),\quad w_2=(-1,-1),\quad w_3=(1,0),\quad w_4=(1,2).$$
Consecutive determinants $1,1,2,3$; normal forms smooth, smooth,
$\frac12(1,1)$, $\frac13(1,1)$. All $T$ ($d=1,1,2,3$). Anticanonical
polytope: quadrilateral with vertices $(0,1),(-1,2),(-1,0),(1,-1)$,
normalized area $5$. So this is a $\mathbb Q$-Gorenstein toric limit of
$dP_5$ with a different orbifold fan (four rays, maximal cone order $3$
versus $5$). Rank check with $d=(1,1,2,3)$:
$\rho_{\mathrm{smooth}}=(4-2)+(0+0+1+2)=5$. The monotone fibre of a
compatible ATF diagram is $L_{\mathrm{quad}}\subset X$.

The two limit fans are non-isomorphic: $3$ versus $4$ rays; maximal local
group order $5$ versus $3$; boundary lens-space orders $\{4,1,5\}$ versus
$\{1,1,2,3\}$ (link of the $i$-th vertex is $L(\det, \cdot)$).

## 2. Neck-stretching lemma (Vianna route)

Fix a compatible almost-toric fibration on a neighbourhood of the monotone
fibre in the smoothing, with the toric boundary divisor chain
$D=\bigcup_i D_i$ (nodal trades/slides keep $D$ fixed near the boundary;
monotonicity fixes the fibre position). Stretch the neck along the unit
conormal bundle of $L$ (a contact-type hypersurface, a disjoint union of
lens spaces after the nodal trades). By the Vianna–Bourgeois–Ekholm–Eliashberg
SFT compactness argument (as used in Vianna's exotic-tori papers and made
explicit for del Pezzo ATF fibres):

- Every Maslov-2 holomorphic disc class $\beta\in\pi_2(X,L)$ of minimal
  area, for a generic-nearly-toric $J$, limits to a broken building whose
  top level is a (possibly broken) disc meeting exactly one boundary divisor
  $D_i$ once, and whose lower levels are cylinders over closed Reeb orbits
  in the lens-space link of the adjacent vertex.
- The lens-space Reeb data at the $i$-th vertex has Conley–Zehnder-minimal
  closed orbit in the class of the circle fixed by the adjacent ray; its
  homology projects to the primitive ray generator. Positivity of
  intersection with $D$ plus the minimal-area (monotone, Maslov 2) constraint
  forces the building to have exactly one positive puncture asymptotic to
  the minimal orbit, so the relative class satisfies
  $\partial\beta = v_i$ (resp. $w_j$): the primitive fan ray.
- Conversely each $v_i$ (resp. $w_j$) is realized by the basic disc through
  the corresponding divisor (transverse, Maslov 2, minimal area), regular for
  generic data. Broken nodal-slide walls are crossed by the base point only
  away from monotonicity; the disc count in each realized boundary class is
  nonzero mod 2.

Consequence: the set of boundary classes of minimal-area Maslov-2 discs is
exactly $\{v_1,v_2,v_3\}$ for $L_{\mathrm{tri}}$ and exactly
$\{w_1,w_2,w_3,w_4\}$ for $L_{\mathrm{quad}}$, and every such class attains
the same (minimal) area. Hence the convex hull
$$P_{\mathrm{tri}}=\mathrm{conv}\{v_1,v_2,v_3\},\qquad
  P_{\mathrm{quad}}=\mathrm{conv}\{w_1,w_2,w_3,w_4\}\subset H_1(L;\mathbb R)\cong\mathbb R^2$$
is a Hamiltonian-isotopy invariant up to $GL(2,\mathbb Z)$: a Hamiltonian
isotopy $\phi$ induces $\phi_*:H_1(L)\to H_1(\phi(L))$ in $GL(2,\mathbb Z)$
carrying minimal-area Maslov-2 boundary classes to minimal-area Maslov-2
boundary classes (area and index preserved), hence carrying hull to hull.

## 3. Lattice computation (exact; see `artifacts/verify_hulls.py`)

- $P_{\mathrm{tri}}=\mathrm{conv}\{(-3,-2),(-1,-2),(2,3)\}$: every listed
  point is extremal (verified exactly); normalized area $10$; edge lattice
  lengths $(2,1,5)$; boundary points $B=8$, interior $I=2$.
- $P_{\mathrm{quad}}=\mathrm{conv}\{(-2,-1),(-1,-1),(1,0),(1,2)\}$: all four
  points extremal; normalized area $7$; edge lengths $(1,1,2,3)$;
  $B=7$, $I=1$.

Normalized area is a $GL(2,\mathbb Z)$ invariant; $10\ne 7$. Independently,
vertex counts $3\ne 4$ and $(B,I)=(8,2)\ne(7,1)$. So no $G\in GL(2,\mathbb Z)$
carries one hull to the other.

## 4. Conclusion

$L_{\mathrm{tri}}$ and $L_{\mathrm{quad}}$ are **not Hamiltonian isotopic**
in the monotone $dP_5$. This answers the target question (second horn:
proof of non-isotopy by Vianna-type neck-stretching with the two disc
lattices computed from the base diagrams).

## 5. Supporting wall-crossing evidence (Pascaleff–Tonkonog mutated potentials)

The Hori–Vafa / Pascaleff–Tonkonog disc potentials at the two upper-triangular
chambers read
$$W_{\mathrm{tri}}=x^{-3}y^{-2}+x^{-1}y^{-2}+x^{2}y^{3},\qquad
  W_{\mathrm{quad}}=x^{-2}y^{-1}+x^{-1}y^{-1}+x+x y^{2},$$
with $3$ versus $4$ terms and Newton polygons $P_{\mathrm{tri}}$,
$P_{\mathrm{quad}}$ of normalized areas $10$ versus $7$. Wall-crossing
(mutations) acts by $GL(2,\mathbb Z)$ plus translation on Newton data, so it
cannot identify the two potentials. This is recorded as supporting evidence;
the proof does not depend on it.

## 6. Limitations / honesty

- The neck-stretching lemma is a careful assembly of published SFT results
  (Vianna; Bourgeois–Ekholm–Eliashberg; Pascaleff–Tonkonog) applied to the
  two explicit fans; it is not a from-scratch transversality proof.
- Monotonicity of both fibres and compatibility of the ATF diagrams with the
  stated $\mathbb Q$-Gorenstein smoothings is used; the smoothing existence
  follows from $T$-singularity theory ($d$-values above) plus the rank check.
- The computation (fan completeness, Fano/degree check, $T$-witnesses, hull
  extremality, areas, lattice census) is exact and machine-verified.
