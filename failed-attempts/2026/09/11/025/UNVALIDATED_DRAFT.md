# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Inclusion-maximality of the four documented 57-line angle-1/5 systems in R^18

## Claim

Let F1, F2, F3, F4 be the four 18x57 integer matrices of Greaves–Syatriadi–Yatsyna
(arXiv:2104.04330, Figs. 1–4), each column of squared norm 10, spanning 57
equiangular lines in R^18 at angle arccos(1/5). For each of the four systems, there
is **no real unit vector** u in R^18 with all 57 inner products in {+1/5, -1/5}.
In particular none of F1..F4 extends to a 58-line angle-1/5 system — not just by
integer-lattice vectors, but by any real vector.

Exact counts from the complete enumeration (Section 3):

| parent | basis det | unit-norm sign patterns | full 58-extensions |
|--------|-----------|------------------------|--------------------|
| F1 | 1572864 | 304 | 0 |
| F2 | -786432 | 174 | 0 |
| F3 | 786432 | 224 | 0 |
| F4 | 1572864 | 154 | 0 |

## Method (exact integer arithmetic, no floats in the certificate)

Fix 18 linearly independent columns as basis B (det B != 0 verified exactly).
Write c = sqrt(2/5). A candidate 58th unit vector u must satisfy B^T u = t with
t = c·s for a sign vector s in {+1,-1}^18 (2^18 = 262144 patterns).

- **Norm condition.** ||u||^2 = c^2 s^T (BB^T)^{-1} s = 1. With M = BB^T this is
  the integer equation 2·s^T adj(M)·s = 5·det(M).
- **Extension condition.** For each non-basis column f, |f·u| = c becomes the
  integer equation |s^T adj(B) f| = |det B|.

Every pattern is tested in exact (arbitrary-precision) integer arithmetic.
Floats are used nowhere in the verdict; an independent float prefilter was
cross-checked against the integer counts during development (a transpose bug was
caught and fixed this way; see WORKLOG).

Fixed bases used: F1 [35..51,54]; F2 [0..15,17,18]; F3, F4 [0..17].

## Proof of completeness

For full column rank B, u = B^{-T} t is the *unique* vector with given basis dots,
so enumerating all 2^18 sign patterns exhausts *all* real candidates. The norm
equation filters to unit vectors; the extension equations test the remaining 39
columns. Zero full passes = no real 58th line. QED.

## Validation

- **Positive control.** Deleting F1 column 57 and re-running the enumeration on the
  56-set recovered the dropped direction with alignment 1.0 (dot error ~5e-15):
  the pipeline detects extensions when they exist.
- **Fresh replay.** `artifacts/verify_noext.py ALL` reproduces the table above
  from the filed matrices in ~53 s, ending VERIFY_OK.

## Relation to the target and the fallback

- *Target (58-line witness):* this result blocks the parent-extension route for
  every machine-readable documented 57-parent and constrains any future 58-search
  to 57-sets outside the F1..F4 families. It is a fragment of the target program,
  not the target itself.
- *Preset fallback (three-point dual with objective < 58):* not pursued because it
  is infeasible as stated — the published three-point (Delta_3) optimum at
  (n,a) = (18,1/5) is 61 (de Laat et al. Table 1; Barg–Yu/King–Tang), so by weak
  duality no dual-feasible vector can have value < 58; no SDP solver exists in
  this environment; Barg–Yu report no improvement from larger degree for |D| = 2.
  The maximality theorems above are the demonstrably better bounded route.

## Limitations

- Per-parent maximality, not global N_{1/5}(18) <= 57: other (undocumented or
  Munemasa-family) 57-sets could in principle extend to 58.
- Says nothing about 58-systems not containing any F1..F4 57-subset.
- Counts depend on the fixed bases but the zero-extension verdict is
  basis-independent (any basis gives the same exhaustive coverage).

## Artifacts

- `artifacts/F1.json` .. `artifacts/F4.json` — parent matrices (parsed from the
  Greaves–Syatriadi–Yatsyna arXiv:2104.04330 source).
- `artifacts/verify_noext.py` — self-contained exact verifier (needs sympy).
- `artifacts/noext_cert.json` — certificate ledger (bases, dets, counts).
