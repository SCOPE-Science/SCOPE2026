# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Symmetric 2-(81,16,3) designs: polarity obstructions and difference-set nonexistence in five groups of order 81

## 1. Setting and results

Let a symmetric 2-(81,16,3) design have v = 81 points, block size k = 16, and
each pair of points in exactly lambda = 3 blocks. Then r = 16, n = k - lambda = 13,
and the Bruck–Ryser–Chowla equation z^2 = 13x^2 + 3y^2 is solvable (4,1,1), so BRC
does not obstruct. Existence of any such design is open; a regular automorphism
group G of order 81 is equivalent to an (81,16,3) difference set D in G,
DD^{(-1)} = 13·1 + 3G.

We prove the following (proofs in Sections 2–4; machine parts reproducible per Section 5):

**Theorem A (abelian regular group + polarity impossible).**
No symmetric 2-(81,16,3) design with a regular abelian group of order 81 admits a
polarity. Equivalently, no (81,16,3) difference set in an abelian group of order 81
is reversible up to translation (D^{(-1)} = Dg), which by the Kantor/Jungnickel
correspondence (polarities of abelian developments = reversible difference sets;
Kantor 1969; Beth–Jungnickel–Lenz) is necessary for a polarity.

**Theorem B (difference-set nonexistence, exact computation).**
No (81,16,3) difference set exists in any of the following groups of order 81:
(i) C3^4; (ii) Heisenberg(27) × C3; (iii) (C9 ⋊ C3) × C3 with action a ↦ 4a;
(iv) C27 ⋊ C3 with action x ↦ x^10; (v) C9 ⋊ C9 with action (a,b) ↦ a + 4^b a′.
In particular no symmetric 2-(81,16,3) design admits a regular action of any of
these groups — nonabelian (ii) and (iii) included — with or without polarity.

**Proposition C (polarity numerics).** Any polarity of any symmetric 2-(81,16,3)
design has exactly 16 absolute points; moreover no polarity normalizes a regular
group of order 81 (the absolute set would be a union of 81-orbits yet have size 16).

## 2. Character constraints and the reversibility obstruction (Theorem A)

Let G be abelian of order 81 and D a putative (81,16,3) difference set. For every
nonprincipal linear character chi, chi(D)·conj(chi(D)) = 13, since chi kills the
3G term. For characters of order 3, writing (a0,a1,a2) for the fiber sizes over
ker(chi), chi(D) = a0 + a1·w + a2·w² with w = e^{2pi·i/3}, so
|a0+a1·w+a2·w²|² = a0²+a1²+a2²−a0a1−a1a2−a2a0 = 13 with a0+a1+a2 = 16. Hence
(a0−a1)²+(a1−a2)²+(a2−a0)² = 26. With signed differences p+q+r = 0, p²+q²+r² = 26,
the only offset pattern compatible with sum 16 is (0,3,4) with base 3 (the other,
(0,1,4), gives base 11/3, non-integral). **Every admissible fiber triple is a
permutation of (3,6,7); in particular all three entries are distinct**
(artifact `fiber_triple_proof.py` certifies this by exhaustive enumeration).

If D is reversible up to translation, D^{(-1)} = Dg, then on the fibers over any
order-3 character, with g in coset c, fiber counts satisfy aⱼ = a_{c−j} for all j:
c = 0 forces a1 = a2; c = 1 forces a0 = a1; c = 2 forces a0 = a2. In every case two
entries coincide — impossible for a permutation of (3,6,7). Hence no reversible
(81,16,3) difference set exists in any abelian group of order 81.

*Second proof.* In a 3-group, squaring is an automorphism, so D^{(-1)} = Dg implies
a symmetric translate E = E^{(-1)} exists. Then chi(E) is real with chi(E)² = 13,
i.e. chi(E) = ±√13, but character values lie in Q(zeta_9), whose unique quadratic
subfield is Q(√−3) (discriminant −3 ≠ 13), which does not contain √13. Contradiction.

## 3. Quotient-profile reduction and exact enumeration

Let G have a central subgroup S of order 3 with abelian quotient Q = G/S of order 27
(exists for all five groups above; verified explicitly). Projecting
DD^{(-1)} = 13·1 + 3G gives pi(D)pi(D)^{(−1)} = 13·1 + 9Q. With fiber sizes
m : Q → {0,1,2,3} (fiber has 3 points), this forces:
(P1) sum m = 16, sumsq m = 22 (shapes: ten 1s + three 2s, or thirteen 1s + one 3);
(P3) all 26 nontrivial autocorrelations equal 9 (since 16² − 22 = 234 = 26·9);
(P2) every order-3-character fiber triple is a permutation of (3,6,7) — for
Q = C3³, all 13 plane-coset triples; for Q = C9×C3, the 4 order-9-subgroup triples.

Exact backtracking enumeration in C (incremental triple feasibility + sum/sumsq bounds):
- Q = C3³: 29,971,377 nodes, 3,744 profiles pass P1+P2, and all 3,744 also satisfy P3
  (6 s; `qprofiles.txt`). They form 3 orbits under GL(3,3) (`qprofile_reps.txt`).
- Q = C9×C3: 1,063,299,948 nodes; 5,202,144 pass P1+P2 but **zero** satisfy P3 (~67 s;
  `qprofiles_c9c3.txt`). Hence groups (iv) and (v) admit no quotient profile at all.

## 4. Exhaustive fiber lifting (Theorem B)

For Q = C3³, each profile lifts by choosing m[q] of 3 points per fiber:
∏_q C(3,m[q]) = 1,594,323 combinations per representative. Direct odometer
enumeration (`liftdirect.c`) tests the full equation DD^{−1} = 13·1 + 3G exactly:
0 lifts in C3^4 arithmetic for all 3 reps. The nonabelian adaptation
(`nonab_liftdirect.c`, verified group tables: identity, inverses, 3000-triple
associativity cross-check in `verify_nonab.py`) gives 0 lifts in groups (ii) and
(iii) for all 3 reps (6 × 1,594,323 exact tests). For (iv), (v) there is nothing to
lift (Section 3). This proves Theorem B. The lifting searches ran to completion
(node-cap set to 2^63−1; reported NODES counts confirm full exhaustion, and the
direct odometer enumerates exactly the stated product space).

## 5. Reproducibility

All programs are in C (gcc −O2) or Python 3 stdlib only; full command log in
`output/artifacts/RUNLOG.md`. Independent Python re-verification of P1/P2/P3 on all
reps: `output/artifacts/verify_quotient_layer.py` (ALL CHECKS PASSED). Positive
controls: the same search/test machinery finds/accepts the classical (16,6,2)
Hadamard difference set, excluding tooling false negatives. `scope_literature_search`
for an originality check was unavailable at submission time (service key error);
originality is therefore NOT claimed — the finding is reported as a proved structural
result with explicit scope, and any overlap with the (81,16,3) literature should be
checked at audit.

## 6. Scope and limitations

- The complete target (polarity + regular nonabelian action, all nonabelian groups)
  is NOT fully closed: nonabelian groups of order 81 whose order-27 quotients are all
  nonabelian (maximal-class / class-3 groups) are outside this pipeline and remain open;
  the general existence of any symmetric 2-(81,16,3) design remains open.
- Theorem A uses the standard Kantor/Jungnickel polarity–reversibility correspondence
  for abelian developments (cited, not re-proved).
- What IS closed: (a) abelian-regular + polarity is impossible (Theorem A, pure proof);
  (b) difference sets — hence regular actions, polar or not — do not exist in the five
  listed groups including two nonabelian ones (Theorem B, exact computation);
  (c) polarity numerics (Proposition C, spectral proof).
- Conjectures vs proof: the SA energy floors (32 abelian, 28 nonabelian) and the-guided
  search failures are reported as heuristics only and carry no probative weight; all
  claimed nonexistence rests on the exhaustive enumerations above.
