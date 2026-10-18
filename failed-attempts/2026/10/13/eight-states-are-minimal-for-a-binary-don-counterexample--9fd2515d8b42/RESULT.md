# Eight states are minimal for a binary Don-counterexample
## Finding
Consider binary completely reachable deterministic automata. A standard structural fact for this class is that one of the two letters acts as a full cycle. Therefore the binary completely reachable class can be normalized by fixing that cycle letter. Don's bound
\[
\operatorname{rt}(S)\le n\bigl(n-|S|\bigr)
\]
holds for every binary completely reachable automaton with at most \(7\) states, but fails already at \(8\) states.

Normalize the cycle letter by
\[
b(q)=q+1\pmod 8.
\]
Among all \(8^8\) choices of the other letter \(a\), exactly \(1{,}093{,}632\) normalized presentations are completely reachable, and exactly \(544\) of those violate Don's bound. Each violating presentation has exactly one violating subset; that subset has size \(6\), shortest reaching length \(17\), and Don's bound \(16\).

The \(544\) normalized violations form exactly \(68\) orbits under cyclic relabeling of the state set, each orbit having size \(8\).

A lexicographically least representative is
\[
a=(0,0,3,5,1,2,6,7),\qquad b=(1,2,3,4,5,6,7,0).
\]
For
\[
S=\{0,1,2,4,5,6\},
\]
a shortest reaching word is
\[
\mathtt{abbbbbbabbbbbabbb},
\]
of length \(17\).

## Assumptions and scope
A subset \(S\) of the state set \(Q\) is reachable when \(S=Qw\) for some input word \(w\). An automaton is completely reachable when every nonempty subset is reachable. The reaching threshold \(\operatorname{rt}(S)\) is the minimum length of a word reaching \(S\).

Every binary completely reachable automaton on more than one state has one input letter acting as a full \(n\)-cycle. Up to relabeling, that cycle can be fixed as \(b(q)=q+1\pmod n\); the other letter is then an arbitrary map \(a:Q\to Q\). Therefore enumerating all \(n^n\) choices of \(a\) is exhaustive for the entire binary completely reachable class.

The counts \(544\) and \(68\) refer to normalized presentations with the designated cycle letter \(b\). They are not asserted to be counts of abstract automata modulo every possible alphabet and state symmetry.

## Proof
For each \(2\le n\le8\), fix
\[
Q=\{0,1,\ldots,n-1\},\qquad b(q)=q+1\pmod n.
\]
There are exactly \(n^n\) possible maps \(a:Q\to Q\).

For each ordered pair \((a,b)\), form the power automaton on the \(2^n-1\) nonempty subsets of \(Q\). A breadth-first search from \(Q\) gives the exact reaching threshold of every reachable subset. The automaton is completely reachable exactly when all \(2^n-1\) nonempty subsets occur in this search.

The exhaustive counts of completely reachable normalized presentations are
\[
\begin{array}{c|rrrrrrr}
n&2&3&4&5&6&7&8\\
\hline
\text{completely reachable}&2&18&128&1200&9936&105840&1093632.
\end{array}
\]
For every completely reachable presentation with \(n\le7\), every subset satisfies
\[
\operatorname{rt}(S)\le n\bigl(n-|S|\bigr).
\]
Hence no smaller binary completely reachable counterexample exists.

At \(n=8\), exactly \(544\) completely reachable presentations violate the inequality. In every one, there is exactly one violating subset, it has cardinality \(6\), and its reaching threshold is exactly
\[
17=8(8-6)+1.
\]
No larger excess occurs.

For the displayed representative, a direct second breadth-first search reaches all \(255\) nonempty subsets and gives
\[
\operatorname{rt}\bigl(\{0,1,2,4,5,6\}\bigr)=17.
\]
Tracing a shortest-path parent tree yields
\[
\mathtt{abbbbbbabbbbbabbb}.
\]
Thus the representative is completely reachable and violates Don's bound by exactly \(1\).

Finally, conjugating \(a\) by powers of the cycle \(b\) implements cyclic state relabeling while keeping the normalized form of \(b\). Partitioning the \(544\) violations by this action gives \(68\) orbits, each of size \(8\).

## Verification
Run `python3 verify.py` beside `census.cpp` and `certificate.json`.

The compiled census exhausts every map \(a\) for every \(2\le n\le8\), for a total final layer of \(8^8=16{,}777{,}216\) maps. For every map it performs exact subset breadth-first search, checks complete reachability, compares every reaching threshold with Don's bound, and recomputes the cyclic-relabeling orbit partition.

The Python layer independently checks the displayed representative: it reconstructs all \(255\) reachable nonempty subsets, verifies distance \(17\) to the target, replays the stored shortest word, and confirms that this target is the representative's unique Don violation.

The certificate records the complete counts but is not trusted as an input to the census.

## Relationship to prior work
Zhu constructed an infinite family of binary completely reachable circular automata violating Don's conjecture. The family is stated for even \(n\ge10\), and its hard subsets have size \(n-2\) with reaching threshold at least
\[
\frac{5}{2}n-3,
\]
which exceeds Don's value \(2n\) there.

Ferens and Szykuła's later general treatment of completely reachable automata summarizes Zhu's family as the known binary counterexample mechanism and notes that the known nontrivial lower bounds occur in the codimension-two case. Their general upper bound does not determine the smallest state size at which a circular counterexample exists.

Casas and Volkov prove Don's conjecture for structured subclasses of binary completely reachable automata, including standardized settings under additional restrictions. Those positive results do not cover all circular binary automata.

The present finite classification sharpens the published binary counterexample onset from the family starting at \(10\) states to the exact binary minimum \(8\), and classifies the entire normalized first layer.

## Limitations
The \(544\)-presentation count is normalization-dependent. Only cyclic state relabelings preserving the chosen standard cycle are quotiented in the \(68\)-orbit count.

No formula or classification is claimed for binary Don-counterexamples on more than \(8\) states.

An unindexed computation or unpublished small-state census could contain the same \(8\)-state boundary.

## References
1. Y. Zhu, “Around Don's conjecture for binary completely reachable automata,” arXiv:2402.19089v1, first public version 2024-02-29; Developments in Language Theory 2024, pp. 282–295, DOI 10.1007/978-3-031-66159-4_20.
2. R. Ferens and M. Szykuła, “Recognizing Completely Reachable Automata in Quadratic Time,” ACM Transactions on Algorithms 22(2) (2026), Article 24, DOI 10.1145/3798283.
3. D. Casas and M. V. Volkov, “Don's conjecture for binary completely reachable automata: an approach and its limitations,” arXiv:2311.00077v1, first public version 2023-10-31; Journal of Automata, Languages and Combinatorics 29 (2024), 159–175.
