# Gaussian-sketch Galerkin has a universal first-moment pole while sketched minimal residual has a dimension-dependent moment threshold

## Finding
Let \(A\in\mathbb R^{n\times n}\) be symmetric positive definite, \(n\ge2\), and let \(b\in\mathbb R^n\) be a deterministic unit vector which is not an eigenvector of \(A\). Given an integer \(m\ge1\), draw a real Gaussian sketch \(S\in\mathbb R^{m\times n}\) with independent \(N(0,1/m)\) entries. Define the one-step sketched Galerkin (sFOM) and sketched minimal-residual (sGMRES) approximations to \(Ax=b\) over \(\operatorname{span}\{b\}\) by
\[
 x_{\mathrm F}=\theta_{\mathrm F}b,\qquad
 \theta_{\mathrm F}=\frac{\langle Sb,Sb\rangle}{\langle Sb,SAb\rangle},\qquad
 x_{\mathrm M}=\theta_{\mathrm M}b,\qquad
 \theta_{\mathrm M}=\frac{\langle SAb,Sb\rangle}{\|SAb\|^2}.
\]
Both denominators are nonzero almost surely. Put \(a=b^{\mathsf T}Ab>0\), \(c=(\|Ab\|^2-a^2)^{1/2}>0\), \(h^2=a^2+c^2\), and \(x_\star=A^{-1}b\). Let \(C_m=\Gamma((m+1)/2)/(\sqrt\pi\,\Gamma(m/2))\). Then, writing \(Z\sim N(0,1)\) and \(R\sim\chi_m\) independently, each coefficient has the following marginal representation (the two representations do **not** assert joint equality using the same random variables):
\[
\theta_{\mathrm F}\ \stackrel{d}{=}\ \frac1{a+cZ/R},\qquad
\theta_{\mathrm M}\ \stackrel{d}{=}\ \frac{a}{h^2}+\frac{c}{h^2}\frac ZR.
\]
Consequently, for every \(q>0\),
\[
\begin{aligned}
\mathbb E\|x_{\mathrm F}-x_\star\|^q<\infty &\quad\Longleftrightarrow\quad q<1,\\
\mathbb E\|x_{\mathrm M}-x_\star\|^q<\infty &\quad\Longleftrightarrow\quad q<m.
\end{aligned}
\]
The same moment thresholds hold in the energy norm \(\|v\|_A=(v^{\mathsf T}Av)^{1/2}\). In particular, no **finite** Gaussian sketch size yields a finite expected absolute error for one-step sFOM on such an instance; sketched minimal residual has finite mean-square error precisely when \(m>2\).

The error-tail constants are also exact:
\[
\begin{aligned}
\lim_{t\to\infty}t\,\mathbb P(\|x_{\mathrm F}-x_\star\|>t)
&=\frac{2C_m}{c}\Bigl(1+\frac{a^2}{c^2}\Bigr)^{-(m+1)/2},\\
\lim_{t\to\infty}t^m\,\mathbb P(\|x_{\mathrm M}-x_\star\|>t)
&=\frac{2C_m}{m}\Bigl(\frac c{h^2}\Bigr)^m.
\end{aligned}
\]
Even though \(A\) is positive definite, sFOM moves in the negative \(b\) direction with probability \(\mathbb P(T_m<-a\sqrt m/c)>0\), where \(T_m\) is a standard Student variable with \(m\) degrees of freedom. This probability tends to zero as \(m\to\infty\), but is nonzero at every finite sketch size.

For \(m>2\), the sGMRES expected squared energy error is explicitly
\[
\mathbb E\|x_{\mathrm M}-x_\star\|_A^2
=b^{\mathsf T}A^{-1}b-\frac{2a}{h^2}+\frac{a^3}{h^4}
+\frac{ac^2}{h^4(m-2)}.
\]

## Assumptions and scope
The system and its exact solution are deterministic, \(b\) has Euclidean norm one, the one-dimensional Krylov search space is \(\operatorname{span}\{b\}\), and the initial iterate is zero. Every sketch entry is a fresh independent centered real Gaussian with variance \(1/m\); the sketch is **not conditioned** on passing a subspace-embedding test. All results are for one step and exact arithmetic. The case \(c=0\), excluded from the theorem, means \(b\) is an eigenvector and both methods produce the exact solution deterministically. The result does not apply to conditioned sketches, orthogonal-row sketches, deterministic sketches, or general multistep Krylov behavior without additional argument.

## Proof
**1. Exact coefficient laws.** Because \(b\) is a unit vector, the vectors \(b\) and \(w=(Ab-ab)/c\) are orthonormal, and \(Ab=ab+cw\). Set \(U=\sqrt m\,Sb\) and \(V=\sqrt m\,Sw\). Orthogonal invariance of the independent Gaussian sketch rows implies that \(U,V\) are independent standard Gaussian vectors in \(\mathbb R^m\). With \(R=\|U\|>0\), the variable \(Z=U^{\mathsf T}V/\|U\|\) has conditional law \(N(0,1)\) given \(U\), so it is independent of \(U\) and hence of \(R\). Substitution into the sketched Galerkin equation \(\langle Sb,S(b-\theta Ab)\rangle=0\) gives \(\theta_{\mathrm F}=1/(a+cZ/R)\). Its denominator vanishes with probability zero because the ratio has a continuous density.

For sketched minimal residual, set \(v=Ab/h\) and \(w'=(b-(a/h)v)/(c/h)\), which are orthonormal and satisfy \(b=(a/h)v+(c/h)w'\). Orthogonal invariance applied to \(\sqrt m Sv\) and \(\sqrt m Sw'\) shows that the least-squares coefficient \(\langle SAb,Sb\rangle/\|SAb\|^2\) has the stated marginal representation. Its denominator is positive almost surely.

**2. Tail density and exact moment cutoffs.** If \(Z\sim N(0,1)\) and \(R\sim\chi_m\) are independent, a change of variables in their joint density yields
\[
 f_m(z)=C_m(1+z^2)^{-(m+1)/2},\quad z\in\mathbb R.
\]
Its two-sided tails satisfy \(\mathbb P(|Z/R|>t)\sim (2C_m/m)t^{-m}\). Therefore the affine nondegenerate image \(\theta_{\mathrm M}\) has moments of order \(q\) exactly when \(q<m\), with the stated tail constant.

For sFOM, \(Y=a+cZ/R\) has continuous density
\[
 f_Y(y)=\frac{C_m}{c}\left(1+\frac{(y-a)^2}{c^2}\right)^{-(m+1)/2}.
\]
In particular \(0<f_Y(0)<\infty\). Since \(\theta_{\mathrm F}=1/Y\),
\[
 t\,\mathbb P(|\theta_{\mathrm F}|>t)
=t\int_{-1/t}^{1/t}f_Y(y)\,dy\longrightarrow 2f_Y(0).
\]
Integrability near \(y=0\) of \(|y|^{-q}f_Y(y)\) holds exactly for \(q<1\); away from zero the inverse is bounded. Hence these are necessary and sufficient moment thresholds. For any fixed \(u\), the inequalities \(\bigl|\|\theta b-u\|-|\theta|\bigr|\le\|u\|\) hold, so subtracting the fixed exact solution preserves the leading heavy-tail constants and moment cutoffs. Positive definiteness makes the Euclidean and energy norms equivalent, proving the energy-norm claim.

**3. Mean-square formula and directional reversal.** The mean and variance of \(Z/R\) are \(0\) and \(1/(m-2)\) for \(m>2\), by conditioning on \(R\) and the inverse-chi-square identity. Write \(\mu=a/h^2\) and \(\eta=c/h^2\). Using \(Ax_\star=b\),
\[
 \|\theta b-x_\star\|_A^2
 =b^{\mathsf T}A^{-1}b-2\theta+a\theta^2.
\]
Take expectation under \(\theta=\theta_{\mathrm M}=\mu+\eta Z/R\) to obtain the displayed formula. Finally \(\theta_{\mathrm F}<0\) exactly when \(a+cZ/R<0\), and \(\sqrt m\,Z/R\sim t_m\), proving the stated exact probability.

## Verification
An illustrative exact-arithmetic family is \(A=\operatorname{diag}(1,3)\) and \(b=(1,1)^{\mathsf T}/\sqrt2\). Then \(a=2\), \(c=1\), \(h^2=5\), and \(b^{\mathsf T}A^{-1}b=2/3\). The sketched Galerkin coefficient is distributed as \((2+Z/R)^{-1}\) and has infinite expected absolute error for every finite \(m\). Its Euclidean error-tail coefficient is \(2C_m5^{-(m+1)/2}\); its negative-step probability is \(\mathbb P(T_m<-2\sqrt m)\). For \(m>2\), the sketched minimal-residual energy error satisfies the exact identity
\[
 \mathbb E\|x_{\mathrm M}-x_\star\|_A^2
 =\frac{14}{75}+\frac{2}{25(m-2)}.
\]
The direct deterministic Galerkin energy error in this family is \(1/6\). The included standalone `verify.py` checks Gaussian-sketch algebraic identities, density normalization, inverse-chi-square moments, pole-tail coefficients, and exact rational examples using only the standard library. The infinite-moment conclusion is established by the analytical integral, not by any finite experiment.

## Relationship to prior work
The sketched Galerkin/FOM and sketched minimal-residual/GMRES constructions are standard and are **not** claimed as new. Güttel and Schweitzer, *Randomized sketching for Krylov approximations of large-scale matrix functions* (first public 2022-08-24, arXiv:2208.11447), explicitly formulate sketched Galerkin orthogonality in their equation (2.3), sketched GMRES in Section 3, and note possible instability when a sketched projected eigenvalue becomes negative. Timsit, Grigori and Balabanov, *Randomized Orthogonal Projection Methods for Krylov Subspace Solvers* (first public 2023-02-15, arXiv:2302.07466), study sketched Petrov–Galerkin methods, embedding-conditioned quasioptimality and observed error spikes. Neither inspected source establishes the unconditional all-finite-sketch first-moment pole and its exact tail constant, nor the contrasted sharp \(q<m\) minimal-residual moment spectrum on this one-dimensional Gaussian benchmark. The distribution formulae are obtained from classical Gaussian/chi and Student-distribution calculations, which are not claimed as new by themselves.

## Limitations
The comparison is specific to unconditioned iid Gaussian sketches and one Krylov step. Because the exact heavy-tail constant decreases rapidly with sketch size, the infinite expectation can be driven by extraordinarily rare bad sketches, and does not contradict high-probability subspace embedding bounds. The case in which a sketch is rejected or regularized when the projected denominator is small is not covered. The result supplies neither a typical-case runtime assessment nor a theorem for finite-precision implementations or later Krylov iterations. No claim of independent scientific validation or definitive publication priority is made.

## References
1. S. Güttel and M. Schweitzer, *Randomized sketching for Krylov approximations of large-scale matrix functions*, arXiv:2208.11447, first posted 2022-08-24, Sections 2–3; DOI: 10.1137/22M1518062.
2. E. Timsit, L. Grigori and O. Balabanov, *Randomized Orthogonal Projection Methods for Krylov Subspace Solvers*, arXiv:2302.07466, first posted 2023-02-15, Sections 2–3.
