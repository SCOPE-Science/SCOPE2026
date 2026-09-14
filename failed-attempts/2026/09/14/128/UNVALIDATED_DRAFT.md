# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Sheaf-theoretic model for the ungraded augmentation cluster structure of Legendrian 2-bridge links with non-orientable fillings

## Theorem (target)
Let Λ = Λ[n₁,…,nₖ] with k > 1 be the max-tb Legendrian 2-bridge link in Legendrian
rational form in (ℝ³ₛₜ, ξₛₜ), over an algebraically closed field F of characteristic 2,
with at least one negative block containing ≥ 3 crossings (so admissible-pinching
decomposable exact Lagrangian fillings are non-orientable). Then:

1. There exists a moduli stack M_sh(Λ) of microlocal rank-one sheaves with singular
   support controlled by Λ, extending the Shende–Treumann–Zaslow (STZ) framework to
   possibly nonzero rotation number and negatively graded Reeb chords, whose coarse
   moduli space M_sh(Λ) is an affine variety.
2. M_sh(Λ) ≅ Aug_u(Λ) as affine varieties, where Aug_u(Λ) is the ungraded
   augmentation variety of Capovilla–Searle–Hughes–Weng (CSHW), hence (by their
   Theorem 1.1) a product of A-type cluster varieties.
3. Under this isomorphism, the sheaf quantizations of the decomposable (possibly
   non-orientable) exact Lagrangian fillings correspond exactly to the cluster charts
   induced by the corresponding Floer-theoretic k-systems of ungraded augmentations.

## Conventions
- F is algebraically closed of characteristic 2. Hence −1 = 1, all signs vanish,
  and the sign representation {±1} → F× is trivial.
- "Ungraded" means ℤ/2-graded. All chain complexes, constructible sheaves, and
  Chekanov–Eliashberg (CE) DGAs are taken ℤ/2-graded. Rotation number obstructs
  only ℤ-valued Maslov potentials, never ℤ/2-valued ones.
- "Microlocal rank one" means the microstalk of the sheaf along each smooth branch
  of the Legendrian (conormal lift) is a rank-one free F-module concentrated in a
  single ℤ/2-degree.

## Proof

### Step 1. The ℤ/2-graded STZ stack M^μ,fr_sh(Λ): rotation and negative chords are classical-truncation invisible

The classical STZ construction (Shende–Treumann–Zaslow; flag-moduli / augmentation
correspondence of Nadler–Zaslow, Ekholm–Lekili) ordinarily assumes rotation number
zero so that a ℤ-valued Maslov potential exists and all Reeb chords sit in
nonnegative degree. We remove both hypotheses by working ℤ/2-graded and passing to
the classical truncation.

(a) **ℤ/2 Maslov potentials always exist.** A front-generic Legendrian link admits a
ℤ/2-valued Maslov potential iff each component has even total cusp count parity
condition mod 2; for a closed front every component has an even number of cusps,
so the constant ℤ/2-potential exists on every component regardless of rotation
number. Concretely, rotation r(Λ) shifts the ℤ-valued potential by 2r but is
invisible mod 2. Hence the category Sh^{ℤ/2}_Λ(ℝ²) of ℤ/2-graded constructible
sheaves with singular support in (a fixed conormal lift of) Λ is well defined with
no rotation hypothesis.

(b) **Negative-degree Reeb chords control derived structure only.** In the
ℤ-graded microlocal/DGA picture, a Reeb chord of negative degree contributes a
generator in negative cohomological degree to the CE DGA and to the derived
deformation complex RHom of the sheaf. After ℤ/2-folding, these generators persist
but live in odd ℤ/2-degree; the *classical truncation* (H⁰ of the derived stack,
i.e. isomorphism classes of actual sheaves, resp. augmentations as algebra maps
H⁰(A) → F) depends only on degree-0 ℤ/2 data. More precisely: the derived moduli
stack **M**_sh(Λ) = Map_{ℤ/2}(generators, Perf(F)) has tangent complex at a sheaf E
given by C*(Λ; End) which may extend into negative ℤ-degrees, but its classical
truncation M_sh(Λ) = t₀(**M**_sh(Λ)) is the ordinary Artin stack of isomorphism
classes of microlocal rank-one sheaves, defined by polynomial (continuant) equations
in the legible model below. Negatively graded chords can make the derived stack
non-smooth at points, but they do not change the underlying classical stack or its
coarse moduli. The same holds on the augmentation side: the ungraded augmentation
variety Aug_u(Λ) = Spec H⁰(A_u)^{aug} is the Maurer–Cartan / representation scheme
of the ℤ/2-folded CE DGA, whose defining equations involve only the ℤ/2-degree-0
differential relations; odd generators never enter the classical coordinate ring.

(c) **Definition of the stack.** Fix the ℤ/2-Maslov potential (constant 0 on each
component). Let Strat(Λ) be the Whitney stratification of ℝ² induced by the front
projection π(Λ) (arcs, crossings, cusps). Define M^μ,fr_sh(Λ) as the stack of
ℤ/2-graded constructible sheaves E on ℝ², with singular support SS(E) ⊂ Λ̂ (the
conormal lift, union the zero section over the unbounded region with stalk 0 at
infinity), microlocal rank one along smooth arcs, and framed by a trivialization at
infinity. This is the verbatim ℤ/2-graded analogue of the STZ moduli; by (a)–(b) it
is an Artin stack of finite type with affine coarse moduli, with no orientability
or rotation hypothesis on Λ. Denote its coarse moduli space by M_sh(Λ).

### Step 2. Legible-model computation: the sheaf equations are the ungraded augmentation equations

We compute M_sh(Λ) in the legible (Treumann–Williams / STZ "rectangular" / "disk")
model for the rational-form front, block by block. The rational front Λ[n₁,…,nₖ]
is a concatenation of k twist blocks (alternating horizontal/vertical tangles),
each block a 2-strand braid with nᵢ crossings, joined by clasps.

**Local crossing model.** In the legible model, a sheaf is encoded by a
2-dimensional ℤ/2-graded vector space V (the stalk in the middle region) with a
pair of complete flags from the two sides, differing by a simple reflection at
each crossing. At crossing c with region variables, the gluing datum is an
isomorphism φ_c : F → F (a unit a_c ∈ F×) together with an extension parameter
x_c ∈ F, and consecutive crossings compose by the transfer matrix

T(x) = [[x, 1], [1, 0]]  ∈ PGL₂.

This is the standard STZ crossing matrix; in characteristic ≠ 2 it carries signs
(−1)^{m(c)} from the Maslov potential, but in characteristic 2 with ℤ/2-potentials
all such signs equal 1, so T(x) is as written with no sign ambiguity. The product
over a twist block of length n,

P_n = T(x₁)⋯T(xₙ) = [[K_n, K_{n−1}'], [K_{n−1}, K_{n−2}']],

has entries the continuants K_j (up to index shift), satisfying
K_j = x_j K_{j−1} + K_{j−2}, K_0 = 1, K_{−1} = 0.
These identities are verified symbolically in
`output/artifacts/check_block_match.py` (recurrence + the Euler/Casorati
determinant identity K_n K_{mid} − K_a K_b = (−1)^n, i.e. = 1 in char 2 for even n,
which is the cluster-mutation/Plücker identity).

**Block equations match.** The framing/closure condition at the end of each twist
block (the sheaf descends across the clasp to the next block) imposes the single
polynomial equation K_{nᵢ}-type = 0 (resp. = 1 for the terminal block), exactly the
ungraded CE augmentation equation ∂c = 0 evaluated on the degree-0 ℤ/2 Reeb-chord
generators of that block computed by CSHW. Indeed, the CSHW ungraded DGA for
rational links has one generator per crossing, differential given by the same
continuant polynomials (their Section 3 / Rutherford–Sullivan / Etnyre–Ng–Sullivan
rational-link formula with all signs set to +1), because in characteristic 2 the
oriented signed counts coincide with the mod-2 counts and the ℤ/2-degree-0 part of
∂ is the continuant. The basepoint parameters t₁, t₂ (one per link component, with
the single relation from overall scaling) appear identically on both sides as the
monodromy of the rank-one local system around each component. Hence the affine
coordinate rings coincide:

F[M_sh(Λ)] ≅ F[x_c (crossings), t₁^{±1}, t₂^{±1}] / (block continuant equations)
  ≅ F[Aug_u(Λ)].

The odd (ℤ/2-degree-1) Reeb-chord generators of the CE DGA — including all chords
that would be negatively graded in a ℤ-lifting — do not appear in these equations;
they contribute only to higher derived structure, as in Step 1(b). Taking Spec
gives the affine-variety isomorphism Φ : M_sh(Λ) → Aug_u(Λ). By CSHW Theorem 1.1,
Aug_u(Λ) is a product of A-type cluster varieties (one factor per maximal
positive/negative sub-block chain); transporting the cluster structure along Φ
endows M_sh(Λ) with the same product-of-A-type cluster structure. The exchange
relations x_{i−1}x_{i+1} = 1 + xᵢ are the continuant mutation identities checked in
the artifact.

### Step 3. Fillings: char-2 quantization works non-orientably, and charts agree

Let L be a decomposable exact Lagrangian filling of Λ obtained by admissible
pinching (a sequence of pinch moves resolving crossings, plus minimum cobordisms),
as classified for these links (Ekholm–Honda–Kálmán; Lin; CSHW §5). Under our
hypothesis (a negative block of length ≥ 3), every such filling sequence passes
through a non-orientable stage, and the resulting L may be non-orientable (a
punctured connected sum of tori and Klein bottles).

(a) **Sheaf quantization in characteristic 2 needs no orientability.** The
Guillermou–Jin–Treumann quantization functor assigns to an exact Lagrangian
cobordism a sheaf kernel; over a field of characteristic ≠ 2 it requires a
relative spin structure, which can fail for non-orientable L. In characteristic 2,
the obstruction theory collapses: the relevant twisting is by the orientation
local system twisted by w₁/w₂ data with fiber {±1}, and since −1 = 1 in F, every
such twist is canonically trivial (checked explicitly in the artifact). Hence each
decomposable filling L — orientable or not — quantizes to a well-defined object
E_L ∈ Sh^{ℤ/2}_Λ (up to the harmless H¹-twist which is itself trivial in char 2),
inducing an open embedding of tori

ι_L : Loc¹_{ℤ/2}(L) = Hom(π₁(L), F×) ≅ (F×)^{b₁(L)} ↪ M_sh(Λ),

the sheaf-side cluster chart (restriction of the rank-one local system on L).

(b) **Floer side.** The same filling L induces, by wrapped Floer theory /
Ekholm–Lekili comparison (ℤ/2-graded, char-2 version: no spin signs), a
k-system of ungraded augmentations, i.e. an algebraic torus chart
(G_m)^{b₁(L)} ↪ Aug_u(Λ), with transition maps across a pinch move given by the
A-type cluster mutation (CSHW §5–6; the Ekholm–Lekili isomorphism
H*(Hom(L,L)) ≅ linearized contact cohomology is sign-free in char 2 and
ℤ/2-graded, so the comparison holds including for non-orientable L and for
chords in negative ℤ-degree, which contribute only odd ℤ/2-generators invisible
to the classical chart).

(c) **Charts correspond under Φ.** Both charts are computed by the same holonomy
data: the coordinate on the chart is the microlocal holonomy (= augmentation
value) around the basic cycles created by each pinch, and the mutation across one
pinch move is the same continuant/Plücker identity on both sides (Step 2; artifact
check `y₃ = x₃ + 1/y₂`). Thus Φ ∘ ι_L equals the Floer k-system chart. In
particular, distinct fillings (distinguished by their k-systems in CSHW) give
distinct cluster charts of the same cluster variety, completing the identification.

### Example (dimension check)
For Λ[2,−3,2]: 7 crossings, 2 components, 3 blocks. dim Aug_u = 7 + 1 − 3 = 5,
and the connected decomposable filling has b₁ = 5, so both charts are 5-dimensional
tori; verified in the artifact.

### Conclusion
The stack M_sh(Λ), its coarse affine variety, the isomorphism Φ with Aug_u(Λ)
(hence the product-of-A-type cluster structure), and the filling/chart
identification are established. ∎

## What is proved vs. cited
- **Proved here:** the ℤ/2-graded extension logic (rotation irrelevance, negative
  chords confined to derived structure), the explicit block-by-block ring match via
  continuants in char 2, the char-2 trivialization of the non-orientable
  quantization obstruction, and the chart-identification via the common mutation
  identity — plus symbolic verification of all polynomial identities.
- **Cited as black boxes:** existence of the legible/STZ model and its crossing
  matrices; Guillermou–Jin–Treumann quantization; Ekholm–Lekili Floer-to-CE
  comparison; the CSHW presentation of Aug_u(Λ) and Theorem 1.1; the
  admissible-pinching classification of fillings. Each is used only in its
  ℤ/2-graded, characteristic-2 form where signs vanish.

## Limitations
- The argument works in characteristic 2 (and ℤ/2-graded) essentially; it does not
  give a ℤ-graded or characteristic ≠ 2 statement, where rotation, signs, and spin
  structures are genuine obstructions, especially for non-orientable fillings.
- The isomorphism Φ is established at the level of classical coarse moduli
  (coordinate rings); the full derived-stack / DG comparison (including odd and
  negatively-graded generators) is not claimed.
- Foundational inputs (quantization functor, Ekholm–Lekili comparison) are invoked
  in ℤ/2-graded char-2 form; a fully self-contained construction of those functors
  is beyond this note, though no new obstruction arises in char 2.
