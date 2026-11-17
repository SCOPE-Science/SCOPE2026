# Symplectic kernel-rank orbits of idempotent pre-endomorphisms of block-Heisenberg algebras

## Finding
Let \(k=\mathbb F_q\) for any prime power \(q\), and let \(m\ge1\). The associative nonunital algebra \(A_m\) consists of strictly upper-triangular \((1,m,1)\)-block matrices. In coordinates \((u,v,z)\), for \(u\in k^{1\times m}\), \(v\in k^{m\times1}\), \(z\in k\), multiplication is
\[
(u,v,z)(u',v',z')=(0,0,uv').
\]
A pre-endomorphism is a \(k\)-linear map \(F\) satisfying \(F(ab-ba)=F(a)F(b)-F(b)F(a)\) for every pair \(a,b\). An invertible pre-endomorphism is called a pre-automorphism, and conjugation means \(F\mapsto TFT^{-1}\) for such \(T\), not necessarily an associative automorphism.

Write \(V=k^{2m}\), choose its standard nondegenerate alternating form \(\omega\) defined by the commutator, and let \(z\) denote the central basis element. Every idempotent pre-endomorphism \(F^2=F\) is either the identity or has the unique form
\[
F(v+tz)=Pv+h(v)z,\qquad P^2=P,\quad h=h\circ P,
\]
where \(W=\operatorname{im}P\) is totally isotropic for \(\omega\). For the nonidentity cases let \(r=\dim W\), and define \(s\) by
\[
\operatorname{rank}(\omega|_{\ker P})=2(m-r+s).
\]
Then \(0\le r\le m\) and \(0\le s\le\lfloor r/2\rfloor\). Two nonidentity maps are conjugate under pre-automorphisms **if and only if** their pairs \((r,s)\) coincide. Thus the number of orbits is
\[
2+\sum_{r=1}^{m}(\lfloor r/2\rfloor+1),
\]
including zero and identity.

For each \((r,s)\), the exact orbit size is
\[
M_{m,r,s}(q)=I_{m,r}(q)\,q^{r+2r(m-r)+r(r+1)/2}\,A_{r,s}(q),
\]
where
\[
I_{m,r}(q)=\prod_{i=0}^{r-1}\frac{q^{2m-i}-q^i}{q^r-q^i},\qquad
A_{r,s}(q)={r\brack 2s}_q\frac{|\mathrm{GL}_{2s}(k)|}{|\mathrm{Sp}_{2s}(k)|}.
\]
Here \({r\brack d}_q\) is the Gaussian binomial coefficient and \(A_{r,s}\) counts alternating bilinear forms of rank \(2s\) on an \(r\)-dimensional space. For \(s=0\), \(A_{r,0}=1\), and for empty products use one. The rank-zero and full-rank identity orbits are singletons.

The first split of a fixed operator rank occurs at \(m=2\): in five dimensions there are five orbits, of sizes \(1,240,480,480,1\) over \(\mathbb F_2\), ordered by zero, rank one, the two rank-two types, and identity. In those rank-two cases the Lie kernel is respectively abelian (\(s=0\)) or nonabelian (\(s=1\)). Over \(\mathbb F_3\) the sizes are \(1,3240,9720,19440,1\).

## Assumptions and scope
The field is arbitrary finite \(\mathbb F_q\), including characteristic two. All endomorphisms, products, brackets and conjugations are \(k\)-linear. The group acting is the **pre-automorphism group**, which agrees with the automorphism group of the associated Heisenberg Lie algebra; this is not the potentially smaller associative automorphism group. The operator rank used to label the orbit is its rank as a linear map. The invariant \(s\) measures the remaining symplectic rank on its kernel modulo its central line.

## Proof
**1. Structural normal form.** The Lie algebra on \(A_m\) has basis \(V\oplus kz\), bracket \([v+az,w+bz]=\omega(v,w)z\), and one-dimensional derived ideal \(kz\). Since \(F\) is a Lie endomorphism, \(F(z)=\lambda z\), and idempotence forces \(\lambda\in\{0,1\}\). If \(\lambda=1\), bracket preservation implies the induced endomorphism \(P\) of \(V\) satisfies \(\omega(Pv,Pw)=\omega(v,w)\); it is invertible. Thus \(F\) is invertible, and \(F^2=F\) gives \(F=\mathrm{id}\). For all other cases \(F(z)=0\). Write \(F(v)=Pv+h(v)z\). Bracket preservation gives \(\omega(Pv,Pw)=0\), hence \(W=\operatorname{im}P\) is isotropic, and idempotence is exactly \(P^2=P\), \(hP=h\). Conversely every such pair defines an idempotent pre-endomorphism. In particular \(r=\dim W\le m\), and \(h\) is an arbitrary linear functional on \(W\), yielding \(q^r\) lifts for fixed \(P\).

**2. Complete geometric invariant.** Let \(K=\ker P\), so \(V=W\oplus K\). Because \(W\subseteq W^\perp\), the intersection \(K_0=K\cap W^\perp\) is a complement of \(W\) inside \(W^\perp\) and has dimension \(2(m-r)\). The form on \(K_0\) is nondegenerate: the radical of \(\omega|_{W^\perp}\) is exactly \(W\). Inside \(K\), take the orthogonal complement \(K_1=K_0^\perp\cap K\). Then \(K=K_0\perp K_1\) and \(\dim K_1=r\). The pairing of \(W\) with \(K_1\) is perfect, while the alternating form on \(K_1\) has even rank \(2s\) for a unique \(s\in\{0,\ldots,\lfloor r/2\rfloor\}\). Consequently \(\operatorname{rank}(\omega|_K)=2(m-r+s)\). These integers are invariant under every symplectic similitude.

Conversely, given two decompositions \(V=W\oplus K\) with identical \((r,s)\), choose symplectic bases of their respective \(K_0\) spaces, and choose bases of \(W\) and dual bases of \(K_1\) for their perfect pairings. The residual alternating forms on \(K_1\) are congruent because alternating forms over **every field**, including characteristic two, are classified by their even rank. Carrying one chosen basis system to the other preserves the full pairing matrix; this produces an element of \(\mathrm{Sp}(V,\omega)\) carrying both \(W\) and \(K\) to their counterparts. Thus \(P\) is conjugate precisely by \((r,s)\). Lie automorphisms additionally permit central shears \(T(v)=v+\phi(v)z\), \(T(z)=z\): conjugation sends \(h\) to \(h+\phi|_W\circ P\). These act transitively on the \(q^r\) choices of \(h\), so the stated criterion classifies the full \(F\), not merely \(P\).

**3. Exact orbit size.** The number of isotropic \(r\)-spaces \(W\) is
\[
I_{m,r}(q)=\prod_{i=0}^{r-1}\frac{q^{2m-i}-q^i}{q^r-q^i}.
\]
Fix \(W\) and a symplectic Witt decomposition \(V=W\oplus X\oplus W^*\), where \(X\) is nondegenerate of dimension \(2(m-r)\). Every complement \(K\) of \(W\) is uniquely the graph of a map \(X\oplus W^*\to W\), with components \(A:X\to W\) and \(B:W^*\to W\). The restriction of \(\omega\) to \(K\) has a nondegenerate \(2(m-r)\)-dimensional block. After eliminating that block, its residual matrix on the remaining \(r\) coordinates is
\[
C=B-B^{\mathsf T}+C_A,
\]
where \(C_A\) is an alternating matrix determined by \(A\); signs depend on basis conventions but do not affect the count. The map \(B\mapsto B-B^{\mathsf T}\) is surjective onto all alternating \(r\)-matrices, including in characteristic two, and every fiber has \(q^{r(r+1)/2}\) elements. There are \(q^{2r(m-r)}\) choices of \(A\), and exactly
\[
A_{r,s}(q)={r\brack 2s}_q\frac{|\mathrm{GL}_{2s}(k)|}{|\mathrm{Sp}_{2s}(k)|}
\]
alternating \(r\)-matrices of rank \(2s\): choose the radical of codimension \(2s\) and then a nondegenerate alternating form on the quotient. Multiplying these independent factors, the isotropic-image count, and the \(q^r\) central lifts gives the asserted \(M_{m,r,s}(q)\). All \((r,s)\) occur, and the orbit transitivity from step 2 shows the counts equal orbit sizes.

## Verification
The included `verify_retractions.py` exhaustively enumerates binary projections on \(V\) in dimensions two and four, tests \(P^2=P\), isotropy and rank of the alternating form on \(\ker P\), and compares the resulting counts (including central lifts) with the theorem. Its five-dimensional binary count is \(1,240,480,480,1\). The independent `verify_orbits.py` computes symplectic conjugacy orbits of all 361 qualifying projections on the four-dimensional binary quotient, using symplectic transvections; these are four orbits of projection counts \(1,120,120,120\). It also exhausts all \(3^9\) linear maps of the three-dimensional ternary Heisenberg Lie algebra and tests the original two operator identities directly, obtaining ranks \(0,1,3\) with counts \(1,36,1\). Both programs terminate with `VERIFY_OK`. These finite checks do not substitute for the universal symplectic proof.

## Relationship to prior work
Ebrahim and Facchini, *Idempotent Pre-Endomorphisms of Algebras* (arXiv:2304.05079v1, April 11, 2023), Theorem 6.1, establishes the general correspondence between idempotent pre-endomorphisms and compatible complementary pre-ideals/pre-subalgebras. The present result specializes that framework and supplies the new all-field **pre-automorphism orbit invariant**, transitivity proof and exact orbit cardinalities. The general correspondence is not claimed new. Cerqua and Facchini (arXiv:2301.02627v1) provide related conceptual foundations. Anil Kumar and Pradhan (arXiv:1908.00331) analyze extra-special \(p\)-groups and automorphism orbits of **group elements**, rather than conjugation classes of idempotent operators over all finite fields. Earlier counts of Heisenberg idempotent maps by ordinary linear rank are likewise not claimed here; those marginal counts do not determine the symplectic-kernel refinement and its orbit sizes. Chandler, Sin and Xiang (arXiv:0801.4392v1) study symplectic incidence modules and orthogonal complements, not this direct-sum complement orbit problem.

## Limitations
The theorem is for the block-Heisenberg family and for pre-endomorphisms modulo **pre-automorphism** conjugation, not for ordinary associative endomorphism conjugacy. The orbital classification is finite-field uniform, but no assertion is made about arbitrary non-field coefficient rings or unrelated nilpotent algebras. Earlier rank-only counts and the general ideal/complement correspondence are prior work. A specialized unpublished symplectic-pair orbit classification could potentially imply the present statement; publication priority and independent review remain open. No independent mathematical audit has been performed.

## References
Ebrahim, F. A., and Facchini, A., *Idempotent Pre-Endomorphisms of Algebras*, arXiv:2304.05079v1 (2023-04-11), especially §6, Theorem 6.1.

Cerqua, M., and Facchini, A., *Pre-Lie algebras, their multiplicative lattice, idempotent endomorphisms*, arXiv:2301.02627v1 (2023-01-06).

Anil Kumar, C. P., and Pradhan, S. S., *On endomorphism semigroups of extra-special p-groups and automorphism orbits*, arXiv:1908.00331 (2019).

Chandler, D. B., Sin, P., and Xiang, Q., *Incidence Modules for Symplectic Spaces in Characteristic Two*, arXiv:0801.4392v1 (2008).
