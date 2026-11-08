# Fibonacci minimal-absent-subsequence count for binary powers with two non-singleton runs

## Finding

Let \(a,b\ge 2\) and \(k\ge 1\) be integers, and consider the finite binary word
\[
W_{a,b,k}=(0^a1^b)^k.
\]
A **minimal absent scattered subsequence** of \(W\) is a nonempty binary word \(v\) which is not a subsequence of \(W\), but such that deletion of any one letter of \(v\) produces a subsequence of \(W\). Let \(\mathcal M(W)\) be the set of distinct such words. Write \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\) for the Fibonacci numbers. Then
\[
\boxed{\lvert\mathcal M(W_{a,b,k})\rvert=F_{2k+2}.}
\]
In particular, this complete count depends only on the number of repeated run pairs, **not** on either run length once both are at least two. The first six counts (\(k=1,2,3,4,5,6\)) are \(3,8,21,55,144,377\); the exponential growth base in \(k\) is \(\varphi^2=(3+\sqrt5)/2\), where \(\varphi=(1+\sqrt5)/2\).

## Assumptions and scope

The alphabet is the fixed labeled binary alphabet \(\{0,1\}\). The powers are finite *linear* words, not circular words. Subsequence means order-preserving scattered subsequence; no adjacency is required. Distinct minimal absent words are counted once each, without counting their embeddings. The theorem requires both \(a\ge2\) and \(b\ge2\); it makes no assertion of the same Fibonacci count when a run has length one.

## Proof

**Greedy bridge criterion.** Let \(w=w_1\cdots w_n\) be a word containing both symbols, and let \(v=v_1\cdots v_{m+1}\) have an embeddable prefix \(v_1\cdots v_m\), with greedy leftmost embedding positions \(i_1<\cdots<i_m\). Set \(i_0=0\). Then \(v\) is minimally absent if and only if, for every \(2\le t\le m+1\), the symbol \(v_t\) occurs in the interval
\[
 w_{i_{t-2}+1}\cdots w_{i_{t-1}},
\]
and the last symbol \(v_{m+1}\) has no occurrence strictly after \(i_m\). This is the greedy-position characterization of minimal absence, included here to identify the exact condition used. Necessity follows by comparing an embedding after deletion of \(v_{t-1}\) with the greedy embedding of the shorter prefix: if the next letter did not occur in that bridge, the deletion could not be embedded. For sufficiency, if \(v_t\) is deleted, match \(v_1,\ldots,v_{t-1}\) greedily and match each later \(v_s\) (\(s>t\)) inside the disjoint, ordered bridge interval \((i_{s-2},i_{s-1}]\). All one-letter deletions embed, while the last-letter condition ensures \(v\) itself does not. The criterion is also proved by Kosche–Koß–Manea–Siemer (Theorem 3.1 of the cited work).

Write the \(2k\) constant runs of \(W\), in order, as \(R_0,R_1,\ldots,R_{2k-1}\); even-indexed runs consist of zeros, odd-indexed runs of ones. Every run has length at least two. A greedy matched prefix is **ready at run \(j\)** if its last matched position is the *first* position of \(R_j\), and its most recent bridge interval contains both symbols. The greedy bridge criterion then allows either symbol as the next target letter.

From a ready state at the first position of \(R_j\), there are exactly two kinds of continuation:

1. Choose the opposite symbol. Its first subsequent occurrence is at the first position of \(R_{j+1}\). Because \(R_j\) has at least two symbols, the interval from the current match to the new match contains an unused symbol of \(R_j\) as well as the first symbol of \(R_{j+1}\). Thus the new state is ready at \(j+1\), provided this next run exists. If \(j=2k-1\), the opposite symbol is absent and this choice terminates in one minimally absent word.
2. Choose the same symbol. The greedy embedding is then forced to consume the remaining positions of \(R_j\) consecutively: their bridge intervals contain only that symbol, so no opposite symbol may follow while still inside the run. Once the current run is exhausted, the next equal symbol is the first position of \(R_{j+2}\), and its bridge skips the entire opposite run \(R_{j+1}\); hence the new state is ready at \(j+2\). If no subsequent run of the same symbol exists, appending one further copy of that symbol terminates in exactly one minimally absent word.

Let \(h_j\) count the possible completed minimally absent words from a ready state at \(R_j\). At the final run, the two choices above both terminate, giving \(h_{2k-1}=2\). At the penultimate run, the same-symbol route terminates and the opposite-symbol route reaches the last run, giving \(h_{2k-2}=1+h_{2k-1}=3\). For every \(0\le j\le2k-3\), the two disjoint possibilities give
\[
h_j=h_{j+1}+h_{j+2}.
\]
The successive continuations are distinguished by their very next symbol, and greedy positions are uniquely determined by the output word; consequently there is no overcounting.

Every minimally absent word starts in one of two ways. If it starts with \(1\), its first greedy match is the first position of \(R_1\), and its first bridge includes \(R_0\) as well as that \(1\). It is therefore ready at \(R_1\), contributing \(h_1\) words. If it starts with \(0\), its first match is the first symbol of \(R_0\), with a pure-zero bridge. The bridge criterion forces the same symbol until \(R_0\) is exhausted; the next zero match (if present) is at the first position of \(R_2\), reached with a mixed bridge. Thus it contributes \(h_2\) words, with the convention \(h_2=1\) when \(k=1\), representing the unary word \(0^{a+1}\).

With the boundary convention \(h_j=1\) for \(j\ge2k\), the recurrence has the solution
\[
h_j=F_{2k-j+2}\qquad(1\le j\le2k-1),
\]
so the total is
\[
h_1+h_2=F_{2k+1}+F_{2k}=F_{2k+2},
\]
as claimed. For \(k=1\), the three words are \(0^{a+1}\), \(10\), and \(1^{b+1}\), agreeing with \(F_4=3\). This covers all integer parameters and all boundary cases within the stated scope. \(\square\)

## Verification

The accompanying standalone Python program `verify_binary_run_mas.py` constructs minimal absent subsequences independently by: (i) enumerating all binary target strings and checking every one-letter deletion against the literal host, and (ii) building greedy bridge paths from literal character positions. It compares the entire output sets for twenty-five parameter triples with run lengths in \(\{2,3,4\}\) and host length at most eighteen, and independently checks the run-graph count against Fibonacci numbers for 4,056 further parameter triples. All tests passed. The finite tests are corroboration, not a substitute for the preceding proof.

To reproduce from the embedded artifact, run `python3 verify_binary_run_mas.py` under Python 3 without third-party dependencies.

## Relationship to prior work

Kosche, Koß, Manea and Siemer established the general greedy-bridge characterization of minimal absent scattered subsequences and exponential families; their published statements cover a general characterization rather than the explicit two-non-singleton-run Fibonacci enumeration here. Manea, Ringleb, Siemer and Winkler provided later output-efficient algorithms for general minimal absent subsequences, again without stating this exact closed-form family count in the relevant inspected material. The novelty asserted here is the specialized but nontrivial **closed count and run-length invariance**, not the definition or the general bridge criterion. Generic algorithms can of course compute any particular finite instance. Similar formulas, if found in unindexed prior work, would supersede originality.

## Limitations

The claim concerns total counts, not the full length distribution, and requires both run lengths at least two. Neither the general minimal-absence characterization nor finite verification alone establishes that the formula is unpublished; bibliographic completeness is not claimed. Independent validation has not occurred. The proof concerns scattered subsequences, not minimal absent contiguous factors.

## References

1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, first posted 2021-08-31; in particular Theorem 3.1 and Proposition 3.8. https://arxiv.org/html/2108.13968v6
2. F. Manea, T. Ringleb, S. Siemer, M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471, first posted 2025-04-30. https://arxiv.org/html/2504.21471v1
