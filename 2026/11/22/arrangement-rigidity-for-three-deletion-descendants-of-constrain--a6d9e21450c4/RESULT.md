# Arrangement rigidity for three-deletion descendants of constrained binary words

## Finding

Let \(w\) be an indexed linear binary word of length \(n\ge3\) beginning with `10` and containing neither `00` nor `111` as a contiguous factor. Let \(\mathcal D_3(w)\) be the **set** of distinct words obtained by deleting exactly three indexed symbols. Write \(R\) for its number of maximal constant-symbol runs and \(H\) for its number of occurrences of `11` (equivalently its number of two-symbol runs). Let \(u\) and \(v\) indicate whether the penultimate and last runs, respectively, have length two. Then

\[
\boxed{|\mathcal D_3(w)|=\binom R3-(R-2)(R-3)+(2R-7)H+u-(R-5)v.}
\]

Thus the **order** of the two-symbol runs is irrelevant to this exact three-deletion count once \(R,H,u,v\) are fixed. It is not asserted that this holds outside the specified language.

For the standard finite Fibonacci words \(f_0=0\), \(f_1=1\), and \(f_m=f_{m-1}f_{m-2}\), define \(\mathrm{Fib}_0=0\), \(\mathrm{Fib}_1=1\), and \(\mathrm{Fib}_{j+2}=\mathrm{Fib}_{j+1}+\mathrm{Fib}_j\). For every \(m\ge3\), put

\[
\varepsilon_m=\mathbf 1_{\{m\text{ odd}\}},\quad R_m=2\mathrm{Fib}_{m-1}+\varepsilon_m,\quad H_m=\mathrm{Fib}_{m-2}-\varepsilon_m,\quad \eta_m=\mathbf1_{\{m\text{ even}\}}.
\]

Then the exact, all-depth Fibonacci specialization is

\[
\boxed{|\mathcal D_3(f_m)|=\binom{R_m}{3}-(R_m-2)(R_m-3)+(2R_m-7)H_m+\eta_m.}
\]

In particular, the values at \(m=3,4,5,6,7,8\) are \(1,4,22,104,578,2409\), and with \(\varphi=(1+\sqrt5)/2\),

\[
\lim_{m\to\infty}\frac{|\mathcal D_3(f_m)|}{\binom{|f_m|}{3}}=\frac{8}{\varphi^6}.
\]

## Assumptions and scope

The alphabet is the fixed, labeled alphabet \(\{0,1\}\). Positions are linear and indexed; deletion of different coordinate triples producing the same surviving word counts **once**. The empty string is allowed when exactly three positions of a three-symbol word are deleted. All factors in the restrictions are nonwrapping. Every admissible word starts in a single `1`-run followed by a single `0`-run; its runs alternate between `1` and `0`. Every `0`-run has length one, every `1`-run has length one or two, and runs of length two are never adjacent. The assumption \(n\ge3\) implies \(R\ge3\).

## Proof

**1. A distinct-subsequence update.** Let \(A_i(t)\) denote the number of distinct subsequences of length \(i-t\) of the prefix of length \(i\), with \(A_i(t)=0\) for lengths outside \(0,\ldots,i\), and \(A_i(0)=1\). When the symbol at position \(i\) last appeared at position \(p<i\), the standard partition by the final occurrence yields

\[
A_i(t)=A_{i-1}(t)+A_{i-1}(t-1)-A_{p-1}(t-i+p).
\]

The last term is zero if \(p\) is absent or its requested subsequence length is outside range. To see the subtraction, an output counted both as an old subsequence and as an old subsequence followed by the new symbol has a unique representation ending at the previous occurrence of that symbol; the prefix before \(p\) supplies exactly the subtracted class. This argument counts output *strings*, not deletion-position sets.

**2. Changes at successive runs.** Number the runs \(1,\ldots,R\). Put \(a_j=1\) when run \(j\) has length two and zero otherwise, \(H_j=\sum_{h\le j}a_h\). Then \(a_1=a_2=0\), all even-indexed \(a_j\) vanish, and \(a_ja_{j-1}=0\). Let \(B_j\) and \(C_j\) count two- and three-deletion descendants of the prefix through run \(j\), respectively. One has \(B_2=1\) and \(C_2=0\).

For a new run \(j\ge3\), its first symbol increases \(B\) by \(j-1-(1-a_{j-1})\), and its second symbol, if present, increases \(B\) by one. The initial `10` gives the boundary correction, so summing through \(j\ge2\) gives

\[
B_j=\binom j2-j+2+2H_j-a_j.
\]

For \(C\), the first symbol of run \(j\ge3\) increases the count by \(B_{j-1}\), minus \(j-3+a_{j-2}\) if the preceding run has length one, or minus one if that preceding run has length two. The expression \(j-3+a_{j-2}\) counts runs in the prefix preceding the previous occurrence of the new symbol. If run \(j\) has a second symbol, it adds a further \(j-2\) outputs, since the previous run then has length one. Hence

\[
C_j-C_{j-1}=B_{j-1}-(j-3+a_{j-2})(1-a_{j-1})-a_{j-1}+(j-2)a_j.
\]

Inserting the expression for \(B_{j-1}\), and using the absence of adjacent length-two runs, simplifies this to

\[
C_j-C_{j-1}=\binom{j-1}{2}-2j+6+2H_{j-1}+(j-5)a_{j-1}-a_{j-2}+(j-2)a_j.
\]

Summing from \(j=3\) to \(R\), the constant contribution is \(\binom R3-(R-2)(R-3)\). Every \(a_h\) with \(3\le h\le R-2\) has coefficient \(2R-7\); \(a_{R-1}\) has coefficient \(2R-6\), and \(a_R\) has coefficient \(R-2\). Therefore

\[
C_R=\binom R3-(R-2)(R-3)+(2R-7)H_R+a_{R-1}-(R-5)a_R,
\]

which is the asserted formula, with \(H_R=H\), \(u=a_{R-1}\), and \(v=a_R\).

**3. Fibonacci specialization.** Every \(f_m\) with \(m\ge2\) begins in `10`, avoids `00` and `111`, and ends in `10` when \(m\) is even and `01` when \(m\) is odd. These facts follow from \(f_m=f_{m-1}f_{m-2}\): the only new possible adjacent `11` at a join occurs at even \(m\). Writing \(H_m\) for the `11` count gives \(H_2=H_3=0\) and

\[
H_m=H_{m-1}+H_{m-2}+\mathbf1_{\{m\text{ even}\}},
\]

hence \(H_m=\mathrm{Fib}_{m-2}-\varepsilon_m\). As `11` pairs are nonoverlapping, \(R_m=|f_m|-H_m=2\mathrm{Fib}_{m-1}+\varepsilon_m\). The last run is a singleton, and the penultimate run has length two exactly at even depths \(m\ge4\) (the terminal blocks are `110` and `101` for even and odd depths, respectively). Substitution into the general formula proves the exact specialization.

Finally \(|f_m|=\mathrm{Fib}_{m+1}\) and \(R_m/|f_m|\to2/\varphi^2\). The other terms in the exact formula are at most quadratic in \(|f_m|\), whereas \(\binom{R_m}{3}\) is cubic, giving the asserted limit.

## Verification

The supplied standalone Python 3 checker `verify.py` compares the theorem against literal sets of surviving words for every qualifying binary word of lengths three through twenty (612 words). Independently, its greedy-subsequence automaton compares the Fibonacci specialization at depths three through seventeen against the structural formula. The checker reports `VERIFY_OK`. Finite checks corroborate the proof but do not replace its induction and telescoping identities.

## Relationship to prior work

Sloane's *On Single-Deletion-Correcting Codes* (arXiv:math/0207197v1, 2002), Section 5, proves a general two-deletion formula in terms of runs and finite differences, and explicitly notes that the analogous three-deletion problem is not simply governed by the same general derivative statistics. The theorem here is an exact three-deletion law for a **restricted** run language and a Fibonacci-word corollary; no general three-deletion solution is claimed. Bar-Lev, Etzion, and Yaakobi (2023) study fixed-length Levenshtein balls, general deletion-sphere bounds, and extremal sizes; their radius-one ball results do not entail this restricted source-wise three-deletion identity. Prior general upper/lower bounds permit many different values at fixed run count. A targeted literature and public-record search has not established an earlier equivalent of the precise restricted formula; that is not a proof of absolute novelty.

## Limitations

The result concerns exactly three arbitrary **linear** deletions from the specified restricted binary source language, and standard finite Fibonacci words only. It does not treat cyclic deletion equivalence, unrestricted binary words, arbitrary deletion counts, nor a deletion-correcting code capacity. The Fibonacci formula does not assert any extremal optimality. Its source-specific enumeration can be checked directly, but the novelty assessment remains conditional on indexed literature coverage; unindexed earlier specializations cannot be excluded by search alone.

## References

- N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, arXiv:math/0207197v1 (first public version 2002-07-22), https://arxiv.org/abs/math/0207197 .
- D. Bar-Lev, T. Etzion, E. Yaakobi, *On the Size of Balls and Anticodes of Small Diameter Under the Fixed-Length Levenshtein Metric*, IEEE Transactions on Information Theory 69 (2023), 2324–2341, https://doi.org/10.1109/TIT.2022.3227128 .
