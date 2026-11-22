# Universal covariance phase diagram for projectively stretched spherical-Dirichlet vectors

## Finding

Let \(p\geq3\), let \(\alpha_1,\ldots,\alpha_p>0\), and partition the coordinates into nonempty blocks \(I,J\), with \(|I|\geq2\). Let \(Z\sim\operatorname{Dirichlet}(\alpha_1,\ldots,\alpha_p)\) and \(X_i=\sqrt{Z_i}\). For a scale ratio \(r>0\), define a positive-sphere random vector by

\[
Y_i^{(r)}=\begin{cases}
\displaystyle\frac{X_i}{\sqrt{\sum_{k\in I}X_k^2+r\sum_{k\in J}X_k^2}},&i\in I,\\[5pt]
\displaystyle\frac{\sqrt r\,X_i}{\sqrt{\sum_{k\in I}X_k^2+r\sum_{k\in J}X_k^2}},&i\in J.
\end{cases}
\]

Set \(A=\sum_{i\in I}\alpha_i\) and \(T=\sum_{j\in J}\alpha_j\). For \(a,t>0\), define the scalar function and constant

\[
W_{a,t}(r)=\frac{B}{B+r(1-B)},\qquad B\sim\operatorname{Beta}(a,t),
\]
\[
Q_{a,t}(r)=\frac{\mathbb E W_{a,t}(r)}{(\mathbb E\sqrt{W_{a,t}(r)})^2},\qquad
K_a=\frac{a\,\Gamma(a)^2}{\Gamma(a+1/2)^2}.
\]

For **every** \(a,t>0\), the equation \(Q_{a,t}(r)=K_a\) has one and only one solution \(R(a,t)\), and \(R(a,t)>1\). Define two boundaries

\[
r_{-}=\frac{1}{R(T,A)}<1<r_{+}=R(A,T).
\]

The entire off-diagonal covariance sign pattern is then:

- For distinct \(i,j\in I\), \(\operatorname{Cov}(Y_i^{(r)},Y_j^{(r)})\) is negative for \(r<r_{+}\), zero exactly at \(r=r_{+}\), and positive for \(r>r_{+}\).
- For distinct \(i,j\in J\), when this pair exists, the covariance is positive for \(r<r_{-}\), zero exactly at \(r=r_{-}\), and negative for \(r>r_{-}\).
- For \(i\in I\) and \(j\in J\), the covariance is strictly negative for **every** finite \(r>0\).

In particular all off-diagonal covariances are strictly negative on \(r_{-}<r<r_{+}\). Each critical scale depends only on the **total shape in each block**, regardless of individual shapes or the number of coordinates. If a block has only one coordinate, its within-block pair statement is vacuous.

For the area-uniform law on the positive orthant of the unit sphere in \(\mathbb R^4\), take all four shapes equal to \(1/2\) and two coordinates per block. The two boundaries are approximately

\[
r_{-}=0.234848401276\ldots,\qquad r_{+}=4.258066031391\ldots.
\]

## Assumptions and scope

All shape parameters are strictly positive. Each scale \(r\) is finite and strictly positive. The direction is obtained by anisotropic rescaling followed by Euclidean normalization of the *original* spherical-Dirichlet vector; it is not an area-uniform law on an ellipsoid, nor is it in general the projection of independent untransformed Gamma variables. Covariances refer to coordinate values \(Y_i^{(r)}\), not their squares. At \(r=1\), the law reduces to the ordinary spherical-Dirichlet law.

## Proof

**1. Block factorization.** Let \(G_1,\ldots,G_p\) be independent \(\operatorname{Gamma}(\alpha_i,1)\) variables and write \(H=\sum_{i\in I}G_i\), \(L=\sum_{j\in J}G_j\). Then \(H\sim\operatorname{Gamma}(A,1)\), \(L\sim\operatorname{Gamma}(T,1)\), independently. The within-block proportions \(P_i=G_i/H\) for \(i\in I\) and \(S_j=G_j/L\) for \(j\in J\) are independent of \((H,L)\) and of each other. With

\[
W=\frac{H}{H+rL}=W_{A,T}(r),
\]

we have \(Y_i^{(r)}=\sqrt{P_i}\sqrt W\) for \(i\in I\) and \(Y_j^{(r)}=\sqrt{S_j}\sqrt{1-W}\) for \(j\in J\).

For distinct \(i,j\in I\), put \(c_i=\Gamma(\alpha_i+1/2)/\Gamma(\alpha_i)>0\). The Dirichlet moment identities give

\[
\mathbb E\sqrt{P_i}=c_i\frac{\Gamma(A)}{\Gamma(A+1/2)},\qquad
\mathbb E(\sqrt{P_iP_j})=\frac{c_ic_j}{A}.
\]

Consequently, with \(m_s(r)=\mathbb E W^s\),

\[
\operatorname{Cov}(Y_i^{(r)},Y_j^{(r)})
=\frac{c_ic_j}{A}\,m_{1/2}(r)^2\bigl(Q_{A,T}(r)-K_A\bigr).
\tag{1}
\]

All factors outside the parentheses are positive. The same calculation on \(J\), noting that \(1-W\) has the law \(W_{T,A}(1/r)\), proves the analogous statement with \((A,T,r)\) replaced by \((T,A,1/r)\).

**2. Strict monotonicity of the scalar criterion.** Put \(V=L/H\); it has a continuous nondegenerate density on \((0,\infty)\), and \(W=(1+rV)^{-1}\). For every \(s>0\), differentiation under the integral for finite \(r>0\) gives

\[
\frac{d m_s}{dr}=-\frac{s}{r}(m_s-m_{s+1}).
\]

The strict Hölder inequality makes \(s\mapsto\log m_s\) strictly convex, as \(W\) is nonconstant. Hence the moment ratio \(m_{s+1}/m_s\) increases strictly with \(s\). Therefore

\[
\frac{d}{dr}\log Q_{A,T}(r)=\frac1r\left(
\frac{m_2(r)}{m_1(r)}-\frac{m_{3/2}(r)}{m_{1/2}(r)}
\right)>0.
\tag{2}
\]

Thus \(Q_{A,T}\) is continuous and strictly increasing on \((0,\infty)\).

**3. The threshold is greater than one.** The strict log-convexity of the Gamma function gives \(K_a>1\) for every \(a>0\). As \(r\downarrow0\), \(W\uparrow1\) and dominated convergence gives \(Q_{A,T}(r)\to1<K_A\). At \(r=1\), \(W\sim\operatorname{Beta}(A,T)\), and direct beta moments show

\[
Q_{A,T}(1)=\frac{K_A}{K_{A+T}}<K_A.
\tag{3}
\]

**4. The large-scale endpoint exceeds the threshold.** The ratio \(V=L/H\) has beta-prime density

\[
f_V(v)=\frac{v^{T-1}}{\mathrm B(T,A)(1+v)^{A+T}},\qquad v>0.
\]

For every fixed \(s>0\), change of variables and dominated convergence (with an intermediate logarithmic estimate at equality) yield the following full asymptotic trichotomy:

\[
m_s(r)\sim\begin{cases}
\displaystyle r^{-s}\frac{\mathrm B(T-s,A+s)}{\mathrm B(T,A)},&T>s,\\[6pt]
\displaystyle\frac{r^{-s}\log r}{\mathrm B(T,A)},&T=s,\\[6pt]
\displaystyle r^{-T}\frac{\mathrm B(T,s-T)}{\mathrm B(T,A)},&T<s.
\end{cases}
\tag{4}
\]

To justify the first case, multiply \((1+rV)^{-s}\) by \(r^s\) and dominate by \(V^{-s}\), integrable when \(T>s\). For the last case, substitute \(u=rV\) and dominate by \(u^{T-1}(1+u)^{-s}/\mathrm B(T,A)\), integrable when \(T<s\). At equality, split the integral into \((0,1/r)\), \((1/r,1)\), and \((1,\infty)\); the middle term is \((\log r)/[\mathrm B(T,A)r^T]\) with a lower-order remainder, and the other pieces are \(O(r^{-T})\).

If \(T>1\), applying (4) with \(s=1\) and \(s=1/2\) gives

\[
\lim_{r\to\infty}Q_{A,T}(r)=K_A\frac{\Gamma(T)\Gamma(T-1)}{\Gamma(T-1/2)^2}>K_A,
\]

again by strict Gamma log-convexity. If \(0<T\le1\), the same trichotomy shows \(Q_{A,T}(r)\to\infty\): for \(0<T<1/2\) it grows on the scale \(r^T\), for \(T=1/2\) on \(r^{1/2}/(\log r)^2\), for \(1/2<T<1\) on \(r^{1-T}\), and for \(T=1\) on \(\log r\). Therefore the endpoint is strictly above \(K_A\) for every \(T>0\). By (2), (3), and continuity, exactly one crossing \(R(A,T)>1\) exists.

**5. The other block and cross-block pairs.** Swapping the blocks sends \(r\) to \(1/r\), so the unique opposite threshold is \(r_{-}=1/R(T,A)<1\). For \(i\in I,j\in J\), independent proportions give

\[
\operatorname{Cov}(Y_i^{(r)},Y_j^{(r)})=
\mathbb E\sqrt{P_i}\,\mathbb E\sqrt{S_j}\,
\operatorname{Cov}(\sqrt W,\sqrt{1-W}).
\]

The last covariance is strictly negative because \(W\) is nondegenerate, \(w\mapsto\sqrt w\) is strictly increasing, and \(w\mapsto\sqrt{1-w}\) is strictly decreasing: with an independent copy \(W'\), twice the covariance is the strictly negative expectation of \((\sqrt W-\sqrt{W'})(\sqrt{1-W}-\sqrt{1-W'})\). Combining these three pair classes proves the entire diagram.

## Verification

The accompanying `verify_covariance.py` evaluates the defining beta integrals at 45 decimal-digit precision and performs 96 deterministic numerical assertions: derivative signs, critical-scale bracketing, crossing behavior, and the three covariance classes in a four-dimensional area-uniform example. Running `python verify_covariance.py` with `mpmath` installed reproduces the checked numbers, including \(R(1,1)=4.2580660313911513\ldots\). Independent direct Gamma simulation also agreed with the signs at representative parameters; sampling was not used for proof. Statements (1)–(4) and the final order argument, rather than finite checks, establish the theorem for all positive shapes and scales.

## Relationship to prior work

Guardiola's spherical-Dirichlet moment formula proves strict negative covariance at the undeformed scale \(r=1\); it does not give the signs after blockwise projective deformation. The 2020 original paper has the same undeformed distribution. The mixed-scaled Dirichlet literature contains examples of positive correlation among **squared coordinate proportions** with unequal Gamma scales; these examples neither determine the two critical scales for square-root coordinate directions nor provide their all-shape uniqueness. Projected-Gamma directional models normalize the Gamma variables themselves, rather than their coordinatewise square roots. Work on other hyperspherical extensions likewise permits positive covariance, but its available abstract does not imply this complete two-block sign diagram.

The theorem therefore claims the exact universal phase diagram for the specified deformation, not invention of positive correlation in general or a full theory of every anisotropically scaled law.

## Limitations

The thresholds are given implicitly by a one-dimensional beta expectation, not by elementary closed formulas for arbitrary shapes. No claim is made for arbitrary independently chosen scales on every coordinate, dependence among the underlying Gamma variables, zero shape parameters, uniform ellipsoidal area measure, or the magnitudes of the eigenvalues of the covariance matrix. A related 2024 dissertation was accessible only through its bibliographic abstract, so historical-priority uncertainty remains despite the mathematical comparisons. The analysis is a proof of the stated theorem, not independent external validation.

## References

1. J. H. Guardiola, *On the Spherical-Dirichlet Distribution: Corrections and Results*, arXiv:2506.04441. First public version 2025-06-04; version 2, 2026-10-28. https://arxiv.org/html/2506.04441v2
2. J. H. Guardiola, *The spherical-Dirichlet distribution*, Journal of Statistical Distributions and Applications 7, article 6 (2020). https://doi.org/10.1186/s40488-020-00106-9
3. E. Furman, Y. Kye, and J. Su, *A Reconciliation of the Top-Down and Bottom-Up Approaches to Risk Capital Allocations: Proportional Allocations Revisited* (2019), section on mixed-scaled Dirichlet distributions and Note 5. https://www.soa.org/globalassets/assets/files/resources/research-report/2019/reconciliation-top-down.pdf
4. E. Geneyro and G. Núñez-Antonio, *A Bayesian nonparametric model for bounded directional data on the positive orthant of the unit sphere*, Journal of Applied Statistics 51 (2024), 721–739; online 2022-12-14. https://doi.org/10.1080/02664763.2022.2156485
5. R. L. Leshilo, *Hypersphere candidates emanating from the Dirichlet and its extension*, MSc dissertation, University of Pretoria (2024). Bibliographic abstract: https://repository.up.ac.za/items/5125d936-e337-4736-a180-feb23c345d47
6. S. Lakhani, *The Scaled Dirichlet Distribution: Lauricella Representations and Estimation*, arXiv:2611.25136v1 (2026-11-18), Section 3. https://arxiv.org/html/2611.25136v1
