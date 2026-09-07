# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact Davenport constant of \(C_3\times C_3\times C_6\) is \(10\)

## 1. Result

**Theorem.** Let \(G=\mathbb{Z}_3\times\mathbb{Z}_3\times\mathbb{Z}_6\)
(order \(54\), exponent \(6\), invariant factors \(3\mid 3\mid 6\)).
Then the Davenport constant \(D(G)=10\).

That is: (a) there exists a zero-sum-free sequence of length \(9\);
(b) every sequence of length \(10\) over \(G\) contains a nonempty
subsequence summing to \((0,0,0)\).

This closes the rank-3 mixed stratum entry \(C_3\times C_3\times C_6\)
(\(D^\star=10\)): the lower bound is tight. The sibling groups
\(C_3\times C_3\times C_7\cong C_3\times C_{21}\) and
\(C_3\times C_3\times C_8\cong C_3\times C_{24}\) collapse to rank 2
with closed formula \(D(C_m\times C_n)=m+n-1\); only \(n=6\) preserves
rank 3, so the choice is structural, not parametric.

## 2. Group setup

Write elements as \((a,b,c)\), \(a,b\in\mathbb{Z}_3\), \(c\in\mathbb{Z}_6\),
addition componentwise. \(|G|=3\cdot3\cdot6=54\), \(\exp(G)=\mathrm{lcm}(3,3,6)=6\).

Element orders (verified in `verify.py`): one identity, one element of
order \(2\), namely \((0,0,3)\); \(26\) elements of order \(3\)
(\(c\in\{0,2,4\}\), not all zero); \(26\) elements of order \(6\).
The \(3\)-torsion \(\{c\in\{0,2,4\}\}\cong C_3^3\) (order 27) and the
\(2\)-torsion \(\{0,(0,0,3)\}\) are characteristic (defined by \(3g=0\)
resp. \(2\)-Sylow), so
\(\mathrm{Aut}(G)\cong GL(3,3)\) of order
\((27-1)(27-3)(27-9)=26\cdot24\cdot18=11232\),
with \(4\) orbits \(\{0\},\{(0,0,3)\}\), order-3 set, order-6 set.
Generators: \(e_1=(1,0,0)\) (order 3), \(e_2=(0,1,0)\) (order 3),
\(e_3=(0,0,1)\) (order 6), with
\(G=\langle e_1\rangle\oplus\langle e_2\rangle\oplus\langle e_3\rangle\).

Hence \(D^\star(G)=1+\sum(n_i-1)=1+(3-1)+(3-1)+(6-1)=10\),
so \(D(G)\ge 10\) in general. We exhibit the bound and prove it tight.

## 3. Lower bound: length-9 extremal witness

$$S = e_1^2\,e_2^2\,e_3^5
= [(1,0,0)^2,(0,1,0)^2,(0,0,1)^5],\qquad |S|=9.$$

**Lemma (textbook \(D^\star\) construction).**
\(S\) is zero-sum-free.

*Proof.* Any subsequence sum is \(ae_1+be_2+ce_3\) with
\(0\le a\le2,0\le b\le2,0\le c\le5\), not all zero.
By direct-sum decomposition this is zero iff each component is zero,
i.e. \(3\mid a,3\mid b,6\mid c\), forcing \(a=b=c=0\). ∎

Machine check: all \(2^9-1=511\) nonempty subsequence sums recomputed by
group arithmetic are nonzero (`witness.json`, `verification_table.csv`,
`verify.py`). The \(54\) distinct subsums including empty equal all of
\(G\), so \(S\) is maximal by inclusion (no single element can be
appended without creating a zero-sum), though this alone does not bound
length.

Thus \(D(G)\ge 10\).

## 4. Upper bound: no zero-sum-free sequence of length 10

### 4.1 Reduction to multisets

Zero-sum property depends only on the multiset of values, not their order.
Every sequence of length \(n\) has a unique sorted (nondecreasing) version
under any fixed total order on \(G\) (we use index
\((a\cdot3+b)\cdot6+c\)). The sorted version is zero-sum-free iff the
original is. Hence it suffices to enumerate multisets, breaking all
\(n!\) permutation symmetry. No automorphism reasoning is needed for
completeness (Aut would only further compress, unnecessary here).

### 4.2 Incremental subsum test

For a prefix with achievable-subsum set \(M\) (including empty \(0\)),
extending by \(g\) creates new subsums \(\{s+g:s\in M\}\).
A new nonempty zero-sum appears iff \(-g\in M\):
indeed any new zero-sum must use \(g\), writing \(0=s+g\) for some
\(s\in M\), i.e. \(s=-g\); conversely if \(-g\in M\) then that \(s\) plus
\(g\) is a zero-sum. Since the prefix was zero-sum-free, \(M\) contains
\(0\) only via empty, so for \(g\ne0\) the test \(-g\in M\) detects exactly
nonempty zero-sums using \(g\). Zero itself is excluded (singleton
zero-sum). Represent \(M\) as a 54-bit mask in one `uint64_t`
(max shift 53); extension is at most 54 ORs.

If a prefix already contains a zero-sum, every extension contains the same
witness, so the branch can be pruned safely. No zero-sum-free completion
is ever discarded.

### 4.3 Exhaustive run

`artifacts/enumerate.c` implements exactly this DFS over nondecreasing
index sequences using nonzero elements only. Deterministic,
single-threaded, no randomness, no external solver.

Result (one core, `gcc -O2`, a few seconds; logged in `enum_log.txt`):

```
depth 0: 1
depth 1: 53
depth 2: 1404
depth 3: 24310
depth 4: 297804
depth 5: 2545946
depth 6: 13495872
depth 7: 33541872
depth 8: 25255152
depth 9: 9723168
depth 10: 0
nodes=84885582 COMPLETE
```

Counts for \(n\le4\) agree with independent brute-force enumeration by
`combinations_with_replacement` plus \(2^n-1\) checks without the mask
trick (`verify.py`: 1404, 24310, 297804). Total \(84{,}885{,}582\) nodes
visited; depth-10 count \(0\) with `COMPLETE` (time limit not hit).

Therefore no zero-sum-free multiset of length \(10\) exists, hence no
zero-sum-free sequence of length \(10\) exists. So \(D(G)\le10\).

Combined with §3, \(D(G)=10=D^\star\).

### 4.4 Why not SAT/DRAT

The audit plan suggested SAT/ILP plus DRAT. We pivoted to direct
multiset backtracking because (i) no SAT solver was available
(stdlib-only plus `gcc` environment), (ii) the 54-bit-mask DFS is simpler
to audit than a CNF+DRAT chain and reruns in ~3 s (vs. minutes),
(iii) sorted enumeration already gives a complete certificate
(branch counts plus replay). The certificate is the program plus its
deterministic log, re-executed by `replay.sh`. Anyone can recompile and
rerun; correctness rests on the two lemmas above plus group arithmetic,
all checkable in the sources.

## 5. Reproducibility

Single command (stdlib Python + gcc, one core, <2 min, observed ~10 s):

```bash
bash output/artifacts/replay.sh
```

It runs `verify.py` (group, witness 511 checks, brute \(n\le4\) cross-checks),
compiles `enumerate.c` with `gcc -O2`, runs `./enumerate 600`, and asserts
`depth 10: 0` plus `COMPLETE`. Artifacts: `enumerate.c`, `verify.py`,
`witness.json`, `verification_table.csv` (511 rows), `enum_log.txt`,
`checksums.sha256`.

## 6. Relation to prior work (no originality overclaim)

- Textbook \(D^\star\) construction gives only the lower bound; the
  non-textbook direction is \(D\le10\) proved here by computation.
- Olson (1969) \(D=D^\star\) for \(p\)-groups covers \(C_3^3\) (\(D=7\))
  but not the mixed group \(C_2\times C_3^3\) (exponent 6, non-\(p\)).
- Rank-two formula \(D(C_m\times C_n)=m+n-1\) covers degenerate siblings
  \(C_3\times C_{21},C_3\times C_{24}\) but not rank-3 \(C_3\times C_3\times C_6\).
- Geroldinger–Grynkiewicz surveys give generic bounds and flag rank-3
  non-\(p\) entries as open; they supply no exact \(D(C_3\times C_3\times C_6)\).
- EGZ/Kemnitz–Reiher rank-\(\le2\) results (\(s(C_n)=2n-1\),
  \(s(C_n^2)=4n-3\)) do not close rank-3 Davenport.
- Heuristic pre-search (random greedy/annealing, ~40 restarts) never reached
  length 10 (best always exactly one zero-sum, often a triple of an
  order-3 element), motivating but not replacing the exhaustive proof.

## 7. Limitations and uncertainty

- Computer-assisted: the upper bound depends on correctness of
  `enumerate.c` (group tables, mask logic, DFS/pruning) and the
  completeness lemmas in §4.1–4.2. Mitigated by: tiny auditable source
  (~100 lines), independent brute cross-checks for \(n\le4\), two
  independent reruns with identical counts, and single-command replay.
- No DRAT-style proof log; the branch-count log plus source is the
  certificate. A fully formal (e.g. proof-assistant) certification is not
  provided.
- No classification of length-9 extremals beyond the single witness and
  the count \(9{,}723{,}168\) multisets; no EGZ constant \(s(G)\) determination
  (left open; product bound \(D\le14\) via \(C_2\times C_3^3\) two-block
  argument is strictly weaker than the computed \(10\)).
- Scope: exact value only for this group; no general rank-3 formula claimed.

## 8. What is proved vs. conjectured

- Proved: \(D(C_3\times C_3\times C_6)=10\) via witness plus complete
  length-10 multiset exhaustion.
- Computed evidence (not proof): heuristic landscape (length-10 best has
  exactly one zero-sum) and \(H=C_3^3\) two-disjoint experiments.
- Not claimed: originality of \(D^\star\) witness, general methods beyond
  this stratum, EGZ values, or length-9 classification.
