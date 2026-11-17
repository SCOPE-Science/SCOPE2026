# All smallest string attractors of repeated two-run binary words

## Finding

Fix integers \(a,b\ge 1\) and \(k\ge 2\). Let \(p=a+b\), \(W=(0^a1^b)^k\), and use one-based positions. A **string attractor** is a set of positions \(\Gamma\) such that every nonempty contiguous factor of \(W\) has an occurrence containing a position of \(\Gamma\).

The minimum attractor size is exactly \(2\). All minimum attractors and their cardinalities are classified below.

**Case 1: both runs have length at least two.** If \(a,b\ge2\), the complete family is
\[
\Gamma_{i,j,\varepsilon}=
\{a+(i-1)p+\varepsilon,\;jp+\varepsilon\},
\quad 1\le i\le k,\;1\le j\le k-1,\;\varepsilon\in\{0,1\}.
\]
All these sets are different. Thus the number of minimum attractors is \(2k(k-1)\), independent of the run lengths.

**Case 2: the zero-run is a singleton.** If \(a=1\), put \(z_i=1+(i-1)p\) and let \(O\) be the set of all \(kb\) positions occupied by the letter \(1\). The complete family consists of
\[
\{1,jp\}\quad (1\le j\le k-1),\qquad
\{z_i,t\}\quad (2\le i\le k,\;t\in O).
\]
Its size is \((k-1)(kb+1)\). This description includes \(a=b=1\) and yields \(k^2-1\) in that subcase.

**Case 3: the one-run is a singleton.** If \(b=1\) and \(a\ge2\), let \(Z\) be the set of all \(ka\) positions occupied by \(0\). The complete family consists of
\[
\{kp,jp+1\}\quad (1\le j\le k-1),\qquad
\{ip,t\}\quad(1\le i\le k-1,\;t\in Z).
\]
Its size is \((k-1)(ka+1)\).

Equivalently, if \(N(a,b,k)\) denotes the number of smallest attractors,
\[
N(a,b,k)=\begin{cases}
2k(k-1),&\min(a,b)\ge2,\\
(k-1)(k\max(a,b)+1),&\min(a,b)=1.
\end{cases}
\]
A notable structural consequence is that **every two-element attractor covering all factors of length at most two automatically covers all factors**, for this family of words. This is not asserted for arbitrary periodic words.

## Assumptions and scope

The alphabet is the labeled binary alphabet \(\{0,1\}\), the word has exactly \(k\) complete copies of \(0^a1^b\), and no circular wraparound occurrence is allowed. The two selected positions are an unordered set and must lie in \(\{1,\ldots,kp\}\). Every run length is positive, and \(k\ge2\). The theorem counts position sets, not occurrences of factors. No result is claimed for incomplete last periods or periods containing more than two runs.

## Proof

Write \(n=kp\). The two single-letter factors force any two-position attractor to choose one \(0\)-position and one \(1\)-position. Hence no singleton attractor exists, and all the two-position sets listed in the Finding have size exactly two.

**Step 1: necessity from length-one and length-two factors.** The occurrences of \(01\) straddle the boundaries \((a+(i-1)p,a+(i-1)p+1)\) for \(1\le i\le k\). The occurrences of \(10\) straddle \((jp,jp+1)\) for \(1\le j\le k-1\). If \(a,b\ge2\), these boundary pairs are disjoint: a single selected position cannot attract both \(01\) and \(10\). Therefore one of the two selected positions is an endpoint of an \(01\) boundary, and the other is an endpoint of a \(10\) boundary. Since one selected position must contain \(0\) and the other \(1\), the only possibilities are that both positions are the left endpoints or both are the right endpoints of their respective boundaries. This is exactly Case 1. All \(2k(k-1)\) pairs are distinct, since the \(01\)-boundary position and the \(10\)-boundary position belong to opposite run types for either choice of \(\varepsilon\).

If \(a=1\), the selected zero must be \(z_i=1+(i-1)p\). For \(i\ge2\) it touches both an occurrence of \(10\) and an occurrence of \(01\), so length-one and length-two factors impose no further restriction on the second (one) position. For \(i=1\), it does not touch any \(10\), which forces the one position to be the last symbol of a nonfinal one-run, namely \(jp\), \(1\le j\le k-1\). This gives Case 2, including \(b=1\). If \(b=1\) and \(a\ge2\), reverse the argument: a selected one at \(ip\) for \(i\le k-1\) touches both transition types and permits any zero, whereas the last one at \(kp\) requires a selected zero immediately after one of the \(k-1\) occurrences of \(10\), at \(jp+1\). This gives Case 3. The families are disjoint by the location of the uniquely selected singleton-run symbol and their stated counts follow.

**Step 2: periodic central-position lemma.** Let \(P\) be a primitive word of length \(p\), and let \(W=P^k\) for \(k\ge2\). Every factor \(F\) of length \(\ell\ge p\) has a unique cyclic starting phase \(s\in\{1,\ldots,p\}\), because distinct conjugates of a primitive word of length \(p\) differ. Its occurrences start exactly at \(s+tp\) for integers \(0\le t\le J=\lfloor(n-s-\ell+1)/p\rfloor\). The intervals
\[
[s+tp,\,s+tp+\ell-1]
\]
overlap or touch since \(\ell\ge p\). Their union is an integer interval \([s,E]\), where
\[
E=s+Jp+\ell-1=n-((n-s-\ell+1)\bmod p)\ge n-p+1.
\]
Consequently, **every position \(g\) in \([p,n-p+1]\) lies within some occurrence of every factor of length at least \(p\)**. (An arbitrary factor starting in a later period also has a copy at its earlier congruent phase, since the earlier start leaves at least as many letters until the end.) The period \(0^a1^b\) is primitive for all positive \(a,b\).

Every candidate pair in Cases 1–3 contains a central position: in Case 1 it is \(jp+\varepsilon\); in Case 2 with \(i\ge2\) it is \(z_i\), and with \(i=1\) it is \(jp\); in Case 3 with \(i\le k-1\) it is \(ip\), and with the last one it is \(jp+1\). Thus all listed pairs attract every factor of length at least \(p\).

**Step 3: shorter factors when both runs are non-singleton.** A factor of length below \(p=a+b\) has either no transition, exactly one transition, or two oppositely oriented transitions; it cannot contain two transitions of the same orientation since their starting positions differ by one whole period. Every pure-zero or pure-one factor embeds in a complete run crossing the selected zero or one position. Any mixed factor containing a \(10\) transition embeds around the selected internal \(10\) boundary \((jp,jp+1)\): both adjacent zero runs and both neighboring one runs needed for a factor with at most two transitions are present, because \(1\le j\le k-1\). The embedding crosses \(jp+\varepsilon\). Any remaining mixed factor has only one \(01\) transition and is \(0^u1^v\), with \(1\le u\le a\) and \(1\le v\le b\). It embeds across the selected \(01\) boundary and crosses \(a+(i-1)p+\varepsilon\), even when that is the last \(01\) boundary. Thus every shorter factor is attracted.

**Step 4: singleton-run cases.** Suppose \(a=1\). A factor of length less than \(p=b+1\) contains at most one zero. A selected zero \(z_i\) with \(i\ge2\) has a full run of \(b\) ones on either side; every short factor containing zero therefore crosses it in some occurrence. Any chosen one lies in a full one-run, and thus attracts every pure-one factor \(1^u\), \(1\le u\le b\). When the selected zero is the first position, factors beginning with zero occur crossing this zero, while short factors having ones before zero embed around the selected internal \(10\) boundary \((jp,jp+1)\) and cross \(jp\); pure-one factors are handled there as well. This includes \(b=1\).

If \(b=1\) and \(a\ge2\), the symmetric argument applies: any internal singleton one has a full zero-run on each side, attracting all short factors with a one, and any chosen zero attracts all pure-zero factors. For a selected final one, every short factor with \(01\) embeds across that final boundary; every remaining short mixed factor contains \(10\) and embeds across the selected internal boundary \((jp,jp+1)\). The chosen zero there also attracts the pure-zero factors. Together with Step 2, these arguments prove sufficiency for every enumerated pair.

The single-letter lower bound proves that these are exactly the smallest attractors. Finally, Step 1 shows that every two-position attractor for factors of length at most two belongs to the list, while Steps 2–4 show every listed pair is a full attractor, proving the structural consequence.

## Verification

The standalone file `verify.py` constructs every distinct factor and the union of all position intervals over its occurrences. It checks each unordered position pair against the full factor set, comparing the answer with the explicit families and count formula. Exhaustive checks cover every \(1\le a,b\le6\) and \(2\le k\le6\); additional seeded checks sample \(180\) larger parameter triples. All \(360\) parameter cases passed, involving \(188{,}975\) distinct factor-pattern instances and \(18{,}192\) positive attractor-pair matches. The proof above, not the finite computation, establishes the infinite-parameter theorem.

To repeat the checks, run `python verify.py` using Python 3, with no external dependencies.

## Relationship to prior work

The definition and significance of string attractors originate with Prezza and subsequent work of Kempa and collaborators. Mantaci et al. (2019), Proposition 4, give a general bound for the attractor size of a power \(u^k\); their Corollary 2 and examples give minimum attractors for words with separate letter runs. Those statements do not give all optimal position sets of the repeated two-run word, nor the counts here. Restivo et al. (2022) relate the profiles and locations of optimal attractors to periodicity, without this two-parameter census. Work on exact position-pair enumeration in specific binary families demonstrates the relevance of the quantity rather than implying the formulas here.

The restricted alternating subfamily \(a=b=1\), with its count \(k^2-1\), has appeared in an earlier public exact attractor enumeration; this boundary case is included only to make the present classification complete, **not claimed independently as new**. The new contribution is the uniform characterization across nontrivial positive run lengths, especially the rigid \(2k(k-1)\) regime and the singleton-run transition.

## Limitations

The result is specific to full integer powers of the two-run binary period, and the central-position argument does not establish a classification for general periodic strings. No independent expert review or formal proof assistant certificate has been obtained. A targeted literature and research-record search did not reveal a stronger existing classification, but possible unindexed or inaccessible equivalent work remains a bibliographic risk.

## References

1. N. Prezza, *String Attractors*, arXiv:1709.05314 (2017), https://arxiv.org/abs/1709.05314.
2. D. Kempa, A. Policriti, N. Prezza, E. Rotenberg, *String Attractors: Verification and Optimization*, arXiv:1803.01695 (2018-03-05), https://arxiv.org/abs/1803.01695.
3. S. Mantaci, A. Restivo, G. Romana, G. Rosone, M. Sciortino, *String Attractors and Combinatorics on Words*, arXiv:1907.04660 (first public 2019-07-10), https://arxiv.org/abs/1907.04660.
4. A. Restivo, G. Romana, M. Sciortino, *String Attractors and Infinite Words*, arXiv:2206.00376 (first public 2022-06-01), https://arxiv.org/abs/2206.00376.
5. M. Banbara et al., *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue--Morse Words*, arXiv:2602.16152 (2026), https://arxiv.org/abs/2602.16152. This later work is cited only for the context of counting all optimal attractors, not as the date-setting source.
