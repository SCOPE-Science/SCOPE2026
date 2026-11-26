# A gamma-law spectral crossover for near-identity embeddings of flat Bergman spaces

## Finding
Fix \(a,\beta>0\). For \(\varepsilon>0\), let \(J_\varepsilon:A^2_{a,\beta}\to A^2_{a+\varepsilon,\beta}\) be the identity inclusion, where
\[
\|f\|_{a,\beta}^{2}=\int_{\mathbb D}|f(z)|^2\exp\!\left[-\frac{a}{(1-|z|)^\beta}\right]\,dA(z),\qquad dA=\frac{dx\,dy}{\pi}.
\]
Put \(\delta=\beta/(\beta+1)\) and \(c_{a,\beta}=2^{\delta-1}(a\beta)^{-\delta}\). Then \(J_\varepsilon\) is compact and lies in every Schatten class \(\mathcal S_p\) with \(p>0\). More sharply, for every \(t>0\),
\[
\lim_{\varepsilon\downarrow0}s_{\lfloor t\varepsilon^{-1/\delta}\rfloor+1}(J_\varepsilon)
=\exp(-c_{a,\beta}t^{\delta}),
\]
and for every real \(p>0\),
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{1/\delta}\|J_\varepsilon\|_{\mathcal S_p}^{p}
=\Gamma(1+1/\delta)(p c_{a,\beta})^{-1/\delta}.}
\]
These are exact constants. For example, \(a=2\), \(\beta=1\), \(p=2\) gives \(\lim_{\varepsilon\downarrow0}\varepsilon^2\|J_\varepsilon\|_{\mathcal S_2}^2=2\). The profile also gives the leading effective approximation rank as the two weights coalesce.

## Assumptions and scope
The source parameter \(a\), flatness exponent \(\beta\), perturbation \(\varepsilon\), and Schatten index \(p\) are strictly positive; \(p\) need not be at least one. Singular values are indexed from one, in decreasing order, with multiplicities. The result concerns the identity between different Hilbert norms on analytic functions, not a composition operator or a Hankel self-commutator. Both spaces contain the polynomials densely; the domain weight is pointwise larger, so the identity is contractive. The comparison parameter \(a\) is fixed while \(\varepsilon\downarrow0\).

## Proof
**Step 1: exact diagonalization and ordering.** Define the radial moments
\[
M_n(u)=2\int_0^1 r^{2n+1}\exp\left[-\frac{u}{(1-r)^\beta}\right]dr,
\qquad n\in\mathbb N_0,\ u>0.
\]
The normalized monomials \(z^n/M_n(a)^{1/2}\) form an orthonormal basis of \(A^2_{a,\beta}\). Their images are orthogonal in the target; thus the squared singular values, *before rearrangement*, are \(M_n(a+\varepsilon)/M_n(a)\). This quotient is strictly decreasing with \(n\): it is the expectation of the strictly decreasing function \(r\mapsto \exp[-\varepsilon/(1-r)^\beta]\) under the probability density proportional to \(r^{2n+1}\exp[-a/(1-r)^\beta]\); increasing \(n\) size-biases that density toward larger \(r\). Hence the exact decreasing singular list is
\[
s_{n+1}(J_\varepsilon)^2=\frac{M_n(a+\varepsilon)}{M_n(a)}.
\tag{1}
\]

**Step 2: a uniform boundary saddle lemma.** Let \(\mu_{n,u}\) be the probability measure on \((0,1)\) proportional to \(r^{2n+1}\exp[-u/(1-r)^\beta]dr\). For each fixed compact interval \(I\subset(0,\infty)\), the following estimate holds uniformly for \(u\in I\):
\[
\mathbb E_{\mu_{n,u}}(1-r)^{-\beta}
=\left(\frac{2n}{u\beta}\right)^\delta(1+o(1)).
\tag{2}
\]
To verify it, write \(v=1-r\) and use the strictly convex phase \(\Phi_{n,u}(v)=-(2n+1)\log(1-v)+uv^{-\beta}\). Its unique minimizer \(v_{n,u}\) solves \((2n+1)/(1-v_{n,u})=u\beta v_{n,u}^{-\beta-1}\), so uniformly on \(I\), \(v_{n,u}\sim(u\beta/(2n))^{1/(\beta+1)}\). Its second derivative is \(\Phi''_{n,u}(v_{n,u})\sim(\beta+1)(2n)/v_{n,u}\), and the Gaussian width divided by \(v_{n,u}\) is of order \((nv_{n,u})^{-1/2}\to0\). For any fixed relative neighborhood of this minimizer, Taylor's theorem bounds the quadratic phase above and below by constants times \((2n/v_{n,u})(v-v_{n,u})^2\); beyond that neighborhood, convexity and the terms \(uv^{-\beta}\) and \(-(2n+1)\log(1-v)\) give an exponentially smaller contribution, uniformly for \(u\in I\). The extra factor \(v^{-\beta}\) is harmless on the Gaussian region and is absorbed by the strictly stronger exponential at \(v\downarrow0\). Consequently the tilted expectation divided by \(v_{n,u}^{-\beta}\) tends to one, proving (2).

**Step 3: coalescing-weight singular-value profile.** Differentiation under the moment integral gives \(\partial_u\log M_n(u)=-\mathbb E_{\mu_{n,u}}(1-r)^{-\beta}\). Integrating from \(a\) to \(a+\varepsilon\) in (1), and using the uniformity of (2), yields, uniformly for \(\varepsilon\) in any small fixed interval and \(n\to\infty\),
\[
-\log s_{n+1}(J_\varepsilon)
=\frac12\int_a^{a+\varepsilon}\mathbb E_{\mu_{n,u}}(1-r)^{-\beta}\,du
=\frac{\varepsilon n^{\delta}}2\left(\frac2{a\beta}\right)^{\delta}(1+o(1)+O(\varepsilon)).
\]
With \(n=\lfloor t\varepsilon^{-1/\delta}\rfloor\), the coefficient tends to \(c_{a,\beta}\) and the asserted profile follows. For each fixed \(\varepsilon>0\), the same estimate shows stretched-exponential decay of the singular values; hence all positive Schatten memberships.

**Step 4: convergence of all Schatten masses.** The same saddle bounds imply that for some constants \(k_0>0\), \(N_0\), and \(\varepsilon_0>0\),
\[
s_{n+1}(J_\varepsilon)^p\le \exp(-k_0p\varepsilon n^{\delta})
\quad(n\ge N_0,\ 0<\varepsilon\le\varepsilon_0).
\]
For each fixed \(t>0\), Step 3 gives pointwise convergence of the rescaled terms to \(\exp(-p c_{a,\beta}t^\delta)\). The preceding stretched-exponential envelope is integrable in the scaling variable \(t=\varepsilon^{1/\delta}n\); the first \(N_0\) terms vanish after multiplication by \(\varepsilon^{1/\delta}\). Dominated Riemann-sum convergence therefore yields
\[
\varepsilon^{1/\delta}\sum_{n=0}^{\infty}s_{n+1}(J_\varepsilon)^p\longrightarrow
\int_0^\infty e^{-p c_{a,\beta}t^\delta}\,dt
=\Gamma(1+1/\delta)(p c_{a,\beta})^{-1/\delta}.
\]
All steps use positive powers, so the argument holds unchanged in quasi-Schatten classes.

## Verification
The exact diagonal formula (1) can be checked by direct monomial orthogonality. The critical constant is verified independently by differentiating the saddle action: the minimizer of \(2nv+uv^{-\beta}\) is \(v=(u\beta/(2n))^{1/(\beta+1)}\), hence \((\partial_u/2)\min_v(2nv+uv^{-\beta})=2^{\delta-1}(u\beta)^{-\delta}n^\delta\). For \(\beta=1\), \(a=2\) one has \(\delta=1/2\), \(c_{a,\beta}=1/2\), and the displayed Hilbert–Schmidt limit evaluates to \(\Gamma(3)/(2c_{a,\beta})^2=2\). These symbolic checks supplement, rather than replace, the uniform saddle and Riemann-sum proof.

## Relationship to prior work
Zhang–Wang–Hu (2021 preprint) treats Carleson embeddings and Toeplitz/Schatten criteria for exponential Bergman weights. Bourass–El-Fallah–Marrhich–Naqos (2021 preprint, 2022 journal) gives exact leading Hankel singular laws for a related flat radial weight, using monomial moment asymptotics; that method motivates the present boundary saddle but their studied operator is \(H_{\overline z}\), not an identity between coalescing norms. Wang–Xia–Liu (2023) treats Schatten criteria for Toeplitz and Hankel operators, not the near-identity embedding's full rescaled singular spectrum. The claim here is the **sharp uniform near-coalescence profile and gamma-law Schatten blow-up**, not the known qualitative compactness of the inclusion or ordinary Laplace asymptotics. No equivalent embedding crossover was found in the checked literature/index, although specialized embedding results could still affect priority.

## Limitations
The result applies to the specific two-parameter exponential radial family and fixed \(a,\beta,p>0\). It does not classify arbitrary radial weights, provide a uniform rate of convergence, or assert originality for general diagonalization of radial Hilbert embeddings.

## References
1. Y. Zhang, X. Wang, Z. Hu, *Toeplitz operators on Bergman spaces with exponential weights*, arXiv:2107.02481v1 (first public 6 July 2021), https://arxiv.org/pdf/2107.02481 .
2. M. Bourass, O. El-Fallah, I. Marrhich, H. Naqos, *On singular values of Hankel operators on Bergman spaces*, arXiv:2102.01743v1 (first public 2 February 2021), https://arxiv.org/pdf/2102.01743 .
3. X. Wang, J. Xia, Y. Liu, *Schatten class operators on exponential weighted Bergman spaces*, Journal of Inequalities and Applications 2023, 129; https://doi.org/10.1186/s13660-023-03031-y .
