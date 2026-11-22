# Symplectic rank gaps and conjugacy rigidity of Heisenberg averaging projections

## Finding
Let \(k\) be any field and \(m\ge2\). On the \((2m+1)\)-dimensional Heisenberg Lie algebra \(H_m=V\oplus kz\), with \(\dim V=2m\) and nondegenerate alternating form \(\omega\), set \([u+az,v+bz]=\omega(u,v)z\). An **averaging projection** is a \(k\)-linear operator \(P:H_m\to H_m\) with
\[
P^2=P,\qquad [Px,Py]=P([Px,y])=P([x,Py])\quad(x,y\in H_m).
\]
Every averaging projection has \(P(z)=cz\) with \(c\in\{0,1\}\) and \(P(v)=Av+f(v)z\). Exactly the following two mutually exclusive branches occur.

**Branch \(c=0\) (the established Lie-retraction branch).** The operator \(A\) is a projection onto a totally isotropic subspace \(U\subseteq V\), and \(f=f\circ A\). Conversely any such data work. These operators are precisely the proper idempotent Lie endomorphisms; their linear rank is \(r=\dim U\), with \(0\le r\le m\). This branch, including its rank enumeration below, is established in the earlier Heisenberg retraction classification [4] and is **not claimed as new**.

**Branch \(c=1\) (the complementary nonendomorphism branch).** The operator \(A\) is the projection onto a **nondegenerate symplectic subspace** \(U\subseteq V\) along its orthogonal complement \(U^\perp\). Thus \(\dim U=2r\) for a unique \(0\le r\le m\); moreover \(f=f\circ(I-A)\), so \(f\) is arbitrary on \(U^\perp\) and zero on \(U\). Conversely all such data define averaging projections, of linear rank \(2r+1\). Only the case \(r=m\), namely the identity, is a Lie endomorphism. For each fixed \(r\), these operators form exactly **one orbit** under the automorphism group of \(H_m\), over every field.

Over any finite field \(k=\mathbb F_q\), including characteristic two, put
\[
I_{m,r}(q)={m\brack r}_q\prod_{i=0}^{r-1}(q^{m-i}+1),\qquad
S_j(q)=q^{j^2}\prod_{i=1}^j(q^{2i}-1),\quad S_0(q)=1.
\]
The exact rank polynomial for **all** labeled averaging projections is
\[
\boxed{\mathcal A_{m,q}(T)=\sum_{r=0}^{m}I_{m,r}(q)q^{r(2m-r+1)}T^r
+\sum_{r=0}^{m}\frac{S_m(q)}{S_r(q)S_{m-r}(q)}q^{2(m-r)}T^{2r+1}.}
\]
The first sum records known retractions [4]; the **second sum and the full averaging classification** supply the new distinction. The possible ranks are exactly
\[
\boxed{\{0,1,\ldots,m\}\cup\{1,3,5,\ldots,2m+1\}.}
\]
Every even rank strictly above \(m\) is impossible. For \(m\ge2\) there are precisely \(m\) non-Lie-endomorphism automorphism orbits, in ranks \(1,3,\ldots,2m-1\). Each has exactly one conjugacy class; its labeled size is the corresponding coefficient from the second sum.

For illustration, when \((m,q)=(2,2)\), the rank profile in ranks \(0\) through \(5\) is \((1,256,960,80,0,1)\). Of these \(1298\) operators, exactly \(96\) are not Lie endomorphisms. The two rank-one mechanisms are different: isotropic-image retractions and the scalar-center branch \(P(z)=z\) with \(P(V)\subset kz\).

As a geometric refinement, the **reduced** averaging-projection variety over any algebraically closed field has exactly \(2m+2\) smooth irreducible (hence connected) components, indexed by \(c\in\{0,1\}\) and the indicated rank of \(A\). On \(c=0\), each component is an affine-space bundle over the symplectic isotropic Grassmannian; on \(c=1\), each is a vector bundle over the open Grassmannian of nondegenerate symplectic \(2r\)-subspaces. This is a statement about the reduced locus; no claim of reducedness of the defining equation scheme is made.

## Assumptions and scope
The field is arbitrary, with no characteristic restriction; \(\omega\) is alternating and nondegenerate also in characteristic two. The parameter \(m\ge2\) is part of the theorem's new contribution. The \(m=1\) boundary is covered by previously available three-dimensional embedding-tensor theory and serves only as a verification check. The rank polynomial is for distinct labeled operators, not conjugacy classes. The second branch is not a classification of arbitrary averaging operators without idempotence, nor of idempotent Rota–Baxter maps of nonzero weight.

## Proof
**1. Elimination of a noncentral image of the center.** Write an arbitrary linear map as \(P(z)=b+cz\) and \(P(v)=Av+f(v)z\), where \(b\in V\). In the averaging identity with \(x=z\), \(y=v\), the noncentral coordinate of \(P([Pz,v])\) equals \(\omega(b,v)b\), while \([Pz,Pv]\) is central. Thus \(\omega(b,v)b=0\) for every \(v\). Nondegeneracy forces \(b=0\). This deduction holds before assuming idempotence.

**2. Matrix equations.** With \(P(z)=cz\), direct substitution of all pairs from \(V\oplus kz\) into the original identities gives precisely
\[
A^2=A,\quad c^2=c,\quad fA+cf=f,\quad
\omega(Au,Av)=c\omega(Au,v)=c\omega(u,Av)\quad(\forall u,v\in V).
\]
The first three equations express idempotence. The last two equalities are necessary and sufficient for *both* averaging identities: their left sides are central, and \(P\) acts on the center by \(c\). Since \(k\) is a field, \(c=0\) or \(c=1\).

**3. Isotropic/retraction branch.** For \(c=0\), the form equations say \(\omega(Au,Av)=0\); this is equivalent to total isotropy of \(U=\operatorname{im}A\). The equation for \(f\) becomes \(fA=f\). Thus a projection \(A\) with image \(U\), any complementary kernel and any \(f\in U^*\) (extended through \(A\)) give all maps in this branch. Since \(P(z)=0\) and \(\omega(Au,Av)=0\), \(P([u,v])=[Pu,Pv]=0\), so these are Lie endomorphisms. Conversely any proper idempotent Lie endomorphism must be of this type, as a center-preserving endomorphism with \(c=1\) is an invertible symplectic similitude and idempotence forces identity [4].

**4. Symplectic branch.** For \(c=1\), idempotence says \(fA=0\). Let \(U=\operatorname{im}A\) and \(K=\ker A\), so \(V=U\oplus K\). Taking \(u\in U\), \(v\in K\), the equality \(\omega(Au,v)=\omega(u,Av)\) yields \(\omega(u,v)=0\). Thus \(K\subset U^\perp\); equality follows from dimension, and \(U\cap U^\perp=0\) makes \(U\) nondegenerate. A nondegenerate alternating space has even dimension \(2r\). Conversely the orthogonal projection for any such decomposition satisfies both \(\omega(Au,Av)=\omega(Au,v)\) and \(\omega(Au,Av)=\omega(u,Av)\). The equation \(fA=0\) allows exactly the arbitrary linear functionals on \(K=U^\perp\). The image contains \(z\) and \(U\), hence rank \(2r+1\).

If such a map is a Lie homomorphism, then \(\omega(Au,Av)=\omega(u,v)\) for all pairs, so \(A\) is invertible by nondegeneracy and must be identity by idempotence. Then \(fA=0\) gives \(f=0\). Hence the unique Lie endomorphism in \(c=1\) is the identity.

**5. Orbit rigidity.** All nondegenerate symplectic \(2r\)-subspaces of \(V\) are conjugate under the symplectic group: choose symplectic bases of them and their orthogonal complements. Every Heisenberg automorphism has form \(G(v+tz)=Sv+(\eta(v)+dt)z\), with \(S\) a symplectic similitude of multiplier \(d\ne0\) and \(\eta\in V^*\). Conjugation sends \((A,f)\) in \(c=1\) to \((SAS^{-1},\, [d f+\eta(A-I)]S^{-1})\). After taking \(S\) to a standard symplectic decomposition, the free shear \(\eta\) kills every functional on the kernel. Thus the sole conjugacy invariant in this branch is \(r\). In particular the action is transitive on every fixed-\(r\) family, even in characteristic two.

**6. Exact counts.** For \(c=0\), choose a totally isotropic \(r\)-space in \(I_{m,r}(q)\) ways, its complement in \(q^{r(2m-r)}\) ways, and a functional \(f\) on \(U\) in \(q^r\) ways. This is exactly the established coefficient \(I_{m,r}(q)q^{r(2m-r+1)}\) [4]. For \(c=1\), the symplectic group acts transitively on nondegenerate \(2r\)-spaces, with stabilizer \(\operatorname{Sp}_{2r}(q)\times\operatorname{Sp}_{2(m-r)}(q)\). Their number is \(S_m(q)/(S_r(q)S_{m-r}(q))\); the functional on the \(2(m-r)\)-dimensional orthogonal complement has \(q^{2(m-r)}\) choices. These count every operator exactly once, including both endpoint ranks. This proves the polynomial and forbidden ranks.

**7. Reduced component geometry.** Since \(c^2=c\), the value \(c\) splits the equation locus into clopen pieces. In any algebraic family of idempotent matrices, rank of \(A\) is locally constant (the image is a direct summand), so each rank sublocus is also clopen. For \(c=0\), the parameter space over \(\operatorname{IGr}(r,V)\) consists of the affine bundle of complements plus a rank-\(r\) functional bundle, smooth and geometrically irreducible. For \(c=1\), the base of nondegenerate \(2r\)-spaces is a nonempty open subvariety of the ordinary Grassmannian and is smooth geometrically irreducible; the attached choice \(f\in (U^\perp)^*\) is a vector bundle. All rank types occur. Thus these \(2(m+1)\) smooth irreducible clopen strata are precisely the components of the reduced solution variety. The proof does not assume the original polynomial ideal is radical.

## Verification
The standalone `checks/verify.py` uses the Python standard library. In dimension three it exhaustively checks *every* \(3\times3\) matrix over \(\mathbb F_2\) and \(\mathbb F_3\) against \(P^2=P\) and both **original** basis-pair averaging identities, producing profiles \((1,16,0,1)\) and \((1,45,0,1)\) for ranks zero through three. These low-dimensional cases are known boundary checks, not part of the new priority claim. For the five-dimensional algebra over \(\mathbb F_2\), it enumerates all \(2^{16}\) quotient matrices, applies the exact necessary conditions to select candidates, then checks every selected central row, both values of \(c\), idempotence and all original basis-pair identities; the resulting full rank profile is \((1,256,960,80,0,1)\). Formula sanity checks also run for field orders \(2,3,5,9\) and \(1\le m\le4\), but these last arithmetic substitutions are not finite-field enumerations over nonprime fields. A successful replay prints `HEISENBERG_AVERAGING_PROJECTIONS_VERIFIED`. The infinite-dimensional parameter range and arbitrary-field assertion follow from the symbolic proof, not finite testing.

## Relationship to prior work
Laraiedh and Silvestrov [1, Proposition 2.24] establish the **general** image-subalgebra/kernel-invariance criterion for idempotent averaging operators; that general criterion is background, not a new claim. Das and Sen [2] and Das [3] develop averaging Lie/Leibniz algebra structures and deformation frameworks. Their inspected full texts do not provide the present full symplectic \(m\ge2\) operator classification or finite-field census.

The prior *Heisenberg Lie retractions: isotropic affine strata and a rank-dominance transition* [4] already proves exactly the entire \(c=0\) branch, with the first Gaussian product term. The independent Heisenberg pre-endomorphism orbit classification [5] likewise refines only Lie endomorphisms. The published Heisenberg splitting Rota–Baxter census [6] counts projections with **both** image and kernel Lie subalgebras; for our \(c=1\) maps with \(r<m\), the kernel projects to the nondegenerate symplectic subspace \(U^\perp\), so its bracket is \(kz\), not contained in the kernel: these averaging projections are not splitting Rota–Baxter maps. The scalar-affine averaging rigidity classification [7] concerns a different Lie algebra, and includes the **known three-dimensional** rank-one Heisenberg counterexample. The three-dimensional Hom-Heisenberg adjoint embedding-tensor classification [8] includes the \(m=1\) boundary, which is excluded from the contribution's novelty claim. None of these published statements implies the newly counted \(m\ge2\), \(c=1\), \(r<m\) stratum. This implication comparison is stronger than a title search, but independent publication priority remains unestablished.

## Limitations
The theorem covers idempotent two-sided averaging projections only, not non-idempotent averaging operators, general embedding tensors, or arbitrary two-step nilpotent Lie algebras. The known retraction branch and all three-dimensional boundary cases are explicitly credited. The finite-field counts are labeled counts, and only the new symplectic branch is shown to have a single conjugacy orbit for each parameter. The geometric component statement concerns the **reduced** solution variety; the original equation scheme may possess nilpotent structure. The computer tests check small prime fields and arithmetic substitutions, not the unbounded theorem. A different published classification under embedding-tensor or module-theoretic terminology could conceivably subsume the new branch; no independent mathematical audit or absolute priority guarantee is claimed.

## References
1. I. Laraiedh and S. Silvestrov, *Averaging operators on q-deformed Witt and q-deformed W(2,2) algebras*, arXiv:2304.00662v1, first public 2023-04-03, especially Proposition 2.24, https://arxiv.org/abs/2304.00662.
2. A. Das and S. Sen, *2-term averaging L∞-algebras and non-abelian extensions of averaging Lie algebras*, arXiv:2308.16668v1, first public 2023-08-31, https://arxiv.org/abs/2308.16668.
3. A. Das, *Averaging operators on groups, racks and Leibniz algebras*, arXiv:2403.06250v1, first public 2024-03-10, https://arxiv.org/abs/2403.06250.
4. *Heisenberg Lie retractions: isotropic affine strata and a rank-dominance transition*, public result and proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-heisenberg-lie-retractions-isotropic-affine-strata-and-a-rank-do--9cf8810a2ae3.
5. *Symplectic kernel-rank orbits of idempotent pre-endomorphisms of block-Heisenberg algebras*, public result and proof, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-symplectic-kernel-rank-orbits-of-idempotent-pre-endomorphisms-of--635464fc5891.
6. *Exact rank and five-phase fluctuation laws for splitting Rota–Baxter projections on finite Heisenberg Lie algebras*, public result and proof, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-rank-and-five-phase-fluctuation-laws-for-splitting-rota-ba--06bda9cc87c0.
7. *Averaging-projection rigidity and a two-parity rank law for scalar-affine Lie algebras*, public result and proof, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-averaging-projection-rigidity-and-a-two-parity-rank-law-for-scal--bad197a33435.
8. *Adjoint embedding tensors on a one-parameter Hom-Heisenberg family*, public result and proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-adjoint-embedding-tensors-on-a-one-parameter-hom-heisenberg-fami--13ec4156c37a.
