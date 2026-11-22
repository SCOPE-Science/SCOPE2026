# A seven-rim reversal between first- and second-order coherence-optimal wheel conductances

## Finding

For each integer \(m\ge3\), let \(W_{m+1}=K_1\vee C_m\) be the wheel with one hub and \(m\) rim vertices. Assign arbitrary nonnegative conductances \(g_e\) to its \(2m\) edges, with \(\sum_e g_e=1\) and connected positive-conductance support. Let \(L(g)\) be the ordinary unnormalized weighted Laplacian, let \(L(g)^+\) be its Moore–Penrose pseudoinverse, and set

\[
F_p(g)=\operatorname{tr}((L(g)^+)^p)=\sum_{j=2}^{m+1}\lambda_j(L(g))^{-p},\qquad p\in\{1,2\}.
\]

Both objectives have **unique global minimizers** over the entire, unrestricted edge-allocation simplex. At their respective optima all spoke conductances equal \(a_{p,m}>0\), all rim-edge conductances equal \(b_{p,m}>0\), and

\[
a_{p,m}=\frac{1-u_{p,m}}m,\qquad b_{p,m}=\frac{u_{p,m}}m,\qquad 0<u_{p,m}<1.\]

The optimal rim-budget fractions satisfy the **exact crossover**

\[
\boxed{u_{2,3}=u_{1,3}=\tfrac12,\quad
u_{2,m}>u_{1,m}\ (4\le m\le6),\quad
u_{2,m}<u_{1,m}\ (m\ge7).}
\]

Moreover,

\[
\boxed{\lim_{m\to\infty}u_{1,m}=\frac13,\qquad
\lim_{m\to\infty}u_{2,m}=\frac{\sqrt7-2}{3}.}
\]

Using the first-order-optimal wheel conductances for the second-order criterion has a strictly positive limiting **relative** regret:

\[
\boxed{\lim_{m\to\infty}\frac{F_2(g^*_{1,m})}{F_2(g^*_{2,m})}
=\frac{\sqrt3/2}{(1+u_\infty)/[(1-u_\infty)(1+3u_\infty)]^{3/2}}
=1.045942437429\ldots,\quad u_\infty=\frac{\sqrt7-2}{3}.}
\]

The crossover is a ranking reversal between two distinct spectral coherence objectives, not merely a change in the magnitude of their optimal values.

## Assumptions and scope

The edge weights are continuous, symmetric, nonnegative, independently adjustable and sum to one. Disconnected weighted supports are inadmissible (equivalently they incur infinite inverse-spectral-trace cost). The graph is a simple wheel; the result is not about self-loop stochastic matrices, directed dynamics or leader placement. The factors that convert \(F_1\) or \(F_2\) to particular noisy-consensus variance normalizations are fixed positive constants and do not affect minimizers. The case \(m=3\) is the complete graph on four vertices.

## Proof

**1. Global uniqueness and orbit symmetry.** Let \(N=m+1\), \(P=\mathbf1\mathbf1^T/N\), and \(X=L+P\). On connected support, \(X\) is positive definite, and \(F_p=\operatorname{tr}(X^{-p})-1\). For a symmetric perturbation \(H\ne0\), diagonalizing \(X\) shows strict positivity of the second derivative of \(\operatorname{tr}(X^{-p})\) for \(p\in\{1,2\}\). For \(p=2\), explicitly,

\[
\frac{d^2}{dt^2}\operatorname{tr}(X+tH)^{-2}\bigg|_{t=0}
=2\operatorname{tr}(X^{-1}HX^{-3}H+X^{-2}HX^{-2}H+X^{-3}HX^{-1}H)>0.
\]

Every nonzero edge-weight perturbation yields \(H\ne0\), because its off-diagonal entries uniquely determine the changed conductances. The objective thus is strictly convex in all edge weights. It diverges when a positive-weight connected graph approaches disconnected support, because a nontrivial eigenvalue approaches zero. Compactness of the budget simplex gives existence and strict convexity gives uniqueness. Rotation of the rim leaves the objective and the budget invariant; uniqueness forces all spoke edges into one class and all rim edges into another. This argument proves globality against nonuniform allocations, not merely optimality within an assumed two-parameter family.

**2. Exact scalar objectives.** Put \(u=mb\), \(a=(1-u)/m\), and

\[\mu_k=2-2\cos(2\pi k/m),\qquad k=1,\ldots,m-1.\]

Fourier diagonalization of the rim and the hub–constant-rim subspace gives the nonzero Laplacian eigenvalues

\[\frac{m+1}{m}(1-u),\qquad \frac1m(1-u+u\mu_k),\quad k=1,\ldots,m-1.\]

Consequently \(F_p=m^p\Phi_p\), where

\[
\Phi_p(u)=\frac{1}{(m+1)^p(1-u)^p}
+\sum_{k=1}^{m-1}\frac{1}{(1-u+u\mu_k)^p},\quad 0\le u<1.
\]

Each summand has positive second derivative except in a zero-slope mode, and the hub summand has strictly positive second derivative; hence \(\Phi_p''(u)>0\). Moreover,

\[
\frac{\Phi_p'(0)}p=(m+1)^{-p}-(m+1)<0,\qquad \lim_{u\uparrow1}\Phi_p(u)=+\infty.
\]

Therefore the respective unique minimizers lie in \((0,1)\), and are characterized exactly by the unique roots of \(\Phi_p'(u)=0\).

**3. Exact finite-size comparison.** Differentiation yields

\[
\frac{\Phi_p'(u)}p=\frac{1}{(m+1)^p(1-u)^{p+1}}
-\sum_{k=1}^{m-1}\frac{\mu_k-1}{(1-u+u\mu_k)^{p+1}}.
\]

For \(4\le m\le10\), the following rational separators \(r_m\) give *exact-rational* derivative signs (not floating-point certificates). The signs are computed by inverting the rational circulant \(A_m(r_m)=(1-r_m)I+r_m L(C_m)\) and evaluating \(-\operatorname{tr}[A_m(r_m)^{-(p+1)}(L(C_m)-I)]-(1-(m+1)^{-p})(1-r_m)^{-(p+1)}\), which is \(\Phi_p'(r_m)/p\). The standalone `verify.py` reproduces every sign with rational Gaussian elimination.

| \(m\) | \(r_m\) | \(\Phi_1'(r_m)\) | \(\Phi_2'(r_m)\) | Consequence |
|---|---|---|---|---|
| 4 | \(119/200\) | positive | negative | \(u_{1,m}<r_m<u_{2,m}\) |
| 5 | \(16/25\) | positive | negative | \(u_{1,m}<r_m<u_{2,m}\) |
| 6 | \(643/1000\) | positive | negative | \(u_{1,m}<r_m<u_{2,m}\) |
| 7 | \(57/100\) | negative | positive | \(u_{2,m}<r_m<u_{1,m}\) |
| 8 | \(1/2\) | negative | positive | \(u_{2,m}<r_m<u_{1,m}\) |
| 9 | \(9/20\) | negative | positive | \(u_{2,m}<r_m<u_{1,m}\) |
| 10 | \(21/50\) | negative | positive | \(u_{2,m}<r_m<u_{1,m}\) |

For the infinitely many sizes \(m\ge11\), define \(q=2-\sqrt3\), \(z=q^m\), \(C=(1+z)/(1-z)\), \(T=z/(1-z)^2\), and

\[S_j=\sum_{k=0}^{m-1}(2-\cos(2\pi k/m))^{-j}.\]

The Poisson-kernel sum and its first two derivatives in the spectral parameter give

\[
S_1=\frac m{\sqrt3}C,\quad
S_2=\frac{2m}{3\sqrt3}C+\frac{2m^2}{3}T,\quad
S_3=\frac m{2\sqrt3}C+\frac{2m^2}{3}T+\frac{m^3}{3\sqrt3}TC.
\]

Set \(D_p=2S_p-3S_{p+1}+1\). Direct substitution shows

\[
\frac{\Phi_p'(1/3)}p=\left(\frac32\right)^{p+1}\left[(m+1)^{-p}-D_p\right],
\]

\[
D_1=1-2m^2T,\qquad
D_2=1-\frac{mC}{6\sqrt3}-\frac{2m^2}{3}T-\frac{m^3}{\sqrt3}TC.
\]

As \(0<q<1/3\), for every \(m\ge3\),

\[
2m^2T<\frac{2m^2 3^{-m}}{(1-3^{-m})^2}
\le\frac{243}{338}<\frac34\le\frac{m}{m+1}.
\]

The middle bound follows because \(m^2 3^{-m}\) and \((1-3^{-m})^{-2}\) decrease for integer \(m\ge3\). Hence \(D_1>(m+1)^{-1}\), so \(\Phi_1'(1/3)<0\). On the other hand, for \(m\ge11\), since \(C>1\) and \(T>0\),

\[D_2<1-\frac{m}{6\sqrt3}<0<(m+1)^{-2},\]

so \(\Phi_2'(1/3)>0\). Strict convexity therefore gives \(u_{2,m}<1/3<u_{1,m}\) for every \(m\ge11\). Finally, \(m=3\) is \(K_4\), and edge-transitivity and uniqueness enforce equal conductances, i.e. \(u_{1,3}=u_{2,3}=1/2\). This completes the exact all-size crossover proof.

**4. Scaling and relative regret.** For any fixed \(u\in(0,1)\), Riemann sums and the elementary cosine integral yield

\[
\lim_{m\to\infty}\frac{F_1(u)}{m^2}=f_1(u)=\frac1{\sqrt{(1-u)(1+3u)}},
\]

\[
\lim_{m\to\infty}\frac{F_2(u)}{m^3}=f_2(u)=\frac{1+u}{[(1-u)(1+3u)]^{3/2}}.
\]

These convergences, together with those of first derivatives, are uniform on compact subintervals of \((0,1)\). The strictly convex objectives have unique roots, and their limiting derivatives change sign uniquely; hence the roots converge to the unique respective minimizers of \(f_1\) and \(f_2\). The first is \(1/3\). The second solves \(3u^2+4u-1=0\), yielding \((\sqrt7-2)/3\). Substitution into \(f_2\) proves the stated relative-regret limit. No numerical enumeration is used to infer any infinite-size result.

## Verification

The standalone standard-library `verify.py` makes 127 successful checks: exact-rational derivative-separator signs; exact agreement of direct full wheel matrix inverses with the Fourier objective for four graph sizes; small-size and numerical all-size diagnostics through 100 rim vertices; and numerical convergence checks at 256, 1024, and 4096 vertices. The infinite-size conclusions instead follow from the analytical inequalities and integrals above. To reproduce: run `python3 verify.py` beside this document; it prints `PASS 127 checks`.

## Relationship to prior work

Ghosh, Boyd, and Saberi introduced convex conductance allocation for total effective resistance and in their 2008 expanded version explicitly solved the **first** inverse spectral moment on weighted wheels (their section 5, pp. 58–60). This is direct prior coverage of the first-order comparator, not of the squared-inverse objective or the crossover between its optimizer and the first-order optimizer. The earlier public conference version (July 2006) describes the general convex conductance design problem but concentrates its worked explicit example on barbells. Patterson and Bamieh (arXiv public October 9, 2013) formulate second-order stochastic network coherence through the **second** inverse spectral moment and analyze fractal networks, not unrestricted conductance design on wheels. Published wheel leader-placement and priced-resistance studies concern different decision variables or spectral functionals and do not directly imply the crossover by restriction or a change of notation. The result uses standard spectral and convex tools; the new claim is the exact all-size reversal and its quantitative asymptotic consequence, not the general principle of optimizing spectral traces.

## Limitations

The proof requires an undirected wheel, a unit linear conductance budget, and the two specific positive inverse powers. It says nothing about more general graphs, other spectral powers, discrete-time stochastic kernels, discrete edge choice, or exogenous edge costs. The 127 program checks are finite reproducibility evidence, not a substitute for the all-size argument. Independent verification and a comprehensive priority determination have not been carried out; the absence of a matching indexed result is not a proof of priority.

## References

1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of MTNS, Kyoto, July 24–28, 2006. https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50(1), 37–66, 2008. Author-available full text: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf
3. S. Patterson and B. Bamieh, *Consensus and Coherence in Fractal Networks*, arXiv:1310.2592, initial submission October 9, 2013. https://arxiv.org/abs/1310.2592
