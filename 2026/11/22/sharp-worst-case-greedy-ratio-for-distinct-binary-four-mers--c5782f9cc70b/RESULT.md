# Sharp worst-case Greedy ratio for distinct binary four-mers

## Finding

Let \(S\) be any nonempty subset of the sixteen binary words of length four. Let \(\operatorname{OPT}(S)\) be the minimum length of a linear word containing every member of \(S\) as a contiguous factor, and let \(G(S)\) be the **maximum** possible output length of the ordinary maximum-overlap Greedy shortest-common-superstring procedure, allowing arbitrary legal tie resolution. Then

\[
\max_{\varnothing\ne S\subseteq\{0,1\}^4}\frac{G(S)}{\operatorname{OPT}(S)}=\frac{17}{11}.
\]

Precisely four labeled input sets attain equality, forming one orbit under reversal and binary complementation. A representative is

`0000`, `0001`, `0010`, `0011`, `0100`, `0101`, `1000`, `1010`.

For this set, a legal Greedy output of length \(17\) is `00001000100110101`, whereas a shortest common superstring of length \(11\) is `00101000011`.

## Assumptions and scope

All inputs are sets of **distinct** length-four words over the fixed alphabet \(\{0,1\}\); there are \(2^{16}-1=65535\) nonempty choices. For strings \(u,v\), let \(\operatorname{ov}(u,v)\) be the largest \(t\ge0\) for which the length-\(t\) suffix of \(u\) equals the length-\(t\) prefix of \(v\). Greedy repeatedly selects an **ordered** pair of different current components maximizing this overlap and replaces them by the overlap merge. At ties, every maximizing pair is permitted. No contained-string deletion step, reverse-complement orientation choice, or other modification of this Greedy model is allowed. Since all original strings have equal length and are distinct, none contains another.

## Proof

**Optimal value.** For a subset \(T\) of initial four-mers and final element \(j\in T\), define \(H(T,j)\) as the maximum overlap sum over Hamiltonian paths on \(T\) ending at \(j\). Initialize \(H(\{j\},j)=0\) and use

\[
H(T,j)=\max_{i\in T\setminus\{j\}}\bigl(H(T\setminus\{j\},i)+\operatorname{ov}(i,j)\bigr).
\]

For \(m=|T|\), the exact shortest-superstring length is

\[
\operatorname{OPT}(T)=4m-\max_{j\in T}H(T,j).
\]

Indeed, any ordering produces a common superstring by overlap merging. Conversely, ordering one chosen occurrence of each length-four input by its start in an arbitrary common superstring gives a path whose maximum-overlap concatenation is no longer than that superstring. Thus the path recurrence is exact, not an approximation.

**Greedy value.** Use the established endpoint-overlap lemma for equal-length substring-free input (Chukhin–Kulikov–Mihajlin–Smal, 2026, Lemma 2.2): at every Greedy stage, the overlap of two distinct current components equals that between their rightmost and leftmost original words. Therefore a current component can be replaced, for purposes of *all future* overlap decisions, by the ordered pair \((\ell,r)\) of its first and last original words. Let \(P\) be the sorted multiset of these pairs. Define

\[
a(P)=\max_{i\ne j}\operatorname{ov}(r_i,\ell_j),\qquad F(P)=0\quad(|P|=1),
\]

and, for \(|P|\ge2\),

\[
F(P)=a(P)+\min_{\substack{i\ne j\\\operatorname{ov}(r_i,\ell_j)=a(P)}}
F\bigl((P\setminus\{i,j\})\cup\{(\ell_i,r_j)\}\bigr).
\]

All legal Greedy moves have overlap \(a(P)\); minimizing the future total overlap sum maximizes final length. If \(P_S=\{(s,s):s\in S\}\), induction on component count gives the exact worst-case length

\[
G(S)=4|S|-F(P_S).
\]

The recurrence includes zero-overlap merges, ordered directions, ties, repeated endpoint-pair states and every intermediate component size. Its keys are canonical sorted byte lists, and memoization changes no transitions. It is exhaustive because each step reduces the number of components by exactly one.

**Complete finite certificate.** The standalone `verify_binary_four.cpp` implements both exact recurrences. Reversing every input and reversing the order of all subsequent merges preserves overlap lengths and the optimum; complementing every bit does likewise. Every subset therefore has the same ratio as the lexicographically smallest one of its four reversal/complement images. The verifier *enumerates* all \(65535\) nonempty masks, evaluates precisely the \(16959\) canonical orbit representatives, and finds that \(17/11\) is largest, with exactly one maximizing representative, encoded by mask `1343` (least significant bit corresponds to `0000`). Its orbit has masks `1343`, `5431`, `60584`, `64672`. All other canonical masks have strictly smaller ratios. Consequently these are the only four labeled equality cases. The verifier asserts these conclusions, rather than merely reporting sampled outcomes.

The exhibited eight-word input needs at least \(8+3=11\) symbols because a length-\(L\) word has at most \(L-3\) distinct length-four factors. The displayed length-eleven word proves that lower bound sharp. An independent literal-string Greedy recursion for this same input checks the worst output length \(17\) without relying on endpoint-pair compression.

## Verification

Compile and run `verify_binary_four.cpp` using a C++17 compiler and optimization (for example `c++ -std=c++17 -O3 verify_binary_four.cpp -o verify_binary_four && ./verify_binary_four`). It uses only the C++ standard library and exact integer comparisons; no random choices, numerical solvers, special libraries or external files are required. `output_binary_four.txt` records the result of an actual complete run. The verifier reports \(16959\) symmetry representatives, \(22055161\) newly computed recursive states across its memoization epochs and exactly four maximizing input masks. It also reconstructs legal Greedy and shortest-superstring witnesses and independently evaluates the worst Greedy output of the extremal eight-word set using the literal words themselves.

The complete finite search is a proof here because the theorem's domain contains exactly \(65535\) subsets, and both recurrences enumerate every legal continuation for each representative, using proved symmetry and endpoint invariance. No inference from random sampling or a timeout is made.

## Relationship to prior work

Kulikov, Savinov and Sluzhaev (CPM 2015) proved the general length-four Greedy upper ratio \(2\), which does not imply the sharp binary finite-alphabet ratio. Chukhin, Kulikov, Mihajlin and Smal (2026) determined the unrestricted-alphabet length-three ratio \(9/5\), and give the endpoint-overlap lemma used to reduce component states; neither result solves this binary length-four enumeration. Related small-cardinality binary four-mer results identify the first eight-word counterexamples to a ratio-\(3/2\) bound, but do not control sets of nine through sixteen input words. The present statement determines the global finite-alphabet optimum and all its equality cases.

## Limitations

This is an exact result only for a binary alphabet and input word length four. It makes no assertion about arbitrary alphabet size, larger fixed word length, random tie-breaking probabilities, or the universal Greedy approximation constant. The computer-assisted upper bound relies on the printed exhaustive recurrence and the cited endpoint-overlap lemma. An independently conducted audit has not been performed. A previously unindexed equivalent finite classification cannot be excluded solely by bibliographic searching.

## References

1. N. Chukhin, A. S. Kulikov, I. Mihajlin and A. Smal, *The Greedy Superstring Algorithm Achieves Ratio 2 for Strings of Length 6 Already*, first public version 20 August 2026, arXiv:2608.20018, https://arxiv.org/abs/2608.20018 . See Section 2, Lemma 2.2, and Sections 4–5.
2. A. S. Kulikov, S. Savinov and E. Sluzhaev, *Greedy Conjecture for Strings of Length 4*, CPM 2015, pp. 307–315, DOI:10.1007/978-3-319-19929-0_26. Public conference presentation: https://cpm.cs.helsinki.fi/cpm15/26_Kulikov.pdf .
3. G. Bernardini, H. Chen, G. Loukides, S. P. Pissis, L. Stougie and M. Sweering, *Making de Bruijn Graphs Eulerian*, CPM 2022, DOI:10.4230/LIPIcs.CPM.2022.12. Context on spectrum reconstruction; it does not classify Greedy tie outcomes.
