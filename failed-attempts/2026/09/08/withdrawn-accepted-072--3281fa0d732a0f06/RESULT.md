# Exact restriction branching census S_{mn} ↓ S_m × S_n for all factor pairs with mn ≤ 12

## Context

For the product action of S_m × S_n on [m] × [n], there is an embedding
S_m × S_n → S_{mn}. C. Ryba (arXiv:2112.01456) showed the Kronecker
comultiplication Δ* on the stable-character basis tilde-s has structure
constants R^λ_{μ,ν} equal to S_{mn}-to-S_m × S_n restriction
multiplicities in the stable regime (m, n sufficiently large relative to
λ), and proved a two-row stability theorem. I. Entova-Aizenbud
(arXiv:1407.1506) placed reduced Kronecker coefficients as structure
constants of Deligne Rep(S_t). No explicit small-(m,n) branching tables
with certificates were recorded in that theory.

## Definitions

- Partitions α ⊢ m, β ⊢ n, λ ⊢ mn index irreducibles χ^α, χ^β, χ^λ.
- `mult(α,β;λ)` = multiplicity of χ^α ⊗ χ^β in Res^{S_{mn}}_{S_m × S_n}(χ^λ)
  for the product action.
- For g ∈ S_m of cycle type μ and h ∈ S_n of type ν, the product-action
  cycle type ρ(μ,ν) ⊢ mn is: each part-pair (a,b) contributes gcd(a,b)
  cycles of length lcm(a,b).
- Class-algebra formula (definitionally):
  mult(α,β;λ) = (m!n!)^{-1} Σ_{μ⊢m,ν⊢n} |C_μ||C_ν|
  χ^λ(ρ(μ,ν)) χ^α(μ) χ^β(ν).

## Result

**Theorem (exact census, machine-checked).** For every (m,n) in
{(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4)}, all values mult(α,β;λ) are
as recorded in `output/artifacts/restriction_tables.json` (4013 entries
total). Per-pair statistics:

| pair | N | entries | nonzero | density | max mult | example attaining triple (α,β;λ) |
|------|---|---------|---------|---------|----------|----------------------------------|
| (2,2) | 4 | 20 | 9 | 45.0% | 2 | ([2],[2];[2,2]) |
| (2,3) | 6 | 66 | 38 | 57.6% | 3 | ([2],[2,1];[3,2,1]) |
| (2,4) | 8 | 220 | 145 | 65.9% | 8 | ([2],[2,1,1];[4,2,1,1]) |
| (2,5) | 10 | 588 | 440 | 74.8% | 19 | ([2],[3,1,1];[4,3,2,1]) |
| (2,6) | 12 | 1694 | 1351 | 79.8% | 86 | ([2],[3,2,1];[5,3,2,1,1]) |
| (3,3) | 9 | 270 | 228 | 84.4% | 24 | ([2,1],[2,1];[4,3,1,1]) |
| (3,4) | 12 | 1155 | 1067 | 92.4% | 320 | ([2,1],[3,1];[5,3,2,1,1]) |

Entry counts equal p(m)·p(n)·p(mn) (p = partition number).
Example attaining triples are valid locations of the global maximum;
several pairs have a second attaining location (transpose/sign partner),
so uniqueness of location is not claimed.

**Two-row rows (exact data).** For the (2,k) chain with α=[2], β=[k]
(trivial), λ=[2k−j,j] over two-row partitions of 2k:

- k=2: [1,0,2] over ([4],[3,1],[2,2])
- k=3: [1,0,2,0] over ([6],[5,1],[4,2],[3,3])
- k=4: [1,0,2,0,3] over ([8],[7,1],[6,2],[5,3],[4,4])
- k=5: [1,0,2,0,3,0] over ([10],[9,1],[8,2],[7,3],[6,4],[5,5])
- k=6: [1,0,2,0,3,0,4] over ([12],[11,1],[10,2],[9,3],[8,4],[7,5],[6,6])

Companion rows for β=[k−1,1] (with [1,1] for k=2): [0,1,0] (k=2),
[0,1,2,0] (k=3), [0,1,2,2,1] (k=4), [0,1,2,2,4,0] (k=5),
[0,1,2,2,4,3,2] (k=6). These are exact small-(m,n) data illustrating
the Ryba two-row stability phenomenon, not a new general bound.

**Small-(m,n) witness.** mult([2],[2];[2,2]) = 2 at (2,2): the
2-dimensional S_4-irreducible [2,2] restricts to S_2 × S_2 containing
the trivial representation twice (class sum 8 / |S_2×S_2|=4).
The word "exceptional" is interpretive framing of this proved exact
multiplicity, not a theorem.

**Global maximum certificate.** mult([2,1],[3,1];[5,3,2,1,1]) = 320 at
(3,4), via an explicit 15-summand class-algebra sum totalling 46080
divided by 3!·4! = 144 (archived in `cert_max_3x4.json`).

## Proof / evidence

From-scratch Murnaghan–Nakayama character tables for S_n (n ≤ 12),
product-action cycle type ρ(μ,ν) above, and the class-algebra inner
product. The independent audit re-verified with a distinct beta-number
Murnaghan–Nakayama implementation:

- 4013/4013 stored entries match exact recomputation (full-table check
  for (2,2),(2,3),(2,4),(3,3); exhaustive beta-number recomputation for
  all 7 pairs including (2,5),(2,6),(3,4)).
- Murnaghan–Nakayama row orthogonality for n ∈ {2,3,4,5,6,8,9,10,12}: OK.
- Per-λ dimension identity dim(λ)=Σ_{α,β} mult·dim(α)·dim(β): OK for
  every λ in all 7 pairs; hook-length vs identity-character agreement: OK.
- Frobenius form Σ_λ mult(α,β;λ)dim(λ)=[G:H]·dim(α)dim(β): OK for every
  (α,β), all pairs.
- Trivial column mult(triv,triv;[N])=1, 0 otherwise: OK all pairs.
- Every entry integral (exact divisibility) and nonnegative.
- Two class-sum certificates recomputed term-by-term: OK.

## Limitations

- No new general stability theorem is proved; two-row rows are exact
  data in the unstable (small m,n) regime, outside Ryba's
  m,n ≥ 2|λ| stability hypothesis, so they do not follow mechanically
  from the general theorem and are not re-proofs of it.
- The census covers only the 7 factor pairs with mn ≤ 12; no claim
  beyond this window.
- "Exceptional / against naive analogy" language is framing, not a
  mathematical classification.
- Location lists for global maxima give one valid attaining triple per
  pair; some pairs admit a second attaining triple (e.g. (3,4) also at
  ([2,1],[2,1,1];[5,3,2,1,1])); values themselves are the certified maxima.
- Replay scripts use hard-coded `output/artifacts/...` paths; rerunning
  requires the same working-tree layout or path edits.

## Reproducibility

```
python3 output/artifacts/compute_restriction.py   # rebuilds restriction_tables.json + summary.json
python3 output/artifacts/analyze.py               # induced-dim, trivial-column, two-row census
python3 output/artifacts/verify.py                # orthogonality + certificates (requires output/artifacts/ layout)
```

Computation is stdlib-only small-integer arithmetic from S_n character
tables (n ≤ 12); largest table (2,6) has 1694 rows.

## References

- C. Ryba, Kronecker Comultiplication of Stable Characters and
  Restriction From S_{mn} to S_m × S_n, arXiv:2112.01456.
  https://arxiv.org/abs/2112.01456 (full HTML: https://arxiv.org/html/2112.01456v1)
- I. Entova-Aizenbud, Deligne categories and reduced Kronecker
  coefficients, arXiv:1407.1506. https://arxiv.org/abs/1407.1506
