# Four variables recognize binary symplectic graphs among all finite graphs

## Finding
For any nonempty finite simple undirected graph \(G\), let \(E\) denote adjacency and \(P\oplus Q\) the exclusive-or of two truth values. The following sentence has only four variable names and quantifier rank four:
\[
\Phi:=\bigl(\forall x\exists y\,E(x,y)\bigr)\land
\forall x\forall y\Bigl[x\ne y\longrightarrow\exists z\forall w\bigl(E(z,w)\leftrightarrow(E(x,w)\oplus E(y,w))\bigr)\Bigr].
\]
**Theorem.** The finite simple graphs satisfying \(\Phi\) are exactly the binary symplectic nonorthogonality graphs \(\operatorname{Sp}(2m,2)\), \(m\ge1\): their vertices are all nonzero vectors in a \(2m\)-dimensional vector space over \(\mathbb F_2\) equipped with a nondegenerate alternating bilinear form \(B\), and two vertices are adjacent exactly when \(B(u,v)=1\). Moreover, four is the *least* variable width of any counting-free first-order sentence recognizing this class among all finite simple graphs. A 63-vertex switched nonmember has exactly the same unrestricted-depth three-variable theory as \(\operatorname{Sp}(6,2)\).

## Assumptions and scope
Graphs are finite, nonempty, loopless, undirected, and simple. The signature contains only equality and adjacency, without constants, counting quantifiers, or vector-space operations. The connective \(\oplus\) is just an abbreviation for \((P\land\neg Q)\lor(\neg P\land Q)\). A bilinear form is alternating when \(B(v,v)=0\) for all \(v\), and nondegenerate when the only vector \(v\) satisfying \(B(v,w)=0\) for all \(w\) is zero. Nondegenerate alternating spaces have even dimension. The smallest graph, \(\operatorname{Sp}(2,2)\), is a triangle.

## Proof
**Recognition, forward.** Let \(r_x\in\mathbb F_2^{V(G)}\) be the row with \(r_x(w)=1\) exactly when \(E(x,w)\). By the first conjunct all rows are nonzero; by the second, for any distinct vertices \(x,y\), the sum \(r_x+r_y\) is also a row. Distinct vertices must have distinct rows: otherwise the required sum would be a zero row. Thus \(S=\{r_x:x\in V(G)\}\) consists of distinct nonzero vectors, is closed under sums of unequal elements, and \(W=S\cup\{0\}\) is a vector subspace of \(\mathbb F_2^{V(G)}\). Indeed equal-element sums are zero, other sums lie in \(S\), and zero is an identity. Moreover \(S=W\setminus\{0\}\).

For nonzero \(a=r_x\), \(b=r_y\), define \(B(a,b)=r_x(y)\); define \(B\) to be zero when either argument is zero. This is well defined because row labels are unique. Evaluation of an adjacency-row sum at the vertex for \(b\) shows \(B(a+a',b)=B(a,b)+B(a',b)\). Graph symmetry yields symmetry of \(B\) and hence additivity in the second argument; graph looplessness yields \(B(a,a)=0\). Every nonzero row has some nonzero entry, so \(B(a,-)\) is nonzero whenever \(a\ne0\). Thus \(B\) is a nondegenerate alternating bilinear form. Its dimension is \(2m\) for some \(m\ge1\). The row map is an isomorphism from \(G\) onto the nonzero-vector graph of \((W,B)\), and a symplectic basis identifies this graph with \(\operatorname{Sp}(2m,2)\).

**Recognition, reverse.** In any nondegenerate alternating space, every nonzero \(x\) has some nonzero \(y\) with \(B(x,y)=1\). For distinct nonzero \(x,y\), the nonzero vector \(z=x+y\) satisfies \(B(z,w)=B(x,w)+B(y,w)\) for all nonzero \(w\). Both conjuncts of \(\Phi\) follow.

**Four-variable optimality.** Abiad and Haemers construct a four-vertex Godsil--McKay switch of \(X=\operatorname{Sp}(6,2)\) yielding a graph \(X'\) with the same strongly regular parameters \((v,k,\lambda,\mu)=(63,32,16,16)\) but adjacency-matrix rank eight over \(\mathbb F_2\), rather than rank six. As a graph with 63 vertices, a binary symplectic graph would have to be \(\operatorname{Sp}(6,2)\), so \(X'\) is not a model of \(\Phi\).

For two distinct adjacent vertices of either graph, the four counts of **other** vertices having adjacency patterns \((1,1),(1,0),(0,1),(0,0)\) to the pair equal \((16,15,15,15)\); for nonadjacent vertices they equal \((16,16,16,13)\). These follow directly from \((63,32,16,16)\), and every count is positive. Every vertex also has neighbors and distinct nonneighbors. In the ordinary three-pebble game, after any move at most two old vertices remain, and Duplicator can choose a fresh response realizing the requested adjacency pattern to those vertices (or copy an old equality). Thus the occupied vertices always form a partial isomorphism, at every round. Hence \(X\equiv_{\mathrm{FO}^{3}}X'\) without any quantifier-depth bound. One graph satisfies \(\Phi\) and the other does not, so no sentence using three or fewer variables defines the class.

## Verification
The standalone standard-library program `verify.py` constructs \(\operatorname{Sp}(2,2)\), \(\operatorname{Sp}(4,2)\), and \(\operatorname{Sp}(6,2)\); reconstructs the published four-vector switch; checks rank, strong regularity, adjacency-row closure and its failure, and all two-fixed-vertex extension patterns in the 63-vertex pair. It also evaluates the criterion on all \(1{,}099\) labelled simple graphs of orders one through five, where exactly the triangle satisfies it. Exact output is `verify_output.txt`; run `python3 verify.py` from the same folder. The computations corroborate the algebraic and game proofs, but do not replace them.

## Relationship to prior work
Abiad and Haemers, *Switched symplectic graphs and their 2-ranks* (arXiv:1412.2945, first version 2014-12-09), establish symplectic parameters and switched examples whose rows fail the binary sum property. The cited theorem of Peeters characterizes symplectic graphs by **specified strongly regular parameters together with minimum binary rank**. Here the row property becomes a *single parameter-free four-variable axiom among arbitrary finite graphs*, and a separate pebble argument proves its variable width sharp. Kubota, *Strongly regular graphs with the same parameters as the symplectic graph* (arXiv:1606.03442), compares switched families by counts of common neighbors of triples; no equivalent first-order recognition theorem was identified in the inspected sections. Grohe and Otto, *Pebble Games and Linear Equations* (arXiv:1204.1990), provide general background on ordinary pebble equivalence without counting.

## Limitations
The domain is nonempty finite simple graphs. Neither the minimum *quantifier rank* nor minimum formula length is claimed. The 63-vertex witness need not be the smallest possible counterexample to three-variable recognition. The result does not classify arbitrary strongly regular graphs or switching families. An uninspected broader binary graph representation or finite-model-theory result could cover the same characterization, so the historical-priority assessment remains qualified. Independent mathematical validation has not been performed.

## References
1. A. Abiad and W. H. Haemers, *Switched symplectic graphs and their 2-ranks*, arXiv:1412.2945, v1 2014-12-09. https://arxiv.org/html/1412.2945v2
2. S. Kubota, *Strongly regular graphs with the same parameters as the symplectic graph*, arXiv:1606.03442, v1 2016-06-10. https://arxiv.org/html/1606.03442v1
3. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990, v1 2012-04-09. https://arxiv.org/abs/1204.1990
4. M. J. P. Peeters, *Uniqueness of strongly regular graphs having minimal p-rank*, *Linear Algebra and its Applications* 226--228 (1995), 9--31 (as quoted in Reference 1).
