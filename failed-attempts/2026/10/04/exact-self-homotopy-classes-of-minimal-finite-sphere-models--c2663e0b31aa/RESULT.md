# Exact self-homotopy classes of minimal finite sphere models

## Finding
For every integer \(n\ge 2\), let
\[
X_n=(S^0)^{\circledast(n+1)}
\]
be the unique \(2n+2\)-point minimal finite model of \(S^n\). Write its points in levels
\[
L_i=\{x_i^0,x_i^1\},\qquad 0\le i\le n,
\]
with every point of \(L_i\) below every point of \(L_j\) when \(i<j\), and with the two points inside each level incomparable.

Every continuous self-map \(f:X_n\to X_n\) is either a homeomorphism or is homotopic, in the ordinary finite-space sense, to a constant map. No two distinct homeomorphisms are homotopic. Consequently
\[
|[X_n,X_n]|=1+2^{n+1},
\]
because
\[
\operatorname{Aut}(X_n)\cong(C_2)^{n+1}
\]
is obtained by independently swapping the two points in each level.

Equivalently, with the compact-open topology, the finite function space \(C(X_n,X_n)\) has exactly one path component containing all nonhomeomorphisms and exactly \(2^{n+1}\) further components, each a singleton homeomorphism.

## Assumptions and scope
The topology on a finite \(T_0\)-space is identified with its specialization order, so continuity is equivalent to order preservation. The space \(X_n\) is the iterated non-Hausdorff suspension model described by Barmak and Minian. Their sphere-minimality theorem identifies it as the unique cardinality-minimal finite model of \(S^n\), and their account of Stong's theory states that a minimal finite space has no nonidentity self-map homotopic to its identity.

The conclusion is about ordinary homotopy of maps between finite spaces, not merely homotopy after passing to an order complex. This distinction is essential: weak equivalence to \(S^n\) does not identify the ordinary homotopy theory of the finite model with that of the sphere.

## Proof
A continuous self-map is an order-preserving map. First suppose \(f\) is surjective. Since \(X_n\) is finite, \(f\) is a permutation. A surjective order-preserving self-map of a finite poset is an order automorphism: some positive power of the permutation is the identity, so the inverse is itself a positive power and is order-preserving. The level of a point is determined order-theoretically by its height and coheight, hence every automorphism preserves each \(L_i\). It may independently exchange the two points of each level, giving
\[
\operatorname{Aut}(X_n)\cong(C_2)^{n+1}.
\]

Now suppose \(f\) is not surjective and let \(Y=f(X_n)\), with the induced order. We show that \(Y\) is contractible as a finite space. For a target level \(L_j\), let
\[
s_j=|Y\cap L_j|\in\{0,1,2\}.
\]
Assume for contradiction that every occupied target level is full, so every nonzero \(s_j\) equals \(2\).

Whenever both points of some target level \(L_j\) occur in the image, choose preimages of those two incomparable points. Comparable source points cannot map to incomparable target points, so the two preimages must themselves be incomparable. In \(X_n\), the only incomparable pairs are the two points of a common level. Thus some source level maps bijectively onto \(L_j\).

List the occupied target levels increasingly as \(j_0<\cdots<j_r\), and let \(i_k\) be a source level mapping bijectively onto \(L_{j_k}\). Order preservation forces
\[
i_0<i_1<\cdots<i_r.
\]
Moreover, \(i_0=0\). Otherwise a source point below level \(i_0\) would have to map below both incomparable points of \(L_{j_0}\), producing an occupied target level below \(j_0\). Similarly \(i_r=n\).

For consecutive occupied target levels \(j_k<j_{k+1}\), there can be no source level strictly between \(i_k\) and \(i_{k+1}\). Such a source level would have to map strictly above both points of \(L_{j_k}\) and strictly below both points of \(L_{j_{k+1}}\), producing an occupied target level strictly between \(j_k\) and \(j_{k+1}\). Therefore
\[
i_{k+1}=i_k+1.
\]
It follows that there are \(n+1\) occupied target levels. Since \(X_n\) itself has only \(n+1\) levels, every target level is occupied and, by assumption, full. Thus \(Y=X_n\), contradicting nonsurjectivity.

Hence a proper image \(Y\) has at least one occupied level containing a single point; call that point \(y\). Delete occupied levels below \(y\) from the nearest level downward. At each stage every point in the highest remaining level below \(y\) is an up beat point with witness \(y\). Then delete occupied levels above \(y\) from the nearest level upward; every point in the lowest remaining level above \(y\) is a down beat point with witness \(y\). This is a sequence of Stong beat-point strong deformation retracts from \(Y\) to \(\{y\}\). Thus \(Y\) is contractible.

The map \(f\) factors through its image,
\[
X_n\longrightarrow Y\hookrightarrow X_n.
\]
Because \(Y\) is contractible, \(f\) is homotopic to a constant map. All constant maps \(X_n\to X_n\) are mutually homotopic because \(X_n\) is connected.

Finally let \(h\) be a homeomorphism. If a self-map \(g\) were homotopic to \(h\), then \(h^{-1}g\) would be homotopic to the identity. The space \(X_n\) is minimal, and Stong's rigidity theorem for minimal finite spaces, as recalled by Barmak and Minian, says that the only self-map homotopic to the identity is the identity. Hence \(g=h\). Each homeomorphism therefore forms a singleton homotopy class.

Kukieła proves that homotopies \(X\to Y\) are exactly paths in the compact-open space \(C(X,Y)\), and for finite \(X\) with Alexandroff \(Y\) that function space is again Alexandroff with the pointwise specialization order. This translates the classification above directly into the asserted path-component decomposition.

## Verification
The proof for arbitrary \(n\) is symbolic. The packaged dependency-free script `artifacts/verify.py` independently exhausts the models for \(n=1,2,3\). It enumerates every order-preserving self-map, identifies the homeomorphisms, checks that every proper image contains a singleton occupied level and beat-reduces to one point, and checks directly that each homeomorphism is incomparable with every other map in the function poset.

The replay gives \(36\), \(446\), and \(6080\) self-maps for \(n=1,2,3\), respectively, and \(5\), \(9\), and \(17\) finite-space homotopy classes, agreeing with \(1+2^{n+1}\). The finite computations are checks of the symbolic argument, not evidence for the all-\(n\) quantifier by extrapolation.

## Relationship to prior work
Barmak and Minian prove that \(X_n\) is the unique \(2n+2\)-point minimal finite sphere model and recall Stong's rigidity of maps homotopic to the identity on a minimal finite space. They do not classify all self-homotopy classes of \(X_n\). Kukieła develops the compact-open function-space formalism for Alexandroff spaces and identifies homotopies with paths, but does not give this sphere-model component classification.

A prior result on the same models established only that every nonhomeomorphism induces a null-homotopic map after order-complex realization; that weaker statement does not imply that the finite-space map itself is null-homotopic. A separate prior exact result for complete height-two bouquet models includes the case \(n=1\), where the formula above gives five classes. The present statement is restricted to \(n\ge2\) and supplies the all-dimensional ordinary finite-space homotopy classification.

Targeted searches of the primary literature, general web indexes, and a mathematical-results database found no statement giving \([X_n,X_n]\) or the path components of \(C(X_n,X_n)\) in this form. A related 2002 paper of Hardie, Vermeulen, and Witbooi studies a continuous pairing associated with the four-point circle, but its accessible abstract does not state a self-homotopy classification; the full text was not available for inspection in this run.

## Limitations
The theorem is specific to the canonical minimal sphere models \(X_n\). It does not classify maps between different sphere dimensions, self-maps of nonminimal finite sphere models, or higher homotopy groups of the function spaces. The case \(n=1\) is intentionally excluded from the novelty claim because it is already contained in a broader exact classification of complete height-two bouquet models.

The closest foundational source by Stong is older than the arXiv-era sources and was not directly accessible in full text during this run; the rigidity fact used here was verified in Barmak and Minian's full-text restatement. No claim of exhaustive bibliographic novelty is made beyond the documented searches.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1, submitted 6 November 2006.
2. M. Kukieła, *On homotopy types of Alexandroff spaces*, arXiv:0901.2621, first submitted 17 January 2009; function-space results inspected in version 2.
3. K. A. Hardie, J. J. C. Vermeulen, and P. Witbooi, *A nontrivial pairing of finite \(T_0\) spaces*, Topology and its Applications 125 (2002), 533–542, DOI 10.1016/S0166-8641(01)00298-X. Only the accessible abstract was inspected here.
