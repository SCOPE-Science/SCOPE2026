# Exact ternary four-symbol permutation-burst maxima and maximizing-center counts

## Finding

Let \(\Sigma=\{0,1,2\}\). For every integer \(n\ge4\), let \(\mathcal B_4(x)\) contain all length-\(n\) words obtained from \(x\in\Sigma^n\) by arbitrarily permuting the symbols in **one contiguous window of exactly four positions**, without wraparound; the identity permutation is allowed. Put
\[
M_n=\max_{x\in\Sigma^n}|\mathcal B_4(x)|,\qquad
A_n=|\{x\in\Sigma^n:|\mathcal B_4(x)|=M_n\}|.
\]
Then
\[
\boxed{M_n=\begin{cases}
8n-18,&n\equiv0\pmod3,\\
8n-20,&n\equiv1\pmod3,\\
8n-19,&n\equiv2\pmod3,
\end{cases}}
\]
and
\[
\boxed{A_n=\begin{cases}
6,&n=3t,\ t\ge2,\\
3(t+2)(t+3),&n=3t+1,\ t\ge1,\\
6(t+2),&n=3t+2,\ t\ge1.
\end{cases}}
\]
These statements jointly give the exact maximum and the number of labeled maximizing input words at every admissible length, not just a finite-length census.

## Assumptions and scope

The alphabet has exactly three distinguishable symbols; every source word is counted separately, including global symbol relabelings. Windows have exactly four consecutive positions; an arbitrary permutation of those four symbols, including the identity, is allowed. Only one window is affected, and it cannot wrap around either end of the word. The maximum is over all \(3^n\) source words, with no composition restriction.

## Proof

**1. A non-overlapping count indexed by the first and last differences.** For \(v=(v_1,\ldots,v_m)\), \(2\le m\le4\), define
\[
T_m(v)=|\{w:\ w\text{ is a distinct multiset permutation of }v,
\ w_1\ne v_1,\ w_m\ne v_m\}|.
\]
For a word \(x\) of length at least four, every nonidentity output \(y\in\mathcal B_4(x)\) has a unique first changed coordinate \(i\) and last changed coordinate \(j\), with \(2\le j-i+1\le4\). The segment \(y_i\cdots y_j\) is a multiset permutation of \(x_i\cdots x_j\) changing both endpoints. Conversely, any such segment change can be implemented by a permutation of a four-position window containing the segment: such a window exists whenever \(n\ge4\), and the remaining symbols of that window are unchanged. Thus the sets for different \((i,j)\) are disjoint and
\[
|\mathcal B_4(x)|=1+\sum_{m=2}^{4}\sum_{i=1}^{n-m+1}T_m(x_i\cdots x_{i+m-1}).\tag{1}
\]
The values \(T_m\) are exact small-integer functions of a word's equality pattern. With \(c_a\) its symbol multiplicities, they are computable by inclusion-exclusion:
\[
T_m(v)=P(c)-P(c-e_{v_1})-P(c-e_{v_m})
+P(c-e_{v_1}-e_{v_m}),\tag{2}
\]
where \(P(d)=(\sum_a d_a)!/\prod_a d_a!\) when every component is nonnegative, and \(P(d)=0\) otherwise. This counts all distinct multiset permutations, subtracting those fixing the first or the last symbol and restoring those fixing both.

**2. Five equality classes and their exact transitions.** For a length-three suffix, replace its first new symbol by \(0\), its next new symbol by \(1\), and (if present) its third new symbol by \(2\). The five possible normalized suffix classes are `000`, `001`, `010`, `011`, `012`. Their numbers of actual labeled suffixes are respectively \(3,6,6,6,6\).

For a formal prefix of length three, set \(\Phi_3(x)=1+T_2(x_1x_2)+T_2(x_2x_3)+T_3(x_1x_2x_3)\). For longer words use the right-hand side of (1), so \(\Phi_n(x)=|\mathcal B_4(x)|\) whenever \(n\ge4\). Appending \(d\) to a prefix ending in \((a,b,c)\) adds precisely
\[
g(a,b,c,d)=T_2(c,d)+T_3(b,c,d)+T_4(a,b,c,d).\tag{3}
\]
Let \(F_n(s)\) be the largest \(\Phi_n\) among words of length \(n\) ending in the particular labeled suffix \(s\in\Sigma^3\), and let \(C_n(s)\) be the number of words attaining that suffix-specific maximum. Their exact recurrences are
\[
F_{n+1}(b,c,d)=\max_{a\in\Sigma}\big(F_n(a,b,c)+g(a,b,c,d)\big),\tag{4}
\]
\[
C_{n+1}(b,c,d)=\sum_{\substack{a\in\Sigma:\ F_n(a,b,c)+g(a,b,c,d)=F_{n+1}(b,c,d)}}C_n(a,b,c).\tag{5}
\]
For each normalized target suffix, the three predecessor options, as ordered by the preceding letter \(a=0,1,2\) of its canonical representative, have the following predecessor class and added weight. The entries follow directly from (2) and (3); they completely determine (4) and (5) by alphabet symmetry.

| Target suffix class | Predecessor at \(a=0\) | Predecessor at \(a=1\) | Predecessor at \(a=2\) |
|---|---|---|---|
| `000` | `000`: 0 | `011`: 1 | `011`: 1 |
| `001` | `000`: 3 | `011`: 3 | `011`: 9 |
| `010` | `001`: 1 | `010`: 3 | `012`: 6 |
| `011` | `001`: 3 | `010`: 1 | `012`: 6 |
| `012` | `001`: 9 | `010`: 9 | `012`: 6 |

The five \(F_3\) values, in the displayed suffix order, are \((1,3,3,3,6)\), and all their \(C_3\) values equal one. Substituting once into (4)–(5) gives \(F_4=(4,12,12,12,12)\) and \(C_4=(2,1,1,1,3)\).

**3. Exact all-length solution of the recurrences.** The next table specifies the suffix-specific maximum as \(M_n+\Delta\), together with its attaining count \(C_n\). Each cell displays \((\Delta,C_n)\). In the third row \(t\ge2\); in the other rows \(t\ge1\).

| Length | `000` | `001` | `010` | `011` | `012` |
|---|---|---|---|---|---|
| \(n=3t+1\) | \((-8,2t)\) | \((0,t)\) | \((0,1)\) | \((0,1)\) | \((0,\binom{t+2}{2})\) |
| \(n=3t+2\) | \((-8,2)\) | \((0,1)\) | \((-3,\binom{t+2}{2})\) | \((-3,\binom{t+2}{2})\) | \((0,t+1)\) |
| \(n=3t\) | \((-11,t(t+1))\) | \((-3,\binom{t+1}{2})\) | \((-3,t)\) | \((-3,t)\) | \((0,1)\) |

Here \(M_{3t+1}=24t-12\), \(M_{3t+2}=24t-3\), and \(M_{3t}=24t-18\). The first row holds for \(t=1\) by the explicit length-four calculation. To verify the inductive step, insert each of the five rows of the transition table into (4) and retain the maximizing predecessors. The maximum increments in the three successive transitions are respectively \(9,9,6\), and the new relative maxima are the next row's displayed deficits. For the counts, each target's contributing predecessors have the following classes (repeated classes indicate different preceding letters):

| Transition | Target `000` | `001` | `010` | `011` | `012` |
|---|---|---|---|---|---|
| \(3t+1\to3t+2\) | `011`, `011` | `011` | `012` | `012` | `001`, `010` |
| \(3t+2\to3t+3\) | `011`, `011` | `011` | `012` | `012` | `001` |
| \(3t\to3t+1\) | `011`, `011` | `011` | `012` | `012` | `001`, `010`, `012` |

For example, the last target in the final row has new count \(\binom{t+1}{2}+t+1=\binom{t+2}{2}\), while the first target in the middle row has count \(2\binom{t+2}{2}=(t+1)(t+2)\), as required for \(n=3(t+1)\). All other entries follow by direct substitution. This proves the table for every \(n\ge4\).

The maximum among the five suffix classes is exactly \(M_n\). There are six labeled suffixes in each nonconstant class, so the numbers of maximizing words are \(6\) at \(n=3t\), \(6[t+1+1+\binom{t+2}{2}]=3(t+2)(t+3)\) at \(n=3t+1\), and \(6[1+(t+1)]=6(t+2)\) at \(n=3t+2\). This establishes both formulas in the Finding.

## Verification

The accompanying standalone `verify.py` implements (2)–(5) with exact integer arithmetic. It checks the small transition table directly against multiset permutations, **symbolically verifies the three phases of the max-plus/tie-count induction as polynomial identities** using exact rational arithmetic, replays the five-class formulas to length \(300\), and independently enumerates **all \(88{,}533\) ternary source words at lengths \(4\) through \(10\)** by actually generating the channel outputs. The latter test does not use formula (1) to construct the output sets. These finite checks are independent cross-checks of, not substitutes for, the all-length induction above. Run `python3 verify.py` from the file directory to obtain `VERIFY_OK`.

## Relationship to prior work

Chen and Milenkovic (arXiv:2610.15701, first public 2026-10-11) introduce substring-permutation burst correction and use a first-changed-position sphere-count formula in the binary case, while explicitly leaving larger alphabets for future work. Here the channel is specialized to a **ternary** four-position window and the previously unoptimized *global maximum and exact maximizing-center multiplicity* are determined. In particular, a general formula for the sphere size of a specified word does not by itself settle the optimization over all words. Kovačević, Kiah and Goyal (arXiv:2509.06692, first public 2025-09-08) study disjoint adjacent swaps, a genuinely different output relation. Their results do not imply these four-position arbitrary-permutation extrema. For alphabets with at least four symbols, a length-four window may have four distinct letters; this simple construction is unavailable over the ternary alphabet, which explains the need for the five-state-type optimization and its period-three structure.

## Limitations

The formulas are specific to exactly one nonwrapping four-position permutation burst on three symbols. They do not classify the maximizing words as a language, give capacities or optimal code sizes, or extend automatically to other alphabet sizes or burst lengths. Historical priority beyond the identified and accessible sources cannot be guaranteed; the result has not undergone independent mathematical review.

## References

1. Y.-P. Chen and O. Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1, first public 2026-10-11, https://arxiv.org/html/2610.15701v1 .
2. M. Kovačević, H. M. Kiah, and K. Goyal, *Bounds on Codes Correcting Adjacent Transpositions*, arXiv:2509.06692v3, first public 2025-09-08, https://arxiv.org/html/2509.06692v3 .
