# Jordan-zero bilinear preservers in odd-degree and quaternion division algebras

## Finding

Let \(F\) be any field of characteristic different from two, let \(D\) be a finite-dimensional central division \(F\)-algebra of degree \(n\), and let \(W\) be any \(F\)-vector space. Write \(x\circ y=xy+yx\). A bilinear map \(f:D\times D\to W\) is *Jordan-zero-compatible* when \(x\circ y=0\) implies \(f(x,y)=0\).

**Theorem.** If \(n\) is odd, no two nonzero elements of \(D\) anticommute. Thus every bilinear map is compatible. For scalar target, the compatible-map space has dimension \(n^4\), the factorable subspace has dimension \(n^2\), and their quotient has dimension \(n^4-n^2\).

If \(n=2\), let \(\operatorname{Trd}\) be reduced trace, \(V=\ker\operatorname{Trd}\), and define \(s(x)=\tfrac12\operatorname{Trd}(x)\), \(v(x)=x-s(x)1\). Then every compatible bilinear map has a *unique* decomposition
\[
\boxed{f(x,y)=\Phi(xy+yx)+c\,s(x)s(y)+\ell(s(x)v(y)-s(y)v(x)),}
\]
where \(\Phi:D\to W\) and \(\ell:V\to W\) are linear and \(c\in W\). For scalar target the compatible space has dimension \(8\), of which \(4\) dimensions factor through the Jordan product; the resulting defect is \(4\). The span in \(D\otimes_FD\) of all pure tensors \(x\otimes y\) with \(xy+yx=0\) has dimension \(8\).

For comparison, a degree-two central simple algebra is either quaternion division or \(M_2(F)\); in the split case all compatible bilinear maps factor through the Jordan product. Therefore the defect takes values \(4\) or \(0\), respectively, and detects splitting.

## Assumptions and scope

For any finite-dimensional unital associative \(F\)-algebra \(A\), define \(\mu_A:A\otimes_FA\to A\) by \(\mu_A(x\otimes y)=xy+yx\), and let \(Z_A\) be the linear span of all \(x\otimes y\) with \(xy+yx=0\). Then \(Z_A\subseteq\ker\mu_A\). The *Jordan-zero defect* is \(\delta_J(A)=\dim_F(\ker\mu_A/Z_A)\). As \(\mu_A(1\otimes a)=2a\), it is surjective; consequently \(\delta_J(A)\) is exactly the dimension of compatible scalar bilinear forms modulo those of the shape \(\Phi(xy+yx)\). The theorem treats all odd division degrees and division degree two, plus the split central simple degree-two comparison. There is no assertion for division degrees divisible by four.

## Proof

**Odd degree.** If nonzero \(x,y\in D\) anticommute, then \(yxy^{-1}=-x\). Reduced norm is conjugacy invariant and satisfies \(\operatorname{Nrd}(-x)=(-1)^n\operatorname{Nrd}(x)\). Odd \(n\) therefore implies \(\operatorname{Nrd}(x)=-\operatorname{Nrd}(x)\); because \(2\ne0\), the norm vanishes, contradicting invertibility. Thus all zero-Jordan pairs have a zero factor, so their tensor span is zero. The tensor space has dimension \(n^4\); multiplication has rank \(n^2\), giving \(\delta_J(D)=n^4-n^2\). In particular the degree-one boundary has defect zero.

**Quaternion zero pairs.** Every quaternion division algebra in characteristic different from two admits the symbol representation \(D=(a,b)_F\) with basis \(1,i,j,k\), \(i^2=a\), \(j^2=b\), \(ij=-ji=k\), where \(a,b\in F^\times\). The trace-zero space \(V=Fi\oplus Fj\oplus Fk\) has dimension three. For \(u,w\in V\), put \(B(u,w)=\operatorname{Trd}(uw)\). In the indicated basis, \(B\) has diagonal matrix \(\operatorname{diag}(2a,2b,-2ab)\), hence is nondegenerate. Quaternion conjugation gives \(uw+wu=B(u,w)1\).

If nonzero \(x,y\) anticommute, conjugation by \(y\) sends \(x\) to \(-x\), and conjugation by \(x\) sends \(y\) to \(-y\). Reduced-trace invariance and \(2\ne0\) force both traces to vanish. Conversely, \(u,w\in V\) anticommute precisely when \(B(u,w)=0\). Hence the nontrivial Jordan-zero pairs are exactly the orthogonal pairs for \(B\) in \(V\times V\).

**Span computation, valid over every permitted field.** Choose an orthogonal basis \(u_1,u_2,u_3\) with \(d_i=B(u_i,u_i)\ne0\). The six tensors \(u_i\otimes u_j\), \(i\ne j\), come from orthogonal pairs. For \(j=2,3\), the pair \((u_1+u_j,d_j u_1-d_1u_j)\) is also orthogonal. Modulo the six off-diagonal tensors these two new tensors have diagonal components \(d_j u_1\otimes u_1-d_1u_j\otimes u_j\). All eight tensors are linearly independent and lie in the kernel of the rank-one linear functional \(B:V\otimes_FV\to F\). That kernel has dimension \(9-1=8\), hence is exactly the span of the zero-pair tensors. Thus the restriction of any compatible bilinear map to \(V\times V\) uniquely equals \(B(u,w)w_0\) for some \(w_0\in W\).

**Complete normal form.** For a compatible \(f\), let \(w_0\) be the unique element in the preceding paragraph and set
\[
\Phi(1)=w_0,\qquad \Phi(u)=\frac{f(1,u)+f(u,1)}4,\qquad
\ell(u)=\frac{f(1,u)-f(u,1)}2,\qquad c=f(1,1)-2w_0.
\]
Since \(D=F1\oplus V\), these formulas define linear \(\Phi\), \(\ell\) uniquely. The displayed normal form agrees with \(f\) on pairs from \(\{1\}\cup V\), and hence everywhere by bilinearity. Each displayed summand vanishes on all nontrivial zero-Jordan pairs, which lie in \(V\times V\), and thus the characterization is necessary and sufficient. With \(W=F\), the parameters have dimensions \(4+3+1=8\); the factorable maps are exactly those with \(c=0\), \(\ell=0\), and have dimension four since \(\mu_D\) is onto. Hence \(\delta_J(D)=4\).

**Split comparison.** Each matrix unit of \(M_2(F)\) is in the span of idempotents: the diagonal units are idempotent and, for \(i\ne j\), \(E_{ij}=(E_{ii}+E_{ij})-E_{ii}\) is the difference of two idempotents. An--Li--He's established theorem (also Theorem 1.1 of Jia--Xiao, 2026) shows that unital associative algebras generated by idempotents are zero-Jordan-product determined in characteristic not two. Thus \(\delta_J(M_2(F))=0\). The division-versus-split dichotomy for degree-two central simple algebras completes the claim.

## Verification

The standard-library Python file `checks/verify.py` performs exact rational Hamilton-quaternion calculations, checks eight explicit Jordan-zero tensors have rank \(8\), checks the Jordan product rank \(4\), and checks four obstruction functionals are independent modulo the factorable maps. It also enumerates all \(81\) matrices of \(M_2(\mathbb F_3)\) and their \(6561\) ordered pairs, finding \(417\) Jordan-zero pairs whose simple tensors span the entire rank-\(12\) multiplication kernel. The output is reproduced in `checks/verification_output.txt`. These finite checks are corroborative: the theorem for arbitrary fields and division algebras follows from the proof above.

## Relationship to prior work

Jia and Xiao, *Finite dimensional zero Jordan product determined algebras are generated by idempotents*, arXiv:2607.05941v1 (first public July 7, 2026), proves the qualitative equivalence of the zero-Jordan-product-determined condition with generation by idempotents. Its theorem supplies the split case, but not the positive defect size or a universal normal form for nonfactorable maps.

Alaminos, Brešar, Extremera and Villena, *Zero Jordan product determined Banach algebras*, arXiv:1902.04846v1 (2019), Example 4.6, gives one explicit nonfactorable scalar bilinear map for the **real** quaternions. This is expressly a known special case of the present result, not a newly discovered counterexample. The inspected Example 4.6 and neighboring results do not present the complete compatible-map space, its quotient dimension, or the field-general classification. The orthogonal-pair tensor-span argument uses established linear algebra rather than asserting an entirely new method.

## Limitations

Historical priority cannot be guaranteed beyond the inspected literature and search comparisons. The arguments have not undergone independent audit or peer review. The theorem excludes characteristic two, central division degrees divisible by four, noncentral division algebras, and general matrix algebras beyond the degree-two split comparator. General orthogonality-preserver literature might contain an unlocated equivalent formulation.

## References

1. H. Jia and Z. Xiao, *Finite dimensional zero Jordan product determined algebras are generated by idempotents*, arXiv:2607.05941v1 (2026), https://arxiv.org/html/2607.05941 .
2. J. Alaminos, M. Brešar, J. Extremera, A. R. Villena, *Zero Jordan product determined Banach algebras*, arXiv:1902.04846v1 (2019), https://arxiv.org/abs/1902.04846 ; original author-uploaded text https://www.researchgate.net/publication/331086960_Zero_Jordan_product_determined_Banach_algebras .
3. G. An, J. Li and J. He, *Zero Jordan product determined algebras*, Linear Algebra Appl. 475 (2015), 90–93, quoted by [1] and [2].
