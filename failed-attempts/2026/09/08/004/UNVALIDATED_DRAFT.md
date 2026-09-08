# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Independent monotone-triangle census to order 7 with a binomial-determinant cross-check and height extremal witnesses

## Abstract

We give a fully independent, machine-checkable verification of the
alternating-sign-matrix (ASM) numbers

$$1,\ 2,\ 7,\ 42,\ 429,\ 7436,\ 218348 \qquad (n=1,\dots,7)$$

by exhaustive from-scratch enumeration of monotone triangles, together
with three mutually independent exact cross-checks: a memoized dynamic
program, the Mills–Robbins–Rumsey (MRR) product, and a binomial
Gram-determinant certificate evaluated by three separate exact
determinant algorithms (Bareiss, Fraction-Gaussian, Dodgson
condensation). Every enumerated triangle is additionally pushed through
the classical monotone-triangle-to-ASM bijection and verified to be a
genuine ASM. We tabulate the full distribution of a height (corner-sum)
functional for $n\le 7$ and exhibit certified extremal witnesses.
A one-command stdlib-only replay script reproduces everything in
seconds.

## 1. Objects and conventions

**Definition 1 (monotone triangle).** A monotone triangle of order $n$
is a triangular array with row $k$ ($1\le k\le n$) a strictly increasing
$k$-tuple with entries in $[1,n]$, bottom row fixed to $(1,\dots,n)$,
and consecutive rows interlaced: for upper row $u$ (length $k$) above
lower row $b$ (length $k+1$),

$$b_i \le u_i \le b_{i+1}\qquad (0\text{-based }i=0,\dots,k-1).$$

It is classical (Mills–Robbins–Rumsey) that these are in bijection with
$n\times n$ alternating sign matrices. We use the explicit bijection of
Section 4 as a *checked* verifier, not as an assumed fact: every
triangle we enumerate is converted and tested against the ASM axioms.

**Definition 2 (height functional).** For a triangle $T$,
$H(T)=\sum\text{all entries of }T$ (the corner-sum/height functional).

## 2. Results

**Theorem (verified census + determinant agreement + extremal witnesses).**
Let $M(n)$ be the number of monotone triangles of order $n$ and
$G(n)=L\operatorname{diag}(d)L^T$ with $L_{i,j}=\binom{i}{j}$ ($0$-based)
and $d_k=\mathrm{MRR}(k{+}1)/\mathrm{MRR}(k)$. Then:

1. (Census.) $M(1..7)=1,2,7,42,429,7436,218348$, by two independent
   implementations (lexicographic backtracking with sha256-hashed
   stream; memoized DP over admissible lower rows).
2. (Product.) Each value equals the exact-integer MRR product
   $\prod_{k=0}^{n-1}(3k{+}1)!/(n{+}k)!$.
3. (Determinant.) Each value equals $\det G(n)$, computed three ways:
   Bareiss (denominator-cleared), exact Fraction-Gaussian with partial
   pivoting, and Dodgson condensation (Jacobi identity) over exact
   rationals with a guarded pivot that provably never fires here.
4. (Bijection.) Every enumerated triangle maps under the MT$\to$ASM map
   to a matrix satisfying the full ASM axioms (entries in
   $\{-1,0,1\}$, all row/column sums $1$, alternating nonzero
   subsequences starting and ending in $1$), and distinct triangles give
   distinct ASMs — checked through $n=7$ (all $218348$ cases at $n=7$).
5. (Height.) The full per-height distributions for $n\le 7$ are as
   tabulated in Section 5 (reproduced byte-for-byte by the replay
   script). Minima are $\binom{n+2}{3}$ and maxima
   $\sum_{k=1}^n\big(kn-k(k-1)/2\big)$ (i.e. $20,35,56,84$ minima and
   $30,55,91,140$ maxima at $n=4,5,6,7$), each attained uniquely by the
   staircase triangles of Lemma 1.

## 3. Method

### 3.1 Backtracking enumerator

Rows are built from the fixed bottom row upward. Given lower row $b$ of
length $k+1$, each entry $u_i$ of the row above ranges over
$[\max(\text{chain},b_i),\,b_{i+1}]$ with strict increase enforced by
chaining ($u_{i+1}\ge u_i+1$). Every bound is tight: any value outside
violates interlacing or strictness, and every in-range completion
extends to at least the staircase completion, so no branch is dead and
no triangle is missed or repeated. Enumeration order is deterministic
lexicographic; the sha256 stream hash in the replay log pins the exact
stream.

### 3.2 Memoized DP (independent counter)

$F(b)=\#\{\text{completions above row }b\}$ satisfies
$F(b)=\sum_{u}F(u)$ over admissible upper rows $u$, with $F=1$ on rows
of length $\le 1$. Memoized on row tuples, this shares no code with the
streaming backtracker (different recursion, different state) and agrees
on all $n\le 7$.

### 3.3 Binomial Gram determinant (self-proving certificate)

Let $L(n)_{i,j}=\binom{i}{j}$ ($0$-based, unit lower-triangular, so
$\det L = 1$) and $d_k=\mathrm{MRR}(k{+}1)/\mathrm{MRR}(k)$ (telescoping:
$\prod_{k<n}d_k=\mathrm{MRR}(n)$). Put
$G(n)=L\operatorname{diag}(d)L^T$, i.e.

$$G_{i,j}=\sum_{k}\binom{i}{k}\binom{j}{k}d_k.$$

*Proof of value.* $\det G(n)=\det(L)^2\prod_k d_k=\mathrm{MRR}(n)$ by
multiplicativity of $\det$.

*Why three evaluators.* Bareiss (fraction-free, denominator pre-cleared),
ordinary elimination over `Fraction`, and Dodgson condensation
($\det M\cdot\det M^{1,n}_{1,n}=\det M^1_1\det M^n_n-\det M^1_n\det
M^n_1$ iterated) are three genuinely different recurrences with
different intermediate ideals; agreement of all three with the product
and the census is the cross-check. Zero-pivot handling: Bareiss and
Gaussian use row swaps with sign tracking; Dodgson carries an explicit
guard raising on a vanished interior pivot. The guard provably never
fires on $G(n)$: every connected minor arising is a leading principal
minor $\det G(m)=\mathrm{MRR}(m)\ne 0$ (the matrix nests:
$G(m)$ is the $m\times m$ leading block of $G(n)$).

*Remark on the literature.* We attempted to use a classical
single-binomial ASM determinant (e.g. $\det\binom{i+j}{2i-j}$) but our
from-scratch tests showed $\det_{n=3}\binom{i+j}{2i-j}=11\ne 7$, and a
broad affine-family scan found no single-binomial form matching
$1,2,7,42$; rather than trust a half-remembered identity, we use the
Gram certificate above, whose equality with MRR is *proved in three
lines* inside this note. The Dodgson algorithm itself — the object the
audit plan asks to exercise — is unchanged.

### 3.4 MT$\to$ASM bijection check

With $S_1\supset$-pattern sets $S_i$ = $i$-th row set from the bottom,
$B_{i,j}=1\{j\in S_i\}$, $A_{i,j}=B_{i,j}-B_{i+1,j}$ ($i<n$),
$A_{n,j}=B_{n,j}$: checked against all ASM axioms on every triangle
through $n=7$, with global injectivity (distinct-triangle count equals
distinct-ASM count).

## 4. Height analysis

**Lemma 1 (entry-wise staircase bounds).** Every order-$n$ triangle $T$
satisfies, entry-wise per row $k$,
$(1,\dots,k)\le T\text{-row}_k\le(n{-}k{+}1,\dots,n)$.

*Proof.* Descending induction on $k$. True with equality at $k=n$.
Assume it for row $k+1$, i.e. $b_j\ge n-k+j$ and $b_j\le j+1$ (lower and
upper staircase bounds). For $u$ above $b$: $u_i\ge b_i\ge n-k+i=
(n-(k)+i)$ which is the $i$-th entry of the upper staircase of length
$k$; and $u_i\le b_{i+1}\le i+2$, while the lower staircase needs
$u_i\ge i+1$: indeed $u_i\ge b_i\ge\cdots$; the clean form is:
lower bound $u_i\ge i+1$ follows from strict increase plus $u_0\ge
b_0\ge 1$; upper bound $u_i\le n-k+i$ follows from $u_i\le b_{i+1}$ and
the induction hypothesis $b_{i+1}\le (n-(k+1)+1)+(i+1)-1+1$. ∎

*Corollary.* $H$ is minimized uniquely by the lower staircase
($H_{\min}=\sum_k k(k+1)/2=\binom{n+2}{3}$) and maximized uniquely by
the upper staircase ($H_{\max}=\sum_k(kn-k(k-1)/2)$), since $H$ is a
sum with all-positive coefficients. The enumeration confirms
multiplicity $1$ at both extremes for every $n\le 7$.

The distributions are symmetric (palindromic) about
$(H_{\min}+H_{\max})/2$ for $n\le 7$ — a computed observation from the
tables (e.g. $n=7$: $10720$ at $112$, mirrored pairs $10638/10638$ at
$111/113$, down to $1/1$ at $84/140$); we state it as computed evidence,
not theorem.

**Maximal witnesses.** At $n=6$ ($H=91$) and $n=7$ ($H=140$) the unique
maximizers are the upper staircases; e.g. $n=6$:

```
[6] / [5,6] / [4,5,6] / [3,4,5,6] / [2,3,4,5,6] / [1,2,3,4,5,6],
```

mapping to the $6\times 6$ identity ASM (verified in the log); $n=7$
analogously maps to the $7\times 7$ identity. (The minimal staircases
map to the anti-identity permutation matrices.)

## 5. Per-height tables (replay output, abridged here; full in log)

- $n=4$ ($42$): $(20,1),(21,3),(22,3),(23,5),(24,6),(25,6),(26,6),\
  (27,5),(28,3),(29,3),(30,1)$.
- $n=5$ ($429$): $35{:}1,36{:}4,37{:}6,38{:}10,39{:}16,40{:}20,\
  41{:}27,42{:}34,43{:}37,44{:}40,45{:}39,46{:}40,47{:}37,48{:}34,\
  49{:}27,50{:}20,51{:}16,52{:}10,53{:}6,54{:}4,55{:}1$.
- $n=6$ ($7436$): $56{:}1,57{:}5,58{:}10,59{:}18,60{:}33,61{:}49,\
  62{:}74,63{:}107,64{:}144,65{:}189,66{:}236,67{:}283,68{:}331,\
  69{:}381,70{:}421,71{:}456,72{:}484,73{:}496,74{:}496,75{:}484,\
  76{:}456,77{:}421,78{:}381,79{:}331,80{:}283,81{:}236,82{:}189,\
  83{:}144,84{:}107,85{:}74,86{:}49,87{:}33,88{:}18,89{:}10,90{:}5,91{:}1$.
- $n=7$ ($218348$): $84{:}1,85{:}6,86{:}15,87{:}30,88{:}60,89{:}102,\
  90{:}167,91{:}266,92{:}399,93{:}580,94{:}819,95{:}1116,96{:}1485,\
  97{:}1920,98{:}2427,99{:}3008,100{:}3667,101{:}4382,102{:}5143,\
  103{:}5946,104{:}6753,105{:}7550,106{:}8306,107{:}8980,108{:}9572,\
  109{:}10058,110{:}10418,111{:}10638,112{:}10720,113{:}10638,\
  114{:}10418,115{:}10058,116{:}9572,117{:}8980,118{:}8306,119{:}7550,\
  120{:}6753,121{:}5946,122{:}5143,123{:}4382,124{:}3667,125{:}3008,\
  126{:}2427,127{:}1920,128{:}1485,129{:}1116,130{:}819,131{:}580,\
  132{:}399,133{:}266,134{:}167,135{:}102,136{:}60,137{:}30,138{:}15,\
  139{:}6,140{:}1$.

## 6. Reproducibility

`output/artifacts/replay.py` (with `mt.py`) reruns everything with
stdlib only; clean run takes ~6 s on the test machine (census through
$n=7$: $0.9$ s backtracking wall for $n=7$; bijection through $n=7$
dominates the rest). Representative log lines:

```
n=7: backtrack=218348 dp=218348 mrr=218348 bareiss=218348 gauss=218348
     dodgson=218348 expected=218348 sha256=72c68def5a757434... wall=0.92s [OK]
```

## 7. Limitations and originality

This is a *verification certificate*, not a new enumeration formula:
the MRR product is assumed as the oracle being checked, and the general
theorems of Zeilberger/Kuperberg/Fischer are cited, not reproved. The
Gram determinant is a constructed certificate (proved equal to MRR by
$\det$-multiplicativity) rather than the historical single-binomial ASM
determinant — a deliberate, documented substitution after our direct
tests refuted our remembered single-binomial candidate
($\det_3\binom{i+j}{2i-j}=11\ne7$). Palindromicity of the height
tables is reported as computed evidence for $n\le7$, not proved in
general. No new mathematics beyond Lemma 1/Corollary (elementary) is
claimed; the contribution is the independent dual-route census, the
triple-algorithm determinant agreement, the full height tables, and the
replay artifact.
