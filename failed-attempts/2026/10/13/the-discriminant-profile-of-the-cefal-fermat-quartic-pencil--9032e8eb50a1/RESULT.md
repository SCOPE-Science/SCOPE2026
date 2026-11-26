# The discriminant profile of the Cefalù–Fermat quartic pencil
## Finding
Consider the pencil of quartic surfaces in \(\mathbb P^3_{\mathbb C}\)
\[
X_t:\quad F_t=(z_1^2+z_2^2+z_3^2+z_4^2)^2+t(z_1^4+z_2^4+z_3^4+z_4^4)=0
\]
for finite \(t\), with the member \(t=\infty\) interpreted as the Fermat quartic \(z_1^4+z_2^4+z_3^4+z_4^4=0\). This is the one-dimensional family singled out by Catanese as the pencil with the coordinate-sign and permutation symmetry containing both the Fermat quartic and the Cefalù quartic.

The singular fibres admit a complete exact description. The member \(X_0\) is the nonreduced double smooth quadric. For each \(k\in\{1,2,3,4}\), the member \(X_{-k}\) is irreducible and normal and has exactly
\[
N_k=\binom{4}{k}2^{k-1}
\]
ordinary nodes. Hence the four reduced singular members have respectively \(4,12,16,8\) nodes. Their singular points are exactly those projective points having precisely \(k\) nonzero coordinates and having all nonzero squares equal. Each nodal set is one orbit under signed coordinate permutations. Every other member, including the Fermat member at \(t=\infty\), is smooth.

The scheme-theoretic discriminant divisor of the pencil is also determined exactly. Up to multiplication by a nonzero constant, its affine equation is
\[
\Delta(t)=t^{68}(t+1)^4(t+2)^{12}(t+3)^{16}(t+4)^8.
\]
In particular, the Cefalù quartic is the unique sixteen-nodal member, while the nonreduced double quadric carries discriminant multiplicity \(68\).

## Assumptions and scope
The ground field is \(\mathbb C\). The statement concerns this specific projective line in the space of quartic forms, not arbitrary quartic surfaces. The parameter normalization agrees with Catanese's expression \(\lambda_1s_1(z_i^2)^2+\lambda_2s_2(z_i^2)=0\) on the affine chart \(\lambda_1=1\), so \(t=\lambda_2\). Catanese lists the five finite singular parameters \(t=0,-1,-2,-3,-4\); the new contribution is the exact singularity basket at every one of them and the complete discriminant multiplicity profile.

## Proof
Put
\[
S=\sum_{i=1}^4z_i^2,\qquad Q=\sum_{i=1}^4z_i^4,
\]
so that \(F_t=S^2+tQ\). The partial derivatives are
\[
\frac{\partial F_t}{\partial z_i}=4z_i(S+t z_i^2).
\]
Assume first that \(t\ne0\) and that \(p=[z_1:z_2:z_3:z_4]\) is singular. For every nonzero coordinate, the derivative equation gives \(z_i^2=-S/t\). Thus all nonzero coordinate squares have a common value \(u\ne0\). If exactly \(k\) coordinates are nonzero, then \(S=ku\), hence \(0=S+tu=(k+t)u\), so necessarily \(t=-k\). Conversely, for \(t=-k\), every projective point with exactly \(k\) nonzero coordinates and common nonzero square is singular; substituting \(S=ku\) and \(Q=ku^2\) gives \(F_{-k}=0\). There are \(\binom4k\) support choices and \(2^{k-1}\) sign choices modulo common projective sign, proving
\[
N_k=\binom4k2^{k-1}=(4,12,16,8).
\]
Signed coordinate permutations are transitive on each such set.

Each of these singularities is an ordinary node. By symmetry it suffices to use, in the affine chart \(z_4=1\), the representatives with \(k-1\) of \(z_1,z_2,z_3\) equal to \(1\) and the rest \(0\). The determinants of the three-variable Hessians at these representatives, for \(k=1,2,3,4\), are respectively
\[
64,\quad -512,\quad 2304,\quad -8192,
\]
all nonzero. Therefore every singularity is of type \(A_1\). The gradient calculation already proves that there are no other singular points. Since a reducible quartic surface in \(\mathbb P^3\) would have a positive-dimensional component intersection contained in its singular locus, the fibres \(X_{-k}\) are irreducible. A hypersurface with isolated singularities is regular in codimension one and is Cohen--Macaulay, so these irreducible fibres are normal.

At \(t=0\), one has \(F_0=S^2\), hence a double copy of the smooth quadric \(S=0\). The member at \(t=\infty\) is smooth because the four partial derivatives of \(Q\) are \(4z_i^3\), which have no common projective zero. The preceding gradient argument proves that there are no further singular members.

It remains to compute the multiplicities of the discriminant. The discriminant of quartic hypersurfaces in \(\mathbb P^3\) has degree \(108\): it is, up to a nonzero constant, the resultant of the four cubic partial derivatives, and the resultant has degree \(3^3=27\) in the coefficients of each of its four inputs, hence total degree \(4\cdot27=108\) after the partials are substituted linearly in the quartic coefficients. At a node of \(X_{-k}\), the first-order deformation in the pencil is represented by \(Q\), and at every listed node \(Q=ku^2\ne0\). Thus the pencil is transverse to the local reduced discriminant branch of each \(A_1\) singularity. The discriminant multiplicity at \(t=-k\) is therefore exactly the number \(N_k\) of nodes. Their total contribution is
\[
4+12+16+8=40.
\]
There is no contribution at infinity because the Fermat member is smooth, and no other finite support. The remaining multiplicity at \(t=0\) is consequently \(108-40=68\), yielding the asserted factorization.

## Verification
The accompanying `verify.py` independently enumerates the support/sign representatives, checks the singular equations, constructs the affine Hessian matrices and reproduces determinants \(64,-512,2304,-8192\), verifies the transversality value \(Q=k\) after the common square is normalized to \(1\), and checks that the discriminant exponents sum to \(108\). A fresh extraction from the packaged row returns `VERIFY_OK`.

The finite computation supplements, but does not replace, the symbolic proof: the exclusion of all other singular fibres follows from the factored gradient equations, and the exponent \(68\) uses the global discriminant degree together with the proved local transversality.

## Relationship to prior work
Catanese introduces the Cefalù quartic, proves that it has sixteen nodes, identifies its large symmetry, and explicitly singles out the pencil containing the Fermat and Cefalù quartics. He states that the pencil has five singular finite members, at parameters \(0,-1,-2,-3,-4\). The inspected text does not give the complete baskets \(4A_1,12A_1,16A_1,8A_1\) for the four reduced members or the discriminant multiplicities \(68,4,12,16,8\).

Dolgachev and Kondō study quartic surfaces with rational double points and Kummer quartics from the viewpoint of bitangents and involutions. Their inspected arXiv text does not discuss the Cefalù pencil or the above discriminant profile. Searches in the compared database and in the available prior result ledgers under equation, parameter, singular-fibre, node-count, and discriminant aliases found no statement implying the result.

## Limitations
The result is specific to characteristic zero and to this highly symmetric pencil. The argument does not classify deformations transverse to this projective line, nor does it determine monodromy on the minimal resolutions. The multiplicity \(68\) at the double quadric is determined globally from the degree of the discriminant after the reduced nodal contributions are proved transverse; no finer local primary decomposition of the discriminant at the double quadric is asserted.

## References
1. Fabrizio Catanese, *Kummer quartic surfaces, strict self-duality, and more*, arXiv:2101.10501v1, first public 2021-01-26. See the introduction around Theorem 1 for the Cefalù quartic, its sixteen nodes, its symmetry, and the symmetric pencil with five singular finite members.
2. Igor Dolgachev and Shigeyuki Kondō, *Bitangent surfaces and involutions of quartic surfaces*, arXiv:2406.16246v1, first public 2024-06-24.
