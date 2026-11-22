# Galois descent and rank strata of commutative post-Lie products on irreducible almost-abelian Lie algebras

## Finding
Let \(k=\mathbb F_q\), let \(d\ge2\), and let \(K=\mathbb F_{q^d}\). Choose \(\alpha\in K\) of degree exactly \(d\) over \(k\), and define the \((d+1)\)-dimensional Lie algebra \(L=kt\oplus K\) by \([t,x]=\alpha x\) and \([x,y]=0\) for \(x,y\in K\). A *symmetric biderivation* is a symmetric \(k\)-bilinear product whose multiplication in each argument is a derivation of the given Lie bracket. A *commutative post-Lie (CPA) product* is a symmetric biderivation additionally satisfying
\[
 [x,y]\cdot z=x\cdot(y\cdot z)-y\cdot(x\cdot z).
\]

**Classification.** Every symmetric biderivation is uniquely parametrized by \((w,b,c)\in K^3\), with
\[
 t\cdot t=w,\qquad t\cdot x=b x,\qquad x\cdot y=cxy \quad(x,y\in K).
\]
It is a CPA product if and only if \(c=0\) and \(b(b-\alpha)=0\). Because \(K\) is a field, the two CPA families are \(b=0\) and \(b=\alpha\), each with arbitrary \(w\in K\). Hence there are \(q^{3d}\) symmetric biderivations, but exactly \(2q^d\) CPA products over \(k\).

**Galois geometry.** Let \(\mathcal C\) be the affine CPA-product scheme cut out by the polynomial CPA identities in the symmetric bilinear structure constants. It is smooth of dimension \(d\), with precisely \(2^d\) geometrically irreducible components, each an affine \(d\)-space; Frobenius permutes the components like cyclic rotation of binary words of length \(d\). For each integer \(s\ge1\), put \(Q=q^s\), \(g=\gcd(d,s)\), and \(h=d/g\). Then
\[
 \#\mathcal C(\mathbb F_{q^s})=Q^d2^g.
\]
Its Hasse--Weil zeta function is
\[
 Z(\mathcal C,T)=\prod_{e\mid d}(1-q^{de}T^e)^{-N_e},\qquad
 N_e=\frac1e\sum_{r\mid e}\mu(e/r)2^r.
\]
Here \(N_e\) counts primitive binary necklaces of length \(e\).

**Rank stratification.** View each CPA product as a linear map \(\operatorname{Sym}^2(L)\to L\). Over \(k\) its rank enumerator is
\[
 1+(q^d-1)z+q^d z^d.
\]
Over \(\mathbb F_{q^s}\) the complete rank enumerator is
\[
 1+(Q^d-1)z+\sum_{j=1}^{g}\binom gj
 \left(Q^{jh}z^{jh}+(Q^d-Q^{jh})z^{jh+1}\right).
\]
Thus scalar extension can create ranks absent over the original field. Over \(k\), the automorphism group of the fixed Lie algebra has exactly three orbits on CPA products if \(q\) is odd, of sizes \(1,q^d-1,q^d\), and exactly four if \(q\) is even, of sizes \(1,q^d-1,1,q^d-1\).

## Assumptions and scope
The Lie bracket is \(k\)-bilinear and alternating, with \(\alpha\ne0\). The extension \(K/k\) is finite and separable. The theorem is valid in all characteristics, including characteristic two, and for every integer \(d\ge2\). The word *rank* above always means the rank of the associated linear map from the symmetric square of the underlying vector space, not the rank of an individual left multiplication. The displayed extension-field formula counts products on the scalar-extended **fixed** Lie algebra, not products on a newly selected irreducible extension algebra of degree \(d\) over \(\mathbb F_{q^s}\).

## Proof
**1. Derivations and the linear biderivation space.** Work first over any extension field \(E/k\) and put \(R=K\otimes_kE\). Let \(A\) be multiplication by \(\alpha\) on \(R\). The derived Lie ideal of \(Et\oplus R\) is \(R\), since \(\alpha\) is a unit. Consequently every derivation \(D\) has
\[
 D(t)=a t+w,\qquad D(x)=B x,
 \qquad [B,A]=aA.
\]
Let \(f\in k[X]\) be the monic minimal polynomial of \(\alpha\). Because \([B,A]\) commutes with \(A\), the identity \([B,f(A)]=aAf'(A)\) holds. Its left side vanishes; its right side can vanish only if \(a=0\), since both \(A\) and \(f'(A)\) are invertible (irreducibility, nonzero root, and separability). Thus \(B\) commutes with \(A\). The centralizer of the cyclic operator \(A\) in \(\operatorname{End}_E(R)\) is precisely \(E[A]=R\), acting by multiplication.

For a symmetric biderivation \(\beta\), the derivation \(\beta(t,-)\) therefore has \(\beta(t,t)=w\in R\) and \(\beta(t,x)=bx\) for one \(b\in R\). Each derivation \(\beta(y,-)\), for \(y\in R\), restricts to a multiplication operator on \(R\). Thus \(\beta(x,y)\) is \(R\)-bilinear in \(x,y\). As \(R\) is the free rank-one module over itself, \(\beta(x,y)=cxy\) for a unique \(c\in R\). Conversely each \((w,b,c)\in R^3\) gives a symmetric biderivation by the stated formulas. This identifies the full biderivation space with affine \(3d\)-space over \(k\) and remains valid after every scalar extension.

**2. Integrability to CPA.** The remaining post-Lie identity for \((t,x,y)\), with \(x,y\in R\), reads \(c\alpha xy=0\); the right side cancels because \(R\) is commutative. Since \(\alpha\) is a unit, \(c=0\). The same identity for \((t,x,t)\) then reads \(b\alpha x=b^2x\), hence \(b(b-\alpha)=0\). All remaining basis cases follow from these equalities and symmetry, proving sufficiency as well as necessity. Write \(e=b/\alpha\in R\). The CPA condition is exactly \(e^2=e\), with \(w\) entirely free.

**3. Geometry, Frobenius, and zeta.** The separable algebra \(K\otimes_k\bar k\) is \(\bar k^d\); its primitive idempotents correspond to the \(d\) embeddings of \(K\) into \(\bar k\), cyclically permuted by \(q\)-Frobenius. Hence the idempotent equation produces \(2^d\) disjoint affine \(d\)-spaces for the free \(w\) coordinate. These are reduced and smooth even in characteristic two because each equation \(e_i^2-e_i=0\) has derivative \(2e_i-1\ne0\) at \(e_i\in\{0,1\}\). An \(s\)-fold Frobenius fixes exactly \(2^{\gcd(d,s)}\) binary vectors, proving the extension-field count. Decomposing binary vectors into cyclic orbits of minimal length \(e\mid d\) gives \(N_e=e^{-1}\sum_{r\mid e}\mu(e/r)2^r\), and the Euler product follows from the definition of the point-count zeta function.

**4. Complete image-rank counts.** The finite étale algebra \(R_s=K\otimes_k\mathbb F_{q^s}\) is a product of \(g\) fields, each of degree \(h=d/g\) over \(\mathbb F_{q^s}\). An idempotent selects \(j\) of the \(g\) factors; the image of multiplication by \(b=\alpha e\) has \(\mathbb F_{q^s}\)-dimension \(jh\). The image of the whole bilinear CPA product is this subspace plus the line spanned by \(w=t\cdot t\). There are \(Q^{jh}\) values of \(w\) within the subspace and \(Q^d-Q^{jh}\) outside. For the zero idempotent, the ranks are zero once and one for the other \(Q^d-1\) choices of \(w\). Summing over \(\binom gj\) idempotents proves the rank polynomial, including the harmless zero coefficient when \(j=g\).

**5. Automorphism orbits over the base field.** Every Lie automorphism preserves the derived ideal \(K\), sends \(t\) to \(a t+u\) with \(a\in k^\times\), and restricts to a \(k\)-linear isomorphism \(G\) on \(K\) satisfying \(G A=a A G\). Under transport of the CPA product, \(b=0\) stays zero and \(b=\alpha\) stays \(\alpha\). Automorphisms \(t\mapsto t+u\), \(x\mapsto x\) shift \(w\) by \(-2\alpha u\) in the \(b=\alpha\) family and leave \(w\) unchanged in the \(b=0\) family. Independently, automorphisms \(x\mapsto c x\), \(c\in K^\times\), scale \(w\) transitively through nonzero values. In odd characteristic the first shift makes the whole \(b=\alpha\) family one orbit; in characteristic two it leaves the zero and nonzero \(w\) strata separate. The stated three- and four-orbit formulas follow.

## Verification
The accompanying standalone Python script `verify_cpa.py` constructs the Lie structure constants, solves the full linear symmetric-biderivation equations over finite fields, and checks the nonlinear CPA identity for **every** solution in four test cases. It does not assume the claimed normal form when enumerating solutions. Its completed results are: \(\mathbb F_2\) with degree \(2\): biderivation dimension \(6\), CPA count \(8\), rank counts \((1,3,4)\); \(\mathbb F_3\) with degree \(2\): dimension \(6\), count \(18\), ranks \((1,8,9)\); \(\mathbb F_2\) with degree \(3\): dimension \(9\), count \(16\), ranks \((1,7,0,8)\); and scalar extension \(\mathbb F_2\to\mathbb F_4\) of the degree-two action: dimension \(6\), count \(64\), ranks \((1,23,40)\). In the last case new mixed idempotents appear and the rank profile differs from the base-field polynomial. These finite checks corroborate, but do not replace, the proofs for arbitrary degree and field size.

## Relationship to prior work
Di Bartolo and La Rosa, *Biderivations of complete Lie algebras* (arXiv:2307.15750v1, 28 July 2023), introduce matrix methods and determine biderivations for **complete** Lie algebras, including semisimple examples. The present algebras are noncomplete for \(d\ge2\): the above derivation calculation gives \(\dim_k\operatorname{Der}(L)=2d\), whereas \(\dim_k\operatorname{ad}(L)=d+1\). The complete-algebra theorems therefore do not supply the current classification. Burde and Moens, *Commutative post-Lie algebra structures on Lie algebras* (arXiv:1512.05096), establish the CPA identities and study perfect and complete algebras; their explicit two-dimensional affine example is the degree-one analogue, not the degree-\(d\ge2\) finite-étale descent and rank census here. Avetisyan, *The structure of almost Abelian Lie algebras* (arXiv:1610.05365), gives the general almost-abelian automorphism/derivation framework, but does not assert this CPA-product variety or its zeta function. The standard classification of finite étale algebras and elementary necklace enumeration are used as known mathematics, not claimed as new.

## Limitations
Only the irreducible, invertible almost-abelian family \(kt\ltimes K\) is addressed, with \(d\ge2\). This is not a classification for general almost-abelian matrices, general post-Lie products on distinct bracket pairs, or arbitrary nonsymmetric biderivations. The orbit statement is over the base field; orbit counts over scalar extensions are not asserted. This is a self-contained mathematical derivation with finite computational cross-checks, not an independent mathematical audit. The novelty assessment is relative to the cited, inspected sources and indexed comparisons; it is not a proof of worldwide publication priority.

## References
1. A. Di Bartolo and G. La Rosa, *Biderivations of complete Lie algebras*, arXiv:2307.15750v1 (first public version 2023-07-28), https://arxiv.org/pdf/2307.15750.
2. D. Burde and W. A. Moens, *Commutative post-Lie algebra structures on Lie algebras*, arXiv:1512.05096v1 (2015), https://arxiv.org/pdf/1512.05096.
3. Z. Avetisyan, *The structure of almost Abelian Lie algebras*, arXiv:1610.05365 (initial version 2016; revised version 2023), https://arxiv.org/pdf/1610.05365.
