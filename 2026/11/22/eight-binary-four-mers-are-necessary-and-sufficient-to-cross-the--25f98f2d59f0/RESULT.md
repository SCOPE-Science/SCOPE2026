# Eight binary four-mers are necessary and sufficient to cross the greedy superstring \(3/2\) barrier

## Finding

Let \(\mathcal U=\{0,1\}^4\), and let \(S\) be any nonempty subset of \(\mathcal U\). Write \(L(S)\) for the minimum length of a linear string containing every member of \(S\) as a contiguous factor. Starting from the distinct strings in \(S\), repeatedly merge an ordered pair of different current strings with *maximum suffix-prefix overlap*, resolving ties arbitrarily, until one string remains. Write \(G(S)\) for the **maximum** possible final length over all legal tie resolutions.

**Theorem.** For every \(S\subseteq\mathcal U\) with \(1\le |S|\le7\),
\[
  G(S)/L(S)\le 3/2.
\]
Among the \(\binom{16}{8}=12870\) eight-element subsets, exactly four satisfy \(G(S)/L(S)>3/2\), and each of those four satisfies
\[
  (G(S),L(S))=(17,11),\qquad G(S)/L(S)=17/11.
\]
They constitute a single orbit under bit complementation and word reversal. A representative is
\[
 S_*=\{\mathtt{0000},\mathtt{0001},\mathtt{0010},\mathtt{0011},
        \mathtt{0100},\mathtt{0101},\mathtt{1000},\mathtt{1010}\}.
\]
Thus eight is the **smallest cardinality** of a distinct binary four-mer input for which maximum-overlap Greedy can exceed a factor of \(3/2\).

The maximum ratios within each input cardinality \(m\le8\), with the number of sets attaining the maximum for that cardinality, are:

| \(m\) | Maximal \(G(S)/L(S)\) | Number attaining maximum |
|---:|:---:|---:|
|1|\(4/4\)|16|
|2|\(5/5\)|120|
|3|\(9/6\)|2|
|4|\(10/7\)|6|
|5|\(13/9\)|2|
|6|\(16/11\)|2|
|7|\(15/10\)|12|
|8|\(17/11\)|4|

## Assumptions and scope

The input consists of a **set**, not a multiset: words are distinct, each has exactly four bits, the alphabet is the labeled binary alphabet, the target is a *linear* superstring, and overlaps are directed suffix-prefix overlaps (including zero). Greedy always merges until one string remains; every tie is legal. The cardinality-specific classification stops at eight input words. The threshold concerns the *number of input words* for fixed four-mer width, not the length of the finished string.

For words \(u,v\), define \(\operatorname{ov}(u,v)\) to be the maximum \(r\ge0\) such that the length-\(r\) suffix of \(u\) equals the length-\(r\) prefix of \(v\); merging produces \(u\odot v=u\) followed by the suffix of \(v\) beyond this overlap.

## Proof

**1. Endpoint reduction.** We use the equal-length endpoint property (also given as Lemma 2.2 in [1]). Here is a direct proof. Initially no current string is a factor of another, and the maximum overlap is at most three. Assume the noncontainment property before a merge \(z=x\odot y\) at global maximum overlap \(h\). If a third current string \(w\) occurs in \(z\), its occurrence cannot lie wholly in either copy of \(x\) or \(y\). It must therefore start strictly before the copy of \(y\) and end strictly after the copy of \(x\). The suffix of \(x\) from that start to the end of \(x\) is a prefix of \(w\) of length greater than \(h\), contradicting maximality. Conversely, \(z\) cannot be a factor of \(w\), since \(z\) contains \(x\). Hence noncontainment is preserved.

An overlap from \(w\) to \(z\) of length at least \(|x|\) would exhibit \(x\) as a factor of \(w\); every shorter overlap from \(w\) to \(z\) is also an overlap from \(w\) to \(x\) and has length at most \(h\). In the reverse direction an overlap from \(z\) to \(w\) of length at least \(|y|\) would exhibit \(y\) as a factor of \(w\); every shorter one is an overlap from \(y\) to \(w\). Thus no new overlap exceeds \(h\). Inductively all overlaps of distinct current strings are at most three. Each current string is formed from a directed path of original strings, with distinct paths partitioning \(S\); it begins and ends with the initial and terminal four-mers of its path. The overlap of distinct current strings therefore equals the overlap from the terminal four-mer of the left path to the initial four-mer of the right path. Merging paths with endpoints \((h_i,t_i)\) and \((h_j,t_j)\) leaves new endpoints \((h_i,t_j)\).

**2. Exact recurrence for the worst Greedy execution.** Given the current set of disjoint path endpoints \(P=\{(h_i,t_i)\}_{i=1}^r\), let \(D(P)\) be the *minimum* total overlap earned by future legal Greedy merges, because this maximizes the final length. For \(r=1\), \(D(P)=0\). For \(r\ge2\), set
\[
 H(P)=\max_{i\ne j}\operatorname{ov}(t_i,h_j).
\]
Then
\[
 D(P)=H(P)+\min_{\substack{i\ne j\\\operatorname{ov}(t_i,h_j)=H(P)}}
 D\!\left((P\setminus\{(h_i,t_i),(h_j,t_j)\})\cup\{(h_i,t_j)\}\right).
\]
With \(P_S=\{(s,s):s\in S\}\), the worst output length is exactly \(G(S)=4|S|-D(P_S)\). Every transition reduces the number of paths by one, so memoized recursion over all legal transitions is exhaustive and terminates.

**3. Exact recurrence for the optimum.** For nonempty \(T\subseteq S\) and \(j\in T\), let \(B(T,j)\) be the largest total consecutive overlap along a permutation of \(T\) ending at \(j\). The initialization is \(B(\{j\},j)=0\) and the transition is
\[
 B(T,j)=\max_{i\in T\setminus\{j\}}
       [B(T\setminus\{j\},i)+\operatorname{ov}(i,j)]
\]
when \(|T|>1\). Any such permutation gives a superstring by appending each successive four-mer with the overlap of the two consecutive original words. Conversely, choose one occurrence of each input word in any superstring and order their starting positions. If two consecutive starts have gap \(g<4\), the corresponding words overlap by at least \(4-g\); for \(g\ge4\) the zero overlap already suffices to place the next word at cost at most \(g\). Thus merging along this order costs at most the distance from first to last start, plus four for the first word, and is no longer than the given superstring. Consequently
\[
 L(S)=4|S|-\max_{j\in S}B(S,j).
\]

**4. Complete finite enumeration.** The 16 possible input words are indexed by their four-bit numerical value. Enumerating all \(\sum_{m=1}^{8}\binom{16}{m}=39202\) nonempty sets of cardinality at most eight gives the displayed table. The four eight-word exceptions are the sets indexed (as a bitmask of member indices) by `1343`, `5431`, `60584`, and `64672`. Those masks encode exactly the representative \(S_*\) and its images under reversal and complement. For every smaller cardinality the largest ratio is at most \(3/2\); at cardinality eight the only ratio strictly exceeding \(3/2\) is \(17/11\). The standalone complete checkers `check_endpoints.cpp` and `check_literals.cpp` implement distinct state representations and return the same rows and exception masks.

**5. Explicit sharpness witness.** The word `00101000011` contains all eight four-mers in \(S_*\) and has length eleven. Since a length-\(\ell\) word has at most \(\ell-3\) distinct length-four factors, any superstring of eight distinct four-mers has length at least eleven. Hence \(L(S_*)=11\). The following sequence is a legal Greedy tie-breaking execution (the overlap lengths are \(3,3,3,3,2,1,0\)):

```
0001 + 0010        -> 00010
00010 + 0100       -> 000100
1000 + 000100      -> 1000100
1010 + 0101        -> 10101
1000100 + 0011     -> 100010011
100010011 + 10101  -> 1000100110101
0000 + 1000100110101 -> 00001000100110101
```

The final word has length seventeen, and each selected pair has the maximum overlap among all ordered pairs present at that step. The finite recurrence proves no Greedy tie resolution can be longer. Reversal and bit complementation preserve shortest length and attainable Greedy length, proving the same sharpness for the other three exceptional sets.

## Verification

From a directory containing the two standalone source files:

```
g++ -O3 -std=c++17 check_endpoints.cpp -o check_endpoints
./check_endpoints 8
g++ -O3 -std=c++17 check_literals.cpp -o check_literals
./check_literals 8
```

The endpoint solver memoizes a path-cover recurrence and uses maximum-overlap Hamiltonian dynamic programming for the optimum. The literal-string solver enumerates Greedy merges on the actual full strings and computes optimum lengths using a separately written minimum-cost subset dynamic program. Both exhaust all \(39202\) sets and print all four exception masks, the eight per-cardinality ratios, and equality counts. The endpoint computation uses \(1443279\) memoized nonterminal states and the literal-string computation uses \(1703924\). Their output logs accompany the source code. The endpoint-proof correction does not change either implementation or the output data.

## Relationship to prior work

Chukhin, Kulikov, Mihajlin and Smal [1] prove the unrestricted-alphabet three-mer ratio \(9/5\) and give lower bounds at widths at least six. Their endpoint lemma applies here, but their width results do not determine the binary four-mer cardinality threshold. The binary three-mer census [3] concerns a different width.

The companion result [4] gives the sharp ratio \(17/11\) over all nonempty binary four-mer sets and the same four global equality cases. This overlaps with the ratio and witnesses for the eight-word row. The global maximum and equality classification do not by themselves exclude ratios strictly between \(3/2\) and \(17/11\) at sizes at most eight. The result here determines the first crossing of \(3/2\), exhausts its strict exceeders through size eight, and gives the separate maxima and multiplicities at each of those sizes. A complete length spectrum for the single sixteen-word instance addresses neither the threshold nor the per-cardinality census.

## Limitations

This is a finite threshold classification for distinct binary four-mers, not a result for arbitrary alphabets or widths. The per-cardinality census stops at eight. No claim is made about mean-case Greedy performance, tie-breaking probabilities, or historical priority.

## References

1. N. Chukhin, A. S. Kulikov, I. Mihajlin, A. Smal, *The Greedy Superstring Algorithm Achieves Ratio 2 for Strings of Length 6 Already*, arXiv:2608.20018, initial version dated 20 August 2026, https://arxiv.org/abs/2608.20018.
2. B. Cazaux, E. Rivals, *Relationship between superstring and compression measures: New insights on the greedy conjecture*, Discrete Applied Mathematics (2018), https://www.lirmm.fr/~rivals/publication/cazaux-dam-2018/.
3. *Sharp binary three-word greedy-superstring ratio and all equality cases*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-sharp-binary-three-word-greedy-superstring-ratio-and-all-equalit--f43f5caa07c5.
4. *Sharp worst-case Greedy ratio for distinct binary four-mers*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-worst-case-greedy-ratio-for-distinct-binary-four-mers--c5782f9cc70b.
