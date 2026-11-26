# Exact random-generation law for finite radical-square-zero quiver algebras

## Finding
Let \(q\) be any prime power, \(Q\) any finite quiver on a nonempty vertex set \(\{1,\ldots,n\}\), and \(k=\mathbb F_q\). Loops and parallel arrows are permitted. Write \(J\) for the arrow ideal of the path algebra and put \(A=kQ/J^2\). Set \(m_{ij}=\dim_k e_iJe_j\), with the corner convention that an arrow in this space contributes to \(m_{ij}\). All products of two arrows vanish.

For integers \(t,s\ge0\), define
\[
\rho_q(t,s)=\begin{cases}\displaystyle\prod_{h=0}^{s-1}(1-q^{h-t}),&0\le s\le t,\\0,&s>t.\end{cases}
\]
In particular, \(\rho_q(t,0)=1\). Let \((N)_{\underline n}\) denote the number of injections from an \(n\)-element set into an \(N\)-element set: it is \(\prod_{h=0}^{n-1}(N-h)\) when \(n\le N\), and zero otherwise.

**Theorem (exact tuple-generation law).** For every integer \(d\ge1\), \(d\) elements sampled independently and uniformly from \(A\) generate it as a unital \(k\)-algebra with probability
\[
\boxed{P_d(A)=\frac{(q^d)_{\underline n}}{q^{dn}}\prod_{i=1}^n\rho_q(d,m_{ii})\prod_{i\ne j}\rho_q(d-1,m_{ij}).}
\]
Equivalently, the exact number of ordered generating \(d\)-tuples is
\[
\boxed{N_d(A)=(q^d)_{\underline n}\prod_i\prod_{h=0}^{m_{ii}-1}(q^d-q^h)\prod_{i\ne j}\left[q^{m_{ij}}\prod_{h=0}^{m_{ij}-1}(q^{d-1}-q^h)\right].}
\]
An empty inner product equals one. If an indicated rank is impossible, its factor is zero. The least \(d\ge1\) for which \(P_d(A)>0\) is exactly the least positive integer satisfying all three inequalities
\[
q^d\ge n,\qquad d\ge\max_i m_{ii},\qquad d-1\ge\max_{i\ne j}m_{ij}.
\]
An empty maximum is zero. The same law depends only on \(q,n\), the multiset of loop multiplicities, and the multiset of off-diagonal corner multiplicities. It does not distinguish different incidence arrangements with the same two multisets.

## Assumptions and scope
The algebra is split basic over \(k\), with radical \(J\) and \(J^2=0\). Vertices are distinguished only for counting the displayed matrix-corner factors; the answer is independent of how the quiver is labeled. Generation is **unital \(k\)-algebra generation**: the field scalars and identity are included from the outset. The formula holds in characteristics two and odd, including nonprime finite fields. We make no claim for general quiver quotients with \(J^2\ne0\) or for nonsplit semisimple quotients.

## Proof
Write a proposed ordered tuple as \(a_h=\sum_i\lambda_{h i}e_i+u_h\), where \(u_h\in J\) and \(1\le h\le d\). For each vertex define its diagonal label \(\lambda_i=(\lambda_{1i},\ldots,\lambda_{di})\in k^d\). The image of the generated subalgebra \(B=k\langle a_1,\ldots,a_d\rangle\) in \(A/J\cong k^n\) is all of \(k^n\) exactly when the \(\lambda_i\) are pairwise distinct: evaluation of multivariate polynomials separates finitely many distinct \(k\)-points by coordinatewise interpolation; coincident points cannot be separated. There are exactly \((q^d)_{\underline n}\) possible diagonal assignments satisfying this condition. Fix one.

Put \(U_{h,ij}=e_i u_he_j\in e_iJe_j\), and let \(U_{ij}:k^d\to e_iJe_j\) send the \(h\)-th standard basis vector to \(U_{h,ij}\). For \(i\ne j\), define the nonzero difference covector \(\Delta_{ij}=(\lambda_{1i}-\lambda_{1j},\ldots,\lambda_{di}-\lambda_{dj})\). We prove that, conditioned on distinct diagonal labels, the generators produce all of \(A\) if and only if:

(i) every loop map \(U_{ii}:k^d\to e_iJe_i\) is surjective;

(ii) every off-diagonal restriction \(U_{ij}|_{\ker\Delta_{ij}}:\ker\Delta_{ij}\to e_iJe_j\) is surjective.

For necessity, a word \(w\) in the generators has, in any loop corner, radical component in the linear span of the \(U_{h,ii}\): inserting two radical factors gives zero and all intervening diagonal factors act as scalars. For an off-diagonal corner, the radical component of a word is \(U_{ij}(c(w))\), where \(c_h(w)\) is the sum, over occurrences of the \(h\)-th generator, of products of preceding diagonal evaluations at vertex \(i\) and succeeding evaluations at vertex \(j\). The elementary telescoping identity gives
\[
\Delta_{ij}\,c(w)=w(\lambda_i)-w(\lambda_j).
\]
The same holds for a linear combination of words. Any member of \(B\cap J\) has zero evaluation at every vertex, so its \((i,j)\)-component lies in \(U_{ij}(\ker\Delta_{ij})\). If \(B=A\), both necessary surjectivity conditions follow.

For sufficiency, the surjection \(B\to k^n\) has square-zero kernel \(B\cap J\), and the semisimple quotient \(k^n\) is separable. Thus its standard mutually orthogonal vertex idempotents admit lifts \(f_i\in B\) with \(f_i\equiv e_i\pmod J\) and \(\sum_i f_i=1\). In a radical-square-zero algebra, \(f_i x f_j=e_i x e_j\) for every \(x\in J\). The \((i,j)\) corner of \([a_h,a_\ell]\) for \(i\ne j\) is
\[
\Delta_{h,ij}U_{\ell,ij}-\Delta_{\ell,ij}U_{h,ij}.
\]
Because \(\Delta_{ij}\ne0\), these vectors span exactly \(U_{ij}(\ker\Delta_{ij})\). By (ii), \(B\) therefore contains all off-diagonal radical corners \(e_iJe_j\) after applying \(f_i[\cdot,\cdot]f_j\). For a loop, \(f_i a_h f_i-\lambda_{hi}f_i\in f_iJf_i=e_iJe_i\) has loop component exactly \(U_{h,ii}\): the loop component of \(f_i-e_i\) is zero by idempotency and \(J^2=0\). By (i), \(B\) contains all loop radical corners too. Hence \(J\subseteq B\), while \(B\to A/J\) is already surjective, so \(B=A\).

Finally, conditional on the diagonal labels, arrow coordinates are independent and uniform. A loop corner of dimension \(m_{ii}\) requires a surjection \(k^d\to k^{m_{ii}}\), in exactly \(\prod_{h=0}^{m_{ii}-1}(q^d-q^h)\) ways. For an off-diagonal corner of dimension \(m_{ij}\), a linear map \(k^d\to k^{m_{ij}}\) restricted to the codimension-one space \(\ker\Delta_{ij}\) must be surjective; the restriction admits \(\prod_{h=0}^{m_{ij}-1}(q^{d-1}-q^h)\) choices, and extending to the missing one-dimensional domain has \(q^{m_{ij}}\) choices. Multiply these independent contributions and the diagonal injection count; division by the total \(q^{d(n+\sum m_{ij})}\) tuples yields the probability formula. Strict positivity of the finite-field full-rank factors gives the threshold. \(\square\)

## Verification
An independent self-contained brute-force checker, `check_generation.py`, implements the multiplication \((\lambda,u)(\mu,v)=(\lambda\mu,\lambda v+u\mu)\) in \(A\) and computes the unital subalgebra generated by each tuple through repeated span closure under multiplication, rather than implementing the proposed characterization. It exhaustively verifies every tuple in 17 dimension/field/quiver configurations over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\), including extension-field arithmetic, loops, parallel arrows, distinct orientations, and both attainable and impossible generator sizes. Execute `python3 check_generation.py`; expected last line: `ALL_GENERATION_COUNTS_VERIFIED 17`.

For example, with \(q=2\), \(n=3\), \(d=2\), and either the path \(1\to2\to3\) or fork \(1\to2,\ 1\to3\), the formula gives \((4)_{\underline3}\cdot2\cdot2=96\) generating pairs among \(1024\) total pairs. For \(q=4\), \(n=2\), \(d=2\), and one arrow, it gives \(240\cdot12=2880\) generating pairs among \(4096\) pairs. Exhaustive finite checks support, but do not constitute, the uniform proof above.

## Relationship to prior work
Sercombe and Shalev, *Random generation of associative algebras* (first public version September 2, 2020, arXiv:2009.01115), study generation probabilities and general bounds for finite algebras, including a generator-number bound. Their inspected main results and generator section do not supply the displayed exact radical-square-zero quiver formula. Iovanov and Sistko, *Maximal Subalgebras of Finite-Dimensional Algebras* (arXiv:1705.00762), classify relevant maximal subalgebra types in the quiver setting; their relevant classification does not enumerate uniformly random generating tuples. Kravchenko, Mazur, and Petrenko (arXiv:1001.2873) study algebra generators and generation probabilities in other families; the inspected relevant sections do not establish this result. The distinction is between existing qualitative/maximal-subalgebra structural information and the present explicit simultaneous full-rank fiber count. Earlier results are not claimed as new.

## Limitations
The result assumes a split semisimple quotient and square-zero arrow ideal. No claim is made for general finite-dimensional algebras. A broader equivalent formula may exist in older finite-ring generation literature or arise by inclusion-exclusion from maximal-subalgebra classifications; that possibility is not eliminated by searching. Independent mathematical audit has not been performed.

## References
1. D. Sercombe and A. Shalev, *Random generation of associative algebras*, arXiv:2009.01115 (first posted 2020-09-02); DOI: 10.1112/jlms.12827.
2. M. Iovanov and A. Sistko, *Maximal Subalgebras of Finite-Dimensional Algebras*, arXiv:1705.00762 (first posted 2017-05-02).
3. I. Kravchenko, M. Mazur, and B. Petrenko, *On the smallest number of generators and probability of generating an algebra*, arXiv:1001.2873.
