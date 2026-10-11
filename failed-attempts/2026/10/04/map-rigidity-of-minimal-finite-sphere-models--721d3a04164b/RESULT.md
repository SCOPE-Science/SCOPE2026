# Map rigidity of minimal finite sphere models
## Finding
For \(X_n=(S^0)^{\circledast(n+1)}\), the unique \(2n+2\)-point minimal finite model of \(S^n\) for \(n\ge 1\), every continuous map \(f:X_n\to X_m\) induces a null-homotopic map \(|K(f)|:S^n\to S^m\) unless \(n=m\) and \(f\) is a homeomorphism. Hence minimal sphere models directly realize only the zero class when \(n\ne m\), and exactly the degree classes \(-1,0,1\) when \(n=m\); in particular no nonzero unstable class with \(n>m\), and no self-map of degree \(|d|\ge 2\), is represented without enlarging or subdividing the finite model.

Equivalently, if \(L_i=\{{a_i,b_i\}}\) is the \(i\)-th two-point level of \(X_n\), then a continuous map between minimal sphere models is either forced to collapse one entire level \(L_i\) to one target point, in which case the image order complex is a cone, or—only when the source and target dimensions agree—it is a levelwise permutation and hence a homeomorphism.

## Assumptions and scope
For \(n\ge 1\), let \(X_n\) be the ordinal (non-Hausdorff) join of \(n+1\) copies of the discrete two-point space \(S^0\). Thus \(X_n\) has levels \(L_0,\ldots,L_n\), each of size two, with every point of \(L_i\) below every point of \(L_j\) for \(i<j\), and no comparability inside a level. Its order complex is the join of \(n+1\) copies of \(S^0\), hence the boundary of the \(n+1\)-dimensional cross-polytope and therefore a triangulated \(S^n\). Barmak and Minian proved that this is the unique \(2n+2\)-point minimal finite model of \(S^n\).

For a continuous map \(f:X_n\to X_m\), continuity is equivalent to order preservation. The phrase “realizes a homotopy class” refers to the class of the induced simplicial map \(K(f):K(X_n)\to K(X_m)\) after identifying the two order-complex realizations with spheres.

## Proof
Write \(M_0,\ldots,M_m\) for the two-point levels of the target and let \(\rho\) be the target rank, so \(\rho(M_j)=j\). Call a source level \(L_i\) *noncollapsed* when its two points have distinct images.

First, consider two noncollapsed source levels \(L_i,L_j\) with \(i<j\), and define
\[
r_i=\min\{\rho(f(a_i)),\rho(f(b_i))\}.
\]
Then \(r_i<r_j\). Indeed, if the two images of \(L_i\) have different ranks, their larger rank is strictly bigger than \(r_i\), while order preservation forces every image of \(L_j\) to have rank at least that larger rank. If instead the two images of \(L_i\) are the two distinct points of one target level \(M_{r_i}\), a target point lying above both must have rank strictly larger than \(r_i\); again \(r_j>r_i\). Consequently the minimum target ranks of noncollapsed source levels form a strictly increasing sequence in \(\{0,\ldots,m\}\). There can therefore be at most \(m+1\) noncollapsed source levels.

If \(n>m\), the source has \(n+1>m+1\) levels, so some level \(L_i\) is collapsed: \(f(a_i)=f(b_i)=v\). In that case the image subcomplex of \(K(f)\) is a cone with apex \(v\). To see this, take any simplex \(\tau\) in the image and a source chain \(\sigma\) mapping onto it. If \(\sigma\) contains one of \(a_i,b_i\), then \(v\in\tau\). If it contains neither, adjoining \(a_i\) preserves the chain condition because every point in a different source level is comparable with \(a_i\); hence \(\tau\cup\{v\}\) is also in the image. Thus the image is contractible and \(|K(f)|\) is null-homotopic.

Now suppose \(n=m\). If a level is collapsed, the same cone argument applies. Otherwise all \(n+1\) source levels are noncollapsed. The strict sequence \(r_0<\cdots<r_n\) uses all integers from \(0\) to \(n\), so \(r_i=i\). The top level \(L_n\) must therefore map bijectively to \(M_n\). Descending inductively, assume \(L_{i+1}\) maps onto the two distinct points of \(M_{i+1}\). Every image of \(L_i\) lies below both of those points. No point of rank \(i+1\) can lie below both distinct points of \(M_{i+1}\), so both images have rank at most \(i\). Since their minimum rank is \(i\) and they are distinct, they are exactly the two points of \(M_i\). Hence every level maps bijectively to the corresponding target level, and \(f\) is a poset automorphism, hence a homeomorphism.

Finally, if \(n<m\), the induced map is null-homotopic because \(\pi_n(S^m)=0\). When \(n=m\), a homeomorphism has degree \(\pm1\); both signs occur, since the identity has degree \(+1\) and swapping the two vertices in one join factor is a reflection of the cross-polytope sphere and has degree \(-1\). A collapsed-level map is null-homotopic and has degree \(0\). This proves the stated classification.

## Verification
The proof is purely finite and combinatorial up to the standard fact \(\pi_n(S^m)=0\) for \(n<m\). The critical points checked directly are: (1) noncollapsed source levels have strictly increasing minimum target ranks; (2) a collapsed source level makes the simplicial image a cone; and (3) in equal dimensions, absence of a collapsed level forces a levelwise bijection by descending induction. Small cases \(1\le n,m\le3\) were also exhaustively enumerated as a sanity check; the enumeration is not used as proof.

## Relationship to prior work
Barmak and Minian identify \(X_n\) as the unique minimal finite model of \(S^n\) and recall that maps of finite \(T_0\)-spaces are order-preserving. Earlier work on finite models of maps demonstrates that nontrivial classical sphere maps often require larger or subdivided finite models: Hardie and Witbooi model the Whitehead square in \(\pi_3(S^2)\) using a 56-point model of \(S^3\) mapping to the six-point minimal model of \(S^2\), while Hardie, Salbany, Vermeulen and Witbooi use a barycentric subdivision of the minimal \(S^3\) model in a quaternion-multiplication construction. The theorem above supplies a general obstruction explaining why a nonzero class with source dimension larger than target dimension cannot be represented directly between the two minimal sphere models.

Mosquera-Lois proves a 2026 Whitehead-type rigidity theorem for weak homotopy equivalences into facet-essential minimal finite models. That result overlaps the equal-dimensional nonzero-degree endpoint: its simplicial cohomology lemma can force surjectivity for suitable cohomologically injective self-maps. It does not state or imply the cross-dimensional nullity theorem by itself, nor the complete directly-realized class set for all pairs \(X_n,X_m\).

## Limitations
The result concerns maps directly between the canonical minimal finite sphere models. It does not obstruct representing nontrivial sphere maps after subdivision or enlargement of the source or target, and it gives no lower bound on how many additional points are necessary. The full texts of two older map-construction papers were not accessible during this check because the publisher required human verification; their abstracts and bibliographic records were inspected. This leaves a residual risk of unlocated partial overlap in those papers, although their accessible statements are specific constructions rather than the general all-dimensions obstruction proved here.

## References
1. J. A. Barmak and E. G. Minian, “Minimal Finite Models,” arXiv:math/0611156 (submitted 6 Nov 2006); later J. Homotopy Relat. Struct. 2 (2007), 127–140.
2. K. A. Hardie and P. J. Witbooi, “The Whitehead square of the 6-point 2-sphere,” Quaestiones Mathematicae 29 (2006), 1–7, DOI 10.2989/16073600609486146.
3. K. A. Hardie, S. Salbany, J. J. C. Vermeulen and P. J. Witbooi, “A non-Hausdorff quaternion multiplication,” Theoretical Computer Science 305 (2003), 135–158, DOI 10.1016/S0304-3975(02)00703-X.
4. D. Mosquera-Lois, “Whitehead's theorem for minimal finite models,” arXiv:2608.06176 (submitted 6 Aug 2026).
