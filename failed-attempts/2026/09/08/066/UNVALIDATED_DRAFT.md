# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified two-sided maximal-determinant interval at order 10 with two
inequivalent extremal witnesses (Hadamard maxdet benchmark, fallback track)

## Status

Proved (machine-checked, stdlib-only replay). The full Hadamard-equivalence
census (exact class count K) is NOT closed; this draft certifies the admitted
fallback plus a partial-census strengthening: at least two HT-classes.

## 1. Objects and notation

Let D(10) = max |det M| over 10x10 (+-1)-matrices. HT-equivalence =
signed row permutations + signed column permutations + transpose.
W1 = output/artifacts/witness_W1.csv, W2 = output/artifacts/witness_W2.csv,
G1 = W1 W1^T (gram_W1.csv), G2 = W2 W2^T (gram_W2.csv).

## 2. Certified claims

(a) det(W1) = det(W2) = 73728 exactly (fraction-free Bareiss, replayed in
    verify.py). Hence D(10) >= 73728.
(b) det(G1) = det(G2) = 73728^2 = 5435817984 exactly (Bareiss on the stored
    Gram, which is re-derived entry-by-entry from the witness, never trusted).
(c) Two-sided interval: 73728 <= D(10) <= 99840, i.e. D(10)/512 in [144,195].
    Upper half: Hadamard |det M|^2 <= 10^10 (Lemma 3) + 2^9-divisibility
    (Lemma 4, proved from scratch): |det M| <= 100000 rounds down to the top
    multiple of 512, 99840.
(d) HT-inequivalence: W1, W2 are NOT HT-equivalent (exact joint row/column
    permutation backtracking with full column-choice backtracking, both
    transpose branches; hteq.py). Cross-checked by an independent brute-force
    canonical-minimum computation over all 9! column permutations on both
    transpose branches (both differ). Hence at least two HT-classes attain
    |det| = 73728 (K >= 2 if the value 73728 is optimal, K_classes_at_max >= 2
    unconditionally among matrices attaining 73728).
(e) The exact HT-decision procedure is validated inside verify.py by a
    positive control (random signed-perm+transpose image accepted), a negative
    control (a determinant-dropping single flip rejected), and reflexivity.

## 3. Lemmas (proofs)

Lemma 3 (Hadamard, n = 10). For real M with |Mij| <= 1,
|det M|^2 = det(M^T M) <= prod_j ||col_j||^2 <= 10^10, since det of a
positive-semidefinite matrix is at most the product of its diagonal entries
(AM-GM on eigenvalues: det = prod lambda_i <= (tr/n)^n), and each diagonal
entry of M^T M is the squared norm of a (+-1)-column, equal to 10.
So |det M| <= 10^5 = 100000.

Lemma 4 (2^(n-1)-divisibility). Let M be n x n (+-1). Subtracting row 1 from
rows 2..n leaves det unchanged; each of rows 2..n then has even entries, so
det M = 2^(n-1) det M' with M' integral (first row +-1, other rows halved).
For n = 10, 512 | det M.

Corollary. D(10) <= 99840: by Lemma 3, D(10) <= 100000; by Lemma 4, D(10) is
a multiple of 512; the largest multiple of 512 not exceeding 100000 is
195 x 512 = 99840. With (a): 73728 <= D(10) <= 99840.

## 4. Method (reproducible)

W1: seeded single-flip hill-climb (numpy seed 0), exactness from Bareiss only.
Candidates: W1 + 6 independent numpy hill-climb maximizers (seed 2026);
all have exact |det| = 73728 (Bareiss). HT table: 6/7 in the W1 class,
1/7 (W2) in a second class. Exact determinants: fraction-free Bareiss with
row-swap sign tracking (hteq.py). Replay: python3 output/artifacts/verify.py
(stdlib only; floats never enter the certificate).

## 5. Sharpness, limits, and what is NOT claimed

- Optimality of 73728 (D(10) = 73728) is NOT proved here: the interval top is
  99840. The value 73728 agrees with OEIS A003433 (cited as background, not
  as evidence). Closing the gap needs the Ehlich bound or exhaustive search.
- The exact census count K is NOT determined; only K_attaining(73728) >= 2
  classes is certified. No claim is made about further classes.
- An early candidate "Ehlich closed form" from memory contradicted the proved
  a(22) value and was discarded; no Ehlich formula is stated or used.
- A triple-product invariant proposed mid-investigation was found NOT to be
  HT-invariant (odd degree in the flipped line) and was discarded; the
  committed inequivalence rests solely on the exact backtracking decider plus
  the independent brute-force canonical-minimum cross-check.
- Two backtracking bugs found during development (dropped column-undo causing
  a false positive; first-extension-only yielding causing incompleteness) are
  documented here; both are fixed in the committed hteq.py, whose soundness
  on this instance is pinned by the positive/negative controls and the
  independent canonical-minimum cross-check in verify.py.

## 6. Files

- output/artifacts/witness_W1.csv, witness_W2.csv (extremal matrices)
- output/artifacts/gram_W1.csv, gram_W2.csv (stored Gram matrices)
- output/artifacts/hteq.py (exact det + HT decider)
- output/artifacts/verify.py (stdlib-only replay of everything)
- output/artifacts/certificates.json (numbers + pairwise table)
- output/artifacts/candidate_maximizers.json (W1 + 6 further maximizers)
- output/artifacts/make_artifacts.py (partial generator; superseded in part
  by the steps logged in WORKLOG.md -- retained for provenance, not needed
  for verification)
