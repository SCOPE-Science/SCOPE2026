# Exact pair-merging distances and unique shortest-word suffixes in Černý automata

## Finding

For every integer \(n\ge 2\), consider the labeled Černý automaton \(\mathcal C_n\) with state set \(Q=\{0,1,\ldots,n-1\}\) and letters \(a,b\) acting by
\[
a(x)=x+1\pmod n,\qquad b(n-1)=0,\quad b(x)=x\ (0\le x<n-1).
\]
For \(0\le i<j<n\), set \(g=j-i\) and let \(d_n(i,j)\) denote the minimum length of a word mapping states \(i,j\) to the same state. Then
\[
\boxed{d_n(i,j)=
\begin{cases}
ng-i,&2g<n,\\
(n+1)(n-g)-n-i,&2g\ge n.
\end{cases}}
\]
The \(\binom n2\) numbers \(d_n(i,j)\) are exactly \(1,2,\ldots,\binom n2\), each occurring once. Furthermore, **every pair has exactly one shortest merging word**. All these shortest words are the nonempty suffixes of a single word \(W_n\), one suffix of each length, where
\[
\boxed{W_n=
\begin{cases}
(a^{n-1}b)^{(n-1)/2},&n\text{ odd},\\
a^{n/2-1}b\,(a^{n-1}b)^{n/2-1},&n\text{ even}.
\end{cases}}
\]
In particular, the unique pair of largest merging distance is \(\{0,\lfloor n/2\rfloor\}\); its unique shortest merging word is \(W_n\). The known general extremal two-state rendezvous bound \(\binom n2\) is attained. The exact all-pair spectrum and the uniqueness/suffix-chain classification are the contributions, not the already-known maximal bound.

## Assumptions and scope

The alphabet is exactly \(\{a,b\}\) with the transition convention above; the labels matter in the uniqueness assertion. A word is read left-to-right, applying each letter to the current states. The pair is unordered, but its labels \(i<j\) are used in the distance formula. Every \(n\ge2\), both parities, all \(\binom n2\) pairs, and the empty word are covered. For two different states, a merging word cannot be empty. Uniqueness means uniqueness as a string over \(\{a,b\}\) of minimum length, not uniqueness among longer merging words.

## Proof

Write \(N=\binom n2\) and define \(D(i,j)\) to be the displayed piecewise integer. We prove that \(D\) is a bijective distance-to-merger rank and that precisely one available letter decreases it by one.

**(1) Bijection onto all possible ranks.** Fix \(1\le r<n/2\). The pairs with gap \(n-r\) are \((i,i+n-r)\) for \(0\le i<r\), and their \(D\)-values form the complete integer interval
\[
\{n(r-1)+1,\ldots,(n+1)r-n\}.
\]
The pairs with gap \(r\) are \((i,i+r)\) for \(0\le i<n-r\), and their \(D\)-values form the immediately following interval
\[
\{(n+1)r-n+1,\ldots,nr\}.
\]
Together they occupy \(\{n(r-1)+1,\ldots,nr\}\), with no repetitions. For odd \(n\), the values \(r=1,\ldots,(n-1)/2\) exhaust all \(N\) ranks. For even \(n=2m\), the ranges for \(r=1,\ldots,m-1\) occupy \(1,\ldots,n(m-1)\). The \(m\) central pairs of gap \(m\) have values \((n+1)m-n-i\), for \(0\le i<m\), and complete the remaining ranks through \(N\). Thus exactly one pair has each rank \(1,\ldots,N\).

**(2) One-step rank law.** For \(j<n-1\), letter \(a\) maps \((i,j)\) to \((i+1,j+1)\) and lowers \(D\) exactly by one, while \(b\) fixes the pair. For \(j=n-1\), distinguish the following exhaustive cases. If \(0\le i\le\lfloor(n-2)/2\rfloor\), the formula gives \(D(i,n-1)=ni+1\); \(b\) maps the pair to the sink when \(i=0\), and otherwise to \((0,i)\), whose rank is \(ni\). In this range, \(a\) maps the pair to \((0,i+1)\) with rank at least \(D(i,n-1)\). If \(\lfloor n/2\rfloor\le i\le n-2\), then \(D(i,n-1)=n(n-1-i)-i\). Letter \(a\) maps it to \((0,i+1)\), whose rank is exactly \(D(i,n-1)-1\); letter \(b\) maps it to \((0,i)\), with rank at least \(D(i,n-1)\). These ranges partition all \(i\in\{0,\ldots,n-2\}\), including the even middle-gap boundary. Set the sink rank to zero. Hence every pair has exactly one outgoing transition lowering rank by one and the other does not lower rank.

**(3) Exact distances and shortest-word uniqueness.** Along any sequence of letters, the rank can drop by at most one per step until it reaches zero. Therefore at least \(D(i,j)\) letters are needed. At each positive rank choose the unique letter that lowers the rank by one. By the bijection in (1), this process reaches the sink after exactly \(D(i,j)\) steps, proving equality. Every shortest word must lower rank by one at *every* step and must therefore make these same uniquely determined choices. Thus the shortest merging word is unique.

**(4) Suffix-chain and explicit universal word.** Since there is exactly one state at each rank and its unique optimal successor has the preceding rank, the descending path from rank \(N\) passes once through every pair. From (2), its optimal letter at rank \(t\) is \(b\) precisely if \(t\equiv1\pmod n\), and is \(a\) otherwise: in the \(b\)-case the pair is \((i,n-1)\) with \(D=ni+1\), including the sink-reaching case \(i=0\). Its label word therefore consists of \(a\)-runs separated by \(b\)'s at exactly those ranks. For odd \(n=2m+1\), \(N=mn\) gives \((a^{n-1}b)^m\). For even \(n=2m\), \(N=n(m-1)+m\) gives the initial \(a^{m-1}b\) followed by \(m-1\) copies of \(a^{n-1}b\). The path beginning at rank \(t\) reads the final \(t\) letters of \(W_n\). Finally, the rank-\(N\) pair is \((0,\lfloor n/2\rfloor)\) by the formulas and interval endpoints. This proves all assertions.

## Verification

Run `python3 verify.py` with Python 3 standard library only. The verifier independently constructs reverse pair-automaton breadth-first distances for \(2\le n\le80\) and compares every value with the formula. It also checks that the non-sink ranks are exactly the consecutive integers, that precisely one transition drops rank by one, that no transition drops by more than one, and that the explicit longest word follows the complete optimal chain. These algebraic and chain checks extend to \(2\le n\le400\). The recorded execution returned `PASS` with 10,666,600 tested pair instances. These finite checks are supplementary to, not substitutes for, the preceding proof for all \(n\ge2\).

## Relationship to prior work

Behague and Johnson, *Synchronizing Times for \(k\)-sets in Automata* (arXiv:2008.12166, first public 2020-08-27), Section 1, already state the sharp general two-state rendezvous upper bound \(\binom n2\) and give a Černý pair attaining it. Gusev, *Synchronizing Automata with Random Inputs* (arXiv:1404.6731, 2014), Section 3 and Figure 3, explicitly develops the odd-state Černý pair-automaton transitions while studying random-input absorption times. That graph provides substantial prior structural information from which some odd-case shortest paths can be derived. The present classification differs by supplying an explicit rank for every labeled pair in **both parities** and proving uniqueness and the single suffix-chain for **all** shortest two-state merging words. No claim is made that the maximum itself or the pair-automaton construction is new.

## Limitations

The result is restricted to merging **two prescribed states** of the given labeled Černý family; it does not classify shortest words resetting all states, longer merging words, other automata, or arbitrary multi-state rendezvous times. The odd-case transition graph in the 2014 paper makes implicit coverage of part of the new presentation a genuine bibliographic risk; a deeper historical equivalence may exist. No independent scientific audit has been performed.

## References

1. N. C. Behague and J. R. Johnson, *Synchronizing Times for \(k\)-sets in Automata*, arXiv:2008.12166 (2020 preprint, revised 2022), https://arxiv.org/abs/2008.12166 .
2. V. V. Gusev, *Synchronizing Automata with Random Inputs*, arXiv:1404.6731 (2014), https://arxiv.org/abs/1404.6731 .
