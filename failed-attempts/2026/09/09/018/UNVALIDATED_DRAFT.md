# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Closed residue-class maximal-gap records G_{4,r}, G_{6,r} to 5,000,000

## 1. Objects and scope
X = 5,000,000. Primes p <= X regenerated from code alone (`sieve.py`, bytearray
sieve; no external list; pi(X) = 348513). Within-class consecutive gaps for the
coprime classes 1,3 mod 4 and 1,5 mod 6. A record is a within-class gap strictly
exceeding all previous within-class gaps in that class (closed table: every record
with upper witness p' <= X, maximality by exhaustive scan).

## 2. Result: exact record tables (gap, lower p, upper p')

### 1 mod 4 (174193 primes, 21 records)
(8,5,13),(12,17,29),(16,73,89),(24,113,137),(32,197,229),(48,461,509),
(56,1493,1549),(60,1801,1861),(68,9533,9601),(72,15661,15733),(88,16741,16829),
(108,33181,33289),(128,39581,39709),(148,50593,50741),(152,180797,180949),
(200,183089,183289),(224,1561829,1562053),(240,1637813,1638053),
(248,2243909,2244157),(252,4468889,4469141),(260,4874717,4874977).

### 3 mod 4 (174319 primes, 23 records)
(4,3,7),(8,11,19),(12,31,43),(20,83,103),(24,283,307),(36,383,419),
(40,1327,1367),(56,2591,2647),(60,7351,7411),(64,7759,7823),(68,11171,11239),
(112,11587,11699),(120,31391,31511),(132,46919,47051),(144,147919,148063),
(156,288023,288179),(168,360611,360779),(176,425603,425779),(184,507163,507347),
(200,666203,666403),(240,1414703,1414943),(256,2198887,2199143),
(272,3358151,3358423).

### 1 mod 6 (174190 primes, 18 records)
(6,7,13),(12,19,31),(18,43,61),(30,241,271),(54,1327,1381),(60,4363,4423),
(78,7789,7867),(84,22189,22273),(90,24247,24337),(96,38461,38557),
(114,40237,40351),(162,69499,69661),(174,480169,480343),(192,1164607,1164799),
(204,1207699,1207903),(252,1467937,1468189),(270,1526659,1526929),
(282,3975721,3976003).

### 5 mod 6 (174321 primes, 15 records)
(6,5,11),(12,29,41),(18,113,131),(30,197,227),(36,521,557),(42,1109,1151),
(54,1733,1787),(60,6389,6449),(84,7349,7433),(126,35603,35729),
(150,148517,148667),(162,180797,180959),(168,402593,402761),
(246,406907,407153),(258,2339039,2339297).

Sanity: class counts satisfy 174193+174319 = 348512 = pi(X)-1 (excludes 2) and
174190+174321 = 348511 = pi(X)-2 (excludes 2,3).

## 3. Certificates (proof, not just computation)
- Endpoints: all 154 record witnesses carry deterministic Miller-Rabin transcripts
  (bases 2,7,61, logged in `certs.json`) AND pass an independent BPSW test
  (MR base 2 + strong Lucas-Selfridge), plus a complete trial-division proof to
  sqrt in the replay (feasible because X = 5e6).
- Interior points: for every record run (a,b), each in-class integer strictly
  between a and b is exhibited composite with its smallest prime factor
  (`spf_logs.json`, 1777 entries), each cross-checked by trial division in replay;
  run-length identity (b-a)/q - 1 verified per record.
- Maximality: exhaustive scan of all within-class gaps in the replay; every gap
  <= the terminal record of its class.

## 4. Kourbatov-trend diagnostic (computed evidence, b = 0 baseline)
Trend T(q,x) = phi(q) x/li(x) (2 log(li(x)/phi(q)) - log x), phi = 2, li by
Simpson (see `verify.py`; full per-record table in `trend_residuals.json`).
Terminal values:
| class | max gap | T0 at upper end | resid G-T0 | G/(2 log^2 x) |
|---|---|---|---|---|
| 1 mod 4 | 260 @ 4874977 | 248.60 | +11.40 | 0.548 |
| 3 mod 4 | 272 @ 3358423 | 233.10 | +38.90 | 0.602 |
| 1 mod 6 | 282 @ 3976003 | 240.06 | +41.94 | 0.611 |
| 5 mod 6 | 258 @ 2339297 | 218.55 | +39.45 | 0.600 |
Every record in all four classes satisfies the Kourbatov empirical bound
G < phi(q) log^2 x = 2 log^2 x. No Gumbel fit is claimed.

## 5. Replay
```
python3 output/artifacts/sieve.py     # regenerates primes, filtered lists, records
python3 output/artifacts/certify.py   # CERT_OK endpoints=154 interior=1777
python3 output/artifacts/verify.py    # VERIFY_OK (distinct MR bases + trial division + exhaustive scan)
```

## 6. Originality / prior art
Kourbatov (arXiv:1610.03340) defines G_{q,r}, proposes T(q,x), Gumbel rescaling
with open limiting distribution, computes to 1e12 but publishes only heuristics,
one example table (q=1000, r=1), figures and PARI code — no closed G_{4,r}/G_{6,r}
tables to 5e6. Kourbatov-Wolf (arXiv:1901.03785) and Kourbatov (arXiv:1709.05508)
likewise give trends/n-indexed statistics, not X-closed witness censuses.
Oliveira e Silva / Caldwell / OEIS A002386/A005250 publish all-prime records only;
the filtered sequences needed for residue-class records are not in those tables.
The four closed witness tables above are therefore new exact ground truth.

## 7. Limits (uncertainty, not proof)
- Finite cutoff X = 5e6; says nothing about asymptotics or the open limiting distribution.
- Trend uses b = 0 baseline (Kourbatov leaves b = O_q(1) fitted); residuals are
  diagnostic only.
- Primality/compositeness certificates are machine certificates replayable in
  stdlib Python, not hand-checkable proofs.
