# Exact Gaussian qubit completion probability and its dimensional collapse

## Finding
For each integer \(d\ge1\), independently sample two \(d\times d\) standard complex Ginibre matrices \(G,H\). Put \(A=GG^*\) and \(B=HH^*\). Let \(\mathcal E_d\) denote the event that **there exists a positive semidefinite** \(C\) for which
\[
(I+mA+nB+mnC)^{-1}=\int_{[0,1]^2}u^m v^n\,dE(u,v),\qquad m,n\in\mathbb N_0,
\]
with a normalized positive operator-valued measure \(E\). Then the *complete dimension law* is
\[
\boxed{\Pr(\mathcal E_d)=\begin{cases}1,&d=1,\\ (24-28\log2)/81,&d=2,\\0,&d\ge3.\end{cases}}
\]
In the qubit case this probability is approximately \(0.05668986351014236\). With probability one, a successful qubit pair has the **unique** completion
\[
C=\|B\|A+\|A\|B-\|A\|\|B\|I.
\]
More finely, given the smaller-to-larger eigenvalue ratios \(r,s\in(0,1)\) for \(A,B\), respectively, the conditional success probability is exactly
\[
\min\!\left\{1,\frac{rs}{(1-r)(1-s)}\right\}.
\]

## Assumptions and scope
All matrix entries of \(G,H\) are independent \(\mathrm{CN}(0,1)\) variables, with squared absolute value of mean one. The random matrices are independent, each is square, the Hilbert space is complex, and dimensions are positive integers. A positive completion means a **single** \(C\ge0\) working simultaneously for **every** nonnegative integer pair of moment indices; pointwise positivity of inverse matrices is insufficient. Almost surely both Wishart matrices are positive definite with simple eigenvalues. Changing the common Gaussian variance does not change any displayed probability. The assertion for \(d\ge3\) is an almost-sure statement for this absolutely continuous ensemble, not a claim that no exceptional higher-dimensional pairs can be completed.

## Proof
**1. The scalar case.** For positive scalars \(a,b\), choose \(C=0\). If \(T\) is an exponential random variable of mean one, the pushforward of its law under \(t\mapsto(e^{-at},e^{-bt})\) is a probability measure on \([0,1]^2\), and
\[
\mathbb E[e^{-maT-nbT}]=\int_0^\infty e^{-(1+ma+nb)t}\,dt=(1+ma+nb)^{-1}.
\]
This proves the case \(d=1\).

**2. Qubit reduction to a random angular test.** Tian's two-dimensional positive-completion theorem [1, Theorem 4.1] says that for noncommuting positive-definite \(2\times2\) matrices the event is equivalent to
\[
A/\|A\|+B/\|B\|\succeq I;
\]
when it holds the displayed formula for \(C\) is the unique completion. Independent complex Wishart matrices almost surely satisfy the noncommuting hypothesis. Write \(r=\lambda_{\min}(A)/\lambda_{\max}(A)\), \(s=\lambda_{\min}(B)/\lambda_{\max}(B)\), and let \(P,Q\) project onto the respective top eigenspaces. Then
\[
D=A/\|A\|+B/\|B\|-I=(r+s-1)I+(1-r)P+(1-s)Q.
\]
If \(U=\operatorname{tr}(PQ)=|\langle v,w\rangle|^2\), direct calculation gives
\[
\operatorname{tr}D=r+s>0,\qquad
\det D=rs-(1-r)(1-s)U.
\]
Because \(D\) is Hermitian of order two with positive trace, \(D\succeq0\) is equivalent to \(\det D\ge0\). Unitary invariance of complex Wishart matrices makes their top-eigenvector lines independent Haar-uniform complex lines, independently of \(r,s\). For two such lines in complex dimension two, \(U\) is uniform on \([0,1]\). Therefore
\[
\Pr(\mathcal E_2\mid r,s)=\min\!\left\{1,\frac{rs}{(1-r)(1-s)}\right\}.
\]

**3. Exact spectral-ratio integration.** The ordered positive eigenvalues \(L>l\) of a square \(2\times2\) complex Wishart matrix have joint density proportional to \((L-l)^2 e^{-(L+l)}\). Put \(l=rL\), whose Jacobian is \(L\). Integrating \(L\) out, then normalizing, yields
\[
f_R(r)=\frac{6(1-r)^2}{(1+r)^4},\qquad 0<r<1.
\]
For \(T=R/(1-R)\), the density is \(f_T(t)=6/(1+2t)^4\), \(t>0\). The independent odds ratios \(T_1,T_2\) therefore satisfy
\[
\Pr(\mathcal E_2)=\int_0^\infty\!\!\int_0^\infty
 \frac{36\min(1,ts)}{(1+2t)^4(1+2s)^4}\,ds\,dt.
\]
Splitting the inner integral at \(s=1/t\) gives exactly
\[
\int_0^\infty\frac{6\min(1,ts)}{(1+2s)^4}\,ds
=\frac{t(t+1)}{(t+2)^2}.
\]
Thus
\[
\Pr(\mathcal E_2)=\int_0^\infty
 \frac{6t(t+1)}{(2t+1)^4(t+2)^2}\,dt
=\frac{24-28\log 2}{81}.
\]
For an exact reproducible evaluation, decompose the last integrand as
\[
-\frac{28}{81(2t+1)}+\frac4{9(2t+1)^2}+\frac4{9(2t+1)^3}
-\frac2{3(2t+1)^4}+\frac{14}{81(t+2)}+\frac4{27(t+2)^2}.
\]
The logarithmic divergences of the first and fifth terms cancel; integrating the full expression from zero to infinity gives the displayed constant.

**4. Higher-dimensional collapse.** Fix \(d\ge3\). With probability one, the spectra of \(A\) and \(B\) are simple and the bottom eigenvector \(p\) of \(B\) is cyclic for \(A\) (all its components in an eigenbasis of \(A\) are nonzero). Under these hypotheses, [1, Theorem 5.1, equation (5.3)] implies that if any positive completion exists, then for \(a=\lambda_{\min}(A)\), the bottom eigenvector \(q\) of \(A\), and some \(\gamma>0\),
\[
(A-aI)^{1/2}(B-bI)(A-aI)^{1/2}=\gamma(I-qq^*),
\]
where \(b=\lambda_{\min}(B)\). Diagonalize \(A\) and take \(q=e_1\). At matrix coordinate \((2,3)\), the identity forces
\[
\sqrt{(\lambda_2-a)(\lambda_3-a)}\,B_{23}=0,
\]
so \(B_{23}=0\). Conditional on \(A\), the independent Wishart \(B\) has an everywhere positive density on the cone of positive-definite Hermitian matrices. Its off-diagonal entry \(B_{23}\) has a continuous two-real-dimensional distribution and is zero with probability zero. Hence \(\Pr(\mathcal E_d)=0\) for every \(d\ge3\).

## Verification
The spectral-ratio density integrates to one. The inner conditional integral and the rational partial fractions are algebraic identities, independently checked by exact rational arithmetic at selected rational arguments, and numerical integration matches the logarithmic constant. A deterministic seeded simulation of independently generated complex \(2\times2\) Ginibre matrices checks the original matrix-inequality event, not merely the reduced integral. Run the attached standard-library `CHECKER.py`; its diagnostics are supplementary and do not replace the analytical calculation. The higher-dimensional zero-probability assertion follows from an explicit off-diagonal necessary condition and the Wishart density, not from numerical nonoccurrence.

## Relationship to prior work
Tian [1] supplies the noncommuting \(2\times2\) completion criterion, uniqueness, and the higher-dimensional spectral necessary condition; **these source results are not claimed as new**. The contribution is the exact Gaussian success probability and the fully quantified, ensemble-specific dimension law. Independent complex-Wishart eigenvalue statistics are classical. Previous work on spectra of sums and differences of Wishart matrices [2,3] studies related random matrix combinations, but its accessible descriptions do not give this *spectral-norm-normalized, simultaneous positive Hausdorff completion* probability. The result is not a statement about the ordinary sum of two unnormalized Wishart matrices or about positive eigenvalues alone.

## Limitations
The logarithmic probability is specific to independent *square* complex Ginibre factors and does not cover real, rectangular, correlated or noncentral Wishart ensembles. The almost-sure obstruction for \(d\ge3\) permits exceptional deterministic pairs. The computation does not give a conditional distribution of the completing matrix \(C\), nor does it address the numerical stability of constructing its representing measure. Absolute literature uniqueness is not certified, and no independent audit has been performed.

## References
[1] James Tian, *Joint Moments of Bilinear Resolvents*, arXiv:2611.03081v1, publicly submitted 2026-11-02, especially Theorems 4.1 and 5.1 and Corollary 5.2; https://arxiv.org/abs/2611.03081.

[2] S. Kumar, G. F. Pivaro, G. Fraidenraich, C. F. Dias, *On the Exact and Approximate Eigenvalue Distribution for Sum of Wishart Matrices*, arXiv:1504.00222 (2015); https://arxiv.org/abs/1504.00222.

[3] Santosh Kumar and S. Sai Charan, *Spectral statistics for the difference of two Wishart matrices*, arXiv:2011.07362 (2020); https://arxiv.org/abs/2011.07362.
