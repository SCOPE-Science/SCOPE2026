# Rooted-forest dynamics and complete image spectra of connected finite KD45 modal algebras

## Finding

Let \(c\ge1\) and \(s\ge0\). Let \(F_{c,s}=(X,R)\) be a finite connected serial, transitive, Euclidean Kripke frame with its uniquely determined nonempty reflexive cluster \(C\), of size \(c\), and the remaining set \(S=X\setminus C\), of size \(s\), where \(xRy\) holds exactly when \(y\in C\). These are precisely the connected finite KD45 frames up to isomorphism. Let \(\mathcal B_{c,s}=(\mathcal P(X),\Diamond)\), where \(\Diamond U=\{x\in X: R(x)\cap U\ne\varnothing\}\), be the associated finite Boolean modal algebra.

A **bounded map** \(f:F_{c,s}\to F_{d,t}\) means a function (not assumed onto) satisfying \(f[R(x)]=R(f(x))\) for every \(x\). Every such map has the exact normal form
\[
 f[C]=D,\qquad f[S]\subseteq D\cup T\text{ arbitrary},
\]
where \(D,T\) are the core and satellites of the target. In particular, the complete hom-set cardinality is
\[
 \bigl|\operatorname{BHom}(F_{c,s},F_{d,t})\bigr|
   =d!\left\{\begin{matrix}c\\d\end{matrix}\right\}(d+t)^s.
\]
The Stirling number is zero when \(d>c\), and its usual convention applies if \(s=0\).

The bounded endomorphisms are dual to the endomorphisms of \(\mathcal B_{c,s}\), by inverse image. Let \(E_{c,s}(z)\) enumerate all such algebra endomorphisms by the cardinality of their algebraic image, \(I_{c,s}(z)\) enumerate the idempotents the same way, and \(A_{c,s}(z)\) enumerate all endomorphisms by the cardinality of the eventual algebraic image under iterates. Set
\[
 B_{s,j}(c)=\sum_{i=0}^{j}(-1)^{j-i}\binom ji(c+i)^s,
 \qquad
 F(n,r)=\begin{cases}1,&n=0,\\r(r+n)^{n-1},&n\ge1.\end{cases}
\]
Then the exact triple of spectra, for all \(c\ge1,s\ge0\), is
\[
 \boxed{E_{c,s}(z)=c!\sum_{j=0}^{s}\binom sj B_{s,j}(c)z^{2^{c+j}}},
\]
\[
 \boxed{I_{c,s}(z)=\sum_{j=0}^{s}\binom sj(c+j)^{s-j}z^{2^{c+j}}},
\]
\[
 \boxed{A_{c,s}(z)=c!\sum_{j=0}^{s}\binom sj j! F(s-j,c+j)z^{2^{c+j}}}.
\]
In particular, all three polynomials have exactly the same positive support \(\{2^c,2^{c+1},\ldots,2^{c+s}\}\), and exactly \(2^s\) subsets of \(X\) occur as embedded dual-frame retraction images: the subsets \(C\cup J\) with \(J\subseteq S\). These correspond to image modal algebras isomorphic to \(\mathcal B_{c,j}\) for the respective \(j\).

For the five-world frame \(F_{2,3}\), the three spectra are respectively
\[
 \begin{aligned}
 E_{2,3}(z)&=16z^4+114z^8+108z^{16}+12z^{32},\\
 I_{2,3}(z)&=8z^4+27z^8+12z^{16}+z^{32},\\
 A_{2,3}(z)&=100z^4+90z^8+48z^{16}+12z^{32}.
 \end{aligned}
\]
Thus its modal algebra has \(250\) endomorphisms and \(48\) idempotents. The eventual-image distribution differs substantially from the one-step image distribution although their attainable ranks agree.

## Assumptions and scope

All sets, frames, and algebras are finite. Connectedness is for the undirected adjacency graph of the relation. The frame has exactly one nonempty reflexive cluster, while its other points are nonreflexive satellites; the parameter \(s=0\) is allowed. Algebra endomorphisms preserve all Boolean operations and the modal operator \(\Diamond\). A non-surjective bounded map is permitted; this is deliberately distinguished from the convention that a “p-morphism” must be onto. Eventual algebraic image means the stabilized image of an iterated endomorphism, not a limit in a topology. Ranks count **elements in the algebraic image**, not cardinalities of the dual-frame images.

## Proof

**1. Frame normal form.** For any finite connected serial Euclidean frame, the nonempty set \(U\) of all successor points is a reflexive equivalence cluster. Transitivity implies that a point outside \(U\) has successor set equal to its attached cluster; connectedness forces the same cluster for every such point. Thus \(R(x)=C\) for all \(x\in X\), establishing the stated form. Equivalently, this follows from the connected KD45-frame structural calculation in Sliusarev (2024), proof of Theorem 3.17. For a function between such frames, the bounded condition is precisely \(f[C]=D\), independent of the argument \(x\). On the core, this is a surjection to \(D\), counted by \(d!\left\{\begin{matrix}c\\d\end{matrix}\right\}\); the satellites have \((d+t)^s\) independent choices.

**2. Duality and one-step image spectrum.** Every Boolean homomorphism between finite powerset algebras is inverse image under a unique set map. It preserves \(\Diamond\) exactly when this set map is bounded: checking singleton sets gives the backward and forward correspondence, and arbitrary sets follow by unions. For a self-map, \(f[C]=C\) means its restriction to the \(c\)-element core is a permutation. For a prescribed set of \(j\) satellite image points, inclusion–exclusion gives \(B_{s,j}(c)\) ways for the \(s\) source satellites to hit every prescribed satellite while allowing arbitrary hits in the core. Multiply by \(c!\binom sj\). The Boolean image of the inverse-image endomorphism has cardinality \(2^{|f[X]|}=2^{c+j}\).

**3. Idempotents and retracts.** If \(f^2=f\) then the core permutation is the identity. A prescribed image \(C\cup J\), for \(|J|=j\), must be pointwise fixed. Each of the remaining \(s-j\) satellites maps freely into \(C\cup J\), giving \((c+j)^{s-j}\) retractions. Every subset \(C\cup J\) occurs and no other subset does. The same statement holds for the dual idempotent algebra endomorphism.

**4. Eventual-image forest law.** For any map of a finite set, \(\bigcap_{n\ge0}f^n[X]\) consists of all periodic vertices of the functional digraph. The core is permuted, so all its points are periodic. If the periodic satellites are precisely \(J\), of cardinality \(j\), then \(f|_J\) must be a permutation (\(j!\) choices), and every satellite outside \(J\) lies in a rooted directed forest whose edges lead eventually to one of the \(c+j\) specified roots. There can be no further directed cycles. For \(n=s-j\) nonroots and \(r=c+j\) roots, the exact number of such forests is \(F(n,r)\). For \(n\ge1\), the all-minors matrix-tree calculation has reduced Laplacian \((n+r)I_n-J_n\), with determinant \(r(n+r)^{n-1}\); for \(n=0\) the empty forest is unique. The independent core permutation, set choice \(J\), permutation of \(J\), and rooted forest give the formula for \(A_{c,s}\). The inverse-image endomorphism has stabilized image size \(2^{c+j}\).

**5. Support and boundary cases.** For every \(0\le j\le s\), the corresponding idempotent coefficient is positive because \(c\ge1\), so each advertised rank occurs in all three spectra. If \(s=0\), all bounded endomorphisms are permutations of the core, the identity is the only idempotent, and the formulas reduce to \(E_{c,0}(z)=A_{c,0}(z)=c!z^{2^c}\), \(I_{c,0}(z)=z^{2^c}\), as required.

## Verification

The standalone file `verify_kd45.py` independently enumerates all function tables for connected frames through six worlds, checks the bounded-map definition directly on successor sets, counts ordinary, idempotent, and stable images, and compares them with all three formulas. It also enumerates source-target pairs through four worlds and compares the hom-set formula, including non-surjective maps and zero satellites. For selected small frames, it verifies preservation of the modal operator on **every** Boolean subset, independently of the successor-set characterization.

A completed local replay returned `VERIFY_OK function_tables 296675 bounded_maps 15403 hom_pairs 100 modal_algebra_checks 550 exact_comparisons 205`, followed by the stated \((c,s)=(2,3)\) example. This is finite corroboration; the proof above handles arbitrary finite parameters. Run `python3 verify_kd45.py` in the directory containing this document.

## Relationship to prior work

Sliusarev's 2024 paper studies the almost-sure valid modal formulas of finite KD45 frames and explicitly identifies each connected KD45 frame by its nonempty reflexive cluster (proof of Theorem 3.17); that structural normal form and the classical theory of bounded morphisms are not claimed as new. Pitman's forest-enumerator work and classical Cayley/matrix-tree formulas already provide the rooted-forest factor \(F(n,r)\), also not claimed as new. The contribution claimed here is their combined **exact interpretation as the three complete, algebra-image-graded dynamical spectra** (one-step, idempotent, eventual) of every connected finite KD45 Boolean modal algebra, together with a complete cross-size bounded-homomorphism normal form. An implicit general transformation-semigroup statement may already imply these formulas; no claim of novelty of the constituent forest identity is made.

## Limitations

The findings apply to connected finite KD45 frames, not arbitrary disjoint unions of such components, not infinite frames, and not the more general KD5 class without transitivity. The proof does not claim any asymptotic distribution or new modal axiomatization. Its novelty assessment relies on inspected and indexed literature and may miss implicit or unindexed antecedents. The finite verifier does not replace the general proof. An independent mathematical audit has not been performed.

## References

1. Vladislav Sliusarev, *Modal logics of almost sure validities in some classes of Euclidean and transitive frames*, arXiv:2406.10770v1, first submitted 2024-06-16, revised 2024-10-18. Full-text version: https://arxiv.org/html/2406.10770v3 ; see Section 3, Theorem 3.17 and its proof. Primary MSC 03B45.
2. Jim Pitman, *Forest Volume Decompositions and Abel–Cayley–Hurwitz Multinomial Expansions*, Journal of Combinatorial Theory A 98 (2002), 175–191, DOI:10.1006/jcta.2001.3238. Author-hosted paper: https://www.stat.berkeley.edu/~pitman/591.pdf.
3. Jim Pitman, *Random Mappings, Forests, and Subsets Associated with Abel–Cayley–Hurwitz Multinomial Expansions*, Séminaire Lotharingien de Combinatoire B46h (2001). https://www.mat.univie.ac.at/~slc/wpapers/s46pitman.html.
