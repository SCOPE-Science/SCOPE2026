# Global two-term critical slowing in an evolutionary replicator interval map

## Finding
For every \(b\in(0,1)\), set \(B=b(1-b)\), \(a=2/B\) and
\[
F_b(x)=\frac{x}{x+(1-x)\exp(a(x-b))},\qquad 0\le x\le1.
\]
The fixed point \(b\) has multiplier \(-1\), so linear stability theory does not determine the relaxation speed. For **every** initial condition \(x_0\in(0,1)\), the forward orbit \(x_{n+1}=F_b(x_n)\) tends to \(b\). Either an iterate is exactly \(b\), in which case all later iterates are \(b\), or the following two-term statement holds with a finite real constant \(c=c(b,x_0)\):
\[
\boxed{\frac{1}{(x_n-b)^2}
=\frac{4(1-3B)}{3B^2}\,n
+\frac{(2-5B)(4-15B)}{5B^2(1-3B)}\log n
+c+o(1).}
\]
The same constant \(c\) works for **both parities** of \(n\). Both displayed coefficients are strictly positive throughout \(0<B\le1/4\). In particular,
\[
\boxed{\lim_{n\to\infty}n(x_n-b)^2=\frac{3B^2}{4(1-3B)}.}
\]
The eventual-landing exceptional set \(\{x_0\in(0,1):\exists n\ge0,\ F_b^n(x_0)=b\}\) is at most countable. No assertion of a universal, initial-condition-independent finite constant is made.

## Assumptions and scope
All parameters are real; \(b\in(0,1)\) and the selection intensity is fixed at the **critical flip** value \(a=2/[b(1-b)]\). Iterations are indexed by nonnegative integers. All initial points are strictly in the population interval \((0,1)\). Endpoints \(0\) and \(1\) are separately fixed and excluded. The map describes the invariant-diagonal replicator family studied in the cited evolutionary-game papers; no assertion is made about arbitrary off-diagonal two-agent dynamics or selection values away from criticality.

## Proof
**1. Global convergence (including the critical value).** Put \(h(x)=\log[x/(1-x)]\). Direct algebra gives the exact identity
\[
h(F_b(x))-h(x)=-a(x-b),\qquad x\in(0,1).
\]
The only fixed points of \(F_b\) on \([0,1]\) are \(0,b,1\). Suppose there is a genuine two-cycle \(x\ne y\) in the interior. Summing the identity on that orbit implies \(x+y=2b\). Write \(x=b+z\), \(y=b-z\), with \(z\ne0\). The first step then forces
\[
a=\frac{h(b+z)-h(b-z)}{z}=\int_{-1}^{1}h'(b+tz)\,dt.
\]
But \(h'(u)=1/[u(1-u)]\) is **strictly convex**: its second derivative is \(h^{(3)}(u)=2[1-3u(1-u)]/[u^3(1-u)^3]>0\). Strict Jensen inequality yields \(a>2h'(b)=2/B\), a contradiction. A two-cycle touching an endpoint cannot be genuine because both endpoints are fixed. Therefore no genuine period-two orbit exists. By the classical continuous-interval-map convergence theorem (Coppel's theorem: every orbit of a continuous interval self-map without a genuine period-two point converges to a fixed point), each orbit converges to one of \(0,b,1\). For \(x<b\), \(F_b(x)>x\); for \(x>b\), \(F_b(x)<x\). These inequalities exclude convergence to either endpoint from an interior initial state. Thus all interior orbits converge to \(b\). This reproduces the *known* global-attraction property by a short independent argument; global attraction itself is **not** the novelty claim.

**2. Exact local coefficients.** Let \(y=x-b\) and \(B=b(1-b)\). Taylor expansion of the explicit reciprocal-exponential formula through order five gives
\[
F_b(b+y)-b=-y+Cy^3+Dy^4+Ey^5+O(y^6),
\]
where
\[
C=\frac{2(1-3B)}{3B^2},\qquad
D=\frac{2(2b-1)(1-3B)}{3B^3},\qquad
E=\frac{2(30B^2-20B+3)}{15B^4}.
\]
The quadratic coefficient vanishes exactly. Since \(B\le1/4\), \(C>0\). Composing the series with itself cancels the fourth-degree term:
\[
G(y):=F_b^2(b+y)-b=y-2Cy^3+(3C^2-2E)y^5+O(y^6).
\]
These identities are checked by the standalone polynomial-series checker; they also follow by ordinary coefficient multiplication, so no numerical limiting inference is used.

**3. Exact two-term asymptotic.** For an orbit which does not land on the fixed point, define \(y_j=x_{2j}-b\) and \(u_j=y_j^{-2}\). Global convergence implies \(u_j\to+\infty\). For sufficiently large \(j\), \(G(y_j)/y_j=1-2Cy_j^2+O(y_j^4)>0\), so no local sign ambiguity occurs. By the expansion in step 2,
\[
u_{j+1}-u_j=4C+\frac{6C^2+4E}{u_j}+O(u_j^{-3/2}).
\]
Consequently \(u_j=4Cj+O(\log j)\) and, writing \(K=(6C^2+4E)/(4C)\),
\[
\frac{6C^2+4E}{u_j}=\frac Kj+O\left(\frac{\log j}{j^2}\right).
\]
Both error series are absolutely summable, so telescoping \(u_{j+1}-u_j-4C-K(\log(j+1)-\log j)\) proves that \(u_j-4Cj-K\log j\) approaches a finite constant. Elementary simplification gives
\[
K=\frac{3C}{2}+\frac EC=\frac{(2-5B)(4-15B)}{5B^2(1-3B)}>0.
\]
Because \(F_b(b+y)-b=-y+Cy^3+O(y^4)\), the reciprocal-square increment between successive even and odd times satisfies
\[
(x_{2j+1}-b)^{-2}-(x_{2j}-b)^{-2}=2C+O(|y_j|).
\]
The rightmost error tends to zero, and \(\log(2j+1)-\log(2j)\to0\), so the same finite constant exists for the full sequence after subtracting \(2Cn+K\log n\). The stated coefficient of \(n\) is \(2C\), establishing the boxed expansion and leading-square limit.

**4. Exceptional initial conditions.** The explicit derivative has numerator proportional to \(1-a x(1-x)\), hence the map has at most two interior turning points and at most three inverse images of any fixed value. Each finite-level preimage set of \(b\) is finite, so the union over all levels is countable.

## Verification
Execute `python3 verify.py` from the extracted package directory with SymPy installed. It reconstructs the order-five Taylor coefficients using exact symbolic series arithmetic, checks the closed formula for \(K\), and tests four leading-rate and two logarithmic-coefficient examples. The observed output is:

`VERIFY_OK critical_taylor=1 inverse_square_log_coefficient=1 global_rate_cases=4 log_coefficient_cases=2`

Only the exact symbolic manipulations verify identities; finite-iterate tests are corroborative, not exhaustive or proofs of convergence. The global and asymptotic arguments above are analytic.

## Relationship to prior work
The interval family, the flip threshold \(a=2/B\), and global attraction up to the threshold are previously established; see Chotibut–Falniowski–Misiurewicz–Piliouras (arXiv:1807.06831, especially §3 and its earlier global-attraction discussion) and Kryzhevich–Zhang–Chmara (arXiv:2412.16379, §§2–3). The latter paper explicitly separates the global attraction and the emergence of a period-two orbit across the threshold. The 2026 follow-up Kryzhevich–Zhang (arXiv:2603.20685) studies shift maps, statistical invariants and higher-selection chaotic dynamics. Their accessible texts were inspected for the present fixed-point critical relaxation; neither supplies the stated explicit inverse-square logarithmic correction and a single full-sequence constant. Related published mathematical findings treat other scalar maps' critical slowing, not this family and coefficient. Standard parabolic-iteration theory suggests the form, but it does not by itself establish this model-specific closed coefficient or its global validity for all interior initial conditions.

## Limitations
The theorem is only at the exact flip intensity; it does not quantify a joint limit in selection strength and iteration number, and does not classify post-flip attractors. The finite constant \(c\) depends on the initial condition and no closed expression for it is offered. Numerical experiments do not prove the asymptotics. Historical priority is provisional, notably regarding possible uncatalogued discussions of this precise high-order critical expansion in general iteration literature. Independent external validation has not been performed.

## References
1. T. Chotibut, F. Falniowski, M. Misiurewicz, G. Piliouras, *Family of chaotic maps from game theory*, preprint 2018, arXiv:1807.06831; journal version *Dynamical Systems* 36 (2021), 48–63, DOI 10.1080/14689367.2020.1795624. Original finite-interval family, fixed-point threshold and global dynamics.
2. S. Kryzhevich, Y. Zhang, M. Chmara, *Bifurcations and invariant sets for a family of replicator maps from evolutionary games*, first public December 20, 2024, arXiv:2412.16379. Sections 2–3 discuss the same family and established bifurcation frontier.
3. S. Kryzhevich, Y. Zhang, *Shift maps and statistical invariants for some dynamical systems*, first public March 21, 2026, arXiv:2603.20685. Related shift and periodicity theory for the same family.
4. W. A. Coppel, *The solution of equations by iteration*, *Proceedings of the Cambridge Philosophical Society* 51 (1955), 41–43, DOI 10.1017/S030500410002990X. Classical continuous-interval-map convergence criterion used in step 1.
