# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# A certified non-periodicity lower bound for the open octal game 0.007 (Treblecross) through heap 200

## Abstract
Let 0.007 be the octal heap game (Treblecross: remove exactly 3 tokens from a
heap; the leftover may optionally be split in two). We compute its exact
Sprague–Grundy values $G(n)$ for $0 \le n \le 200$ by logged dynamic
programming directly from the octal rule, and prove: **no pair
$(q,p)$ with $0 \le q \le 100$ and $1 \le p \le 100$ is an eventual-periodicity
pair for the infinite sequence** — for each such pair we exhibit an explicit
failing index $n$ with $q \le n \le 200-p$ and $G(n) \ne G(n+p)$.
Consequently, if the infinite Grundy sequence is eventually periodic with
least preperiod $Q^*$ and least period $P^*$, then $Q^* > 100$ or $P^* > 100$.
All 10,100 pairs are excluded (zero survivors), verified by an independent
replay script (`VERIFY_OK`).

## 1. Definitions
Heap game 0.007: from a heap of size $n \ge 3$, the options are the heap
$n-3$ (no split) or a pair $(i, n-3-i)$, $0 \le i \le n-3$ (split the
remainder; part $0$ means that side vanishes). Heaps $0,1,2$ have no moves.
Grundy numbers: $G(0)=G(1)=G(2)=0$, $G(3)=\mathrm{mex}\{G(0)\}=1$, and for
$n > 3$,
$$R(n)=\{G(n-3)\}\cup\{G(i)\oplus G(n-3-i):0\le i\le n-3\},\quad
  G(n)=\mathrm{mex}\,R(n).$$

A pair $(q,p)$ with $q\ge 0$, $p\ge 1$ is an *eventual-periodicity pair* for
the infinite sequence if $G(n)=G(n+p)$ for **all** $n\ge q$.
A *failing witness* for $(q,p)$ within computed range $N$ is an index $n$
with $q\le n\le N-p$ and $G(n)\ne G(n+p)$; one such $n$ refutes $(q,p)$
as an eventual-periodicity pair of the infinite sequence, since infinite
$(q,p)$-periodicity would require equality at $n$ in particular.

## 2. Theorem (certified exclusion bound)
Let $G(n)$ be as above and $N=200$. For **every** $(q,p)$ with
$0\le q\le 100$, $1\le p\le 100$ there exists $n$, $q\le n\le 200-p$,
with $G(n)\ne G(n+p)$.
Hence no such $(q,p)$ is an eventual-periodicity pair; if the infinite
sequence is eventually periodic with least preperiod $Q^*$ and least
period $P^*$, then $Q^*>100$ or $P^*>100$.

*Remark on scope.* This is a finite falsification certificate on $[0,200]$:
it rules out the stated box only. It does not prove (or disprove) eventual
periodicity itself, nor bound parameters outside the box. The tight-corner
pair $(100,100)$ is tested at the single index $n=100$ ($G(100)=0\ne
12=G(200)$); every other pair in the box has at least two test indices.

## 3. Proof and computation
**Step 1 — DP.** `artifacts/compute_grundy.py` (stdlib only, deterministic,
no randomness) computes $G(0..200)$ by the recurrence above in $O(N^2)$
xor/mex operations and writes `grundy_007_N200.csv`. Result: max value 17
(attained at $n=177,198$); prefix string for $n=0..15$ is `0001112203311104`,
agreeing with the published Flammenkamp prefix (used only as a consistency
check, never as proof source).

**Step 2 — scan.** `artifacts/scan_box.py` loads the CSV and, for each of
the $101\times 100=10{,}100$ pairs, records the *least* failing index $n$
with $G(n)\ne G(n+p)$ ($q\le n\le 200-p$), writing
`witnesses_Q100_P100.csv` ($q,p,n,G(n),G(n+p)$). Outcome: 10,100 excluded,
0 survivors. Spot witnesses: $(0,1)$ fails at $n=2$ ($0\ne1$); $(0,12)$
at $n=0$ ($0\ne1$); $(0,34)$ at $n=1$ ($0\ne1$); $(52,34)$ at $n=52$
($7\ne8$); $(100,100)$ at $n=100$ ($0\ne12$); $(100,1)$ at $n=100$
($0\ne11$); $(0,100)$ at $n=1$ ($0\ne11$). Note $q+p\le 200$ for every
pair in the box, so each pair has $\ge 1$ test index.

**Step 3 — independent verification.** `artifacts/verify.py` recomputes
$G(0..200)$ with an independently structured loop, checks the CSV
entry-by-entry, replays every witness ($q\le n\le 200-p$,
$G(n)=g_n$, $G(n+p)=g_{np}$, $g_n\ne g_{np}$), and asserts exact coverage
of all 10,100 pairs plus the corner case. Result: `VERIFY_OK`.
SHA256: grundy CSV
`97bf087c6065afd8edd288f5a7ee128ba74a6df1b3d097e59e7c550342cac615`;
witnesses CSV
`781223418c0a411a43c3d3c746ccb3bc48e9fdcfc9c14aab27bd99c30747e684`
(see `artifacts/verification_log.txt`).
Replay: `python3 artifacts/compute_grundy.py && python3 artifacts/scan_box.py
&& python3 artifacts/verify.py`.

## 4. Exact table $G(0..200)$
```
n:   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
G:   0  0  0  1  1  1  2  2  0  3  3  1  1  1  0  4  3  3  3  2
n:  20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39
G:   2  2  4  4  0  5  5  2  2  2  3  3  0  5  0  1  1  1  3  3
n:  40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59
G:   3  5  6  4  4  1  0  5  5  6  6  2  7  7  7  8  0  1  9  2
n:  60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79
G:   7  2  3  3  3  9  0  5  4  4  8  6  6  2  7  1  1  1  0  5
n:  80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99
G:   5  9  3  1  8  2  8  5  0  1  1 12  2  2  7  3  3  9  4  4
n: 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119
G:   0  11  3  3  3  9  2  2  8  1  3  5  0  9 12  2  6 13 13  5
n: 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139
G:   0  1  1  4 11  7  7 10  3  4  1  4  0  5  0  3  3  6  7  2
n: 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159
G:  14 13 10  4 12  9  2  2  3  3  6  9  9  1 16  4  8  3  3  2
n: 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179
G:  15  1  1  4  0  5  5 16  6  6  6  8  0 16  5  4  4 17  2  2
n: 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200
G:   7  14  6 10 12  1  0 16 13  3  6  2  7  7  8  1  0  5 17  2 12
```
P-positions ($G=0$) on $[0,200]$ (22 total):
0, 1, 2, 8, 14, 24, 32, 34, 46, 56, 66, 78, 88, 100, 112, 120, 132, 134,
164, 172, 186, 196.
Value distribution: 0:22, 1:26, 2:26, 3:28, 4:17, 5:17, 6:13, 7:12, 8:8,
9:9, 10:3, 11:2, 12:5, 13:4, 14:2, 15:1, 16:4, 17:2.

## 5. Originality and relation to prior work
- Flammenkamp's octal tables list .007 with blank period/preperiod (no
  proved period) despite computation past $10^9$; OEIS A071426 gives bare
  values only. Neither states a Guy–Smith exclusion bound with per-pair
  failing witnesses — the theorem here is new (per admission live review).
- Guy–Smith (1956) supplies the method (window lemma); Gangolli–Plambeck
  (1989) closes only specific codes, not .007. This note applies direct
  refutation witnesses, not the Guy–Smith closure direction.
- No closed formula exists for .007; the bound is proved from the logged
  DP plus new witnesses, not copied from any database (Flammenkamp prefix
  used only as consistency check).

## 6. Limitations, conjecture, uncertainty
- Proved: exclusion of the $(Q,P)=(100,100)$ box on $[0,200]$ (machine-checked).
- Not proved: eventual periodicity or non-periodicity of .007 in general;
  any bound outside the stated box; minimality of witnesses (least failing
  $n$ recorded, but leastness is a scan artifact, not part of the claim).
- Uncertainty: none in the certificate itself (fully replayable); the
  open question of .007's eventual periodicity is untouched beyond this
  boundary lemma.
- Downstream use: citable exclusion lemma for the open-octal-periodicity
  program; regression test for CGT software (any correct .007
  implementation must reproduce the table and all witnesses).
