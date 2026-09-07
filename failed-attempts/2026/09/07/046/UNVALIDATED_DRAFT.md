# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified prime-interval census: every [x, x+x/30000] with 1e7 ≤ x ≤ 1e8 contains a prime

## Claim

**Theorem.** For every real $x$ with $10^7 \le x \le 10^8$, the interval
$[x, x + x/30000]$ contains at least one prime.

**Stronger finite record (computed).** The same sieve data certify that every
$[x, x+x/D]$ with $10^7 \le x \le 10^8$ contains a prime for every integer
$D \le 72168$, and $D = 72169$ is best possible for this method over this range
(the pair $p=11113933$, $q=11114087$ of consecutive primes is the unique
tightest constraint). The headline $D=30000$ is kept to match the assigned
target; the $D=72168$ sharpening is reported as an explicit computed corollary.

## Context and comparison

- Schoenfeld (1976, Thm 12) gives a prime in $(x(1-1/16598), x]$ for
  $x > 2010760$, i.e. effective $\Delta = 16598$ in this range. The certified
  $D = 72168$ is $\approx 4.3\times$ narrower; even the headline $D=30000$ is
  $\approx 1.8\times$ narrower.
- Dusart-type bounds ($|\theta(x)-x| \le 0.2x/\log^2 x$) give effective
  $\Delta \approx 6$–$8$k here — far *wider* intervals than the target, so they
  imply nothing about $D = 30000$ (see §4 for the quantitative failure).
- Bertrand's postulate ($[x,2x]$) is $\sim 10^4\times$ wider than the certified
  width at $10^8$.
- The proof is a *bounded-range certificate*, not a global theorem: it makes no
  claim outside $[10^7, 10^8]$ and does not improve any asymptotic result.

## Proof

Let $P = (p_1 < p_2 < \dots)$ be the primes in $[9.9\times 10^6,\, 100.1\times
10^6]$, computed by the segmented sieve (§3). The sieve starts below $10^7$ so
that the prime preceding $10^7$ is included, and ends above
$10^8 + 10^8/30000 \approx 100003334$ so that every $x \le 10^8$ has its
candidate prime inside the sieved range.

**Lemma (gap criterion).** Fix $D \ge 1$. Suppose $(p, q)$ are consecutive
primes and $[p, q]$ meets $[X_L, X_R] = [10^7, 10^8]$. Put
$a = \max(p, X_L)$. Then every $x \in [X_L, X_R] \cap [p, q)$ has a prime in
$[x, x + x/D]$ *unless* $D(q - a) > a$.

*Proof.* If $x \le p$, then $p \in [x, x + x/D]$. If $x > p$, the next prime at
or after $x$ is $q$, so failure means $x + x/D < q$ for some
$x \ge a$, i.e. $a(1 + 1/D) < q$ (by continuity, approaching $a$ from above),
i.e. $D(q-a) > a$. ∎

Hence it suffices to check the integer inequality $D(q - a) \le a$ for every
consecutive-prime pair meeting $[10^7, 10^8]$ — exact integer arithmetic, no
floating point.

**Computation.** The script `artifacts/reproduce.py` sieves
$[9.9\times 10^6, 100.1\times 10^6)$ with base primes through $\sqrt{\mathrm{HI}}$
(segment size $2^{20}$, `numpy` boolean slices) and checks the criterion for
$D = 30000$ over all $5{,}096{,}877$ touching consecutive pairs. All pass. The
tightest pair is $(p, q) = (10156049, 10156187)$ (gap $138$), with slack
$a - 30000(q-a) = 6016049 > 0$. The maximal gap meeting the range is $220$,
versus the minimal window width $\lceil 10^7/30000 \rceil = 334$. ∎

**Correctness anchors.** The same prime array satisfies $\pi(10^7) = 664579$
and $\pi(10^8) = 5761455$ (both classical values), where primes below the
sieve start are counted by an independent small sieve of $[2, 9.9\times 10^6)$.
An independent brute-force bytearray sieve over the two halves reproduces the
maximal gaps $220$ ($[9.9\mathrm{M}, 55\mathrm{M})$) and $210$
($[55\mathrm{M}, 100.2\mathrm{M}]$).

## Method notes (what each leg contributes)

### Segmented sieve (the proof)

Base primes to $\lceil\sqrt{\mathrm{HI}}\rceil = 10006$ (in production the
script extends to the next prime, $10111$; see §6 for the documented deviation
from the audit plan's $10^4$), segment size $2^{20}$, `numpy` boolean slices
over $[9.9\times 10^6, 100.1\times 10^6)$. Per-segment witness primes and
counts are in `artifacts/gap_table.csv` (87 blocks). Runtime $\approx 0.4$ s
for the sieve $+$ gap check on the run machine (32 cores available, single
core used).

### Analytic theta margin (documents infeasibility — not part of the proof)

For $h(x) = x/30000$ and an explicit Dusart-type envelope
$E(t) = 0.2\,t/\log^2 t$ plus the Rosser–Schoenfeld prime-power correction
$U(t) = 1.000081\sum_{k \ge 2} t^{1/k} \ge \psi(t) - \theta(t)$, the analytic
leg would need $m(x) = h(x) - E(x+h) - E(x) - U(x+h) > 0$. On a 164-point
log-spaced grid over $[10^7, 10^8]$ (`artifacts/margin_table.csv`), the best
margin is $-18602.7$ (classic shape) and $-4877.3$ even for a decade-sharper
$E_2(t) = 0.35\,t/\log^3 t$ envelope. The analytic route fails by one to two
orders of magnitude in this range — honestly reported rather than tuned away.
Consequently there is no $X_1 \in [3\times 10^7, 5\times 10^7]$ above which the
theta inequality takes over; the sieve covers the *entire* range, which the
audit plan explicitly permits ("this closes $[10^7, X_1]$" with $X_1$ pushed
to the top end).

### Selberg upper-sieve fragment (one-sided consistency check, not a lower bound)

Optimal Selberg weights for sifting $\{2, 3, 5\}$ with level $D = 36$ on
support $\{1,2,3,5,6,10,15,30\}$ are solved exactly over $\mathbb{Q}$ via
$Mv = e_1$ ($M_{d,e} = 1/\mathrm{lcm}(d,e)$), giving
$\lambda = (1,-1,-1,-1,1,1,1,-1)$ with $G = 15/4$ and remainder bound
$R = (\sum|\lambda_d|)^2 = 64$. On each of 12 sampled blocks $[X, X+X/30000)$
the exact sieve identity $S = \sum_{d,e}\lambda_d\lambda_e\lfloor\cdot\rfloor$
is asserted (exact rational equality with the brute-force coprime count), the
sieve prime count $\le$ survivor count, and the survivor count $\le y/G + R$
(`artifacts/selberg_table.csv`). This cross-checks block counts against an
independent quadratic-form upper bound; it proves no lower bound and is not
claimed to.

## Reproduction

```
python3 artifacts/reproduce.py
```

Single script, stdlib + numpy only. It writes `margin_table.csv`,
`gap_table.csv`, `selberg_table.csv`, `summary.json` next to itself, asserts
all certificates (pi anchors, gap closure with exact integer arithmetic,
Selberg exact identities and upper bounds, runtime $< 2$ h), and exits $0$ iff
everything holds. Observed runtime $< 1$ s on the run machine
($\approx 0.66$ s total); the 2-hour budget leaves $\sim 10^4\times$ headroom.

## Limitations and uncertainty

1. Bounded range only: nothing is claimed outside $[10^7, 10^8]$.
2. The analytic ($\theta$-margin) leg *fails* in this range (best margin
   $-18602.7$); the proof is the sieve, not the theta inequality. The audit
   plan's "theta margin for $x \ge X_1$" step is therefore discharged by
   documenting infeasibility, with the sieve covering the whole interval.
3. The Selberg fragment is a one-sided upper-bound consistency check, not an
   independent lower-bound proof.
4. Correctness rests on the segmented-sieve implementation; mitigated by two
   independent verifications (pi-value anchors and a second brute-force sieve
   reproducing the maximal gaps) plus exact-integer gap arithmetic.
5. No originality is claimed for the sieve method itself (segmented Eratosthenes
   is classical); the contribution is the certified bounded sharpening
   ($D = 72168$ effective, $D = 30000$ as targeted — both beating Schoenfeld's
   $16598$ in $[10^7, 10^8]$) with a from-scratch two-hour reproducer.
6. Two audit-plan deviations, both documented: (a) base primes go to $10111$
   rather than $10^4$ because $\sqrt{100.1\times 10^6} \approx 10005 > 10^4$ —
   sieving only to $10^4$ would be incorrect; (b) $X_1$ is effectively the top
   of the range since the analytic leg fails everywhere below it.

## Artifacts

- `artifacts/reproduce.py` — single-script reproducer (stdlib + numpy).
- `artifacts/margin_table.csv` — 164-row theta-margin grid (analytic
  infeasibility record).
- `artifacts/gap_table.csv` — 87 per-segment witness primes and counts.
- `artifacts/selberg_table.csv` — 12-block Selberg upper-bound checks.
- `artifacts/summary.json` — machine-readable certificate summary with timings.
