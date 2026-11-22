# Self-attacking symmetric forests: a local coherence criterion and an exact path census

## Finding

Let \(G=(V,E)\) be a finite simple forest and \(S\subseteq V\). Define a Dung attack relation by taking both directions of every undirected edge and adding a self-attack at precisely the vertices of \(S\). Set \(U=V\setminus S\) and let \(I\subseteq U\) consist of the isolated vertices of \(G[U]\). Then

\[\operatorname{Pref}(G,S)=\operatorname{MIS}(G[U]),\qquad
\operatorname{Pref}(G,S)=\operatorname{Stable}(G,S)
\iff S\subseteq N_G(I).\]

Here \(\operatorname{MIS}\) denotes the family of inclusion-maximal independent vertex sets, while \(N_G(I)\) is the set of vertices with an undirected neighbour in \(I\). This is a necessary-and-sufficient *local* agreement test even when self-attacks are present.

For the path \(P_n\) with \(n\ge0\) labelled vertices, let \(c_n\) count those sets \(S\subseteq V(P_n)\) for which all preferred extensions are stable (including the empty path, with one marking). Then

\[\boxed{\sum_{n\ge0}c_nt^n=\frac{1+t^2-t^3+t^4}{1-t-t^2+t^4-t^5}.}\]

The first counts are \(1,1,3,3,6,9,13,22,32,51,79,121,190\). The recurrence \(c_n=c_{n-1}+c_{n-2}-c_{n-4}+c_{n-5}\) holds for all \(n\ge5\). In particular the fraction \(c_n/2^n\) of all possible self-attack markings which preserve agreement tends to zero exponentially. More precisely, \(c_n\sim C\lambda^n\), where \(\lambda\) is the largest-modulus root of \(z^5-z^4-z^3+z-1\), with \(\lambda\approx1.54990607259428\) and \(C\approx0.98314236892756\).

## Assumptions and scope

Dung conflict-free sets contain no attacking pair, including a self-attack. A set is admissible if it is conflict-free and attacks every attacker of any of its members. Preferred extensions are inclusion-maximal admissible sets; stable extensions are conflict-free sets attacking every vertex outside them. The forest need not be connected and may contain isolated vertices. All edges between distinct vertices are symmetric. The agreement statement compares *sets of extensions*, not only their nonemptiness. The path is an ordinary undirected simple path whose edges become mutual attacks; each of its vertices may independently acquire a self-loop.

## Proof

**Step 1: Preferred sets.** No conflict-free set contains a vertex of \(S\). For any independent \(A\subseteq U\), every attacker \(b\) of any \(a\in A\) is a neighbour of \(a\), hence \(a\) attacks \(b\) back. Thus every independent subset of \(U\) is admissible. Preferred sets are exactly the inclusion-maximal independent sets of \(G[U]\).

**Step 2: Stability reduces to domination of loops.** A maximal independent set of \(G[U]\) attacks every unselected member of \(U\). Therefore it is stable in the whole framework precisely when it also attacks every marked vertex in \(S\).

**Step 3: A local necessity-and-sufficiency lemma for forests.** For each \(s\in S\), every maximal independent set of \(G[U]\) meets \(N_G(s)\cap U\) if and only if this neighbourhood contains some vertex isolated in \(G[U]\). The reverse direction is immediate: every maximal independent set contains every isolated vertex of \(G[U]\). For the forward direction, contrapositively suppose that each \(u\in N_G(s)\cap U\) has another neighbour \(v_u\in U\). Because \(G\) is a forest, the vertices \(v_u\) are distinct, none belongs to \(N_G(s)\), and no two are adjacent: equality or adjacency would create respectively a cycle of length \(4\) or \(5\), and membership in \(N_G(s)\) would create a triangle. Hence the selected vertices \(\{v_u\}\) form an independent set disjoint from \(N_G(s)\); extend it to a maximal independent set of \(G[U]\). Each neighbour \(u\) of \(s\) is already adjacent to \(v_u\), so no extension can contain \(u\). Thus this maximal set fails to attack \(s\). If \(N_G(s)\cap U\) is empty, the empty selection itself gives the same conclusion. Applying this lemma simultaneously to all marked vertices proves the iff condition.

**Step 4: Five-local path language.** Encode a marking on \(P_n\) by a binary word \(b_0\cdots b_{n-1}\), where \(1\) denotes a self-loop, \(0\) an unlooped vertex. Pad the word at both ends with two virtual \(1\)'s. A real central vertex with bit \(c\) is locally acceptable exactly when

\[\mathsf{ok}(a,b,c,d,e)\iff(c=0)\ \lor\ (b=0\land a=1)\ \lor\ (d=0\land e=1),\]

where \((a,b,c,d,e)\) is its five-bit window. The two final alternatives say that a looped vertex is adjacent to an isolated unlooped vertex. At a path boundary the virtual \(1\)'s correctly represent the missing outer neighbours. A marking is coherent exactly when all its real-centred windows pass.

**Step 5: An exact rational-census certificate.** Index \(16\) states by quadruples \(s=(a,b,c,d)\in\{0,1\}^4\), in lexicographic order. Put \(T_{s,s'}=1\) when \(s'=(b,c,d,e)\) for a bit \(e\) with \(\mathsf{ok}(a,b,c,d,e)\), and \(0\) otherwise; if two transitions share an endpoint their multiplicities are added. Set \(\alpha_s=1\) for the four states \((1,1,x,y)\) and \(0\) otherwise, and let

\[B_{a,b,c,d}={\bf1}\{\mathsf{ok}(a,b,c,d,1)\land\mathsf{ok}(b,c,d,1,1)\}.\]

The exact column \(B\), in lexicographic order, is \((1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0)^\mathsf T\). For \(n\ge2\), the path count is \(c_n=\alpha T^{n-2}B\). The two shorter cases both have count \(1\). Direct integer multiplication of this explicitly defined sparse matrix gives the exact identity

\[\bigl(T^5-T^4-T^3+T-I_{16}\bigr)B=0.\]

It follows, for every \(n\ge7\), that \(c_n-c_{n-1}-c_{n-2}+c_{n-4}-c_{n-5}=0\). Direct evaluation of the same state formula yields \((c_0,\ldots,c_6)=(1,1,3,3,6,9,13)\), which also satisfies the recurrence at \(n=5,6\). Multiplication of the formal series by \(1-t-t^2+t^4-t^5\) now gives exactly \(1+t^2-t^3+t^4\), proving the generating function for every \(n\ge0\).

For the asymptotic assertion, direct exact determinant computation on the same explicit matrix gives

\[\det(zI_{16}-T)=z^{11}(z^5-z^4-z^3+z-1).\]

The directed graph of positive entries of \(T\) has a unique cyclic strongly connected component on the states \(0000,0001,0010,0100,0101,0110,1000,1001,1010,1011,1101\); all other states are transient. This component contains the self-loop \(0000\to0000\), so its nonnegative irreducible adjacency matrix is primitive. Perron–Frobenius therefore gives a *simple positive root strictly dominating the moduli of all other nonzero eigenvalues*. This dominant root is the stated \(\lambda\). The simple positive pole \(\rho=1/\lambda\) is not cancelled by \(N(t)=1+t^2-t^3+t^4\), which is positive for \(0<t<1\). Consequently \(C=-N(\rho)/(\rho D'(\rho))\), with \(D(t)=1-t-t^2+t^4-t^5\), gives the stated asymptotic.

## Verification

The attached `verify.py` uses only the Python standard library. It reconstructs the attack and admissibility semantics directly and checks the local forest criterion against every loop marking of every labelled forest on at most five vertices: \(340\) underlying forests and \(9987\) marked instances. Independently, it exhausts every marking of every path of order through \(14\) and compares the result to the transfer enumeration. It verifies the exact \(16\)-entry polynomial matrix identity over integers and the recurrence through order \(44\). The matrix identity plus the proof in Step 5, rather than finite enumeration alone, establishes the infinite series.

Run `python3 verify.py`. The program prints `VERIFY_OK forests=340 loop_markings=9987 path_orders=0..14 transfer_order=44 exact_PTB=zero`.

## Relationship to prior work

Zhang and Liu (2026), *When Stable and Preferred Semantics Agree: A Path-Based Approach*, establish general path-based sufficient conditions and local variants; their global agreement theorems principally assume absence of self-defeating arguments, whereas their self-attack handling concerns existence or preferred extensions extending a chosen admissible set. The present result instead gives an iff criterion for **all** preferred extensions in the symmetric, self-looped forest class, followed by a complete enumeration of successful markings on paths. Andrews and San Mauro (2026), *Complexity in infinite argumentation with structural constraints*, include the known reduction \(\operatorname{Pref}=\operatorname{Naive}\) for symmetric attack frameworks with possible self-attacks; that reduction is used here as the elementary Step 1, not claimed as new. Earlier surveys establish coincidence without self-attacks. OEIS A253412 concerns minimal dominating sets on paths and begins \(1,1,2,2,4\), not this \(1,1,3,3,6\) marking census. These are comparisons of the actual statements, not merely titles.

## Limitations

This theorem requires underlying *forests* and a symmetric distinct-vertex attack relation. The local iff need not hold in graphs with cycles: choosing a neighbour for each marked neighbour may fail to produce an independent witness set. The enumeration counts labelled path loop markings, not isomorphism classes, and makes no claim about all possible attack relations. The complete text of one closely related journal paper was not accessible through the inspected source interface; the available introduction, Lemma 20 and discussion support the cited reduction but do not by themselves settle all historical priority. No external or independent audit has been performed.

## References

1. Y. Zhang and K. Liu, *When Stable and Preferred Semantics Agree: A Path-Based Approach*, arXiv:2610.30176, first public version 2026-10-19. https://arxiv.org/abs/2610.30176
2. U. Andrews and L. San Mauro, *Complexity in infinite argumentation with structural constraints*, Journal of Logic and Computation 36(5), published 2026-07-16, DOI: 10.1093/logcom/exag036. https://doi.org/10.1093/logcom/exag036
3. *Abstract Argumentation Frameworks and Their Semantics*, survey chapter on symmetric argumentation (2018). https://www.martincaminada.net/publications/HOFA_semantics.pdf
4. OEIS A253412, *Number of n-bit legal binary words with maximal set of 1s*. https://oeis.org/A253412
