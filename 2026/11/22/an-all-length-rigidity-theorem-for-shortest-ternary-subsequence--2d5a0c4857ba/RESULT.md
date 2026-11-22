# An all-length rigidity theorem for shortest ternary subsequence covers

## Finding

Let \(S\) be any nonempty finite word on an alphabet of at most three letters. A *subsequence cover* (s-cover) is a nonempty word \(C\) such that each position of \(S\) belongs to at least one scattered-subsequence occurrence of \(C\). An s-cover is *shortest* if its length is minimum over all s-covers. Define \(R(S)\) by replacing every maximal constant-letter run of \(S\) with its single letter.

**Theorem (complete ternary ambiguity language).** Every such word \(S\) has a unique shortest s-cover, except precisely when some injective renaming of its letters makes

\[
R(S)=(01)^a\,2\,(02)^b\,(10)^c,\qquad a,c\ge2,\quad b\ge1.
\]

In every exception there are **exactly two**, both of length six. Under the displayed renaming they are \(\mathtt{010210}\) and \(\mathtt{012010}\). In particular, no ternary word has three shortest s-covers.

The number \(E_n\) of labeled ternary words of length \(n\) with two shortest covers has the exact ordinary generating function

\[
\sum_{n\ge1}E_nz^n
 =\frac{6z^{11}}{(1-z)^5(1-2z)^3}.
\]

Consequently \(E_{11}=6\), \(E_{12}=66\), \(E_{13}=414\), and \(E_n\sim (3/64)n^2 2^n\). The exceptional words with no equal adjacent symbols have odd lengths \(11+2k\) and exactly \(6\binom{k+2}{2}\) labeled members of each such length.

## Assumptions and scope

Words are nonempty; occurrences may overlap, and distinct shortest covers are counted as distinct letter sequences, not as embeddings. The alphabet may be any subset of \(\{0,1,2\}\), and arbitrary positive run lengths are allowed. The displayed family uses exactly three distinct letters. Letter permutations do not affect cover multiplicities. The assertions quantify over **all finite word lengths**, not only the directly enumerated cases.

The all-length argument uses two published facts about s-covers: any shortest s-cover is s-primitive and has no adjacent equal letters, and the longest s-primitive word on at most three letters has length eight. See the foundational reference for transitivity and the value \(\gamma(3)=8\).

## Proof

**1. Reduction to run-free words.** A candidate shortest s-cover has no two consecutive equal letters; alternatively, deleting one of any consecutive equal letters of a cover preserves the coverage of all host positions (an occurrence through the removed copy can retain that host position as the remaining equal copy). If \(C\) has no equal adjacent letters, every occurrence of \(C\) uses at most one position in each maximal constant-letter run of \(S\). Expanding or contracting the runs thus preserves the existence of an occurrence through a given run: any chosen position in that run can replace the originally chosen one without violating the order of the other letters. Therefore \(C\) covers \(S\) if and only if it covers \(R(S)\). As all shortest s-covers are run-free, this also preserves the *complete set* of shortest covers and their lengths.

If \(S\) uses just one letter, its shortest cover is the one-letter word. If it uses two letters, its shortest cover is unique: the published \(\gamma(2)=3\) bound, together with the first/last-letter and adjacency constraints, leaves at most one candidate of each possible shortest length; more explicitly a run-free binary host beginning in \(0\) has the unique shortest cover \(\mathtt{01}\) when it ends in \(1\), or \(\mathtt{010}\) when it ends in \(0\). For two-letter hosts this is checked directly by the same occurrence criterion below. It remains to consider run-free ternary words, normalized by alphabet permutation to begin with \(\mathtt{01}\).

**2. A bounded local-state machine for one candidate.** For each nonrepeating candidate \(C=c_0\cdots c_{m-1}\), \(1\le m\le8\), with \(c_0=0\), maintain a state \((p,r)\) or a permanently rejecting state. The number \(p\) is the greatest prefix length of \(C\) appearing as a scattered subsequence of the host prefix read so far. The number \(r\) is the length of the *largest* still-unmatched suffix obligation of \(C\) among all already seen host positions. Each host position must be placed at some index \(j\) of \(C\) after an embedded prefix and before an embedded suffix. In the nonrepeating case the maximal feasible \(j\) with \(c_j=x\) and \(j\le p\) gives the shortest new suffix obligation. All obligations are suffixes of the *same* word, so matching the longest outstanding obligation by its leftmost greedy embedding simultaneously satisfies every shorter obligation.

On reading \(x\), first decrease \(r\) if \(r>0\) and \(x=c_{m-r}\), then choose the largest \(j\le p\) with \(j<m\) and \(c_j=x\). If there is none, reject permanently: the new position cannot be part of any occurrence. Otherwise set

\[
r\leftarrow\max(r,m-j-1),\qquad
p\leftarrow p+[p<m\ \text{and}\ c_p=x].
\]

The second update advances the greedy prefix-subsequence step; the first maintains the longest residual suffix. A full host is covered by \(C\) **if and only if** the final state is nonrejecting and \(r=0\). To justify necessity, each covered position induces one feasible index and corresponding matched right suffix; to justify sufficiency, each obligation introduced for a position is discharged by a subsequently greedily matched suffix. The longest-obligation invariant is exact because every shorter obligation is a suffix of the longer one. This is a finite-state *decision* procedure, not an assumed classification.

**3. Exhausting all hosts with one finite transition graph.** By transitivity of s-covers, any shortest s-cover is s-primitive, hence has length at most \(\gamma(3)=8\), starts with \(0\), and has no equal neighboring letters. There are exactly \(1+2+4+\cdots+128=255\) such candidate words. The supplied standalone C++17 program `certify_dfa.cpp` constructs their direct-product automaton, adjoining the last host symbol and a deterministic recognizer for the displayed three-parameter regex. It starts after the host prefix \(\mathtt{01}\), permits every next symbol except the previous one, interns *every* reachable state, and expands *every* allowed edge. The graph search closes after exactly **84,725 states and 169,450 transitions**; there are no omitted branches.

For each reachable graph state, the program explicitly computes all candidates \(C\) whose individual cover states accept, identifies the minimum length, and checks the following exhaustive state invariant:

* if the regex recognizer is in an accepting state, the minimum length is exactly six and the entire minimum set is \(\{\mathtt{010210},\mathtt{012010}\}\);
* otherwise the minimum set has exactly one element.

All 84,725 cases satisfy the invariant, and the maximum minimum-cover length is eight. Together with the reduction to a fixed alphabet and every run-free host with normalized prefix \(\mathtt{01}\), closure of the state graph proves the asserted equivalence **for all lengths**. The finite graph, its successor rule, and its acceptance test are included in full; no finite-length sampling is used to infer the infinite result.

**4. Exact enumeration.** The language of normalized run-free exceptions has bivariate run-length generating series

\[
\sum_{\substack{a,c\ge2\\b\ge1}}u^{2a+2b+2c+1}
=\frac{u^{11}}{(1-u^2)^3}.
\]

There are six injective letter relabelings. Replacing each run-free letter by an arbitrary positive-length run substitutes \(u=z/(1-z)\), yielding

\[
\sum_{n\ge1}E_nz^n
=6\frac{(z/(1-z))^{11}}{(1-(z/(1-z))^2)^3}
=\frac{6z^{11}}{(1-z)^5(1-2z)^3}.
\]

The first coefficients and the singularity at \(z=1/2\) give the stated values and asymptotic. The normalized run-free coefficient at \(11+2k\) is \(\binom{k+2}{2}\), proving its asserted census. \(\square\)

## Verification

Compile and run from the directory containing the two included C++17 files:

```sh
c++ -std=c++17 -O2 certify_dfa.cpp -o certify_dfa
./certify_dfa
c++ -std=c++17 -O2 verify_independent.cpp -o verify_independent
./verify_independent
```

The exact full-automaton certificate reports `states=84725 edges=169450 patterns=255 max_shortest=8 ambiguity_states=12`. The independent cross-check does **not** use automaton transitions: it forms the positional-subsequence bitmask unions for every run-free, prefix-normalized ternary word of lengths two through twelve (2,047 total), enumerates its complete minimum covers, and independently checks the earliest/latest-embedding membership test against brute positional enumeration. It reports one exceptional normalized input, which occurs at length eleven. `verification_output.txt` records the actual executable outputs. Both programs are standalone and require only a C++17 compiler; the first is the all-length finite-state certificate, while the second is a bounded, logically different independent check.

## Relationship to prior work

Charalampopoulos, Pissis, Radoszewski, Rytter, Waleń and Zuba introduced s-covers, proved the short-candidate and s-primitivity facts used here, and gave general algorithms. Their original conference paper was publicly available in November 2022; the later journal and arXiv versions are revisions of that earlier work and **do not** determine the date of the newer motivating finite classification. Their examples of multiple shortest covers use larger alphabets, and their all-length constructions with exponentially many shortest covers use growing alphabets rather than the fixed ternary case.

The published, dated October 18, 2026 finite classification *First ambiguity of shortest ternary subsequence covers* proves that exactly six labeled words of length eleven first exhibit two shortest covers. It expressly makes no assertion about lengths greater than eleven. The present result implies that boundary and additionally determines the full ternary ambiguity language at every length, rules out three shortest covers, and enumerates all expanded-run exceptions. The earlier finite census does not imply these infinite consequences; the proof here requires closing the 84,725-state automaton graph.

## Limitations

The global classification is a **computer-assisted theorem** whose finite graph closure and acceptance checks must be reproduced from the supplied code. The second enumerator is independent in mechanism but proves only its explicitly enumerated finite range. The paper relies on the published \(\gamma(3)=8\) fact; it does not independently reprove that bound. The assertion applies to ordinary overlapping scattered-subsequence covers, not contiguous covers or disjoint shuffle covers. No independent scholarly audit or formalized proof is claimed. An earlier unindexed equivalent of the all-length classification could exist; literature checks cannot conclusively prove priority.

## References

1. P. Charalampopoulos, S. P. Pissis, J. Radoszewski, W. Rytter, T. Waleń and W. Zuba, *Subsequence Covers of Words*, SPIRE 2022, DOI `10.1007/978-3-031-20643-6_1`, full author manuscript: https://ir.cwi.nl/pub/32638/32638.pdf .
2. Same authors, *Subsequence covers of words*, *Theoretical Computer Science* **1041** (2025), 115216, DOI `10.1016/j.tcs.2025.115216`, full text: https://arxiv.org/abs/2509.05827 .
3. *First ambiguity of shortest ternary subsequence covers*, publicly dated 2026-10-18, exact finite classification and independent certificate: https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-first-ambiguity-of-shortest-ternary-subsequence-covers--19792ff873a4/RESULT.md .
