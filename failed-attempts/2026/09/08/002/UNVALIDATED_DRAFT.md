# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified real hyperbolic-center census for x^2+c in periods 4–7
## via Gleason/dynatomic elimination, Sturm isolation, and orbit replay
### Lane-61 draft — 2026-09-07

## 1. Claim (closed census)

Let `f_c(x)=x^2+c`, `c` real. Let `C_n={c in R : 0 has exact period n under f_c}`.
Define `F_n(c)=f_c^n(0) in Z[c]` (`F_1=c`, `F_{n+1}=F_n^2+c`, `deg F_n=2^{n-1}`)
and dynatomic quotients `P_n` by exact division of all `P_d`, `d|n`, `d<n`.

**Theorem (computed + Sturm-certified).**
- `|C_4|=2`, `|C_5|=3`, `|C_6|=5`, `|C_7|=9`.
- Each `P_n` (`n=4,5,6,7`) is monic irreducible over Q (hence the minimal
  polynomial of every period-`n` center), separable, with discriminants
  - `disc(P_4)=58673`,
  - `disc(P_5)=319210993681318817`,
  - `disc(P_6)=-1041479942838787424502668691138595310951`,
  - `disc(P_7)=-153520438551539200635009419307199073882244641478128015821165293535598058722242376398611282776948544829749027404671`.
- Every real root lies in `[-2,0]` and is isolated in the pairwise-disjoint
  rational intervals below, each of width `5.82e-11 <= 1e-10`, with exact
  Sturm count 1 per interval and Sturm total = number of intervals.
- Kneading (signs of `x_k=f_c^k(0)`, `k=1..n-1`; `x_0=x_n=0` at the exact
  center) is constant on each interval (interval-arithmetic certified) and
  pairwise distinct within each `n` (table §5).
- Witness: the rightmost period-7 interval `I*_8` (midpoint
  `c0=-54112778801/34359738368 ≈ -1.574889139767038`) contains exactly one
  center `c*`. Its minimal polynomial is `P_7`, discriminant as above, kneading
  `-+----`, and midpoint/interval orbit replay is given in §6. At `c*`,
  `f_{c*}^7(0)=0` with minimal period 7, hence the cycle is superattracting
  (multiplier 0 since it contains the critical point where `f'=0`).
- An independent stdlib-only verifier replays all midpoint orbits exactly
  (Fractions), checks `P_n(a)P_n(b)<0`, widths, disjointness,
  `|F_n(mid)|,|P_n(mid)|<1e-6`, kneading equality and `X_n∋0`; all pass
  (`artifacts/verification.log`).

This is a *certified table*, not a structural theorem about dynatomic curves.
No claim is made beyond periods 4–7, beyond the real line, or about Galois
groups/monodromy. Irreducibility is over Q by `sympy.factor_list`; no claim
about mod-`p` reduction or complex dynamics.

## 2. Preliminaries (proof)

**Escape lemma.** All centers lie in `[-2,0]`.
*Proof.* If `c>0`, `x_1=c>0` and `x^2+c>0`, so `x_k>0` for all `k>=1`, never 0.
If `c<-2`, `|x_1|=|c|>2`. If `|x|>=|c|>2` then
`|x^2+c|>=x^2-|c|=|x|^2-|c|>|x|`: indeed for `|x|=|c|`,
`|c|(|c|-1)>|c|` since `|c|>2`, and LHS increases in `|x|`. Hence
`|x_k|` is strictly increasing for `k>=1`, bounded below by `|c|>2`, so never 0.
∎

**Dynatomic identity.** `F_n=∏_{d|n}P_d` in `Z[c]`, by construction with exact
remainders 0 (log `artifacts/derive.log`). Explicitly degrees:
`deg F_n=2^{n-1}`; `deg P_4=6`, `deg P_5=15`, `deg P_6=27`, `deg P_7=63`
(Möbius `∑_{d|n}μ(n/d)2^{d-1}`). Verified `F_4=F_1F_2`-quotient chain and
`F_6=P_1P_2P_3P_6` equality, all remainders `0` in `ZZ`.

**Exact-period correspondence.** `gcd(P_n,P_d)=1` for every `d|n`, `d<n`
(computed `sympy.gcd`, all `1`; log `artifacts/factor_disc.log`), and each
`disc(P_n)≠0` (values above), so roots are simple. If `0` has exact period
`n`, then `F_n(c)=0`, `F_d(c)≠0` for `d<n` (else period would divide `d`:
write `n=qd+r`, `f^n(0)=f^r(0)`), hence for `d|n`, `d<n`, `F_d(c)≠0`.
Since `F_n=∏_{e|n}P_e` and each `P_e|F_e` for `e<n`, all `P_e(c)≠0` for `e<n`,
so `P_n(c)=0`. Conversely if `P_n(c*)=0` then `F_n(c*)=0` and, by coprimality,
`P_e(c*)≠0` for `e|n`, `e<n`, hence `F_d(c*)≠0` for all proper divisors
`d|n`; if the minimal period were `d<n` then `d|n` (standard: `n=qd+r`
forces `r=0`), contradiction. So `P_n` roots ↔ exact-period-`n` centers
bijectively. Constant terms are all `1` (`P_n(0)=1`), so `c=0` is never a
higher-period root, consistent with `gcd=1`.

**Sturm certification.** For each `P_n`, `sympy.sturm()` over QQ gives a
Sturm sequence of length `deg+1` (7,16,28,64) ending in a nonzero constant
(§4 values), proving separability independently of discriminants. Sign
variations `V` evaluated in exact `Fraction` arithmetic (Horner, no floats)
give `V(-∞)-V(+∞)` = total real roots and `V(-2)-V(0)` = roots in `[-2,0]`:
- n=4: `V(-∞)=4,V(+∞)=2` → 2; `V(-2)=4,V(0)=2` → 2.
- n=5: `9-6=3`; `9-6=3`.
- n=6: `16-11=5`; `16-11=5`.
- n=7: `36-27=9`; `36-27=9`.
Hence no roots outside `[-2,0]`, and with the Escape lemma no centers are
missed. Bisection at exact dyadic rationals (denominators `2^k`), with
additivity `N(a,b)=N(a,m)+N(m,b)` asserted and checked at every split and
`P_n(m)≠0` checked (no rational roots possible: monic, constant 1, `±1`
are not roots since `P_n(±1)=1` or `-1` as logged), isolates each root in
width `≤1/10^10`. Each final interval has Sturm count 1 and endpoint sign
change `P_n(a)P_n(b)<0` (exact, independently rechecked). Disjointness is by
construction (sorted, non-overlapping). Full subdivision logs in
`artifacts/sturm.log` (iters 70,101,163,281).

## 3. Center polynomials (exact)

- `P_1=c`, `P_2=c+1`, `P_3=c^3+2c^2+c+1`.
- `P_4=c^6+3c^5+3c^4+3c^3+2c^2+1`.
- `P_5=c^15+8c^14+28c^13+60c^12+94c^11+116c^10+114c^9+94c^8+69c^7+44c^6+26c^5+14c^4+5c^3+2c^2+c+1`.
- `P_6=c^27+13c^26+78c^25+293c^24+792c^23+1672c^22+2892c^21+4219c^20+5313c^19+5892c^18+5843c^17+5258c^16+4346c^15+3310c^14+2331c^13+1525c^12+927c^11+536c^10+298c^9+155c^8+76c^7+35c^6+17c^5+7c^4+3c^3+c^2-c+1`.
- `P_7=c^63+32c^62+496c^61+4976c^60+36440c^59+208336c^58+971272c^57+3807704c^56+12843980c^55+37945904c^54+99582920c^53+234813592c^52+502196500c^51+981900168c^50+1766948340c^49+2943492972c^48+4562339774c^47+6609143792c^46+8984070856c^45+11500901864c^44+13910043524c^43+15941684776c^42+17357937708c^41+17999433372c^40+17813777994c^39+16859410792c^38+15286065700c^37+13299362332c^36+11120136162c^35+8948546308c^34+6939692682c^33+5193067630c^32+3754272037c^31+2625062128c^30+1777171560c^29+1166067016c^28+742179284c^27+458591432c^26+275276716c^25+160617860c^24+91143114c^23+50323496c^22+27049196c^21+14162220c^20+7228014c^19+3598964c^18+1749654c^17+831014c^16+385741c^15+175048c^14+77684c^13+33708c^12+14290c^11+5916c^10+2398c^9+950c^8+365c^7+132c^6+42c^5+14c^4+5c^3+2c^2+c+1`.
Full integer lists in `artifacts/polys.json`. All divisions have remainder 0;
`P_n(0)=1`, `P_n(-2)=±1` as logged, so endpoints `±2,0` are never roots.

Factorization over Q: each `P_n` is irreducible (`factor_list` returns one
factor, mult 1; times 0.001–0.03 s). Hence it is the minimal polynomial of
each of its roots; root-to-factor map is trivial (all roots → the single
factor). Discriminants as in §1 (computed by `sympy.discriminant` in
0.002–0.014 s; `P_7` 376-bit). Nonzero ⇒ simple roots, consistent with
Sturm final constants:
`58673/1074528400` (n=4), large positive quotient (n=5), large negative
quotient (n=6), huge negative quotient (n=7) — see `artifacts/sturm.log`.

## 4. Isolating intervals (exact rationals, width ≤1e-10)

Format `[a,b]` exact Fractions, midpoint `m=(a+b)/2`, `w=1/17179869184≈5.82e-11`.
Decimals for human reading; certification uses Fractions.

n=4 (2):
- I0 `[-33342686789/17179869184, -8335671697/4294967296]` ≈ `[-1.940799806558,-1.940799806500]`, m≈-1.940799806529.
- I1 `[-11258849959/8589934592, -22517699917/17179869184]` ≈ `[-1.310702641378,-1.310702641320]`, m≈-1.310702641349.

n=5 (3):
- I0 `[-34109328943/17179869184, -17054664471/8589934592]` ≈ `[-1.985424253100,-1.985424253042]`.
- I1 `[-3996000039/2147483648, -31968000311/17179869184]` ≈ `[-1.860782522243,-1.860782522184]`.
- I2 `[-872637349/536870912, -27924395167/17179869184]` ≈ `[-1.625413725153,-1.625413725094]`.

n=6 (5):
- I0 `[-4287185111/2147483648, -34297480887/17179869184]` ≈ `[-1.996376137715,-1.996376137657]`.
- I1 `[-33788906573/17179869184, -8447226643/4294967296]` ≈ `[-1.966773216438,-1.966773216380]`.
- I2 `[-16383411231/8589934592, -32766822461/17179869184]` ≈ `[-1.907280091080,-1.907280091022]`.
- I3 `[-15229034079/8589934592, -30458068157/17179869184]` ≈ `[-1.772892903420,-1.772892903362]`.
- I4 `[-6339434619/4294967296, -25357738475/17179869184]` ≈ `[-1.476014642743,-1.476014642685]`.

n=7 (9):
- I0 `[-34344202309/17179869184, -8586050577/4294967296]` ≈ `[-1.999095682346,-1.999095682288]`.
- I1 `[-8554776731/4294967296, -34219106923/17179869184]` ≈ `[-1.991814172594,-1.991814172536]`.
- I2 `[-33967686659/17179869184, -16983843329/8589934592]` ≈ `[-1.977179587062,-1.977179587004]`.
- I3 `[-4195551461/2147483648, -33564411687/17179869184]` ≈ `[-1.953705894295,-1.953705894237]`.
- I4 `[-16554072773/8589934592, -33108145545/17179869184]` ≈ `[-1.927147709415,-1.927147709357]`.
- I5 `[-16190339399/8589934592, -32380678797/17179869184]` ≈ `[-1.884803571622,-1.884803571564]`.
- I6 `[-491858367/268435456, -31478935487/17179869184]` ≈ `[-1.832315202802,-1.832315202744]`.
- I7 `[-28760236457/17179869184, -3595029557/2147483648]` ≈ `[-1.674066091480,-1.674066091422]`.
- I8 `[-27056389401/17179869184, -3382048675/2147483648]` ≈ `[-1.574889139796,-1.574889139738]`, m=`-54112778801/34359738368`≈-1.574889139767.

Machine-readable: `artifacts/census.json` (Fractions as strings + `V` counts +
`sturm_len`). Each interval verified: Sturm count 1, `P_n(a)P_n(b)<0` exact,
disjoint, inside `[-2,0]`.

## 5. Kneading table (certified stable)

Convention: for exact center `c*`, `x_0=0`, `x_{k+1}=x_k^2+c*`, `x_n=0`,
`x_k≠0` (`k<n`). Symbol `k=1..n-1`: `-` if `x_k<0` (left), `+` if `>0`
(right). Published word is the length-`n-1` free word; full orbit adds
`x_0=x_n=0`. Stability: with `C=[a,b]`, `X_0=[0,0]`,
`X_{k+1}=X_k^2+C` in exact Fraction interval arithmetic (square of
straddling interval is `[0,max(l^2,u^2)]`), each `X_k` (`k<n`) is strictly
signed (does not contain 0), so every `c∈[a,b]` — in particular `c*` —
has the same word; `X_n∋0` as must hold (true image contains `F_n(c*)=0`).
Midpoint orbit (exact Fractions at `m`) matches interval word in all 19
cases; residuals `|F_n(m)|` range `2.5e-12`–`1.8e-08` (tolerance `1e-6`).
Log `artifacts/kneading.log`; machine table `artifacts/kneading.json`.

- n=4: I0 `-++`, I1 `-+-`.
- n=5: I0 `-+++`, I1 `-++-`, I2 `-+--`.
- n=6: I0 `-++++`, I1 `-+++-`, I2 `-++--`, I3 `-++-+`, I4 `-+---`.
- n=7: I0 `-+++++`, I1 `-++++-`, I2 `-+++--`, I3 `-+++-+`, I4 `-++--+`,
  I5 `-++---`, I6 `-++-+-`, I7 `-+--+-`, I8 `-+----`.
All words within each `n` are distinct. `X_n` widths `5.9e-10`–`2.0e-07`,
all contain 0; `X_k` (`k<n`) widths `≤~1e-8` except n=7 I0–I1 (still `≪`
distance to 0). Minimal `|x_k|` at midpoints is `0.105` (n=6 I3) and
otherwise `0.3`–`1.4`, so no accidental lower-period near-miss
(verifier threshold `0.01`).

## 6. Extremal witness (period 7, rightmost center)

Because `P_7` is irreducible, there is a single `|disc|` value; “minimal’’
is trivial — every period-7 center shares it. We publish the rightmost
(maximal-`c`) center as a canonical representative: it is the most separated
from `-2` and has the smallest `|F_7|` residual among n=7 mids.
Interval `I*_8=[-27056389401/17179869184, -3382048675/2147483648]`,
midpoint `c0=-54112778801/34359738368≈-1.574889139767038`.
Minimal polynomial `P_7` above, `disc` as in §1.

Midpoint orbit (exact rationals; floats for reading):
- `x0=0`
- `x1=-54112778801/34359738368≈-1.574889139767038`
- `x2=1068891907598138260833/1180591620717411303424≈0.905386662789122`
- `x3=-1052545178738574905109756068129967243239743/1393796574908163946345982392040522594123776≈-0.755164130610614`
- `x4≈-1.004616275606153` (exact Fraction in `artifacts/witness.json`)
- `x5≈-0.565635278554259`
- `x6≈-1.254945871421884`
- `x7≈4.318e-10` (exact Fraction numerator/denominator in witness file;
  `|x7|<1e-6`, consistent with `c0` approximating the true root to `~3e-11`).

Interval orbit `X_1..X_7` (exact Fractions in witness file; floats):
`X_1≈[-1.574889139796,-1.574889139738]`,
`X_2≈[0.905386662668,0.905386662910]`,
`X_3≈[-0.755164130858,-0.755164130363]`,
`X_4≈[-1.004616276010,-1.004616275203]`,
`X_5≈[-0.565635279394,-0.565635277715]`,
`X_6≈[-1.254945872401,-1.254945870443]`,
`X_7≈[-2.054e-09,2.918e-09]∋0`.
All `X_1..X_6` are strictly signed with word `-+----`; `X_7∋0`.
*What this proves.* The midpoint table itself does not prove `c0` is exact
(it is not — residual `4.3e-10`). The proof that the *interval* contains an
exact period-7 center is: Sturm count 1 in `I*_8` + sign change +
`gcd(P_7,P_1)=1` (so `c*≠0`, minimal period exactly 7, not 1) +
separability. Multiplier 0 follows abstractly: the cycle contains `0`,
where `f_c'=0`, so `∏2x_k=0`. Full exact Fractions in
`artifacts/witness.json`.

## 7. Independent verification

`artifacts/verifier.py` (stdlib only, no sympy) reads *only*
`polys.json`, `census.json`, `kneading.json`, `witness.json`, re-evaluates
everything with `Fraction` Horner + naive interval arithmetic (independent
code path), checks widths `≤1e-10`, containment in `[-2,0]`, disjointness,
`P_n(a)P_n(b)<0`, `|F_n(mid)|,|P_n(mid)|<1e-6` (observed max `1.8e-08`),
kneading equality, `min|x_k|>0.01` for `k<n`, interval stability and
`X_n∋0`, and witness orbit replay. Output `artifacts/verification.log`:
`ALL CHECKS PASSED` (19/19 intervals). To reproduce:
`python3 output/artifacts/verifier.py`; to regenerate:
`python3 output/derive.py`, `python3 output/census.py`,
`python3 output/kneading.py` (needs `sympy`; `census.py` exact bisection
dominates runtime, `<2 s` for n≤6, `~1 s` for n=7 Sturm + subdivision on
this machine; total well under a minute).

## 8. Limitations, uncertainty, and originality

- Scope is exactly periods 4–7 on the real line. No claim about `n≥8`
  (degrees `≥128`, Sturm/interval costs grow fast), complex centers, Galois
  groups, or external angles.
- “Kneading word’’ here means critical-orbit signs vs `0`; it coincides with
  the usual one-sided kneading for real quadratics but we do not prove
  admissibility/combinatorial classification — only certified sign stability.
- Discriminants are for the monic irreducible `P_n`; “lowest-|disc|’’ for
  n=7 is degenerate (single factor). We explicitly do *not* claim multiple
  period-7 factors or a discriminant ordering among distinct fields.
- Computations are exact (integers/Fractions) except `sympy.sturm`,
  `factor_list`, `discriminant`, `gcd`, whose algorithms are exact over QQ
  but treated as trusted libraries; the independent verifier avoids sympy
  entirely for the replay half. Floats appear only for human-readable
  decimals; all certificates use Fractions.
- Originality: structural dynatomic literature (smoothness/irreducibility of
  complex curves; `Y_1(n)` reduction; Hubbard-tree kneading combinatorics;
  effectivity of dynatomic cycles — see topic bibliography) proves theorems
  without shipping Sturm-certified real tables with minimal polynomials,
  discriminants, intervals and replay logs. The artifact here (counts
  2,3,5,9 + 19 disjoint `1e-10` intervals + 4 irreducible minimal polynomials
  + 19 stable kneading words + replayable witness + stdlib verifier) is, to
  our knowledge, not in those sources. We do not claim the polynomials
  themselves were previously unknown — only the closed certified package.
- Failure-mode avoided: unlike the 2D Hénon period-7 Krawczyk attempt
  (SCOPE-FAIL-20260907-010), this is 1D exact elimination + Sturm, with no
  interval-Newton/cone machinery; period-7 factorization succeeded (0.03 s),
  so the anticipated fallback (unfactored enclosures) was not needed.

## Artifacts

- `artifacts/polys.json` — `F_n,P_n` integer lists.
- `artifacts/census.json` — intervals (Fractions), Sturm `V` counts, lengths.
- `artifacts/kneading.json` — words + midpoints + `X_n`.
- `artifacts/witness.json` — period-7 `I*_8` full exact orbit + intervals.
- `artifacts/verifier.py`, `artifacts/verification.log` — independent replay.
- `artifacts/derive.log`, `artifacts/sturm.log`, `artifacts/kneading.log`,
  `artifacts/factor_disc.log` — generation logs (degrees, remainders,
  Sturm constants, discs, gcds, sign changes).
