# Exact rim-price transition and optimizer rigidity for fastest diffusion on wheel networks

## Finding

For every integer \(m\ge3\), let \(W_{m+1}=K_1\vee C_m\) have hub \(0\) and rim vertices \(1,\ldots,m\), with rim indices modulo \(m\). Independently assign nonnegative conductances \(s_j\) to hub--rim edges \(\{0,j\}\) and \(r_j\) to rim edges \(\{j,j+1\}\). Each hub edge costs one unit per unit conductance and each rim edge costs \(c>0\). Fix any total budget \(B>0\). Let \(L(s,r)\) be the unnormalized, symmetric weighted Laplacian and maximize its second-smallest eigenvalue \(\lambda_2\) subject to
\[
\sum_{j=1}^{m}s_j+c\sum_{j=1}^{m}r_j\le B.
\]
Put \(\kappa_m=4\sin^2(\pi/m)\). The optimum and **all** its (not necessarily symmetric a priori) conductance assignments are:

1. When \(0<c<\kappa_m\), the unique optimum is
\[
s_j=a=\frac{B\kappa_m}{m(\kappa_m+mc)},\qquad
r_j=b=\frac{B}{\kappa_m+mc}\quad\text{for every }j,
\]
with \(\lambda_2^*=\frac{(m+1)B\kappa_m}{m(\kappa_m+mc)}\).
2. When \(c=\kappa_m\), the complete set of optima is the closed line segment
\[
s_j=a=\frac{B}{m}-\kappa_m b,\qquad
r_j=b,\qquad 0\le b\le\frac{B}{(m+1)\kappa_m},
\]
with \(\lambda_2^*=B/m\).
3. When \(c>\kappa_m\), the unique optimum has \(s_j=B/m\) and \(r_j=0\) for every \(j\), with \(\lambda_2^*=B/m\).

Consequently the sharp rim-investment cutoff is \(c=4\sin^2(\pi/m)\). At equal prices \(c=1\), all optimal rims are funded for \(3\le m\le5\); \(m=6\) has a nontrivial interval of optima; for every \(m\ge7\), the unique optimal network is a uniform star with every rim edge unfunded. The critical relative price decreases as
\[
\kappa_m=\frac{4\pi^2}{m^2}-\frac{4\pi^4}{3m^4}+O(m^{-6}).
\]

## Assumptions and scope

This is the continuous-time symmetric diffusion process with generator \(-L\), not the discrete-time stochastic-matrix SLEM problem. The physical convergence objective is \(\lambda_2(L)\), not the largest Laplacian eigenvalue, Kirchhoff index, a normalized Laplacian, or an intermediate timestep method. Individual rim and spoke conductances are unrestricted except for nonnegativity and the single total weighted-cost constraint. When rim conductances vanish, the positive spoke edges leave a connected star, so the positive optimal gap remains well defined. The result includes the complete four-vertex wheel \(m=3\).

## Proof

Set \(S=\sum_j s_j\) and \(R=\sum_jr_j\). Since the objective is positively homogeneous and a positive-gap feasible solution exists, every optimum exhausts the budget: \(S+cR=B\).

**Two universal Rayleigh bounds.** The hub-versus-rim vector \(v=(m,-1,\ldots,-1)\) is orthogonal to the constant vector. It has squared norm \(m(m+1)\) and Dirichlet energy \((m+1)^2S\). Therefore
\[
\lambda_2(L)\le \frac{(m+1)S}{m}.\tag{1}
\]
For \(\theta=2\pi/m\), take the two real vectors \(x_j=\cos(j\theta)\) and \(y_j=\sin(j\theta)\) on the rim, both zero at the hub. They are orthogonal to constants, each has squared norm \(m/2\), and their sum of spoke-edge Dirichlet energies equals \(S\). The sum on the rim edges equals \(\kappa_m R\), since \(|e^{i\theta}-1|^2=\kappa_m\). As both Rayleigh quotients are at least \(\lambda_2\),
\[
\lambda_2(L)\le\frac{S+\kappa_m R}{m}.\tag{2}
\]

**Optimize both bounds.** Substitute \(S=B-cR\) into the smaller of (1) and (2):
\[
\lambda_2(L)\le \frac1m\min\{(m+1)(B-cR),\ B+(\kappa_m-c)R\},\quad 0\le R\le B/c.\tag{3}
\]
For \(c<\kappa_m\), the first affine function decreases and the second increases; their unique intersection is \(R=mB/(\kappa_m+mc)\), giving the announced first value. For \(c>\kappa_m\), the second bound strictly decreases with \(R\), so its unique maximizing aggregate is \(R=0\). For \(c=\kappa_m\), the second is constant \(B\) while the first is at least \(B\) precisely if \(0\le R\le mB/[(m+1)\kappa_m]\). This proves the best possible upper bounds and the required aggregate conductance ranges.

**Attainment.** With uniform spoke conductance \(a\) and uniform rim conductance \(b\), the exact Laplacian eigenvalues are
\[
0,\quad (m+1)a,\quad
 a+4b\sin^2(\pi k/m),\quad k=1,\ldots,m-1.\tag{4}
\]
Thus \(\lambda_2=\min\{(m+1)a,a+\kappa_m b\}\). The stated allocations meet their corresponding upper bound (3), including every point of the critical interval. They are global optima.

**Rigidity of every optimizer.** In all three regimes, any global optimum attains the Fourier bound (2): for \(c<\kappa_m\) its aggregates must be the intersection of (1) and (2); for \(c>\kappa_m\) it must have \(R=0\); and for \(c=\kappa_m\) the Fourier bound is \(B/m\) for every budget-exhausting design. Equality in the averaged Rayleigh inequality implies that both \(x\) and \(y\) individually attain the minimum Rayleigh quotient on the orthogonal complement of constants. Hence both are eigenvectors for \(\lambda_2\), and so is their complex combination \(z_j=e^{ij\theta}\), with \(z_0=0\). At rim vertex \(j\), divide the eigen-equation \((Lz)_j=\lambda_2z_j\) by \(z_j\) to obtain
\[
s_j+r_j(1-e^{i\theta})+r_{j-1}(1-e^{-i\theta})=\lambda_2.\tag{5}
\]
Because \(\sin\theta\ne0\) for every \(m\ge3\), its imaginary part forces \(r_j=r_{j-1}\) for every \(j\), and then its real part forces all \(s_j\) equal. Conversely these uniform configurations satisfy the hub eigen-equation, since \(\sum_je^{ij\theta}=0\). Thus no asymmetric optima are hidden by the symmetry reduction, proving the **complete** classification.

**Equal-cost and asymptotic corollaries.** The function \(4\sin^2(\pi/m)\) strictly decreases for integers \(m\ge3\), is greater than one for \(3\le m\le5\), equals one at \(m=6\), and is less than one thereafter. Taylor expansion of \(\sin^2 x\) at zero gives the displayed asymptotic series.

## Verification

Run `python3 verify.py` with a standard Python 3 installation. The executable uses only standard-library `math` and `random`; its deterministic Jacobi eigensolver checks the predicted optimum on \(m=3,\ldots,13\) for several price/budget combinations, tests critical interval points, compares universal Rayleigh bounds on heterogeneous feasible weights, checks the Fourier rigidity forcing under nonuniform rim rates, and checks three exactly known trigonometric cases. An actual replay produced `VERIFY_OK 1279`. These are finite checks, not a substitute for the analytic proof of all \(m,c,B\).

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis (2006) formulate the general fastest-mixing Markov *process* with cost-weighted edge rates as a semidefinite program and solve path/cycle examples. Their general SDP encompasses this instance, but the inspected sections do not give its wheel-specific two-price optimizer, support cutoff, or classification of every asymmetric optimum. Boyd, Diaconis, Parrilo and Xiao (2007/2009), section 5.3.3, explicitly solve fastest mixing on the wheel for a **discrete-time** Markov chain under stochastic-row constraints and optimize SLEM; their Fourier block is a useful precursor but neither their feasible set nor their objective is the present one. Ghosh and Boyd (2006) use symmetry for upper bounds in algebraic connectivity of constrained graph families; this provides a general method rather than the stated independently priced wheel threshold. Previous wheel results optimizing the Kirchhoff index instead minimize resistance and therefore do not imply a maximized spectral-gap allocation. The proof here establishes the two Rayleigh upper bounds and equality rigidity for the claimed cost regime.

## Limitations

The theorem does not classify heterogeneous edge prices within one orbit, directed or normalized-Laplacian diffusion, or discrete-time Markov chains with local row-sum limits. It does not assert that the price threshold is absent from every unindexed source: the literature comparison is bounded to the specifically inspected material. No independent external audit of the mathematical proof has been performed.

## References

1. J. Sun, S. Boyd, L. Xiao and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699; first electronic publication November 2, 2006. DOI: 10.1137/S0036144504443821. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (September 6, 2007), especially section 5.3.3 on discrete-time wheel chains. https://arxiv.org/abs/0709.0955.
3. A. Ghosh and S. Boyd, *Upper Bounds on Algebraic Connectivity via Convex Optimization*, Linear Algebra and its Applications 418 (2006), 693–707; available online May 5, 2006. DOI: 10.1016/j.laa.2006.03.006. Full text: https://www-leland.stanford.edu/~boyd/papers/pdf/eigbounds_laplacian.pdf.
