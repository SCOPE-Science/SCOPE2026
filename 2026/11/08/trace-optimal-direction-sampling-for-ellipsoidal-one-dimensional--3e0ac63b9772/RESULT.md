# Trace-optimal direction sampling for ellipsoidal one-dimensional alignment

## Finding
Fix any integer \(n\ge2\) and symmetric positive definite \(S\in\mathbb R^{n\times n}\). For every nonzero \(g\in\mathbb R^n\) and unit direction \(q\in\mathbb S^{n-1}\), define
\[
\Xi_S(g,q)=\frac{(g^\top q)^2}{\|g\|_2^2(q^\top S q)}.
\]
This is the one-dimensional case of the ellipsoidal subspace-alignment statistic introduced by Chen and Xie [1]. For a direction law \(\mathcal P\), let \(\mathcal R(\mathcal P,S)=\inf_{g\ne0}\mathbb E_{q\sim\mathcal P}\Xi_S(g,q)\). Then
\[
\boxed{\sup_{\mathcal P}\mathcal R(\mathcal P,S)=\frac{1}{\operatorname{tr}S}.}
\]
A probability distribution is optimal precisely when its alignment matrix is isotropic:
\[
\boxed{\mathbb E_{\mathcal P}\frac{qq^\top}{q^\top S q}=\frac{I_n}{\operatorname{tr}S}.}
\]
Two constructive optimal distributions are (i) an eigenvector direction \(e_i\) with probability \(\lambda_i/\operatorname{tr}S\), where \((\lambda_i,e_i)\) are any orthonormal eigenpairs of \(S\), and (ii) an absolutely continuous full-support law with density
\[
\boxed{w_S(q)=\frac{n(q^\top S q)}{\operatorname{tr}S}}
\]
relative to normalized Haar probability \(\sigma\) on the sphere. The continuous sampler is exact: propose \(q\sim\sigma\), accept with probability \((q^\top S q)/\lambda_{\max}(S)\), and repeat. The acceptance probability is \(\operatorname{tr}S/(n\lambda_{\max}(S))\) and the mean number of trials is its reciprocal.

For nonscalar \(S\), the sharp worst-gradient mean alignment obeys the strict ranking
\[
\boxed{\mathcal R(\mathrm{metric\ guided},S)=\frac{1}{n\lambda_{\max}(S)}<\mathcal R(\mathrm{Haar},S)<\frac{1}{\operatorname{tr}S}.}
\]
The universal optimum divided by the metric-guided worst-direction guarantee is \(n\lambda_{\max}(S)/\operatorname{tr}S\), approaching \(n\) along \(S=\operatorname{diag}(1,\epsilon,\ldots,\epsilon)\) as \(\epsilon\downarrow0\).

For \(n=2\), \(S\) with distinct positive eigenvalues \(a,b\), and \(u\sim\sigma\), consider the rejection-free power sampling family
\[
q_\gamma=\frac{S^{-\gamma/2}u}{\|S^{-\gamma/2}u\|_2},\qquad \gamma\in\mathbb R.
\]
Writing \(M_\gamma=\mathbb E[q_\gamma q_\gamma^\top/(q_\gamma^\top S q_\gamma)]\), its eigenvalues in the eigenbasis of \(S\) are explicitly
\[
\boxed{(M_\gamma)_{ii}=\frac{\lambda_i^{-(1+\gamma)/2}}{a^{(1-\gamma)/2}+b^{(1-\gamma)/2}},\quad(\lambda_1,\lambda_2)=(a,b).}
\]
They coincide if and only if \(\gamma=-1\). Thus \(q_{-1}=S^{1/2}u/\|S^{1/2}u\|_2\) achieves the minimax constant without rejection. For nonscalar \(S\), the source's metric-guided family member \(\gamma=1\) does not.

## Assumptions and scope
All matrices are real symmetric positive definite, every direction distribution is Borel and chosen independently of the gradient, and the gradient is any nonzero real vector. All statements concern one-dimensional subspaces and the mean of the squared ellipsoidal linear-alignment statistic, not the success probability above a threshold. A direction may be identified with its antipode, since the statistic is invariant under sign. The planar power-family uniqueness requires unequal eigenvalues. Under scalar \(S\), every power sampler is Haar and hence optimal.

The statistic is the exact squared normalized support-function gain for a linear model over the line section \(\{tq:t^2q^\top S q\le\Delta^2\}\): its maximal linear gain is \(\Delta|g^\top q|/\sqrt{q^\top S q}\), whose square divided by \(\Delta^2\|g\|_2^2\) is \(\Xi_S\). This gives a direct geometric reason to optimize its worst-direction expectation, but alone does not control iterations of a model-based optimization algorithm.

## Proof
**1. Exact minimax upper bound and equality.** For a direction law \(\mathcal P\), define the real symmetric positive semidefinite matrix
\[
M_{\mathcal P}=\mathbb E_{\mathcal P}\frac{qq^\top}{q^\top S q}.
\]
It is well defined since \(q^\top S q\ge\lambda_{\min}(S)>0\). For unit \(g\), the mean alignment is \(g^\top M_{\mathcal P}g\), so \(\mathcal R(\mathcal P,S)=\lambda_{\min}(M_{\mathcal P})\). Independently of \(\mathcal P\),
\[
\operatorname{tr}(S M_{\mathcal P})=\mathbb E\frac{\operatorname{tr}(Sqq^\top)}{q^\top S q}=1.
\]
As \(M_{\mathcal P}\succeq\lambda_{\min}(M_{\mathcal P})I_n\), taking the trace against positive definite \(S\) yields \(1\ge\lambda_{\min}(M_{\mathcal P})\operatorname{tr}S\). If equality holds, \(M_{\mathcal P}-I_n/\operatorname{tr}S\succeq0\) has zero trace against positive definite \(S\), and therefore vanishes; the converse is immediate.

**2. Attainment, exact sampling cost.** Choose an orthonormal eigenbasis of \(S\) and sample \(q=e_i\) with probability \(\lambda_i/\operatorname{tr}S\). The summand on this event is \(e_i e_i^\top/\lambda_i\), so the mean is exactly \(I_n/\operatorname{tr}S\). For the continuous law, rotational invariance of normalized Haar measure gives \(\int qq^\top\,d\sigma(q)=I_n/n\). The proposed density has integral \(n\operatorname{tr}(S(I_n/n))/\operatorname{tr}S=1\), and cancellation yields
\[
\int\frac{qq^\top}{q^\top S q}w_S(q)\,d\sigma(q)=\frac{n}{\operatorname{tr}S}\int qq^\top\,d\sigma(q)=\frac{I_n}{\operatorname{tr}S}.
\]
Rejection sampling from Haar with acceptance factor \((q^\top S q)/\lambda_{\max}(S)\) is legitimate because this factor lies in \((0,1]\). Its normalization and mean geometric trial count follow by integrating the acceptance factor against Haar.

**3. Strict comparison with two published sampling rules.** For metric-guided sampling [1], set \(q=S^{-1/2}u/\|S^{-1/2}u\|_2\), with \(u\sim\sigma\). The normalization cancels from the alignment matrix, giving
\[
\frac{qq^\top}{q^\top S q}=S^{-1/2}uu^\top S^{-1/2},\qquad M_G=\frac{S^{-1}}n.
\]
Hence its worst-gradient mean is exactly \(1/(n\lambda_{\max}(S))\). For the Haar law, denote the diagonal entries of \(M_H\) in an eigenbasis by \(m_i=\mathbb E[u_i^2/D]\) with \(D=\sum_j\lambda_j u_j^2\). Off-diagonal entries vanish by sign symmetry. For each \(i\), we have \(D\le\lambda_{\max}(S)\) and strict inequality almost surely when \(S\) is nonscalar, so
\[
m_i>\frac{\mathbb E[u_i^2]}{\lambda_{\max}(S)}=\frac1{n\lambda_{\max}(S)}.
\]
Thus \(\lambda_{\min}(M_H)>\lambda_{\min}(M_G)\). If \(\lambda_i<\lambda_j\), swapping coordinates \(i,j\) in the Haar integral, with \(D'\) denoting the swapped denominator, gives the strict identity
\[
m_i-m_j=\frac{\lambda_j-\lambda_i}{2}\mathbb E\left[\frac{(u_i^2-u_j^2)^2}{DD'}\right]>0.
\]
So \(M_H\) is not a scalar matrix unless \(S\) is scalar; the equality characterization in Step 1 makes Haar strictly suboptimal for nonscalar \(S\).

**4. Planar power-family calculation.** In an eigenbasis with \(S=\operatorname{diag}(a,b)\) and \(u=(\cos t,\sin t)\) uniformly over \(0\le t<2\pi\), the normalization of \(q_\gamma\) again cancels. Its diagonal entries are
\[
m_i(\gamma)=\lambda_i^{-\gamma}\mathbb E\frac{u_i^2}{a^{1-\gamma}u_1^2+b^{1-\gamma}u_2^2}.
\]
For arbitrary positive \(A,B\), direct substitution in the circle integral or differentiation of \(\mathbb E\log(Au_1^2+Bu_2^2)=2\log((\sqrt A+\sqrt B)/2)\) yields
\[
\mathbb E\frac{u_1^2}{Au_1^2+Bu_2^2}=\frac1{\sqrt A(\sqrt A+\sqrt B)}.
\]
Interchanging the two coordinates gives the companion identity. Substituting \(A=a^{1-\gamma}\), \(B=b^{1-\gamma}\) yields the displayed formula. Off-diagonal entries vanish by sign symmetry. For \(a\ne b\), these two eigenvalues coincide exactly when \((1+\gamma)/2=0\), namely \(\gamma=-1\); at that value both equal \(1/(a+b)\), which realizes the global minimax optimum. All dimensions and boundary cases claimed are now covered.

## Verification
The included standalone `verify.py`, executable with `python verify.py`, uses only Python's standard library. It performs exact rational checks on the optimal spectral-axis distribution for dimensions two through fourteen, deterministic periodic midpoint quadrature checks against the planar closed form over four eigenvalue pairs and five power parameters, strict-planar-ordering checks, and Gaussian-Haar Monte Carlo checks of the continuous tilted measure's moment matrix in dimensions three and four. The script completed with `PASS 622 structured exact and numerical checks` on the packaged source. The proof above, not these finite checks, establishes all global and uniqueness assertions.

## Relationship to prior work
Chen and Xie [1, Sections 2.2 and 3.4] introduce the exact ellipsoidal alignment statistic, bound its probability for Haar sampling, and calculate the mean and distribution for metric-guided sampling. They do not optimize its worst-gradient mean across all direction laws or identify the continuous trace-tilted law and its planar opposite-power realization. Chen, Hu and Wu [2] analyze coordinate-subspace sampling, including weights proportional to local Lipschitz constants; probability-weighted axis designs are therefore not claimed as new here. Roberts and Royer [3] develop probabilistic descent under reduced-space random sampling rather than this shape-specific minimax alignment criterion. Standard E-optimal design formulations also explain why maximizing a smallest information eigenvalue is a natural objective; the theorem's claim is the explicit solution and strict comparison for the fixed ellipsoidal denominator. The exact spectral-axis solution is a benchmark component, not itself a claimed novel optimization method.

## Limitations
The optimality is for the *mean* of a static squared alignment statistic with the gradient adversarially selected before drawing an independent direction. It is not a uniform high-probability guarantee, not an expected progress bound for a nonlinear objective with finite interpolation models, not an algorithmic speedup, and not a result for subspaces of dimension exceeding one. The continuous optimal sampler may have high rejection cost at large condition number. The planar smooth no-rejection construction is only proven in dimension two. Historical E-optimal-design or importance-sampling literature may contain equivalent variants under another interpretation; this is a residual priority risk. Independent mathematical validation has not been carried out.

## References
[1] Yiwen Chen and Pengcheng Xie, *Random-subspace Ellipsoidal Trust-region Methods for Derivative-free Optimization*, arXiv:2610.24866v1 (first public 17 October 2026), https://arxiv.org/html/2610.24866v1, especially Sections 2.2 and 3.4.

[2] Long Chen, Xiaozhe Hu and Huiwen Wu, *Randomized Fast Subspace Descent Methods*, arXiv:2006.06589v1 (2020), https://arxiv.org/html/2006.06589v1, Sections 2 and 4.

[3] Lindon Roberts and Clément W. Royer, *Direct search based on probabilistic descent in reduced spaces*, arXiv:2204.01275v2 (2023), https://arxiv.org/html/2204.01275v2, Section 3.

[4] Michał Dereziński, Kenneth L. Clarkson, Michael W. Mahoney and Manfred K. Warmuth, *Minimax experimental design: Bridging the gap between statistical and worst-case approaches to least squares regression*, arXiv:1902.00995 (2019), https://arxiv.org/abs/1902.00995. Its different observation-design objective does not directly imply the fixed-metric alignment calculation.
