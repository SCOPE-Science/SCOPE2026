# Exact reaching threshold for size-\(n-2\) subsets of the Černý automaton

## Finding

For every \(n\ge3\), let \(C_n\) be the deterministic automaton on \(Q=\mathbb Z_n\) with \(a(i)=i+1\pmod n\), while \(b(i)=i\) for \(0\le i<n-1\) and \(b(n-1)=0\). For a nonempty subset \(S\subseteq Q\), define its reaching threshold as
\[
\operatorname{rt}(S)=\min\{|w|:\delta(Q,w)=S\}.
\]
Then
\[
\max_{|S|=n-2}\operatorname{rt}(S)=2n,
\]
and the unique maximizing target (under this standard state labeling) is \(S_*=Q\setminus\{n-3,n-2\}\).

## Assumptions and scope

The automaton is complete and deterministic; words act from left to right. The symbol \(a\) is the cyclic permutation and \(b\) fixes all states except that it maps \(n-1\) to \(0\). Only target subsets of cardinality \(n-2\) are considered. The claim concerns shortest reaching words, not reset thresholds, avoiding thresholds, or the number of words attaining a threshold.

## Proof

Write \(H=Q\setminus S\) for the set of holes. The letter \(a\) rotates every hole by one. The action of \(b\) on holes is:

1. if neither \(0\) nor \(n-1\) is a hole, add the hole \(n-1\) (the image loses one state);
2. if \(0\) is a hole and \(n-1\) is not, replace the hole \(0\) by \(n-1\);
3. if \(n-1\) is already a hole, \(b\) does not change the hole set.

A word reaching a set with exactly two holes must contain exactly two rank-decreasing uses of \(b\); no later rank decrease is possible because image cardinality never increases. The first such use leaves \(H=\{n-1\}\). Immediately before the second, the single hole must be some \(h\in\{1,\ldots,n-2\}\), so the second use leaves \(H=\{h,n-1\}\).

**Upper bound and uniqueness of the extremal target.** Let the target holes be an unordered pair \(\{u,v\}\). Orient it so that \(d=(v-u)\bmod n\) lies in \(\{2,\ldots,n-1\}\); if one orientation has difference \(1\), take the reverse orientation. Put \(h=d-1\), and choose \(t\in\{0,\ldots,n-1\}\) with \(t=(u-(n-1))\bmod n\). The word
\[
 b\,a^d\,b\,a^t
\]
first creates hole \(n-1\), rotates it to \(h\), creates the second hole \(n-1\), and then rotates \(\{h,n-1\}\) to \(\{u,v\}\). Its length is \(d+t+2\le2n\). Equality in this construction requires \(d=t=n-1\), which gives exactly \(\{u,v\}=\{n-3,n-2\}\). Thus every other target has a reaching word shorter than \(2n\).

**Lower bound for the target \(H_*=\{n-3,n-2\}\).** Consider any word reaching \(H_*\), and let \(h\in\{1,\ldots,n-2\}\) be the singleton hole immediately before its second rank-decreasing \(b\). Between the first and second rank decreases, the hole starts at \(n-1\); the shortest way to put it at \(h\) is \(a^{h+1}\). A \(b\) at hole \(0\) sends it back to \(n-1\), and a \(b\) elsewhere is a no-op, so this segment has length at least \(h+1\).

After the second rank decrease, track the oriented cyclic gap from the hole that was at \(n-1\) to the other hole. It starts at \(h+1\). Rotations preserve the gap. Each later effective \(b\) acts on a pair \(\{0,r\}\) and replaces it by \(\{n-1,r\}\), increasing this oriented gap by one modulo \(n\). Let \(E\) be the number of these effective moves. Since the target pair is adjacent, its oriented gap is either \(1\) or \(n-1\), hence \(E\ge n-h-2\). Each effective move needs an intervening rotation, and after the last effective move at least \(n-1\) rotations are needed to reach \(H_*\): its output must be \(\{n-2,n-1\}\), which rotates to \(H_*\) only after \(n-1\) steps. If \(E=0\), the same final-rotation bound holds and requires \(h=n-2\). Therefore the suffix after the second rank decrease has length at least \(n-1+2E\).

Including the two rank-decreasing letters gives
\[
 |w|\ge 1+(h+1)+1+(n-1+2E)
 \ge 3n-h-2\ge2n,
\]
where the last inequality uses \(h\le n-2\). The word \(b a^{n-1} b a^{n-1}\) reaches \(H_*\) and has length \(2n\), proving equality. Combined with the upper bound, this proves both the maximum and uniqueness of the maximizing target for all \(n\ge3\).

## Verification

The symbolic argument proves the result for every \(n\ge3\). A standard-library breadth-first search checker included with this package independently enumerates all subset images for \(3\le n\le10\); it confirms that every target with two holes is reachable, the maximum distance is \(2n\), and the unique maximizer is \(H_*\). This finite check is corroboration only and is not used as the infinite proof.

## Relationship to prior work

Ferens and Szykuła define the reaching threshold for completely reachable automata and prove a general upper bound \(2n(n-|S|)-nH_{n-|S|}\), which specializes to \(5n/2\) for \(|S|=n-2\). Zhu studies Don's conjecture for binary completely reachable automata and gives counterexamples in other automata families, including targets of size \(n-2\). Neither inspected statement supplies the exact reaching-threshold profile of the canonical Černý automaton at size \(n-2\), nor the unique extremizer proved here. A separate exact-results search found a general \(2n\) two-defect upper construction and an exact Černý avoiding-threshold result; those concern the upper bound or a different objective, and do not give the lower bound plus unique target characterization.

## Limitations

The theorem is limited to the canonical Černý automaton and target subsets of size \(n-2\). It does not classify reaching thresholds for other subset sizes or other automata, and it makes no claim about reset thresholds or avoiding thresholds. The finite checker covers only \(3\le n\le10\); the universal conclusion rests on the symbolic proof above. A literature search cannot certify absolute novelty against every unpublished or unindexed source.

## References

1. Robert Ferens and Marek Szykuła, *Completely reachable automata: a quadratic decision algorithm and a quadratic upper bound on the reaching threshold*, arXiv:2208.05956, first submitted 2022-08-11; version 5 dated 2025-02-10.
2. Yinfeng Zhu, *Around Don's conjecture for binary completely reachable automata*, arXiv:2402.19089, first submitted 2024-02-29.
