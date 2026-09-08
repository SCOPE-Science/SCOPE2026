# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# First exact enumeration of Av(4123,31524) to n=12, Wilf-separation from Av(4123,1324), and a certified growth interval

## 1. Objects and results

Let $C=\mathrm{Av}(4123,31524)$ (one length-4 plus one length-5 forbidden pattern).
Write $c_n=|C_n|$ with $c_0=1$ (empty permutation).

**Theorem (exact enumeration + separation + growth interval).**

- (a) The exact counts of $C$ are

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $c_n$ | 1 | 1 | 2 | 6 | 23 | 102 | 496 | 2569 | 13934 | 78295 | 452439 | 2674769 | 16115110 |

- (b) $C$ is not Wilf-equivalent to $A=\mathrm{Av}(4123,1324)$: with
  $a_n=|A_n|$ equal to $1,1,2,6,22,87,352,1428,5768$ for $n=0,\dots,8$,
  $c_4=23\ne 22=a_4$, so the classes already differ at $n=4$.
- (c) $C$ is sum-closed (both $4123$ and $31524$ are sum-indecomposable),
  hence $(c_n)$ is supermultiplicative and the Stanley–Wilf limit
  $\mu=\lim_n c_n^{1/n}$ exists (Marcus–Tardos gives finiteness).
  Moreover

$$3.986 \le \mu \le 9.$$

  The lower bound is the integer-arithmetic certificate
  $3986^{12} < 16115110\cdot 10^{36}$ (i.e. $3.986^{12} < c_{12}$);
  the upper bound is $c_n\le |\mathrm{Av}_n(4123)|\le 9^n$ (Regev bound
  for length-4 avoidance).

No prior enumeration, recurrence, generating function, or growth bound for
$\mathrm{Av}(4123,31524)$ is known (Miner arXiv:1610.01908 mentions $31524$
only as a typically-avoided remark inside $\mathrm{Av}(4123,1324)$); the
table, the $n=4$ separator, and the interval $[3.986,9]$ are new.

## 2. Method: insert-max generating tree (reproducible)

Every $\sigma\in S_n$ is obtained uniquely by deleting its maximum $n$;
conversely a child of $\pi\in S_{n-1}$ inserts $n$ at some position
$p\in\{0,\dots,n-1\}$. The tree levels are exactly the classes $C_n$
provided the child test is exact. New maximum $n$ can only create a
forbidden copy using $n$ as its largest entry:

- $4123$ has maximum first: a new $4123$ appears iff the suffix after $n$
  contains an increasing triple. Tested by 2-register patience
  ($\mathrm{LIS}\ge 3$), which never materializes the child.
- $31524$ has maximum last (value 5 at the final position): a new $31524$
  appears iff there are prefix indices $i_1<i_2<p$ with values
  $v_1,v_2$ and suffix indices $j_1<j_2$ (after $p$) with values
  $w_1,w_2$ satisfying $v_2<w_1<v_1<w_2$. Direct scan with a
  suffix-maximum pass and a prefix suffix-minimum array; also exact.

Both tests are local to the insertion and were validated three ways:

1. Program 1 (`enum_tree.py`): straightforward patience + pair loops;
2. Program 2 (`fast_tree.py`): optimized suffix-max/suffix-min scan —
   agrees with Program 1 on **every** tree node to $n=9$ (78295 nodes);
3. Program 3 (ad-hoc quadruple loop over $i_1<i_2$, $j_1<j_2$) — agrees
   with both on every tree node to $n=9$;
4. full symmetric-group brute force with an independent classical
   subsequence normalizer agrees with the tree counts for $n\le 8$
   ($40320$ permutations checked at $n=8$) for **both** classes.

Counts to $n=12$ ($c_{12}=16115110$ leaves, ~50 s single-core) come from
Program 1; Program 2 independently confirmed the table through $n=9$.

## 3. Proofs of (b) and (c)

**(b) Separation.** $4123$ is avoided by all $23$ non-$4123$ permutations
of $4$ but $1324$ itself is a permutation of $4$, so
$a_4 = 24-2 = 22$ while $c_4 = 24-1 = 23$. Machine enumeration confirms.

**(c) Sum-closure.** $\sigma\oplus\tau$ places all values of $\sigma$
below those of $\tau$. A copy of $4123$ with entries split across the
blocks would need its values $\{4,1,2,3\}$ split: entries in the left
block are all smaller, so the pattern's value-maximum $4$ and
value-minimum $1$ force all four entries into one block (a $4123$ copy
spanning blocks would normalize to a direct sum of two nonempty
patterns, but $4123$ is easily checked not to be such a sum — and
likewise $31524$). Hence $C$ is sum-closed, $c_{m+n}\ge c_m c_n$, and by
Fekete $\mu=\sup_n c_n^{1/n}$ exists (finite by Marcus–Tardos). The
interval follows from $c_{12}$ and $C\subseteq\mathrm{Av}(4123)$.

## 4. Status of the regularity target and what the data say

The target claim (regular insertion encoding, rational GF, growth exactly
$4$) is **not proved** and the computed evidence points the other way:
$c_{12}^{1/12}\approx 3.9866$ already nearly reaches $4$ from below while
$c_n/c_{n-1}$ is still increasing ($5.91$ at $n=11$, $6.02$ at $n=12$),
and $c_{12}=16115110$ is within 4% of $4^{12}=16777216$. Since $C$
strictly contains $\mathrm{Av}(4123,1324)$ (growth $4$) and Fekete gives
$\mu\ge 3.986$, the plausible truth is $\mu>4$, contradicting the
conjectured equality to $4$ — Miner's "typical avoidance" remark does not
lift to a growth coincidence. Regularity of the insertion encoding
remains open. This report therefore claims the fallback theorem above,
not the rational-GF target.

## 5. How to reproduce

- `output/artifacts/enum_tree.py` — Program 1 (reference tree counter).
- `output/artifacts/fast_tree.py` — Program 2 (independent fast checker).
- `output/artifacts/counts.json` — the exact tables.
- `output/artifacts/verify_bounds.py` — integer-arithmetic replay of the
  growth-interval certificates (no enumeration needed).

Replay: `python3 output/artifacts/enum_tree.py 9 31524` (seconds) and the
$n\le 8$ brute-force cross-check script in the worklog; the full $n=12$
run takes ~1 min single-core.
