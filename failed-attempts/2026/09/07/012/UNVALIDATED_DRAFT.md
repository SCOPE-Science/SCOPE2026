# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Doubly-sorted BH(6,3) with fixed third row [1,ω,1,ω²,ω,ω²]: certified completion by exact cyclotomic backtracking

## 1. Statement of result (proved) vs computed certificates vs conjecture

**Proved (hand + machine-checked exact integer arithmetic, no floating point).**
Let ω = exp(2πi/3), so 1+ω+ω² = 0, ω³ = 1, ω̄ = ω², ω̄² = ω.
Let dephased mean first row and column are all 1.
Define
- R1 = [1,1,1,1,1,1],
- R2 = [1,1,ω,ω,ω²,ω²],
- C2 = [1,1,ω,ω,ω²,ω²]ᵀ,
- R3* = [1,ω,1,ω²,ω,ω²].

Then:
(a) R3* is exactly orthogonal to R1 and R2 (Section 3).
(b) **Existence + uniqueness in slice.** There exists a dephased Butson matrix
H ∈ BH(6,3) (entries in {1,ω,ω²}, HH̄ᵀ = 6I) with second row R2, second column C2
and third row R3*. Up to swapping the last two rows (which preserves C2 since
both have second entry ω²), the completion is unique. Explicitly, with
exponents mod 3 (entry = ω^e), the default completion is

| row | exponents | entries |
|---|---|---|
| R1 | 0 0 0 0 0 0 | 1 1 1 1 1 1 |
| R2 | 0 0 1 1 2 2 | 1 1 ω ω ω² ω² |
| R3* | 0 1 0 2 1 2 | 1 ω 1 ω² ω ω² |
| R4 | 0 1 2 0 2 1 | 1 ω ω² 1 ω² ω |
| R5 | 0 2 1 2 0 1 | 1 ω² ω ω² 1 ω |
| R6 | 0 2 2 1 1 0 | 1 ω² ω² ω ω 1 |

The matrix is symmetric (rows equal columns as sequences) with all diagonal
entries 1. Swapping R5 ↔ R6 gives the second ordered completion; no others exist.
(c) The 6×6 Gram matrix over Z[ω] is exactly 6I (verifier certificate).
(d) The R4-catalog lemma: among 12 vectors [1,ω,…] with row-sum zero, exactly one
(R4 above) is orthogonal to R1,R2,R3*; among 12 vectors [1,ω²,…], exactly two
(A,B above) are orthogonal to R1,R2,R3*,R4, and A ⊥ B.
(e) Canonical 2-border lemma (Section 2): any dephased BH(6,3) can be brought to
R2/C2 form by a column permutation fixing column 1 then a row permutation fixing
rows 1–2; both preserve dephasing and the BH property.

**Computed certificates (exact, reproducible in seconds).**
- Exhaustive backtracking log: pools 12/12/12, depth-4 12→1, depth-5 12→2,
  depth-6 24→2 ordered solutions; 48 inner checks; timing ~10⁻⁴ s.
- Defect d(H) = 0 (isolated): 30×36 integer linearized-unitarity matrix has rank 25,
  nullity 11 = 2·6−1. Dephased 25-variable nullity 0. Fourier F6 reference computed
  by the same code has defect 4. Exact Fractions arithmetic.
- Haagerup set Λ(H) = {1,ω,ω²}, size 3, counts (576,360,360)/1296. Fourier F6
  Λ = all six 6th roots, size 6. Λ is invariant under monomial equivalence, so H is
  inequivalent to every member of the Fourier family.

**Conjecture / uncertainty (clearly separated, not claimed as proved here).**
- The matrix is of Tao type. Its alphabet, defect 0 and Λ = μ₃ match the isolated
  Tao/S6 example, and the published catalog (Tadej–Życzkowski) lists a single
  BH(6,3) equivalence class. We did **not** machine-check an explicit monomial map
  (row/column permutations plus μ₃ phases) to a frozen published Tao array in this
  pass (no network to fetch a canonical array), so formal monomial equivalence to a
  specific published S6 array is stated as catalog-supported identification, not as a
  machine-checked certificate. Inequivalence to Fourier is proved (above).

## 2. Preliminaries and canonical-border lemma

Work in the Eisenstein integers Z[ω] = {a+bω : a,b ∈ Z}, ω² = −1−ω.
Represent (a,b) = a+bω. Then
- addition componentwise;
- (a1+b1ω)(a2+b2ω) = (a1a2−b1b2) + (a1b2+a2b1−b1b2)ω (using ω²=−1−ω);
- conjugation: 1̄=1, ω̄=ω²=−1−ω, so conj(a+bω) = (a−b)−bω;
- 1=(1,0), ω=(0,1), ω²=(−1,−1). All exact over Z.

**Count lemma.** Let u,v ∈ μ₃⁶, μ₃={1,ω,ω²}. Write ratio exponents
eᵢ ∈ Z₃ with uᵢv̄ᵢ = ω^{eᵢ}, eᵢ = (exp(uᵢ)−exp(vᵢ)) mod 3.
Then ⟨u,v⟩ = Σ uᵢv̄ᵢ = n₀·1+n₁·ω+n₂·ω² with nⱼ = #{i:eᵢ=j}, n₀+n₁+n₂=6.
Since n₀+n₁ω+n₂ω² = (n₀−n₂)+(n₁−n₂)ω and {1,ω} is Z-free (minimal polynomial
x²+x+1), the sum is 0 iff n₀=n₁=n₂=2. In particular a row is orthogonal to the
all-ones row iff its entries contain two 1's, two ω's, two ω²'s (row-sum zero).

*Proof of freeness:* if a+bω=0 with a,b∈Q then taking norms or solving
ω=(−1±√−3)/2 gives a=b=0. ∎

**Canonical-border lemma.** Let H be dephased BH(6,3). Then there are a column
permutation π fixing column 1 and a row permutation σ fixing rows 1,2 such that
σ(π(H)) has second row R2 and second column C2.

*Proof.* By the count lemma each row has pattern (2,2,2). Row 2 starts with 1
(dephased), so its tail has one 1, two ω, two ω². Permuting columns 2..6 groups
them as [1,1,ω,ω,ω²,ω²] = R2. This fixes column 1 so column 1 stays all-1; row 1
(still all-1) is unchanged; BH property (pairwise row ratios (2,2,2)) is invariant
under column permutation. Column 2 vs column 1 (all-1) has pattern (2,2,2) by the
same lemma applied to columns (columns of a Hadamard are also orthogonal: see
remark). Its top entries are R1C2=1, R2C2=1, so rows 3..6 of column 2 are
{ω,ω,ω²,ω²}. Permuting rows 3..6 (fixing rows 1,2) sorts them to [ω,ω,ω²,ω²],
giving C2. Row permutation preserves row-orthogonality and dephasing. ∎

*Remark (rows suffice).* If H has unimodular entries and HH̄ᵀ=6I then
(1/√6)H is unitary, so H̄ᵀH=6I automatically. Hence checking row Gram suffices;
the verifier also checks columns directly.

*Explicit permutation search.* Given any matrix: dephase (row i × ω^{−H[i][0]},
column j × ω^{−H[0][j]}), sort columns 2..6 by row-2 key, sort rows 3..6 by
column-2 key. `artifacts/canonical_border.py` does this and was tested on 5 random
monomial transforms (random row/column permutations plus row/column μ₃ phases) of
the solution: all return to R2/C2 with BH property preserved.

## 3. Hand verification of the R3* border

Encode 1/ω/ω² as 0/1/2. R1=(0,0,0,0,0,0), R2=(0,0,1,1,2,2), R3*=(0,1,0,2,1,2).

⟨R1,R3*⟩: ratios e = R1−R3* = (0,2,0,1,2,1), i.e. entries
(1,ω²,1,ω,ω²,ω) = 2·(1+ω+ω²) = 0. Counts (2,2,2). ✓
⟨R2,R3*⟩: e = (0,2,1,2,1,0), i.e. (1,ω²,ω,ω²,ω,1) = 2·(1+ω+ω²) = 0. ✓
Row-sum of R3*: exponents {0×2,1×2,2×2}, sum 2(1+ω+ω²)=0 ✓ (orthogonal to R1).
Column-2 check: R3*[1]=1=ω matches C2 row 3 = ω ✓. First column 1 ✓.

No textbook divisibility rules this out: n=6 is divisible by 3 so the necessary
n₀=n₁=n₂ condition is satisfiable; the slice is not covered by the trivial
H(7,3)=∅ argument. Completability is genuinely open before search.

## 4. Exhaustive enumeration (exact, 48 checks)

Fix col1=1 everywhere and col2 per C2: R4 starts [1,ω], R5,R6 start [1,ω²].
Row-sum zero forces exact remaining counts, giving pools (pure product+filter):
- C4 ([0,1,…]): need one more 0, one more 1, two 2's in last 4 places: 4!/(1!1!2!)=12.
- C5, C6 ([0,2,…]): 12 each by the same count.
Orthogonality is tested by exact ratio counts (Section 2), equivalently exact
Z[ω] sums. No floats anywhere.

Search tree (`artifacts/search.py`, log `artifacts/search_log.json`):
- Depth 4: scan 12 R4 candidates; exactly 1 passes vs R1,R2,R3*:
  R4=(0,1,2,0,2,1), with vsR2 counts (2,2,2) (ratios (0,1,1,2,0,2)) and
  vsR3 counts (2,2,2) (ratios (0,0,2,1,1,2)).
- Depth 5: given that R4, scan 12 R5 candidates; exactly 2 pass vs R1,R2,R3*,R4:
  A=(0,2,1,2,0,1), B=(0,2,2,1,1,0).
- Depth 6: for each of the 2 R5 branches scan 12 R6 candidates (24 checks);
  exactly 2 ordered triples pass, because A⊥B (ratios (0,0,2,1,2,1), counts
  (2,2,2)) while A⊄A, B⊄B (self-ratios (0,0,0,0,0,0)). So R5,R6 must be {A,B}
  in either order.
- Totals: 12+12+24=48 inner checks, ~10⁻⁴ s (far below the 10⁶-node budget).
  Column partial-inner-product pruning is redundant here (Section 2 remark) and
  the verifier confirms all column pairs are orthogonal a posteriori.

Hence exactly 2 ordered completions (1 unordered pair under R5↔R6, which fixes C2
because both rows have col2=ω²). Existence is proved; the gap alternative is
refuted for this slice. The fallback R4-catalog is the depth-4 statement above.

## 5. Independent Gram verification (Eisenstein integers)

`artifacts/verify.py` re-encodes exponents via 1=(1,0), ω=(0,1), ω²=(−1,−1),
multiplies with (a1a2−b1b2, a1b2+a2b1−b1b2), conjugates with (a−b,−b), and forms
G=H·conj(Hᵀ) and the column Gram. It also asserts alphabet ⊂ μ₃, dephasing,
R2/C2/R3* border, and row counts (2,2,2). Output:

- alphabet, dephasing, border, counts: PASS;
- row Gram = 6I, column Gram = 6I (all diagonal (6,0), off-diagonal (0,0)): PASS.

## 6. Defect and Haagerup invariants; (in)equivalence

**Defect.** For H with |H|≡1, curves H(t)=H∘exp(iRt) preserve unitarity to first
order iff for all i<j: Σₖ H_{ik}H̄_{jk}(R_{ik}−R_{jk})=0 with R real.
With cₖ=H_{ik}H̄_{jk} ∈ μ₃ (exp eₖ): Re(cₖ)∈{1,−1/2}, Im(cₖ)∈{0,±√3/2}.
Multiplying by 2 and 2/√3 gives integer equations
Σ rₖ(R_{ik}−R_{jk})=0 (r=2 if e=0 else −1) and Σ sₖ(…)=0 (s=0/+1/−1).
For n=6 this is a 30×36 integer matrix M. d(H)=dim ker(M)−(2n−1); the dephased
defect (first row/column of R fixed to 0, 25 variables) equals d(H).
Rank is computed by exact Fraction Gaussian elimination (no floats, no sympy
needed). Results (`artifacts/defect_haagerup.py`, `defect_lambda.json`):

| matrix | rank | null | defect | dephased null |
|---|---|---|---|---|
| bordered solution H | 25 | 11 | **0** | 0 |
| Fourier F6 (ref) | 21 | 15 | **4** | 4 |

F6 (entries ζ^{jk}, ζ=exp(πi/3)) uses 2Re∈{±2,±1}, Im/(√3/2)∈{0,±1}, same integer
method. The value 4 matches the literature (F6 defect 4); 0 means H is isolated.

**Haagerup set.** Λ(H)={H_{ij}H_{kl}H̄_{il}H̄_{kj}} (i,j,k,l ∈ [6]).
For μ₃ alphabet this is ω^{(e_{ij}+e_{kl}−e_{il}−e_{kj}) mod 3} ⊆ μ₃.
Enumeration of all 6⁴=1296 quadruples (exact mod-3):
Λ(H)={1,ω,ω²}, size 3, frequencies {1:576, ω:360, ω²:360}.
For F6 (mod 6): all six 6th roots, size 6, frequencies {0:540,1:72,2:216,3:180,4:216,5:72}.
Λ is invariant under row/column permutations and row/column phase multiplications
(phases cancel in the 4-term product), hence under Hadamard (monomial) equivalence.
Different sizes (3 vs 6) prove H is inequivalent to F6 and to its orbit.

*Tao identification (honest scope).* Alphabet μ₃ forces Λ⊆μ₃; defect 0 matches the
isolated Tao/S6 profile (Fourier has defect 4). The Tadej–Życzkowski catalog lists
BH(6,3) as a single monomial class (Tao). Our H is therefore catalog-consistent
with Tao type. An explicit machine-checked monomial map to a frozen published S6
array was not performed (offline pass) and is not claimed.

## 7. Reproducibility

All in `output/artifacts/`, pure Python 3 stdlib only, seconds on a laptop:

- `bordered_matrix.json` — bordered matrix + completions (exponents).
- `search.py` → `search_log.json` — exhaustive log (pools, node counts, solutions, timing).
- `verify.py` — Eisenstein Gram/dephasing/alphabet/border certificate.
- `defect_haagerup.py` → `defect_lambda.json` — defect/Haagerup table + Fourier reference.
- `canonical_border.py` — constructive 2-border demo (5 random trials).

Commands: `python3 artifacts/search.py`, `python3 artifacts/verify.py`,
`python3 artifacts/defect_haagerup.py`, `python3 artifacts/canonical_border.py`
(all exit 0; total < 1 min).

## 8. Limitations and what is not claimed

- Uniqueness is within the fixed R3* slice (up to R5↔R6), not a new global
  classification of BH(6,3); global single-class status is cited, not re-proved.
- Explicit monomial equivalence to a specific published Tao array is not
  machine-checked here (invariant match + catalog citation only).
- Defect convention is stated explicitly (ker minus 2n−1); readers using the
  un-shifted convention should add 11.
- NoOriginality overclaim: the matrix coincides (up to the bordered gauge) with the
  known Tao-type example; the contribution is the first certified
  completion-or-gap verdict for this doubly-sorted R3* slice with exact logs and
  defect/Haagerup certificates, not a new inequivalent Hadamard.

## 9. References (nearest known, for comparison)

- Tadej–Życzkowski, quant-ph/0607136: order-6 catalog incl. Tao/S6, Fourier F6,
  defect/equivalence notions. Does not decide this R3* slice.
- Bengtsson et al., quant-ph/0610161: Hadamards and MUB-6. No bordered BH(6,3)
  enumeration or Haagerup/defect data for fixed R3* prefixes.
- Szöllősi/Karlsson parametric order-6 families (0811.3936): continuous families
  transverse to the Butson locus (positive defect); our μ₃, defect-0 object is
  orthogonal to those, distinguished by alphabet and Λ.
