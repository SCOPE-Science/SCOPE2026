# Smooth parameter response of both maximal-entropy measures in heterochaos baker maps

## Finding

**Theorem (smooth-observable parameter response).** Fix any integer \(M\ge2\). Let \(f_{a,b}\) be the three-dimensional heterochaos baker map of Saiki--Takahasi--Yamamoto--Yorke on \([0,1]^3\), with \((a,b)\in\Delta=(0,1/M)^2\). Write \(\mu_{\alpha,a,b}\) and \(\mu_{\beta,a,b}\) for its two ergodic maximal-entropy measures, as defined by the parameter-independent Dyck-shift symbolic measures \(\nu_\alpha,\nu_\beta\). For every integer \(r\ge1\), every \(\Phi\in C^r\) on a neighborhood of \([0,1]^3\), and either \(\gamma\in\{\alpha,\beta\}\), the map
\[
(a,b)\longmapsto I_\gamma(a,b):=\int\Phi\,d\mu_{\gamma,a,b}
\]
is jointly \(C^r\) on \(\Delta\); it is \(C^\infty\) if \(\Phi\) is \(C^\infty\), and real analytic if \(\Phi\) is a polynomial. First derivatives have explicit absolutely convergent symbolic series, given below. The center-coordinate marginal \((x_c)_*\mu_{\gamma,a,b}\) does not depend on \(a\) or \(b\) (even when tested against bounded Borel observables). In particular, Conjecture 2.7 of the originating paper holds for every \(C^1\) observable and is strengthened to arbitrary finite differentiability for correspondingly smooth observables.

## Assumptions and scope

The symbol set is \(\mathcal D=\{\alpha_1,\dots,\alpha_M,\beta_1,\dots,\beta_M\}\). For \(1\le k\le M\), the base expansion on the \(\alpha_k\) branch is \(u\mapsto(u-(k-1)a)/a\), and on the \(\beta_k\) branch is \(u\mapsto(u-Ma)/(1-Ma)\). The center maps are \(c\mapsto(c+k-1)/M\) on \(\alpha_k\), and \(c\mapsto Mc-k+1\) on \(\beta_k\). The stable maps are \(s\mapsto(1-Mb)s\) on \(\alpha_k\), and \(s\mapsto bs+1+b(k-M-1)\) on \(\beta_k\), with the canonical branch domains and boundary convention of the cited model.

The symbolic shift \(\Sigma_\mathcal D\) is its two-sided Dyck coding. The probability laws \(\nu_\alpha\) and \(\nu_\beta\) on that coding are the two explicit, parameter-independent ergodic measures of maximal entropy identified in the originating literature. Their almost-sure singleton inverse coding is assumed only as the *published theorem* (Lemma 3.7 and equations (3.8)--(3.9) of arXiv:2401.00836v2), not inferred from a numerical simulation. All formulas hold for each of these two measures; no claim is made for arbitrary invariant measures or for all continuous observables.

## Proof

**Step 1: a common parameter-independent symbolic coupling.** Set, for \(t\in(0,1/M)\),
\[
\begin{array}{ll}
 g_{\alpha_k,t}(u)=tu+(k-1)t,&g_{\beta_k,t}(u)=(1-Mt)u+Mt,\\
 h_{\alpha_k,t}(s)=(1-Mt)s,&h_{\beta_k,t}(s)=ts+1+t(k-M-1).
\end{array}
\]
Every one of these four types maps \([0,1]\) into itself with positive slope strictly below one. For a two-sided admissible sequence \(\omega\), define
\[
 U_a(\omega)=\lim_{n\to\infty}g_{\omega_0,a}\circ\cdots\circ g_{\omega_{n-1},a}(0),\qquad
 S_b(\omega)=\lim_{n\to\infty}h_{\omega_{-1},b}\circ\cdots\circ h_{\omega_{-n},b}(0).
\]
These are the unique bounded forward-unstable inverse coding and backward-stable forward coding, respectively. The defining center branch maps contain neither \(a\) nor \(b\). The cited singleton-coding lemma implies that on a fixed, full \(\nu_\gamma\)-measure set (for each \(\gamma\)), the center cylinder intersection is a singleton \(C(\omega)\), independent of the parameters. Hence, simultaneously for each \((a,b)\in\Delta\),
\[
\mu_{\gamma,a,b}=(\omega\mapsto(U_a(\omega),C(\omega),S_b(\omega)))_*\nu_\gamma.
\]
The exceptional coding set can be chosen parameter-independent because the symbolic laws and center branch constraints are parameter-independent; the contracting outside coordinates are defined for *every* symbolic sequence.

**Step 2: uniform convergence of every parameter derivative.** Write each affine factor \(g_{\omega_j,t}(u)=A_j(t)u+B_j(t)\), and similarly for \(h\). The coefficients \(A_j,B_j\) are affine in \(t\), with \(|A'_j|\le M\), \(|B'_j|\le M\), \(|B_j|\le1\). On an arbitrary compact parameter interval \(K\subset(0,1/M)\), choose \(0<\rho_K<1\) such that \(|A_j(t)|\le\rho_K\) for all \(j,t\in K\). The \(n\)-to-\(n+1\) increment of either coding series is exactly
\[
 D_n(t)=B_n(t)\prod_{j=0}^{n-1}A_j(t).
\]
For each fixed derivative order \(q\ge0\), the product rule, the vanishing of all coefficient derivatives of order two or higher, and the bounds above give
\[
\sup_{t\in K,\omega}|\partial_t^q D_n(t)|\le C_{q,K,M}(n+1)^q\rho_K^{n-q}\qquad(n\ge q),
\]
with the finitely many \(n<q\) treated separately. This is summable in \(n\), uniformly in \(\omega\). Thus both \(U_a(\omega)\) and \(S_b(\omega)\) depend \(C^\infty\)-smoothly on their own parameter, with every derivative uniformly bounded on compact parameter intervals. The other parameter does not enter the corresponding series.

**Step 3: differentiate under the fixed symbolic measure.** For \(\Phi\in C^r\), apply the ordinary chain rule to \(\Phi(U_a(\omega),C(\omega),S_b(\omega))\). The preceding derivative bounds and compactness of \([0,1]^3\) dominate each mixed derivative up to total order \(r\) uniformly on compact parameter rectangles. Dominated differentiation therefore proves the asserted joint \(C^r\) response. In particular,
\[
\partial_a I_\gamma=\int (\partial_u\Phi)(U_a,C,S_b)\,\partial_a U_a\,d\nu_\gamma,\qquad
\partial_b I_\gamma=\int (\partial_s\Phi)(U_a,C,S_b)\,\partial_b S_b\,d\nu_\gamma.
\]
Both coding derivatives have explicit absolutely convergent expansions: writing \(P_n=\prod_{j<n}A_j\),
\[
\partial_t U_t=\sum_{n\ge0}(P'_nB_n+P_nB'_n)
\]
for the unstable coefficient sequence, with the identical expression for \(\partial_t S_t\) using the past stable coefficient sequence. Here \(P'_n=\sum_{j<n}A'_j\prod_{0\le i<n,\ i\ne j}A_i\), and the empty product is one. Uniform convergence follows from Step 2.

**Step 4: analyticity and center rigidity.** For polynomial \(\Phi\), complexify \(a,b\) near any fixed real parameter pair. All affine slopes still have modulus below one on a sufficiently small complex neighborhood, uniformly in the symbolic sequence, so the two coding series converge uniformly as holomorphic functions there. The polynomial composition does as well; integration against the fixed probability \(\nu_\gamma\) preserves holomorphy, establishing real analyticity. Finally, because \(C(\omega)\) and \(\nu_\gamma\) are parameter-independent, the pushforward law \(C_*\nu_\gamma\) is fixed, proving the center-marginal statement without a smoothness hypothesis on its test function.

## Verification

The accompanying standard-library Python file `check_affine_response.py` tests the four affine branch formulas using exact fractions for \(M=2,3,4\), two interior rational parameter values for each \(M\), both outside coordinates, and all words through length four. Two algebraically independent implementations of finite compositions and their first derivatives agree, the images remain in the unit interval, and checked truncation increments obey the stated first-order envelope. The program reports 105496 successful rational assertions. These finitely many calculations are corroboration only; the uniform infinite-word bounds in Step 2 are the proof of smoothness.

## Relationship to prior work

Saiki--Takahasi--Yamamoto--Yorke (arXiv:2401.00836v2) establish the two symbolic maximal-entropy measures, an almost-sure singleton coding (Lemma 3.7), and **weak-star continuity** of the corresponding measures with respect to \((a,b)\) (Theorem 2.6). Their **Conjecture 2.7** explicitly asks for differentiability of the integral of suitable observables against these measures. The present result proves that differentiability for every \(C^1\) observable and all higher orders for correspondingly smooth observables, exploiting parameter-free symbolic laws and two uniformly contracting *outside-coordinate* codings. It does not claim differentiability in the dual norm of all continuous functions or total variation. Takahasi--Yamamoto (arXiv:2209.04905) supply the symbolic underpinning; Takahasi (arXiv:2307.08119) studies mixing; Takahasi (arXiv:2409.01261) studies periodic-point equidistribution, not this parameter response.

## Limitations

The result applies to the specified three-dimensional *affine* model, the two named maximal-entropy laws and observables with the stated differentiability. It does not show stability under nonlinear perturbations, differentiability for arbitrary continuous observables, differentiability in total variation, a uniform bound approaching the boundary of \(\Delta\), or independent scholarly confirmation of publication priority. The centered coordinate remains nonuniform, but its exact parameter independence is enough for the stated class of tests.

## References

1. Saiki, Takahasi, Yamamoto and Yorke, *The dynamics of the heterochaos baker maps*, arXiv:2401.00836v2 (2024), Sections 1.1, 2.4, 3.5--3.6 and 4.3.
2. Takahasi and Yamamoto, *Heterochaos baker maps and the Dyck system: maximal entropy measures and a mechanism for the breakdown of entropy approachability*, arXiv:2209.04905.
3. Takahasi, *Exponential mixing for heterochaos baker maps and the Dyck system*, arXiv:2307.08119.
4. Takahasi, *Distributions of periodic points for the Dyck shift and the heterochaos baker maps*, arXiv:2409.01261.
