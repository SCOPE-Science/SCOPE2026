# Optimal two-step identification of ternary Kautz shift networks

## Finding

Let \(K(2,n)\) be the directed Kautz graph on the ternary words \(w=w_0\cdots w_{n-1}\in\{0,1,2\}^n\) whose successive symbols are unequal. There is an arc \(w\to w_1\cdots w_{n-1}a\) whenever \(a\ne w_{n-1}\). For each vertex \(v\), its *incoming two-step ball* consists of all vertices from which \(v\) can be reached in at most two directed steps. A code \(C\) is two-step identifying when all signatures \(B^-_2(v)\cap C\) are nonempty and pairwise distinct.

**Theorem.** For every integer \(n\ge3\), the exact minimum size of such a code is
\[
\gamma^-_2(K(2,n))=3\cdot 2^{n-2}=\tfrac12|V(K(2,n))|.
\]
An explicit optimum is obtained by treating the alphabet as \(\mathbb Z/3\mathbb Z\) and setting \(\epsilon_i(w)=+1\) if \(w_{i+1}-w_i\equiv1\pmod3\), or \(-1\) if it is congruent to \(-1\). Put \(j_n=0\) for odd \(n\) and \(j_n=1\) for even \(n\). Then
\[
C_n=\{w\in V(K(2,n)):\epsilon_{j_n}(w)=\epsilon_{n-2}(w)\}
\]
is an optimal code. Moreover, signatures can be decoded into their unique vertices using \(O(n)\) symbol operations. At lengths \(n=1,2\), two-step identification is impossible, because distinct vertices have equal full incoming two-step balls.

## Assumptions and scope

All graph paths are directed, and balls include the zero-step center. Words and sites are indexed from zero. No loops are allowed, because consecutive symbols must differ. The term *two-step* means radius at most two, not exactly two. Each sensor reports whether its vertex lies in the incoming ball of the unknown vertex, and the list of reporting sensors is the signature. The theorem is specific to the degree-two ternary Kautz family and is not a statement about the full ternary de Bruijn graph.

## Proof

**1. The sibling lower bound.** There are \(3\cdot2^{n-1}\) vertices and \(3\cdot2^{n-2}\) admissible length-\((n-1)\) prefixes. Each prefix \(p\) has two successors \(pa,pb\). For any such pair, their one-step predecessor sets are identical, as are their two-step predecessor sets: these depend only on the prefix of length \(n-1\) or \(n-2\). Consequently the symmetric difference of their radius-two incoming balls is contained in \(\{pa,pb\}\). Every identifying code must select at least one member of each *disjoint* sibling pair. Thus it contains at least \(3\cdot2^{n-2}\) vertices.

**2. The explicit half-sized code.** Given any length-\((n-1)\) prefix \(p\), its two possible final letters have opposite last-step orientations \(\epsilon_{n-2}\). Since \(j_n<n-2\), the earlier orientation is independent of the last letter. Exactly one extension lies in \(C_n\), proving its claimed size. An alternating (period-two) admissible word never lies in \(C_n\): its step orientations alternate, so \(\epsilon_0\ne\epsilon_{n-2}\) at odd length and \(\epsilon_1\ne\epsilon_{n-2}\) at even length.

**3. The predecessor decomposition.** For \(v=v_0\cdots v_{n-1}\), put \(t=v_0\cdots v_{n-3}\), of length \(n-2\). Its incoming ball is the union of the center \(\{v\}\) and
\[
P_1(v)=\{av_0\cdots v_{n-2}:a\ne v_0\},\qquad
P_2(v)=\{bat:a\ne v_0,\ b\ne a\}.
\]
The two predecessor layers are disjoint because an overlap would force two consecutive equal letters. The center can belong to \(P_2(v)\) only if \(v\) is period two, but then \(v\notin C_n\). Thus the selected sensor sets of these components are disjoint. We show how to recover \(v\) from the signature \(S(v)=B^-_2(v)\cap C_n\).

**4. Odd length: recover the prefix.** When \(n\) is odd, the membership test for \(bat\in C_n\) chooses exactly one \(b\) for each of the two admissible \(a\). Consequently \(P_2(v)\cap C_n\) contains exactly two words with the common suffix \(t\) of length \(n-2\). Similarly, \(P_1(v)\cap C_n\) contains exactly one word \(x=av_0\cdots v_{n-2}\). Neither this word nor an optional selected center can share the suffix \(t\), since that would force adjacent equal letters or a selected period-two center. Nor can the two share any other length-\((n-2)\) suffix. Hence \(t\) is exactly the unique suffix appearing twice among the sensors of \(S(v)\).

The unique sensor \(x\) whose positions \(1,\ldots,n-2\) spell \(t\) is the selected one-step predecessor. Indeed \(x_1\cdots x_{n-2}=t\). A selected two-step predecessor cannot satisfy this equality, because its second symbol \(a\ne t_0\), and the center cannot satisfy it since \(v_1\ne v_0\). Therefore the first \(n-1\) symbols of the unknown \(v\) are exactly \(x_1\cdots x_{n-1}\). This argument also covers the boundary \(n=3\): the last orientation of a two-step predecessor may depend on \(a\), but there remains exactly one valid \(b\) for each \(a\).

**5. Even length: recover the prefix.** When \(n\) is even, the membership test on \(bat\) fixes one of the two possible symbols \(a\) and accepts both possible \(b\). Hence \(P_2(v)\cap C_n\) is a two-word pair with a common length-\((n-1)\) suffix \(x=at\). The two one-step predecessors are either both selected or both unselected; if selected they form a second two-word pair with common suffix \(y=v_0\cdots v_{n-2}=tu\), where \(u=v_{n-2}\). A selected center forms no other suffix pair: equality of its suffix with a one-step suffix forces adjacent equality, and equality with the two-step suffix forces the excluded period-two pattern.

If two pairs occur, their suffixes are \(x=at\) and \(y=tu\), and satisfy \(x_1\cdots x_{n-2}=y_0\cdots y_{n-3}=t\). This ordering is **unique**. The reverse overlap would imply \(t\) alternates between two letters and \(a=t_1\). But then the step \(a\to t_0\) is opposite to the last step of \(t\), contradicting the condition that selected two-step predecessors have equal second-step and last-step orientations. Thus we identify \(y\), the desired prefix of length \(n-1\).

If just one pair occurs it must be the two-step pair; its common suffix \(x=at\) reveals \(t=x_1\cdots x_{n-2}\). Absence of the one-step pair means that \(\epsilon_{n-3}(v)\ne\epsilon_0(v)\): the orientation between \(t_{n-3}\) and the next letter \(u\) is opposite to the orientation between \(t_0\) and \(t_1\). Exactly one of the two admissible symbols \(u\) satisfies this, so again the prefix \(y=tu\) is recovered. The argument includes \(n=4\).

**6. Determine the last letter.** In either parity, once the prefix \(y=v_0\cdots v_{n-2}\) is known, there are exactly two possible target vertices \(ya,yb\), and exactly one, say \(z\), belongs to \(C_n\). The signature contains \(z\) if and only if the target itself is \(z\). Indeed a selected sibling cannot belong to the one-step predecessor set of the other (this would force adjacent equal letters). If it belonged to the other's two-step predecessor set, its symbols would repeat at distance two throughout, making it an alternating word, which is excluded from \(C_n\). Therefore membership of \(z\) in the signature chooses the correct sibling. The two-step predecessors always supply two sensors, so no signature is empty. This proves injectivity and optimality.

The reconstruction uses at most five reporting vertices, scans their length-\(n\) labels a constant number of times, and hence runs in \(O(n)\) symbol operations. For \(n=1\), the graph is the loopless complete digraph on three vertices and its radius-two balls coincide. For \(n=2\), every vertex reaches every other within two steps, so all incoming two-step balls coincide.

## Verification

The accompanying standalone Python 3 program `VERIFY.py` directly enumerates all admissible vertices and radius-two in-balls, constructs \(C_n\) from the local orientation condition, checks nonempty and pairwise different signatures, and separately replays the described decoder for every vertex for all \(3\le n\le11\). It also checks the optimal-size sibling constraints for \(3\le n\le7\), the exclusion of all alternating vertices, and the small-length nonexistence for \(n=2\). It terminates with `VERIFY_OK`. These finite checks supplement, but do not replace, the all-length proof above.

## Relationship to prior work

Boutin, Goliber and Pelto give sharp radius-\(t\) identification bounds and constructions for the **unrestricted directed de Bruijn graph**, in which adjacent symbols may coincide [1]. Their proof of the sibling lower bound is closely analogous, but their graph and code construction differ: simply restricting a de Bruijn identifying code to the proper-adjacency Kautz subgraph does not preserve identifying signatures in general. Their work does not state the present ternary Kautz optimum or orientation decoder. Araki studies tuple domination and connected tuple twin domination in de Bruijn and Kautz networks [2,3]; domination does not require all vertex signatures to differ. These results therefore neither assert nor imply the theorem above. The formula for radius-one identification of the same directed Kautz family likewise does not imply that its code remains identifying at radius two. Current literature searches did not find a prior statement covering the claimed two-step theorem; absence from indexed searches is not a proof of historical priority.

## Limitations

The explicit parity construction relies on the two possible extensions of a prefix over a three-letter no-repeat alphabet; it is not claimed for arbitrary outdegree, different ball orientation conventions without graph reversal, undirected Kautz graphs, or identification of multiple simultaneous faults. The proof gives an optimum and a decoder but not a classification of all optima. Historical priority is subject to unindexed or inaccessible earlier publications; independent review has not been performed.

## References

[1] D. Boutin, V. H. Goliber and M. Pelto, *Identifying Codes on Directed De Bruijn Graphs*, first arXiv posting 2014-12-18, arXiv:1412.5842, https://arxiv.org/abs/1412.5842 (full text examined, particularly the lower-bound argument and Theorem 3.6).

[2] T. Araki, *On the k-tuple domination of de Bruijn and Kautz digraphs*, Information Processing Letters 104 (2007), 86–90, DOI:10.1016/j.ipl.2007.05.010.

[3] T. Araki, *Connected k-tuple twin domination in de Bruijn and Kautz digraphs*, Discrete Mathematics 309 (2009), 6229–6234, DOI:10.1016/j.disc.2009.05.031.
