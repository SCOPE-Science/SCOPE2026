# Exact short- and long-horizon locations for worst-direction sensing of two heat modes

## Finding

For the first two Dirichlet heat modes on \((0,1)\), the best fixed point sensor for the least observable unit direction has different short- and long-horizon limits. Write \(x_T\in(0,1/2)\) for its left-half location and put \(u_T=\cos^2(\pi x_T)\). With continuous noiseless observations over \([0,T]\) and diffusivity \(1/\pi^2\),
\[
\lim_{T\downarrow0}u_T=\frac{\sqrt5-1}{4},\qquad
\lim_{T\to\infty}u_T=u_\infty,
\quad 50u_\infty^3+19u_\infty^2+4u_\infty-9=0,
\]
where the cubic has exactly one root in \((0,1)\). The corresponding left sites are \(0.312376431107\ldots\) and \(0.273760552610\ldots\). By reflection there is a right site for each left site. The result concerns the exact horizon limits, not monotonicity at intermediate horizons. The uniqueness used to define \(x_T\) is an application of classical spectral-radius log-convexity.

## Model and design criterion

Take \(v(x,0)=\alpha_1\sin(\pi x)+\alpha_2\sin(2\pi x)\), with Euclidean norm on \((\alpha_1,\alpha_2)\). The signal at the chosen point \(x\in[0,1]\) is \(\alpha_1 e^{-t}\sin(\pi x)+\alpha_2 e^{-4t}\sin(2\pi x)\). The criterion is the minimum squared \(L^2(0,T)\) signal norm over unit amplitudes. Thus it is the smaller eigenvalue of the observation Gramian. There is no optimization over the temporal samples or over multiple points.

Put \(u=\cos^2(\pi x)\). The smallest eigenvalue is unchanged by reflection, and on the left half the Gramian is
\[
(1-u)\begin{pmatrix}a_T&2b_T\sqrt u\\2b_T\sqrt u&4c_Tu\end{pmatrix},
\quad (a_T,b_T,c_T)=\left(\frac{1-e^{-2T}}2,\frac{1-e^{-5T}}5,\frac{1-e^{-8T}}8\right).
\tag{1}
\]
The entries are the inner products of the temporal profiles. Strict Cauchy–Schwarz gives \(\Delta_T=a_Tc_T-b_T^2>0\). The eigenvalue vanishes at \(u=0,1\), and is positive between them.

## Proof

**Uniqueness from known log-convexity.** For constants \(a,c>0\), \(ac-b^2=\Delta>0\), invert the matrix in (1) with these constants and remove the off-diagonal sign by diagonal orthogonal conjugation. The reciprocal of its smaller eigenvalue is the spectral radius of
\[
\frac{1}{\Delta(1-u)}\begin{pmatrix}c&|b|/(2\sqrt u)\\ |b|/(2\sqrt u)&a/(4u)\end{pmatrix}.
\]
For \(z=\log(u/(1-u))\), factor out \(1+e^z\). The remaining matrix has constant upper-left entry, off-diagonal entry proportional to \((1+e^{-z})^{1/2}\) and lower-right entry proportional to \(1+e^{-z}\). Its nonzero entries are log-convex. By Kingman's spectral-radius theorem (see also Nussbaum, Corollary 1.2), the residual log spectral radius is convex for \(b\ne0\); for \(b=0\) this follows by taking the maximum of the two diagonal logarithms. The scalar factor adds the strictly convex \(\log(1+e^z)\). The reciprocal eigenvalue diverges as \(z\to+\infty\) by the upper-left diagonal and as \(z\to-\infty\) by the lower-right diagonal. There is therefore one minimizing logit, which for the physical sensor gives exactly two reflected optimal points. This argument also applies to the limiting temporal Gram below.

**Short horizons.** Denote the smaller eigenvalue by \(\Lambda_T(u)\). From trace and determinant,
\[
\Lambda_T(u)=\frac{8u(1-u)\Delta_T}{a_T+4c_Tu+\sqrt{(a_T-4c_Tu)^2+16b_T^2u}}.
\tag{2}
\]
The short-time Gram determinant has the integral representation
\[
\Delta_T=\frac12\int_0^T\int_0^T(e^{-s-4t}-e^{-t-4s})^2\,ds\,dt.
\]
On setting \(s=Tr,t=Tq\), the difference of exponentials is \(3T(r-q)+O(T^2)\), uniformly for \(r,q\in[0,1]\). Since \(\int_0^1\int_0^1(r-q)^2\,dr\,dq=1/6\), \(\Delta_T/T^4\to3/4\). The three Gram entries divided by \(T\) tend to 1, so the denominator in (2) divided by \(T\) converges uniformly on \([0,1]\) to \(2(1+4u)\), bounded away from zero. Hence
\[
T^{-3}\Lambda_T(u)\longrightarrow \frac{3u(1-u)}{1+4u}
\quad\text{uniformly on }[0,1].
\]
The derivative has the sign of \(1-2u-4u^2\); its sole zero in the unit interval is \((\sqrt5-1)/4\). Every accumulation point of maximizers of uniformly converging functions on a compact set maximizes the limit, so uniqueness yields the stated short-horizon location. The cubic-in-time information scale is needed because the two profiles become indistinguishable to leading order.

**Long horizons.** The Gram entries tend to \((1/2,1/5,1/8)\). The information matrices converge uniformly on the compact design interval, so the smallest eigenvalues converge uniformly as well. The limiting matrix has \(\Delta=9/400\); the argument above gives a unique maximizing \(u\) in \((0,1)\). Its smaller eigenvalue is simple there because the off-diagonal entry is nonzero. The limiting trace and determinant are \(S=(1-u^2)/2\) and \(P=9u(1-u)^2/100\). At the maximizing \(u\), the characteristic polynomial \(F(\ell,u)=\ell^2-S\ell+P\) and its partial \(u\)-derivative vanish. The resultant in \(\ell\) is
\[
-\frac{9}{10000}(1-u)^2(50u^3+19u^2+4u-9).
\]
The cubic increases strictly on \([0,1]\) and changes sign there. The interior optimizer is therefore its unique root in \((0,1)\); uniform convergence and uniqueness give the long-horizon limit. For comparison, the determinant criterion in (1) maximizes \(u(1-u)^2\), always at \(u=1/3\). Thus the horizon dependence here is a property of the worst-direction objective, not merely a scaling of overall signal energy.

## Reproducibility and scope

The accompanying `verify.py` checks the Gram determinant coefficient, short-time stationary equation and long-time resultant with SymPy, and supplies finite numerical checks. These calculations are supplementary; coercivity, uniqueness and both limits use the analytic proof. The comparison is restricted to two modes, Euclidean amplitude normalization and a single spatial point with continuous-time signal energy. It does not cover noisy discrete samples, higher modes, or monotonicity with horizon.

The known matrix log-convexity, including its application to the inverse information transform, is not claimed as a new result. The specific addition is the distinct exact endpoints for the two-mode heat experiment. The random-initial-data observation-domain problem of Privat, Trélat and Zuazua and the free scalar actuator design of Geshkovski and Zuazua use different admissible designs and criteria. These comparisons do not establish absolute publication priority.

## References

1. J. F. C. Kingman, *A Convexity Property of Positive Matrices*, Q. J. Math. 12 (1961), 283–284, https://doi.org/10.1093/qmath/12.1.283.
2. R. D. Nussbaum, *Convexity and Log Convexity for the Spectral Radius*, Linear Algebra Appl. 73 (1986), 59–122, Corollary 1.2, https://sites.math.rutgers.edu/~nussbaum/Pubs/logconvexity1986.pdf.
3. Y. Privat, E. Trélat and E. Zuazua, *Optimal shape and location of sensors for parabolic equations with random initial data*, https://arxiv.org/abs/1403.6445.
4. B. Geshkovski and E. Zuazua, *Optimal actuator design via Brunovsky’s normal form*, https://arxiv.org/abs/2108.05629.
