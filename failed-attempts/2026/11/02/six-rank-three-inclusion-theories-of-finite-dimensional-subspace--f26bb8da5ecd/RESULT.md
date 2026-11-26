# Six rank-three inclusion theories of finite-dimensional subspace lattices

## Finding
For every field \(F\), let \(\mathcal L(n,F)\) be the poset of **all** linear subspaces of \(F^n\), with equality and the binary inclusion relation \(\subseteq\) as its only nonlogical symbols. For all fields \(F,K\) and integers \(m,n\ge1\),
\[
\mathcal L(n,F)\equiv_3\mathcal L(m,K)
\quad\Longleftrightarrow\quad
\min(n,6)=\min(m,6).
\]
Here \(\equiv_3\) means agreement on every first-order sentence of quantifier rank at most three. In particular, the characteristic, cardinality, and even finiteness of the fields are invisible to all such sentences. Exactly six classes occur, indexed by dimensions \(1,2,3,4,5,\ge6\). Over the subfamily of finite fields, the sharp smallest size bound for a representative is \(2825\) subspaces, attained by \(\mathcal L(6,\mathbb F_2)\).

## Assumptions and scope
All dimensions are positive finite integers; fields may be arbitrary, finite or infinite. The language is **only** \(\subseteq\), with first-order equality, and has no named zero space, ambient space, rank predicates, lattice operations, membership relation, scalars, or counting quantifiers. Strict containment \(X<Y\) abbreviates \(X\subseteq Y\land X\ne Y\). The quantifier rank of nested quantification, not the number of variables, is bounded by three.

## Proof
**Pair parameters.** For any distinct or equal subspaces \(X,Y\), put
\[
p=\dim(X\cap Y),\quad u=\dim X-p,\quad v=\dim Y-p,\quad w=n-\dim(X+Y).
\]
These are nonnegative integers with \(p+u+v+w=n\). Conversely, every such quadruple is realized over every field by the decomposition \(F^n=C\oplus U\oplus V\oplus D\), with \(X=C\oplus U\) and \(Y=C\oplus V\). Fixing \(\dim X=a\) and \(\operatorname{codim}X=b\), the possible quadruples are exactly those with \(p+u=a\), \(v+w=b\).

**One further selection.** For any subspace \(Z\), write its relation to \(X\) as \(E\) if \(Z=X\), \(U\) if \(Z>X\), \(D\) if \(Z<X\), and \(I\) if \(Z\) is incomparable with \(X\). A third move is completely described by the ordered pair of its relations to \(X,Y\). The following is an exhaustive table of feasible signatures; every unlisted signature is impossible. All conditions in the table are necessary and sufficient.

| Relation of \(X,Y\) | Always feasible | Additional feasible signatures and exact conditions |
|---|---|---|
| \(X=Y\), so \(u=v=0\) | \((E,E)\) | \((U,U):w>0\); \((D,D):p>0\); \((I,I):p>0,w>0\) |
| \(X<Y\), so \(u=0,v>0\) | \((E,D),(U,E)\) | \((U,U),(U,I):w>0\); \((U,D):v\ge2\); \((D,D),(I,D):p>0\); \((I,I):p>0,w>0\) |
| \(X>Y\), so \(u>0,v=0\) | \((E,U),(D,E)\) | \((U,U),(I,U):w>0\); \((D,U):u\ge2\); \((D,D),(D,I):p>0\); \((I,I):p>0,w>0\) |
| \(X\parallel Y\), so \(u,v>0\) | \((E,I),(U,U),(D,D),(I,E),(I,I)\) | \((D,I):p+u\ge2\); \((I,D):p+v\ge2\); \((U,I):v\ge2\text{ or }w>0\); \((I,U):u\ge2\text{ or }w>0\) |

The entries follow from elementary subspace geometry. For example, when \(X\parallel Y\), the spaces \(X\cap Y\) and \(X+Y\) give \((D,D)\) and \((U,U)\). Given \(x\in X\setminus Y\), \(y\in Y\setminus X\), the line spanned by \(x+y\) is incomparable with both, giving \((I,I)\), even over \(\mathbb F_2\). A strict intermediate space between two nested spaces exists precisely when the dimension gap is at least two. For incomparable \(X,Y\), a proper subspace of \(X\) incomparable with \(Y\) exists exactly when \(\dim X=p+u\ge2\); a strict superspace of \(X\) incomparable with \(Y\) exists exactly when an independent direction outside \(X+Y\) is available or \(\dim(Y/(X\cap Y))\ge2\). These constructions and their duals establish every line of the table, including boundary dimensions and zero spaces.

**Pointed two-move profiles.** A subspace of dimension \(a\) and codimension \(b\) permits exactly the union of the table signatures as \(p+u=a\), \(v+w=b\) vary. The table uses only tests of an integer being zero, positive, or at least two, together with \(p+u\ge2\) and \(p+v\ge2\). For \(a\ge3\), all needed possibilities in \((p,u)\) are represented by \((0,a),(1,a-1),(a-1,1),(a,0)\), whose relevant tests equal those from \((0,3),(1,2),(2,1),(3,0)\); likewise for \(b\ge3\) and \((v,w)\). Therefore the complete two-move profile at a first-selected subspace depends only on
\[
(\min(a,3),\min(b,3)).
\]
It is *exactly* that invariant. Indeed, a pointed formula of remaining rank at most two can test \(\dim X\ge j\), for each \(j=1,2,3\): for \(j=1\), \(\exists Y\,(Y<X)\); for \(j=2\), \(\exists Y\exists Z\,(Z<Y<X)\); and for \(j=3\),
\[
\exists Y\,[Y<X\ \land\ (\exists Z\,Z<Y)\ \land\ (\exists Z\,Y<Z<X)].
\]
The final formula forces a chain of four distinct subspaces \(Z<Y<Z'<X\); it is satisfied exactly when \(\dim X\ge3\). The order-dual formulas test \(\operatorname{codim}X\ge j\). Thus these clipped ranks are both sufficient and necessary for the pointed rank-two type.

**Empty-tuple rank three.** By the ordinary three-round Ehrenfeucht--Fraïssé criterion, two lattices agree at rank three precisely when their available first-element pointed rank-two types coincide. In dimension \(n\), the available types are
\[
S_n=\{(\min(a,3),\min(n-a,3)):0\le a\le n\}.
\]
For dimensions \(1\) through \(5\), these six-coordinate-profile sets are distinct (respectively of cardinalities \(2,3,4,5,6\)); for every \(n\ge6\), \(S_n\) is the same seven-element set
\[
\{(0,3),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0)\}.
\]
Hence the equivalence criterion follows, for arbitrary fields.

**Sharp finite representative.** Every finite field has at least two elements. At fixed dimension the number of subspaces grows with field size, and at fixed field size grows strictly with dimension. Thus the least-size stable representative has dimension six over \(\mathbb F_2\), where the Gaussian binomial coefficients are \(1,63,651,1395,651,63,1\), summing to \(2825\).

## Verification
Execute `python3 verify_pair_extensions.py` to compare the symbolic table against direct subspace enumeration over \(\mathbb F_2\) in dimensions \(1\) through \(7\), and \(\mathbb F_3\) in dimensions \(1\) through \(5\); it also checks analytic profile saturation through dimension \(40\). Execute `python3 verify_full_types.py` for a separate all-formula-type recursion through rank three over binary dimensions \(1\) through \(5\) and ternary dimensions \(1\) through \(4\). Both run with Python's standard library only. Recorded outputs are in `pair_checks.txt` and `full_types_checks.txt`. These finite computations corroborate, but do not replace, the all-dimensions/all-fields proof above.

## Relationship to prior work
Gillibert's *Critical points between varieties generated by subspace lattices of vector spaces* (arXiv:0809.4323, first public version 2008-09-25) studies varieties and compact-congruence semilattices of the **same subspace lattices**, rather than bounded-rank first-order theories. He's *On the strictness of the quantifier structure hierarchy in first-order logic* (arXiv:1409.7488) develops general quantifier-resource and game methods, without this subspace-lattice classification. A related finite Boolean **inclusion-poset** rank-three cutoff at dimension six does not imply the result here: Boolean lattices are distributive, while subspace lattices have nontrivial modular intervals, extra points, and field-dependent projective geometry. The pair-extension table above supplies the non-Boolean argument required for field-size independence.

## Limitations
This is a theorem about **pure inclusion** at rank at most three; it makes no assertion at rank four, in signatures with scalar arithmetic, named rank functions, lattice operations, extra sorts, or counting logic. Computational checks only cover specified finite fields and dimensions; the general proof is combinatorial. Historical priority was checked against directly relevant inspected sources and semantic mathematical research records but is not exhaustively established. No independent mathematical audit was conducted.

## References
1. Pierre Gillibert, *Critical points between varieties generated by subspace lattices of vector spaces*, arXiv:0809.4323 (first submitted 2008-09-25). https://arxiv.org/abs/0809.4323
2. Yuguo He, *On the strictness of the quantifier structure hierarchy in first-order logic*, arXiv:1409.7488 (first submitted 2014-09-26). https://arxiv.org/abs/1409.7488
