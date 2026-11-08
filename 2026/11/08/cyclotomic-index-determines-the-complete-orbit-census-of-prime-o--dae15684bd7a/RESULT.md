# Cyclotomic index determines the complete orbit census of prime-order generalized Paley automata

## Finding

Let \(p\) be an odd prime and \(k\geq3\) a divisor of \(p-1\) such that \(d=(p-1)/k\) is positive and even. Let \(H=\{h^k:h\in\mathbb F_p^\times\}\), the multiplicative subgroup of size \(d\), and let \(G=\operatorname{Cay}(\mathbb F_p,H)\) be the undirected graph joining \(a\) to \(b\) exactly when \(b-a\in H\). Let \(Q=p^f\), with \(f\ge1\), and update vertex states in \(\mathbb F_Q\) synchronously by the neighbor sum \(x(t+1)=Ax(t)\), where \(A\) is the adjacency matrix of \(G\) over \(\mathbb F_Q\).

Write \(J_s(\lambda)\) for a Jordan block of size \(s\) and eigenvalue \(\lambda\). **The complete Jordan decomposition is**
\[
A\sim J_{k+1}(d)\oplus J_k(d)^{\oplus(d-1)}.
\]
In particular, \(A\) is invertible. Put \(\ell=\operatorname{ord}_{\mathbb F_p^\times}(d)\), the multiplicative order of the residue \(d\) modulo \(p\). Since \(2\le d<p\), \(\ell>1\). Every state is periodic already at its initial time. The exact number of states fixed by the \(t\)-th iterate, for each integer \(t\ge1\), is
\[
\#\operatorname{Fix}(A^t)=
\begin{cases}
1,&\ell\nmid t,\\
Q^d,&\ell\mid t\text{ and }p\nmid t,\\
Q^p,&p\ell\mid t.
\end{cases}
\]
The only possible least periods are \(1\), \(\ell\), and \(p\ell\), with exact *numbers of distinct temporal orbits*
\[
\begin{array}{c|ccc}
\text{least period}&1&\ell&p\ell\\\hline
\text{number of orbits}&1&(Q^d-1)/\ell&(Q^p-Q^d)/(p\ell).
\end{array}
\]
There are no orbits of any other least period. Both nontrivial classes occur, so the permutation order of \(A\) on all states is exactly \(p\ell\). Equivalently, the finite dynamical zeta function is
\[
\zeta_A(z)=\frac1{(1-z)(1-z^\ell)^{(Q^d-1)/\ell}(1-z^{p\ell})^{(Q^p-Q^d)/(p\ell)}}.
\]

## Assumptions and scope

The vertex count is the prime \(p\), not the state-field size \(Q\). The graph uses the multiplicative subgroup \(H\) **inside \(\mathbb F_p\)**; state values lie in the extension field \(\mathbb F_{p^f}\), so the adjacency operator is taken in the same characteristic as the vertex count. The degree is \(d\), the cyclotomic index is \(k\), and \(p=kd+1\). The requirement that \(d\) is even is exactly \(-1\in H\), ensuring the Cayley graph is an undirected simple graph. The condition \(k\ge3\) excludes the ordinary quadratic-residue Paley family of index two. The result includes the prime-cycle endpoint \(d=2\), but does not require that the graph have girth greater than three, and includes arbitrary allowed even degrees. All orbit counts refer to **labelled configurations**, without quotienting by graph automorphisms.

## Proof

**Step 1: reduce the adjacency operator to one cyclic translation.** Number vertices by \(\mathbb F_p\), and let \(S\) be translation by one on the vector space \(V=\mathbb F_Q^{\mathbb F_p}\). Since \(S\) cyclically permutes a basis of size \(p\), it has minimal polynomial \(X^p-1=(X-1)^p\) in characteristic \(p\). Therefore \(Z=S-I\) is one nilpotent Jordan block of size \(p\), and \(Z^p=0\). With \(h\) represented by the integer in \(\{1,\ldots,p-1\}\), the adjacency operator is \(A=F(S)\) for \(F(X)=\sum_{h\in H}X^h\). The sign convention for translation is immaterial because \(H=-H\).

**Step 2: locate the first nonconstant coefficient.** Expand
\[
A=F(1+Z)=\sum_{j=0}^{p-1}c_jZ^j,\qquad
c_j=\sum_{h\in H}\binom hj\pmod p.
\]
For any positive integer \(j\), the power sum \(\sum_{h\in H}h^j\) vanishes in \(\mathbb F_p\) unless \(d\mid j\); for \(d\mid j\), it equals \(d\). Indeed, the elements of \(H\) are the \(d\)-th roots of unity, and multiplication by a generator of \(H\) permutes them. For \(1\le j<d\), the polynomial \(\binom Xj=X(X-1)\cdots(X-j+1)/j!\), defined over \(\mathbb F_p\) because \(j<p\), is a linear combination of monomials of degrees \(1,\ldots,j\). Hence \(c_j=0\) for \(1\le j<d\). At \(j=d\), only its leading term \(X^d/d!\) contributes, giving \(c_d=d/d!\ne0\). The constant coefficient is \(c_0=d\). Therefore
\[
A-dI=Z^dU(Z),\qquad U(0)=d/d!\ne0.
\]
The operator \(U(Z)\) is invertible, since it is a polynomial in the nilpotent \(Z\) with nonzero constant term.

**Step 3: determine all Jordan blocks.** Set \(N=A-dI\). Since \(U(Z)\) commutes with \(Z\), for every integer \(t\ge0\),
\[
N^t=Z^{dt}U(Z)^t,\qquad
\dim\ker(N^t)=\min(dt,p).
\]
Thus \(N\) and \(Z^d\) have identical nullity sequences and hence identical nilpotent Jordan block multisets. Write \(p=kd+1\). The \(d\) residue chains of powers of \(Z\), modulo \(d\), have one chain of length \(k+1\) and \(d-1\) chains of length \(k\). This proves the stated Jordan decomposition of \(A\). In particular \(A\) is invertible, \(\dim\ker N=d\), and the nilpotency index of \(N\) is exactly \(k+1\le p\).

**Step 4: find iterate kernels and orbits.** Since the characteristic is \(p\),
\[
A^p=(dI+N)^p=dI+N^p=dI,
\]
and therefore \(A^{p\ell}=I\). For \(t\ge1\) with \(\ell\nmid t\), the constant term of the polynomial \((d+X)^t-1\) is \(d^t-1\ne0\), so \(A^t-I\) is invertible and fixes only the zero vector. If \(\ell\mid t\) and \(p\nmid t\), that polynomial has a simple root at \(X=0\), because its linear coefficient is \(td^{t-1}\ne0\). Consequently \(A^t-I=NV(N)\) for an invertible \(V(N)\), and its kernel has dimension \(d\). If \(p\ell\mid t\), then \(A^t=I\). These cases give the fixed-point formula.

All periods divide \(p\ell\). As \(p\) and \(\ell\) are coprime and \(\ell\mid p-1\), the only divisors of \(p\ell\) that can occur are \(1\), \(\ell\), or \(p\ell\): any period not divisible by \(\ell\) would force an iterate with just one fixed state. Moreover the \(Q^d-1\) nonzero vectors in \(\ker N\) have period exactly \(\ell\), while all remaining \(Q^p-Q^d\) vectors have period exactly \(p\ell\). Division by the orbit length gives the claimed orbit counts. The latter population is nonempty because \(p>d\), proving the sharp permutation order. Multiplying the standard factors \((1-z^{\text{period}})^{-\text{number of orbits}}\) gives the displayed zeta function.

## Verification

Three standalone, standard-library Python programs accompany this statement and were executed from their actual source files. `verify_matrix.py` constructs adjacency matrices over \(\mathbb F_p\) and checks nullity sequences for all eligible \((p,k)\) with \(p\in\{7,13,19,31,37,43\}\) (15 families), including sampled exact iterate fixed-space dimensions. `verify_moments.py` independently checks subgroup power sums, binomial coefficients, and orbit-count divisibility for 89 eligible families with odd primes through 127. `verify_orbits.py` exhaustively enumerates all \(7^7=823{,}543\) states on \(\operatorname{GPaley}(7,2)=C_7\) over \(\mathbb F_7\), finding exactly one fixed state, 16 distinct three-cycles, and 39,214 distinct 21-cycles. Each program's captured output is included as an accompanying text file. These tests confirm only finite instances; the all-parameter assertion is proved above independently of them.

Another non-cycle example is \(p=13\), \(k=3\), \(d=4\), \(Q=13\), \(\ell=6\): it has precisely one fixed state, \((13^4-1)/6=4760\) six-cycles, and \((13^{13}-13^4)/78\) 78-cycles.

## Relationship to prior work

Lim and Praeger's 2006 definition and structural theorems establish the generalized Paley graph family and investigate connectivity and automorphisms, not modular neighbor-sum orbit counts. Chandler, Sin and Xiang (2014) compute Smith forms of adjacency and Laplacian matrices for **quadratic-residue** Paley graphs (the excluded index \(k=2\)), rather than arbitrary higher-index prime-order generalized Paley automata. Podestá and Videla (2023 preprint) compute characteristic-zero adjacency spectra through Gaussian periods and related spectral graph properties, not the characteristic-\(p\) nilpotent Jordan decomposition or its dynamical implications. The eigenvalue multiset over characteristic zero cannot by itself determine the Jordan block lengths after modular reduction. The present claim concerns exact characteristic-\(p\) Jordan chains and all finite-field orbit counts for index \(k\ge3\).

## Limitations

The theorem treats prime vertex counts only; for vertex set \(\mathbb F_{p^m}\) with \(m>1\), the regular representation and subgroup moment argument require additional analysis and no analogous classification is asserted. It applies only when the state field has characteristic \(p\), not when it has another characteristic. The graph must be undirected (\(d\) even) and have index at least three. All counts refer to labelled states rather than isomorphism classes under graph automorphisms. The literature comparison is a documented best-knowledge assessment, not a guarantee that no earlier unindexed modular-circulant result exists. No independent external audit has been performed.

## References

1. T. K. Lim and C. E. Praeger, *On generalised Paley graphs and their automorphism groups*, arXiv:math/0605252, initially posted 10 May 2006. https://arxiv.org/abs/math/0605252
2. D. B. Chandler, P. Sin and Q. Xiang, *The Smith and critical groups of Paley graphs*, arXiv:1401.8260, initially posted 31 January 2014. https://arxiv.org/abs/1401.8260
3. R. A. Podestá and D. E. Videla, *Spectral properties of generalized Paley graphs*, arXiv:2310.15378, initially posted October 2023. https://arxiv.org/abs/2310.15378
