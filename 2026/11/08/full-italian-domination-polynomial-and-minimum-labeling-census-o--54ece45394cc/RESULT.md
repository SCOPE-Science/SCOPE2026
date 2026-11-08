# Full Italian-domination polynomial and minimum-labeling census of sunlet graphs

## Finding

For every integer \(n\ge3\), let \(S_n=C_n\odot K_1\) be the sunlet graph formed from a labelled cycle \(c_0,c_1,\ldots,c_{n-1}\), with one private pendant vertex \(p_i\) at each \(c_i\). An Italian dominating function is a labelling \(f:V(S_n)\to\{0,1,2\}\) such that every zero-labelled vertex has neighbours of total label at least \(2\). Set \(D_n(z)=\sum_f z^{\sum_v f(v)}\), summing over all such functions.

**Full weight enumerator.** Index a \(9\times9\) matrix \(T(z)\) by ordered pairs \((a,b)\in\{0,1,2\}^2\). Its only potentially nonzero entry from \((a,b)\) to \((b,c)\) is
\[
T(z)_{(a,b),(b,c)}=\begin{cases}
z^2+z\,\mathbf1_{\{a+c\ge1\}},&b=0,\\
z^2+z^3,&b=1,\\
z^2+z^3+z^4,&b=2.
\end{cases}
\]
Then the full Italian-domination polynomial is
\[
\boxed{D_n(z)=\operatorname{tr}(T(z)^n).}
\]
Thus this fixed-size transfer determines every weight coefficient for every sunlet order.

**Exact minimum-function census.** The known scalar minimum \(\gamma_I(S_n)=n+\lceil n/3\rceil\) follows also from the structural analysis below; it is not asserted to be new. Put \(k=\lceil n/3\rceil\). The number \(M_n=[z^{n+k}]D_n(z)\) of minimum-weight Italian dominating functions on the labelled graph is
\[
\boxed{M_n=\begin{cases}
3\cdot2^k,&n\equiv0\pmod3,\\
n(k+2)2^{k-1},&n\equiv1\pmod3,\\
n2^k,&n\equiv2\pmod3.
\end{cases}}
\]
All minimum functions are classified as follows. In each column \((f(c_i),f(p_i))\), exactly \(\lfloor2n/3\rfloor\) columns have type \(A=(0,1)\); every other column has type \(B=(0,2)\), \(C=(1,1)\), or \(D=(2,0)\). Between consecutive non-\(A\) columns in cyclic order lie at most two \(A\) columns. Across any length-two gap both endpoint columns must have type \(C\) or \(D\), and across any length-one gap at least one endpoint has type \(C\) or \(D\). These conditions are necessary and sufficient. In particular, type \(B\) occurs in a minimum function only when \(n\equiv1\pmod3\): then exactly one \(B\) occurs, situated between the two gaps of length one. The count of minimum functions containing \(B\) is \(n2^{k-1}\); the other minimum functions use only \(A,C,D\).

## Assumptions and scope

The graph is finite, simple, undirected, with \(n\ge3\) distinct labelled cycle centres and one distinct private leaf at each centre. The labels \(0,1,2\) are distinguished, as are the graph vertices. Indices are cyclic modulo \(n\). The polynomial counts functions, not orbits under graph automorphisms; \(z\) is a formal indeterminate. No assumption of a probabilistic or independent auditing model is needed.

## Proof

**Transfer identity.** Write \(a=f(c_{i-1})\), \(b=f(c_i)\), \(c=f(c_{i+1})\), and \(\ell=f(p_i)\). If \(b=0\), then \(\ell=0\) cannot defend its leaf. The choices are \(\ell=2\), always feasible, and \(\ell=1\), feasible exactly when \(a+c\ge1\) so that the zero-labelled centre is sufficiently defended. Their column weights are \(2\) and \(1\). If \(b=1\), the pendant label is either \(1\) or \(2\), with weights \(2,3\); \(\ell=0\) is invalid because the leaf would see centre label \(1\). If \(b=2\), the pendant label may be \(0,1,2\), with weights \(2,3,4\). These are all possibilities, and their respective weight generating functions are exactly the three transfer entries. Each closed length-\(n\) walk in the pair-state digraph corresponds uniquely to a cyclic sequence of centre labels and a choice of pendant label at every position; the trace counts each labelled sequence once. This proves the full polynomial identity.

**Minimum weight and columns.** Every valid centre–leaf column has weight at least \(1\), and the unique valid weight-\(1\) column is \(A=(0,1)\). All other valid columns have weight at least \(2\). If three consecutive columns were \(A\), the middle centre would see labels \(1+0+0<2\) from its leaf and the neighbouring centres, contradicting validity. Therefore the number \(a\) of \(A\)-columns satisfies \(a\le\lfloor2n/3\rfloor\), and every function has weight at least \(2n-a\ge2n-\lfloor2n/3\rfloor=n+\lceil n/3\rceil\). A cyclic arrangement with \(\lfloor2n/3\rfloor\) occurrences of \(A\), separated by \(k=\lceil n/3\rceil\) columns of type \(C\), attains this bound. At equality there must be exactly that maximum number of \(A\) columns and every other column must have weight exactly \(2\). Exhausting weight-\(2\) valid columns gives precisely \(B,C,D\), proving the four-type restriction.

**Gaps and compatibility.** Let the \(k\) non-\(A\) columns be arranged cyclically, and let \(t_j\) be the number of intervening \(A\) columns between successive non-\(A\) columns. Since three consecutive \(A\) are forbidden, \(t_j\in\{0,1,2\}\). Every \(A\) has leaf label \(1\), so it requires at least one positive neighbouring centre. A gap of length \(2\) requires its two endpoint centres positive, and a gap of length \(1\) requires at least one endpoint positive. Types \(C,D\) have positive centre, while \(B\) has centre label zero. These conditions are exactly necessary and sufficient for all the \(A\)-centres; all other centres and leaves are already protected by their local type constraints. The number of gap deficits is
\[
\sum_{j=1}^{k}(2-t_j)=2k-(n-k)=3k-n=:\delta\in\{0,1,2\}.
\]

**Enumeration with positive non-\(A\) centres.** If every non-\(A\) column is \(C\) or \(D\), any allowed gap vector is feasible. In the cases \(\delta=0,1,2\), there are respectively \(1\), \(k\), and \(k+\binom{k}{2}=k(k+1)/2\) indexed gap vectors: all gaps length two; exactly one length-one gap; or one length-zero gap or two length-one gaps. A labelled cycle with \(k\) non-\(A\) positions can be counted by choosing a distinguished non-\(A\) position in \(n\) ways and specifying a gap vector, then dividing by \(k\) because each resulting labelled configuration has exactly \(k\) choices of distinguished non-\(A\) position. Independently assigning either \(C\) or \(D\) at each of the \(k\) non-\(A\) positions gives
\[
\begin{cases}
3\cdot2^k,&\delta=0,\\
n2^k,&\delta=1,\\
n(k+1)2^{k-1},&\delta=2.
\end{cases}
\]
This pointed counting remains valid when \(k=1\) (the smallest permitted graph \(n=3\)).

**The exceptional zero-centre type.** For a non-\(A\) type \(B\) to be feasible, both its incident gaps must have length at most one: a neighbouring gap of length two would contain an \(A\) centre whose only adjacent non-\(A\) centre is the zero-labelled \(B\). This consumes at least two units of deficit, forcing \(\delta=2\) and both incident gaps to have length one. Conversely such a \(B\) is allowed provided all other non-\(A\) columns are of type \(C\) or \(D\), so each adjacent \(A\) is defended from its other end. The two short gaps share only one non-\(A\) position if \(k\ge3\); if \(k=2\), they share both positions, but at most one can be \(B\), since otherwise the two intervening \(A\) centres are undefended. Thus every exceptional configuration has precisely one \(B\). Choose its labelled position (\(n\) choices); the gap vector with two length-one gaps incident to it and all other gaps length two is forced, and the remaining \(k-1\) non-\(A\) labels can independently be \(C\) or \(D\). This contributes exactly \(n2^{k-1}\) additional minimum functions for \(\delta=2\), and none for \(\delta=0,1\). Adding this term to the previous count proves the stated residue-class formula and the complete classification. \(\square\)

## Verification

The standalone `verify.py` implements the polynomial transfer using ordered label-pair states, compares complete polynomials to direct enumeration over all \(3^{2n}\) vertex labellings for \(3\le n\le6\), checks minimum weights and leading coefficients for \(3\le n\le16\), and independently enumerates only the four possible minimum-column types for \(3\le n\le9\), including the exceptional \(B\)-case multiplicities. A successful replay ends with `VERIFY_OK`. These are finite corroborations; the theorem for all \(n\ge3\) follows from the combinatorial proof, not from extrapolation.

## Relationship to prior work

Hernández-Ortiz, Montejano, and Rodríguez-Velázquez, *Italian domination in rooted product graphs* (arXiv:2006.02124v1, 2020), Corollary 3.1, already prove \(\gamma_I(G\odot K_1)=|V(G)|+\gamma(G)\), which yields the scalar minimum \(n+\lceil n/3\rceil\) here. That prior result is not claimed as new; its statement does not determine the weight polynomial, the number of minima, or the minimum-column patterns.

Shao and Zhao, *Counting Weight-\(k\) Italian Dominating Sets on Trees and Cycles* (arXiv:2610.00108v1; public date 2026-09-09), give coefficient-counting algorithms for paths, trees, and cycles and explicitly identify broader bounded-treewidth and cactus graph classes as a further direction. Their full text was examined, including the algorithms, tables and conclusion; no sunlet or pendant-cycle enumeration was identified. A sunlet is a unicyclic cactus but is neither a tree nor a plain cycle, and the pendant-leaf state interaction does not follow from their cycle formulas by substitution.

The terms Italian domination and Roman \(\{2\}\)-domination refer to the same rule. Published research-record and literature searches using both names, sunlet, corona, cycle with private leaves, polynomial, transfer matrix, and minimum-function census revealed no equivalent result. Absence of a match is not a proof of priority; unindexed sources or independently developed counting arguments may exist.

## Limitations

The classification concerns labelled sunlet graphs for \(n\ge3\). It is not a general corona polynomial formula, a theorem for all cactus graphs, or an enumeration modulo dihedral symmetries. The fixed-size transfer is exact but is not an explicit coefficient-by-coefficient closed form for arbitrary weights. Historical originality has not been independently validated. The computations check only the stated finite ranges and do not prove the unrestricted claim.

## References

1. Pingping Shao and Chengye Zhao, *Counting Weight-\(k\) Italian Dominating Sets on Trees and Cycles*, arXiv:2610.00108v1 (first public date shown as 2026-09-09), https://arxiv.org/abs/2610.00108.
2. R. Hernández-Ortiz, L. P. Montejano, and J. A. Rodríguez-Velázquez, *Italian domination in rooted product graphs*, arXiv:2006.02124v1 (2020), https://arxiv.org/abs/2006.02124.
3. M. Chellali, T. W. Haynes, S. T. Hedetniemi, and A. A. McRae, *Roman \(\{2\}\)-domination*, Discrete Applied Mathematics 204 (2016), 22–28.
