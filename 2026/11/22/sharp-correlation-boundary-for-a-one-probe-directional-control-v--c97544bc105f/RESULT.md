# Sharp correlation boundary for a one-probe directional control variate

## Finding

For an isotropic quadratic, reusing a Gaussian exploratory probe to construct the *same step's* directional reference can reverse the mean gradient and make every positive constant step unstable. The exact correlation threshold is determined by the hint-subspace rank rather than the ambient dimension.

**Theorem.** Let integers \(d\geq 1\) and \(1\leq k\leq d\) be given. Let \(P\in\mathbb R^{d\times d}\) be an orthogonal projector of rank \(k\), and let \(f(x)=\tfrac12\|x\|_2^2\). At every iteration independently of the past, sample a jointly centered Gaussian pair \((u,v)\) with
\[
\mathbb E[uu^\top]=\mathbb E[vv^\top]=I_d,\qquad
\mathbb E[uv^\top]=\rho I_d,\qquad -1\leq\rho\leq1.
\]
Put \(q=\rho^2\), choose any positive constant \(h\), and set
\[
 m=Pvv^\top x,\quad G=m+uu^\top(x-m),\quad x^+=x-hG.
\]
Then the exact conditional mean is
\[
\mathbb E[G\mid x]=\big[(1-kq)I_d-qP\big]x.
\]
Define
\[
\begin{aligned}
 C_{\parallel}&=dk+d+k+2
 +(dk^2+3dk+4d+2k^2+8k+10)q
 +(2k^2+10k+12)q^2,\\
 C_{\perp}&=dk+d+k+2
 +(dk^2-dk+2k^2)q+(2k^2+2k)q^2.
\end{aligned}
\]
For all \(x\), with the perpendicular contribution absent if \(k=d\),
\[
\begin{split}
 \mathbb E[\|G\|_2^2\mid x]
 &=C_{\parallel}\|Px\|_2^2+C_{\perp}\|(I_d-P)x\|_2^2,\\
 \mathbb E[\|x^+\|_2^2\mid x]
 &=\big(1-2h[1-(k+1)q]+h^2C_{\parallel}\big)\|Px\|_2^2\\
 &\quad+\big(1-2h[1-kq]+h^2C_{\perp}\big)\|(I_d-P)x\|_2^2.
\end{split}
\]
Because \(C_{\parallel}\geq C_{\perp}\), the exact worst-case expected squared-norm multiplier is
\[
 R(h)=1-2h\big[1-(k+1)q\big]+h^2C_{\parallel}.
\]
Thus **there exists a positive constant step giving uniform one-step mean-square contraction if and only if**
\[
\boxed{|\rho|<\frac1{\sqrt{k+1}}.}
\]
In this subcritical regime, uniform strict contraction holds exactly for
\[
 0<h<\frac{2[1-(k+1)q]}{C_{\parallel}},
\]
and the unique step minimizing its worst-case one-step factor is
\[
 h_{\mathrm{opt}}=\frac{1-(k+1)q}{C_{\parallel}},\qquad
 R(h_{\mathrm{opt}})=1-\frac{[1-(k+1)q]^2}{C_{\parallel}}.
\]
For independent fresh probe pairs across iterations, the latter bounds the squared-norm mean by \(R(h)^t\|x_0\|_2^2\) after \(t\) steps. At equality \(q=1/(k+1)\), every nonzero hinted initial component has unchanged expectation and cannot converge to zero in mean square at any positive step. Above equality, the expected hinted component grows geometrically for every positive step, and therefore its squared norm has diverging expectation.

## Assumptions and scope

The reference \(m\) uses one *Gaussian* direction \(v\), projected into a predetermined hint subspace. The exploration direction \(u\) may share Gaussian randomness with \(v\), parametrized by the same-coordinate correlation \(\rho\). Pairs are freshly and independently sampled between iterations. Exact, noiseless, centered two-point directional differences of the quadratic evaluate \(v^\top x\) and \(u^\top x\) for every positive perturbation radius, so the update can be implemented with function values alone. This is a **modified one-probe reference rule**, not the independent-exploration algorithm in the cited directional-hint paper. No assumption of bounded global gradient is made for this quadratic benchmark.

The question is whether an inexpensive sampled reference can safely share randomness with the Gaussian exploration correction. The result measures both the sharp correlation boundary and the whole one-step mean-square frontier at each rank.

## Proof

**1. Mean drift.** Conditional on \(x\), apply the fourth-order Gaussian pairing identity:
\[
\mathbb E[uu^\top Pvv^\top]=(1+q)P+kqI_d.
\]
Since \(\mathbb E[uu^\top]=I_d\) and \(\mathbb E[Pvv^\top]=P\), substitution into
\(G=uu^\top x+(I_d-uu^\top)Pvv^\top x\) proves the asserted mean. In particular its eigenvalue on \(\operatorname{ran}(P)\) is \(a=1-(k+1)q\), while the eigenvalue on its orthogonal complement is \(b=1-kq\).

**2. Exact second moment.** Let \(\|x\|_2=1\) and abbreviate
\[
 U=u^\top u,\quad V=u^\top Pu,\quad
 A=u^\top x,\quad T=u^\top Px,\quad p=x^\top Px,\quad z=1-q.
\]
The conditional Gaussian law is \(v\mid u\sim\mathcal N(\rho u,zI_d)\), also valid in the degenerate cases \(|\rho|=1\) as a point mass. Set \(K=I_d-uu^\top\) and \(B=PK^2P=P+(U-2)Puu^\top P\). Expanding the square of \(G=A u+K Pv(v^\top x)\), and then applying the ordinary quadratic Gaussian fourth-moment identity, gives
\[
\begin{split}
 \mathbb E[\|G\|_2^2\mid u,x]
 &=A^2U+2A(1-U)(q A V+z T)\\
 &\quad+(q A^2+z)\left(q[V+(U-2)V^2]+z[k+(U-2)V]\right)\\
 &\quad+4zq AT[1+(U-2)V]+2z^2[p+(U-2)T^2].
\end{split}
\]
For completeness, this identity follows directly by expanding \(v=\rho u+\sqrt z\,w\), \(w\sim\mathcal N(0,I_d)\), and using
\[
\begin{split}
 \mathbb E[(v^\top x)^2(v^\top Bv)\mid u]
 &=(q A^2+z)(q u^\top Bu+z\operatorname{tr} B)\\
 &\quad+4zqA(x^\top Bu)+2z^2(x^\top Bx),
\end{split}
\]
with \(u^\top Bu=V+(U-2)V^2\), \(\operatorname{tr} B=k+(U-2)V\), \(x^\top Bu=T[1+(U-2)V]\), and \(x^\top Bx=p+(U-2)T^2\).

The expression is invariant under the subgroup of orthogonal transformations preserving \(P\), so its expectation is a scalar quadratic form on each of the two orthogonal subspaces with no cross term. To calculate its two coefficients, first take a unit \(x\in\operatorname{ran}(P)\), so \(T=A\) and \(p=1\). The independent variables \(V\sim\chi_k^2\) and \(U-V\sim\chi_{d-k}^2\) satisfy \(\mathbb E[A^2\mid V]=V/k\). Next, for \(k<d\), take unit \(x\in\ker(P)\), so \(T=p=0\), and \(\mathbb E[A^2\mid U-V]=(U-V)/(d-k)\). In both cases evaluate the preceding polynomial with the identities
\[
 \mathbb E[(\chi_r^2)^j]=\prod_{i=0}^{j-1}(r+2i),\qquad j=0,1,2,\dots.
\]
Collecting constant, \(q\), and \(q^2\) terms yields exactly \(C_{\parallel}\) and \(C_{\perp}\) as displayed. These are polynomial identities for all positive integral \(d,k\), not extrapolations from finite tests.

**3. Sharp contraction and impossibility.** Direct subtraction gives
\[
 C_{\parallel}-C_{\perp}
 =(4dk+4d+8k+10)q+(8k+12)q^2\geq0.
\]
Since \(b-a=q\geq0\), the hinted coefficient in the expected squared step exceeds the complementary coefficient for every \(h>0\); equality can occur only at \(q=0\). The supremum over nonzero \(x\) is therefore attained by any \(x\in\operatorname{ran}(P)\), and equals \(R(h)\). For \(h>0\), \(R(h)<1\) is equivalent to \(a>0\) and \(0<h<2a/C_{\parallel}\). The positive quadratic in \(h\) has its unique minimizer at \(h=a/C_{\parallel}\).

At \(a=0\), conditioning on the history gives \(\mathbb E[Px_{t+1}\mid x_t]=Px_t\) for all \(t\), hence \(\mathbb E[Px_t]=Px_0\). Jensen's inequality rules out mean-square convergence to zero whenever \(Px_0\ne0\). If \(a<0\), then \(\mathbb E[Px_t]=(1-ha)^tPx_0\) and the factor \(1-ha>1\). Jensen then proves divergence of \(\mathbb E\|x_t\|_2^2\). In the subcritical case, the uniform conditional bound \(\mathbb E[\|x_{t+1}\|_2^2\mid x_t]\leq R(h)\|x_t\|_2^2\) iterates by the tower property.

## Verification

A standalone standard-library script, `check_correlated_cv.py`, expands the estimator polynomial coordinatewise and computes the relevant Gaussian moments by exact Wick pairings with rational arithmetic. It checks both moment formulas, drift and the contraction expression for all \(1\le k\le d\le6\) and five distinct rational correlations, giving **105 exact-rational dimension/rank/correlation cases**. Execute `python check_correlated_cv.py` from the extracted package. The checks test the formulas; the all-dimensional result rests on the foregoing symbolic proof.

For example, at \(d=2,k=1\), \(C_{\parallel}=7+36q+24q^2\). Hence a positive uniformly contracting step exists exactly for \(q<1/2\), with sharp upper step \(2(1-2q)/(7+36q+24q^2)\).

## Relationship to prior work

Ryabchenko, Qian and Mou introduce the Gaussian directional-hint control-variate estimator and require a fresh exploratory draw *independent of its already chosen reference* (their Section 3, algorithm and theorem). Their practical construction uses separate projected directional estimates; their guarantee does not concern the within-iteration correlated Gaussian reference considered here. The present conclusion is about a **different, deliberately coupled** estimator and should not be interpreted as a failure of their algorithm.

Geffner and Domke analyze variance reduction through quadratic-approximation control variates for reparameterization gradients; the distinct estimator and sampling structure there do not imply the rank-dependent coupling threshold proved here. Independent-probe noise floors and oracle-reference descent stability studied in other literature similarly retain a different reference/probe dependence structure.

The general risk of bias from estimating a control variate on dependent observations is familiar; the claim here is the **exact Gaussian projected-reference bias, sharp rank-dependent reversal threshold, and complete worst-case one-step mean-square frontier for this specified iterative model**, not that biased reuse is a previously unknown concept.

## Limitations

The result is exact for a noiseless isotropic quadratic, a fixed orthogonal hint projector, a single Gaussian reference probe, jointly Gaussian within-iteration probe coupling, and fresh independent pairs across iterations. It makes no assertion about general nonlinear objectives, arbitrary correlated sampling laws, noisy finite differences, adaptive reference selection, time-correlated innovations or the source's independent-exploration method. Above the stable step interval but below the correlation threshold, lack of one-step uniform contraction is **not** claimed to establish eventual divergence. Independent external validation has not been carried out.

## References

1. A. Ryabchenko, J. Qian and W. Mou, *Adaptively Incorporating Directional Hints into Zeroth-Order Optimization*, arXiv:2609.08277v1 (8 September 2026), revised v2 (9 November 2026). https://arxiv.org/abs/2609.08277
2. T. Geffner and J. Domke, *Approximation Based Variance Reduction for Reparameterization Gradients*, arXiv:2007.14634 (2020). https://arxiv.org/abs/2007.14634
