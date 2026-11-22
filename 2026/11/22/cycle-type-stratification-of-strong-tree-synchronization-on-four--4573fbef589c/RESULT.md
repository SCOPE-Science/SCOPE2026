# Cycle-type stratification of strong tree synchronization on four states

## Finding

**Theorem (complete finite classification).** Let \(Q=\{0,1,2,3\}\). Consider every complete bottom-up tree automaton with precisely two positive-rank symbols: a unary transition \(w\colon Q\to Q\) that is a permutation and a commutative binary transition \(f\colon Q^2\to Q\) satisfying \(f(x,y)=f(y,x)\). A *full context* is a finite term whose leaves are distinct independent state variables (no constants). Its output set consists of evaluations over all leaf assignments. Its *strong reset height* \(h(f,w)\) is the smallest root-to-leaf height of a full context with singleton output, or \(\infty\) if none exists.

For each of the five cycle types of \(w\), the following vector gives the **exact number of labeled commutative operations** \(f\) realizing reset heights \(\infty,1,2,\ldots,11\), in that order. Each row sums to \(4^{10}=1,048,576\); entries for missing heights are zero.

| Cycle type of \(w\) | Representative \((w(0),w(1),w(2),w(3))\) | Histogram for heights \(\infty,1,\ldots,11\) | Maximum finite height |
| --- | --- | --- | ---: |
| \(1^4\) | \((0,1,2,3)\) | `1035528,4,2124,10920,0,0,0,0,0,0,0,0` | 3 |
| \(2\,1^2\) | \((1,0,2,3)\) | `1020908,4,2124,12160,7128,4916,1204,132,0,0,0,0` | 7 |
| \(2^2\) | \((1,0,3,2)\) | `1012112,4,2124,12664,7328,11080,2568,688,8,0,0,0` | 8 |
| \(3\,1\) | \((1,2,0,3)\) | `980154,4,2124,12780,11814,18279,10617,8640,3003,1104,57,0` | 10 |
| \(4\) | \((1,2,3,0)\) | `951360,4,2124,13032,11576,19672,17232,14360,10608,6568,1816,224` | 11 |

There are exactly **1,419,120** synchronizing labeled pairs \((f,w)\) among all \(24\cdot4^{10}=25,165,824\) eligible pairs. Exactly **1,344** pairs have strong reset height eleven; their unary transition must be a four-cycle. These 1,344 pairs form exactly **56 state-isomorphism classes**. In particular, restricting the binary operation to be commutative does *not* reduce the universal sharp four-state reset-height bound of eleven, but the unary cycle type imposes the strict sequence of maxima \(3,7,8,10,11\).

## Assumptions and scope

The state set is labeled and finite, all operations are total, and \(f\) is symmetric under interchange of its two inputs but need not be associative or idempotent. The unary transition is any element of the symmetric group on four states. There are no nullary symbols and every leaf is a fresh variable, so independent choices of input states are required at separate leaves. The counts are *labeled* except for the separately stated 56 isomorphism classes; no graph isomorphism reduction is made in the primary histograms.

## Proof

**Closure lemma.** For nonempty \(S,T\subseteq Q\), define \(w[S]=\{w(s):s\in S\}\) and \(f[S,T]=\{f(s,t):s\in S,t\in T\}\). Let \(\mathcal R_0=\{Q\}\) and recursively set
\[
\mathcal R_{r+1}=\mathcal R_r\cup\{w[S]:S\in\mathcal R_r\}\cup\{f[S,T]:S,T\in\mathcal R_r\}.
\]
Induction on term height, with disjoint fresh variable names for separate branches, proves that \(\mathcal R_r\) is precisely the set of images of all full contexts of height at most \(r\). A singleton in \(\mathcal R_r\) is therefore equivalent to a reset term of height at most \(r\). If \(\mathcal R_{r+1}=\mathcal R_r\), the family is closed under every operation and no further mask can appear. There are eleven nonempty nonsingleton subsets of a four-element set, including \(Q\) itself. Thus every synchronizing pair has \(h(f,w)\le11\); the closure through height eleven or stabilization decides the infinite-height case *exactly*.

**Exhaustive finite classification.** A commutative binary operation on four labeled states is completely specified by its ten values on
`(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)`.
Enumerate their base-four code from `0` to `1048575` inclusive. For each code and each of the five displayed unary permutations, encode each subset by the four-bit mask \(\sum_{i\in S}2^i\) and apply the closure lemma. The full source `verify_bfs.cpp` supplies a deterministic exhaustive implementation and checks every histogram cell. The independently structured `verify_relax.cpp` instead computes shortest derivation heights using increasing-cost label setting for unary images and commutative binary images. It obtains the same five twelve-entry histograms and sharp maxima. This is a finite exhaustive proof of the displayed census because the code covers all ten-digit base-four tables without omissions, uses complete Cartesian images, terminates with a mathematically justified bound, and checks a single first singleton per table. Its scope is the four-state universe, not a statistical sample or a claim for larger sizes.

**Conjugacy and the labeled total.** If \(g\) is a relabeling of \(Q\), conjugating \(w\) and simultaneously transporting \(f\) through \(g\) preserves all full-context images and their heights. Every permutation belongs to one of the five displayed conjugacy types, containing respectively \(1,6,3,8,6\) permutations. Hence multiplying each row's number of finite-height cases by its class size and summing gives 1,419,120; the last row gives \(6\cdot224=1,344\) height-eleven pairs.

**Exactly 56 extremal isomorphism classes.** A synchronizing four-cycle pair \((f,w)\) has no nonidentity state automorphism: any automorphism commuting with \(w\) belongs to the centralizer \(\langle w\rangle\), and each nonidentity member of this group is fixed-point free. Every output image of a full context is invariant under every automorphism of \((f,w)\), by induction on the term. If the image is a singleton, the automorphism must fix that state. Thus the stabilizer of every height-eleven pair under relabeling is trivial. Its labeled orbit has size \(4!=24\), giving \(1,344/24=56\) isomorphism classes.

**Concrete attaining commutative witness.** For \(w=(1,2,3,0)\), base-four operation code `739` (using the ten-pair digit order above) has

| \(f\) | 0 | 1 | 2 | 3 |
| :--- | ---: | ---: | ---: | ---: |
| 0 | 3 | 0 | 2 | 3 |
| 1 | 0 | 2 | 0 | 0 |
| 2 | 2 | 0 | 0 | 0 |
| 3 | 3 | 0 | 0 | 0 |

At successive heights \(0,1,\ldots,11\), its *only newly appearing* output masks are exactly
`15,13,11,7,14,5,10,9,3,6,12,1`.
In particular no singleton occurs before height eleven. Explicit terms with renamed distinct variables are obtained from \(T_0=x\) by
\[
\begin{aligned}
T_1&=f(T_0,T_0),&T_2&=w(T_1),&T_3&=w(T_2),&T_4&=w(T_3),\\
T_5&=f(T_4,T_4),&T_6&=w(T_5),&T_7&=f(T_5,T_6),&T_8&=w(T_7),\\
T_9&=w(T_8),&T_{10}&=w(T_9),&T_{11}&=f(T_9,T_{10}).
\end{aligned}
\]
Whenever a subterm is copied, its leaf variables are independently renamed. The output of \(T_{11}\) is \(\{0\}\). The exact mask certificate and derivation recipes are included in `witness.json` and replayed by `verify_witness.py`.

## Verification

Compile and execute both C++17 programs with, for example,

```sh
c++ -O3 -std=c++17 verify_bfs.cpp -o verify_bfs
./verify_bfs
c++ -O3 -std=c++17 verify_relax.cpp -o verify_relax
./verify_relax
python3 verify_witness.py
```

All three checks passed on the actual included sources. The complete outputs are in `bfs.out`, `relax.out`, and `witness.out`; no downloads, auxiliary libraries or random seeds are needed. The first program evaluates full Cartesian product images and height-layer closure; the second uses a separate label-setting recurrence for least achievable term height. Both traverse all \(5\cdot4^{10}\) representative operation pairs; the conjugacy argument accounts for all \(24\cdot4^{10}\) labeled pairs. Every integer count and sharpness assertion refers to exact finite enumeration.

## Relationship to prior work

Blažej, Janoušek and Plachý establish the strong full-context notion and universal bound \(2^n-n-1\) in general, including automata with many ranked symbols. Herrmann and Mörbitz (first posted 1 September 2026) prove large reset heights over one unary and one binary symbol via a Landau-function construction; the present finite classification is not a corollary of their asymptotic bounds. A previous published four-state construction exhibits height eleven with one unary and one binary symbol but uses a *noncommutative* binary table (for example its \(f(1,2)\) and \(f(2,1)\) differ), so it neither supplies a commutative extremizer nor gives the cycle-type histogram or 56-class count. The present claim is exclusively the complete restricted census and its consequences, not the previously established general height bound itself.

## Limitations

The result concerns four labeled states, commutative (but not necessarily associative) binary transitions, and permutation unary transitions only. It does not classify arbitrary unary transitions, noncommutative binary transitions, or automata with more than four states. Finite exhaustive verification proves this finite classification but gives no asymptotic law. The originality comparison is against the examined literature and available indexed research; an equivalent unindexed result remains possible, and no independent human review has been performed.

## References

1. L. Herrmann and R. Mörbitz, *On smallest synchronizing terms over constant alphabets*, arXiv:2609.01184 (first publicly posted 2026-09-01). https://arxiv.org/abs/2609.01184
2. V. Blažej, J. Janoušek and Š. Plachý, *On the Smallest Synchronizing Terms of Finite Tree Automata*, International Journal of Foundations of Computer Science 37 (2026), 215–239; first publicly available in earlier conference form (2023). https://doi.org/10.1142/S0129054125410096 ; open text: https://umu.diva-portal.org/smash/get/diva2%3A2007938/FULLTEXT01.pdf
3. *Sharp four-state tree synchronization over two ranked symbols*, publicly indexed four-state extremal construction, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-four-state-tree-synchronization-over-two-ranked-symbols--5734bc809a8e
