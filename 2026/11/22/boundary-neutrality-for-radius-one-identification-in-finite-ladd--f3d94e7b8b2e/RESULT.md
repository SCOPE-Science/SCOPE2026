# Boundary neutrality for radius-one identification in finite ladder networks

## Finding

For each integer \(n\ge2\), let \(L_n=P_n\square K_2\) be the open two-row ladder with vertex set \(\{(i,r):0\le i<n,\ r\in\{0,1\}\}\), edges joining vertices in the same rung and corresponding vertices in successive rungs. A radius-one *identifying code* is a set \(C\subseteq V(L_n)\) such that all \(2n\) sets \(N[v]\cap C\) are nonempty and pairwise distinct. Let \(I_n\) be its minimum cardinality.

**Theorem.** For every integer \(n\ge2\),
\[
 I_n=\left\lceil\frac{6n}{7}\right\rceil+\mathbf1_{\{n\bmod7\in\{1,2\}\}}.
\]
In particular, \(I_{n+7}=I_n+6\) for \(n\ge6\), the full initial sequence at widths \(2\) through \(12\) is \((3,3,4,5,6,6,8,9,9,10,11)\), and \(\lim_{n\to\infty} I_n/(2n)=3/7\). Comparing with Bouznif–Darlay–Moncel–Preissmann's already published formula for the **circular** square-grid strip \(C_n\square K_2\), we further obtain the boundary-neutrality identity
\[
 \gamma_{\mathrm{ID}}(P_n\square K_2)=\gamma_{\mathrm{ID}}(C_n\square K_2)\quad\text{for every }n\ge5.
\]
This equality is an equality **of optimal cardinalities**, not a claim that an optimal code for one graph remains identifying in the other graph.

## Assumptions and scope

The graphs are finite, simple, undirected, with closed rather than open neighbourhoods, and code membership can be at either or both vertices of any rung. All vertices, including code vertices, must be separated. The two endpoint rungs of \(P_n\square K_2\) have no wrap-around edges. The case \(n=1\) has two closed twins and no identifying code; hence it is excluded. The second equality uses the circular-strip convention in which \(C_n\) is the cycle on at least five vertices, as in the cited primary literature.

## Proof

**Locality.** Write a sensor selection by \(n\) masks \(a_i\in\{0,1,2,3\}\), with bit \(r\) of \(a_i\) selected precisely when \((i,r)\in C\). Each closed-neighbourhood signature at column \(i\) depends on only masks \(a_{i-1},a_i,a_{i+1}\). If two vertices lie at column distance at least three, their full closed neighbourhoods—and hence their signatures—are disjoint; provided their signatures are nonempty, they are automatically distinct. Therefore one needs only nonemptiness and the distinctness of signatures for pairs at column separation zero, one or two.

For a centre column \(i\), let \(G_i(a_{i-1},a_i,a_{i+1},a_{i+2},a_{i+3})\) be the Boolean predicate saying that both vertices in column \(i\) have nonempty signatures and each is separated from every distinct vertex at columns \(i,i+1,i+2\) within the graph. Here masks at nonexistent columns are declared zero, and comparisons to nonexistent vertices are omitted. Five masks suffice because the signature of a vertex in column \(i+2\) can use column \(i+3\). Every identifying code is precisely a mask word satisfying all the \(G_i\).

**Exact fixed-state reduction.** Order the \(4^4=256\) states \(s=(a,b,c,d)\in\{0,1,2,3\}^4\) lexicographically. For \(n\ge4\), define \(v_n(s)\) as the minimum selected-vertex cost of a length-\(n\) mask word ending in the four masks \(s\), subject to all predicates \(G_0,\ldots,G_{n-4}\); set it to \(+\infty\) if no such word exists. The initialization is
\[
 v_4(a,b,c,d)=\begin{cases}
 \mathrm{wt}(a)+\mathrm{wt}(b)+\mathrm{wt}(c)+\mathrm{wt}(d),&G_0(0,a,b,c,d),\\
 +\infty,&\text{otherwise},
 \end{cases}
\]
where \(\mathrm{wt}\) is the number of set bits of a two-bit mask. On appending mask \(e\), the exact recurrence is
\[
 v_{n+1}(b,c,d,e)=\min_{a:\,G_1(a,b,c,d,e)}\bigl(v_n(a,b,c,d)+\mathrm{wt}(e)\bigr).
\]
For interior columns \(G_1\) is translation invariant, so this recurrence uses one fixed min-plus matrix. At the right boundary, a fixed Boolean predicate \(T(s)\) tests the three remaining columns by adjoining three all-zero ghost masks; then \(I_n=\min_{s:T(s)}v_n(s)\). This terminal test is independent of \(n\) because the final four mask states are identified with the same relative columns.

**Finite all-length certificate.** Exact enumeration of all \(256\) states and their \(737\) permissible transitions yields the following *componentwise* formulas for all \(s=(a,b,c,d)\in\{0,1,2,3\}^4\):
\[
 v_6(a,b,c,d)=3+\mathbf1_{\{a=3\}}+\mathrm{wt}(b)+\mathrm{wt}(c)+\mathrm{wt}(d),
\]
\[
 v_{13}(a,b,c,d)=9+\mathbf1_{\{a=3\}}+\mathrm{wt}(b)+\mathrm{wt}(c)+\mathrm{wt}(d).
\]
All \(256\) entries in both vectors are finite. These explicit identities are checked by the standalone exact-integer program `verify_transfer.py`, beginning from the stated initialization and recurrence, and their full integer arrays are supplied in `certificate.json`. Because the recurrence is min-plus linear and commutes with adding a constant to all finite entries, this single finite equality \(v_{13}=v_6+6\) proves by induction that \(v_{n+7}=v_n+6\) for **every** \(n\ge6\). Applying the fixed terminal predicate proves \(I_{n+7}=I_n+6\) for all \(n\ge6\).

The terminal minima calculated exactly at \(n=6,7,8,9,10,11,12\) are \((6,6,8,9,9,10,11)\). The smaller values \((I_2,I_3,I_4,I_5)=(3,3,4,5)\) follow from direct enumeration or the same locality recurrence for widths at least four. These base values and the seven-step shift yield the theorem's ceiling-and-indicator formula for every \(n\ge2\).

**Comparison to closed strips.** Proposition 2 of Bouznif–Darlay–Moncel–Preissmann, in the height-two circular square-grid case, gives exactly the same ceiling-and-indicator expression for \(n\ge5\). Equality of the two separately established formulas proves the boundary-neutrality identity. The circular formula and the infinite-strip density \(3/7\) are *prior results*, not newly asserted discoveries.

## Verification

Execute `python3 verify_transfer.py`, `python3 verify_direct.py`, and `python3 construct_witnesses.py` using Python 3.8 or newer. The first independently recomputes the 256-state integer min-plus certificate and full seven-step identity; it compares the complete arrays against `certificate.json`. The second directly tests *all* sensor subsets of each labeled ladder from \(n=2\) through \(n=9\), without using the state recursion. The third constructs and directly checks optimal identifying-code witnesses at widths \(2\) through \(13\). They return `VERIFY_OK`, `DIRECT_OK` and `WITNESSES_OK` respectively. A computer is used only for an explicitly finite set of exact integer comparisons, and the mathematical induction above extends the verified identity to all lengths. No numerical optimization tolerances or unproved search completion assumptions are required.

## Relationship to prior work

Daniel, Gravier and Moncel (2004) proved the optimal **infinite** two-row square-strip identifying density \(3/7\) and proposed a general grid-identification algorithm; this establishes the asymptotic value but does not state the exact non-circular finite formula or boundary-neutrality identity. Rall and Wash (original public preprint of 12 February 2016) supplied general prism and finite-grid bounds rather than exact formulas. Bouznif, Darlay, Moncel and Preissmann (2019, preprint available from 2017) proved the **circular** height-two formula and established a broad exact dynamic-programming method applicable to noncircular strips; this is the closest comparison, and its transfer-method framework is credited. In their Section 5, the explicit small-height formulas are for circular strips, while Section 3.3 provides a general *algorithm* for noncircular cases but no height-two open-ladder formula or equality theorem. The present exact 256-state vector identity evaluates this specific open-boundary problem and proves the all-length equality with the circular optimum. A general algorithm with a broader domain does not by itself imply this explicit equality without an evaluation/certificate. Earlier unpublished calculations or different presentations of these exact open-ladder values remain possible.

The term 'circular ladder' must not be confused with the Cartesian *open* ladder: closing the rails changes the graph and, in general, the sets of identifying codes. The already published minimum-density and circular-optimum statements are not counted as new.

## Limitations

The theorem concerns only open two-row ladders with radius-one closed-neighbourhood identification. It does not classify all optimal sets, establish equivalence of optimal codebooks between open and closed ladders, or extend to wider strips, larger radius, or total-identification variants. The originality assessment is based on the specifically inspected published results and search coverage; an earlier unindexed finite-strip calculation would override the priority claim. The finite exact computation has a standalone checker but no independent mathematical audit.

## References

1. M. Daniel, S. Gravier and J. Moncel, 'Identifying codes in some subgraphs of the square lattice,' *Theoretical Computer Science* 319 (2004), 411–421, DOI: 10.1016/j.tcs.2004.02.007. https://doi.org/10.1016/j.tcs.2004.02.007
2. D. F. Rall and K. Wash, 'On minimum identifying codes in some Cartesian product graphs,' arXiv:1602.04089v1 (12 February 2016), https://arxiv.org/abs/1602.04089.
3. M. Bouznif, J. Darlay, J. Moncel and M. Preissmann, 'Exact values for three domination-like problems in circular and infinite grid graphs of small height,' *Discrete Mathematics & Theoretical Computer Science* 21(3), article 12 (2019), DOI: 10.23638/DMTCS-21-3-12; original preprint arXiv:1708.00758 (2017). https://dmtcs.episciences.org/en/articles/5458
4. M. Karpovsky, K. Chakrabarty and L. Levitin, 'On a new class of codes for identifying vertices in graphs,' *IEEE Transactions on Information Theory* 44(2) (1998), 599–611.
