# All-arity compatible retractions of dicyclic groups: an odd-prime label law and a diameter-three transition

## Finding
Let \(G_m=\operatorname{Dic}_m\) denote the dicyclic group of order \(4m\), with \(m\ge2\). Write \(m=2^e r_1\cdots r_k\) where the \(r_i\) are the *maximal powers of distinct odd primes* dividing \(m\). Thus \(r_i\ge3\), and \(k=0\) precisely for powers of two. We determine all group-homomorphism retractions, their image orders, and their full simultaneous-commutation pattern.

For \(S\subseteq[k]\), set \(d_S=2^e\prod_{i\in S}r_i\) and \(t_S=m/d_S\). There is exactly one integer \(c_S\pmod{2m}\) satisfying
\[
c_S\equiv1\pmod{2d_S},\qquad c_S\equiv0\pmod{t_S}.
\]
The retractions of \(G_m\) are precisely the trivial endomorphism \(0\), and the distinct maps
\[
\rho_{S,v}(a)=a^{c_S},\qquad\rho_{S,v}(b)=a^v b,\qquad v\in\mathbb Z/(2m),\quad v\equiv0\pmod{2d_S}.
\]
There are \(t_S\) choices of \(v\), and \(\lvert\operatorname{im}\rho_{S,v}\rvert=4d_S\). The exact image-size enumerator is
\[
F_m(z)=z+\sum_{S\subseteq[k]}t_Sz^{4d_S},\qquad \lvert\operatorname{Retr}(G_m)\rvert=1+\prod_{i=1}^k(1+r_i).
\]

For every \(t\ge0\), the number of ordered \(t\)-tuples of *pairwise commuting nontrivial* retractions, including identity as a permitted entry, is
\[
C_t=\prod_{i=1}^k\bigl(1+(2^t-1)r_i\bigr).
\]
If the trivial endomorphism is permitted, the count is \(\widehat C_t=\sum_{j=0}^t\binom{t}{j}C_j\). In particular the total number of ordered commuting pairs is \(1+2\prod_i(1+r_i)+\prod_i(1+3r_i)\).

Define the *reduced commuting-retraction graph* to have the retractions except the trivial map and identity as its vertices, with an edge between distinct commuting maps. For \(k=0\) it is empty; for \(k=1\) it has \(r_1\) isolated vertices; for \(k\ge2\) it is connected of diameter **exactly three**. For \(k\ge1\) its maximal cliques number \(\prod_i r_i\), each of size \(2^k-1\). A vertex with active prime-power set \(S\) has degree
\[
2^{k-|S|}\prod_{i\in S}(1+r_i)-2.
\]

## Assumptions and scope
The maps are ordinary unital group endomorphisms (a group homomorphism automatically sends the identity to the identity). Composition-idempotence means \(\rho^2=\rho\). The special symbol \(0\) denotes the trivial group homomorphism, *not* the identity map. The terms *rank* and *image order* refer to the order of the image subgroup, not matrix rank. All formulas are exact for each integer \(m\ge2\), including odd, even, and pure two-power cases. Tuple entries are ordered and repetitions are allowed. The graph excludes both universally commuting maps, and has no loops.

## Proof
**1. Reduction to the cyclic subgroup.** The defining relations are \(a^{2m}=1\), \(b^2=a^m\), \(bab^{-1}=a^{-1}\). Each element is uniquely \(a^u\) or \(a^u b\). Every element outside \(\langle a\rangle\) has order four. Let \(f\) be an idempotent group endomorphism and write \(A=f(a)\), \(B=f(b)\). If \(A=a^u b\) lies outside \(\langle a\rangle\), idempotence gives \(A=f(A)=A^uB\) and hence \(B=A^{1-u}\). But then \(A\) and \(B\) commute, whereas the group relation requires \(BAB^{-1}=A^{-1}\), contradicting order four. Thus \(A=a^c\).

If \(B\in\langle a\rangle\), then \(BAB^{-1}=A=A^{-1}\), so \(c\equiv0\) or \(m\pmod{2m}\). With \(c=0\), the idempotence relation \(f(B)=B\) forces \(B=1\), giving the trivial map. With \(c=m\), idempotence on \(a\) requires \(m^2\equiv m\pmod{2m}\), hence \(m\) odd. But \(B^2=A^m=a^m\) then has no solution in \(\langle a\rangle\), since squares have even exponent and \(m\) is odd. Consequently every nontrivial retraction satisfies \(A=a^c\), \(B=a^v b\).

**2. All nontrivial retractions.** The three defining relations hold for these generator images exactly when \(c\) is odd (the other two relations follow automatically). Composition-idempotence additionally requires \(c^2\equiv c\pmod{2m}\) and \(cv\equiv0\pmod{2m}\), because \(f^2(b)=f(a^v b)=a^{cv+v}b\). By the Chinese remainder theorem an idempotent exponent \(c\) equals zero or one modulo each prime-power factor of \(2m\). Since it is odd, its residue modulo \(2^{e+1}\) must be one. The remaining active factors are exactly a subset \(S\) of the odd prime powers, yielding the unique \(c_S\) above. The equation \(cv=0\) forces \(v\) to vanish on every active factor, including the two-primary factor, leaving one arbitrary residue modulo each inactive \(r_i\). Thus \(t_S\) choices. Since \(a^{c_S}\) has order \(2d_S\) and \(a^v b\) lies outside the cyclic subgroup and squares to \(a^m\), the image has order \(4d_S\). This proves both classification and image-size formula.

**3. Exact commutation law and tuples.** For any two nontrivial retractions with parameters \((c,v)\), \((d,w)\), their compositions agree on \(a\) automatically. On \(b\) the two images are \(a^{cw+v}b\) and \(a^{dv+w}b\). Therefore they commute if and only if
\[
(1-d)v\equiv(1-c)w\pmod{2m}.
\]
At an odd factor \(r_i\), a retraction is either *active* with local exponent one and parameter zero, or *inactive* with exponent zero and a freely chosen label \(x_i\in\mathbb Z/r_i\). The congruence is automatic unless both retractions are inactive at that factor; in that case it demands equality of their labels. For a compatible \(t\)-tuple, at any fixed factor either all \(t\) entries are active (one possibility), or the set of inactive positions is a nonempty subset of \([t]\) and shares a common label (\((2^t-1)r_i\) possibilities). Independence of the local Chinese-remainder coordinates gives \(C_t\). Inserting the universally commuting trivial map in an arbitrary subset of positions gives \(\widehat C_t\).

**4. Graph structure.** A proper nontrivial retraction is encoded by a nonempty set of inactive coordinates and one label on each inactive coordinate. A vertex with active set \(S\) is compatible with exactly \(2^{k-|S|}\prod_{i\in S}(1+r_i)\) retractions including itself and identity: at each inactive coordinate the neighbor chooses either active or the same label; at an active coordinate the neighbor is either active or chooses any of \(r_i\) labels. Subtracting identity and itself proves the degree formula.

For \(k\ge2\), choose any two distinct coordinates \(i,j\). From every vertex one can select a compatible vertex having *only coordinate \(i\) inactive*, and from every second vertex one can select a compatible vertex with *only coordinate \(j\) inactive*. The two selected vertices commute, furnishing a path of length at most three (repeated vertices can only shorten it). Two all-inactive vertices with different labels in every coordinate have no common proper nontrivial commuting neighbor, as a common neighbor would have to be active on every coordinate, hence the identity. Their distance is three. For \(k=1\), any two distinct nonidentity vertices differ in the only inactive label and cannot commute, so the graph is edgeless.

Finally, a pairwise commuting set fixes a unique common label at each coordinate that is inactive at any of its vertices. It is therefore contained in the clique consisting of all nonidentity active/inactive patterns with labels inherited from a complete label vector \(x=(x_1,\ldots,x_k)\). Each such complete clique contains exactly one vertex for each proper active subset and so has size \(2^k-1\). It cannot be enlarged, since it includes the all-inactive vertex and every singly-inactive pattern; two distinct full vectors yield different cliques. These are all maximal cliques, proving their total \(\prod_i r_i\).

## Verification
The standalone `verify.py` uses the group normal forms \(a^u b^v\) and exact modular multiplication; for each tested \(m\), it independently enumerates all pairs of potential generator images, tests all presentation relators, then retains idempotent homomorphisms by direct composition. It compares the resulting full maps with the stated parameters, image orders, degrees, pairwise compatibility and (in selected cases) ordered commuting triples and graph diameters. All checks passed for \(m\in\{2,3,4,5,6,7,8,9,10,12,14,15,18,20,21,30}\). In particular, \(m=15\) has exactly \(25\) retractions and \(209\) ordered commuting pairs (including the trivial map). These computations are finite tests, not proofs for arbitrary \(m\); the preceding CRT and composition arguments establish the infinite assertion.

## Relationship to prior work
Madhusudanan, Sudhakara, and Seth (2023) classify descending endomorphisms of dicyclic groups (their Theorem 6.1), including forms \(a\mapsto a^i\), \(b\mapsto a^j b\), and study a *different* directed graph whose vertices are **group elements** and whose edges come from images under descending endomorphisms. Their earlier work develops descending endomorphisms of groups generally. The present classification of individual retractions is readily compatible with, and derivable in part by applying composition-idempotence to, their generator-image forms. The distinctive result here is the local commutation criterion for **operators**, all-arity product enumeration, and exact diameter and maximal cliques of the reduced operator-commutation graph. Results on commuting retractions of elementary generalized dihedral groups concern a different split group family and do not imply this odd-prime label law for dicyclic groups. Related dicyclic quotient-poset classifications concern quotients rather than commuting idempotent endomorphisms.

## Limitations
No claim is made about all endomorphisms or the full commuting graph of arbitrary endomorphisms. This theorem is elementary group theory once the correct operator-composition model is recognized; the existing classification of descending endomorphisms provides substantial prior structure. Literature coverage cannot establish absolute publication priority, and an earlier book chapter on descending endomorphisms of particular group families was not fully available for checking independently. Computations cover only explicitly listed finite values of \(m\). No independent mathematical audit has been performed.

## References
1. Vinay Madhusudanan, G. Sudhakara and Arjit Seth, “Descending endomorphism graphs of groups,” *AKCE International Journal of Graphs and Combinatorics* **20** (2023), 148–155, published online 15 August 2023, DOI: https://doi.org/10.1080/09728600.2023.2234956. Full source, especially Sections 2 and 6.
2. Vinay Madhusudanan, Arjit Seth and G. Sudhakara, “Descending Endomorphisms of Groups,” *Palestine Journal of Mathematics* **12** (2023), 318–325, https://pjm.ppu.edu/sites/default/files/papers/PJM_Feb_2023_318_to_325.pdf.
3. “Commuting retractions of elementary generalized dihedral groups,” https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-commuting-retractions-of-elementary-generalized-dihedral-groups--0ef9efc1c172.
4. “Two divisor branches and a sharp meet defect in dicyclic quotient-isomorphism posets,” https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-two-divisor-branches-and-a-sharp-meet-defect-in-dicyclic-quotien--717cdc2d9788.
