# Unique radius-two identifying codes at length three in directed de Bruijn graphs

## Finding
Let \(q\ge 2\) be an integer and \(A\) an alphabet of cardinality \(q\). The directed de Bruijn graph \(\vec B(q,3)\) has vertices \(A^3\) and arcs \(abc\to bcz\) for \(a,b,c,z\in A\). A radius-two identifying code \(C\subseteq A^3\) has the property that the sets \(I_C(v)=C\cap B_2^+(v)\), with \(B_2^+(v)\) the vertices reachable in at most two directed steps from \(v\), are all nonempty and pairwise distinct.

**Theorem.** For every integer \(q\ge3\), the **unique** minimum radius-two identifying code in \(\vec B(q,3)\) is
\[
C_q=\{abc\in A^3:a\ne c\},\qquad |C_q|=q^2(q-1).
\]
For the exceptional binary alphabet \(q=2\), the minimum cardinality is seven and the two optimal codes are \(A^3\setminus\{000\}\) and \(A^3\setminus\{111\}\). This binary case was already described in the cited foundational paper and is included only as a sharp boundary, **not as a novelty claim**. The nonbinary result settles the first boundary case \(n=2t-1\) at \(t=2,n=3\) that is not covered by the earlier minimum-size constructions for \(n\ge2t\).

The same theorem holds if the code is defined using radius-two **incoming** balls: reversing every word carries the outgoing-ball problem to the incoming-ball problem and preserves \(C_q\).

## Assumptions and scope
The graph is the **directed** de Bruijn graph, not its undirected simplification. Loops, where present, are allowed. The ball includes paths of lengths zero, one and two; the code condition uses sets, not path multiplicities. All letters are individually named; uniqueness means equality of codeword subsets of this labeled vertex set, not merely uniqueness up to isomorphism. No restrictions are placed on the algebraic structure of the alphabet; only its finite cardinality matters.

## Proof
Write
\[
Q_c=\{cuv:u,v\in A\},\qquad R_{b,c}=\{bcz:z\in A\}.
\]
The definition of directed edges gives the exact radius-two formula
\[
B_2^+(abc)=Q_c\cup R_{b,c}\cup\{abc\}.\tag{1}
\]
In particular the entire set \(Q_c\) is reached after two steps, the set \(R_{b,c}\) after one step, and the starting vertex at distance zero. This equality includes all coincidences when letters repeat.

**Forced vertices.** Fix \(a,b,c\in A\) with \(a\ne c\). Compare the vertices \(abc\) and \(cbc\). Their balls have the same \(Q_c\) and \(R_{b,c}\) terms. The self-vertex \(cbc\) belongs to \(Q_c\), while \(abc\) belongs to neither \(Q_c\) (its first letter differs from \(c\)) nor \(R_{b,c}\) (membership there would force both \(a=b\) and \(b=c\), hence \(a=c\)). Consequently
\[
B_2^+(abc)\mathbin\triangle B_2^+(cbc)=\{abc\}.\tag{2}
\]
Every identifying code must contain \(abc\), since otherwise the two radius-two identifying sets coincide. This holds for every \(a\ne c\); therefore every identifying code contains \(C_q\) and has at least \(q^2(q-1)\) members.

**Separation when \(q\ge3\).** We show that \(C_q\) itself identifies all vertices. All its signatures are nonempty because \(Q_c\cap C_q\) has \(q(q-1)\) members. Let \(abc\ne a'b'c'\).

First, if \(c\ne c'\), the signature of \(abc\) contains all \(q(q-1)\) codewords of \(Q_c\cap C_q\). The ball of \(a'b'c'\) contains at most \(q\) codewords in \(Q_c\cap C_q\): the two-step term \(Q_{c'}\) has different first letter; its one-step term \(R_{b',c'}\) contributes at most \(q-1\) such codewords, and its self-vertex contributes at most one. Since \(q(q-1)>q\) for \(q\ge3\), the signatures differ.

Next suppose \(c=c'\), but \(b\ne b'\). At least one of \(b,b'\) differs from \(c\); without loss, suppose \(b\ne c\). Then \(R_{b,c}\cap C_q\) has exactly \(q-1\ge2\) members, and none belongs to \(Q_c\). The other ball has the same \(Q_c\) and a different one-step prefix \(R_{b',c}\), so it meets \(R_{b,c}\cap C_q\) in at most the one self-vertex \(a'b'c\). At least one member of this set distinguishes the signatures.

Finally suppose \(b=b'\) and \(c=c'\), while \(a\ne a'\). At least one of \(a,a'\) differs from \(c\); say \(a\ne c\). Then \(abc\in C_q\), and by the forced-vertex argument it lies outside \(Q_c\cup R_{b,c}\). It belongs to \(B_2^+(abc)\), but not to \(B_2^+(a'bc)\), because it differs from that ball's self-vertex. All cases have distinct identifying sets. Therefore \(C_q\) is a code attaining the forced-size lower bound. Since every code contains \(C_q\), it is the **only** optimum.

**Binary boundary (previously known).** Equation (2) forces the four vertices \(C_2\). In addition, the signatures of the pairs \((011,101)\), \((010,100)\), and \((001,110)\), restricted to the forced four codewords, coincide. Their respective ball symmetric differences among the remaining four possible codewords are \(\{010\}\), \(\{101\}\), and \(\{000,111\}\). Thus every radius-two code also contains \(010\) and \(101\), plus at least one of \(000,111\). Direct substitution in (1) verifies that either seven-vertex set obtained by omitting exactly one constant word identifies all eight vertices: for omission of \(000\), the eight identifying sets have sizes \(3,7,5,5,4,6,6,4\) in lexicographic vertex order, and they are pairwise distinct. In fact, for the code omitting \(000\), the eight signatures in order \(000,001,010,011,100,101,110,111\) are explicitly

| Vertex | Identifying set (codewords written as triples) |
| --- | --- |
| \(000\) | \(\{001,010,011\}\) |
| \(001\) | \(\{001,010,011,100,101,110,111\}\) |
| \(010\) | \(\{001,010,011,100,101\}\) |
| \(011\) | \(\{011,100,101,110,111\}\) |
| \(100\) | \(\{001,010,011,100\}\) |
| \(101\) | \(\{010,011,100,101,110,111\}\) |
| \(110\) | \(\{001,010,011,100,101,110\}\) |
| \(111\) | \(\{100,101,110,111\}\) |

Symbol interchange gives the other code. Hence the two listed sets are exactly the binary minima.

**Incoming balls.** The reversal map \(\rho(abc)=cba\) reverses each directed arc. Thus \(\rho(B_2^+(v))=B_2^-(\rho(v))\). As \(\rho(C_q)=C_q\), all minimum-size, uniqueness and binary-boundary statements transfer unchanged to incoming balls.

## Verification
The supplied program `checks/verify_outballs.py` constructs the directed arc sets and two-step balls by breadth-first expansion, confirms the claimed signatures and forced singleton differences for all \(2\le q\le9\), and exhaustively enumerates all subsets in the eight-vertex binary case. The separate `checks/verify_inballs.py` constructs reverse adjacency and verifies the same statements with incoming balls for \(2\le q\le7\). Their recorded outputs are in `checks/outballs_output.txt` and `checks/inballs_output.txt`. These finite tests are independent computational checks **of examples**; the preceding proof establishes the statements for all permitted alphabet sizes.

## Relationship to prior work
Boutin, Goliber and Pelto (first arXiv version 18 December 2014, later revised and published) proved the general lower bound \(q^{n-1}(q-1)\) for directed radius-\(t\) codes (Theorem 3.5), constructed optimal radius-two codes for \(n\ge4\) (Theorems 3.6–3.7), treated \(n=2t-1\ge5\) with a possibly nonoptimal construction (Theorem 3.9), and gave an optimal radius-one code with the same set \(C_q\) when \(n=3\) (Theorem 3.11). Their Figure 2 records the binary radius-two exception. **None of those results proves the nonbinary radius-two boundary case \(n=3,t=2\)**: radius-one identification does not generally imply radius-two identification; the binary counterexample is a direct warning. The new contribution is the radius-two sufficiency and uniqueness for every nonbinary alphabet, not the earlier lower bound, radius-one code construction, or binary example.

Horan's 2015 paper concerns **undirected** de Bruijn graphs and proves identification/existence results for a different neighborhood relation; it does not imply the claimed directed optimum. Direct searches for length-three directed radius-two identifying-code minima, incoming/outgoing duals, graph-line-digraph descriptions, and exact small-alphabet tables did not identify stronger published coverage. Historical priority outside the searched sources is not proved.

## Limitations
The theorem concerns **exactly word length three and radius two**. It does not resolve the cases \(n=2t-1\ge5\), or other network models (undirected, Kautz, partially observed alphabets), or robustness to sensor loss. Database coverage and historical priority may be incomplete. Computational tests do not replace the infinite proof.

## References
1. Debra Boutin, Victoria Horan Goliber, Mikko Pelto, *Identifying Codes on Directed De Bruijn Graphs*, arXiv:1412.5842, first posted 2014-12-18, https://arxiv.org/abs/1412.5842 ; later publication *Discrete Applied Mathematics* (2019), DOI:10.1016/j.dam.2019.02.005. Relevant: Theorems 3.5–3.11 and Figure 2 in the available full text.
2. Victoria Horan, *On the Existence of t-Identifying Codes in Undirected De Bruijn Graphs*, arXiv:1508.00403, first posted 2015-08-03, https://arxiv.org/abs/1508.00403. Relevant: Definitions 1.1–1.4, Theorem 2.1, and distinction between directed and undirected balls.
