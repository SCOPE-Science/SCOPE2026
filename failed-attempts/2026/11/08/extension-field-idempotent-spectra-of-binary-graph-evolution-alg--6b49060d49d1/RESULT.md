# Extension-field idempotent spectra of binary graph evolution algebras

## Finding
Let \(A\in M_n(\mathbb F_2)\) and let \(E_A\) be the evolution algebra with natural basis \(e_1,\ldots,e_n\), with \(e_i e_j=0\) for \(i\ne j\) and \(e_j^2=\sum_i A_{ij}e_i\). For each integer \(f\ge1\), let \(I_A(f)\) be the number of idempotent **elements** \(x^2=x\) of \(E_A\otimes_{\mathbb F_2}\mathbb F_{2^f}\), including zero. Then
\[
I_A(f)=2^{d_A(f)},\qquad d_A(f)=\dim_{\mathbb F_2}\ker(A^f-I_n).
\]
Indeed, the idempotents form an \(\mathbb F_2\)-vector space (not generally an \(\mathbb F_{2^f}\)-subspace) isomorphic, after a choice of normal basis, to \(\ker(A^f-I_n)\).

Let \(W=\operatorname{im}(A^n)\), let \(r=\dim W\), and let \(M\) be the multiplicative order of \(A|_W\) in \(\operatorname{GL}(W)\), with \(M=1\) when \(W=0\). The **least positive period** of the entire sequence \(f\mapsto I_A(f)\) is exactly \(M\). Its maximum is \(2^r\), attained exactly at extension degrees divisible by \(M\). Thus the extension-field idempotent counts recover the stable-image order of the adjacency/structure operator.

In rational canonical terms, list the elementary-divisor blocks \(P(X)^e\) of \(A\), where \(P\in\mathbb F_2[X]\) is monic irreducible. For each \(P\ne X\), let \(o(P)\) be the multiplicative order of one (hence every Frobenius conjugate) nonzero root. Writing \(f=2^a u\) with \(u\) odd gives the fully explicit spectral formula
\[
d_A(f)=\sum_{P\ne X}\deg(P)\sum_{P^e\text{ a block}}\mathbf 1_{\{o(P)\mid u\}}\min(e,2^a),
\]
where the inner sum counts each elementary-divisor block with multiplicity. Equivalently, the least period is the least common multiple of \(o(P)\,2^{\lceil\log_2 e\rceil}\) over nonzero elementary-divisor blocks, with the lcm of the empty family defined as \(1\).

For the directed cycle on \(n\) vertices, \(I_A(f)=2^{\gcd(n,f)}\), so every positive integer occurs as a least period. A three-vertex binary directed graph with companion matrix for \(X^3+X+1\) has \(I_A(f)=1\) when \(7\nmid f\), but \(I_A(f)=8\) when \(7\mid f\). In particular, an algebra can have no nonzero idempotent over its base field and acquire seven at the first degree-seven extension.

## Assumptions and scope
We assume \(n\ge1\), \(A\) has **binary** structure coefficients, and the scalar extension is exactly \(\mathbb F_{2^f}\) for an integer \(f\ge1\). Directed graphs are allowed to have loops, and their adjacency matrices are taken in the convention \(A_{ij}=1\) when there is an arrow from vertex \(j\) to vertex \(i\). The result applies equally to all binary matrices, whether invertible or singular; no graph connectedness or symmetry is assumed. It does not assert the formula for a general matrix whose entries lie in \(\mathbb F_{2^s}\) with \(s>1\).

The word *idempotent* refers to **elements** \(x\) satisfying \(x^2=x\); it must not be confused with an *idempotent evolution algebra*, a term often meaning \(E^2=E\).

## Proof
For a coordinate column \(x=(x_i)\) over \(\mathbb F_{2^f}\), the multiplication rules give \(x^2=A x^{[2]}\), where \(x^{[2]}\) squares each coordinate. Thus \(x\) is idempotent precisely when \(x=A x^{[2]}\). The map \(x\mapsto Ax^{[2]}\) is \(\mathbb F_2\)-linear because the characteristic is two.

By the normal basis theorem, choose \(\theta\in\mathbb F_{2^f}\) such that \(\theta,\theta^2,\ldots,\theta^{2^{f-1}}\) is an \(\mathbb F_2\)-basis. Write uniquely
\[
x=\sum_{j=0}^{f-1}\theta^{2^j}v_j,\qquad v_j\in\mathbb F_2^n.
\]
Because \(A\) has entries in \(\mathbb F_2\), the equality \(x=Ax^{[2]}\) becomes \(v_j=Av_{j-1}\) with subscripts modulo \(f\). Hence \(v_j=A^jv_0\) and \((A^f-I_n)v_0=0\). Conversely, each \(v_0\in\ker(A^f-I_n)\) produces a unique idempotent
\[
x(v_0)=\sum_{j=0}^{f-1}\theta^{2^j}A^jv_0.
\]
This is an explicit \(\mathbb F_2\)-linear bijection and proves the exact count.

The Fitting decomposition gives \(\mathbb F_2^n=W\oplus\ker(A^n)\), where \(A|_W\) is invertible and \(A|_{\ker A^n}\) is nilpotent. Since \(I-A^f\) is invertible on a nilpotent operator's space, \(d_A(f)=\dim\ker((A|_W)^f-I_W)\). Consequently \(d_A(f)\le r\), with equality if and only if \((A|_W)^f=I_W\), that is, \(M\mid f\). The sequence is periodic modulo \(M\). If \(T>0\) were any period, then \(d_A(M+T)=d_A(M)=r\), forcing \(M\mid(M+T)\) and hence \(M\mid T\). This proves the least-period and maximum assertions, including the case \(W=0\).

For the elementary-divisor formula, on a cyclic primary block \(\mathbb F_2[X]/(P^e)\), multiplication by \(A^f-I\) has kernel dimension \(\deg\gcd(P^e,X^f-1)\). For \(f=2^a u\) with odd \(u\), one has \(X^f-1=(X^u-1)^{2^a}\) in characteristic two. The polynomial \(X^u-1\) is separable, and \(P\ne X\) divides it exactly when \(o(P)\mid u\). This gives the displayed sum. The order of the primary block operator is \(o(P)2^{\lceil\log_2 e\rceil}\), by the same simple-root valuation and the divisibility characterization; taking lcm over blocks gives the explicit period formula.

For a directed cycle, \(A\) cyclically permutes the coordinate basis, so the fixed vectors of \(A^f\) are constant on its \(\gcd(n,f)\) permutation cycles, giving the claimed count. For the degree-seven example, take
\[
A=\begin{pmatrix}0&0&1\\1&0&1\\0&1&0\end{pmatrix}.
\]
Its irreducible characteristic polynomial is \(X^3+X+1\); a root has multiplicative order seven, so the kernel is zero unless \(7\mid f\), when it has dimension three.

## Verification
The self-contained standard-library script `verify.py` directly enumerates all algebra elements over finite fields represented by the irreducible binary polynomials \(X+1\), \(X^2+X+1\), \(X^3+X+1\), and \(X^4+X+1\). It checks the actual idempotent equation, not just the linear algebra derivation, against \(2^{\dim\ker(A^f-I)}\).

It exhausts **all** binary matrices in dimensions one through three at the indicated extension degrees: 2 matrices in dimension one over \(\mathbb F_2\), 16 in dimension two over each of \(\mathbb F_2,\mathbb F_4,\mathbb F_8\), and 512 in dimension three over each of those three fields. It also checks six mixed four-dimensional matrices over \(\mathbb F_{16}\) and the directed-cycle formula for sizes 1 through 8 and degrees 1 through 20. The script's successful terminal marker is `VERIFY_OK`. These finite tests corroborate but do not prove the theorem for unrestricted dimensions and extension degrees; the proof above does.

## Relationship to prior work
Elduque and Labra, *Evolution algebras, automorphisms, and graphs* (arXiv:1902.02191v1, first public 2019-02-06), establish the graph/structure-matrix setting and examine automorphisms and derivations; their results do not give the extension-field idempotent-count sequence. Reis and Cadavid, *Derivations of Evolution Algebras associated to graphs over a field of any characteristic* (arXiv:2006.11934v1, first public 2020-06-21), treat binary adjacency matrices and characteristic-two derivations, not idempotent-element counts. The normal basis theorem and rational canonical form are classical ingredients, not claimed as discoveries.

The 2023 Wei–Zou paper *Isomorphism Classes of Idempotent Evolution Algebras* counts **algebras with square equal to the whole algebra** up to isomorphism; that is not a count of individual elements satisfying \(x^2=x\). Its full text was not available during this comparison, leaving a publication-priority risk, although its identified central invariant is different. García-Martínez and Pérez-Rodríguez, *A note on complete evolution algebras* (published 2026-04-22), explicitly formulate the general idempotent-equation system but investigate existence and completeness over the complex field, not the binary-extension rank/period formula.

Earlier related enumeration of idempotents in weighted-permutation evolution algebras over a fixed field, and the statistical classification of perfect binary evolution-algebra automorphisms, concern different parameters or objects. The new assertion here is the uniform all-binary-matrix **extension-degree spectrum**, its elementary-divisor resolution, and its exact least-period recovery. Any preexisting general theorem on semilinear fixed points that directly implies these statements would reduce the priority of this application; that possibility remains a stated risk.

## Limitations
This is not a classification of all evolution algebras or all idempotents over arbitrary base fields. The exact formula assumes binary coefficients, characteristic two, and finite fields of degree \(f\) over the binary prime field. The normal-basis identification depends on the chosen normal basis. Direct enumeration was restricted to the listed finite cases. The result is self-reviewed; independent audit and comprehensive literature-priority review have not been performed.

## References
1. A. Elduque and A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191v1, 2019-02-06, https://arxiv.org/abs/1902.02191.
2. T. Reis and P. Cadavid, *Derivations of Evolution Algebras associated to graphs over a field of any characteristic*, arXiv:2006.11934v1, 2020-06-21, https://arxiv.org/abs/2006.11934.
3. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368v1, 2023-10-18, https://arxiv.org/abs/2310.12368.
4. X. García-Martínez and A. Pérez-Rodríguez, *A note on complete evolution algebras*, Archiv der Mathematik (published 2026-04-22), https://doi.org/10.1007/s00013-026-02251-0.
5. The normal basis theorem and the primary decomposition theorem for finite-dimensional linear operators, standard algebraic results.
