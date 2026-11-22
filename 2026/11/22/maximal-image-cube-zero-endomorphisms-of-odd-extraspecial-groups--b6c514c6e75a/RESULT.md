# Maximal-image cube-zero endomorphisms of odd extraspecial groups

## Finding

Let \(p\) be an odd prime, \(n\ge1\), and let \(G\) be the extraspecial group of exponent \(p\) and order \(p^{2n+1}\). Write \(0_G\) for the trivial endomorphism. The largest image of a nonautomorphism of \(G\) has order \(p^{n+1}\). Define \(M_{n,p}\) to count the endomorphisms \(f:G\to G\) satisfying \(f^3=0_G\) and \(|f(G)|=p^{n+1}\). Put

\[
L_n(p)=\prod_{j=1}^{n}(p^j+1),\qquad
Q_{n,s}(p)={n\brack s}_p{n-s\brack s}_p\prod_{j=0}^{s-1}(p^s-p^j),
\]

where \({a\brack b}_p\) denotes the Gaussian binomial coefficient and empty products equal one. Then

\[
\boxed{M_{n,p}=L_n(p)\sum_{s=0}^{\lfloor n/2\rfloor}
Q_{n,s}(p)\,p^{ns}
\left(\prod_{j=0}^{n-s-1}(p^n-p^j)\right)
(p^{2n-s}-p^n).}
\]

Each summand classifies the maps according to the rank \(s\) of the induced action restricted to the horizontal image. Every counted endomorphism has **nilpotency index exactly three**: \(f^2\ne0_G\) and \(f^3=0_G\). In contrast, any endomorphism satisfying \(f^2=0_G\) has image order at most \(p^n\). Thus index three is the **sharp first nilpotency index at which the maximal proper image size appears**. In the smallest examples, \(M_{1,3}=48\), \(M_{1,5}=480\), and \(M_{2,3}=552960\).

## Assumptions and scope

The exponent-\(p\) extraspecial group has a presentation in Baker–Campbell–Hausdorff coordinates as the set \(G=V\oplus\mathbb F_pz\), where \(V\) is a \(2n\)-dimensional symplectic space with nondegenerate alternating form \(\omega\), and
\[
(v,t)(w,u)=(v+w,t+u+\tfrac12\omega(v,w)).
\]
This is a group since \(p\) is odd. Here \(f^k\) is \(k\)-fold composition, \(0_G\) maps everything to the group identity, and \(|f(G)|\) denotes the cardinality of the image subgroup. The theorem excludes exponent-\(p^2\) extraspecial groups and characteristic two.

## Proof

**1. Singular endomorphism normal form.** The commutator subgroup is the center \(\mathbb F_pz\). Every homomorphism \(f\) has the form \(f(v,t)=(Av,\ell(v)+ct)\) with \(A\in\operatorname{End}(V)\), \(\ell\in V^*\), and \(c\in\mathbb F_p\), subject to \(\omega(Av,Aw)=c\omega(v,w)\). If \(c\ne0\), \(A\) is a symplectic similitude and \(f\) is invertible, so it cannot be composition-nilpotent. Hence \(c=0\), the subspace \(W=\operatorname{im}A\) is isotropic, and all \(\ell\) are permitted. The image subgroup is elementary abelian of order \(p^{\operatorname{rank}(A,\ell)}\), using the rank of the linear map \(v\mapsto(Av,\ell(v))\). The isotropic bound gives \(\operatorname{rank}(A,\ell)\le n+1\). An automorphism has full image, and this bound applies to every nonautomorphism.

**2. Reduce maximal-rank cube nilpotence to a square-zero restriction.** To have \(|f(G)|=p^{n+1}\), necessarily \(\dim W=n\), so \(W\) is Lagrangian, and \(\ell\) does not annihilate \(\ker A\). There are \(L_n(p)=\prod_{j=1}^n(p^j+1)\) Lagrangians in \(V\). For a fixed \(W\), put \(B=A|_W:W\to W\). Because \(A(V)=W\), the conditions \(A^3=0\) and \(B^2=0\) are equivalent: \(A^3=B^2A\). Also \(A^2(V)=B(W)\). On group coordinates, \(f^3(v,t)=(A^3v,\ell(A^2v))\), so \(f^3=0_G\) is equivalent to \(B^2=0\) and \(\ell(B(W))=0\).

**3. Count the possible restrictions.** If \(B^2=0\) and \(s=\operatorname{rank}B\), then \(0\le s\le\lfloor n/2\rfloor\). Choose \(U=\operatorname{im}B\) (\({n\brack s}_p\) choices) and \(K=\ker B\), with \(U\subseteq K\) and \(\dim K=n-s\) (\({n-s\brack s}_p\) choices). The induced map \(W/K\xrightarrow{\sim}U\) is arbitrary invertible (\(\prod_{j=0}^{s-1}(p^s-p^j)\) choices). This gives exactly \(Q_{n,s}(p)\) restrictions \(B\).

**4. Extend to a surjective horizontal endomorphism.** Fix \(W\) and \(B\) of rank \(s\). To extend \(B\) to an operator \(A:V\to W\) with image \(W\), its action on any complementary \(n\)-space to \(W\), modulo \(U=B(W)\), must surject onto \(W/U\), a space of dimension \(n-s\). There are \(\prod_{j=0}^{n-s-1}(p^n-p^j)\) such surjections, and each has \(p^{ns}\) lifts to \(W\). The count is independent of the chosen complement.

**5. Count the central functionals.** The remaining condition \(\ell A^2=0\) is exactly \(\ell|_U=0\), giving \(p^{2n-s}\) functionals. Among these, those annihilating \(\ker A\), of dimension \(n\), number \(p^n\), since \(U\subseteq\ker A\). The remaining \(p^{2n-s}-p^n\) functionals make \((A,\ell)\) have rank \(n+1\). Multiplying Steps 2–5 and summing \(s\) yields the claimed formula without overcounting.

**6. Sharp nilpotency-index boundary.** If \(f^2=0_G\), the image is elementary abelian and is contained in the kernel; in the \((2n+1)\)-dimensional BCH coordinates this implies \(\operatorname{rank}f\le\lfloor(2n+1)/2\rfloor=n\). Thus the image order is at most \(p^n\). Conversely the \(s=0\) summand in the formula is strictly positive, as it includes Lagrangian \(W\), square-zero \(A\) of rank \(n\), and an \(\ell\) not annihilating \(W=\ker A\). These maps have image order \(p^{n+1}\) and cube zero. Their square is nonzero by the rank bound, so their composition-nilpotency index is exactly three.

## Verification

The dependency-free program `artifacts/verify_cube.py` independently enumerates entire quotient linear matrices and central functionals; it tests the isotropy equation, cube nilpotence and image rank directly rather than using the Lagrangian-extension formula. It gives \(48\) and \(480\) in cases \((n,p)=(1,3)\) and \((1,5)\), respectively. It also checks the polynomial identity by exhaustive finite matrix enumeration for \((n,q)=(2,2)\), obtaining \(3240\) on the corresponding characteristic-two **Lie-algebra** model, not claiming this is a group instance. The general odd-prime theorem follows from Steps 1–6; these tests are finite corroboration, not an infinite proof. Arithmetic reconstructions give \(M_{2,3}=552960\) and larger examples.

## Relationship to prior work

Anil Kumar and Pradhan (2019), Theorem \(\Omega\), supply the symplectic-similitude normal form and total endomorphism counts for the same extraspecial groups. Their Theorem 5.2 counts isotropic subspaces, used as an established ingredient. They do not give the maximal-image cube-zero distribution or the index-three threshold. A published note titled *Rank distribution of square-zero weight-one Rota–Baxter operators on finite Heisenberg Lie algebras* counts all square-zero operators via the isotropic-image normal form. For singular Heisenberg endomorphisms, the analogous weight-one Rota–Baxter square-zero normal form yields equivalent square-zero counts, **so no novelty is claimed for any square-zero marginal**. The present cube-zero condition instead allows nonzero second iterates and requires a new enumeration of square-zero restrictions on a Lagrangian image and their surjective extensions. Existing full-rank statistics for all Heisenberg Lie endomorphisms do not isolate composition index three. The 2019 paper and the full text of the square-zero note were read for this comparison.

## Limitations

The count concerns only the top proper image size and index exactly three; it does not enumerate all cube-zero maps at smaller image orders or general nilpotency indices. The formula is for odd prime fields and exponent-\(p\) extraspecial groups; extension fields require distinct group-family conventions. Unindexed equivalent enumerations of nilpotent endomorphisms and specialized consequences of general nilpotent-matrix theory remain possible historical-priority risks. The self-review is not an independent audit.

## References

1. C. P. Anil Kumar and S. S. Pradhan, *On the Endomorphism Semigroups of Extra-special \(p\)-groups and Automorphism Orbits*, arXiv:1908.00331v1, first public August 1, 2019; *International Journal of Group Theory* 11 (2022), 201–220, DOI 10.22108/IJGT.2021.129815.1708. https://arxiv.org/abs/1908.00331
2. *Rank distribution of square-zero weight-one Rota–Baxter operators on finite Heisenberg Lie algebras*, 2026 public note, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-rank-distribution-of-square-zero-weight-one-rota-baxter-operator--7993ea6e7a2b.
3. *Rank gaps and asymptotic concentration among Heisenberg Lie endomorphisms over finite fields*, 2026 public note, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-rank-gaps-and-asymptotic-concentration-among-heisenberg-lie-endo--b85cf894e197.
