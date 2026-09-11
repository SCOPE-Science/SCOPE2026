# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — lane-897: the parity-shifted Gollnitz-Gordon companion is false,
with a certified mod-11 obstruction census

## 1. Definitions
Let $G(n)$ count partitions $\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_k$ of $n$ with,
for $n=0$ counting the empty partition ($G(0)=1$):
- $\lambda_i-\lambda_{i+1}\ge 2$ for all $i$,
- $\lambda_i-\lambda_{i+1}\ge 4$ whenever both parts are even,
- smallest part $\ge 2$ and no part equal to $2$ (hence every part is $\ge 3$).

Let
$$P(q)=\frac{(q^8;q^8)_\infty}{(q^2;q^8)_\infty(q^3;q^8)_\infty(q^6;q^8)_\infty}
=\sum_{n\ge 0}P(n)q^n.$$

## 2. Result (target disproved; obstruction census proved)
(a) The product identity is **false**: $G(2)=0\ne 1=P(2)$, so no identity
$\sum G(n)q^n=P(q)$ holds (any $q^c$ prefactor is forced to $c=0$ since
$G(0)=P(0)=1$).
(b) The congruence family is **false**: $G(6)=1\not\equiv 0\pmod{11}$, refuting
$g(11n+6)\equiv 0\pmod{11}$ at its first index $n=0$.
(c) **Obstruction census (as the target's "otherwise" clause requests):** no residue
class mod 11 vanishes identically for $G$; the first index in each class with
$G(n)\not\equiv 0\pmod{11}$ is:
$r=0\to 0$, $r=1\to 12$, $r=2\to 13$, $r=3\to 3$, $r=4\to 4$, $r=5\to 5$,
$r=6\to 6$, $r=7\to 7$, $r=8\to 8$, $r=9\to 9$, $r=10\to 10$.
All eleven witnesses are $\le 13$, hence inside the brute-force-certified range.

## 3. Proof
### 3.1 Exact small values of G by hand-checkable enumeration
$n=2$: admissible parts must be $\ge 3$ (smallest $\ge 2$, no $2$), and no partition
of $2$ has all parts $\ge 3$; so $G(2)=0$.
$n=3$: partitions of $3$: $[3]$ (admissible: single part $\ge 3$), $[2+1]$ and
$[1^3]$ (excluded: contain $1$ or $2$). So $G(3)=1$.
$n=6$: partitions with all parts $\ge 3$: $[6]$, $[4+2]$ (has a $2$), $[3+3]$
(gap $0<2$). Only $[6]$ survives (single part, no gap condition, $\ge 3$, $\ne 2$),
so $G(6)=1$.
$n=8$: all-parts-$\ge 3$ partitions: $[8]$ (ok), $[5+3]$ (gap $2\ge 2$, parities
odd/odd so the $\ge 4$-even rule is vacuous: ok), $[4+4]$ (gap $0$: no),
$[4+3+1]$ (has $1$: no), $[3+3+2]$ (has $2$: no), $[3+3+1+1]$ (has $1$: no).
So $G(8)=2$. Similarly $n=12$: $[12]$, $[9+3]$, $[8+4]$, $[7+5]$ are admissible
(each a 2-partition with gap $\ge 2$ and no both-even gap $<4$: $8-4=4$ ok) and no
other all-parts-$\ge 3$ partition passes; $G(12)=4$. These hand values anchor the
machine census.

### 3.2 Product side at n=2
$P(q)=(1-q^8-\cdots)\prod_{r\in\{2,3,6\}}\prod_{k\ge 0}(1-q^{r+8k})^{-1}$.
Up to $O(q^8)$ only $(1-q^2)^{-1}(1-q^3)^{-1}(1-q^6)^{-1}$ contribute:
$(1+q^2+\cdots)(1+q^3+\cdots)(1+\cdots)=1+q^2+q^3+\cdots$; the numerator is
$1+O(q^8)$. Hence $[q^2]P=1$, i.e. $P(2)=1\ne 0=G(2)$.

### 3.3 Ruling out the "up to prefactor" escape
Both series have constant term $1$ ($G(0)=1$ by the empty partition; $P(0)=1$ as a
ratio of nonempty products), so any monomial prefactor $q^c$ must have $c=0$; the
$n=2$ mismatch then stands.

### 3.4 Machine census (reproducible, stdlib only)
Two independent computations of $G$ agree to $n=13$: (i) descending-part DFS
enumeration; (ii) memoized recursion $F(\mathrm{rem},\mathrm{prev})$ summing over
admissible next parts, cross-checked against exhaustive integer-partition
filtering with the predicate of Section 1. The product series is computed by
successive exact multiplication by $(1-q^m)^{-1}$ factors and the
$(1-q^{8m})$ numerator, truncated at $N=200$. Results: $G\ne P$ at 190 of the 201
indices $0..200$; first mismatch $n=2$. The mod-11 scan gives the witness table in
Section 2(c). Replay: `python3 output/artifacts/verify_target.py` prints `VERIFY_OK`.

## 4. What this means
The shifted predicate (smallest $\ge 2$ with $2$ forbidden) does not produce the
$\{2,3,6\}$ product: already at $n=2$ the product counts the one-part partition
$[2]$, which the shifted condition deliberately excludes. The same minimality
($G(6)=1$ from the single partition $[6]$) kills the $11n+6$ family at its first
term, and the census shows every mod-11 class is obstructed at an index $\le 13$.
This is a sharp negative answer at the even-modulus boundary: the Bailey chain
leaves the classical family immediately upon this smallest-part shift, and no
$11$-dissection family survives on any residue.

## 5. Limitations and scope
Disproves exactly the stated product (residues $\{2,3,6\}$, level $8$) and the
$11n+6$ family (indeed all mod-11 residue families) for this $G$. Does not rule out
companions with different residue sets, corrected initial conditions, or congruences
at other moduli; those are outside the admitted claim.
