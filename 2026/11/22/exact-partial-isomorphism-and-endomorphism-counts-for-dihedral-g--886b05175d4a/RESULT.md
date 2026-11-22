# Exact partial-isomorphism and endomorphism counts for dihedral groups

## Finding

For a finite group \(H\), let \(\operatorname{PIso}(H)\) be the set of all isomorphisms between *subgroups* of \(H\), with domain and range included in the data, and let \(\operatorname{End}(H)\) be its group endomorphisms.

**Theorem.** Let \(A\ne1\) be a finite abelian group of odd order \(N\), and set \(G=\operatorname{Dih}(A)=A\rtimes\langle s\rangle\), where \(s\) acts by inversion. Let \(\mathcal T(A)\) consist of the isomorphism types of subgroups of \(A\). For \([B]\in\mathcal T(A)\), write \(b=|B|\), \(a_B=|\operatorname{Aut}(B)|\), and \(h_B=|\{C\le A:C\cong B\}|\). Then

\[
|\operatorname{PIso}(G)|=\sum_{[B]\in\mathcal T(A)}h_B^2 a_B\left(1+\frac{N^2}{b}\right),\qquad
|\operatorname{End}(G)|=N|\operatorname{End}(A)|+1.
\]

In particular,

\[
|\operatorname{PIso}(G)|\ge(N+1)|\operatorname{End}(A)|>|\operatorname{End}(G)|.
\]

The ordinary dihedral groups also have an explicit **all-parity** formula. For \(D_{2n}=\langle r,s:r^n=s^2=1,\ srs=r^{-1}\rangle\), \(n\ge3\), and \(\epsilon_n=1\) when \(n\) is even and \(0\) otherwise,

\[
|\operatorname{PIso}(D_{2n})|=n^2\left(\sum_{d\mid n}\frac{\varphi(d)}d+\epsilon_n\right)+n(1+2\epsilon_n),
\]
\[
|\operatorname{End}(D_{2n})|=
\begin{cases} n^2+1,&n\text{ odd},\\(n+2)^2,&n\text{ even}.\end{cases}
\]

Both expressions give a strict inequality for all \(n\ge3\). For an odd prime \(p\), the two counts are \(2p^2\) and \(p^2+1\). For \(n=2^k\), \(k\ge2\), the counts are \((k+4)n^2/2+3n\) and \((n+2)^2\); hence the ratio is unbounded as \(k\to\infty\).

## Assumptions and scope

All groups are finite, and subgroup isomorphisms are ordinary group isomorphisms. The first set of identities requires that \(A\) have odd order; it does not assert the same type formula when \(A\) has two-torsion. The ordinary dihedral formulas hold for every integer \(n\ge3\), including even \(n\). In every count, the trivial subgroup and its unique identity map contribute one partial isomorphism.

## Proof

**1. Subgroups of an odd generalized dihedral group.** Every subgroup of \(G\) contained in \(A\) is some \(C\le A\). If \(H\nsubseteq A\), then \(C=H\cap A\) has index two in \(H\). The other coset contains an involution \(sa\), so \(H=C\cup(sa)C\cong\operatorname{Dih}(C)\). For each fixed \(C\), exactly \(N/|C|\) outside subgroups arise: they are indexed by the cosets \(aC\in A/C\). Distinct isomorphism types of \(C\) yield distinct outside-subgroup types because the derived group of \(\operatorname{Dih}(C)\) is \(C\): inversion has commutator subgroup \(C^2=C\) when \(|C|\) is odd. The case \(C=1\) gives a group of order two; it remains distinct from all odd-order subgroup types.

For \(C\ne1\), every automorphism of \(\operatorname{Dih}(C)\) preserves its odd-order subgroup \(C\), restricts to an arbitrary automorphism of \(C\), and sends \(s\) to one of the \(|C|\) involutions outside \(C\). Conversely each such choice defines an automorphism. The same counting identity holds for \(C=1\). Therefore

\[
|\operatorname{Aut}(\operatorname{Dih}(C))|=|C|\,|\operatorname{Aut}(C)|.
\]

For a fixed subgroup isomorphism type \(B\), there are \(h_B\) inside subgroups and \(Nh_B/b\) outside subgroups. Consequently the number of isomorphisms between inside subgroups of type \(B\) is \(h_B^2a_B\), while between outside subgroups of type \(\operatorname{Dih}(B)\) it is \((Nh_B/b)^2ba_B\). Summation gives the first formula. (Inside and outside types cannot coincide since their orders have different parity.)

**2. Endomorphisms.** Every homomorphism \(G\to G\) maps \(A\) into \(A\), since every element of \(A\) has odd order. If the reflection \(s\) has an outside image, it can be sent to any of the \(N\) reflections, while its restriction to \(A\) is any endomorphism of \(A\); the inversion relation is automatically respected. If \(s\) is not sent outside, its image is the identity (there is no nonidentity involution in \(A\)); the inversion relation forces every image of \(A\) to equal its inverse, so the entire endomorphism is trivial. The second formula follows.

**3. Strict inequality.** For any finite abelian group \(A\), the identity

\[
\sum_{[B]\in\mathcal T(A)}h_B^2a_B=|\operatorname{End}(A)|
\]

follows by subgroup duality, as proved by Cameron (2025). Since \(b\le N\), every factor \(1+N^2/b\) in the first formula is at least \(N+1\). Since \(A\ne1\), its identity and zero maps are distinct, so \(|\operatorname{End}(A)|\ge2\), proving strict inequality.

**4. Ordinary dihedral groups.** Every subgroup is one of the unique rotation groups \(C_d\), for \(d\mid n\), or one of the \(n/d\) subgroups \(D_{2d}\), for \(d\mid n\), with \(D_2=C_2\). For even \(n\), the rotation subgroup \(C_2\) is isomorphic to all \(n\) reflection subgroups, giving \(n+1\) subgroups of type \(C_2\). Also \(D_4=C_2\times C_2\) has six automorphisms; for \(d\ge3\), \(|\operatorname{Aut}(D_{2d})|=d\varphi(d)\). Thus for odd \(n\) the general formula above applies, and for even \(n\) direct type counting yields

\[
|\operatorname{PIso}(D_{2n})|=1+(n+1)^2+\sum_{\substack{d\mid n\\d\ge3}}\varphi(d)
+\frac{3n^2}{2}+n^2\sum_{\substack{d\mid n\\d\ge3}}\frac{\varphi(d)}d.
\]

Using \(\sum_{d\mid n}\varphi(d)=n\) gives the claimed unified parity formula.

For the endomorphisms, let \(x\) and \(y\) be the images of \(r\) and \(s\), respectively. The presentation requires \(x^n=y^2=1\) and \(yxy=x^{-1}\). There are \(n^2\) choices with \(x\) a rotation and \(y\) a reflection. With both images rotations, there is one choice if \(n\) is odd and four if \(n\) is even. Only for even \(n\) may \(x\) be a reflection; then there are \(n\) choices for \(x\) and four involutions \(y\) centralizing it. This gives \(n^2+1\) or \(n^2+4+4n=(n+2)^2\).

For even \(n\ge4\), the terms \(d=1,2\) in the divisor sum already yield \(|\operatorname{PIso}|\ge5n^2/2+3n>(n+2)^2\); for odd \(n\ge3\), \(|\operatorname{PIso}|\ge n^2+n>n^2+1\). The specializations for primes and powers of two follow by evaluating the divisor sum. This completes the proof.

## Verification

The accompanying `checks/check_dihedral.py` independently enumerates the actual subgroup lattice, groups subgroups by isomorphism type, and counts all generator-image homomorphisms in the dihedral presentation for every \(3\le n\le16\), confirming both formulas. Its output ends in `DIHEDRAL_PARTIAL_ISOMORPHISM_OK 3..16`.

The separate `checks/check_generalized_dihedral.py` constructs the full multiplication law of \(\operatorname{Dih}(C_3\times C_3)\), enumerates its 28 actual subgroups, and independently counts their automorphisms and the full group's endomorphisms via generators and relation consistency. It obtains \(1458\) partial isomorphisms and \(730\) endomorphisms, matching the theorem. These finite calculations test the proof but are not substitutes for its infinite-family arguments. Both scripts use only Python's standard library.

## Relationship to prior work

Cameron (2025) proves equality of partial-isomorphism and endomorphism counts for finite abelian groups and explicitly asks whether the former strictly exceeds the latter for **every** finite nonabelian group. The result above establishes that proposed inequality for all odd-kernel generalized dihedral groups and all ordinary dihedral groups, with full count formulas; it does not settle the question for other nonabelian groups. Classical dihedral subgroup descriptions and automorphism counts are used as ingredients, not claimed new. The literature comparisons distinguish subgroup-commuting probabilities, partial automorphisms of *semigroups*, and partial automorphisms of *graph actions* from isomorphisms between subgroups of an abstract group.

## Limitations

The result is specific to the stated group families. It does not classify all finite nonabelian groups or calculate the multiplication structure of the partial-isomorphism inverse monoid. The formula for an odd abelian kernel is a finite sum over subgroup isomorphism types, not necessarily an elementary closed expression in arbitrary invariant factors. Indexed literature searches cannot exclude unindexed earlier derivations. Verification is mathematical and computational within the stated scope; there has been no independent external audit.

## References

1. P. J. Cameron, *Endomorphisms and partial isomorphisms*, Semigroup Forum **111** (2025), 538–539, https://doi.org/10.1007/s00233-025-10514-5 (first public date: 2025-03-14).
2. S. M. Goberstein, *\(\mathcal{PA}\)-isomorphisms of inverse semigroups*, Algebra Universalis **53** (2005), 407–424, https://doi.org/10.1007/s00012-005-1910-8 (background on a different partial-automorphism construction).
3. *Fixed Points of Automorphisms of Certain Non-Cyclic \(p\)-Groups and the Dihedral Group*, Symmetry **10** (2018), 238, https://doi.org/10.3390/sym10070238 (classical dihedral automorphism parameterization).
