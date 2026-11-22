# Sharp eventual periodicity and alphabet threshold for avoidance of Abelian squares of orders two and three

## Finding

Let \(\Sigma_q=\{0,1,\ldots,q-1\}\). An *Abelian square of order* \(r\) is a consecutive factor \(uv\) with \(|u|=|v|=r\) and identical multiplicities of each letter in \(u\) and \(v\). Let \(L_q\) be the finite words over \(\Sigma_q\) that avoid Abelian squares of **exact orders two and three**, with no condition imposed at other orders, and let \(a_q(n)\) count words in \(L_q\) of length \(n\).

**Theorem.** The binary counts satisfy
\[
(a_2(0),\ldots,a_2(7))=(1,2,4,8,10,12,10,8),\qquad a_2(n)=6\quad(n\ge8).
\]
For every \(n\ge8\), the six words counted are exactly the six different length-\(n\) factors of the periodic word \((000111)^\omega\), one at each starting phase. For every \(q\ge3\) and \(n\ge5\),
\[
a_q(n)\ge 2^{\lfloor (n-5)/6\rfloor},
\]
so the entropy of the factorial language is positive, whereas binary entropy vanishes. Furthermore, if *either* order-two or order-three Abelian squares are forbidden in isolation over the binary alphabet, the resulting language has positive entropy. Thus the two-order ban is inclusion-minimal among its two single-order subrestrictions as a binary zero-entropy constraint.

## Assumptions and scope

Words are linear, not circular. A factor is contiguous. Two blocks are Abelian equivalent exactly when their complete Parikh vectors agree. Orders two and three mean **half-lengths** two and three (forbidden total factor lengths four and six). The empty word is counted at length zero. The alphabet is labeled and word positions are indexed; equality is literal, not up to reversal, complementation, rotation or relabeling. Only the prescribed two orders are forbidden; longer Abelian squares may occur.

## Proof

**Finite binary overlap graph.** For a fixed alphabet and the forbidden orders \(\{2,3\}\), take as vertices all allowable five-letter words. Join \(v\) to \(v_2v_3v_4v_5c\) if appending \(c\) to \(v\) creates no forbidden length-four or length-six factor. Every permitted word of length at least five corresponds bijectively to a directed walk starting at its initial five-letter factor. In the binary case direct comparison of the four- and six-letter Parikh vectors gives **exactly twelve vertices and ten edges**. There is one directed six-cycle:

`00011` → `00111` → `01110` → `11100` → `11000` → `10001` → `00011`.

The only other edges form two disjoint finite chains:

`00010` → `00100` → `01000`, and `11101` → `11011` → `10111`.

All twelve listed vertices occur, and there are no other vertices or edges. The graph enumeration is a fully specified finite certificate: list all \(2^5=32\) candidate five-letter vertices, check the order-two restriction, and list all \(2^6=64\) candidates for six-letter edges, rejecting those containing an order-two or order-three Abelian square. The independent executable verification enumerates these without relying on the displayed list.

The directed six-cycle accounts for precisely six paths of every nonnegative length. Each of the two transient three-vertex chains has three possible starting vertices for a zero-edge walk, two for a one-edge walk, one for a two-edge walk, and none for three or more. Hence the numbers of allowable words of lengths five, six, seven, and all lengths at least eight are respectively \(12,10,8,6\). Direct enumeration of length at most four gives \(1,2,4,8,10\). Every length at least eight word follows the six-cycle, whose edge-letter sequence is the period-six word \(000111\), proving the classification and sharp onset (the two extra seven-letter transient paths show that length seven does not yet stabilize).

**Alphabet threshold.** In the ternary five-context overlap graph, the vertex `00011` has two distinct permitted six-edge return paths, obtained by appending the words `100011` and `200011`. For each option, every intermediate six-letter factor avoids the two forbidden Abelian-square orders and the final five-letter context again equals `00011`. Thus concatenating any sequence of the two distinct return blocks produces an admissible word. For length \(n\ge5\), append \(m=\lfloor(n-5)/6\rfloor\) chosen blocks to the seed `00011`, then any initial \(n-5-6m\) symbols of `100011`. This gives \(2^m\) different length-\(n\) words, since the choices occupy disjoint fixed six-position blocks. For any \(q\ge3\) the same ternary examples embed into \(\Sigma_q\). Since \(a_q(n+m)\le a_q(n)a_q(m)\), the entropy \(h_q=\lim_{n\to\infty}n^{-1}\log a_q(n)\) exists by subadditivity; the lower bound proves \(h_q\ge (\log 2)/6\) for \(q\ge3\), while the binary eventual constant count proves \(h_2=0\).

**Both restrictions are necessary for binary zero entropy.** Forbidding only Abelian squares of order two, the valid three-symbol context `000` admits two distinct ten-edge return blocks `1000111000` and `1110001000`. Forbidding only order three, the valid five-symbol context `00011` admits two distinct eight-edge return blocks `10000011` and `11100011`. Checking all intermediate edges in the corresponding finite overlap graphs proves each is a valid return to its original context. The same arbitrary-concatenation argument produces respectively at least \(2^{\lfloor(n-3)/10\rfloor}\) and \(2^{\lfloor(n-5)/8\rfloor}\) words for all sufficiently large \(n\), so deleting either restriction yields positive entropy. This establishes inclusion-minimality of the stated pair; it does **not** classify all other possible sets of forbidden orders.

## Verification

Run `python3 verify_direct.py` and `python3 verify_graph.py` from the extracted package. The first program tests each binary word through length 13 by independent literal Parikh comparison, verifies the six explicit periodic phases at all tested stabilized lengths, and checks all concatenations of up to four return blocks for all three return constructions. The second program derives the complete twelve-state/ten-edge binary graph from all candidate words and verifies its edges and exact word counts by independent walk propagation through length 100. It also verifies each return path in its corresponding order-specific graph. The all-length assertions above are consequences of the exhaustively enumerated finite graph and the loop-concatenation proofs, **not** extrapolations from finite numerical tests.

## Relationship to prior work

Grant [1] studies binary words avoiding Abelian squares at **all orders at least a varying lower cutoff**, obtaining extremal growth bounds; that is a distinct restriction from forbidding exactly the two isolated small orders considered here. Rao and Rosenfeld [2] study long \(k\)-Abelian repetitions. Their equivalence for \(k=2,3\) is more restrictive than ordinary Abelian equality, and their long-period avoidance results neither entail this exact two-order language nor its binary stabilization. Classical finite automata for bounded forbidden factors provide the proof method; no novelty is claimed for that method. The new assertion is the exact rigidity/entropy threshold and the inclusion-minimality, subject to the historical-priority limitation below.

## Limitations

No count formula is claimed for \(q\ge3\); only an explicit positive-entropy lower bound is proved. No assertion is made about avoidance of Abelian squares at order one or orders at least four, nor about avoiding *all* Abelian squares. The finite overlap graph has been exhaustively specified and checked but the overall derivation has had self-review, not independent mathematical validation. An unindexed historical computation of this small finite-state language could cover the claim; the literature comparison cannot exclude that possibility.

## References

1. Elyot Grant, *On Avoiding Sufficiently Long Abelian Squares*, arXiv:1012.0524, first public version 2010-12-02. https://arxiv.org/abs/1012.0524
2. Michaël Rao and Matthieu Rosenfeld, *Avoidability of long \(k\)-abelian repetitions*, arXiv:1507.02581, first public version 2015-07-09. https://arxiv.org/abs/1507.02581
