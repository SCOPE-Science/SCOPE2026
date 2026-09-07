# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact Alabama-Paradox Census for the Five-State House-18 Stratum

## Abstract
We close a fixed apportionment stratum by exact integer arithmetic. For the
S5-quotiented set of primitive population vectors with five states and entries
in [1,30], we enumerate all 264463 canonical vectors, compute Hamilton
largest-remainder apportionments at house sizes 18 and 19, and count Alabama
paradoxes. We exhibit the least witness, give hand-checkable quota ledgers and
divisor-method certificates, and report cross-method agreement. All claims are
replayable in ~15 s by a pure-stdlib script using only integers and
`Fraction`, with zero float constants.

## 1. Definitions (auditable, fixed in code)

- **Stratum.** `S = {p in Z^5 : 30 >= p1 >= p2 >= p3 >= p4 >= p5 >= 1,
  gcd(p1,...,p5) = 1}`. Canonical form is weakly decreasing; this quotients by
  S5 permutation symmetry. Raw combinations with replacement in [1,30] number
  C(30+5-1,5) = C(34,5) = **278256** (the audit plan's figure 118755 is a typo;
  the sub-box figure C(24,5)=42504 for max<=20 is correct and confirms the
  formula). Primitive subset: **264463**.
- **Hamilton (largest remainder), deterministic.** For house size H and total
  P = sum p: quota `q_i = p_i*H/P` (as `Fraction`); floor `f_i = (p_i*H)//P`;
  remainder numerator `r_i = (p_i*H)%P` (remainder is `r_i/P`); deficit
  `R = H - sum f_i`; order states by `(-r_i, index)`; give one extra seat to the
  first R. Sums equal H by construction. Hamilton satisfies quota
  (`floor(q_i) <= a_i <= ceil(q_i)`) on every instance.
- **Alabama violation.** `a(19)_i < a(18)_i` for some state i (index in canonical
  order), H = 18 -> 19.
- **Divisor methods** via exact highest-averages from zero, tie-break by smaller
  index (hence the seat sequences for H = 18, 19 are prefixes of one chain, so
  house-monotonicity is built in and then verified):
  - *Jefferson / D'Hondt:* next seat to max `p_i/(a_i+1)`, i.e. compare
    `p_i*(a_j+1)` vs `p_j*(a_i+1)`.
  - *Webster / Sainte-Lague:* next seat to max `p_i/(a_i+0.5)`, i.e. compare
    `p_i*(2a_j+1)` vs `p_j*(2a_i+1)`.
  - *Huntington-Hill:* each state starts at 1; remaining H-5 seats to max
    `p_i/sqrt(a_i(a_i+1))`, i.e. compare `p_i^2*a_j(a_j+1)` vs
    `p_j^2*a_i(a_i+1)` (squared integers, no floats).
- **Divisor certificates (weak optimality, integer).** An allocation `a` with
  sum H is divisor-optimal iff, with the stated tie convention:
  - Jeff: `p_i*a_j <= p_j*(a_i+1)` for all i and all j with `a_j > 0`
    (i.e. `max p_i/(a_i+1) <= min_{a_j>0} p_j/a_j`);
  - Web: `p_i*(2a_j-1) <= p_j*(2a_i+1)` for all i and all j with `a_j >= 1`;
  - HH: `p_i^2*(a_j-1)*a_j <= p_j^2*a_i*(a_i+1)` for all i and all j with
    `a_j >= 1`.
  Strict `<` selects a unique divisor interval; equality `=` is a documented tie
  broken by index. Explicit divisors are given below as `Fraction`s where they
  exist (HH tie case needs an irrational divisor; the squared ledger is exact).

## 2. Main result (computed theorem)

**Theorem (stratum census, machine-checked).**
For S as above at H = 18 -> 19, with index tie-breaks:

- (a) `N_total = 278256`, `N_primitive = 264463`,
  **`N_18 = 13343`** canonical vectors exhibit an Alabama paradox under
  Hamilton (about 5.04% of primitive vectors).
- (b) The least Alabama witness in `(max(p), p_lex)` order — hence also least
  total population — is **`p* = (4,4,1,1,1)`**, `P = 11`, with Hamilton seats
  `[6,6,2,2,2]` at H=18 and `[7,7,2,2,1]` at H=19 (state index 4 loses 2->1).
- (c) On `p*`, Jefferson gives `[8,7,1,1,1] -> [8,8,1,1,1]`, Webster gives
  `[6,6,2,2,2] -> [7,6,2,2,2]`, Huntington-Hill gives
  `[6,6,2,2,2] -> [7,6,2,2,2]`: all three are house-monotone (no loss), with
  divisor certificates in Section 4.
- (d) Stratum-wide, Jefferson, Webster and Huntington-Hill have **zero**
  house-monotonicity violations (0/0/0 over all 264463 vectors at 18->19) and
  zero weak-optimality violations.
- (e) Pairwise method agreement counts (equality of full 5-vectors) are tabulated
  in Section 5. In particular Hamilton agrees with Webster on ~88.5% of vectors
  but with Jefferson on only ~45%.
- (f) Verified paradox-free prefixes: every vector with `max <= 3` and every
  vector with total population `P <= 10` is paradox-free (min paradox max is 4,
  min paradox P is 11). Sub-box `max <= 20`: 42504 raw, 40213 primitive, 2390
  Alabama.

Status of each part: (a)-(f) are **computed evidence** proved by exhaustive
exact-integer enumeration replayed by an independent verifier; the hand tables
for (b)-(c) are additionally **proof checkable by hand** below. No asymptotic
claim, no originality claim beyond the triage in `inputs/topic.json`
(Balinski-Young, Census methods, encyclopedia exposition cover only general
theorems / single historic witnesses / definitions).

## 3. Minimal witness: hand ledger

`p* = (4,4,1,1,1)`, `P = 11`. Minimality means: no primitive canonical vector
with `max <= 3` and none with `P <= 10` is Alabama (exhaustively verified), and
`p*` is the lexicographically first among `max = 4` Alabama vectors. Full
recount confirms the next `(max,lex)` witnesses are `(4,4,4,1,1)`,
`(6,6,6,5,2)`, `(7,4,1,1,1)`, `(7,6,6,4,2)` (see `top5_witnesses.csv`).

### Hamilton at H = 18
Quotas: `72/11 = 6 + 6/11` (states 0,1), `18/11 = 1 + 7/11` (states 2,3,4).
Floors `[6,6,1,1,1]`, sum 15, `R = 3`. Remainder numerators (units of 1/11):
`[6,6,7,7,7]`. Order: 2,3,4 then 0,1. R=3 seats go to 2,3,4.
**Seats `[6,6,2,2,2]`**, sum 18. No cutoff tie (7/11 vs 6/11).
Quota check: 6 in [6,7], 2 in [1,2]. Pass.

### Hamilton at H = 19
Quotas: `76/11 = 6 + 10/11` (states 0,1), `19/11 = 1 + 8/11` (states 2,3,4).
Floors `[6,6,1,1,1]`, sum 15, `R = 4`. Remainders: `[10,10,8,8,8]`.
Order: 0,1 then 2,3,4. R=4 seats go to 0,1,2,3; **cutoff tie at 8/11 among
states 2,3,4 broken by index (2,3 over 4)**.
**Seats `[7,7,2,2,1]`**, sum 19. Quota check: 7 in [6,7], 2 in [1,2], 1 in
[1,2]. Pass.
**Alabama paradox: state 4 drops 2 -> 1 while H grows 18 -> 19.**

Anyone can verify the above with pencil: multiply, divide with remainder,
sort five numbers.

## 4. Divisor certificates on p* (exact)

Sums all equal H. Weak-optimality inequalities were checked for all 25 (i,j)
pairs by integer arithmetic (see `verification.csv`); explicit divisors:

- **Jefferson** `[8,7,1,1,1]` (H18), `[8,8,1,1,1]` (H19), divisor **`d = 1/2`**
  both. Ledger: `max p/(a+1) = 1/2 = min p/a` (states: 4/8, 1/2 on the left;
  4/8, 1/1 on the right at H18 up to permutation). Equality tie broken by index
  to reach exactly H (at d=1/2 the floor sums jump 17 -> 22; the index rule
  selects which tied 1/2-seats are seated). House-monotone: 7->8 at index 1.
  Note: Jefferson **violates quota** here (8 > ceil 72/11 = 7 and 8 > ceil
  76/11 = 7) — the expected Balinski-Young tension, recorded as a
  quota-compliance check, not a failure.
- **Webster** `[6,6,2,2,2]` (H18) with **`d = 2/3`**: `max 2p/(2a+1) = 8/13`
  (states 0,1) `< d = 2/3 = min 2p/(2a-1)` (states 2,3,4 at 2/3). Quotients:
  4/(2/3)=6, 1/(2/3)=1.5 -> rounds to 6 and 2 (half up). Strict except the
  upper tie at 2/3. `[7,6,2,2,2]` (H19) with **`d = 8/13` (tie)**:
  `max = 8/13 = min`; both states 0,1 sit at quotient 6.5 (half-integer tie);
  index gives the 19th seat to state 0. House-monotone: 6->7 at index 0.
  Both Webster allocations satisfy quota.
- **Huntington-Hill** `[6,6,2,2,2]` (H18) with **`d = 2/3` (`d^2 = 4/9`)**:
  `max p^2/(a(a+1)) = 16/42 = 8/21 <= 4/9 < min p^2/((a-1)a) = 1/2`.
  `[7,6,2,2,2]` (H19) with **squared divisor `d^2 = 8/21` (tie)**:
  `max = 8/21 = min` (state 1's next-seat priority equals state 0's last-seat
  priority). Hence `d = sqrt(8/21)`, **irrational — no `Fraction` divisor
  exists**; the certificate is the exact squared-integer ledger above with the
  index tie-break. This is disclosed rather than forced into a `Fraction`.
  House-monotone: 6->7 at index 0. Both HH allocations satisfy quota.

## 5. Stratum tables

Agreement = number of canonical vectors (of 264463) where two methods return
identical 5-vectors:

| pair | H=18 | H=19 |
|---|---|---|
| Ham vs Jeff | 119770 | 117331 |
| Ham vs Web | 234198 | 233830 |
| Ham vs HH | 187328 | 192491 |
| Jeff vs Web | 125612 | 125073 |
| Jeff vs HH | 80675 | 82179 |
| Web vs HH | 189885 | 193410 |

Divisor house-monotonicity violations 18->19: Jeff 0, Web 0, HH 0.
Divisor weak-optimality violations: 0, 0, 0 (both H).

Distribution note (secondary observation, computed): Alabama counts by
`max(p)`: 4:2, 5:0, 6:1, 7:7, 8:6, ... (full histogram in census log; max=5
layer has 69 primitive vectors, zero Alabama). Occurrence is not monotone in
max. Smallest total populations with paradoxes: P=11 (1 vector), 14 (2), 22
(2), 23 (4).

## 6. Reproduction (deterministic, <60 s, single core)

```
python3 output/artifacts/census.py    # ~15 s, writes 4 CSVs, prints counts
python3 output/artifacts/verify.py    # independent replay, ends ALL CHECKS PASSED
sha256sum output/artifacts/*
```

- `census.py`: stdlib only (`itertools`, `math`, `csv`, `hashlib`, `time`,
  `fractions.Fraction`); zero float constants (AST-verified); deterministic
  iteration + index tie-breaks; asserts every sum and quota/optimality property.
- `verify.py`: separate Fraction-based Hamilton path + independent greedy
  divisor path; rechecks every CSV row, every inequality, explicit divisors,
  full Hamilton recount (N_prim/N_ala/sub/minimality), top-5 replay, no-float
  audit.
- CSVs: `census_counts.csv` (counts + agreement + bounds + timing),
  `witness.csv` (per-state quotas/floors/remainders/seats + divisor seats),
  `verification.csv` (quota bounds, sums, tie/divisor ledgers),
  `top5_witnesses.csv` (five least `(max,lex)` Alabama vectors with loss indices).

SHA256 (this run):
- census.py `4900570b40e8f4705f77604d2c4bc97059b2ac3947a5a0315b57dbc3ef6bc026`
- verify.py `bc0295cc1fd3311d2f949fd32108e44219bdec1508f179e6fcca95b3cc945787`
- census_counts.csv `bead41a73a0ae3a460f0a7f0d5591d2313fe0571dfc347df9e4555adf0f9544d`
- witness.csv `c1d7720da59e8b10c925e0e77550c1e931292bb8d5cddf6a6750f3160bdc3faa`
- verification.csv `70dc656448810870e03ab3f89a474c1e9034f28b2e1cd71987812141bead6dd3`
- top5_witnesses.csv `574edb4856c8675971fb846fb51f5a0df31f637e3c74d6c4e77759d574905633`

## 7. Limitations and uncertainty (honest)

- Fixed stratum only: n=5, H=18->19, box entries [1,30], S5-quotiented,
  stated index tie-breaks. Different tie-breaks move some boundary vectors
  (the witness H19 cutoff tie at 8/11 and divisor ties at 1/2, 8/13, 8/21 are
  tie-sensitive; the ledger documents the rule). The count N_18=13343 is
  relative to this rule.
- Method implementations are highest-averages equivalents of divisor methods;
  certified by weak-optimality inequalities, the standard Balinski-Young
  characterization, not by separately searching real divisors.
- HH H19 on p* needs an irrational divisor; we certify via squared integers
  (exact) rather than a `Fraction` d.
- No claim of scholarly priority: triage rests on the knowledge-cutoff sources
  in `inputs/topic.json`; web probes failed (proxy/403/timeout) as documented
  there. Contribution is the closed citable stratum + hand witness + ledgers,
  not a new paradox theorem.
- Conjecture (not claimed): the max==5 gap (zero Alabama among 69 primitive
  vectors) is verified computationally for this stratum only; no general
  explanation is offered.

## References
- Balinski & Young, *Fair Representation* (Yale UP, 1982) — impossibility and
  divisor-method characterization.
- U.S. Census Bureau, Methods of Apportionment / Computing Apportionment
  (Huntington-Hill description) — divisor rounding definitions.
- Alabama paradox encyclopedia exposition (classic H=299->300 witness).
