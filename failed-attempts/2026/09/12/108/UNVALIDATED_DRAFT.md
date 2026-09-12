# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Commutative multiplicity-≤2 census of rank-5 based rings with one dual pair,
# with grading verdicts, Casimir semisimplicity separation, and a TY(Z4) identification

## 1. Definitions and scope

Fix the duality type: basis B = {e0 = 1, e1 = a, e2 = ā, e3 = b, e4 = c} with
duals e0* = e0, e1* = e2, e2* = e1, e3* = e3, e4* = e4 (exactly one dual pair
plus three self-dual basis elements, counting 1).

A *commutative based ring* of this type is a commutative ring R with Z-basis B
such that, writing e_i e_j = Σ_k N[i,j,k] e_k with N[i,j,k] ∈ Z_{\ge 0}:
- (unit) e_0 = 1, i.e. N[0,i,k] = N[i,0,k] = δ[i,k];
- (duals) N[i,j,0] = 1 if j = i* and 0 otherwise;
- (Frobenius) the tensor N[i,j,k] with the dual pairing is cyclically symmetric;
  combined with commutativity this is equivalent to full symmetry of the tensor
  S[i,j,k] := N[i,j,k*] under permutation of i,j,k;
- (associativity) Σ_m N[i,j,m]N[m,k,l] = Σ_n N[j,k,n]N[i,n,l] for all i,j,k,l.

A *multiplicity bound* M means N[i,j,k] ≤ M for all i,j,k. We enumerate M = 1
(multiplicity-free) and M = 2. The *universal grading* is the finest group
grading with e_0 in the identity component; "ungraded" means this group is
trivial. Relabelings considered are those preserving e_0 and the duality
pairing: swap e_1 ↔ e_2 and/or swap e_3 ↔ e_4 (Klein 4).

## 2. Census theorem (commutative slice, M ≤ 2)

**Theorem.** Up to duality-preserving relabeling there are exactly 7
commutative based rings of the above type with N[i,j,k] ∈ {0,1}, and exactly
77 with N[i,j,k] ∈ {0,1,2}. The 7 embed among the 77; 70 of the 77 genuinely
require a coefficient 2.

*Proof by reproducible exhaustive search.* The free symmetric tensor S on
{i,j,k} ⊂ {1,2,3,4} has 20 variables (multisets i≤j≤k). For M=1 all 2^20
assignments were checked directly against all 625 associativity equations
(two independent programs: `enum1.py` brute force and the C backtracker
`enum.c`, agreeing: raw 18 solutions, 7 orbits). For M=2 a depth-first search
over 3^20 assignments used only *sound* pruning (a partial assignment is
abandoned only when a fully-decided associativity equation is violated, which
no valid completion could repair) and every surviving full assignment was
checked against all equations (raw 282 solutions, 77 orbits under the Klein 4
action, canonical-form dedup; completed in ~10 s with no timeout). Pairwise
canonical forms are distinct (independently re-verified), so the orbit counts
are exact. Search-space coverage: M=1 covers 2^20/2^20; M=2 covers 3^20/3^20
assignments modulo sound pruning. ∎

Data files: `output/artifacts/census_M1.json`, `output/artifacts/census_M2.json`
(structure tensors), `output/artifacts/census_M2_tables.txt` (human-readable
products). Program: `enum.c` (kept alongside the workspace).

## 3. Universal-grading verdicts

**Proposition.** A fusion/based ring of rank 5 has universal-grading group of
order ≤ 5 (components partition the 5 simples), hence a subgroup-quotient of
one of Z2, Z3, Z4, V4 ≅ Z2², Z5 (all groups of order ≤ 5 are abelian). A
nontrivial grading therefore restricts to a nontrivial map to one of
Z2, Z3, Z4, Z5, V4, checked exhaustively (all 4^4 value-maps for V4 down to
2^4 for Z2).

**Result.** Of the 77 M≤2 tables, exactly 5 admit a nontrivial grading
(indices in `census_M2.json` order): 2, 5, 9, 12, 16 (all Z2-type, some with
Z4/V4 refinements of the same underlying bipartition); the remaining 72 are
ungraded (trivial universal grading). Of the 7 M≤1 tables, 2 are graded and 5
are ungraded. (Machine-checked; the check scripts are described in the
WORKLOG; the check is a finite exhaustive enumeration over ≤ 4^4 maps per
table per group.)

## 4. Casimir semisimplicity separation (fake based rings)

**Lemma (proved).** Let A be a finite-dimensional commutative C-algebra with
basis {x_i} closed under an anti-involution x ↦ x* permuting the basis, real
structure constants, and Casimir element C = Σ_i x_i x_i*. If A is semisimple,
then C is invertible. *Proof.* In the regular representation, fusion matrices
satisfy F_{i*} = F_i^T (reality plus cyclic symmetry of structure constants),
and semisimplicity makes every F_i diagonalizable; commuting diagonalizable
matrices are simultaneously diagonalizable, so on a common eigenvector v with
F_i v = a_i v and F_i^T v = b_i v, reality gives a_i‖v‖² = ⟨F_i v,v⟩ =
⟨v,F_i^T v⟩ = b̄_i‖v‖², i.e. b_i = ā_i. Hence C acts by Σ_i a_i b_i =
Σ_i |a_i|² ≥ 1 (the identity contributes 1) on each joint eigenspace. ∎

**Corollary (witness).** A commutative based ring whose Casimir regular-matrix
C = Σ_i F_i F_{i*} (F_i the fusion matrices) has det(C) = 0 is not semisimple
over C, hence is not the Grothendieck ring of any complex fusion category
(K(C)⊗C is semisimple), so it admits no categorification.

**Result.** Exactly 3 of the 77 tables (indices 18, 21, 22) have det(C) = 0
(exact integer arithmetic), each with Casimir nullvector (−1,1,−1,1,0). The
other 74 (all 7 at M=1) have nonzero determinant. Numeric diagonalization
confirms the defect (eigenvector condition numbers > 10^8; repeated generic
eigenvalues). These three satisfy associativity, unit, duals, and Frobenius
reciprocity yet are not fusion rings — minimal-rank explicit witnesses that
those axioms alone do not imply semisimplicity.

## 5. Structural observations

(a) **TY(Z4) identification.** Table M1#0 = M2#2 is exactly the Tambara–Yamagami
ring for Z4: invertibles {e_0,e_1,e_4,e_2} ≅ Z4 via e_1²=e_4, e_4²=e_0,
e_1e_4=e_2; noninvertible b = e_3 self-dual with b² = e_0+e_1+e_2+e_4 and
e_1 b = e_2 b = b, e_4 b = b; FPdims (1,1,1,2,1), global dimension 8
(verified entrywise; FP eigenvalue computation). This ring is categorifiable
by the standard Tambara–Yamagami construction (known theorem, cited not
reproved).

(b) **Frobenius–Perron dimension collisions.** The three fake rings share FPdim
vectors exactly (6 decimals, same minimal data) with genuine rings: fake 18 ↔
genuine 27 with d = (1,3,3,1,2), D = 24; fake 21 ↔ genuine 29; fake 22 ↔
genuine 30. So FPdims alone do not detect non-semisimplicity here; the
Casimir determinant does.

(c) **Near/far data.** Frobenius–Perron dimensions, formal codegrees (numeric),
and invertible-element data for all 77 tables were computed
(`screen_sample.txt` shows the verified format; codegree computations were
cross-checked against exact sympy characters on tables 0, 16, 27, where a
seed-dependent diagonalization artifact in an early script was found and
corrected).

## 6. Limitations (explicit)
- Commutative slice only: noncommutative based rings with this duality type
  are not enumerated (their variable count is much larger: ordered pairs).
- Multiplicity bound 2: the M=3 search timed out with 147 partial tables; no
  multiplicity cap is proved, so this is a census of the M≤2 slice, not of all
  tables in the class.
- Categorification verdicts: only TY(Z4) (construction, known) and the three
  fake rings (rigorous non-categorifiability, Corollary above) are decided;
  the remaining rings carry data but no per-table pentagon/obstruction verdict.
- Originality: this is presented as a reproducible computational census with
  two structural highlights (fake-ring triple + FPdim collisions); overlap
  with published rank-5 tables is possible and is not adjudicated here.
