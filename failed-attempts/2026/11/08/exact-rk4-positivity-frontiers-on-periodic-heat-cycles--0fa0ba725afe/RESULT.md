# Exact RK4 positivity frontiers on periodic heat cycles

## Finding

Let \(n\ge3\) and let \(S_n\) be cyclic shift on \(\mathbb R^n\). With the periodic nearest-neighbor heat generator \(L_n=S_n+S_n^{-1}-2I\), one step of classical four-stage, fourth-order Runge–Kutta at dimensionless time \(h\ge0\) is
\[
T_n(h)=\sum_{k=0}^4\frac{(hL_n)^k}{k!}.
\]
Then \(T_n(h)\) maps *every* nonnegative vector into a nonnegative vector if and only if \(0\le h\le c_n\), where the entire exact classification is
\[
\begin{array}{c|c}
n&c_n\\\hline
3&\text{unique positive root of }9h^3-12h^2+12h-8=0\\
4&\text{unique positive root of }8h^3-8h^2+6h-3=0\\
5&\text{unique positive root of }55h^3-60h^2+48h-24=0\\
6&1/2\\
7&4/7\\
n\ge8&1/2
\end{array}
\]
Numerically, \(c_3=0.928431187801761\ldots\), \(c_4=0.696323390851320\ldots\), and \(c_5=0.720325733182606\ldots\). The dependence on cycle size is not monotone: \(c_5>c_4\) and \(c_7>c_6\), owing to modulo-cycle aliasing of the fourth-degree stencil. For \(n\ge8\), RK4 has exactly the forward-Euler *endpoint positivity* limit \(h=1/2\), although its linear stability window is larger.

In fact, write \(\Lambda_n=4\) for even \(n\), and \(\Lambda_n=2+2\cos(\pi/n)\) for odd \(n\), and let \(\beta\) be the unique positive root of \(\beta^3-4\beta^2+12\beta-24=0\), namely \(\beta=2.78529356340528\ldots\). The spectral \(\ell^2\)-stability window is exactly \(0\le h\le\beta/\Lambda_n\). Its upper endpoint equals \(c_n\) for \(n=3,4\), but is **strictly larger** than \(c_n\) for every \(n\ge5\).

## Assumptions and scope

The state dimension is an arbitrary integer \(n\ge3\), with scalar, uniform, isotropic, one-dimensional periodic nearest-neighbor diffusion. The dimensionless parameter is the physical timestep multiplied by diffusivity and divided by squared mesh spacing. All statements concern exact arithmetic, classical RK4, one complete end-step, and preservation of the **whole nonnegative coordinate cone**, not positivity of individual internal stages, nor the positivity of one particular initial vector. Since \(L_n\mathbf 1=0\), \(T_n(h)\mathbf 1=\mathbf 1\); endpoint positivity is therefore equivalent to \(T_n(h)\) being a stochastic circulant matrix. The diagonal is included in the nonnegativity requirement; positive initial vectors may contain zero entries.

## Proof

**1. Universal nine-point Laurent stencil.** Set \(P_4(z)=1+z+z^2/2+z^3/6+z^4/24\) and expand \(P_4(h(z+z^{-1}-2))=\sum_{j=-4}^{4}a_{|j|}(h)z^j\), with
\[
\begin{aligned}
a_0&=(35h^4-40h^3+36h^2-24h+12)/12,\\
a_1&=h(6-12h+15h^2-14h^3)/6,\\
a_2&=h^2(3-6h+7h^2)/6,\\
a_3&=h^3(1-2h)/6,\\
a_4&=h^4/24.
\end{aligned}
\]
For the \(n\)-cycle the actual coefficient of the matrix power \(S_n^r\) is precisely \(b_{n,r}(h)=\sum_{-4\le j\le4,\ j\equiv r\pmod n}a_{|j|}(h)\). This exhausts **every** matrix entry for **every** \(n\ge3\); no uncomputed tail remains. Equivalence between positivity for all nonnegative states and the inequalities \(b_{n,r}(h)\ge0\) follows by testing the standard basis vectors.

**2. Certificates for the always-positive terms.** For \(h\ge0\), \(a_4\ge0\), \(a_2>0\) whenever \(h>0\), because the quadratic \(7h^2-6h+3\) has negative discriminant and positive leading coefficient. Also
\[
a_0=P_4(-2h)+h^2\big((1-h)^2+5h^2/4\big)>0.
\]
Here \(P_4(-t)>0\) for every \(t\ge0\): Taylor's theorem gives \(P_4(-t)=e^{-t}+e^{-\xi}t^5/120\) for some \(\xi\in(0,t)\) when \(t>0\). Finally \(f(h)=6-12h+15h^2-14h^3\) has \(f'(h)=-12+30h-42h^2<0\) for all real \(h\), and \(f(4/7)=10/7>0\), hence \(a_1\ge0\) throughout \([0,4/7]\).

**3. Small cycles and their one boundary each.** Aliasing gives the following potentially restrictive coefficients, with all the remaining distinct coefficients positive over the intervals claimed:
\[
\begin{array}{c|c|c}
n&\text{critical coefficient}&\text{other nontrivial coefficient}\\\hline
3&b_{3,1}=b_{3,2}=-h(9h^3-12h^2+12h-8)/8&b_{3,0}=(3h^2+2)(3h^2-4h+2)/4>0\\
4&b_{4,1}=b_{4,3}=-h(8h^3-8h^2+6h-3)/3&b_{4,2}=2a_2>0\\
5&b_{5,1}=b_{5,4}=-h(55h^3-60h^2+48h-24)/24&b_{5,2}=b_{5,3}=h^2(5h^2-5h+3)/6>0.
\end{array}
\]
For \(n=4,5\), \(b_{n,0}=a_0+2a_4\) and \(a_0\), respectively, both positive. The displayed quadratics have negative discriminants. Each of the three defining cubics is strictly increasing on \([0,\infty)\): their derivatives are respectively \(27h^2-24h+12\), \(24h^2-16h+6\), and \(165h^2-120h+48\), all positive by negative discriminants. Each cubic starts negative and becomes positive. Thus it has exactly one positive root, the sole nonnegative threshold, and negativity returns forever beyond that root. For strict nonmonotonicity, the fourth-cycle cubic is positive at \(h=7/10\), while the fifth-cycle cubic is negative at \(h=7/10\).

**4. Longer cycles, including the wrap-around anomalies.** When \(n=6\), the distance-three coefficient is \(b_{6,3}=2a_3=h^3(1-2h)/3\). When \(n=7\), the paired distance-three coefficient is \(b_{7,3}=b_{7,4}=a_3+a_4=h^3(4-7h)/24\). For \(n\ge8\), a coefficient \(b_{n,3}=a_3=h^3(1-2h)/6\) is unaliased. These force respectively \(h\le1/2\), \(h\le4/7\), and \(h\le1/2\), with a strictly negative entry at every larger \(h\). Sufficiency is not merely local: for \(h\le1/2\) all five Laurent coefficients are nonnegative; for \(n=7\) and \(1/2<h\le4/7\), \(a_0,a_1,a_2,a_4\) and \(a_3+a_4\) are nonnegative, as already certified. This proves the complete classification.

**5. Difference from spectral stability.** The Fourier eigenvalues of \(L_n\) are \(-4\sin^2(\pi k/n)\), so the maximum modulus is \(\Lambda_n\). The fourth Taylor polynomial satisfies \(P_4(-x)>0\) and \(P_4(-x)-1=x(x^3-4x^2+12x-24)/24\) for \(x>0\). The cubic factor is strictly increasing (derivative \(3x^2-8x+12>0\)), so the exact spectral stability radius is \(\beta/\Lambda_n\). For \(n=3,4\) the two positivity cubics coincide with the spectral boundary after the substitutions \(x=3h\) and \(x=4h\), respectively. For \(n\ge6\), \(c_n\le4/7<11/16<\beta/4\le\beta/\Lambda_n\), using \(\beta>11/4\). For \(n=5\), the defining cubic is positive at \(h=3/4\), so \(c_5<3/4\); meanwhile \(\Lambda_5=(5+\sqrt5)/2<11/3\) and \(\beta>11/4\) give \(\beta/\Lambda_5>3/4\). Thus the gap is strict for every \(n\ge5\).

## Verification

The attached standalone Python standard-library verifier `verify.py` computes all coefficients with `fractions.Fraction`, checks polynomial and finite-cycle alias identities exactly, independently evaluates classical RK4 through its four stages on every basis impulse for cycles of sizes \(3\) through \(30\), and tests rational points on and beyond the boundaries. It returned `VERIFICATION_OK 13403 exact-rational assertions`. The direct derivative, discriminant, alias, and Taylor arguments above—not finite enumeration—prove the assertions for every \(n\) and \(h\) in scope. Reproduce using `python3 verify.py`.

## Relationship to prior work

Omle, Askar and Kovács (2022) examine positivity-preserving explicit time integrators for the heat equation; their motivation is directly related, but their inspected methods and heat experiments do not establish the exact classical RK4 finite-periodic-cycle frontiers. Nüßlein, Ranocha and Ketcheson (2020) analyze positivity-preserving adaptive RK weights and a broader set of ODE/PDE examples; this is not the same fixed-coefficient RK4 matrix positivity classification. Horváth (2005) gives general RK positivity step-size frameworks and a Dirichlet heat equation example with different methods; his work provides the established conceptual background, not the algebraic \(n\)-dependent result here. Existing published numerical work may still contain equivalent or stronger specialized cycle calculations not found in the inspected literature, and a dedicated priority audit remains appropriate. No claim of novelty is made for the RK4 stability polynomial, the finite-difference heat model, or the standard absolute-monotonicity framework.

## Limitations

Only classical explicit RK4 applied to a uniform one-dimensional periodic nearest-neighbor diffusion operator is classified. This is an exact **one-step endpoint** cone-invariance result; it does not imply positivity of internal stages, accuracy of the heat approximation, an RK4 positivity guarantee for arbitrary Markov generators, or a sharp multidimensional/nonperiodic boundary condition. The normalizing mesh factor is essential. Finite numerical checks are supporting reproducibility, not an infinite proof. Independent validation of proof and publication priority has not been performed.

## References

1. F. Omle, S. Askar and E. Kovács, “Systematic testing of explicit positivity preserving algorithms for the heat-equation” (2022), https://doi.org/10.28919/jmcs/7407 (first public date used for literature cohort: 2022-05-31).
2. J. Nüßlein, H. Ranocha and D. I. Ketcheson, “Positivity-Preserving Adaptive Runge-Kutta Methods” (2020), https://arxiv.org/abs/2005.06268.
3. Z. Horváth, “On the positivity step size threshold of Runge–Kutta methods,” *Applied Numerical Mathematics* **53** (2005), 341–356, https://doi.org/10.1016/j.apnum.2004.08.026.
