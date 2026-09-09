# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Girth-5 extremal ceilings at n = 54, 55, 56 (lane-340)

## 1. Objects and notation

For $n \ge 1$ let $a(n) = \mathrm{ex}_{\{C_3,C_4\}}(n)$ be the maximum number of
edges in a simple graph on $n$ vertices of girth at least 5 (no 3- or 4-cycles).
Write $d_v$ for the degree of vertex $v$ and $m$ for the edge count.

**External anchor (trusted, not re-derived).** We take as given the published
exact value
$$a(53) = 181$$
(OEIS A006856 with b-file through $n = 53$; McKay extremal-graph table).
All "conditional" ceilings below depend on this anchor; the Cauchy ceilings do not.

## 2. Results

**Theorem (unconditional, self-contained).** Every graph on $n$ vertices with no
$C_3$ and no $C_4$ satisfies $4m^2 \le n^2(n-1)$. Hence
$$a(54) \le 196, \qquad a(55) \le 202, \qquad a(56) \le 207.$$

**Theorem (conditional on the anchor $a(53) = 181$).** Monotone vertex-deletion
induction gives
$$a(54) \le 187, \qquad a(55) \le 194, \qquad a(56) \le 201.$$

**Witnesses (machine-checked).** Explicit girth-$\ge 5$ graphs in
`output/artifacts/graphs.json` have
$$L(54) = 184, \qquad L(55) = 188, \qquad L(56) = 188,$$
each verified $C_3$-free and $C_4$-free by the independent adjacency-list audit
in `output/artifacts/verify.py` (prints `VERIFY_OK`).

Consequently, with the anchor, the proved two-sided brackets are
$$a(54) \in [185, 187], \quad a(55) \in [189, 194], \quad a(56) \in [193, 201],$$
where the left endpoints are the OEIS-recorded lower bounds (cited, not
re-derived) and the right endpoints are proved here; unconditionally (without
the anchor) the right endpoints are $196/202/207$. Our own witnesses sit
$1$--$5$ edges below the recorded lower bounds (see limitations).

## 3. Proofs

### 3.1 Neighborhood lemma (girth $\ge 5$)

Fix $v$ and let $N(v)$ be its neighbor set, $d = d_v$.
No two vertices of $N(v)$ are adjacent (else a triangle with $v$), and no two
distinct $x, y \in N(v)$ share a common neighbor besides $v$ (else a 4-cycle
$x, v, y, w$). Hence the sets $N(x) \setminus \{v\}$ for $x \in N(v)$ are
pairwise disjoint subsets of $V \setminus (N(v) \cup \{v\})$, which has
$n - 1 - d$ vertices. Therefore
$$\sum_{x \in N(v)} (d_x - 1) \le n - 1 - d_v,
\qquad\text{i.e.}\qquad \sum_{x \in N(v)} d_x \le n - 1. \tag{1}$$

### 3.2 Unconditional Cauchy ceiling

Summing (1) over all $v$, each vertex $x$ contributes $d_x$ once for every
neighbor $v$, i.e.\ $d_x^2$ in total:
$$\sum_v d_v^2 \le n(n-1). \tag{2}$$
By Cauchy-Schwarz, $(2m)^2 = (\sum_v d_v)^2 \le n \sum_v d_v^2 \le n^2(n-1)$.
Since $4m^2 \le n^2(n-1)$ with integers, $m \le \lfloor \sqrt{n^2(n-1)}/2 \rfloor$:
- $n = 54$: $n^2(n-1) = 154548$, $392^2 = 153664 \le 154548 < 153661 = 393^2$... more precisely $4\cdot196^2=153664\le154548<155296=4\cdot197^2$, so $m\le196$.
- $n = 55$: $4\cdot202^2 = 163216 \le 163350 < 164836 = 4\cdot203^2$, so $m \le 202$.
- $n = 56$: $4\cdot207^2 = 171396 \le 172480 < 173056 = 4\cdot208^2$, so $m \le 207$.

Indeed $196 = \lfloor\mathrm{isqrt}(154548)/2\rfloor$ etc.; the script checks
$4m^2 \le n^2(n-1) < 4(m+1)^2$ in pure integer arithmetic.

### 3.3 Conditional anchored induction

**Lemma (monotone induction).** $a(n) \le \big\lfloor n\,a(n-1)/(n-2) \big\rfloor$.

*Proof.* Let $G$ be extremal on $n$ vertices with $a(n)$ edges, $n \ge 3$.
Summing edges of the $n$ vertex-deleted subgraphs $G - v$ counts each edge of
$G$ exactly $n - 2$ times, so $\sum_v e(G - v) = (n-2)\,a(n)$.
Each $G - v$ is girth-$\ge 5$ on $n - 1$ vertices, so $e(G - v) \le a(n-1)$;
thus $(n-2)\,a(n) \le n\,a(n-1)$, and integrality gives the floor. ∎

Applied from $a(53) = 181$ (integer divisions verified in `verify.py`):
- $a(54) \le \lfloor 54\cdot181/52 \rfloor = \lfloor 9774/52 \rfloor = 187$
  ($187\cdot52 = 9724 \le 9774 < 9776 = 188\cdot52$);
- $a(55) \le \lfloor 55\cdot187/53 \rfloor = \lfloor 10285/53 \rfloor = 194$
  ($194\cdot53 = 10282 \le 10285 < 10335 = 195\cdot53$);
- $a(56) \le \lfloor 56\cdot194/54 \rfloor = \lfloor 10864/54 \rfloor = 201$
  ($201\cdot54 = 10854 \le 10864 < 10908 = 202\cdot54$).

### 3.4 Witness verification

The audit in `verify.py` checks vertex counts, adjacency symmetry, no loops,
zero triangles (for every edge $ij$, $N(i) \cap N(j) = \varnothing$), and zero
4-cycles (for every pair $i < j$, $|N(i) \cap N(j)| \le 1$), then counts edges:
$184/188/188$ at $n = 54/55/56$.

## 4. How the witnesses were found (method, not proof)

Randomized maximal-girth-5 greedy completion with kick-and-refill perturbation
tens of thousands of iterations (see `scratch/`), starting from simulated
annealing outputs. Witness quality plateaued at $184/188/188$ across
$\sim$28k restarts, suggesting these maximal graphs are locally strong but not
extremal (recorded lower bounds $185/189/193$ stand).

## 5. Limitations and what is NOT claimed

- The ceilings $187/194/201$ are **conditional** on the trusted external anchor
  $a(53) = 181$; only $196/202/207$ are proved from scratch here.
- Our witnesses do **not** meet the recorded lower bounds $185/189/193$
  (short by $1/1/5$); we claim no new lower bound and no exact value.
- The KST-style bounds $210/216/222$ are a checked sanity side-result only.
- No claim about $n \notin \{54,55,56\}$, uniqueness, or extremal structure.

## 6. Replay

```
python3 output/artifacts/verify.py   # expect VERIFY_OK
```

Checks the KST inequalities (holds at $U$, fails at $U+1$), the three anchored
divisions, and the full $C_3/C_4$ audit plus edge counts of `graphs.json`.
Stdlib only, seconds-scale.
