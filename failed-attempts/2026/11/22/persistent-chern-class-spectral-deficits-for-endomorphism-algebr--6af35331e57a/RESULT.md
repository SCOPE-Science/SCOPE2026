# Persistent Chern-class spectral deficits for endomorphism algebras over even spheres

## Finding

Let \(k\ge 2\) and \(r\ge k\) be integers. For a rank-\(r\) complex vector bundle \(E\to S^{2k}\), let \(\mathcal A_E=\Gamma(S^{2k},\operatorname{End}E)\) denote its unital Banach (indeed \(C^*\)) algebra of continuous bundle endomorphisms. Define the spectral depth \(d_\sigma(\mathcal B)\) of a unital complex Banach algebra to be the supremum, over \(b\in\mathcal B\), of the number of connected components of \(\sigma_\mathcal B(b)\). Then, for every integer \(m\ge1\),

\[
d_\sigma(M_m(\mathcal A_E))=
\begin{cases}
rm,& c_k(E)=0,\\
rm-k+1,& c_k(E)\ne0.
\end{cases}
\]

In the nonzero-Chern case, every element whose spectrum has the maximal \(rm-k+1\) components has Riesz spectral subbundles of ranks \(k,1,\ldots,1\), up to permutation. The rank-one bundles are trivial, while the unique rank-\(k\) spectral subbundle has \(k\)-th Chern class equal to \(m c_k(E)\), and hence is determined up to bundle isomorphism by that class. Conversely, such a maximal-component element exists and can be chosen self-adjoint with constant finite spectrum.

Thus a nonzero top Chern class creates a sharp spectral-component deficit of exactly \(k-1\) at every matrix amplification; it never disappears on passage to larger finite matrices.

## Assumptions and scope

The sphere is the standard connected topological sphere of real dimension \(2k\), and vector bundles, homotopies, and endomorphisms are complex and continuous. The integers satisfy \(k\ge2\), \(r\ge k\), and \(m\ge1\). The Chern class \(c_k(E)\in H^{2k}(S^{2k};\mathbb Z)\cong\mathbb Z\) is evaluated integrally. The spectrum is the Banach-algebra spectrum, not the spectrum of the corresponding operator on all continuous sections or of a single fiber. The amplification uses the spatial matrix algebra and is canonically isomorphic to \(\Gamma(S^{2k},\operatorname{End}(E^{\oplus m}))\).

On \(S^{2k}\), the only potentially nonzero positive-degree Chern class of any complex vector bundle is its \(k\)-th Chern class. For rank at least \(k\), clutching classification and Bott integrality imply that its vanishing is equivalent to topological triviality. The necessary stable-range and integrality facts are used explicitly below.

## Proof

**1. Spectral components and bundle splittings.** Put \(F=E^{\oplus m}\) and \(R=rm\). A bundle Hermitian metric gives an isometric \(C^*\)-identification \(M_m(\mathcal A_E)\cong\Gamma(S^{2k},\operatorname{End}F)\). By the Riesz-idempotent criterion of Bračič--Kandić, having at least \(q\) spectral components is equivalent to the existence of \(q\) nonzero pairwise orthogonal idempotents summing to the unit. For this section algebra, their ranges are continuous subbundles \(F_1,\ldots,F_q\), and \(F\cong\bigoplus_{j=1}^qF_j\). Because the sphere is connected, each rank \(r_j\) is a positive constant, with \(\sum_jr_j=R\). Conversely, a splitting into \(q\) positive-rank bundles can be made orthogonal by a Hermitian metric, and assigning \(q\) distinct real scalars to the corresponding projections gives a self-adjoint section whose spectrum is exactly those \(q\) scalars. It follows that \(d_\sigma\) is exactly the largest number of nonzero subbundles in a direct-sum decomposition of \(F\).

**2. Sharp Chern obstruction.** Suppose \(c_k(E)\ne0\). By the Whitney-sum formula and the vanishing of all positive-degree cohomology below degree \(2k\),

\[
c_k(F)=m\,c_k(E)\ne0.
\]

If every summand \(F_j\) had rank less than \(k\), each would have zero \(k\)-th Chern class; again lower positive-degree Chern classes vanish on the sphere. The Whitney-sum formula would then give \(c_k(F)=0\), contradiction. Thus some \(r_j\ge k\), and since every other rank is at least one, \(q\le R-k+1\).

**3. Attaining the bound.** The clutching theorem identifies rank-\(s\) complex vector bundles on \(S^{2k}\) with \(\pi_{2k-1}(U(s))\) for \(s\ge1\). The fibration \(U(s)\to U(s+1)\to S^{2s+1}\) shows that \(\pi_{2k-1}(U(k))\to\pi_{2k-1}(U(R))\) is an isomorphism whenever \(R\ge k\): at each intermediate step, the homotopy of the quotient sphere vanishes in the two relevant degrees. Hence the clutching map of \(F\) is homotopic to the block inclusion of a clutching map into \(U(k)\). There exists a rank-\(k\) bundle \(G\) with

\[
F\cong G\oplus\underline{\mathbb C}^{\,R-k},\qquad c_k(G)=m c_k(E).
\]

This is a direct sum of exactly \(R-k+1\) nonzero bundles. Step 1 produces the required self-adjoint section, and Step 2 proves optimality.

**4. The zero-Chern case.** By Bott periodicity and the same stable-range inclusion, \(\pi_{2k-1}(U(r))\cong\mathbb Z\) for \(r\ge k\). On \(S^{2k}\), the map from the clutching integer to the top Chern number is multiplication by \(\pm(k-1)!\); in particular it is injective. Thus \(c_k(E)=0\) forces \(E\) to be trivial. Then \(F\) splits into \(R\) trivial lines, giving \(d_\sigma\ge R\), while no decomposition can have more than \(R\) nonzero summands. Hence \(d_\sigma=R\).

**5. Rigidity of every maximizer.** In the nonzero-Chern case, an element with exactly \(R-k+1\) spectral components has Riesz bundles \(F_j\) with some rank at least \(k\). Since \(\sum_j(r_j-1)=R-(R-k+1)=k-1\), there is exactly one rank-\(k\) summand and all others have rank one. For \(k\ge2\), \(H^2(S^{2k};\mathbb Z)=0\), so all line bundles are trivial. Whitney additivity gives \(c_k(G)=m c_k(E)\) for the remaining rank-\(k\) bundle, which is uniquely classified by this integer via clutching and Bott integrality. This proves the asserted rank profile and uniqueness up to vector-bundle isomorphism.

## Verification

The argument is infinite-dimensional only through the section algebra; all bundle fibers have finite rank. The upper bound uses the exact Whitney-sum identity and the absence of lower cohomology, not finite enumeration. The lower bound uses the explicitly stated stabilization range for unitary clutching groups. As checks on indices, for nontrivial rank-two bundles over \(S^4\), the depths at amplification levels \(m=1,2,3\) are \(1,3,5\); for nontrivial rank-three bundles over \(S^6\) they are \(1,4,7\). These checks illustrate, but do not prove, the general theorem. Every possible Riesz rank profile at the maximum is determined in Step 5.

## Relationship to prior work

Bračič and Kandić (2026, Proposition 3.1) proved the general equivalence between spectral components and orthogonal-idempotent decompositions. Their paper's finite-dimensional algebra computations are also prior. The new claim is the exact all-rank, all-amplification spectral depth for nontrivial section algebras over every even sphere and the compulsory Chern-bearing Riesz component. The bundle classification, stabilization range, and top Chern integrality are classical and are not claimed as original results. Dror Farjoun and Schochet (2011/2012) study homotopy and K-theory of Banach-algebra section spaces; their accessible abstract describes a different invariant. The independently studied odd-sphere torsion stabilization phenomenon is not used to infer this non-torsion, persistent even-sphere obstruction.

## Limitations

The result is restricted to ranks \(r\ge k\) over even spheres \(S^{2k}\), and makes no assertion about smaller-rank unstable torsion bundles, odd-dimensional spheres, other bases, the geometry of nonmaximal spectral strata, or norm estimates. It depends on standard topological theorems (clutching, Bott periodicity and top Chern integrality); these are cited rather than reproved. The inspected literature did not give this exact spectral-depth classification, but a differently formulated earlier bundle-splitting theorem could imply it; originality is therefore subject to ordinary bibliographic uncertainty. Independent validation has not been performed.

## References

1. J. Bračič and M. Kandić, *On operators with many spectral components*, arXiv:2611.12208v1 (first posted 9 November 2026), especially Proposition 3.1. https://arxiv.org/abs/2611.12208
2. J. Bračič and M. Kandić, *On operators with infinitely many spectral components*, arXiv:2611.14394v1 (10 November 2026), Section 3. https://arxiv.org/html/2611.14394v1
3. E. Dror Farjoun and C. L. Schochet, *Spaces of sections of Banach algebra bundles*, arXiv:1101.0444v3 (2012). https://arxiv.org/abs/1101.0444
4. A. Hatcher, *Vector Bundles & K-Theory*, Version 2.2 (2017), clutching and Bott periodicity. https://pi.math.cornell.edu/~hatcher/VBKT/VBpage.html
5. B. Cnossen, *Stable Homotopy Theory and Higher Algebra*, Section 9.1, vector-bundle clutching classification. https://bastiaancnossen.com/notes/stable-homotopy-higher-algebra/section/complex-k-theory/vector-bundles/index.html
