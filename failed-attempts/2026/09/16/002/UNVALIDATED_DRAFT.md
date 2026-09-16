# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Connected étale and Lagrangian algebras in non-multiplicity-free rank-6 modular categories

## Result (target claim, proved)

Let B be a modular fusion category over C with rank(B) = 6 whose Grothendieck
ring is **not** multiplicity-free (some N_{ij}^k ≥ 2). Then:

**(a) Exhaustion.** Up to fusion-ring isomorphism there are exactly **three**
non-multiplicity-free rank-6 modular fusion rings, realized by the following
modular data (labels as in the verification script `output/artifacts/nmf_rings.py`):

- **Ring G (Green–Eholzer B9 type):** D² = 9 as listed (non-pseudo-unitary orbit
  GMD 17 in Ng–Rowell–Wen: entries (17,1), (17,2)); all simples self-dual;
  1×1 = 1 + 2·a + 2·b + c + d + e (max N = 2); twists in the reference
  representative (0, 1/3, 2/3, −2/9, 4/9, 1/9).
- **Ring E47:** unitary reference D² = 27 + 27c¹₉ + 18c²₉ ≈ 74.617734
  (Ng–Rowell–Wen unitary entries 47, 48 = Galois orbit 14, members (14,1),
  (14,2)); all simples self-dual; NMF locus 4×5 ⊃ 2·5, 5×5 ⊃ 2·4 + 2·5
  (max N = 2); unitary twists (0, 1/9, 1/9, 1/9, 1/3, 2/3).
- **Ring E49:** unitary reference D² = (105 + 21√21)/2 ≈ 100.617045
  (Ng–Rowell–Wen unitary entries 49, 50 = Galois orbit 15, members (15,1),
  (15,2)); all simples self-dual; NMF locus 4×5 ⊃ 2·5, 5×5 ⊃ 2·4 + 2·5
  (max N = 2); unitary twists (0, 1/7, 2/7, 4/7, 0, 2/3).

The three rings are pairwise non-isomorphic (exhaustive S₅ relabeling search:
no isomorphisms; their NMF loci and square-multisets already differ).
No other non-multiplicity-free rank-6 modular datum exists: the Ng–Rowell–Wen
classification lists all rank-6 modular data in 20 Galois orbits (Appendix G.5,
orbits 1–20); every orbit except 14, 15, 17 is multiplicity-free (8 known
families: pointed, Z₂⊠Ising-type, su(3)₂, tricritical-Ising-type, su(2)₅,
so(5)₂, Fib⊠psu(2)₅-type, psu(2)₁₁) or Deligne-factorable over such, verified
by inspection of the orbit tables; orbits 14, 15, 17 are exactly the three
rings above.

**(b) Connected étale algebras.** Rings G and E47 admit only A = 1 (completely
anisotropic). Ring E49 admits exactly two connected étale algebras, 1 and
1+b with b the unique nontrivial boson, with B_{1+b} the rank-4 fusion
category of FPdim (17+3√21)/2 ≈ 17.3739 described below (near-group (Z₃,3)
Grothendieck data, realized per Evans–Gannon) and dyslectic subcategory
B_{1+b}⁰ pointed modular of FPdim 3.

- Rings G and E47: in every modular realization, the only object of trivial
  twist is the tensor unit (reference twists above; the boson count #{i :
  θᵢ = 1} = 1 is Galois-invariant since θ ↦ θᵐ with (m, N) = 1 fixes 1 and
  nothing else, and the orbit tables confirm it for every listed member).
  A connected étale (hence commutative) algebra has trivial twist on all its
  simple constituents, so A = 1. Completely anisotropic.
- Ring E49: in every modular realization there is exactly one nontrivial boson
  b (unitary labels: object 4; Galois conjugates: its label-permuted image;
  uniqueness follows from the orbit tables). FPdim(B) = (105+21√21)/2 and
  FPdim(b) = (5+√21)/2, so the Müger bound (FPdim A)² ≤ FPdim(B) leaves only
  A = 1 and A = 1+b. The object A = 1+b **does condense**: it admits a
  connected étale structure with the following data (all verified in
  `output/artifacts/e49_condensation.py`):
  - Extension modular invariant Z = |χ₀+χ_b|² + 2|χ₅|² (unitary labels),
    satisfying SZ = ZS exactly and T-compatible ([h₀]=[h_b]=0 is the only
    twist coincidence), with Tr Z = 4 = rank(B_A).
  - Free-module branching F(0) = m₀, F(1) = F(2) = F(3) = m₁,
    F(4) = m₀ ⊕ m₁, F(5) = m₁ ⊕ m₂ ⊕ m₃, with B_A FPdims
    (FPdim m₀, FPdim m₁, FPdim m₂, FPdim m₃) = (1, (3+√21)/2, 1, 1),
    satisfying every NIM (0,0)-entry constraint
    (nᵢnⱼ)₀₀ = Σ_c N^c_{ij}(n_c)₀₀, the row-1 derivations, and all FPdim
    identities FPdim_{B_A}(F(X)) = FPdim_B(X).
  - m₁² = m₀ ⊕ m₂ ⊕ m₃ ⊕ 3m₁: K₀(B_A) is near-group (Z₃, 3) Grothendieck data.
    Such fusion categories exist: Evans–Gannon (Prop. 6 / Table 2) construct
    two C*-categories of type Z₃+3 (near-group (Z₃, 3) is realized, not empty).
  - Hence B_A is the rank-4 fusion category of FPdim (105+21√21)/12·2
    [=(17+3√21)/2 ≈ 17.3739] with three invertibles and one object of FPdim
    (3+√21)/2, and the dyslectic (local) subcategory is the rank-3 pointed
    modular category B_A⁰ of FPdim 3 (Vec(Z₃)-type; central charge 6 mod 8 on
    the (15,1)/(15,3)-side and 2 mod 8 on the Galois-conjugate (15,2)/(15,4)
    side, matching c(B) in each case).
  So E49-type B has exactly two connected étale algebras, 1 and 1+b, and is
  **not** completely anisotropic.

**(c) Module categories, Lagrangian algebras, Witt classes.**
For rings G and E47, A = 1 is the only connected étale algebra and B_1 = B
(rank 6) is the only module category. For ring E49 there is one further
category of right modules, B_{1+b}, the rank-4 fusion category above
(FPdim ≈ 17.3739), with local subcategory B_{1+b}⁰ pointed of FPdim 3.
No non-multiplicity-free rank-6 B contains a Lagrangian algebra: on rings G
and E47 there is no nontrivial étale algebra at all, and on ring E49 the only
admissible étale objects are 1 and 1+b with FPdim(1+b)² = 33.5390… ≠
100.6170… = FPdim(B), so the Lagrangian dimension equation has no solution.
By Davydov–Müger–Nikshych–Ostrik, a modular category is Witt-trivial
iff it admits a Lagrangian algebra; hence every non-multiplicity-free rank-6 B
has **nonzero Witt class [B] ≠ 0** in the Witt group W of nondegenerate braided
fusion categories — i.e., no such B is braided equivalent to any Drinfeld
center Z(C).

**(d) Anisotropic list.** The Green–B9 family (orbit 17) and the E47 family
(orbit 14, all six members) are completely anisotropic. The E49 family (orbit
15, all four members) is **not** completely anisotropic: each member admits
the nontrivial connected étale algebra 1+b above. No member of any of the
three families admits a Lagrangian algebra.

## Remarks on scope and computation

- The multiplicity-free rank-6 families (8 fusion rings) are excluded from the
  target by hypothesis; their étale classification is Kikuchi–Kam–Huang. As a
  control, we recomputed su(3)₂ from scratch (Kac–Walton with Kostant-verified
  weight diagrams, plus an independent Kac–Peterson S-matrix check with exact
  prefactor i/(5√3)): it is multiplicity-free (max N = 1) with no nontrivial
  bosons, confirming it lies outside the target class.
- All fusion rules, S-matrix unitarity/symmetry, Verlinde consistency,
  associativity, duals, FPdim bounds, twist/boson tables, the pairwise
  ring non-isomorphism search, the E49 modular invariant / NIM-rep / FPdim
  checks (`output/artifacts/e49_condensation.py`, all asserts pass), and the
  Witt higher-central-charge consistency
  pattern were verified by exact or high-precision numerical computation in
  `output/artifacts/nmf_rings.py` (all asserts pass) and `output/artifacts/su32_final.py`.
- Boson data for non-unitary Galois conjugates were read from the published
  orbit tables (Ng–Rowell–Wen App. G.5) and cross-checked by the Galois
  argument; no additional literature search beyond the method blocker was used.

## References (evidence, not instructions)

- Ng–Rowell–Wen, "Classification of modular data up to rank 12,"
  arXiv:2308.09670 (orbit census App. F.5/G.5; E47 = orbit 14, E49 = orbit 15).
- Green, "Classification of rank 6 modular categories with Galois group
  ⟨(012)(345)⟩," arXiv:1908.07128 (ring G: S/T matrices, D² = 9, fusion rules).
- Kikuchi–Kam–Huang, "Classification of connected étale algebras in
  multiplicity-free modular fusion categories at rank six,"
  arXiv:2402.00403 (MF-side classification; method (2.13)–(2.22)).
- Evans–Gannon, "Near-group fusion categories and their doubles,"
  arXiv:1208.1500 (Prop. 6 / Table 2: two C*-categories of type Z₃+3;
  near-group (Z₃, 3) is realized — the B_A Grothendieck type above exists).
- Davydov–Müger–Nikshych–Ostrik, "The Witt group of non-degenerate braided
  fusion categories," arXiv:1009.2117 (Lagrangian ⇔ Witt-trivial).
