# Nijenhuis-operator orbits on split square-zero local algebras over finite fields

## Finding
Let \(q\) be a prime power and \(n\ge0\). For the split square-zero local algebra \(A_n=\mathbb F_q1\oplus V\), where \(\dim V=n\) and \(V^2=0\), the associative Nijenhuis operators are exactly
\[
N(c1+v)=c\lambda1+cw+T(v),\quad
\lambda\in\mathbb F_q,\quad T\in\operatorname{End}_{\mathbb F_q}(V),\quad (T-\lambda I)w=0.
\]
Their total number is \(q^{n^2+1}(2-q^{-n})\). Under conjugation by \(\operatorname{Aut}_{\mathbb F_q\text{-alg}}(A_n)\), the number \(c_n(q)\) of orbits has generating function
\[
\boxed{\sum_{n\ge0}c_n(q)z^n=\frac{q}{1-z}\prod_{j\ge1}\frac1{1-qz^j}.}
\]
Equivalently, writing \(k_i(q)\) for the number of similarity classes of \(i\times i\) matrices over \(\mathbb F_q\), with \(k_0(q)=1\),
\[
c_n(q)=q\sum_{i=0}^n k_i(q).
\]
For fixed scalar \(\lambda\) and similarity type \(T\), the orbit classes of admissible \(w\) consist of zero plus one class for each **distinct size** of a Jordan block of \(T\) with eigenvalue \(\lambda\). Hence the orbit enumeration depends on marked eigenvectors, not merely the usual similarity classes of \(T\).

## Assumptions and scope
The field is the finite field \(\mathbb F_q\), without a restriction on characteristic. The algebra is unital and commutative, with multiplication \((c,v)(d,u)=(cd,cu+dv)\). A *Nijenhuis operator* is an \(\mathbb F_q\)-linear map \(N\) satisfying, for every \(a,b\in A_n\),
\[
N(a)N(b)=N\big(N(a)b+aN(b)-N(ab)\big).
\]
Two operators are considered equivalent only if they differ by conjugation under a unital algebra automorphism of \(A_n\). We count all operators, including zero; \(n=0\) is allowed, giving \(c_0(q)=q\). Not counted are orbits under all invertible linear maps of the underlying vector space.

## Proof
**(1) Normal form.** Any linear operator has unique coordinates
\[
N(1)=\lambda1+w,\qquad N(v)=f(v)1+T(v),
\]
where \(f\in V^*\), \(w\in V\), \(T\in\operatorname{End}(V)\). For \(u,v\in V\), the scalar component of the Nijenhuis identity reads \(f(u)f(v)=2f(u)f(v)\); thus \(f(u)f(v)=0\) for every pair. Taking \(u=v\) shows \(f=0\) over every field, including characteristic two. For \(a=b=1\), the vector component becomes \(2\lambda w=\lambda w+Tw\), or \(Tw=\lambda w\). For \((1,v)\) and \((u,v)\), with \(f=0\), the identity holds automatically. These basis-pair checks are sufficient by bilinearity. This proves the normal form in both directions.

**(2) Raw count.** Fix \(\lambda\). Translate \(T\) by \(-\lambda I\); it suffices to count pairs \((S,w)\) with \(Sw=0\). The zero vector admits \(q^{n^2}\) matrices. Each of the \(q^n-1\) nonzero vectors admits \(q^{n(n-1)}\) matrices (one independent linear constraint on each of \(n\) rows). Multiplying by \(q\) possible scalars yields
\[
q\big(q^{n^2}+(q^n-1)q^{n(n-1)}\big)=q^{n^2+1}(2-q^{-n}).
\]

**(3) Reducing conjugacy.** An algebra automorphism fixes \(1\) and preserves the Jacobson radical \(V\). Conversely, every \(g\in\operatorname{GL}(V)\) extends uniquely to an algebra automorphism fixing \(1\), so the full automorphism group is \(\operatorname{GL}(V)\). It sends \((\lambda,T,w)\) to \((\lambda,gTg^{-1},gw)\).

**(4) Centralizer orbits on the eigenspace.** Fix \(T\), and decompose \(V\) into its primary \(\mathbb F_q[t]\)-modules. An admissible vector \(w\in\ker(T-\lambda I)\) lies in the \((t-\lambda)\)-primary part. The latter is a direct sum of modules \(\mathbb F_q[s]/(s^j)\), with multiplicities \(m_j\), where \(s=t-\lambda\). The centralizer of \(T\) acts on the socle (the kernel of \(s\)); its orbits are indexed by zero and the smallest block length \(j\) with a nonzero socle coordinate. Indeed, every module automorphism preserves the descending filtration \(\ker s\cap s^{j-1}V\), and hence the smallest nonzero block length is invariant. In each fixed-length family, invertible block changes make the first nonzero coordinate standard. Homomorphisms from a shorter cyclic block to any longer cyclic block can remove all longer-block socle coordinates. The same argument applies over every field. Thus the number is \(1+d_\lambda(T)\), where \(d_\lambda(T)=|\{j:m_j>0\}|\).

**(5) Euler product.** Let \(P(z)=\prod_{j\ge1}(1-z^j)^{-1}\) enumerate partitions. If one weights a partition by \(1\) plus the number of its distinct part sizes, its generating function is
\[
P(z)\Big(1+\sum_{j\ge1}z^j\Big)=\frac{P(z)}{1-z},
\]
since the weighted contribution of partitions containing a part \(j\) is \(z^jP(z)\). A similarity class of \(T\) is specified by a partition for each monic irreducible polynomial \(h\) over \(\mathbb F_q\), of weight \(\deg h\). For fixed \(\lambda\), replace the ordinary partition contribution of the degree-one factor \(t-\lambda\) by \(P(z)/(1-z)\); other factors are unchanged. The ordinary matrix similarity-class series is
\[
K_q(z)=\prod_{h\text{ irreducible}}P(z^{\deg h})
=\prod_{j\ge1}\frac1{1-qz^j}.
\]
The second equality follows from unique factorization of monic polynomials: \(\prod_h(1-u^{\deg h})^{-1}=(1-qu)^{-1}\). The fixed-\(\lambda\) orbit series is therefore \(K_q(z)/(1-z)\). There are \(q\) independent choices of \(\lambda\), giving the theorem.

## Verification
Run \(\texttt{python verify.py}\). The standalone verifier exhausts the defining Nijenhuis identity among all linear endomorphisms for \((q,n)=(2,1),(3,1),(2,2),(3,2)\); in each case it checks equality with the normal form and raw count. Separately it enumerates the actual \(\operatorname{GL}_n(\mathbb F_q)\)-orbits of the normal-form triples for those cases and \((q,n)=(2,3)\), comparing the resulting counts against the Euler-product coefficient. The tested orbit totals are \(6,12,18,48,46\) in this order, and the tested raw counts are \(6,15,56,459\). The program ends with \(\texttt{VERIFY_OK}\). The finite tests corroborate, but do not replace, the proof for all prime powers and all \(n\).

## Relationship to prior work
The Nijenhuis identity is established in the literature on associative operated algebras. Zou, Gao, Kang, and Lü, arXiv:2308.12121 (first public version August 23, 2023), classify Nijenhuis operators on three-dimensional complex associative algebras. Their algebra \(C_{10}\) is the case \(\dim V=2\); Theorem 4.1 gives complex-field parameter families, and the paper explicitly leaves automorphism-orbit analysis aside. The present theorem does **not** claim a first three-dimensional parameterization: it gives an arbitrary-dimensional field-independent reduction and exact finite-field orbit generating function.

Achar and Henderson, arXiv:0712.1079, classify the broader enhanced nilpotent-cone orbits of a vector paired with a nilpotent matrix. Such classical framed-matrix orbit theory underlies the eigenvector-orbit step and is not claimed as new. Standard rational canonical classification and the matrix similarity Euler product are likewise prior mathematics. Wang, Zhu, and Gao, arXiv:2203.02851, treat operated polynomial identities and Gröbner–Shirshov bases rather than this specific automorphism-orbit count. Ma and Long (DOI below) study associative Nijenhuis bialgebra structures, without an identified statement of the present finite-field orbit series. No uniqueness-of-publication claim is made: an unlocated equivalent counting formula remains possible.

## Limitations
Only split local algebras with square-zero radical are treated. No claim is made for higher radical length, nonunital algebras, general associative products, or conjugation by \(\operatorname{GL}_{n+1}(\mathbb F_q)\). The given normal form is a special feature of the unital square-zero multiplication. Verification code checks prime fields and small dimensions; the mathematical proof, not the tests, establishes the result over nonprime finite fields and all dimensions. An independent mathematical audit and exhaustive literature-priority validation have not been performed.

## References
1. X. Zou, X. Gao, C. Kang, J. Lü, *Nijenhuis operators on 2D pre-Lie algebras and 3D associative algebras*, arXiv:2308.12121v1, first posted 2023-08-23; relevant full text arXiv:2308.12121v3, §§2 and 4, especially Theorem 4.1. https://arxiv.org/abs/2308.12121
2. P. N. Achar, A. Henderson, *Orbit closures in the enhanced nilpotent cone*, arXiv:0712.1079v1 (2007), §2. https://arxiv.org/abs/0712.1079
3. J. Wang, Z. Zhu, X. Gao, *New operated polynomial identities and Gröbner–Shirshov bases*, arXiv:2203.02851v1 (2022), DOI:10.3390/math10060961. https://arxiv.org/abs/2203.02851
4. T. Ma, L. Long, *Nijenhuis operators and associative D-bialgebras*, J. Algebra (2024), DOI:10.1016/j.jalgebra.2023.09.047.
