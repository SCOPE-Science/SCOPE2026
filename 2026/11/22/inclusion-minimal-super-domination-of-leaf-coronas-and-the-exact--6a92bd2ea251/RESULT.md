# Inclusion-minimal super domination of leaf coronas and the exact sunlet spectrum

## Finding
Let \(H\) be any finite simple graph with vertex set \(V\) of cardinality \(n\geq1\). Form the *one-leaf corona* \(H\circ K_1\) by adding a private pendant vertex \(v'\) at each \(v\in V\). A subset \(S\) of its vertices is *super dominating* if every \(x\notin S\) has a witness \(y\in S\) whose only neighbour outside \(S\) is \(x\). A super dominating set is *inclusion-minimal* if deleting any selected vertex destroys this property.

There is an exact classification of **all** inclusion-minimal super dominating sets. Put \(O=V(H\circ K_1)\setminus S\), and partition the base into
\[
 A=\{v\in V:v\in O\},\qquad
 B=\{v\in V:v'\in O\},\qquad
 E=V\setminus(A\cup B).
\]
Then \(S\) is inclusion-minimal super dominating if and only if \(A,B,E\) form a partition of \(V\) satisfying both conditions:

1. No edge of \(H\) joins \(A\) to \(B\).
2. Each \(v\in E\) has at least one neighbour in \(A\) and at least one neighbour in \(B\).

Conversely every such partition uniquely specifies \(O= A\cup\{v':v\in B\}\) and thus one inclusion-minimal super dominating set. In particular, \(|S|=n+|E|\).

For the labelled sunlet \(L_n=C_n\circ K_1\) with \(n\geq3\), the **complete** cardinality enumerator of inclusion-minimal super dominating sets is
\[
 \boxed{F_n(z)=2z^n+\sum_{j=1}^{\lfloor n/4\rfloor}\frac nj\binom{n-2j-1}{2j-1}z^{n+2j}.}
\]
Thus their possible cardinalities are *exactly* \(n,n+2,\ldots,n+2\lfloor n/4\rfloor\), their upper super domination number is
\[
 \boxed{\Gamma_{\mathrm{sp}}(L_n)=n+2\lfloor n/4\rfloor,}
\]
and, with \(q=\lfloor n/4\rfloor\), the number of maximum-cardinality inclusion-minimal sets is \(2\) at \(n=3\), and for \(n\geq4\) is
\[
 \boxed{\frac nq\binom{n-2q-1}{2q-1}.}
\]
The latter is \(4\), \(2n\), \(2(2q+1)^2\), or \(2n(q+1)(2q+1)/3\), respectively, when \(n=4q,4q+1,4q+2,4q+3\), for \(q\geq1\). The term \(2z^n\) recovers the known two minimum-cardinality solutions for a connected one-leaf corona; the new assertions concern inclusion-minimal configurations of all sizes and the upper spectrum.

## Assumptions and scope
Graphs are finite, simple, labelled, undirected, and loopless. The base \(H\) may be disconnected and may have isolated vertices. Each vertex receives exactly one distinct private leaf, not a clique or a neighbourhood-corona attachment. All counting is of labelled **vertex sets**, not witness assignments or isomorphism classes. The cycle \(C_n\) is simple, and its statement starts at \(n=3\). For \(n=3\) the sum is empty by convention. Terms such as \(\Gamma_{\mathrm{sp}}\) refer to **maximum sizes of inclusion-minimal** super dominating sets, not the minimum super domination number.

## Proof
**1. Super domination and permitted omissions.** Write \(O\) for omitted vertices. The condition is equivalent to: for each \(x\in O\) there is \(y\notin O\) with \(N(y)\cap O=\{x\}\). If both \(v\) and \(v'\) were omitted, the omitted leaf \(v'\) would have no selected neighbour. Thus at most one of them is omitted; the triple \((A,B,E)\) is a partition. If \(v\in A\), its selected leaf \(v'\) witnesses it, regardless of other base omissions. If \(v\in B\), its omitted leaf \(v'\) has only one possible witness, the selected core \(v\); this witness works exactly when \(N_H(v)\cap A=\varnothing\). Therefore \(O\) is the complement of a super dominating set if and only if there are no edges between \(A\) and \(B\).

**2. Inclusion-minimality.** The family of omitted sets satisfying super domination is downward-closed: after removing any omitted vertex, all witnesses for the other omitted vertices remain available, and their omitted-neighbour sets only shrink. Consequently \(S\) is inclusion-minimal exactly when \(O\) is maximal under single-vertex additions. If \(v\in E\), omitting its *core* \(v\) is possible exactly when \(v\) has no neighbour in \(B\): the new omitted core is witnessed by \(v'\), while a neighbour in \(B\) would lose its sole witness. Similarly, omitting its *leaf* \(v'\) is possible exactly when \(v\) has no neighbour in \(A\): the core would otherwise fail to witness that leaf. There are no other possible additions because any occupied private pair already contains one omission. Thus no addition is possible if and only if each \(v\in E\) has neighbours of both types. This proves the general bijection and \(|S|=2n-|O|=n+|E|\).

**3. Cyclic words.** For \(H=C_n\), read the partition as a cyclic word over the three symbols \(A,B,E\). The no-cross-edge condition forbids adjacent \(A,B\). Each \(E\) must have one neighbour of each type, so each occurrence lies in \(AEB\) or \(BEA\); in particular, two \(E\)'s never touch. If there is no \(E\), connectedness forces the two constant words, accounting for \(2z^n\). Otherwise the cyclic word has an even number \(2j\) of \(E\)-symbols, with positive alternating runs of \(A\)'s and \(B\)'s between successive \(E\)'s. Necessarily \(4j\leq n\), since every separator requires a positive run after it. Conversely any such alternating cyclic run word meets both conditions, and every \(j\) with \(1\le j\le\lfloor n/4\rfloor\) occurs.

**4. Exact enumeration.** Fix \(j\geq1\). Mark one of the \(2j\) separators \(E\). There are \(n\) choices of its labelled position, two choices for the type of the first positive run, and
\[
 \binom{(n-2j)-1}{(2j)-1}=\binom{n-2j-1}{2j-1}
\]
ordered positive compositions of the remaining \(n-2j\) positions into \(2j\) run lengths. Every unmarked word is counted exactly \(2j\) times, independently of any rotational symmetry. Hence the coefficient is \(\frac nj\binom{n-2j-1}{2j-1}\), and its selected-set size is \(n+2j\). The full enumerator, support, maximum size, and maximum-set multiplicities follow. Substitution \(n=4q+r\) gives the stated four residue cases. No limiting argument or unproved computational classification is used.

## Verification
Execute `python3 verify_corona_minimal.py` using Python 3 and the standard library. The script evaluates the original graph-neighbourhood definition independently of the three-state classification, compares all vertex subsets of every one-leaf corona whose base graph has one through four vertices, and checks further seeded five- and six-vertex base graphs. For sunlets of sizes \(3\) through \(8\), it checks all \(2^{2n}\) vertex subsets; for sizes \(9\) through \(13\), it directly checks all \(3^n\) profiles compatible with the proved at-most-one omission per private pair. The script separately checks integer coefficients, the complete size spectrum, and the extremal formula over \(3\leq n<150\). Its output is saved as `verification_output.txt`.

These finite checks corroborate the theorem, but the classification and formula for unbounded \(n\) follow from the argument above; the script is not an exhaustive proof for all graphs or orders.

## Relationship to prior work
The October 2026 published result *Super-domination polynomial of arbitrary heterogeneous pendant coronas* gives a complete all-super-dominating-set polynomial for this graph operation, but does not determine which sets are inclusion-minimal or the sunlet upper spectrum. The present refinement requires the extra two-neighbour maximality condition and an alternating-run census. Avella-Alaminos, Lemańska and Zuazua (arXiv:2611.23464, first submitted 17 November 2026) introduce the upper super domination parameter, study paths and cycles, and give a bound for cycles, but not one-leaf coronas or the above complete upper-size enumerator. Klein, Rodríguez-Velázquez and Yi (arXiv:1705.00928, Theorem 18) obtain scalar *minimum* super domination numbers for coronas. Ghanbari, Jäger and Lehtilä (arXiv:2209.01795, Section 6) enumerate *minimum* super dominating sets for several base graph families and treat the neighbourhood corona separately. Earlier published records on one-leaf coronas characterize their minimum sets (two when the base is connected) and enumerate **all** super dominating sets by cardinality; neither statement by itself determines inclusion-minimality, whose full profile here is characterized by the two-neighbour test. The present theorem agrees with the known minimum count at size \(n\) and provides the full inclusion-minimal and maximum-size spectrum. The comparison does not claim that every historical source has been exhaustively indexed.

## Limitations
The precise sunlet polynomial is specialized to one pendant leaf per vertex and a simple cyclic base. The general three-state classification covers arbitrary base graphs but is not itself a polynomial-time optimizer for arbitrary \(H\); determining the best three-state partition may be difficult. The new enumerator is not the polynomial counting *all* super dominating sets. All originality assessments are relative to inspected and retrieved literature; an unindexed equivalent formulation remains possible. Independent mathematical validation has not been performed.

## References
1. *Super-domination polynomial of arbitrary heterogeneous pendant coronas*, published research result, 12 October 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/12/SCOPE-super-domination-polynomial-of-arbitrary-heterogeneous-pendant-c--08492630563f/RESULT.md.
2. D. Avella-Alaminos, M. Lemańska and R. Zuazua, *Minimal super dominating sets of maximum cardinality*, arXiv:2611.23464v1, first publicly posted 17 November 2026, https://arxiv.org/abs/2611.23464, full text https://arxiv.org/html/2611.23464.
3. D. J. Klein, J. A. Rodríguez-Velázquez and E. Yi, *On the super domination number of graphs*, arXiv:1705.00928v2, https://arxiv.org/html/1705.00928v2, Theorem 18.
4. N. Ghanbari, G. Jäger and T. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, arXiv:2209.01795v3, https://arxiv.org/html/2209.01795v3, Sections 3 and 6.
