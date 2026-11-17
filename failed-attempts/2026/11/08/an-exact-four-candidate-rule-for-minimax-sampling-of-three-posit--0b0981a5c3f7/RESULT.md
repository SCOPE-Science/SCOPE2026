# An exact four-candidate rule for minimax sampling of three positively correlated coordinates

## Finding
Consider a real symmetric positive-definite matrix
\[
C=\begin{pmatrix}1&a&b\\a&1&c\\b&c&1\end{pmatrix},
\qquad 0<a,b,c<1,
\]
and independently sample exactly one coordinate in each exact coordinate-descent step on the quadratic \(f(x)=\tfrac12 x^\mathsf{T}Cx\). The unique probability vector \(p^*\) that maximizes the worst-case fractional one-step decrease in \(f\) can be found without iterative optimization, by testing at most **four explicit algebraic certificates** below. Its optimal decrease \(\rho^*\) is given simultaneously.

Put \(u=(ab/c,ac/b,bc/a)\), \(w^D_i=1-u_i\), and \(\ell_i^2=u_i/(w^D_i)^2\). First test the **double-eigenvalue candidate**: require all \(w^D_i>0\) and
\[
\mathcal H=2(\ell_1^2\ell_2^2+\ell_2^2\ell_3^2+\ell_3^2\ell_1^2)
-(\ell_1^4+\ell_2^4+\ell_3^4)\ge0.
\]
If it passes, set
\[
Q_D=\sum_{i=1}^3\frac1{w^D_i},\qquad
\rho^*=\frac1{Q_D},\qquad p_i^*=\frac{1/w^D_i}{Q_D}.
\]
Otherwise test the three sign vectors \(s=(1,-1,-1),(-1,1,-1),(-1,-1,1)\). For each, compute \(v=C^{-1}s\), \(q_i=s_iv_i\), and test \(q_i>0\) for every \(i\) and the positive-semidefiniteness of
\[
M_s=C-\operatorname{diag}(1/q_1,1/q_2,1/q_3).
\]
At least one of these three tests necessarily passes. For any passing sign candidate, set
\[
Q_s=\sum_iq_i=s^\mathsf{T}C^{-1}s,\qquad
\rho^*=\frac1{Q_s},\qquad p_i^*=\frac{q_i}{Q_s}.
\]
If two candidate certificates pass at a boundary, they produce the same unique optimal probabilities and decrease. All tests reduce to rational operations and signs of principal minors when \(a,b,c\) are rational. A double-eigenvalue certificate corresponds to a two-dimensional smallest-eigenspace; a sign-vector certificate corresponds to a one-dimensional smallest-eigenspace except on a phase boundary.

The classification includes the *genuinely frustrated inverse-correlation region* \(a>bc\), \(b>ac\), \(c>ab\). In this region every off-diagonal entry of \(C^{-1}\) is negative, and no diagonal sign change can make \(C^{-1}\) entrywise nonnegative because the triangle's sign product is negative. Thus a known inverse-positive sampling formula does not determine this region.

## Assumptions and scope
All quantifiers in the finding range over \(a,b,c\in(0,1)\) with \(C\succ0\), and probability vectors \(p_i\ge0\), \(\sum_i p_i=1\). Each sampled coordinate receives the exact one-coordinate minimizer, and probabilities are fixed and independently drawn at each step. The quantity \(\rho^*\) is the worst-case conditional expected relative decrease of the quadratic energy **for one step**, maximized over all such probabilities. It is not a claim about optimal adaptive sampling, finite-horizon total error, or the spectral radius of a deterministic iteration. Matrices on the singular boundary are excluded.

For the genuinely unequal positive triangle \((a,b,c)=(1/5,21/100,19/100)\), the double-eigenvalue branch gives
\[
p^*=\left(\frac{1308017}{3824794},\frac{1243977}{3824794},\frac{1272800}{3824794}\right),
\quad \rho^*=\frac{2547191}{9561985}.
\]
For \((a,b,c)=(3/10,1/10,1/20)\), the sign-vector branch gives
\[
p^*=\frac1{1447}(551,506,390),\qquad
\rho^*=\frac{1801}{7235}.
\]
Both triples are strictly in the frustrated inverse-correlation region. The first has a two-dimensional limiting eigenspace, the second a one-dimensional one.

## Proof
**Step 1: Exact contraction.** If \(e_i\) is the \(i\)-th coordinate vector, the exact update is \(x^+=x-(Cx)_ie_i\) because \(C_{ii}=1\). Its energy satisfies
\[
2f(x)-2f(x^+)=(Cx)_i^2.
\]
Under probabilities \(p\), the least expected fractional energy decrease over nonzero \(x\) is
\[
\rho(p)=\lambda_{\min}\bigl(C^{1/2}\operatorname{diag}(p)C^{1/2}\bigr)
=\lambda_{\min}\bigl(\operatorname{diag}(\sqrt p)C\operatorname{diag}(\sqrt p)\bigr).
\]
A probability vector with a zero entry yields \(\rho(p)=0\), whereas positive probabilities yield \(\rho(p)>0\); hence every optimum is interior.

**Step 2: Convex diagonal-obstacle formulation.** For \(\rho=\rho(p)>0\), put \(w_i=\rho/p_i\). Then \(C-\operatorname{diag}(w)\succeq0\) and \(\sum_i1/w_i=1/\rho\). Conversely, every \(w_i>0\) with \(C-\operatorname{diag}(w)\succeq0\) yields a feasible \(p_i=(1/w_i)/(\sum_j1/w_j)\) and guarantees \(\rho(p)\ge1/(\sum_j1/w_j)\). Therefore \(1/\rho^*\) is exactly the minimum of the strictly convex function \(\Phi(w)=\sum_i1/w_i\) subject to \(w>0\) and \(C-\operatorname{diag}(w)\succeq0\). A minimizer exists because feasible \(w_i\le1\) and the objective diverges when any \(w_i\downarrow0\). It is unique. Small positive \(w\) is strictly feasible because \(C\succ0\), so the semidefinite KKT conditions are necessary and sufficient.

**Step 3: Exhausting all possible KKT ranks.** Write \(M=C-\operatorname{diag}(w)\). There exists \(Z\succeq0\) with \(Z_{ii}=w_i^{-2}\) and \(MZ=0\). Since all \(Z_{ii}>0\), \(Z\ne0\), so \(M\) is singular. Also \(M\ne0\), since its off-diagonal entries are \(a,b,c>0\). Consequently \(\operatorname{rank}M\) is exactly one or two.

If \(\operatorname{rank}M=2\), then \(Z=vv^\mathsf{T}\) for some \(v\) whose entries obey \(|v_i|=1/w_i\). Let \(s_i=\operatorname{sgn}v_i\). The kernel relation \(Mv=0\) becomes \(Cv=s\), so \(v=C^{-1}s\), \(s_iv_i>0\), and \(w_i=1/(s_iv_i)\). All signs cannot agree: a positive null vector is impossible for a positive-semidefinite matrix with nonnegative diagonal and strictly positive off-diagonal entries. Up to common negation, only the three sign vectors specified in the finding remain. Conversely, any passing sign candidate has the dual certificate \(Z=vv^\mathsf{T}\) and satisfies every KKT condition, proving global optimality.

If \(\operatorname{rank}M=1\), its positive off-diagonal entries force \(M=rr^\mathsf{T}\) with \(r_i>0\), \(r_1^2=ab/c\), \(r_2^2=ac/b\), \(r_3^2=bc/a\); thus \(w=w^D\). A dual certificate \(Z\) with diagonal \(1/w_i^2\) and \(Zr=0\) is equivalent to three Euclidean vectors \(z_i\) with \(\|z_i\|=1/w_i\) and \(\sum_i r_i z_i=0\). Such vectors exist if and only if lengths \(\ell_i=r_i/w_i\) form a (possibly degenerate) triangle. Heron's squared-area identity makes that condition exactly \(\mathcal H\ge0\). Its Gram matrix supplies \(Z\). Conversely the passing double-eigenvalue candidate satisfies KKT and is globally optimal.

These cases exhaust every optimizer. Strict convexity of \(\Phi\) proves uniqueness, including the meeting boundaries. The formula for \(p^*\) follows from the diagonal-obstacle correspondence.

## Verification
Run `python3 verify.py` in the same directory. It uses only Python's standard library and exact `fractions.Fraction` arithmetic. The checker enumerates \(1000\) positive rational correlation triples with entries in \(\{1/20,\ldots,10/20\}\); all are positive definite. It finds \(238\) double-eigenvalue and \(762\) sign-vector branches. For every triple, it checks positive normalized probabilities, the exact singular positive-semidefinite primal matrix, reconstructed diagonal parameters, and (in the double case) a rational Gram dual certificate satisfying stationarity and complementarity. It also checks the exact example probabilities and rates above. This finite run is supplementary; the proof is the KKT rank classification, not enumeration.

## Relationship to prior work
Richtárik and Takáč (2013) optimize convergence **bounds** for nonuniform coordinate-descent sampling. Qu and Richtárik (2014) develop arbitrary-sampling coordinate-descent analysis. Gower and Richtárik (2015), Section 5.1, formulate general optimal discrete sampling as a semidefinite program (equations (45)--(46)); the contribution here is its complete algebraic evaluation on every strictly positive three-coordinate correlation triangle, including an exact dual-rank transition and explicit equality certificates. A published inverse-positive SPD sampling formula applies to entrywise inverse-positive matrices and some sign-gaugeable special cases; it does not cover the genuinely frustrated inverse-correlation triangle discussed above. The general E-optimal-design literature includes algorithms, notably Martinez and Wegman (2000), and may contain further equivalent special cases; see limitations.

## Limitations
The theorem assumes dimension exactly three, strictly positive pairwise correlations, exact line minimization, and independent fixed single-coordinate draws. It does not assert a new general algorithm for arbitrary dimension. The rank transition may be represented in equivalent language within older E-optimal experimental-design literature. The Martinez--Wegman publication could not be inspected in full; only its abstract, introduction and visible section snippets were accessible, so publication-priority confidence is qualified. The result has undergone only self-review and no independent mathematical audit.

## References
1. P. Richtárik and M. Takáč, *On Optimal Probabilities in Stochastic Coordinate Descent Methods*, arXiv:1310.3438v1 (first public 2013-10-13), https://arxiv.org/html/1310.3438v1.
2. Z. Qu and P. Richtárik, *Coordinate Descent with Arbitrary Sampling I: Algorithms and Complexity*, arXiv:1412.8060v1 (first public 2014-12-27), https://arxiv.org/html/1412.8060v2.
3. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296v1 (first public 2015-06-10), https://arxiv.org/html/1506.03296v5, Section 5.1.
4. W. L. Martinez and E. J. Wegman, *An alternative criterion useful for finding exact E-optimal designs*, *Statistics & Probability Letters* 47 (2000), 325--328, https://doi.org/10.1016/S0167-7152(99)00173-X (partial accessible text only).
5. *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics*, published research record dated 2026-09-20 (comparison restricted to its explicitly stated inverse-positive hypothesis).
