# The complete three-short-distance seating-couples criterion

## Finding
Fix an integer \(n\ge3\). Number the vertices of a complete graph \(K_{2n}\) by \(0,1,\ldots,2n-1\) in cyclic order and define the circular length of an edge \(\{i,j\}\) by
\[
\ell(i,j)=\min\{|i-j|,2n-|i-j|\}.
\]
For nonnegative integers \(a,b,c\) with \(a+b+c=n\), a perfect matching with exactly \(a\) edges of circular length \(1\), \(b\) of length \(2\), and \(c\) of length \(3\) exists **if and only if**
\[
\boxed{\quad b\equiv0\pmod2\quad\text{and}\quad (3\nmid n\;\text{or}\;b>0\;\text{or}\;a\ne1).\quad}
\]
Thus the only obstruction beyond parity is the list consisting of one length-\(1\) edge and \(n-1\) length-\(3\) edges when \(3\mid n\). In particular, for every prime \(p\ge5\), *every* prescribed length multiset supported on \(\{1,2,3\}\), of size \(p\), is realizable in \(K_{2p}\) precisely when the number of occurrences of length \(2\) is even. This verifies the three-short-length case of the prime-order seating-couples conjecture in [1].

## Assumptions and scope
Graphs are finite and simple. A perfect matching consists of \(n\) pairwise disjoint edges covering all \(2n\) vertices. All multiplicities \(a,b,c\) are arbitrary nonnegative integers, subject only to \(a+b+c=n\) and \(n\ge3\). The edge lengths use **circular** distance, not ordinary linear difference. The positive proof actually realizes nearly all profiles with ordinary differences \(1,2,3\); a single all-length-\(3\) case uses a circular wrap.

## Proof
**Parity obstruction.** An edge of odd circular length joins vertices of opposite parity; an edge of length \(2\) joins vertices of the same parity. Suppose the matching uses \(u\) even-to-even and \(v\) odd-to-odd length-\(2\) edges. Its \(n-b\) odd-length edges cover equally many even and odd vertices, so the numbers of same-parity vertices still needing partners agree: \(2u=2v\). Hence \(b=u+v=2u\) is even.

**Exceptional obstruction.** Suppose \(3\mid n\), \(a=1\), and \(b=0\). Edges of length \(3\) always join vertices with the same residue modulo \(3\). As \(3\mid 2n\), each of the three residue classes has \(2n/3\) vertices, an even number. The unique length-\(1\) edge has endpoints in two different residue classes. Removing those endpoints leaves an odd number of vertices in each of those two classes. Edges of length \(3\) cannot match either odd class internally, which is impossible.

**Constructive sufficiency.** Write each short *linear block* as its number of consecutive positions together with its perfect-matching edges, numbered from zero within the block. The signatures below record the numbers of length-\(1\), length-\(2\), and length-\(3\) edges respectively.

| Block | Positions | Edges | Signature \((a,b,c)\) |
| --- | ---: | --- | --- |
| A | 2 | \((0,1)\) | \((1,0,0)\) |
| B | 4 | \((0,2),(1,3)\) | \((0,2,0)\) |
| C | 4 | \((0,3),(1,2)\) | \((1,0,1)\) |
| D | 6 | \((0,3),(1,4),(2,5)\) | \((0,0,3)\) |
| E | 6 | \((0,2),(1,4),(3,5)\) | \((0,2,1)\) |
| F | 8 | \((0,2),(1,4),(3,6),(5,7)\) | \((0,2,2)\) |

Every row is a perfect matching of the stated interval, and each listed edge has the displayed ordinary distance. Translate and concatenate such blocks to fill \([0,2n-1]\). Every resulting edge has ordinary difference at most \(3\), which equals its circular length because \(n\ge3\).

Assume first that \(b\ge2\) is even. Write \(c=3q+r\), where \(q\ge0\) and \(r\in\{0,1,2\}\). Take \(b/2-1\) copies of B, \(q\) copies of D, \(a\) copies of A, and one more block chosen as B when \(r=0\), E when \(r=1\), or F when \(r=2\). The signatures add to exactly \((a,b,c)\), and the blocks cover \(2n\) positions.

Now assume \(b=0\). Again write \(c=3q+r\). If \(a\ge r\), concatenate \(q\) copies of D, \(r\) copies of C, and \(a-r\) copies of A. This produces exactly \((a,0,c)\).

It remains to consider \(a<r\). Since \(r\le2\), either \(a=0\) with \(r\in\{1,2\}\), or \(a=1\) with \(r=2\). In the first case \(n=c\): pair each even-labeled vertex \(2j\) with \((2j+3)\bmod 2n\), for \(j=0,\ldots,n-1\). The second endpoints are precisely the odd-labeled vertices, so this is a perfect matching, and every edge has circular length \(3\). In the second case \(n=1+3q+2=3(q+1)\), exactly the previously excluded obstruction. These cases exhaust every profile and prove sufficiency.

## Verification
The standalone script `verify.py` implements the six short blocks and the cyclic all-length-\(3\) construction, validates all their edge lengths and vertex coverage, and tests every nonnegative multiplicity profile for every \(3\le n\le80\). It verified \(46{,}748\) feasible constructed profiles. A separate definition-based subset recursion, independent of the block construction, exhaustively computes the support of the feasible profile distribution for each \(3\le n\le18\), checking \(702\) attainable profiles and the complete complement. All comparisons passed with `VERIFY_OK`. This finite testing is corroboration; the proof above treats all \(n\ge3\).

## Relationship to prior work
Meszka, Pasotti, and Pellegrini [1] study this exact circular-length perfect-matching problem; their Proposition 2.4 proves the parity obstruction, Theorem 1.4 handles lists with at most two distinct lengths, and Section 4 handles certain equal-multiplicity lists. Their Conjecture 3 asserts parity sufficiency for lists of lengths strictly below an odd prime. The present result gives the full arbitrary-multiplicity classification on support \(\{1,2,3\}\), including composite \(n\), using explicit block constructions. The exceptional length-\(1\)/length-\(3\) two-support case is consistent with (and may also be recovered from) their Theorem 1.4; it is not separately claimed to be new.

Kohen and Sadofschi Costa [2] prove existence for lists whose differences are all units modulo \(2n\); that theorem does not cover profiles containing length \(2\). Earlier Hamiltonian-path realizations of prescribed differences [3] concern paths with \(2n-1\) edges and do not directly produce an arbitrary prescribed perfect-matching length list. The closest known general Skolem-type formulations [4] concern linear pairings and related multiset existence questions. No equivalent unrestricted three-short-distance matching theorem was located in the inspected literature, but an unindexed or unstated stronger theorem remains a possibility.

## Limitations
The result concerns existence, not the number of perfect matchings realizing a prescribed profile. It does not classify lists containing any distance greater than \(3\). The result for odd primes is only the support-\(\{1,2,3\}\) case of the broader conjecture. The parity obstruction and two-distance specializations are known prior work; novelty attaches to the complete unrestricted three-short-distance criterion and construction. Publication priority has not been independently established.

## References
[1] M. Meszka, A. Pasotti, and M. A. Pellegrini, *The seating couple problem in even case*, arXiv:2308.16553, first posted 2023-08-31. https://arxiv.org/abs/2308.16553 ; full public preprint transcription https://www.researchgate.net/publication/373551798_The_seating_couple_problem_in_even_case

[2] D. Kohen and I. Sadofschi Costa, *On a generalization of the seating couples problem*, arXiv:1603.06625 (2016). https://arxiv.org/abs/1603.06625

[3] M. A. Ollis, A. Pasotti, M. A. Pellegrini, and J. R. Schmitt, *New methods to attack the Buratti-Horak-Rosa conjecture*, Discrete Mathematics 344 (2021), 112486. https://doi.org/10.1016/j.disc.2021.112486

[4] G. Nordh, *Perfect Skolem sets*, Discrete Mathematics 308 (2008); arXiv:math/0506155. https://arxiv.org/abs/math/0506155
