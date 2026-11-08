# Exact shadowing criterion for diagonal weighted compositions on entire-function spaces

## Finding

Let \(d\ge1\), \(c\in\mathbb C\setminus\{0\}\), and \(\lambda_1,\ldots,\lambda_d\in\mathbb C\setminus\{0\}\). On the Fréchet space \(H(\mathbb C^d)\), endowed with the compact-open topology, consider the linear homeomorphism
\[
(Tf)(z_1,\ldots,z_d)=c\,f(\lambda_1z_1,\ldots,\lambda_dz_d).
\]
**Theorem.** The operator \(T\) has the two-sided shadowing property if and only if both conditions hold:

1. either \(\max_{1\le j\le d}|\lambda_j|<1\) or \(\min_{1\le j\le d}|\lambda_j|>1\);
2. for every multi-index \(\nu\in\mathbb N_0^d\),
\[
|c|\prod_{j=1}^d|\lambda_j|^{\nu_j}\ne1.
\]

In particular, a diagonal linear symbol with at least one contracting and at least one expanding coordinate never has two-sided shadowing, **even if every Taylor monomial has a multiplier of modulus different from one**. The same obstruction holds if any coordinate has unit-modulus dilation. For one variable, the criterion covers every nonzero scalar weight and every nonzero linear dilation. For example, \(5f(z_1/2,3z_2)\) has no shadowing despite having no resonant monomial, whereas \(5f(z_1/2,z_2/3)\) and \(f(2z_1,3z_2)/5\) do have shadowing.

## Assumptions and scope

For \(R>0\), set \(p_R(f)=\sup_{|z_j|\le R}|f(z)|\); these seminorms generate the compact-open topology on \(H(\mathbb C^d)\). A two-sided \(U\)-pseudotrajectory is a family \((x_n)_{n\in\mathbb Z}\subset H(\mathbb C^d)\) with \(x_{n+1}-Tx_n\in U\) for every \(n\). The two-sided shadowing property means: for each zero-neighborhood \(V\), there is a zero-neighborhood \(U\) such that every such family satisfies \(x_n-T^ny\in V\) for every \(n\), for some entire function \(y\). No uniform boundedness of the pseudotrajectory itself is assumed. Only finite \(d\), nonzero \(c\), and nonzero diagonal entries are covered. This is **not** a statement about positive-only or finite shadowing, nor about arbitrary nondiagonal matrices.

Write \(z^\nu=\prod_jz_j^{\nu_j}\), \(|\nu|=\sum_j\nu_j\), and \(t_\nu=c\prod_j\lambda_j^{\nu_j}\). Then \(Tz^\nu=t_\nu z^\nu\). The projectors onto total Taylor degree smaller than \(N\) and its complement are denoted \(P_N\) and \(Q_N=I-P_N\).

## Proof

**1. Resonant monomials obstruct shadowing.** If \(|t_\nu|=1\) for some \(\nu\), fix a nonzero \(a\) so small that \(p_{R_0}(az^\nu)\) is below any prescribed positive error tolerance. Put \(x_n=na t_\nu^n z^\nu\). Then \(x_{n+1}-Tx_n=a t_\nu^{n+1}z^\nu\) has uniformly small \(p_{R_0}\)-seminorm, while \(x_n-T^ny\) cannot stay in \(\{p_1<1\}\) for all integers \(n\): the \(\nu\)-coefficient of the difference, after division by \(t_\nu^n\), equals \(na-[z^\nu]y\), which is unbounded.

**2. A bounded-modulus monomial subsequence obstructs shadowing.** Suppose there are pairwise distinct multi-indices \(\nu_k\), with \(|\nu_k|/k\to\infty\), and constants \(0<\eta\le M<\infty\) such that \(\eta\le|t_{\nu_k}|\le M\). If some \(|t_{\nu_k}|=1\), part 1 applies. Otherwise, pass to a subsequence, reindexing it so that still \(|\nu_k|/k\to\infty\), on which either every \(|t_{\nu_k}|<1\) or every \(|t_{\nu_k}|>1\).

Fix any \(R_0>0\) and \(\delta>0\). Put \(a_k=\delta/(2R_0^{|\nu_k|})\). In the stable alternative, prescribe the error \(e_{-k}=a_kz^{\nu_k}\) for \(k\ge1\), zero at other times; set \(x_0=0\), \(x_n=0\) for \(n\ge0\), and define \(x_n\) backward recursively by \(x_n=T^{-1}(x_{n+1}-e_n)\). Every \(x_n\) is a polynomial (only finitely many errors occur between \(n\) and zero), and \(p_{R_0}(e_n)\le\delta/2\). If an entire \(y\) traced this pseudotrajectory within \(p_1<1\), Cauchy's coefficient estimate at radius one and passage to times \(n=-m\to-\infty\) would force
\[
[z^{\nu_k}]y=-t_{\nu_k}^{k-1}a_k.
\]
Indeed, once \(m\ge k\), the relevant coefficient of \(x_{-m}\) is \(-t_{\nu_k}^{-m+k-1}a_k\); multiply the uniformly bounded coefficient difference by \(t_{\nu_k}^{m}\to0\). Hence for any \(S>R_0\),
\[
|[z^{\nu_k}]y|S^{|\nu_k|}\ge (\delta/2)\eta^{k-1}(S/R_0)^{|\nu_k|}\longrightarrow\infty,
\]
contradicting Cauchy's estimate for an entire function on the polydisk of radius \(S\).

In the unstable alternative, prescribe \(e_{k-1}=a_kz^{\nu_k}\) for \(k\ge1\), zero elsewhere, set \(x_n=0\) for \(n\le0\), and construct forward with \(x_{n+1}=Tx_n+e_n\). Again each \(x_n\) is a polynomial and the errors are uniformly small. Tracing as \(n=m\to+\infty\) forces \([z^{\nu_k}]y=t_{\nu_k}^{-k}a_k\). For \(S>R_0\), the lower bound \((\delta/2)M^{-k}(S/R_0)^{|\nu_k|}\to\infty\) gives the same contradiction. Thus the bounded-modulus subsequence prevents shadowing.

If \(|\lambda_j|=1\), use \(\nu_k=k^2 e_j\); the moduli \(|t_{\nu_k}|=|c|\) are constant. If \(|\lambda_i|<1<|\lambda_j|\), let \(a=-\log|\lambda_i|>0\), \(b=\log|\lambda_j|>0\), choose integers \(m_k\ge k^2\) increasing, and set \(n_k=\lfloor m_kb/a\rfloor\). For \(\nu_k=n_ke_i+m_ke_j\),
\[
\log|t_{\nu_k}|=\log|c|+m_kb-n_ka\in[\log|c|,\log|c|+a),
\]
so the preceding lemma applies. This proves the necessity of uniform contraction or uniform expansion.

**3. Uniformly contracting symbols yield shadowing off resonance.** Assume \(\rho=\max_j|\lambda_j|<1\) and no \(|t_\nu|=1\). Choose a positive integer \(N\) so large that \(q=|c|\rho^N<1\). The space decomposes as the topological direct sum of the finite-dimensional invariant polynomial space \(P_NH(\mathbb C^d)\) and the invariant tail \(Q_NH(\mathbb C^d)\). On the finite-dimensional space, each diagonal eigenvalue is strictly inside or outside the unit circle. For a scalar coefficient error sequence \(b_n\), the uniformly bounded correction is \(v_n=\sum_{j\ge0}t^j b_{n-1-j}\) when \(|t|<1\), and \(v_n=-\sum_{j\ge0}t^{-j-1}b_{n+j}\) when \(|t|>1\). Both satisfy \(v_{n+1}=t v_n+b_n\). There are finitely many such modes, so these Green series correct the entire low-degree error with a bound proportional to its input seminorm.

For the tail, the multivariable Schwarz estimate gives, for every \(R>0\), every \(j\ge0\), and every entire \(f\) vanishing to total order at least \(N\),
\[
p_R(T^jf)\le |c|^j\rho^{Nj}p_R(f)=q^jp_R(f).
\]
To justify this, write \((\lambda_1^jz_1,\ldots,\lambda_d^jz_d)=\rho^jw\) with \(|w_i|\le R\), and apply the order-\(N\) Schwarz lemma to the one-variable function \(s\mapsto f(sw)\). Given a pseudotrajectory \((x_n)\) with errors \(e_n=x_{n+1}-Tx_n\), define
\[
u_n=\sum_{j=0}^{\infty}T^jQ_N e_{n-1-j}.
\]
For each fixed radius \(R\), choose \(J\) so that \(\rho^JR\le R_0\). For \(j\ge J\), Schwarz's lemma at radius \(R_0\) gives the stronger bound
\[
p_R(T^jQ_Ne_{n-1-j})\le |c|^j(\rho^jR/R_0)^Np_{R_0}(Q_Ne_{n-1-j}).
\]
The finite Taylor projection and its complement are bounded for every fixed compact-open seminorm. Therefore uniform smallness of \(p_{R_0}(e_n)\) makes this geometric tail summable for every \(R\): each \(u_n\) is **entire**, not merely analytic on one disk. For a target radius \(r\le R_0\), the first estimate bounds \(p_r(u_n)\) uniformly by a constant times \(\sup_np_{R_0}(e_n)/(1-q)\). We have \(u_{n+1}=Tu_n+Q_Ne_n\). Adding the finite-dimensional Green correction yields an entire \(v_n\) with \(v_{n+1}=Tv_n+e_n\) and uniformly small \(p_r(v_n)\). Hence \(x_n-v_n=T^n(x_0-v_0)\) gives an entire shadowing orbit. For each target neighborhood, choosing the error tolerance sufficiently small proves shadowing.

**4. Uniformly expanding symbols yield shadowing off resonance.** Assume \(\min_j|\lambda_j|>1\). Apply the same argument to \(T^{-1}f(z)=c^{-1}f(z_1/\lambda_1,\ldots,z_d/\lambda_d)\), whose coordinate multipliers have moduli below one. A homeomorphism has two-sided shadowing if and only if its inverse does: reverse the integer indexing of any pseudotrajectory, using continuity of \(T^{-1}\) to convert its error neighborhood. The resonance condition is unchanged under reciprocation. This completes the sufficiency proof and the theorem. \(\square\)

## Verification

The proof is analytic and does not use finite enumeration as an infinite-dimensional certificate. The accompanying standard-library checker performs exact rational tests of the coefficient recurrences and forced Taylor coefficients for stable and unstable pulse pseudotrajectories, exact rational resonance tests for illustrative parameter choices, and sample tail-contraction inequalities. Execute `python check_shadowing.py` in the same directory; it prints a success marker and assertion count. The decisive steps remain the uniform compact-open convergence of the Green correction and the Cauchy obstruction to an entire tracing vector.

## Relationship to prior work

Wu and Wang (arXiv:2607.28705v1, Theorem 1) prove shadowing for \(0<|c|<1\) and a general invertible linear symbol of spectral radius below one; their theorem supplies a sufficient regime, not a diagonal necessity-and-sufficiency classification or the mixed-direction obstruction. Bernardes, Caraballo, Darji, Fávaro and Peris (arXiv:2403.02843; Example 8 and Remark 9) discuss failure of shadowing for scalar **multiplication** on entire-function spaces and the limitations of generalized hyperbolicity, not composition by a diagonal linear map. Bernardes and Peris (arXiv:2305.02714; Theorem 2) prove that scalar multiplication fails full shadowing, again not a complete diagonal composition criterion. Pinto (arXiv:2607.28361v1; Theorems 22 and 32) studies Banach spaces of continuous functions and bounded analytic function spaces, not the compact-open Fréchet space of entire functions; its statements do not directly imply the present necessity criterion. The theorem above is a classification for a fixed, natural operator family and does not assert a general Fréchet-space shadowing characterization.

## Limitations

The result assumes a diagonal invertible linear symbol and a nonzero scalar weight. For general matrices with nontrivial Jordan blocks, nonlinear symbols, nonconstant analytic weights, or noninvertible symbols, no classification is asserted. A broader unpublished or differently formulated theorem for Köthe spaces or weighted compositions may subsume some cases; a literature search does not establish publication priority. The proof gives a qualitative neighborhood-dependent modulus, not a universal sharp shadowing constant.

## References

1. X. Wu and G. Wang, *Shadowing and metric expansivity on Fréchet spaces*, arXiv:2607.28705v1 (first posted 2026-07-30), Theorem 1 and Section 2, https://arxiv.org/abs/2607.28705.
2. N. C. Bernardes Jr., B. M. Caraballo, U. B. Darji, V. V. Fávaro, and A. Peris, *Generalized hyperbolicity, stability and expansivity for operators on locally convex spaces*, arXiv:2403.02843, Example 8, Remark 9 and Theorem 6, https://arxiv.org/abs/2403.02843.
3. N. C. Bernardes Jr. and A. Peris, *On shadowing and chain recurrence in linear dynamics*, arXiv:2305.02714, Theorem 2, https://arxiv.org/abs/2305.02714.
4. J. V. A. Pinto, *Shadowing for weighted composition operators on spaces of continuous functions*, arXiv:2607.28361v1 (first posted 2026-07-30), Theorems 22 and 32, https://arxiv.org/abs/2607.28361.
