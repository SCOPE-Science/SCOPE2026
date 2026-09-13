# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Nonexistence of an admissible 28-set in one class mod 30

## Question
Does there exist an integer residue `r` with `gcd(r,30)=1` and an integer
set `H = {h_1 < ... < h_28}` with `0 <= h_1` and `h_28 <= 1000` such that

1. every `h_i` is congruent to `r` modulo 30, and
2. `H` is admissible, meaning for every prime `p <= 28` the residues
   `{h_i mod p}` omit at least one class modulo `p`?

## Answer
**No. No such pair `(r, H)` exists.**

## Proof
Since condition (i) only depends on `r mod 30`, we may take `r` in
`{1,...,30}`. The condition `gcd(r,30)=1` leaves exactly the 8 classes

    1, 7, 11, 13, 17, 19, 23, 29.

Fix such a class `r`. Every admissible `H` must be a 28-element subset of
the finite pool `P(r) = {x : 0 <= x <= 1000, x = r (mod 30)}`. The pool
sizes are:

- `|P(1)| = |P(7)| = 34` (e.g. `1, 31, ..., 991`; `7, 37, ..., 997`),
- `|P(r)| = 33` for `r in {11, 13, 17, 19, 23, 29}`.

Hence the total search space is finite and small:

- `C(34,28) = C(34,6) = 1344904` subsets per 34-element pool,
- `C(33,28) = C(33,5) = 237336` subsets per 33-element pool,
- total `2 * 1344904 + 6 * 237336 = 4113824` subsets.

Each subset is tested directly against the defining property: for every
prime `p <= 28` (i.e. `2,3,5,7,11,13,17,19,23`), the set of residues
`{h mod p : h in H}` must have size at most `p - 1`. Exhaustive
enumeration over all 8 classes checks all 4113824 subsets and finds zero
admissible sets. The deterministic verifier is
`output/artifacts/verify_nonexistence.py`, which asserts the pool
construction, the expected binomial counts, and reports:

    r= 1: pool_size=34 subsets_checked=1344904 admissible_found=0
    r= 7: pool_size=34 subsets_checked=1344904 admissible_found=0
    r=11: pool_size=33 subsets_checked=237336 admissible_found=0
    r=13: pool_size=33 subsets_checked=237336 admissible_found=0
    r=17: pool_size=33 subsets_checked=237336 admissible_found=0
    r=19: pool_size=33 subsets_checked=237336 admissible_found=0
    r=23: pool_size=33 subsets_checked=237336 admissible_found=0
    r=29: pool_size=33 subsets_checked=237336 admissible_found=0
    TOTAL_SUBSETS_CHECKED=4113824
    VERIFIED: no admissible 28-set exists in any coprime class mod 30.

Since every candidate `(r, H)` belongs to one of these 8 enumerations,
this is a complete proof that no 28-element subset of any coprime residue
class modulo 30 inside `[0,1000]` is admissible, which is exactly the
nonexistence half of the target claim's complete answer.

## Reproducibility
Run with a clean module path (to avoid any local shadowing):

    PYTHONPATH="" python3 output/artifacts/verify_nonexistence.py

The script uses only `itertools`/`math`, has no randomness, and enumerates
every `C(n,28)` combination per class with an exact admissibility test.
Runtime is on the order of ~15 seconds on a single core.
