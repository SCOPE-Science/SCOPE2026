# Noncontingency on finite paths: exact small-frame algebras and an unbounded depth hierarchy

## Finding
Let \(P_n\) be the irreflexive, symmetric path with \(n\ge2\) vertices. In the Boolean modal language with one atom \(p\), unrestricted Boolean connectives, and only the noncontingency modality \(\Delta\), interpreted by
\[
P_n,\nu,v\models\Delta\varphi\quad\Longleftrightarrow\quad
\text{all neighbors of }v\text{ agree on the truth of }\varphi,
\]
write \(t_n(d)\) for the number of distinct depth-at-most-\(d\) pointed theories over all valuations \(\nu:P_n\to\{0,1\}\) and all vertices \(v\). The exact profiles through the first nontrivial path sizes are:

| Path | Depth-zero onward, through stabilization | First stable depth |
| --- | --- | --- |
| \(P_2\) | \(2,2\) | \(0\) |
| \(P_3\) | \(2,4,4\) | \(1\) |
| \(P_4\) | \(2,4,12,14,14\) | \(3\) |
| \(P_5\) | \(2,4,14,36,40,40\) | \(4\) |
| \(P_6\) | \(2,4,14,52,110,122,122\) | \(5\) |

In particular, \(P_4\) has exactly \(14\) complete pointed theories and exactly \(2^{14}=16384\) formula-equivalence classes; modal depth three is necessary and sufficient on this fixed frame. \(P_4\) is the smallest path with depth-three formulas not reducible to depth two, also when shorter paths are included in the comparison.

For every integer \(d\ge1\), there is a pointed valuation on \(P_{d+2}\) and a second valuation on the same pointed frame which agree on **every** formula of modal depth below \(d\), but disagree on \(\Delta^d p\). Hence the one-variable noncontingency modal-depth hierarchy is strict over the class of all finite irreflexive paths. The finite witnesses have only \(d+2\) worlds.

## Assumptions and scope
The graph relation is undirected adjacency, without loops; it is not a reflexive epistemic relation. The only propositional atom is \(p\); truth assignments are arbitrary and Boolean. Modal depth counts nested occurrences of \(\Delta\), and formulas may have arbitrary Boolean size. Formula equivalence over \(P_n\) means equal truth at every vertex under all \(2^n\) valuations. The count \(t_n(d)\) refers to pointed theories, not formulas; since Boolean connectives are available, the number of formula-equivalence classes at bound \(d\) is exactly \(2^{t_n(d)}\).

## Proof
**Exact semantic refinement.** Enumerate the finite state set \(U_n=\{(\nu,v):\nu\in\{0,1\}^{n},\ v\in\{0,\ldots,n-1\}\}\). Give a state its atomic label \(c_0(\nu,v)=\nu(v)\). At each stage, give it the signature consisting of its previous label and an *unordered discordant successor pair*: if the two neighbors have unequal depth-\(d\) labels, record their unordered pair; otherwise record a single neutral symbol. Replace equal signatures by the same canonical label; these are \(c_{d+1}\).

This recursion gives **exactly** depth-\(d\) equivalence by induction. In the induction step, Boolean closure makes every union of previous color classes definable. For any such union \(S\), \(\Delta\varphi_S\) fails precisely when the two successor labels lie on opposite sides of \(S\). The family of all these cuts distinguishes every unordered pair of distinct labels from every other pair, while all homogeneous and singleton successor sets satisfy every \(\Delta\varphi_S\). Retaining the previous label accounts for unnested old formulas. This proves soundness and completeness of the partition recurrence, including the case of end vertices (which have only one neighbor).

**Finite closed certificates.** The exhaustive recursion, run on \(n\cdot2^n\) states, gives the table above. A second independent implementation uses the truth values of the singleton characteristic tests \(\Delta\chi_C\) rather than unordered-pair labels. A third implementation enumerates every Boolean truth vector at each depth on \(P_4\), applies \(\Delta\) directly and repartitions the \(64\) pointed states. It gives \(2,4,12,14,14\). At the last equal stage no further splitting is possible, because the next signature is a deterministic function of the current partition. The complete \(16\)-valuation by \(4\)-root table of stable \(P_4\) class identifiers is in `types_P4.csv`; its labels are arbitrary identifiers, not numerical invariants. The fixed-point class-size multiset is twelve occurrences of \(2\) and two occurrences of \(20\). The fact that \(P_2\) and \(P_3\) stabilize at depths zero and one also holds for their union: the same recurrence on their disjoint state sets gives stabilization at depth one, so four worlds is the first possible path size for a depth-three distinction.

**All-depth witnesses.** Fix \(d\ge1\). Put vertices \(0,1,\ldots,d+1\) in path order and point at vertex \(1\). Compare the zero valuation with the valuation taking value one only at vertex \(d+1\). They agree on the radius-\((d-1)\) neighborhood of the pointed vertex, so ordinary locality induction makes every formula of depth less than \(d\) agree there. For a Boolean vector \(f\), at each internal vertex \(\Delta f\) has truth value \(1+f_{i-1}+f_{i+1}\) in \(\mathbf{F}_2\), while both endpoints always have value \(1\). Let \(A\) be the matrix whose internal rows mark the two neighbors and whose endpoint rows are zero. Thus \(\Delta f=\mathbf{1}+Af\), with \(A\mathbf{1}=0\), and induction yields \(\Delta^d f=\mathbf{1}+A^d f\) for \(d\ge1\). The zero valuation gives truth value \(1\) everywhere. For the single defect at \(d+1\), the entry \((A^d)_{1,d+1}\) is \(1\): the unique walk of length \(d\) between these vertices runs straight toward the pointed vertex, and all its intermediate row indices are internal. Hence \(\Delta^d p\) is false at the pointed vertex in the defective valuation and true in the zero valuation. This proves strictness for every \(d\).

## Verification
Run `python3 refinement_checker.py`, `python3 singleton_checker.py`, `python3 semantic_checker.py`, and `python3 hierarchy_checker.py`. The first two independently recompute the exact finite profiles, the third constructs full Boolean truth-vector semantics for every depth bound through four on \(P_4\), and the fourth directly evaluates the all-depth witnesses for \(1\le d\le100\). Each ends with a distinct `*_OK` marker. None of the finite tests substitutes for the general induction and unique-walk argument.

## Relationship to prior work
Wang and Zenger (2026) give uniform proof-theoretic systems for noncontingency over relational frame classes, including symmetric relations; their results do not enumerate one-variable pointed theories on finite paths or determine this path-specific depth hierarchy. Fan, Wang and van Ditmarsch (2013) develop knowing-whether semantics, frame expressivity and axiomatization. Their general expressivity comparisons and the fact that one-successor worlds cannot observe contingency are compatible with the present endpoint behavior but do not determine the enumerated quotient or the all-depth path witnesses. The Boolean identity \(\Delta\varphi\equiv\Box\varphi\lor\Box\neg\varphi\), ordinary modal locality, and the parity-of-walks identity are standard ingredients, not originality claims. Previously known small modal-type classifications on other frame families, including complete multipartite frames, do not imply these path results: neither frame family contains the other.

## Limitations
There is no asserted closed formula for \(t_n(d)\) for arbitrary \(n\). The displayed finite table is exhaustive only at the specified sizes; the general theorem is the strict hierarchy, the complete semantic refinement procedure, and its finite witnesses. The \(d+2\)-world bound is sufficient, not claimed minimal for distinguishing depth \(d\). All results require one Boolean atom and the irreflexive path relation. Other frame classes, additional atoms, and non-Boolean truth degrees are not classified here. Priority outside the inspected sources is not independently established.

## References
1. Y. Wang and L. Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975, first publicly posted 2026-09-30. https://arxiv.org/abs/2609.38975
2. J. Fan, Y. Wang and H. van Ditmarsch, *Knowing Whether*, arXiv:1312.0144, first publicly posted 2013-11-30. https://arxiv.org/abs/1312.0144
3. O. Martin, A. M. Odlyzko and S. Wolfram, *Algebraic properties of cellular automata*, Communications in Mathematical Physics 93 (1984), 219–258; standard linear parity-automaton background, not required for the argument.
