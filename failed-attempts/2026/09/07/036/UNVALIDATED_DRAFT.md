# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Triple-verified census of length-4 pattern-pair avoidance to n=9 and finite-n verification of Le's hard equivalences by a disjoint insertion-encoding route

Lane 55 — deterministic, stdlib-only, seed 55. No randomness in enumeration.

## 1. Objects and prior art (originality boundary)

Let $S_n$ be permutations of $[n]$. For $p\in S_4$, $\pi\in S_n$ *contains* $p$
if some $i_1<i_2<i_3<i_4$ has $(\pi_{i_1},\dots,\pi_{i_4})$ order-isomorphic to $p$.
$Av_n(p,q)=\{\pi\in S_n:\pi\text{ avoids }p\text{ and }q\}$,
$a_n(p,q)=|Av_n(p,q)|$, with $a_0=1$.

Symmetries reverse $r$, complement $c$, inverse $i$ generate the 8-element
dihedral-plus-inverse group. For unordered pairs $\{p,q\}$ they act
simultaneously: $g\cdot\{p,q\}=\{g(p),g(q)\}$. This trivially preserves $a_n$.

Prior art (not claimed as new):
- Le (E-JC 12(1) R25, 2005) completes the Wilf-classification of length-4 pairs
  by block bijections, including the hard equivalences
  $(1342,2143)\sim(3142,2341)$ and $(1342,3124)\sim(1243,2134)$, with a
  generating function for the former. No code or census shipped.
- Kremer–Shiu (Disc. Math. 268, 2003) gives finite transition matrices for a
  subset of pairs. No exhaustive census, no insertion tree, no brute replay.
- Bean et al. (arXiv:2312.07716) proves regular insertion encodings for
  height-$\le2$ POPs (rational GFs). Classical length-4 pairs are generally
  irregular, so no rationality is claimed here; we truncate to $n\le 9$.

What is new here (finite, auditable): the first triple-agreement census
(insertion-tree vs Lehmer-code vs brute) for *all* symmetry-distinct
length-4 pairs to $n=9$, with replay code, plus finite-$n$ confirmation of
Le's two hard equivalences by a disjoint method. We do **not** prove
Wilf-equivalence for all $n$ and do **not** exhibit a general insertion-code
bijection; an explicit attempt at a max-insertion active-site isomorphism is
documented as failing (Section 5). This is the stated fallback claim.

## 2. Symmetry reduction (proof)

$S_4$ has 24 elements, $\binom{24}{2}=276$ unordered distinct pairs.
Breadth-first closure under $\{r,c,i\}$ gives 7 single-pattern orbits of
sizes $2,2,2,2,4,4,8$ and, for simultaneous action on pairs, **56 canonical
representatives** with orbit-size distribution $4{\times}1+8{\times}2+24{\times}4+20{\times}8=276$.
Canonical rep = lexicographically minimal sorted pair in its orbit.
Verified: sum of orbit sizes $=276$; reps list in `artifacts/symmetry_map.json`.
Example: $(3142,2341)$ has canon $((1,4,3,2),(2,4,1,3))$, distinct from
$((1,3,4,2),(2,1,4,3))$, so the Le-hard target spans two symmetry classes.

## 3. Three independent counters (truncated at $n\le 9$)

All stdlib-only, deterministic, fixed seed 55 (no randomness; enumeration
orders fixed). Pattern matching in each method is textually distinct code.

**Method A — max-insertion generating tree (per-pair).**
Lemma (hereditary): if $\pi\in S_n$ avoids $p$ and $\sigma$ is $\pi$ with the
maximum $n$ deleted, then $\sigma$ avoids $p$. Proof: $\sigma$ (standardized)
is a pattern of $\pi$; pattern containment is transitive, so $\sigma\supset p
\Rightarrow\pi\supset p$; contrapositive gives the claim. Hence every
avoider at level $n$ has its parent in $Av_{n-1}$, and expanding each
$\sigma\in Av_{n-1}$ by inserting $n$ in the $n$ slots and keeping those
children that avoid (checking only quadruples containing the new $n$, since
all other quadruples lie in the avoiding parent) enumerates $Av_n$ exactly.
Active sites of $\sigma$ = slots whose child avoids; profile = histogram of
$|\text{active}(\sigma)|$. Checker A uses direct comparison-count ranks,
no lookup table. For $n<4$ all $n!$ perms avoid.

**Method B — Lehmer/factorial-code enumeration (insertion codes, truncated).**
Codes $c=(c_0,\dots,c_{n-1})$, $0\le c_i<n-i$, decode by
`rem=[1..n]; pi[i]=rem.pop(c[i])`, a bijection $C_n\to S_n$ enumerated by
odometer. Each decoded $\pi$ is tested on all $\binom{n}{4}$ quadruples via
an independent lookup table `TAB` built by comparison-count ranks
($r_a=1+(a>b)+(a>c)+(a>d)$, etc., mapped to 24 pattern ids). No pruning,
no rationality claim; "transfer-matrix" here means only finite-$n$ code
enumeration, consistent with irregularity of classical pairs.

**Method C — naive brute over `itertools.permutations` (third arbiter).**
$C$-level lexicographic generation of $n!$ perms, tested via a *separately
constructed* table `TABC` built by `sorted()+list.index` ranks. Early exit on
first forbidden quadruple. Complexity $O(n!\binom{n}{4})$ per pair.

Independence: distinct generators (max-insertion expansion vs factorial-code
odometer vs $C$-level permutations) and distinct checkers
(comparison-ranks inline vs comparison-built table vs sort-built table).
A shared bug producing identical false counts across all three is implausible;
moreover $a_4=22$ for all reps and $a_0..a_3=1,1,2,6$ are combinatorial
sanity checks ($24-2=22$ at $n=4$).

## 4. Result: triple-verified table and finite-n Le verification (computed evidence)

Run: `bash artifacts/replay.sh --nmax 9 --workers 32` (~15 s on 32 cores,
~150 s single-core). It recomputes all $56\times 10$ counts by A, B, C and
asserts $A{=}B{=}C$ per rep. **Result: 0 mismatches.** `counts.csv` SHA-256
`462554e9c873c4524ab86330794e02cb54f203530d0df8fadd7a28342180219c`.

Clustering by vectors $(a_0,\dots,a_9)$ gives **38 distinct vectors**
(stable from $n=8$ to $n=9$; no split at $n=9$). Sizes: one 10-class, one
5-class, one 4-class, two 2-classes including the Le pairs, rest singletons.
Full table in `artifacts/counts.csv`; per-pair A/B/C vectors in
`artifacts/countsABC.json`.

Target (computed, not proved for all $n$):
- $a(1342,2143)=a(1432,2413)=[1,1,2,6,22,88,368,1584,6968,31192]$.
  Since $(1432,2413)$ is the canon of $(3142,2341)$,
  $|Av_n(1342,2143)|=|Av_n(3142,2341)|$ for all $n\le 9$ by three agreeing
  methods. At $n=9$ both are $31192$.
- Le second: $a(1243,2134)=a(1342,3124)=[1,1,2,6,22,87,354,1459,6056,25252]$,
  both $25252$ at $n=9$.
- Sanity separation (matches prior SCOPE failure record for different pairs):
  $a(1234,1342)=[\dots,7584,34875]$ vs $a(1324,1432)=[\dots,7566,34676]$,
  diverging at $n=7$ by 1 and by 199 at $n=9$; they are correctly *not*
  merged. The minimized-automaton/$n\le14$ part of that record is not
  attempted here.

Conjecture (not claimed as theorem): the 38 finite-$n$ classes coincide with
Le's Wilf-classes. Uncertainty: equality to $n=9$ does not imply equality for
all $n$; only Le's proof gives the infinite statement. Our contribution is an
independent finite-$n$ certificate by a disjoint route.

## 5. Attempted insertion-code isomorphism: negative result (proof of failure for max-insertion)

We attempted a max-insertion active-site relabeling
$Av(1342,2143)\to Av(1432,2413)$: map $k$-th active site (left-to-right) to
$k$-th active site recursively. Machine check to $n\le 9$:
- Global active-site histograms coincide to $n=9$ (e.g. at $n=8$,
  $\{8{:}64,7{:}96,6{:}180,5{:}288,4{:}396,3{:}560\}$ in both), but
  left-to-right rank already fails at $n=4$: e.g. parent $(1,2,3)$ has
  children with mismatched arities in order, and parent $(2,3,1,4)$ has
  $4$ vs $3$ active sites across classes.
- Sorted-by-$(child\_arity,pos)$ rank also fails at $n=4$:
  parent $(2,3,1)$ has child-arity multisets $[4,4,5,5]$ vs $[3,4,5,5]$.
- Unordered max-insertion trees truncated to depth 6 are non-isomorphic
  (AHU hashing: 23 vs 25 subtree types; joint root types differ; level
  multisets differ at depths 0–4). Hence no recursive arity-preserving
  bijection of max-insertion trees exists to that depth.

So the envisioned "profile-preserving insertion-code relabeling" for
max-insertion does **not** exist; we report this honestly and do not claim
the target bijection. Other encodings (min-insertion, left-to-right) were not
exhaustively searched and remain open. Scripts `work/rankmap.py`,
`sortedmap.py`, `treeiso.py` document the checks (investigative, not in
`artifacts/`).

## 6. Limitations and replay

- Finite-$n$ only ($n\le 9$); $n=10$ ($3.6$M perms $\times56$) was not run.
- No general bijection, no generating function, no rationality/automaton claim.
- Correctness rests on three implementations; common-spec misunderstanding is
  mitigated by distinct code paths and $a_4$ sanity, but not formally proved.
- 38 classes are finite-$n$ clusters, not a proof of Wilf-classification;
  that classification remains Le's theorem.

Replay (stdlib only): `bash output/artifacts/replay.sh --nmax 9 --workers 32`
regenerates `counts.csv`/`countsABC.json`, asserts $A{=}B{=}C$, and checks the
two Le equalities. Deterministic; seed 55 unused for randomness (enumeration
is exhaustive).

## 7. Artifact inventory

`output/artifacts/`: `counts.csv` (56 reps $\times$ $a_0..a_9$),
`countsABC.json` (A/B/C vectors + Method-A profiles),
`symmetry_map.json` (276$\to$56 map), `methodA.py`, `methodB.py`,
`methodC.py`, `census_all.py`, `sym.py`, `replay.sh`.
