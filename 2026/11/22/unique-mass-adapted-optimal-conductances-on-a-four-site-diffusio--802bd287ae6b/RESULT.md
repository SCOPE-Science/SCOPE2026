# Unique mass-adapted optimal conductances on a four-site diffusion chain

## Finding

**Theorem.** Fix any interior-to-endpoint mass ratio \(t>0\). On the four-vertex path, assign vertex masses \(M=\operatorname{diag}(1,t,t,1)\), and independently choose all three positive edge conductances \(w_1,w_2,w_3>0\). Let \(L_w\) be the associated ordinary weighted path Laplacian. Write the generalized eigenvalues of \((L_w,M)\) as \(0=\lambda_1<\lambda_2\leq\lambda_3\leq\lambda_4\), and define the mean-zero spectral condition number \(\kappa_M(w)=\lambda_4/\lambda_2\).

Then the exact global minimum over **all** positive triples is

\[
\inf_{w_1,w_2,w_3>0}\kappa_M(w)
=\frac{\sqrt{1+t}+1}{\sqrt{1+t}-1}.
\]

Equality holds **if and only if** there is an \(a>0\) such that

\[
(w_1,w_2,w_3)=a\left(1,\frac{1+t}{2},1\right).
\]

Thus the minimizer is unique up to the inevitable common conductance scaling. The central link is weaker than each outer link for \(0<t<1\), equal for \(t=1\), and stronger for \(t>1\). Under any specified positive total-conductance budget, the optimal triple is uniquely determined by normalizing this ratio.

## Assumptions and scope

The path has vertices \(1,2,3,4\), edges \(\{1,2\},\{2,3\},\{3,4\}\), positive **independently adjustable** conductances, and fixed positive masses in the ratio \(1:t:t:1\). The weighted Laplacian is defined by

\[
 x^{\mathsf T}L_w x
=w_1(x_1-x_2)^2+w_2(x_2-x_3)^2+w_3(x_3-x_4)^2.
\]

The generalized eigenproblem is \(L_wx=\lambda Mx\). Equivalently it is the ordinary symmetric eigenproblem for \(M^{-1/2}L_wM^{-1/2}\). Its constant generalized zero mode is omitted from the condition number. No stochastic transition or nonnegative-diagonal timestep restriction is imposed. The result is not claimed for other mass patterns or graph topologies.

In a first-order mass-lumped diffusion model \(M\dot{x}=-L_wx\), these eigenvalues are the positive decay rates. In a mass-normalized linear iteration, their ratio controls the best possible scalar relaxation factor on the mean-zero modes. The ratio is invariant under uniform conductance scaling, so its minimization is a natural shape-design problem.

## Proof

Put \(s=\sqrt{1+t}>1\), so \(t=s^2-1\). Define two explicit, mass-orthogonal-to-constants vectors

\[
 p=(s+1,1,-1,-s-1)^{\mathsf T},\qquad
 q=(s-1,-1,1,1-s)^{\mathsf T}.
\]

Both obey \(\mathbf1^{\mathsf T}Mp=\mathbf1^{\mathsf T}Mq=0\). Their three signed edge differences are respectively

\[
(s,2,s),\qquad(s,-2,s).
\]

Consequently **for every positive triple** their Dirichlet energies are identical:

\[
 p^{\mathsf T}L_wp=q^{\mathsf T}L_wq
=s^2(w_1+w_3)+4w_2=:E_w>0.
\]

Their distinct mass norms are exactly

\[
 p^{\mathsf T}Mp=4s(s+1),\qquad
 q^{\mathsf T}Mq=4s(s-1).
\]

By Rayleigh--Ritz restricted to the mass-orthogonal complement of constants,

\[
 \lambda_2\leq\frac{E_w}{4s(s+1)},\qquad
 \lambda_4\geq\frac{E_w}{4s(s-1)}.
\]

Because \(\lambda_2>0\), division gives \(\kappa_M(w)\geq(s+1)/(s-1)\) for **all** choices of the three weights. This is a common-energy, unequal-mass-norm spectral certificate, not an inference from numerical optimization or a symmetry restriction on candidate weights.

To prove attainability, take \(w=(a,a s^2/2,a)\) for any \(a>0\). Direct substitution into \(L_wp=\lambda Mp\) and \(L_wq=\lambda Mq\) yields

\[
 \lambda_p=\frac{as}{s+1},\qquad
 \lambda_q=\frac{as}{s-1}.
\]

The constant vector has eigenvalue zero, and the remaining mass-orthogonal vector \((t,-1,-1,t)^{\mathsf T}\) has eigenvalue \(\lambda_e=as^2/(s^2-1)\). For all \(s>1\),

\[
 0<\frac{as}{s+1}<\frac{as^2}{s^2-1}<\frac{as}{s-1}.
\]

Hence \(p\) and \(q\) give precisely the least-positive and greatest generalized eigenvalues, and the lower bound is attained.

For rigidity, suppose an arbitrary positive weight triple attains equality. Both displayed Rayleigh bounds must then be equalities, so in particular \(p\) is a generalized eigenvector for \(\lambda_2\). Its first and fourth coordinate equations read

\[
 sw_1=\lambda_2(s+1),\qquad
 -sw_3=-\lambda_2(s+1),
\]

forcing \(w_1=w_3=:a\) and \(\lambda_2=as/(s+1)\). Its second coordinate equation is

\[
 -sa+2w_2=t\lambda_2=as(s-1),
\]

so \(2w_2=as^2=a(1+t)\). Thus the displayed family exhausts **all** global minimizers. No differentiability, eigenvalue simplicity assumption at arbitrary weights, or boundary compactness argument is required. This completes the proof.

## Verification

The supplied standalone `VERIFY.py` checks the two exact mass-orthogonality identities, the identical edge energies for three independently symbolic weights, both norm formulas, and all four claimed eigenpairs for the explicit minimizing conductances. It also checks representative exact rational masses and a deterministic sample of positive weight triples numerically as auxiliary error-detection tests. Run with Python 3, SymPy and NumPy using `python3 VERIFY.py`.

The symbolic identities and the Rayleigh--Ritz inequalities constitute the all-parameter proof; finite numerical sampling is not used to prove universal optimality. No external computational certificate or independent audit is asserted.

## Relationship to prior work

Kempton, Herrmann and di Bernardo (2015) optimize the eigenratio of the **ordinary** weighted graph Laplacian, employing local constraints and distributed weight adaptation. Balan, Begué, Clark and Okoudjou (2016, Section 3) formulate graph Laplacian reweighting as a frame-conditioning problem. Both motivate the same spectral shape objective, but neither inspected treatment gives an exact optimizer for a **generalized** four-site problem with heterogeneous vertex masses \(M=\operatorname{diag}(1,t,t,1)\).

Boyd, Diaconis, Sun and Xiao (2006) prove a different fastest-mixing theorem for symmetric **nonnegative stochastic** transition kernels on uniformly weighted state spaces. The distinction is substantive: at \(t=1/3\) and the normalized optimal conductances \((1,2/3,1)\), the spectral-rate-optimal scalar relaxation step \(\tau=2/(\lambda_2+\lambda_4)=1/4\) makes a central diagonal of \(I-\tau M^{-1}L_w\) exactly \(-1/4\). Hence the nonnegative transition and uniform-mass assumptions cannot imply this result for arbitrary positive \(t\) and unconstrained generalized-Laplacian relaxation. Jafarizadeh and collaborators' 2021 accessible path calculations concern the ordinary Laplacian with unit vertex masses and finite small topologies, not this continuum of heterogeneous-mass problems.

Xu and Jabbari (2026) directly treat node-weighted finite-Laplacian conditioning and discuss combined node/edge optimization, including a four-robot numerical demonstration. Their article uses distributed algorithms and numerical examples and explicitly leaves joint optimization as further work; it does not state the exact fixed-heterogeneous-mass, independently adjustable path-edge theorem proved here. Their publication is used as a comparison, not as the dated focal source.

This is a precise local four-site, all-mass-ratio classification. It does not claim a general graph algorithm, and it should not be read as an assertion that all weighted paths have uniform optimal conductances under other normalization conventions.

## Limitations

The theorem requires paired equal endpoint masses and paired equal interior masses. It excludes zero conductances, finite-horizon objectives, asymmetric node masses, nonsymmetric directed dynamics, and additional per-edge capacity or nonnegative stochastic-step constraints. It optimizes the ratio of positive generalized eigenvalues, not the graph's algebraic connectivity under a fixed budget. The literature comparison is limited to the sources identified below and related indexed records; undiscovered equivalent work remains possible. In particular, a relevant 2020 journal article on optimizing synchronizability was located by abstract and later citations, but its full text was inaccessible, so publication-priority claims should be regarded as provisional rather than exhaustive.

## References

1. L. Kempton, G. Herrmann and M. di Bernardo, *Self-organization of weighted networks for optimal synchronizability*, first public preprint 2015-05-27, https://arxiv.org/abs/1505.07279 .
2. R. Balan, M. Begué, C. Clark and K. A. Okoudjou, *Optimization methods for frame conditioning and application to graph Laplacian scaling*, first public preprint 2016-09-08, https://arxiv.org/abs/1609.02233 .
3. S. Boyd, P. Diaconis, J. Sun and L. Xiao, *Fastest mixing Markov chain on a path*, American Mathematical Monthly 113 (2006), 70–74, https://web.stanford.edu/~boyd/papers/pdf/fmmc_path.pdf .
4. S. Jafarizadeh, D. Veitch, F. Tofigh, J. Lipman and M. Abolhasan, *Optimal Synchronizability in Networks of Coupled Systems: Topological View*, IEEE Transactions on Network Science and Engineering 8 (2021), 1517–1530, https://tklab.feit.uts.edu.au/~darryl/Publications/Synchronizability_accepted.pdf .
5. S. Jafarizadeh, F. Tofigh, J. Lipman and M. Abolhasan, *Optimizing synchronizability in networks of coupled systems*, Automatica 112 (2020), article 108711, https://doi.org/10.1016/j.automatica.2019.108711 (full text not inspected).
6. Y. Xu and F. Jabbari, *Distributed Optimization of Finite Condition Number for Laplacian Matrix in Multi-Agent Systems*, International Journal of Robust and Nonlinear Control 36 (2026), 5030–5043, https://doi.org/10.1002/rnc.70479 (full open-access article, Section 3.4.3 and discussion of joint node-edge optimization inspected).
