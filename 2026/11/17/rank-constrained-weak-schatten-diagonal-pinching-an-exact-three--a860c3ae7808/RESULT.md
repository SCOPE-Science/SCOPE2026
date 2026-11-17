# Rank-constrained weak-Schatten diagonal pinching: an exact three-phase law

## Finding
For integers \(1\le r\le n\) and real \(0<p<\infty\), write \(q=1/p\). Let \(\mathsf E_n:M_n(\mathbb C)\to M_n(\mathbb C)\) retain the diagonal and annihilate every off-diagonal entry, and equip matrices with the weak Schatten quasi-norm
\[
\|A\|_{p,\infty}=\max_{1\le j\le n}j^{1/p}s_j(A),
\]
where the singular values \(s_1(A)\ge\cdots\ge s_n(A)\ge0\) include zero multiplicities. The **exact rank-restricted amplification** is
\[
\boxed{\sup_{0<\operatorname{rank}A\le r}\frac{\|\mathsf E_n(A)\|_{p,\infty}}{\|A\|_{p,\infty}}
=\begin{cases}
 n^{q-1}\displaystyle\sum_{j=1}^r j^{-q},&0<p<1,\\[3pt]
 \displaystyle\sum_{j=1}^r j^{-1},&p=1,\\[3pt]
 r^{q-1}\displaystyle\sum_{j=1}^r j^{-q},&1<p<\infty.
\end{cases}}
\]
At \(r=n\) this is the full multiplier norm. At fixed \(r\), the amplification grows polynomially with \(n\) below \(p=1\), while for \(p\ge1\) it is independent of \(n\). At \(p=1\) unbounded amplification requires increasing input rank; rank-one inputs already suffice for divergence if \(p<1\).

All extremizers are classified as follows. Normalize \(\|A\|_{p,\infty}=1\). Choose an integer \(m\) satisfying \(m=n\) for \(p<1\), \(r\le m\le n\) for \(p=1\), or \(m=r\) for \(p>1\). Then \(A\) is extremal if and only if \(A=DB\), where \(D\) is a diagonal unitary and \(B\) is positive semidefinite, supported on an \(m\)-element coordinate subset, has nonzero eigenvalues exactly \(1,2^{-q},\dots,r^{-q}\), and has constant diagonal \(m^{-1}\sum_{j=1}^r j^{-q}\) on that subset and zero elsewhere. Such extremizers exist for every parameter triple.

## Assumptions and scope
Matrices are arbitrary complex square matrices, not assumed normal or positive. The restriction \(\operatorname{rank}A\le r\) is not a linear subspace unless \(r=n\); its supremum is therefore called an amplification rather than a linear-operator norm. All parameters are finite and positive as specified. The \(p\)-parameter denotes the weak singular-value quasi-norm, not the strong Schatten \(p\)-norm, and no statement is made at \(p=\infty\).

## Proof
Put \(H_k(q)=\sum_{j=1}^k j^{-q}\). For a matrix \(A\) of rank at most \(r\), set \(a_k\) to the \(k\)-th largest modulus of its diagonal entries. By the Ky Fan trace inequality, the sum of any \(k\) diagonal-entry moduli is bounded by the sum of the \(k\) largest singular values:
\[
 k a_k\le\sum_{i=1}^k a_i\le\sum_{j=1}^{\min(k,r)}s_j(A).
\]
If \(\|A\|_{p,\infty}=1\), each \(s_j(A)\le j^{-q}\), hence
\[
 \|\mathsf E_n(A)\|_{p,\infty}\le
 \max_{1\le k\le n} k^{q-1}H_{\min(k,r)}(q).
\]
The sequence \(f_k(q)=k^{q-1}H_k(q)\) is **strictly increasing** for every \(q>0\). Indeed, the Laplace representation of \(j^{-q}\) gives
\[
 f_k(q)=\frac1{\Gamma(q)}\int_0^\infty t^{q-1}
 \frac{1-e^{-t}}{k(e^{t/k}-1)}\,dt.
\]
For each positive \(t\), the denominator is \(t\,(e^{t/k}-1)/(t/k)\), strictly decreasing as \(k\) increases, because \((e^x-1)/x\) is strictly increasing in \(x>0\). Thus the integral increases strictly. For \(k\ge r\) the upper-bound expression is \(k^{q-1}H_r(q)\), which is strictly increasing for \(q>1\), constant for \(q=1\), and strictly decreasing for \(0<q<1\). The displayed three-case maximum follows.

For sharpness take \(m\) according to the theorem, let \(F_m\) be the unitary discrete Fourier matrix, and put
\[
 B=\left[F_m\operatorname{diag}(1,2^{-q},\ldots,r^{-q},0,\ldots,0)F_m^*\right]\oplus 0_{n-m}.
\]
Then \(B\ge0\), \(\operatorname{rank}B=r\), \(\|B\|_{p,\infty}=1\), and its first \(m\) diagonal entries equal \(H_r(q)/m\), the rest being zero. Thus \(\|\mathsf E_n(B)\|_{p,\infty}=m^{q-1}H_r(q)\), attaining the bound.

For equality, let \(A\) be normalized and suppose equality holds, with \(m\) an index attaining the maximum in the Ky Fan bound. Strict monotonicity above forces exactly the permitted choices of \(m\). Equality implies \(a_m=H_r(q)/m\) and therefore
\[
 H_r(q)\le\sum_{i=1}^{m}a_i\le\sum_{i=1}^{n}a_i\le\sum_{j=1}^{r}s_j(A)\le H_r(q).
\]
All inequalities are equalities. Consequently the nonzero singular values are exactly \(j^{-q}\), every one of the first \(m\) diagonal moduli is \(H_r(q)/m\), and every remaining diagonal entry is zero. Choose a diagonal unitary \(D\) matching their phases. Since
\(\operatorname{Tr}(D^*A)=\sum_i|A_{ii}|=\|A\|_1\), equality in trace-norm duality forces \(D^*A\) to be positive semidefinite. Its zero diagonal outside the chosen subset forces corresponding rows and columns to vanish. This gives the stated classification, and the converse follows from the sharpness calculation.

## Verification
The accompanying `checker.py` constructs Fourier witnesses for all \(n\le12\), all ranks, and six values of \(p\); it also checks randomly sampled complex rank-constrained matrices, exact rational harmonic specializations, and the monotonicity of the scalar maximizing sequence. The executed checker reported `FINITE_WEAK_PINCH_OK 22604 checks`. These finite diagnostics are not used to infer the universal quantifiers: the proof above covers all finite \(n,r\) and all \(p>0\).

In particular, at \(r=n\), the exact constants have the sharp asymptotic phases
\[
 C_{p,n,n}\sim\begin{cases}
 \zeta(1/p)n^{1/p-1},&0<p<1,\\
 \log n,&p=1,\\
 p/(p-1),&p>1.
\end{cases}
\]
For fixed \(r\), \(C_{1,n,r}=H_r(1)\), so the minimum necessary rank for amplification beyond \(K\) grows on the exponential scale \(e^K\).

## Relationship to prior work
The work of McDonald, Sukochev and Zanin (arXiv:2605.07564, originally posted 8 May 2026) characterizes qualitatively when a diagonal Schur pattern acts boundedly on symmetric operator ideals, and proves diagonal weak submajorization in its Section 4. The classical Schur–Horn framework and its infinite-dimensional extensions by Kaftal and Weiss characterize achievable diagonals for prescribed spectra. Those results provide the majorization ingredient here; the present calculation optimizes the finite weak-Schatten quasi-norm subject to a rank constraint, locates the sharp support change at \(p=1\), and classifies equality, none of which is stated in the inspected source material. The result is therefore a quantitative finite-dimensional refinement, not a new Schur–Horn theorem or a qualitative Schur-pattern classification.

## Limitations
The proof covers canonical diagonal pinching only, not arbitrary Schur masks or block conditional expectations. Its finite-dimensional extremizer classification is exact, but it makes no claim of an analogous classification for infinite noncompact operators. Majorization theory and discrete Hardy inequalities are substantial prior inputs; an equivalent formula may exist in older Lorentz-space literature. The asymptotic rank statement is a direct consequence of the exact formula, not a separate new result.

## References
1. E. McDonald, F. Sukochev, D. Zanin, *Schur bounded patterns, submajorisation and operator Lipschitz functions*, arXiv:2605.07564v2 (2026), Sections 2 and 4. https://arxiv.org/html/2605.07564v2
2. V. Kaftal, G. Weiss, *An infinite dimensional Schur-Horn theorem and majorization theory with applications to operator ideals*, arXiv:0710.5566 (2007), Introduction and majorization preliminaries. https://arxiv.org/abs/0710.5566
3. W. D. Banks, A. Harcharras, *On the norm of an idempotent Schur multiplier on the Schatten class*, Proc. Amer. Math. Soc. 132 (2004), 2121–2125. https://doi.org/10.2307/4097188
