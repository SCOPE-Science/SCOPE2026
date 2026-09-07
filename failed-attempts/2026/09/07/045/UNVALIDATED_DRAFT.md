# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# The BKLC [36,10] gap: a machine-checkable Delsarte-dual + MacWilliams/residual
partial certificate for the [36,10,14] question

**Status: partial result (NO_RESULT on full nonexistence).** This note proves no
new nonexistence theorem. It delivers exactly what it claims: (a) a rigorously
verified Delsarte-dual upper bound for (n,d)=(36,14); (b) exact Griesmer data
showing textbook bounds do not decide the entry; (c) the complete LP-level
weight-multiplicity profile of a putative [36,10,14]; (d) a proved residual-branch
table; (e) an audit showing the Grassl shortening scaffold does not close the
case split. All computations replay in minutes with the archived numpy-only /
stdlib scripts. The gap itself remains OPEN.

## 1. Problem and table context (live-verified 2026-09-07)

Let d_max(36,10) be the largest d for which a binary linear [36,10,d] code exists.
Grassl's BKLC pages (re-fetched live for this work) state:

- **[36,10]: Lb=13, Ub=14 (OPEN).** Lb chain: BE [39,12,14] (Bierbrauer–Edel 1997)
  -> puncture [38,12,13] -> shorten [36,10,13]. Ub: shortening to Ub(33,7)=14,
  since otherwise adding a parity-check bit would contradict Ub(34,7)=15 (vT3 =
  van Tilborg 1981, smallest length of binary 7-dim codes).
- **[33,7]: Lb=Ub=14 (CLOSED)** via subcode of HY2 [33,8,14].
- **[34,7]: Lb=Ub=15 (CLOSED)** (vT3; DHM chain [36,8,16]->[35,8,15]->[34,7,15]).

No arXiv/table source found settles [36,10,14] (triage in topic.json: Li 2022
Delsarte-uniqueness is generic; Bouyukliev d=8/10 classifications are distant
parameters; half-rate-LP 2026 and LRC moment-LP papers touch no (36,10) entry).

## 2. What is proved here (precise statements)

**Proposition 1 (exact Griesmer audit).** With G(k,d)=sum_{i<k} ceil(d/2^i):
G(10,13)=32, G(10,14)=33, G(10,15)=35 (all <= 36); G(9,7)=19<=22, G(9,8)=20<=22;
G(9,6)=17, G(9,5)=16, G(9,4)=13, G(9,3)=12. *Proof.* Direct integer arithmetic;
replay `python3 griesmer.py`. *Consequence.* Griesmer permits [36,10,d] even for
d=15; textbook Griesmer/Plotkin levels cannot decide the entry.

**Proposition 2 (verified Delsarte-dual bound).** Every binary code of length 36
and distance >= 14 has size M <= 1 + 3192131922/10^6 = 3193.131922.
*Proof.* Delsarte dual: with K_k the binary Krawtchouk matrix, any y>=0 with
sum_k K_k(i) y_k <= -1 for all i in [14..36] gives M <= 1+sum_k C(36,k) y_k.
The archived vector Ynum/10^6 (sparse: k=1:549451, 2:211152, 3:73307, 4:17143,
5:3571, 31:237, 32:1131, 33:546; all other y_k=0) satisfies all 23 constraints
in EXACT integer arithmetic (min slack 3790, at i=26). Replay
`python3 verify_delsarte.py` (stdlib only; exit 0; re-derives Krawtchouk from
scratch). The float LP optimum is M<=3176.7273, so the rounded certificate
loses <1%. *Consequence.* Since 3193 > 1024, this does NOT rule out [36,10,14]:
an explicit, quantified non-closure (Delsarte is weak at this entry).

**Proposition 3 (LP weight-multiplicity profile).** For a putative [36,10,14]
with A_0=1, A_{1..13}=0, sum A=1024, B_j=2^{-10}sum_i K_j(i)A_i>=0, the per-weight
LP max/min (70 two-phase-simplex solves: 46 general + 24 even-subcase) are: every weight 14..36 allowed
(max >= 1 everywhere; only A_14 forced positive: min 54.55 general, 152.73 even
subcase); the even-weight subcase is LP-feasible with no weight forbidden
(maxima e.g. A_18<=486.5, A_20<=670.2, A_36<=1.0). Replay
`python3 macwilliams.py`. *Consequence.* MacWilliams-LP level does not eliminate
any weight; integer search is unconstrained at this level (hundreds of DoF).

**Lemma 4 (residual code).** Let C be binary linear [n,k,d] and c in C of weight t.
Let Res(C;c) be C punctured at supp(c) (delete those t coordinates).
(a) For EVERY nonzero y = x|_{outside supp(c)} in Res(C;c),
wt(y) >= d - t/2 (hence >= ceil(d-t/2)).
(b) If t = d (c has minimum weight), then dim Res(C;c) = EXACTLY k-1, so
Res(C;c) is a binary linear [n-d, k-1, >=ceil(d/2)] code.
(c) If t > d, then dim Res(C;c) <= k-1 (possibly strictly less); the
Griesmer-necessary condition G(k-1, ceil(d-t/2)) <= n-t remains valid (G is
increasing in dimension, so a smaller true dimension only weakens the required
inequality — no branch is wrongly discharged).
*Proof.* (a) For any x in C, wt(x)+wt(x+c) >= 2d. Writing w for wt of x on
supp(c): wt(x) = wt(y)+w, wt(x+c) = wt(y)+(t-w); summing gives
2wt(y)+t >= 2d, i.e. wt(y) >= d-t/2. (b) The puncture map has kernel
{x in C : supp(x) subset supp(c)}: any nonzero kernel word has weight <= t = d,
hence weight exactly d; supported in a d-set it must equal 1_{supp(c)} = c.
So ker = {0,c}, dim 1, and dim Res = k-1 exactly. (c) For t > d the kernel may
be larger, so dim Res <= k-1; monotonicity of G in k preserves the necessary
direction. All branches used here have t <= 23 < 28 = 2d.
*Computed corollary (exact).* For (n,k,d)=(36,10,14), every residual branch
t=14..23 is Griesmer-admissible: t=14 -> [22,9,>=7] G=19<=22 (exact-dim case);
t=15 -> [21,9,>=7] G=19<=21; t=16 -> [20,9,>=6] G=17<=20;
t=18 -> [18,9,>=5] G=16<=18; t=20 -> [16,9,>=4] G=13<=16;
t=22 -> [14,9,>=3] G=12<=14 (full table in survivors_log.txt).
*Consequence.* Residual+Griesmer eliminates NOTHING here.
(Self-correction note: an early draft of the table used ceil(t/2) as the
residual distance — valid only at t=d — and asserted dim exactly k-1 for all t.
Both were fixed by re-deriving (a)–(c) above; in particular the kernel={0,c}
argument is exact only at t=d, and the table now records (c) explicitly.)

**Proposition 5 (shortening-chain non-closure).** The children of a putative
[36,10,14] — one-coordinate shortenings ([35,9,>=14] or [35,10,>=13]-type) and
puncture [35,10,>=13] — are all unclassified by the cited closed entries
([33,7]=14, [34,7]=15); the vT3 scaffold Ub(33,7)/Ub(34,7) alone discharges no
branch. *Proof.* Inspection of the live pages: none lists these parameters;
Griesmer admits them (G(10,13)=32<=35). Recorded to block circular reasoning.

## 3. Computed evidence (not proofs of nonexistence)
- Float Delsarte LP optima: (36,14): 3176.7273; (36,13): 5256.9327;
  (36,15): 704.0; (36,16): 352.0; (33,14): 628.7719; (34,15): 215.2357;
  (22,7): 2048.0; (22,8): 1024.0 (all in delsarte_log.txt; optima are solver
  floats, only the DUAL bound of Prop. 2 is exact).
- LP weight profile: full min/max table in macwilliams_log.txt.
- Small-support integer DFS datum: on even support (14,18,20,22,24,28,36),
  40 (sum,S_1)-feasible raw vectors, 0 passing S_2,S_3,S_4 >= 0 + 0-mod-1024 —
  a scoping illustration only (support-restricted; NOT an elimination result).

## 4. Replay instructions (one CPU, minutes, no network, no proprietary code)
1. `python3 griesmer.py` — exact Griesmer table (stdlib). 2. `python3 simplex.py`
   + `python3 simplex2.py` — solver unit tests. 3. `python3 delsarte.py`
   (numpy only; ~1 min; writes delsarte_results.json + log). 4. `python3
   verify_delsarte.py` — MUST print VERIFY PASS with exit 0 (stdlib exact).
   5. `python3 macwilliams.py` (~2–4 min; 70 LP solves). 6. `python3
   survivors.py` + `python3 chain_audit.py` — residual table + chain audit.
   All paths are directory-local (run from `output/artifacts/`).

## 5. What remains (honest gap analysis)
Closing [36,10] needs strictly stronger machinery than deployed here:
classification of [22,9,7]-type residuals, higher-order (Terwilliger/SDP or
split-LP) hierarchies, or targeted backtracking with isomorph rejection —
each beyond the 2h single-CPU budget. The verified dual vector + LP profile +
residual table above are designed as reusable inputs to such an attack
(e.g. the Prop. 2 certificate warm-starts any LP/SDP hierarchy; Prop. 3 bounds
prune any enumerator search; Lemma 4 fixes the residual branch parameters).

## References
Grassl BKLC pages [36,10],[33,7],[34,7] (live 2026-09-07); Brouwer tables;
Bierbrauer–Edel 1997 (BE); van Tilborg 1981 (vT3); Helleseth–Ytrehus 1989 (HY2);
Dodunekov–Helleseth–Manev–Ytrehus 1987 (DHM); Hill residual/Griesmer theory;
Delsarte LP; Huffman–Pless; Li arXiv:2204.06090 (generic uniqueness, no entry
certificate); Bouyukliev et al. arXiv:1006.0109 (distant parameters).
