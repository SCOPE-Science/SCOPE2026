# Exact four-mode diagonal preconditioning for two-community correlation matrices

## Finding

For positive-definite, two-community compound-symmetry correlation matrices, the spectral-condition-number-optimal **unrestricted diagonal congruence preconditioner** can be chosen constant on each community. The optimal relative scale has a completely explicit clipped formula with three possible governing spectral mechanisms: balancing the two quotient eigenmodes, balancing the within-group modes, or a collision of the lower quotient eigenvalue with a within-group eigenvalue.

Set
\[
\alpha=1+(m-1)u,\quad \beta=1+(n-1)v,\quad a=1-u,\quad b=1-v,\quad \Delta=mn g^2.
\]
Define \(x_0=\beta/\alpha\), \(x_c=b/a\), and \(\operatorname{clip}(z;l,r)=\min\{r,\max\{l,z\}\}\). The globally optimal ratio of squared community scales is
\[
x_* = \begin{cases}
\operatorname{clip}\!\left(\dfrac{\beta-\Delta/(\alpha-a)}a;x_0,x_c\right),&x_0\le x_c,\\[6pt]
\operatorname{clip}\!\left(\dfrac{b(\beta-b)}{\alpha(\beta-b)-\Delta};x_c,x_0\right),&x_0>x_c\text{ and }\alpha(\beta-b)>\Delta,\\[6pt]
x_0,&x_0>x_c\text{ and }\alpha(\beta-b)\le\Delta.
\end{cases}
\]
In particular \(D_*=\operatorname{diag}(\sqrt{x_*}I_m,I_n)\) attains the global minimum over **all** positive diagonal \(D\), not merely community-constant scalings. Its condition number is
\[
\kappa_* = \frac{\lambda_+(x_*)}{\min\{a x_*,b,\lambda_-(x_*)\}},\qquad
\lambda_\pm(x)=\frac{\alpha x+\beta\pm\sqrt{(\alpha x-\beta)^2+4\Delta x}}2.
\]
For \(g>0\), the optimal relative squared scale \(x_*\) is unique within the block-constant family; no uniqueness of arbitrary entrywise scalings is asserted.

## Assumptions and scope

Take integers \(m,n\ge2\); real within-community correlations \(0<u,v<1\); and \(g>0\). The matrix \(A\) has diagonal entries one, off-diagonal entries \(u\) in the first \(m\)-coordinate group and \(v\) in the other \(n\)-coordinate group, and every cross-group entry equal to \(g\). Assume \(\Delta<\alpha\beta\). These conditions make \(A\) real symmetric positive definite. All diagonal preconditioners considered are strictly positive (allowing arbitrary individual weights), and their objective is the ratio \(\kappa_2(DAD)=\lambda_{\max}(DAD)/\lambda_{\min}(DAD)\), where \(D\) is a positive diagonal matrix.

## Proof

**1. Reduction from unrestricted diagonal scaling.** For \(\kappa\ge1\), there exists positive diagonal \(D\) with \(\kappa_2(DAD)\le\kappa\) if and only if there exists positive diagonal \(W\) such that \(W\preceq A\preceq\kappa W\). In one direction put \(W=\lambda_{\min}(DAD)D^{-2}\); in the other put \(D=W^{-1/2}\). The feasibility inequalities are affine in \(W\). For each within-community permutation \(P\), \(PAP^T=A\); hence averaging a feasible \(W\) over the within-group permutation group preserves feasibility and produces a positive diagonal matrix constant within each group. Thus the infimum over all diagonal scalings equals the infimum over \(D(x)=\operatorname{diag}(\sqrt{x}I_m,I_n)\), \(x>0\), and the resulting attained optimum is globally optimal.

**2. Exact four-mode spectrum.** The within-group zero-sum subspaces have eigenvalues \(a x\) and \(b\), of multiplicities \(m-1\) and \(n-1\). On the normalized two-group indicator vectors the matrix \(D(x)AD(x)\) reduces to
\[
B(x)=\begin{pmatrix}\alpha x&\sqrt{\Delta x}\\\sqrt{\Delta x}&\beta\end{pmatrix}.
\]
Its eigenvalues are \(\lambda_\pm(x)\). Because \(\Delta>0\) and all entries are positive, \(\lambda_+(x)>\max\{\alpha x,\beta\}>\max\{a x,b\}\); thus the largest eigenvalue is always \(\lambda_+\), and
\[
\kappa(x)=\max\left\{\frac{\lambda_+(x)}{\lambda_-(x)},\frac{\lambda_+(x)}{ax},\frac{\lambda_+(x)}b\right\}.
\]

**3. Three monotonicity facts.** The first term \(f_0\) strictly decreases until \(x_0=\beta/\alpha\) and strictly increases afterward. Indeed, for the positive two-by-two matrix \(B(x)\), its eigenvalue ratio is strictly increasing with \((\operatorname{tr} B)^2/\det B=(\alpha x+\beta)^2/[x(\alpha\beta-\Delta)]\), whose unique minimum is at \(x_0\). The term \(f_1=\lambda_+(x)/(ax)\) strictly decreases: it equals \(1/a\) times the Perron eigenvalue of the positive matrix \(\bigl(\begin{smallmatrix}\alpha&\sqrt{\Delta/x}\\\sqrt{\Delta/x}&\beta/x\end{smallmatrix}\bigr)\), which decreases entrywise as \(x\) grows. Likewise \(f_2=\lambda_+(x)/b\) strictly increases because \(B(x)\) increases entrywise. Finally \(f_1\ge f_2\) exactly when \(x\le x_c=b/a\).

**4. Locating the global minimum.** If \(x_0\le x_c\), the objective decreases for \(x<x_0\), increases for \(x>x_c\), and on \([x_0,x_c]\) equals the maximum of the decreasing \(f_1\) and increasing \(f_0\). Their equality is equivalent to \(\lambda_-(x)=a x\). Substitution in the characteristic polynomial of \(B(x)\) gives \((\alpha-a)(\beta-a x)=\Delta\), so the unique crossing, if inside the interval, is \((\beta-\Delta/(\alpha-a))/a\). Clipping this crossing to \([x_0,x_c]\) gives the stated unique minimum.

If \(x_0>x_c\), the objective on \([x_c,x_0]\) is the maximum of decreasing \(f_0\) and increasing \(f_2\). Their crossing requires \(\lambda_-(x)=b\), equivalent to \(x[\alpha(\beta-b)-\Delta]=b(\beta-b)\). When the bracket is positive, clipping the resulting crossing to \([x_c,x_0]\) gives the unique minimum. When it is nonpositive, no positive crossing occurs and \(f_0>f_2\) everywhere, so the unique minimum is \(x_0\). This proves the formula and the specified global optimality.

**5. Exact four-coordinate example.** For \(m=n=2\), \(u=3/10\), \(v=3/5\), \(g=1/2\), the matrix is positive definite. One finds \(x_0=16/13\), \(x_c=4/7\), and \(x_*=6/7\). The optimized eigenvalues, with multiplicity, are \(2/5,2/5,3/5,81/35\); hence \(\kappa_*=81/14\). Unscaled Jacobi normalization gives \(\kappa_\mathrm{Jacobi}=(29+\sqrt{409})/8>81/14\). The two repeated smallest eigenvalues arise from different subspaces (a community fluctuation and the quotient), exhibiting the eigenmode collision mechanism.

## Verification

The standalone `check_preconditioning.py` reproduces the determinant-factorization of the four-dimensional rational example at five distinct rational evaluation points, checks the exact optimized spectrum and condition number, and compares the formula against direct one-variable spectral minimization on 3,000 reproducibly generated admissible parameter sets with different community sizes. Its numerical checks are tests rather than proof of the infinite family: the proof above establishes global optimality analytically. Run with `python check_preconditioning.py` using only the Python standard library.

## Relationship to prior work

Optimal diagonal scaling of positive-definite matrices has general convex and semidefinite formulations; in particular Jambulapati et al. [1] study near-optimal diagonal preconditioning and Qu et al. [2] develop optimization algorithms. This result is not a claim of a new general-purpose preconditioning algorithm. Its proposed distinction is an explicit, all-parameter, constructive classification for the two-community compound-symmetry model, where within-group fluctuation modes compete with the group-average quotient. Older work includes block-optimality conditions [3] and a complete three-by-three scaling classification [4]. The latter does not directly settle the present four-mode problem for groups of sizes at least two, although alternate deductions from general scaling theory remain possible.

## Limitations

Only positive within-community and positive cross-community correlations are included, with both communities of size at least two. Optimality concerns spectral condition number under positive diagonal congruence scaling; no assertions are made for indefinite matrices, nonsymmetric systems, arbitrary block structure, actual iterative-solver runtime, or uniqueness of every nonuniform optimum. General optimal-scaling criteria from the older literature can potentially yield alternate proofs; publication precedence is not independently certified.

## References

[1] A. Jambulapati, J. Li, C. Musco, A. Sidford, and K. Tian, *Fast and Near-Optimal Diagonal Preconditioning*, first posted 2020-08-04, https://arxiv.org/abs/2008.01722.

[2] Z. Qu, W. Gao, O. Hinder, Y. Ye, and Z. Zhou, *Optimal Diagonal Preconditioning*, first posted 2022-09-02, https://arxiv.org/abs/2209.00809.

[3] L. Yu. Kolotilina, *Optimally conditioned block matrices*, Linear Algebra and Its Applications 340 (2002), 55–67, https://doi.org/10.1016/S0024-3795(01)00412-8.

[4] L. Yu. Kolotilina, *Solution of the Problem of Optimal Diagonal Scaling for Quasireal Hermitian Positive-Definite 3×3 Matrices*, Journal of Mathematical Sciences 132 (2006), 190–213, https://doi.org/10.1007/s10958-005-0488-1.

[5] J. Demmel, *Nearly Optimal Block-Jacobi Preconditioning*, SIAM Journal on Matrix Analysis and Applications 44 (2023), 408–413, https://doi.org/10.1137/22M1504901.
