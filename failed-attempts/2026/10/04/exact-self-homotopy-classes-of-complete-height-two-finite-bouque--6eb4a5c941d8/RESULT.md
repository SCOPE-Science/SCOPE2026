# Exact self-homotopy classes of complete height-two finite bouquet models
## Finding
For every integer \(q\ge 2\), let \(P_q\) be the finite \(T_0\)-space with two minimal points \(a,b\), \(q\) maximal points \(c_1,\ldots,c_q\), and all relations \(a,b<c_i\). Then the unbased self-homotopy set has exactly \(1+2(q^q-q)\) classes. One class consists of all self-maps inducing zero on \(H_1(P_q;\mathbb Z)\) and has exactly \(2(q+1)^q+7q\) maps. Every other class is a singleton: these are exactly the maps that permute \(a,b\) and send the maximal level nonconstantly into itself, equivalently exactly the self-maps inducing a nonzero endomorphism of \(H_1(P_q;\mathbb Z)\). Thus every homologically nontrivial self-map is an isolated point of the finite function space \(P_q^{P_q}\). The total number of continuous self-maps is \(2(q+1)^q+2q^q+5q\).

The order complex of \(P_q\) is the complete bipartite graph \(K_{2,q}\), hence it is homotopy equivalent to a bouquet of \(q-1\) circles. The result describes the intrinsic finite-space homotopy classes of all direct self-maps, not merely the ordinary homotopy classes of maps of that graph.

## Assumptions and scope
A finite \(T_0\)-space is identified with its specialization poset. The order on the finite function space is pointwise: \(f\le g\) when \(f(x)\le g(x)\) for every \(x\). For finite spaces, a fence of comparable continuous maps gives a homotopy, and conversely homotopic maps lie in the same connected component of this function-space order. The statement is unbased.

The theorem concerns the complete height-two family \(P_q\). For \(q=3\) and \(q=4\) these are the five- and six-point complete-bipartite bouquet models previously used in direct homology-action censuses; for larger \(q\), \(P_q\) need not be a minimum-cardinality finite model of the corresponding bouquet.

## Proof
A continuous self-map is exactly an order-preserving function. Classify it by the images of the two minimal points.

If \(f(a)=f(b)=u\) is a minimal point, then the constant map \(c_u\) satisfies \(c_u\le f\). If \(f(a),f(b)\) are the two distinct minima and all maximal points have the same image \(M\), then \(f\le c_M\). If one of \(f(a),f(b)\) is a maximal point \(M\), order preservation forces every maximal point of the domain to map to \(M\), and again \(f\le c_M\). The only remaining possibility with both minimal-domain points maximal is the constant map \(c_M\). All constant maps are connected by fences such as \(c_a\le c_M\ge c_b\). Hence every map in these cases belongs to one homotopy class, the null class.

Now suppose \(f(a),f(b)\) are the two distinct minima and the restriction of \(f\) to the maximal level is nonconstant. Such an \(f\) is incomparable with every distinct continuous self-map. Indeed, if \(g\le f\), the minimal images force \(g(a)=f(a)\) and \(g(b)=f(b)\); each \(g(c_i)\) must lie above both minima, hence is maximal, and \(g(c_i)\le f(c_i)\) then gives equality. Conversely, if \(f\le g\) and, say, \(g(a)\) were maximal, monotonicity would force all \(g(c_i)\) to equal that maximum; since each \(f(c_i)\) is maximal and lies below \(g(c_i)\), all \(f(c_i)\) would be equal, contradicting nonconstancy. Thus \(g(a)=f(a)\), similarly \(g(b)=f(b)\), and then maximality forces \(g(c_i)=f(c_i)\). Therefore \(f\) is isolated in the function space and forms a singleton homotopy class.

It remains to identify these isolated maps homologically. The order complex is the graph \(K_{2,q}\), so \(H_1(P_q;\mathbb Z)\cong\mathbb Z^{q-1}\). Every non-isolated map is homotopic to a constant and therefore induces zero on first homology. For an isolated map, choose maximal points \(c_i,c_j\) with distinct images. The four-edge cycle
\[
a-c_i-b-c_j-a
\]
represents a nonzero class. Its image is again a four-edge cycle with two distinct minimal and two distinct maximal vertices, hence is a nonzero integral one-cycle. Because the order complex is one-dimensional, there are no nonzero two-boundaries, so the induced map on \(H_1\) is nonzero. This proves the equivalence between isolation and homological nontriviality.

Finally count maps. There are \(2(q+1)^q\) maps with both minima sent to the same minimum, \(2q^q\) with the minima sent bijectively to the two minima, \(4q\) maps with one minimal-domain point sent to a minimum and the other to a maximum, and \(q\) constant-to-a-maximum maps. Thus
\[
|\operatorname{End}(P_q)|=2(q+1)^q+2q^q+5q.
\]
Among the second family, exactly \(2(q^q-q)\) have a nonconstant maximal-level map and are isolated. Subtracting gives a null component of size \(2(q+1)^q+7q\), and therefore \(1+2(q^q-q)\) homotopy classes.

## Verification
The package includes `verify.py`, which independently enumerates every set map for \(q=2,3,4\), filters the order-preserving maps, constructs the comparability graph of the finite function space, and checks its connected components. It also computes the images of a standard integral cycle basis of \(K_{2,q}\) and confirms map-by-map that nonzero first-homology action is equivalent to the stated isolation criterion.

The replay output is:

- \(q=2\): \(36\) maps, \(4\) isolated nonzero-homology maps, null component \(32\), \(5\) homotopy classes.
- \(q=3\): \(197\) maps, \(48\) isolated nonzero-homology maps, null component \(149\), \(49\) homotopy classes.
- \(q=4\): \(1782\) maps, \(504\) isolated nonzero-homology maps, null component \(1278\), \(505\) homotopy classes.

The program terminates with `VERIFY_OK`.

## Relationship to prior work
Barmak and Minian characterize minimal finite models of bouquets and explicitly identify finite \(T_0\)-spaces with posets, with continuity equal to order preservation. Their theorem fixes the graph-model context but does not classify self-homotopy components of the complete \(K_{2,q}\) family. Stong's classical theory and Barmak's exposition give the finite-space homotopy machinery; in particular, pointwise-comparable maps are homotopic and homotopies can be represented by fences. Those general tools do not state the component formula above.

Barmak and Minian's later paper on simple homotopy types characterizes maps inducing simple homotopy equivalences between associated complexes. Its map classification has a different target: it does not enumerate ordinary self-homotopy classes of \(P_q\), nor does it identify the unique zero-\(H_1\) component and the isolated nonzero-\(H_1\) maps.

Previously computed direct \(H_1\)-action censuses for \(P_3\) and \(P_4\) overlap in objects and numerical self-map totals. They classify realized homology matrices; they do not determine homotopy components, do not prove that every nonzero-homology map is isolated, and do not give the all-\(q\) formulas. The present theorem therefore uses those cases only as overlap checks, not as premises.

Targeted searches using the aliases “complete height-two finite space”, “\(K_{2,q}\) finite model”, “self maps”, “mapping space”, “homotopy classes”, and “finite poset” found no source stating an implication-equivalent all-\(q\) classification. The closest sources concern minimal-model cardinality, general finite-space homotopy machinery, or simple homotopy equivalences rather than this mapping-space component structure.

## Limitations
The theorem is specific to the complete height-two family with exactly two minimal points. It does not classify mapping spaces of arbitrary minimal finite graph models, nor does it claim that the induced \(H_1\) endomorphism determines a singleton class uniquely: distinct isolated maps can induce the same homology endomorphism.

The literature comparison is targeted rather than logically exhaustive. The original Stong article was checked bibliographically and through later full-text restatements, but its publisher-hosted full text was not needed for the new counting argument. An obscure historical enumeration of this exact family could therefore remain a residual bibliographic risk.

## References
1. Jonathan Ariel Barmak and Elias Gabriel Minian, *Minimal Finite Models*, arXiv:math/0611156v1, first posted 2006-11-06; Journal of Homotopy and Related Structures 2 (2007), 127–140.
2. R. E. Stong, *Finite topological spaces*, Transactions of the American Mathematical Society 123 (1966), 325–340, DOI 10.1090/S0002-9947-1966-0195042-2.
3. Jonathan A. Barmak and Elias G. Minian, *Simple homotopy types and finite spaces*, Advances in Mathematics 218 (2008), 87–104, DOI 10.1016/j.aim.2007.11.019.
4. Jonathan A. Barmak, *Algebraic Topology of Finite Topological Spaces and Applications*, Lecture Notes in Mathematics 2032, Springer, 2011, DOI 10.1007/978-3-642-22003-6.
