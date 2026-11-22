# Affine-to-dihedral automorphism collapse for cyclic and wheel partial-isometry monoids

## Finding

For a finite metric space \((X,d)\), let \(\mathcal I(X,d)\) be the inverse monoid of all distance-preserving partial bijections, including the empty map. Its **abstract monoid automorphism group** is canonically the group of permutations of \(X\) that may permute the *names of positive distance classes* but preserve equality of distances. Concretely,

\[
\operatorname{Aut}(\mathcal I(X,d))\cong
\left\{\pi\in\operatorname{Sym}(X):
 d(x,y)=d(u,v)\iff
 d(\pi x,\pi y)=d(\pi u,\pi v)
 \quad(x\ne y,\;u\ne v)\right\}.
\]

Let \(C_n\) be the simple cycle on \(\mathbb Z/n\mathbb Z\), endowed with shortest-path distance, for every \(n\ge3\). Let \(W_n=K_1\vee C_n\) be its wheel with one universal hub, for every \(n\ge5\). Then

\[
\boxed{\operatorname{Aut}(\mathcal I(C_n))\cong
 C_n\rtimes(\mathbb Z/n\mathbb Z)^\times,\qquad
 |\operatorname{Aut}(\mathcal I(C_n))|=n\varphi(n)}
\]

and

\[
\boxed{\operatorname{Aut}(\mathcal I(W_n))\cong
 D_{2n},\qquad
 |\operatorname{Aut}(\mathcal I(W_n))|=2n.}
\]

The first group acts on cycle vertices by the affine permutations \(x\mapsto a+ux\), where \(a\in\mathbb Z/n\mathbb Z\) and \(u\) is a multiplicative unit; the second fixes the hub and acts on the rim by \(x\mapsto a\pm x\). Here \(D_{2n}\) denotes the group of order \(2n\). When \(\varphi(n)>2\), adjoining a universal wheel hub removes all non-dihedral monoid automorphisms.

## Assumptions and scope

The metric is finite and has strictly positive distance between distinct points. All partial bijections are allowed, with empty domain permitted. The automorphisms are abstract, composition-preserving bijections of the **monoid**; they are not assumed a priori to be given by vertex relabeling or metric isometries. Distances on each graph mean shortest-path graph distances. There is no claim here about nonbijective graph-endomorphism monoids or about other graph families.

## Proof

**1. Every abstract automorphism is spatial.** A partial bijection \(f\) is idempotent exactly when it is the identity \(e_A\) on some subset \(A\subseteq X\). Since every \(e_A\) is distance-preserving, the idempotents of \(\mathcal I(X,d)\) form the full Boolean semilattice \((2^X,\cap)\). An abstract monoid automorphism \(\Phi\) permutes the atoms \(e_{\{x\}}\); write \(\Phi(e_{\{x\}})=e_{\{\pi(x)\}}\). This gives a unique \(\pi\in\operatorname{Sym}(X)\). An automorphism of an inverse monoid preserves inverses, since they are uniquely characterized by the inverse identities. Therefore \(\Phi(f^{-1}f)=\Phi(f)^{-1}\Phi(f)\) identifies the domain of \(\Phi(f)\) with \(\pi(\operatorname{dom}f)\). For each \(x\in\operatorname{dom}f\) and \(y=f(x)\), the product \(e_{\{y\}}\,f\,e_{\{x\}}\), with the usual right-to-left composition convention, is the unique singleton map \(x\mapsto y\). Its image under \(\Phi\) is the singleton \(\pi(x)\mapsto\pi(y)\). Thus \(\Phi(f)=\pi f\pi^{-1}\) on its full domain, and \(\pi\) is unique.

**2. Spatial normalization is equivalent to permuting distances.** Let \(\mathcal D=\{d(x,y):x\ne y\}\) denote the finite set of positive realized distances. There exists an element of \(\mathcal I(X,d)\) with domain \(\{x,y\}\) sending \(x\mapsto u\) and \(y\mapsto v\) if and only if \(d(x,y)=d(u,v)\). Conjugation by \(\pi\) preserves the monoid in both directions precisely when it preserves this equivalence for every pair of positive-distance vertex pairs. This is equivalent to a permutation \(\rho\) of \(\mathcal D\) satisfying \(d(\pi x,\pi y)=\rho(d(x,y))\). Conversely, this condition makes every partial distance-preserver conjugate to another partial distance-preserver: equality of all pairwise distances is preserved in both directions. The group displayed in the finding is therefore exact.

**3. The cycle is affine.** Suppose \(\pi\) normalizes the cycle monoid and sends the distance-one class to the distance-\(k\) class. For \(1\le k\le\lfloor n/2\rfloor\), the graph of distance-\(k\) pairs has \(\gcd(n,k)\) connected components when \(k<n/2\), and is a matching if \(k=n/2\). Since its image under \(\pi\) is the connected \(n\)-cycle, it follows that \(\gcd(k,n)=1\) and \(k<n/2\), except for the harmless triangle case \(n=3\), where the same conclusion holds. Every graph isomorphism from the standard cycle to the cycle with edges \(\{x,x+k\}\) has the form \(\pi(x)=a+ux\) with \(u=\pm k\) modulo \(n\). (Choose the image of vertex zero and one of its two neighbors; continuation around the cycle is forced.) Therefore \(u\in(\mathbb Z/n\mathbb Z)^\times\). Conversely, every affine permutation with unit multiplier preserves equality of circular distances: if two unordered differences are equal up to sign, their images after multiplication by \(u\) are also equal up to sign, and conversely. The normalizer consists of exactly the \(n\varphi(n)\) stated affine permutations.

**4. The wheel eliminates the multiplier freedom.** When \(n\ge5\), wheel distances between distinct vertices have exactly two classes: graph edges at distance one and nonedges at distance two. A distance-class-permuting permutation either preserves the graph edges or interchanges edges and nonedges. The latter would be a graph isomorphism from \(W_n\) to its complement, impossible because \(W_n\) has a vertex of degree \(n\), while its complement has maximum degree \(n-3\). Thus every normalizer is an ordinary graph automorphism of \(W_n\). The hub is the unique vertex of degree \(n\), so it is fixed, and the restriction to the rim belongs to \(\operatorname{Aut}(C_n)=D_{2n}\). Conversely all such rim dihedral permutations are wheel isometries and therefore normalize the monoid. This proves the second formula and the claimed contrast.

## Verification

The accompanying `verification.py` independently enumerates permutations of vertices and tests the equality-of-distance-class criterion, comparing the resulting sets with the stated affine and dihedral groups. It verifies cycles for every \(3\le n\le8\), and wheels for every \(5\le n\le7\). The observed cycle normalizer sizes are \(6,8,20,12,42,32\) for \(n=3,4,5,6,7,8\), respectively. The corresponding wheel normalizer sizes for \(n=5,6,7\) are \(10,12,14\). These are finite corroborations; the proof above establishes the unlimited parameters.

## Relationship to prior work

Fernandes and Paulista identify the cycle partial-isometry monoid with restrictions of the dihedral action and investigate presentation, Green's relations, cardinality and generating rank [1]. Fernandes investigates the wheel partial-isometry monoid and related subsemigroups, again through their ranks and Green's relations [2]. Jajcay, Jajcayová, Szakács and Szendrei develop a structural characterization of finite inverse monoids of partial graph automorphisms and their edge-colored analogues [3], providing a significant antecedent for rank-two reconstruction; the present result does **not** claim priority for general spatiality or for using pair-distance classes. Araújo and collaborators give a general method for automorphisms of partial endomorphism semigroups [4], but the accessible published abstract does not establish the two concrete distance-isometry monoid groups asserted here. The claimed distinction is the full *abstract automorphism group* of the two specific metric partial-isometry monoids, including the affine-to-dihedral drop, not the known groups of graph isometries, the rank of either monoid, or a novel general reconstruction technique.

## Limitations

No classification is asserted for all finite graph metrics. The claim concerns abstract automorphisms of inverse monoids, not automorphisms of the full graph endomorphism semigroups. Existing general monoid-automorphism methods may give another derivation; the full 2011 source [4] was not accessible for a page-by-page comparison. The literature comparison is evidence-based, not a proof of historical uniqueness. The verification script enumerates the normalizing vertex permutations in the specified finite range; it does not directly enumerate all abstract self-maps of these much larger monoids.

## References

[1] V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, arXiv:2205.02196 (first publicly posted 2022-05-04), https://arxiv.org/abs/2205.02196 ; Turkish Journal of Mathematics 47 (2023), 1746–1760, https://doi.org/10.55730/1300-0098.3460.

[2] V. H. Fernandes, *On the monoid of partial isometries of a wheel graph*, arXiv:2307.16257 (first publicly posted 2023-07-30), https://arxiv.org/abs/2307.16257.

[3] R. Jajcay, T. Jajcayová, N. Szakács and M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422 (2018), https://arxiv.org/abs/1809.04422 ; Journal of Algebraic Combinatorics 53 (2021), 829–849.

[4] J. Araújo, V. H. Fernandes, M. M. Jesus, V. Maltcev and J. D. Mitchell, *Automorphisms of partial endomorphism semigroups*, Publicationes Mathematicae Debrecen 79 (2011), 23–39, https://doi.org/10.5486/PMD.2011.4703 (abstract inspected; full text not obtained).
