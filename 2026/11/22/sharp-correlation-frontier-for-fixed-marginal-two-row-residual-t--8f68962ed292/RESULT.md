# Sharp correlation frontier for fixed-marginal two-row residual tracking

## Finding

**Theorem.** Consider residual-tracking randomized least squares on two identical scalar rows, under an independent-in-time subset scheme with the same per-row inclusion probability and the same expected row count for every correlation parameter. Define the probabilities for the empty, singleton, and full subsets by
\[
\Pr(\varnothing)=\Pr(\{1,2\})=u,\quad
\Pr(\{1\})=\Pr(\{2\})=\tfrac12-u,\qquad 0\le u\le\tfrac12.
\]
For every deterministic initial iterate and residual memory, joint mean-square convergence to the least-squares solution and optimal residual table is guaranteed **if and only if** the fixed, positive, unnormalized estimator stepsize satisfies
\[
\boxed{\quad 0<h<h_*(u),\qquad h_*(u)=\frac{\sqrt{9u^2+12(1-u)}-3u}{6}.\quad}
\]
The sharp threshold strictly decreases with the probability of correlated all-or-none sampling, despite the identical per-row inclusion marginals. Its exact values at three natural designs are
\[
\begin{array}{c|c|c}
\text{scheme}&u&h_*(u)\\\hline
\text{one row every step}&0&1/\sqrt3\\
\text{independent row inclusion}&1/4&(\sqrt{17}-1)/8\\
\text{both or neither}&1/2&(\sqrt{33}-3)/12
\end{array}
\]
At equality, some deterministic initial state does not converge in mean square; above the threshold, some state has exponentially growing second moment. The all-or-none ceiling is smaller than the one-row ceiling by the exact factor \(12/[\sqrt3(\sqrt{33}-3)]\), approximately \(2.52\). These are robust stability ceilings, not statements about convergence rates or work-normalized efficiency.

## Assumptions and scope

Let \(A=(1,1)^\mathsf T\in\mathbb R^{2\times1}\), \(b\in\mathbb R^2\), and \(x_*=(b_1+b_2)/2\). The stored scalar residuals \(r_i\) are arbitrary finite real values initially, and the aggregate residual is their sum. At each iteration draw a fresh subset \(S\) independently with the probabilities above, then form from **pre-update** values
\[
 g=r_1+r_2+2\sum_{i\in S}(x-b_i-r_i),\quad
 x^+=x-hg,\quad
 r_i^+=\begin{cases}x-b_i,&i\in S,\\r_i,&i\notin S.\end{cases}
\]
Each row belongs to \(S\) with probability \(1/2\), and \(\mathbb E|S|=1\), for **every** \(u\). The estimator is unbiased for the **sum** of squared-residual gradients, with \(\mathbb E[g\mid x,r]=2(x-x_*)\). The empty subset is a legitimate draw and still permits the cached aggregate update. No stopping rule, momentum, clipping, or normalization by the realized subset size is used.

Define \(e=x-x_*\), \(z_i=r_i-(x_*-b_i)\), \(t=(z_1+z_2)/2\), and \(d=(z_1-z_2)/2\). Then the four exact linear maps on \((e,t,d)^\mathsf T\), in order empty, first-only, second-only, both, are
\[
M_\varnothing=\begin{pmatrix}1&-2h&0\\0&1&0\\0&0&1\end{pmatrix},\quad
M_1=\begin{pmatrix}1-2h&0&2h\\1/2&1/2&-1/2\\1/2&-1/2&1/2\end{pmatrix},
\]
\[
M_2=\operatorname{diag}(1,1,-1)M_1\operatorname{diag}(1,1,-1),\quad
M_{12}=\begin{pmatrix}1-4h&2h&0\\1&0&0\\0&0&0\end{pmatrix}.
\]

## Proof

**1. Exact moment reduction.** By symmetry between rows, the four moments
\[
\mathbf m_k=\bigl(\mathbb E[e_k^2],\;2\mathbb E[e_kt_k],\;\mathbb E[t_k^2],\;\mathbb E[d_k^2]\bigr)^\mathsf T
\]
form an invariant subsystem \(\mathbf m_{k+1}=T(h,u)\mathbf m_k\), where direct expansion of the four matrices gives
\[
T=\begin{pmatrix}
1-4h+4h^2+8h^2u&-8h^2u&8h^2u&4h^2(1-2u)\\
1-2h-4hu&(1-2h+8hu)/2&-4hu&-2h(1-2u)\\
(1+2u)/4&(1-2u)/4&(1+2u)/4&(1-2u)/4\\
(1-2u)/4&-(1-2u)/4&(1-2u)/4&(1+2u)/4
\end{pmatrix}.
\]
One obtains the exact factorization
\[
\det(I-T)=-hF(h,u),\qquad F(h,u)=3h^2+3uh+u-1.
\]
For each \(u\in[0,1/2]\), \(F\) increases strictly on positive \(h\), begins below zero, and has the unique positive root \(h_*(u)\) given above.

**2. Construct an exact drift certificate below the root.** Write
\[
\begin{split}
a&=[1-u+h(1-4u)]/(2h),\\
b_0&=-h(1+2u),\\
c&=h(1+2u)(2h+1),\\
\delta&=3h(1-2u)(2h+1).
\end{split}
\]
For \(h>0\), define \(\mathcal V(e,t,d)=ae^2+2b_0et+ct^2+\delta d^2\). Direct multiplication of its coefficient row by the moment matrix gives the identity, valid for **every** deterministic state,
\[
\boxed{\;\mathbb E[\mathcal V(e^+,t^+,d^+)\mid e,t,d]-\mathcal V(e,t,d)=2F(h,u)e^2.\;}
\]
We verify positivity of its \((e,t)\) block throughout \(0<h<h_*(u)\). First, at the root, using \(u=(1-3h^2)/(1+3h)\),
\[
a_* =\frac{3h(2h+1)}{3h+1}>0.
\]
Since \(a\) is affine in \(1/h\), positivity at the root and as \(h\downarrow0\) ensures positivity below it. Moreover
\[
ac-b_0^2=\frac{1+2u}{2}\bigl[(1-u)+3h(1-2u)-12h^2u\bigr].
\]
The bracket is concave as a function of \(h\) on the closed interval from zero to the root, so its minimum is attained at an endpoint. At zero it equals \(1-u>0\); at the root the determinant is
\[
(ac-b_0^2)_* = \frac{27h^3(1-h)(2h+1)^2}{(3h+1)^2}>0,
\]
using \(0<h_*(u)\le 1/\sqrt3<1\). Finally \(\delta>0\) for \(u<1/2\). Thus \(\mathcal V\) is positive definite when \(u<1/2\), and is positive definite in \((e,t)\) at the endpoint \(u=1/2\). In either case, the negative drift gives
\[
2[-F(h,u)]\sum_{k=0}^{N-1}\mathbb E[e_k^2]\le\mathbb E\mathcal V_0\quad(N\ge1),
\]
so \(\mathbb E[e_k^2]\to0\). Every individual tracker error has exact conditional replacement probability \(1/2\), and hence
\[
\mathbb E[z_{i,k+1}^2]=\tfrac12\mathbb E[e_k^2]+\tfrac12\mathbb E[z_{i,k}^2].
\]
This stable scalar filter yields \(\mathbb E[z_{i,k}^2]\to0\) for both rows even when \(u=1/2\). Sufficiency follows.

**3. Necessity for a universal guarantee.** The full second-moment map on symmetric covariance matrices is a finite-dimensional positive map,
\[
\Phi(C)=\sum_{S}\Pr(S)M_SCM_S^\mathsf T.
\]
The four-dimensional moment system is an invariant quotient of this covariance evolution, and every initial covariance generated by deterministic states spans the symmetric covariance space. For \(h=h_*(u)\), \(T\) has eigenvalue one because \(\det(I-T)=0\). For \(h>h_*(u)\), \(\det(I-T)<0\). The monic real polynomial \(\det(\lambda I-T)\) tends to positive infinity for \(\lambda\to+\infty\), so it has a real root \(\lambda>1\). Thus the full covariance map cannot have all its eigenvalues strictly inside the unit disk. If every deterministic initial full state decayed in mean square, linearity and spanning by its rank-one covariance matrices would force \(\Phi^k\to0\), contradicting that eigenvalue. Therefore at least one deterministic initialization fails at and above the root. Moreover, when \(h>h_*\), the positivity-preserving covariance map has a nonzero positive-semidefinite Perron eigenmatrix at spectral radius greater than one. Its finite decomposition into rank-one positive matrices shows that at least one deterministic initial state has an exponentially growing second moment. This is a robust *existence* assertion, not a claim about every possible initial state.

**4. Correlation ordering.** Implicit differentiation of \(F(h_*(u),u)=0\) gives
\[
\frac{dh_*}{du}=-\frac{3h_*+1}{6h_*+3u}<0.
\]
Substitution at the three listed probabilities yields the stated exact thresholds, independently of the response values and with constant marginal inclusion probabilities.

## Verification

Run `python verify.py` with SymPy and NumPy. It builds the four sample-state matrices, reconstructs the exact four-moment operator from these matrices, proves the determinant factorization, the conditional Lyapunov drift identity, and the boundary positivity identities symbolically. It checks 675 additional exact-rational initial-state/marginal/step combinations and illustrative numerical eigenvalue inequalities on both sides of the thresholds; its current output is `VERIFY_OK 709`. The universal theorem relies on the displayed analytic argument rather than the finite checks.

## Relationship to prior work

The residual-tracking method and its general subset estimator are from Xie, Qi and Han [1]; their bounds are sufficient conditions and do not give this exact correlation-dependent necessary-and-sufficient frontier. General arbitrary-sampling SAGA bounds by Qian, Qu and Richtárik [2] allow subsets but their inspected results are sufficient complexity estimates, not this exact two-row second-moment classification. Gazagnadou, Gower and Salmon [3] study fixed-size minibatch SAGA, whereas the present family varies between empty, singleton, and doubleton subsets while holding the expected batch size constant. The published exact frontier for two unequal singleton probabilities [4] and the uniform-singleton identical-row frontier [5] are related but do not imply the classification across joint inclusion correlations: their samplers always select exactly one row. All these comparisons concern the displayed sampling laws and claims, not title matches. Standard SAGA/JacSketch covariance techniques are prior art.

## Limitations

This is a two-row rank-one least-squares benchmark, with iid subsets, a fixed unnormalized stepsize and arbitrary residual-memory initialization. The exact threshold concerns *uniform guarantees over starting states*. It does not imply that each particular initialized run diverges beyond the boundary, does not optimize finite-time contraction, and does not extend to heterogeneous rows, arbitrary sampling probabilities, large systems, nonconstant steps, or cost-normalized efficiency. Full historical mathematical priority, including unindexed specialized arbitrary-sampling second-moment analyses, is not independently certified.

## References

1. J. Xie, H.-D. Qi, D. Han, *Efficient variance reduction for randomized Kaczmarz methods via residual-tracking control variates*, arXiv:2610.39537v1 (first posted 2026-10-29), https://arxiv.org/abs/2610.39537.
2. X. Qian, Z. Qu, P. Richtárik, *SAGA with Arbitrary Sampling*, arXiv:1901.08669 (2019), https://arxiv.org/abs/1901.08669.
3. N. Gazagnadou, R. M. Gower, J. Salmon, *Optimal mini-batch and step sizes for SAGA*, arXiv:1902.00071 (2019), https://arxiv.org/abs/1902.00071.
4. *Sharp sampling-imbalance frontier for two-row residual-tracking Kaczmarz*, published mathematical note, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-sampling-imbalance-frontier-for-two-row-residual-tracking--8163c39ed9e1/RESULT.md.
5. *Sharp mean-square stability frontier for rank-one residual-tracking Kaczmarz*, published mathematical note, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-mean-square-stability-frontier-for-rank-one-residual-track--aa3a11255837/RESULT.md.
