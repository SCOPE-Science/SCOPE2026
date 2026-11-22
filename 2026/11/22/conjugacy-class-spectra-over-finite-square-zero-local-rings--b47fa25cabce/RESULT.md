# Conjugacy-class spectra over finite square-zero local rings

## Finding
Let \(R\) be a finite commutative local ring with identity, maximal ideal \(\mathfrak m\ne0\) satisfying \(\mathfrak m^2=0\), residue field \(k=R/\mathfrak m\cong\mathbb F_q\), and \(d=\dim_k\mathfrak m\ge1\). Write \(G=\operatorname{GL}_2(R)\) and \(U=|\operatorname{GL}_2(k)|=q(q-1)^2(q+1)\). The number \(K(G)\) of conjugacy classes is
\[
K(G)=(q^2-1)q^{2d}+\frac{q^{4d}-q^{2d}}{q(q+1)}.
\]
In fact, the following eight-row table is an **exact centralizer-order census**: in each row, the number of elements of \(G\) is given in the second column and their common centralizer order in the third. Rows with coincident centralizer orders are to be added, and zero-population rows omitted.

Put
\[
\begin{aligned}
c_s&=(q-1)^2,&c_i&=q^2-1,&c_j&=q(q-1),\\
N_s&=\tfrac12 q(q+1),&N_i&=\tfrac12 q(q-1),&N_j&=q+1,\\
M_s&=\tfrac12(q-1)(q-2)U/c_s,&
M_i&=\tfrac12 q(q-1)U/c_i,&M_j&=(q-1)U/c_j,\\
D&=q^{4d}-(q^2+q+1)q^{2d}+(q^2+q)q^d.
\end{aligned}
\]
The subscripts \(s,i,j\) denote split semisimple, irreducible quadratic, and nontrivial Jordan types over \(k\), respectively.

| Reduction/radical type | Number of elements | Centralizer order |
|---|---:|---:|
| Scalar reduction, scalar radical | \((q-1)q^d\) | \(Uq^{4d}\) |
| Scalar reduction, split quadratic radical | \((q-1)N_s(q^{2d}-q^d)\) | \(c_sq^{4d}\) |
| Scalar reduction, field quadratic radical | \((q-1)N_i(q^{2d}-q^d)\) | \(c_iq^{4d}\) |
| Scalar reduction, Jordan quadratic radical | \((q-1)N_j(q^{2d}-q^d)\) | \(c_jq^{4d}\) |
| Scalar reduction, noncommuting radical coefficients | \((q-1)D\) | \((q-1)q^{4d}\) |
| Nonscalar split reduction | \(M_sq^{4d}\) | \(c_sq^{2d}\) |
| Nonscalar irreducible reduction | \(M_iq^{4d}\) | \(c_iq^{2d}\) |
| Nonscalar Jordan reduction | \(M_jq^{4d}\) | \(c_jq^{2d}\) |

The exceptional noncommuting-radical row is empty exactly when \(d=1\), and otherwise gives precisely \(D/[q(q+1)]\) conjugacy classes, each of size \(q(q^2-1)\). In particular, for fixed \(q\), as \(d\to\infty\), its share of **all conjugacy classes** tends to \(1\). The exact number of remaining classes is \(q^{2d+2}-q^d\).

Equivalently, the number of ordered commuting pairs in \(G\) is
\[
|G|K(G)=U(q^2-1)q^{6d}+(q-1)^2(q^{8d}-q^{6d}),
\qquad |G|=Uq^{4d}.
\]
These formulas are independent of the multiplication structure of \(R\), including whether its characteristic is the square of a prime or the residue characteristic. They recover \(K(G)=q^4-q\) in the principal length-two case \(d=1\).

## Assumptions and scope
The ring is **commutative, finite, unital and local**; the radical is nonzero and square-zero. The vector-space structure on \(\mathfrak m\) over \(k\) is canonical because \(\mathfrak m^2=0\). All prime powers \(q\ge2\), all integers \(d\ge1\), and all such rings are included, without a coefficient-field or splitting assumption. The census concerns elements of the finite group \(\operatorname{GL}_2(R)\) under conjugation, not all singular matrices in \(M_2(R)\), not matrices of larger degree, and not arbitrary higher-nilpotency local rings.

A choice of \(k\)-basis of \(\mathfrak m\) identifies a matrix with scalar reduction with a \(d\)-tuple of matrices over \(k\). Whether these coefficient matrices commute pairwise, and the isomorphism type of their common centralizer, is invariant under a basis change and under adding scalar matrices to the coefficients.

## Proof
**1. Reduction and lift fibers.** Reduction gives a surjective group homomorphism \(G\to G_0=\operatorname{GL}_2(k)\) with kernel \(I_2+M_2(\mathfrak m)\), of cardinality \(q^{4d}\). If \(g_0\in G_0\) is nonscalar, it is a cyclic \(2\times2\) matrix. Therefore \(C_{M_2(k)}(g_0)=kI_2+kg_0\) has dimension two and \(C_{G_0}(g_0)\) is its unit group. Given any lift \(g\) of \(g_0\) and any \(h_0=\alpha I_2+\beta g_0\in C_{G_0}(g_0)\), choose arbitrary lifts \(\widetilde\alpha,\widetilde\beta\in R\). Then \(\widetilde\alpha I_2+\widetilde\beta g\) is an invertible commuting lift of \(h_0\). Any other commuting lift differs by \(T\in M_2(\mathfrak m)\) satisfying \([g,T]=0\). Since \(\mathfrak m^2=0\), this is \([g_0,T]=0\), a \(2d\)-dimensional \(k\)-linear condition space. Consequently \(|C_G(g)|=|C_{G_0}(g_0)|q^{2d}\).

**2. Scalar reduction.** If \(g_0=\lambda I_2\) with \(\lambda\in k^\times\), choose a central scalar lift \(\widetilde\lambda I_2\) and write \(g=\widetilde\lambda I_2+T\), \(T\in M_2(\mathfrak m)\). Fix a basis \(e_1,\ldots,e_d\) of \(\mathfrak m\), and write \(T=\sum_{r=1}^d e_r A_r\) with \(A_r\in M_2(k)\), interpreting this tensor identity independently of chosen representatives because \(\mathfrak m^2=0\). A reduction \(h_0\in G_0\) admits commuting lifts of \(g\) exactly when \([h_0,A_r]=0\) for all \(r\). In this case, *every* one of the \(q^{4d}\) lifts of \(h_0\) commutes with \(g\), since the error commutator lies in \(M_2(\mathfrak m^2)=0\). Thus
\[
|C_G(g)|=q^{4d}\bigl|C_{G_0}(A_1,\ldots,A_d)\bigr|.
\]
The same conclusion holds for mixed-characteristic rings: only the action of the residue field on the square-zero radical was used.

**3. Exhausting simultaneous centralizers.** Every nonscalar \(A\in M_2(k)\) generates its full two-dimensional commutative centralizer algebra \(k[A]\), which is one of \(k\times k\), \(\mathbb F_{q^2}\), or \(k[t]/(t^2)\). There are respectively \(N_s=q(q+1)/2\), \(N_i=q(q-1)/2\), and \(N_j=q+1\) distinct embedded subalgebras of those types. One may count these as unordered pairs of distinct projective lines, nonsplit quadratic embeddings modulo Frobenius, and nilpotent rank-one lines, respectively. Each has \(q^2\) elements, of which exactly \(q\) are scalar. Two distinct such subalgebras meet only in \(kI_2\), since a shared nonscalar matrix would generate both.

Therefore exactly \(q^d\) coefficient tuples are all-scalar; for each of the \(N_s+N_i+N_j=q^2+q+1\) quadratic algebras, exactly \(q^{2d}-q^d\) tuples lie in it and are not all-scalar. The remaining
\[
D=q^{4d}-q^d-(q^2+q+1)(q^{2d}-q^d)
\]
tuples contain a noncommuting pair. Their common centralizer in \(G_0\) is precisely the scalar group \(k^\times I_2\): if a nonscalar matrix commuted with all coefficients, they would all lie in its unique quadratic centralizer algebra. Thus the scalar-reduction five rows follow. If \(d=1\), then \(D=0\); for \(d\ge2\), noncommuting matrix pairs exist over every field, so \(D>0\).

**4. Nonscalar reductions.** The group \(G_0\) has \((q-1)(q-2)/2\) split-semisimple classes with distinct nonzero eigenvalues, \(q(q-1)/2\) irreducible-quadratic classes, and \(q-1\) nontrivial Jordan classes. Their centralizer orders are \(c_s,c_i,c_j\). Orbit-stabilizer yields the populations \(M_s,M_i,M_j\) given above, and each reduction has \(q^{4d}\) lifts. Step 1 supplies the last three rows. The sum of all rows is \(Uq^{4d}\).

**5. Classes and dominant stratum.** Summing the centralizer orders over all group elements, divided by \(|G|\), counts conjugacy classes. Alternatively count commuting pairs: the \((q-1)^2\) ordered pairs whose two reductions are scalar have \(q^{8d}\) commuting lift pairs each; all other commuting pairs in \(G_0\) have \(q^{6d}\) commuting lifts: fixing a lift of a nonscalar reduction leaves a \(2d\)-dimensional linear space of compatible partner lifts, while a scalar/nonscalar reduction pair is counted by choosing the nonscalar lift first. Since \(G_0\) has \(q^2-1\) conjugacy classes, there are \(U(q^2-1)\) commuting pairs in \(G_0\). Hence
\[
K(G)=\frac{(U(q^2-1)-(q-1)^2)q^{6d}+(q-1)^2q^{8d}}{Uq^{4d}},
\]
which simplifies to the displayed formula. Each noncommuting radical tuple has centralizer \((q-1)q^{4d}\), hence a conjugacy class of size \(U/(q-1)=q(q^2-1)\). Its number of classes is \(D/[q(q+1)]\). Subtracting from \(K(G)\) gives \(q^{2d+2}-q^d\) exactly. The first term is of order \(q^{4d}\), whereas this complement is of order \(q^{2d}\), proving the concentration assertion.

## Verification
The included standalone `check_commuting.py` constructs ring addition and multiplication tables independently of the centralizer proof, enumerates all invertible \(2\times2\) matrices, and compares matrix products entry-by-entry for every ordered pair. Its output is included in `checker_output.txt`. All five checks passed: \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\), \(\mathbb F_2[u,v]/(u,v)^2\), \(\mathbb F_3[\varepsilon]/(\varepsilon^2)\), \(\mathbb Z/4\mathbb Z\), and the mixed-characteristic nonprincipal ring \((\mathbb Z/4\mathbb Z)[u]/(2u,u^2)\). The two nonisomorphic rings of order eight have identical checked centralizer spectra, as predicted. These finite enumerations are corroboration; the five proof steps establish the full infinite parameter range.

Reproduce by running `python check_commuting.py` with NumPy installed. The checker performs no network access.

## Relationship to prior work
Prasad, Singla and Spallone [1] give extension-theoretic similarity classifications over length-two *principal* local rings, including the familiar \(d=1\) formula \(q^4-q\) for \(\operatorname{GL}_2\), and in Section 10 (Theorem 10.3 and Corollary 10.4) establish a general orbit reduction and ring-independence for arbitrary square-zero maximal ideals. **Those general structural reductions are acknowledged and not claimed as new.** The explicit complete \(\operatorname{GL}_2\) centralizer-size populations for every nonprincipal radical dimension, and the emergence and dominance of noncommuting coefficient tuples, are the narrower quantitative assertions evaluated here. Sharma [2] counts simultaneous similarity orbits for *pairwise commuting* tuples over finite fields. The noncommuting coefficient tuples that dominate the present conjugacy count are excluded from that restriction. Neither inspected full text states the table above or its exact exceptional-class complement. The quantitative result follows by an explicit, separate dimension-two centralizer and subalgebra census; historical equivalents remain possible.

## Limitations
No claims are made for general \(n\times n\) matrices with \(n>2\), higher radical nilpotency, or singular matrices. Some rows have zero populations for small \(q,d\), and distinct row labels can yield the same centralizer size; the table is a weighted multiset rather than a claim that eight different numeric sizes always occur. No result about independent mathematical certification is claimed. Priority beyond the two closely related sources and the documented database searches cannot be guaranteed.

## References
[1] A. Prasad, P. Singla, S. Spallone, *Similarity of matrices over local rings of length two*, arXiv:1212.6157 (first public version December 26, 2012), especially Sections 1 and 10, https://arxiv.org/abs/1212.6157 .

[2] U. B. Sharma, *Simultaneous Similarity Classes of Commuting Matrices over a Finite Field*, arXiv:1409.2698 (first public version September 7, 2014), especially Sections 1 and 3, https://arxiv.org/abs/1409.2698 .
