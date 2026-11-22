# An exact log-kill budget separating extinction from growth in a resistant two-stage population

## Finding

Consider a two-life-stage population with continuous dynamics \(\dot x=Ax\) between periodic treatments, where \(A\in\mathbb R^{2\times2}\) is irreducible Metzler (both off-diagonal entries strictly positive). At every interval of length \(\tau>0\), treatment multiplies the two stage abundances by \(s_1,s_2\in(0,1]\). A fixed additive *log-kill* budget \(B>0\) means
\[
-\log s_1-\log s_2=B,\qquad s_1s_2=q=e^{-B}.
\]
Write \(E=e^{\tau A}\), \(u=E_{11}>0\), \(v=E_{22}>0\), and \(d=\det E>0\). Then the unique allocation minimizing the full-resistance Floquet multiplier \(\rho(\operatorname{diag}(s_1,s_2)E)\) is
\[
s_1^*(q)=\operatorname{clip}_{[q,1]}\sqrt{\frac{qv}{u}},\qquad s_2^*(q)=\frac{q}{s_1^*(q)}.
\]
In particular, optimality balances the **post-period diagonal returns** \(s_1u=s_2v\) whenever the clipping constraints are inactive, not the survival probabilities themselves. For \(0<q<1\), equal allocation is optimal if and only if \(u=v\); at \(q=1\) it is the only feasible allocation. For every two-stage generator the strict equal-treatment-growth/optimal-treatment-extinction reversal occurs exactly when \(\sqrt q\,\rho(E)>1>R_*(q)\). The optimal multiplier is exactly
\[
R_*(q)=\frac{T_*(q)+\sqrt{T_*(q)^2-4qd}}2,
\qquad T_*(q)=us_1^*(q)+vs_2^*(q).
\]

For the biologically admissible juvenile–adult generator and pulse interval
\[
A=\begin{pmatrix}-3/2&15/4\\1&-1/2\end{pmatrix},\qquad \tau=\log2,
\]
where maturation is \(1\), juvenile natural mortality is \(1/2\), adult natural mortality is \(1/2\), and adult fecundity is \(15/4\), one has
\[
E=\begin{pmatrix}53/64&225/128\\15/32&83/64\end{pmatrix},\qquad \rho(E)=2.
\]
Define the **sharp optimal-treatment critical survival product**
\[
q_c=\frac{3887-\sqrt{14846625}}{128}
=0.264594976096743\ldots.
\]
For all \(0<q<q_c\), some admissible allocation makes the full-resistance population decline exponentially; for all \(q>q_c\), every admissible allocation makes it grow exponentially. The multiplier is neutral at \(q=q_c\). Equal treatment \(s_1=s_2=\sqrt q\) has multiplier \(2\sqrt q\). Thus for **every**
\[
\boxed{\quad\frac14<q<q_c\quad}
\]
equal treatment produces exponential growth while optimal stage-targeted treatment produces exponential extinction, despite identical total log-kill expenditure.

As a simple exact interior witness, \(q=13/50\) and \((s_1,s_2)=(3/5,13/30)\) give \(\operatorname{tr}(\operatorname{diag}(s_1,s_2)E)=2033/1920\), \(\det(\operatorname{diag}(s_1,s_2)E)=13/200\), and
\[
1-\operatorname{tr}(\operatorname{diag}(s_1,s_2)E)+\det(\operatorname{diag}(s_1,s_2)E)=\frac{59}{9600}>0.
\]
Hence targeted treatment has multiplier below \(1\), whereas equal treatment with the same product \(q\) has multiplier \(\sqrt{26}/5>1\).

## Assumptions and scope

The theorem for the unique optimal split holds for every real irreducible two-stage Metzler generator \(A\), every \(\tau>0\), and every \(q\in(0,1]\), with strictly positive survival in each life stage. The explicit sharp budget threshold and strict policy reversal are asserted for the displayed generator and interval, not for arbitrary generators. The stated costs are **defined** as additive negative logarithms of stage-specific survival; they are not asserted to be linear in an empirical pesticide dose.

For the eco-evolutionary interpretation of Long, Adjei and Patel, identify \(s_i\) with survival of fully resistant genotypes, let susceptible and heterozygous survival respectively be \((1-\sigma)s_i\) and \((1-\sigma h)s_i\), and take \(\sigma=h=1/2\), no fitness cost, and no mutation. Under the source model's allele-mixing equations, initial abundances \(x_i(0)>0\) and positive initial resistant frequencies \(y_i(0)>0\) imply convergence of resistance frequencies to one. The strict full-resistance multiplier comparison then controls extinction versus unbounded density-independent growth of the total population. No conclusion is made at neutral multiplier one.

## Proof

**Optimal allocation.** The matrix \(E\) is strictly positive because \(A\) is irreducible Metzler and \(\tau>0\), and \(d=e^{\tau\operatorname{tr}A}>0\). Parametrize admissible allocations by \(s_1=x\in[q,1]\) and \(s_2=q/x\). The two characteristic coefficients of \(M(x)=\operatorname{diag}(x,q/x)E\) are
\[
\operatorname{tr}M(x)=ux+\frac{qv}{x},\qquad\det M(x)=qd.
\]
The discriminant equals \((ux-qv/x)^2+4qE_{12}E_{21}>0\), so the positive eigenvalues are distinct and the Perron root is \((T+\sqrt{T^2-4qd})/2\). At fixed \(q\), this root increases strictly with \(T\). The derivative of the trace is \(u-qv/x^2\), with unique positive zero \(\sqrt{qv/u}\); the second derivative is \(2qv/x^3>0\). Projection onto \([q,1]\) therefore gives the stated unique optimizer. This proves the formula for every allowed \(q\), including boundary-attaining cases.

**Exact two-stage flow.** The displayed \(A\) satisfies \(A^2+2A-3I=0\) and has eigenvalues \(1\) and \(-3\). Its spectral projectors are \(P_+=(A+3I)/4\), \(P_-=(I-A)/4\). As \(\tau=\log2\),
\[
E=2P_++\frac18P_- =\frac{15A+49I}{32},
\]
which gives the displayed strictly positive rational entries, \(d=1/4\), \(u=53/64\), and \(v=83/64\).

**Sharp budget boundary.** In the range \(q\le u/v=53/83\), the optimizer is interior, giving \(T_*(q)=2\sqrt{q(4399/4096)}\) and determinant \(q/4\). For \(q\in(0,1]\), an irreducible positive \(2\times2\) matrix with positive determinant has \(\rho<1\) if and only if \(\det M<1\) and \(1-\operatorname{tr}M+\det M>0\). In the present interior range these conditions reduce to
\[
64q^2-3887q+1024>0.
\]
Its smaller root is \(q_c=(3887-\sqrt{14846625})/128\), which lies strictly between \(1/4\) and \(27/100\), and hence in \((0,53/83)\). The optimum is strictly increasing in \(q\): if \(q_1<q_2\), scaling both entries of any feasible policy at \(q_2\) by \(\sqrt{q_1/q_2}\) yields a feasible policy at \(q_1\) whose multiplier is strictly smaller. Thus this root is the unique global crossing even for \(q>53/83\). Equal allocation has multiplier \(\sqrt q\,\rho(E)=2\sqrt q\). The sharp window follows. For the exact rational witness, the polynomial at one is \(59/9600>0\) and the determinant is \(13/200<1\), establishing extinction; the equal-treatment multiplier exceeds one because \(26/25>1\).

**Evolutionary interpretation.** In the cited eco-evolutionary formulation the stage survival at frequency \(y_i\) never exceeds its fully resistant value \(s_i\), so when \(\rho(\operatorname{diag}(s_i)E)<1\), comparison with the fixed positive matrix implies extinction for any genotype frequencies. Under positive selection and positive initial resistant frequencies, the source's resistance-convergence theorem gives \(y_i(t)\to1\). When the full-resistance multiplier exceeds one, for some \(\varepsilon>0\) the eventual pulse matrices dominate \((1-\varepsilon)\operatorname{diag}(s_i)\), whose Floquet multiplier still exceeds one. Iterated comparison with this positive matrix implies unbounded growth at pulse times and during each bounded intervening period. These arguments require strict inequalities; at the boundary no dynamical classification is asserted.

## Verification

The accompanying standard-library file `verify.py` checks, using exact rational arithmetic, the quadratic matrix identity, the two spectral projectors, the displayed exponential, determinant, exact targeted-policy characteristic coefficients, and the strict sign \(59/9600>0\). It brackets the exact algebraic critical root using high-precision decimal arithmetic and performs 6,000 seeded numerical comparisons between the analytic optimum and alternative allocations. The finite comparisons are supplementary sanity tests, **not** the proof of the universal optimizer or infinite-time behavior. Run `python3 verify.py` in a directory containing this file.

## Relationship to prior work

Long, Adjei and Patel (2026, arXiv:2609.10581) define the stage-structured eco-evolutionary pulse model and establish resistance fixation and population fate in terms of the full-resistance Floquet multiplier. Those underlying theorems are prior results. Their model treats stage-specific survivals as given and does not supply the fixed-log-kill optimization, its exact admissible allocation, or the sharp budget window derived here.

Patel and De Leenheer (2023 preprint; 2024 journal publication, arXiv:2310.07616) study the spectral radius of \(D e^{\tau A}\), explicitly keeping \(D\) fixed and varying the pulse period \(\tau\). Friedland's 1981 log-convexity of positive-matrix spectral radii under logarithmic diagonal scaling and related results of Kingman/Nussbaum supply general convexity background. Generic geometric-programming formulations for Perron eigenvalue optimization are also known; they are not claimed as new. The specific solved allocation, positive-survival feasibility boundary, and fixed-budget eco-evolutionary growth-versus-extinction reversal constitute the claim here.

## Limitations

The fixed budget is a mathematically defined sum of log-survival reductions, not a measured field-treatment cost. The explicit sharp numerical budget threshold concerns a constructed two-stage system with density-independent demography and a fixed treatment interval; it is not calibrated to an observed species. Resistance is assumed to have no fitness cost and no mutation. The population model's divergence is a linear-model prediction, not literal unbounded real biological abundance. The exact neutral case \(\rho=1\), stochastic extinction, off-target effects, nonlinear ecology, and intervention optimization across pulse periods are outside the claim. Earlier generic spectral optimization might permit the calculation as a specialization; the originality assertion is limited to the explicit ecology-focused budget classification after the cited comparisons, and is not an independent priority certification.

## References

1. A. D'Ovidio Long, A. Adjei and S. Patel, *On the formulation and analysis of a stage-structured eco-evolutionary model with pulsed disturbances* (first public 2026-09-05), https://arxiv.org/abs/2609.10581 .
2. S. Patel and P. De Leenheer, *On the spectral radius properties of a key matrix in periodic impulse control* (preprint first public 2023-10-11; journal 2024), https://arxiv.org/abs/2310.07616 .
3. S. Friedland, *Convex Spectral Functions*, Linear and Multilinear Algebra **9** (1981), 299–316, https://doi.org/10.1080/03081088108817381 .
4. R. D. Nussbaum, *Convexity and log convexity for the spectral radius*, Linear Algebra and Its Applications **73** (1986), 59–122, https://doi.org/10.1016/0024-3795(86)90233-8 .
5. S. Boyd and L. Vandenberghe, *Convex Optimization*, §4.5.4 (positive-system Perron optimization), https://web.cvxr.com/cvx/examples/cvxbook/Ch04_cvx_opt_probs/html/min_spec_rad_ppl_dynamics.html .
