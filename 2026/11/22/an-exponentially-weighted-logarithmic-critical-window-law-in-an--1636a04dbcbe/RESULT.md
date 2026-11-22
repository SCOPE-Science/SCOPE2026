# An exponentially weighted logarithmic critical-window law in an immigration host-parasitoid map

## Finding

An immigration-driven host–parasitoid map develops a universal second-order clock on the \(1/N\) detuning scale of its transcritical bifurcation. Fix \(0<\alpha<1\), \(\lambda\in\mathbb R\), and positive initial densities \(x_0,y_0\) independent of the integer \(N\). For each sufficiently large \(N\), keep the parameter \(\beta_N\) fixed for all iterates of **that** experiment:
\[
 x_{n+1}=\alpha x_ne^{-y_n}+\beta_N,\qquad
 y_{n+1}=\alpha x_n(1-e^{-y_n}),\qquad
 \beta_N=\frac{1-\alpha}{\alpha}+\frac{\lambda}{N}.
\]
Define
\[
 c=\frac{\alpha}{1-\alpha},\quad
 a=\frac{1+\alpha}{2(1-\alpha)},\quad
 B=\frac{1+3\alpha+9\alpha^2-\alpha^3}{6(1-\alpha)^2(1+\alpha)}>0,
\]
and, for \(t>0\),
\[
 U_\lambda(t)=a\int_0^t e^{-c\lambda s}\,ds=
 \begin{cases}a(1-e^{-c\lambda t})/(c\lambda),&\lambda\ne0,\\at,&\lambda=0.\end{cases}
\]
Then for every fixed compact interval \([\varepsilon,T]\subset(0,\infty)\),
\[
 \boxed{\frac1{y_{\lfloor Nt\rfloor}}=N U_\lambda(t)+ B e^{-c\lambda t}\log N+O_{\alpha,\lambda,x_0,y_0,\varepsilon,T}(1)}
\]
uniformly in \(t\in[\varepsilon,T]\). Consequently, uniformly on these intervals,
\[
 Ny_{\lfloor Nt\rfloor}\longrightarrow U_\lambda(t)^{-1},\qquad
 N(x_{\lfloor Nt\rfloor}-1/\alpha)\longrightarrow\frac{\lambda-U_\lambda(t)^{-1}}{1-\alpha}.
\]
This identifies both the leading near-critical crossover and the exponential weighting of its logarithmic finite-horizon correction. In particular, the logarithmic coefficient is independent of positive initial densities.

## Assumptions and scope

All parameters \(\alpha,\lambda,x_0,y_0\) and the compact positive-time window are fixed as \(N\to\infty\); the initial densities are strictly positive, and \(\beta_N>0\) for all sufficiently large \(N\). The asymptotic is for integer iterates \(n=\lfloor Nt\rfloor\), with a uniform bounded remainder, not a claim of convergence for the bounded residual. The fast host transient is included: initial states need not lie on any slow invariant manifold.

## Proof

**1. Entry into a uniform small neighborhood.** Write \(\mu=\lambda/N\), \(R_\mu=\beta_N/(1-\alpha)=1/\alpha+\mu/(1-\alpha)\), and \(h_n=x_n-R_\mu\). At \(\mu=0\), \(x_{n+1}\le\alpha x_n+\beta_0\) implies \(\limsup x_n\le1/\alpha\); for each \(\eta>0\), eventually \(x_n\le1/\alpha+\eta\). Hence \(y_{n+1}\le(1+\alpha\eta)(1-e^{-y_n})\). Comparison with this increasing scalar map, whose unique positive fixed point tends to zero as \(\eta\downarrow0\), gives \(y_n\to0\); then \(x_n\to1/\alpha\) follows from the first recurrence. By continuity of finitely many iterates, for all sufficiently large \(N\) the solution is in any chosen small neighborhood of \((h,y)=(0,0)\) by one fixed index \(n_0\), independent of \(N\). The local positive quadrant in that neighborhood is forward-trapped during \(n\le NT\): this follows from the ratio estimates below and the negative quadratic coefficient \(a\), after choosing the neighborhood small and \(N\) large.

**2. Exact fast-coordinate identity and slow jet.** The sum of the original equations gives the exact identity
\[
 h_{n+1}=\alpha h_n-y_{n+1},\qquad
 y_{n+1}=(1+c\mu+\alpha h_n)(1-e^{-y_n}).
\]
Let \(H(y)=py+qy^2\), where
\[
 p=-\frac1{1-\alpha},\qquad q=-\frac{\alpha(1+\alpha)}{2(1-\alpha)^3}.
\]
Substitution into the preceding identities and Taylor expansion gives, uniformly for small positive \(y\) and \(|\mu|\),
\[
 Y(y,\mu)=(1+c\mu+\alpha H(y))(1-e^{-y})
 =y+c\mu y-a y^2+b y^3+O(y^4+|\mu|y^2),
\]
where
\[
 b=\frac{1-6\alpha^2-\alpha^3}{6(1-\alpha)^3}.
\]
The quadratic polynomial has an invariance defect
\[
 H(Y(y,\mu))-[\alpha H(y)-Y(y,\mu)]
 =O(y^3+|\mu|y).
\]
Defining \(e_n=h_n-H(y_n)\), direct subtraction (including the variation of \(H(y_{n+1})\)) gives
\[
 |e_{n+1}|\le (\alpha+C y_n)|e_n|+C\bigl(y_n^3+|\mu|y_n\bigr).
\]
The coefficient is **not** exactly \(\alpha e^{-y_n}\): differentiating the polynomial graph adds \(O(y_n)e_n\), which is included here. To establish uniform trapping and ratio bounds independently, put \(z_n=h_n/y_n\) and \(r_n=y_{n+1}/y_n\). The exact relation gives \(z_{n+1}=(\alpha/r_n)z_n-1\), while \(r_n=(1+c\mu+\alpha y_nz_n)(1-e^{-y_n})/y_n\). Along the critical base trajectory, \(r_n\to1\) and this contractive affine equation implies \(z_n\to p\). Thus one can choose a fixed entry index so \(y_n\) is small and \(z_n\) is close to \(p\) there. For all sufficiently small \(|\mu|\), the wedge \(|z-p|\le\delta\), \(0<y\le\delta\) is preserved for \(n\le NT\): its \(z\)-update contracts about \(p\), and within the wedge \(r_n\le 1+C/N-c_1y_n\) for some \(c_1>0\). In particular, comparison with \(r_n\ge1-C/N-c_2y_n\) gives constants \(C,c>0\) with \(c(n+1)\le1/y_n\le C(n+1)\) through \(n\le NT\). This establishes local trapping and the reciprocal bounds without using a higher-order expansion.

Choose the wedge small enough that \(\alpha+C\delta<1\) and all \(r_n\in[1-\delta,1+\delta]\), with \((\alpha+C\delta)(1-\delta)^{-3}<1\). The geometric convolution of the preceding error inequality gives
\[
 |e_n|\le C\bigl(y_n^3+|\mu|y_n+\vartheta^{n-n_0}\bigr),\qquad \alpha<\vartheta<1,
\]
uniformly for \(n_0\le n\le NT\). The initial term has a fixed finite prefactor. This is a *finite-window* stable-slaving estimate; no assertion of globally defined center manifolds is required.

**3. Reciprocal clock and its bounded error.** Put \(u_n=1/y_n\). The wedge comparison above already proves \(u_n\asymp n+1\) for \(n_0\le n\le NT\), with constants depending on \(T\).

Expanding the reciprocal of \(y_{n+1}\) using Step 2 and \(u_n\asymp n+1\) gives
\[
 u_{n+1}=\left(1-\frac{c\lambda}{N}\right)u_n+a+\frac{d}{u_n}+E_{n,N},\qquad d=a^2-b,
\]
with a uniform bound
\[
 |E_{n,N}|\le C\left(\frac1{u_n^2}+\frac1N+\frac{u_n}{N^2}+\vartheta^{n-n_0}u_n\right).
\]
Consequently \(\sum_{n=n_0}^{\lfloor NT\rfloor}|E_{n,N}|=O_T(1)\). In addition, this recurrence implies the rough but uniform expansion
\[
 u_n=an+O_T\bigl(1+n^2/N+\log(n+1)\bigr),
\]
so
\[
 \sum_{j=n_0}^{\lfloor NT\rfloor}\left|\frac1{u_j}-\frac1{aj}\right|=O_T(1).
\]
These statements include all initial fast-transient contributions as bounded sums.

**4. Weighted summation.** Put \(r_N=1-c\lambda/N\); it is positive for sufficiently large \(N\). Variation of constants gives
\[
 u_n=r_N^{n-n_0}u_{n_0}
 +a\sum_{j=n_0}^{n-1}r_N^{n-1-j}
 +d\sum_{j=n_0}^{n-1}\frac{r_N^{n-1-j}}{u_j}+O_T(1).
\]
The middle sum equals \(N U_\lambda(n/N)+O_T(1)\). For \(n=\lfloor Nt\rfloor\) with \(\varepsilon\le t\le T\), replacing \(u_j^{-1}\) by \((aj)^{-1}\) changes the last sum by only \(O_T(1)\). Moreover
\[
 \sum_{j=n_0}^{n-1}\frac{r_N^{n-1-j}}j
 =e^{-c\lambda t}\log N+O_{\varepsilon,T}(1),
\]
since \(r_N^{n-1-j}=e^{-c\lambda t}+O_T((j+1)/N)\) and \(\sum_{j\le NT}((j+1)/N)/j=O_T(1)\). Therefore the logarithmic coefficient is \(d/a=(a^2-b)/a\), which simplifies to the stated \(B\). Replacing \(n/N\) by \(t\) affects the leading term by \(O_T(1)\).

**5. Host scaling.** From \(h_{n+1}=\alpha h_n-y_{n+1}\) and \(y_n\asymp1/n\), the stable convolution yields \(h_n=-y_n/(1-\alpha)+O_T(n^{-2}+N^{-1}n^{-1})+O(\vartheta^n)\) for \(\varepsilon N\le n\le TN\). Combine with \(R_\mu=1/\alpha+\lambda/((1-\alpha)N)\) to obtain the claimed host limit.

## Verification

`checker.py` uses exact polynomial arithmetic in SymPy to rederive the degree-two fast graph and the quadratic and cubic slow-map coefficients, and floating-point trajectory diagnostics for several positive data sets and both signs of detuning. It checks boundedness and stability of the residual on growing finite horizons; finite computations corroborate the algebra but are not the proof of the uniform infinite-horizon assertion. The proof is analytic and the checker has no hidden data or external inputs.

## Relationship to prior work

Hu, Shen and Jia [1, Sections 4–5] identify the transcritical threshold and global attraction at and below it, but give no two-order finite-horizon inverse-density asymptotic. The source's normal-form analysis stops at the local bifurcation criterion; the explicit cubic contribution and its logarithmic finite-window accumulation are new calculations here.

An independently published analysis of a neutral **flip** sigmoid interval map [2] obtains an exponentially weighted logarithmic crossover for its inverse-square amplitude. Its state variable, critical eigenvalue, smooth map and asymptotic coefficient differ; it neither states nor directly specializes to the two-dimensional host–parasitoid transcritical system. The leading finite-time scaling law for generic one-dimensional transcritical normal forms was established earlier [3]; it yields the leading \(N U_\lambda(t)\) profile after reduction, but does not give the model-dependent logarithmic term or fast-coordinate response. The shared weighted-summation mechanism is acknowledged, and no claim is made to invent that general technique.

## Limitations

The statement is for fixed positive initial histories, fixed finite detuning \(\lambda\), and times bounded away from zero on the \(N\)-scale. It does not quantify transient times uniformly across varying initial densities, nor describe behavior at times much greater than \(N\). It does not assert a universal bounded correction constant, or global convergence for each supercritical fixed parameter. The negative detuning and positive detuning have a common finite-window limit but different eventual states. The first public availability of [1] is recorded from the publisher's dated source, not a later journal-issue date.

## References

[1] Linxia Hu, Yonghong Shen and Xiumei Jia, *Global behavior of a discrete population model*, AIMS Mathematics **9** (2024), 12128–12143, first public 27 March 2024, DOI: https://doi.org/10.3934/math.2024592; full paper: https://www.aimspress.com/aimspress-data/math/2024/5/PDF/math-09-05-592.pdf.

[2] *An exponentially weighted logarithmic crossover at the neutral flip of a sigmoid interval map*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-an-exponentially-weighted-logarithmic-crossover-at-the-neutral-f--ec7e4796f3ca; the full open repository result was inspected for its model, hypotheses, proof and implications.

[3] Daniel A. Martin, Qian-Yuan Tang and Dante R. Chialvo, *Finite-time scaling on low-dimensional map bifurcations*, arXiv:2505.24673v1, first public 30 May 2025, https://arxiv.org/html/2505.24673v1. Sections II and III treat leading-order finite-time scaling and selected one- and two-dimensional maps; no present next-order host–parasitoid term.
