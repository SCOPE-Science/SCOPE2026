# Dual high-energy occupation laws and beta reaction-flux moments for the classical Lotka–Volterra oscillator

## Finding
For the normalized classical predator–prey equations
\[
\dot u=u(1-v),\qquad \dot v=v(u-1),\qquad (u,v)\in(0,\infty)^2,
\]
write \(f(z)=z-1-\log z\) and \(L=f(u)+f(v)>0\). Every positive energy level \(L\) is a periodic orbit, of least period \(T_L\). Let \(\mu_L\) be normalized **physical-time** occupation on that orbit. Then \(\mathbb E_{\mu_L}[uv]=1\), so
\[
 d\nu_L=uv\,d\mu_L
\]
is a probability measure, the **reaction-flux occupation law**. Let \(S\) be uniform on \([0,1]\). As \(L\to\infty\), both limits hold with the stated quantitative rates:
\[
 W_1\!\left(\mathcal L_{\mu_L}\left(-\frac{\log u}{L},-\frac{\log v}{L}\right),\mathcal L(S,1-S)\right)=O\!\left(\frac{\log L}{L}\right),
\]
\[
 W_1\!\left(\mathcal L_{\nu_L}\left(\frac{u}{L},\frac{v}{L}\right),\mathcal L(S,1-S)\right)=O\!\left(\frac{\log L}{L}\right).
\]
Here \(W_1\) uses the \(\ell^1\) distance on \(\mathbb R^2\). In particular, for every pair of fixed integers \(r,s\ge1\),
\[
 L^{2-r-s}\,\mathbb E_{\mu_L}[u^r v^s]
 =\frac{(r-1)!(s-1)!}{(r+s-1)!}
 +O_{r,s}\!\left(\frac{\log L}{L}\right).
\]
These are **two distinct samples of the same orbit**: ordinary time samples exponentially small concentrations, whereas reaction-weighted time samples concentrations of order \(L\). The joint limiting shapes coincide although the raw scales do not.

## Assumptions and scope
All statements use the fixed parameter-free symmetric normalization displayed above, on its strictly positive compact nonconstant energy curves. The asymptotic parameter \(L>0\) is \(u+v-\log(uv)-2\), **twice** the energy \(h\) in Boulnois (2023). Measures are normalized in the original physical time, not logarithmic time or Hamiltonian angle. No convergence is claimed for arbitrary unequal natural growth/decay rates, noisy systems or discrete-time approximations. Rates are upper bounds, not asserted sharp.

## Proof
**1. Geometry and exact flux normalization.** Since \(f\) is nonnegative, strictly convex, has minimum \(f(1)=0\), and diverges at both endpoints of \((0,\infty)\), every \(L>0\) level is a regular simple closed curve. Direct differentiation gives \(d(f(u)+f(v))/dt=0\). The unique equilibrium is \((1,1)\), excluded by \(L>0\); hence the level is periodic. Periodicity of \(\log u,\log v,u\) gives
\[
 \mathbb E_{\mu_L}[v]=1,\quad
 \mathbb E_{\mu_L}[u]=1,\quad
 0=\mathbb E_{\mu_L}[u(1-v)],\quad
 \mathbb E_{\mu_L}[uv]=1.
\]
This proves \(\nu_L\) is a probability without an asymptotic normalization.

**2. Inverse branches and integrable distortion.** For \(q>0\) let \(a(q)<1<b(q)\) solve \(f(z)=q\). The inverse derivatives satisfy \(a'(q)=1/f'(a)<0\), \(b'(q)=1/f'(b)>0\). Taylor expansion at \(1\) and elementary growth comparisons imply
\[
 \frac{a(q)}{1-a(q)}=O(q^{-1/2})\quad(q\downarrow0),\qquad
 \frac{1}{b(q)-1}=O(q^{-1/2})\quad(q\downarrow0),
\]
\[
 \frac{a(q)}{1-a(q)}=O(e^{-q})\quad(q\to\infty),\qquad
 \frac{1}{b(q)-1}=O(q^{-1})\quad(q\to\infty).
\]
Indeed \(f(1+w)=w^2/2+O(w^3)\); for large \(q\), \(a(q)e^{-a(q)}=e^{-q-1}\) and \(b(q)=q+1+\log b(q)\). Consequently, with
\[
 F_-(q)=\frac{a(q)}{1-a(q)},\qquad F_+(q)=\frac{1}{b(q)-1},
\]
one has \(\int_0^\infty F_-(q)\,dq<\infty\) and \(\int_0^Q F_+(q)\,dq=O(\log(2+Q))\).

Let \(u_-<1<u_+\) solve \(f(u_\pm)=L\). On each horizontal branch, set \(q(u)=L-f(u)\); then \(v_-(u)=a(q(u))<1\) and \(v_+(u)=b(q(u))>1\). The exact positive-time elements (respectively increasing and decreasing \(u\)) are
\[
 dt_-=\frac{du}{u(1-v_-(u))},\qquad dt_+=\frac{du}{u(v_+(u)-1)},\qquad u_-<u<u_+,
\]
where the second is integrated with increasing \(u\) only to express its positive duration. For later use define
\[
 A_L=\int_{u_-}^{u_+}\frac{v_-}{u(1-v_-)}\,du,\quad
 B_L=\int_{u_-}^{u_+}\frac{du}{u(v_+-1)},\quad
 C_L=\int_{u_-}^{u_+}\frac{du}{v_+-1},\quad
 D_L=\int_{u_-}^{u_+}\frac{v_-}{1-v_-}\,du.
\]
The inverse-branch bounds yield \(A_L=O(1)\), \(B_L=O(\log L)\), \(C_L=O(\log L)\), \(D_L=O(1)\). Here is a uniform justification rather than an unproved endpoint assertion. On \(u\le1/2\), change variable \(q\) using \(dq/d\log u=1-u\in[1/2,1]\), so the first two integrals are bounded by twice the corresponding \(q\)-integrals. On \(u\ge2\), use \(dq/du=-(1-1/u)\in[-1,-1/2]\) and \(du/u\le du/2\); hence all four are bounded by constant multiples of their \(q\)-integrals (and \(D_L\) by that for \(F_-\)). On \(1/2\le u\le2\), for large \(L\) the quantity \(q\ge L-O(1)\), so all four integrals are uniformly bounded using the large-\(q\) bounds. For \(D_L\) on \(u\le1/2\), simply use \(du=u\,d\log u\le d\log u\); for \(C_L\) on \(u\le1/2\), use \(du\le d\log u\). This establishes all estimates including integrable square-root turning points.

**3. Physical-time logarithmic occupation.** At the endpoints, \(u_-=e^{-L-1+u_-}\) and \(u_+=L+1+\log u_+=L+O(\log L)\), so \(\log(u_+/u_-)=L+O(\log L)\). Since \(1/(1-v_-)=1+v_-/(1-v_-)\),
\[
 T_L=\log(u_+/u_-)+A_L+B_L=L+O(\log L).
\]
On the increasing branch with \(u_-\le u\le1\), \(dt_-=d(\log u)+F_-(q(u))\,d(\log u)\). The integrated distortion is \(O(1)\), and the omitted parts of both branches have total duration \(O(\log L)\) (the increasing part with \(u>1\) has logarithmic length \(O(\log L)\)). Thus \(\mu_L\), except for mass \(O(\log L/L)\), is the pushforward of normalized Lebesgue measure in \(\log u\in[\log u_-,0]\). The variable \(-\log u/L\) is therefore uniform on an interval differing from \([0,1]\) by \(O(1/L)\). Along that branch, the energy equation gives
\[
 -\frac{\log v}{L}=1+\frac{2-u-v}{L}+\frac{\log u}{L},
\]
with \(0<u,v\le1\), so the \(\ell^1\) distance to \((S,1-S)\) is \(O(1/L)\) under a suitable coupling. The remaining \(O(\log L/L)\) mass lies in a uniformly bounded region of scaled log coordinates: for either species \(-L-1\le\log z\le\log u_+=O(\log L)\). Coupling it arbitrarily proves the first \(W_1\) bound.

**4. Flux-weighted linear occupation.** The exact branch formula for any bounded Borel \(\Phi\) is
\[
 \int\Phi(u/L,v/L)\,d\nu_L
 =\frac1{T_L}\int_{u_-}^{u_+}\left[
 \frac{v_-}{1-v_-}\Phi(u/L,v_-/L)+
 \frac{v_+}{v_+-1}\Phi(u/L,v_+/L)\right]du.
\]
The first branch has total mass \(D_L/T_L=O(1/L)\). On the second branch \(v_+/(v_+-1)=1+1/(v_+-1)\), and the excess has integral \(C_L=O(\log L)\). The portion \(u<1\) under the unit weight has bounded length, and \(u_+/L=1+O(\log L/L)\). Therefore, up to total-variation error \(O(\log L/L)\), its \(u/L\) marginal is uniform on \([0,1]\). On the dominant segment \(u\ge1\), both species lie in \([1,u_+]\), and the energy equation says
\[
 \frac{u+v_+}{L}=1+\frac{2+\log u+\log v_+}{L}
 =1+O\!\left(\frac{\log L}{L}\right).
\]
The support of \((u/L,v/L)\) is uniformly bounded, so a coupling proves the second \(W_1\) estimate.

**5. Beta moments.** Since \(d\nu_L=uv\,d\mu_L\), exactly
\[
 L^{2-r-s}\mathbb E_{\mu_L}[u^r v^s]
 =\mathbb E_{\nu_L}\left[(u/L)^{r-1}(v/L)^{s-1}\right].
\]
For fixed \(r,s\ge1\), the polynomial on the right is Lipschitz on the uniformly bounded concentration domain \([0,u_+/L]^2\), with \(u_+/L\le2\) for all sufficiently large \(L\). Applying the second \(W_1\) estimate produces its integral on \((S,1-S)\): \(\int_0^1 t^{r-1}(1-t)^{s-1}dt=B(r,s)\), with the claimed error. No numerical experiment is used to justify the infinite limit.

## Verification
A standalone symbolic and quadrature reproducibility script is included as `check_dual_occupation.py`. Symbolic checks verify the conserved energy, the exact generator identities, the positivity/normalization of the flux measure, and the beta-moment coefficients. Representative finite-energy quadratures corroborate the two different scalings and the period normalization, but do **not** prove convergence. The proof above supplies global branch estimates and explicit treatment of the turning-point singularities. All constants implicit in the estimates depend only on fixed integer moment orders where indicated.

## Relationship to prior work
The classical oscillator, its conserved energy, exact quadratures and large-energy period growth are longstanding. Boulnois (2022, arXiv:2301.00673v1) provides analytic orbit/time representations and high-energy period approximations; Boulnois (2023, arXiv:2303.09317v1), Sections 2–5, derives an exact solution in the same equal-natural-rate normalization and a period quadrature. The later combined treatment (Boulnois, 2023, *Hybrid Species and Closed-Form Solutions of the Lotka–Volterra Equations*) similarly addresses integration and periods. An independently published stationary-measure result for the classical Lotka–Volterra flow establishes the exact conditional means and vanishing covariance, subsuming the normalization \(\mathbb E[uv]=1\); it does not assert the two high-energy occupation distributions or their beta mixed moments. The novelty claim is solely the **quantitative paired ordinary-time and flux-time scaling laws, and the resulting all-order mixed-moment constants**. We do not claim invention of energy quadratures, periods, or stationary mean identities.

## Limitations
The \(O(\log L/L)\) rates may not be optimal. The dual laws are for the symmetric normalized classical oscillator only, not arbitrary unequal-rate prey-predator systems. The exact first and mixed stationary moments are not new; the asymptotic joint higher-moment law is the claimed contribution. The proof establishes theoretical limits, not confidence intervals or stochastic population statistics. Unindexed earlier occupation calculations, and later derivative calculations from existing quadratures, remain possible publication-priority risks. Independent audit has not been performed.

## References
1. J.-L. Boulnois, *Predator-Prey Linear Coupling with Hybrid Species*, arXiv:2301.00673v1 (first public 2022-12-29), https://arxiv.org/abs/2301.00673 .
2. J.-L. Boulnois, *An Exact Closed-Form Solution of the Lotka–Volterra Equations*, arXiv:2303.09317v1 (first public 2023-03-08), https://arxiv.org/abs/2303.09317 .
3. J.-L. Boulnois, *Hybrid Species and Closed-Form Solutions of the Lotka–Volterra Equations*, American Journal of Biomedical Science & Research 18 (2023), https://doi.org/10.34297/AJBSR.2023.18.002503 .
4. *Mutual mean-independence and exact zero covariance in the classical Lotka–Volterra flow*, published finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mutual-mean-independence-and-exact-zero-covariance-in-the-classi--5a8ff27e72a6 .
