# Quadratic detours under adjacent swaps of \(231\)-avoiding permutations

## Finding
For every integer \(n\ge 2\), form the graph \(G_n\) of permutations avoiding the classical pattern \(231\). Two vertices are adjacent exactly when swapping the values in consecutive positions gives another \(231\)-avoiding permutation. Define
\[
A_n=(n-1,n-2,\ldots,1,n),\qquad B_n=(n,n-1,\ldots,1).
\]
Then \(G_n\) is connected and
\[
\boxed{d_{G_n}(A_n,B_n)=(n-1)^2.}
\]
Their ordinary adjacent-transposition distance in the full symmetric group is only \(n-1\). Hence, along this explicit infinite sequence, the ratio of the avoidance-preserving distance to the unrestricted adjacent-transposition distance is \(n-1\), which is unbounded.

An auxiliary exact formula is
\[
d_{G_n}(\pi,\operatorname{id})=\operatorname{inv}(\pi)
\quad\text{for every }\pi\in\operatorname{Av}_n(231).
\]
The theorem determines an exact pairwise distance, not the complete diameter of \(G_n\).

## Assumptions and scope
We work with permutations of the distinct integers \(1,\ldots,n\), written in one-line notation. A permutation contains \(231\) if there are positions \(i<j<k\) with \(\pi_k<\pi_i<\pi_j\); avoidance means no such triple. Every intermediate permutation in a path must avoid \(231\). Graph distance is minimum edge count, not a Gray-code Hamming difference and not the cover distance in the induced weak-order poset. The inversion count \(\operatorname{inv}(\pi)\) counts pairs \(i<j\) with \(\pi_i>\pi_j\). The two displayed endpoint permutations avoid \(231\) for all \(n\ge2\).

## Proof
**Lemma 1 (separation around the maximum).** If \(\pi\in\operatorname{Av}_n(231)\) and its maximum value \(n\) is in position \(k\), then the values to its left are exactly \(1,\ldots,k-1\), and the values to its right are exactly \(k,\ldots,n-1\). Indeed, if some left value exceeded some right value, those entries together with \(n\) would form \(231\). Because there are \(k-1\) entries to the left, they must be precisely the \(k-1\) smallest values.

**Lemma 2 (sorting by valid descent swaps).** Let \(\pi\in\operatorname{Av}_n(231)\), with \(\pi\ne\operatorname{id}\). Select the rightmost adjacent descent, say adjacent values \(x>y\), and swap them. The new permutation still avoids \(231\). Only the relative order of \(x\) and \(y\) changes. Were a new \(231\) created, it would necessarily use the pair in their new order \(y,x\) as the first two entries of the forbidden triple, followed by some value \(z<y\). But the original suffix after \(y\) is strictly increasing (as the selected descent is rightmost), starts with a value greater than \(y\), and therefore contains no such \(z\). The swap decreases inversion count by exactly one. Iteration reaches the identity in \(\operatorname{inv}(\pi)\) permitted swaps. Since every adjacent swap changes the inversion count by one, no shorter path to identity exists. This proves the auxiliary formula and connectedness of \(G_n\).

**Lower bound.** Consider any permitted adjacent-swap path from \(A_n\) to \(B_n\), without assuming that the maximum moves monotonically. For each \(j\in\{1,\ldots,n-1\}\), let \(t_j\) be the first move taking the value \(n\) from position \(j+1\) into position \(j\). These times exist because \(n\) moves from the last position to the first, and satisfy \(t_j<t_i\) whenever \(i<j\). Lemma 1 shows that at move \(t_j\), the value exchanged with \(n\) is exactly \(j\). In particular, \(n\) must exchange with all of its \(n-1\) smaller values.

Fix \(1\le i<j\le n-1\). Initially, in \(A_n\), the larger value \(j\) precedes \(i\). Immediately after \(t_j\), the value \(i\) lies left of \(n\), while \(j\) lies right of \(n\); hence \(i\) precedes \(j\). Thus the pair \(\{i,j\}\) must have been exchanged by an adjacent swap at least once before or at \(t_j\). Immediately before \(t_i\), the value \(i\) is immediately left of \(n\) and \(j\) is right of \(n\), so \(i\) still precedes \(j\). In the final permutation \(B_n\), \(j\) precedes \(i\), so they must be exchanged at least once after \(t_i\). These two exchanges are distinct because \(t_j<t_i\). Every smaller-value pair must therefore exchange at least twice. There are \(\binom{n-1}{2}\) such pairs, giving the path-length bound
\[
L\ge (n-1)+2\binom{n-1}{2}=(n-1)^2.
\]
Every adjacent swap exchanges exactly one unordered value pair, so the contributions cannot overlap.

**Matching upper bound.** Lemma 2 gives paths \(A_n\to\operatorname{id}\) and \(B_n\to\operatorname{id}\) of lengths \(\operatorname{inv}(A_n)=\binom{n-1}{2}\) and \(\operatorname{inv}(B_n)=\binom n2\). Reverse the second path and concatenate. The resulting permitted path has length
\[
\binom{n-1}{2}+\binom n2=(n-1)^2.
\]
The lower and upper bounds agree. In the unrestricted symmetric group, moving \(n\) from last to first position requires and achieves exactly \(n-1\) adjacent swaps; the smaller values remain in the same relative order. This proves the claimed distortion ratio.

## Verification
Two independent, self-contained finite checkers accompany this result. Run `python3 proof_checks/verify_bruteforce.py` to enumerate all permutations, filter forbidden triples directly, and perform a breadth-first search for each order from \(1\) through \(8\). Run `g++ -std=c++17 -O2 proof_checks/verify_recursive.cpp -o verify_recursive && ./verify_recursive` for independent Catalan-recursive enumeration, checking all orders from \(2\) through \(12\), including \(208{,}012\) states at order \(12\). Both verify the class size, connectedness, and the exact endpoint distance. The mathematical proof above establishes the result for all orders; finite computations are supplementary.

## Relationship to prior work
Knuth's stack-sortable class is precisely classical \(231\)-avoidance, and its Catalan enumeration is standard. Dukes, Flanagan, Mansour and Vajnovszki (first available arXiv version 16 April 2007) give Gray-code generation with bounded **Hamming distance**, rather than shortest paths constrained to single allowed adjacent swaps. Drake studies the weak-order subposet for pattern-avoiding permutations; comparability in this poset and its covers do not give the graph metric of the **induced** adjacent-swap graph considered here. Hyatt and Remmel analyze descent and maximum-drop enumerations of \(231\)-avoiders. Hartung, Hoang, Mütze and Williams study permutation-generation languages and Gray codes. These sources motivate the question but do not supply the exact displayed pairwise metric in the inspected relevant material.

## Limitations
The full diameter, all-pairs distance distribution, and classification of all extremal pairs of \(G_n\) are not established by this theorem. The novelty assessment is literature-based rather than an exhaustive historical priority certification; an unindexed or differently formulated result may exist. No independent scholarly audit has been performed.

## References
1. W. M. B. Dukes, M. F. Flanagan, T. Mansour, and V. Vajnovszki, *Combinatorial Gray codes for classes of pattern avoiding permutations*, arXiv:0704.2048 (first posted 2007-04-16); *Theoretical Computer Science* 396 (2008), 35–49.
2. B. Drake, *The Weak Order on Pattern-Avoiding Permutations*, *Electronic Journal of Combinatorics* 21 (2014), P3.15, DOI:10.37236/4000.
3. M. Hyatt and J. Remmel, *The classification of 231-avoiding permutations by descents and maximum drop*, arXiv:1208.1052 (2012).
4. E. Hartung, H. P. Hoang, T. Mütze, and A. Williams, *Combinatorial generation via permutation languages. I. Fundamentals*, arXiv:1906.06069 (2019).
