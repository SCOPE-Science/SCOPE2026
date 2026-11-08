# Exact rank–population threshold ordering and finite-size shift for Brownian resetting

## Finding

For \(N\) independent one-dimensional Brownian searchers with diffusivity \(D>0\), all initially at distance \(d>0\) from an absorbing target and independently returned to their starting positions at Poisson rate \(r\), let \(T_{(k)}(r)\) be the \(k\)-th smallest target-arrival time. For every integer \(N\ge5\) and \(1\le k\le N-4\), the mean has a finite right derivative at zero resetting. In dimensionless variables,
\[
S_{N,k}:=\frac{D^2}{d^4}\left.\frac{\partial}{\partial r}\mathbb E T_{(k)}(r)\right|_{r=0+}=\mathbb E\,G(B_{N,k}),
\qquad B_{N,k}\sim\operatorname{Beta}(N-k+1,k),
\]
where
\[
\begin{split}
q(u)&=\operatorname{erf}\!\left(\frac1{2\sqrt u}\right),\quad
 a(u)=\frac{e^{-1/(4u)}}{2\sqrt\pi\,u^{3/2}},\\
H(u)&=2\sqrt{\frac u\pi}\bigl(e^{-1/(4u)}-e^{-1/u}\bigr)
 -(u+1)\operatorname{erfc}\!\left(\frac1{2\sqrt u}\right)
 +(u+2)\operatorname{erfc}\!\left(\frac1{\sqrt u}\right),\\
G(q(u))&=H(u)/a(u).
\end{split}
\]
The function \(H\) is positive before exactly one zero \(u_*=0.743904342806780476\ldots\), and negative thereafter. Set
\[\phi_*=\operatorname{erfc}(1/(2\sqrt{u_*}))=0.412310175458719274\ldots.\]
Consequently the **sign of zero-resetting mean sensitivity has an exact two-axis single-crossing law**: for a fixed population size, once a rank has negative sensitivity, every larger admissible rank has strictly negative sensitivity; once a rank has positive sensitivity, every smaller rank has strictly positive sensitivity. At fixed rank, enlarging the population can only change the sign from negative to positive, never the reverse. Equality at any one rank makes the respective inequalities strict at all comparable distinct admissible ranks. Negative sensitivity means that an infinitesimal resetting rate *improves* mean arrival time.

Extend the beta expression continuously to real \(k\in(0,N-3)\). For every sufficiently large \(N\) there is one (sign-changing) critical rank \(k_{\mathrm{crit}}(N)\) in this interval, and
\[
\boxed{\displaystyle
k_{\mathrm{crit}}(N)=\phi_*N+c_*+O(N^{-1}),\qquad
c_*=-2.076367087943007658\ldots.}
\]
Precisely, with \(q_*=1-\phi_*\),
\[
c_*=\phi_*+\frac{q_*\phi_*}{2}\frac{G''(q_*)}{G'(q_*)},\qquad
\frac{G''(q_*)}{G'(q_*)}=-20.541225560793936967\ldots.
\]
For sufficiently large populations the critical number of required hits is therefore shifted by about **2.076 ranks** below the naive infinite-population fraction, an order-one finite-size correction.

## Assumptions and scope

Searchers diffuse independently on the half-line and start at the same position \(d\). Each has an independent exponential resetting clock of rate \(r\) returning that searcher instantaneously to \(d\) until it hits the absorbing boundary. The ensemble stops at the \(k\)-th absorption. The local sensitivity exists in the specified range \(N-k\ge4\); the theorem does not assert finite first derivatives for all later ranks. The derivative is at \(r=0+\), and does not determine global resetting-rate optimality.

Dimensionless time is \(u=Dt/d^2\), with dimensionless reset rate \(\rho=rd^2/D\). All displayed constants are independent of the physical scales \(D,d\). The critical-rank continuation is an analytic interpolation of an integer-rank statistic, not a physical fractional-order arrival.

## Proof

**1. Renewal and first derivative.** The unreset survival of a single searcher is \(q(u)\). The single-searcher reset survival has the absolutely convergent renewal expansion
\[
q_\rho(u)=e^{-\rho u}\sum_{j=0}^{\infty}\rho^j q^{*(j+1)}(u),
\]
where \(*\) is ordinary time convolution. Thus
\[\left.\partial_\rho q_\rho(u)\right|_{0+}=(q*q)(u)-u q(u)=H(u).\]
Laplace transforming \(q\), or integrating the two error functions directly, gives the stated elementary expression for \(H\). Its independent check is included in the verifier. The survival probability that fewer than \(k\) of the \(N\) particles have arrived is
\[
P_{N,k}(q)=\sum_{j=0}^{k-1}\binom Nj(1-q)^j q^{N-j},\qquad
P'_{N,k}(q)=N\binom{N-1}{k-1}q^{N-k}(1-q)^{k-1}.
\]
Using \(\mathbb ET_{(k)}=(d^2/D)\int_0^\infty P_{N,k}(q_\rho(u))\,du\), differentiation gives
\[
S_{N,k}=N\binom{N-1}{k-1}
\int_0^\infty q(u)^{N-k}(1-q(u))^{k-1}H(u)\,du.
\]

**2. Justification at the infinite integration boundary.** Since \(q(u)\le(\pi u)^{-1/2}\), the convolution beta integral yields, for \(j\ge0\),
\[q^{*(j+1)}(u)\le u^{(j-1)/2}/\Gamma((j+1)/2).\]
Put \(z=\rho\sqrt u\) and \(F(z)=\sum_{j\ge0}z^j/\Gamma((j+1)/2)\). Elementary separation of the even and odd sums gives, for \(z\ge0\), \(F(z)\le C(1+z)e^{z^2}\) and \(F'(z)\le C(1+z^2)e^{z^2}\), with an absolute constant \(C\). For \(u\ge1\), \(0\le\rho\le1/2\), the renewal expansion and its termwise derivative therefore imply
\[
0\le q_\rho(u)\le C u^{-1/2},\qquad
|\partial_\rho q_\rho(u)|\le C(1+\sqrt u).
\]
Here \(e^{-\rho u+\rho^2u}\le e^{-\rho u/2}\), which controls every polynomial factor in \(\rho u\). On \(0<u\le1\) the same series gives an integrable bound directly. Since \(P'_{N,k}(q_\rho)=O(u^{-(N-k)/2})\) on the tail, the product with the derivative is bounded by \(C u^{-(N-k-1)/2}\), integrable whenever \(N-k>3\). Dominated convergence proves the stated derivative, with no unproved interchange at infinity.

**3. Beta sensitivity and exactly one change of sign.** Changing variables from \(u\) to \(x=q(u)\) uses \(q'(u)=-a(u)\) and maps \(u\in(0,\infty)\) to \(x\in(1,0)\). The preceding integral becomes the expectation of \(G(x)=H(q^{-1}(x))/a(q^{-1}(x))\) under \(\operatorname{Beta}(N-k+1,k)\). At \(x\downarrow0\), \(G(x)\sim-2/(\pi^2x^4)\), making the condition \(N-k>3\) sharp for integrability of this representation.

The derivatives simplify to
\[
H'(u)=-\operatorname{erfc}\!\left(\frac1{2\sqrt u}\right)
+\operatorname{erfc}\!\left(\frac1{\sqrt u}\right)
+\frac{e^{-1/(4u)}}{2\sqrt{\pi u}},
\quad
H''(u)=a(u)\left(\frac1{4u}-\frac32+2e^{-3/(4u)}\right).
\]
With \(y=1/(4u)\), the bracket is \(f(y)=y-3/2+2e^{-3y}\). Its derivative \(1-6e^{-3y}\) has exactly one zero; its value at that minimum is strictly negative, while \(f(0)=1/2\) and \(f(y)\to\infty\). It therefore has precisely two positive zeros. Together with \(H'(0+)=0+\), \(H'(u)\sim-1/(2\sqrt{\pi u})\) as \(u\to\infty\), and \(H(0+)=0+\), \(H(u)=1-\sqrt{u/\pi}+o(\sqrt u)\) at infinity, the resulting convexity–concavity–convexity pattern proves that \(H\) has a unique positive zero, positive before and negative after it. As \(q\) decreases with time, \(G(x)<0\) on \((0,q_*)\), and \(G(x)>0\) on \((q_*,1)\).

**4. Exact sign staircase.** At fixed \(N\), the ratio of two successive beta densities when the rank decreases from \(k\) to \(k-1\) is a positive constant times \(x/(1-x)\), strictly increasing in \(x\). At fixed \(k\), the ratio when the population increases from \(N\) to \(N+1\) is a positive constant times \(x\), likewise strictly increasing. If \(f_2/f_1\) is strictly increasing and \(G\) has one negative-to-positive crossing, then
\[\mathbb E_{f_1}G\ge0\quad\Longrightarrow\quad \mathbb E_{f_2}G>0.\]
Indeed subtract the likelihood-ratio value at the crossing and integrate; the added weighted integral is strictly positive, while the constant multiple of the original expectation is nonnegative. Iterating proves both sign-ordering statements and strictness at equality. This argument requires only the single crossing of \(G\), not monotonicity of its magnitude.

**5. Finite-size shift.** For continuous real \(k\), the same likelihood-ratio ordering applies. If \(k/N\to\phi\in(0,1)\), the beta variable converges in probability to \(1-\phi\), and its expectation of \(G\) converges to \(G(1-\phi)\); endpoint singularity is harmless because both beta shape parameters grow proportionally to \(N\). Hence the two sides of \(\phi_*\) eventually have opposite signs; the strict sign-ordering implies a unique continuous crossing for all large \(N\). Put \(k=\phi_*N+c\) with bounded \(c\). The beta mean and variance satisfy
\[
\mathbb EB_{N,k}=q_*+\frac{\phi_*-c}{N}+O(N^{-2}),\quad
\operatorname{Var}(B_{N,k})=\frac{q_*\phi_*}{N}+O(N^{-2}).
\]
Taylor expansion at \(q_*\), whose higher beta central moments and exponentially small endpoint tails give a uniform \(O(N^{-2})\) remainder, yields
\[
S_{N,k}=\frac1N\left[G'(q_*)(\phi_*-c)+\tfrac12G''(q_*)q_*\phi_*\right]+O(N^{-2}).
\]
Since \(G'(q_*)=-H'(u_*)/a(u_*)^2>0\), solving for the zero gives the claimed \(k_{\rm crit}=N\phi_*+c_*+O(N^{-1})\). To evaluate the coefficient without numerical differentiation,
\[
\frac{G''(q_*)}{G'(q_*)}=-\frac{H''(u_*)}{a(u_*)H'(u_*)}+3\frac{a'(u_*)}{a(u_*)^2},\quad
\frac{a'(u)}{a(u)}=-\frac3{2u}+\frac1{4u^2}.
\]
Evaluating these explicit expressions yields the numerical constants quoted above.

## Verification

The accompanying standalone `verify.py` calculates \(u_*\), \(\phi_*\) and \(c_*\) with high-precision arithmetic, checks an independent time-convolution identity for \(H\), uses Gaussian–Jacobi quadrature for the beta sensitivity, checks the finite-rank staircase for multiple populations, and locates the continuous critical rank at \(N=20,50,100,200\). It reports, respectively, the approximate offsets \(-2.0600693500,-2.0702208953,-2.0733494018,-2.0748715452\), converging to \(c_*\). These tests check formulas numerically; the infinite-population and all-rank assertions follow from the proof above, not from finite tests.

## Relationship to prior work

Vatash, Goldfarb, Rudyak and Roichman (2026) established finite-population rank-resolved resetting first-passage distributions and reported monotone rank dependence of optimal rates, a broader optimization statement that already supports qualitative rank ordering. The separate monotonicity in population at fixed rank, together with the explicit nonzero finite-size critical-rank offset, is the quantitative boundary isolated here. Biroli, Majumdar and Schehr (2023) derived the single-searcher first-order response kernel used here and the special first-arrival population crossover. Belan (2019) analyzed first-passage quantiles under restart and identifies the same infinite-population critical fraction \(\phi_*\). None of those parent statements is claimed as new. The principal assertion assessed here is the **explicit nonzero order-one finite-size critical-rank offset**, with a directly proved local-response population ordering and a complementary rank-ordering proof, under the finite-derivative domain above. The beta-law and the likelihood-ratio proof exhibit how these results follow from the established response kernel without assuming global optimum behavior.

## Limitations

This is a zero-resetting derivative theorem for independent identically initialized diffusion, not a theorem on global optimal rates or correlated/collective resetting. The integer ranks near or above \(N-3\) are outside the proven integrable domain. The continuous critical rank is an interpolation for asymptotic analysis. The sign boundary can lie between physical integer ranks. Numerical constants require the stated dimensionless convention. Earlier unindexed supplements or derivations may contain equivalent order-statistic asymptotics; scientific publication priority is not certified. No independent audit was performed.

## References

1. Vatash, Goldfarb, Rudyak and Roichman, *Rank-dependent optimal resetting in multiparticle search*, arXiv:2609.23542 (first public September 20, 2026), https://arxiv.org/abs/2609.23542.
2. Biroli, Majumdar and Schehr, *Critical number of walkers for diffusive search processes with resetting*, arXiv:2303.18012 (2023), https://arxiv.org/abs/2303.18012.
3. Belan, *Median and Mode in First Passage under Restart*, arXiv:1906.05619 (2019), https://arxiv.org/abs/1906.05619.
4. Lee and collaborators, collective state-dependent search/reset analysis, arXiv:2604.24406 (2026), https://arxiv.org/abs/2604.24406.
