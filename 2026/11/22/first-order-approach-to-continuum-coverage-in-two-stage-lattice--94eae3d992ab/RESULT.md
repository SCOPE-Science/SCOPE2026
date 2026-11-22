# First-order approach to continuum coverage in two-stage lattice parking

## Finding

For every fixed integer \(s\ge2\), consider one-dimensional random sequential adsorption in two stages. First deposit length-\(k\) rods uniformly among the currently feasible positions until none remain; then similarly deposit length-\(s\) rods in every remaining gap, with \(k>s\). Let \(p_{s,k}^{\mathrm I}\) be the limiting expected proportion of covered sites when the substrate length tends to infinity **before** the rod length \(k\) tends to infinity. Write \(p_s\) for the usual length-\(s\) lattice jamming coverage, \(p_\infty\) for the Rényi continuum parking constant, and \(\gamma\) for the Euler–Mascheroni constant. Then

\[
\boxed{\lim_{k\to\infty}k\left[p_s+(1-p_s)p_\infty-p_{s,k}^{\mathrm I}\right]
=(1-p_s)\left[\left(s-\tfrac12\right)p_\infty+\tfrac12e^{-2\gamma}\right]>0.}
\]

In particular, for every fixed \(s\), the two-stage density approaches its known continuum-short-rod limit **from below**, with an explicit positive inverse-length defect. For \(s=2\) the coefficient is approximately \(0.173095891965\).

A useful stronger intermediate estimate is
\[
p_{s,k}^{\mathrm I}=p_s+(1-p_s)p_k-\frac{s(1-p_s)p_k}{k}
+O_s\!\left(\frac{\log k}{k^2}\right).
\]
This separates the finite-short-rod boundary penalty from the first-stage lattice-to-continuum correction.

## Assumptions and scope

At every deposition event choose uniformly among all feasible placements of the prescribed rod length; an accepted rod permanently occupies its sites. Start with a finite integer interval, complete both stages and take the infinite-substrate expectation-density limit. The short length \(s\) is held fixed, \(k\) ranges over integers tending to infinity with \(k>s\). The theorem does not concern the simultaneous competition model, nonuniform rates, or the joint limit in which \(s\) also grows.

Define, for each integer \(r\ge2\),
\[
F_r(t)=\exp\!\left(-2\sum_{j=1}^{r-1}\frac{1-t^j}{j}\right),
\quad p_r=r\int_0^1F_r(t)\,dt,
\quad g_{r,\ell}=2\int_0^1(1-t)t^\ell F_r(t)\,dt
\quad(0\le\ell<r).
\]
The classical gap identities are \(\sum_{\ell=0}^{r-1}g_{r,\ell}=p_r/r\) and \(\sum_{\ell=0}^{r-1}\ell g_{r,\ell}=1-p_r\). Here \(p_\infty=\int_0^\infty W(x)\,dx\), where
\[
W(x)=\exp\!\left(-2\int_0^1\frac{1-e^{-xt}}t\,dt\right).
\]
All integrals are ordinary convergent real integrals.

## Proof

**1. Exact finite short-rod boundary term.** Let \(b_s(n)\) be the expected number of covered sites after length-\(s\) adsorption on an interval of \(n\) sites, with \(b_s(n)=0\) for \(n<s\). Splitting at the first accepted placement yields
\[
(n-s+1)b_s(n)=s(n-s+1)+2\sum_{j=0}^{n-s}b_s(j),\qquad n\ge s.
\]
For \(B_s(z)=\sum_{n\ge0}b_s(n)z^n\) and \(P_{s-1}(z)=\sum_{j=1}^{s-1}z^j/j\), solving the resulting first-order differential equation gives
\[
B_s(z)=\frac{A_s(z)}{(1-z)^2},\quad
A_s(z)=s z^{s-1}e^{-2P_{s-1}(z)}\int_0^z e^{2P_{s-1}(u)}\,du.
\]
The function \(A_s\) is entire, \(A_s(1)=p_s\), and differentiation gives \(A_s'(1)=s-(s-1)p_s\). Subtracting the double and simple poles at \(z=1\), the remaining generating function is entire. Consequently
\[
\boxed{b_s(n)=p_s n-s(1-p_s)+\varepsilon_{s,n},\qquad
\sum_{n\ge0}|\varepsilon_{s,n}|<\infty.}
\]
This uses no unproved assumption on the finite-interval boundary correction.

**2. A uniform small-gap estimate and the two-stage identity.** The known gap formula for \(k\)-rod adsorption gives
\[
p_{s,k}^{\mathrm I}=p_k+\sum_{\ell=0}^{k-1}g_{k,\ell}b_s(\ell).
\]
Set \(H_{k-1}=\sum_{j=1}^{k-1}1/j\). Since \(F_k(t)\le\min\{1,e^{-2H_{k-1}}(1-t)^{-2}\}\),
\[
0\le g_{k,\ell}\le g_{k,0}=O\!\left(\frac{\log k}{k^2}\right)
\quad(0\le\ell<k).
\]
Hence \(\left|\sum_{\ell<k}g_{k,\ell}\varepsilon_{s,\ell}\right|=O_s((\log k)/k^2)\). Substitution of the two exact gap-sum identities proves
\[
p_{s,k}^{\mathrm I}
=p_s+(1-p_s)p_k-s(1-p_s)\frac{p_k}{k}
+O_s\!\left(\frac{\log k}{k^2}\right).
\]

**3. First-order lattice-to-continuum expansion.** We supply the coefficient because replacing it with a mere \(O(k^{-1})\) estimate would not determine the claimed limit. Define \(S_k(x)=\sum_{j=1}^{k-1}(1-e^{-xj/k})/j\) and \(F(x)=\int_0^1(1-e^{-xt})/t\,dt\). The substitution \(t=e^{-x/k}\) gives
\[
p_k=\int_0^\infty I_k(x)\,dx,
\qquad I_k(x)=e^{-x/k-2S_k(x)},\qquad W(x)=e^{-2F(x)}.
\]
Take \(L=k^{1/4}\). Euler–Maclaurin with the integrand \(f_x(u)=(1-e^{-xu})/u\), continuously defined at zero, yields uniformly for \(0\le x\le L\)
\[
S_k(x)=F(x)-\frac{x+1-e^{-x}}{2k}+O\!\left(\frac{x^2}{k^2}\right).
\]
Because \(W(x)=O((1+x)^{-2})\), integration after expanding the exponential shows
\[
\lim_{k\to\infty}k\int_0^L(I_k-W)\,dx
=\int_0^\infty(1-e^{-x})W(x)\,dx=\frac{p_\infty}{2}.
\]
The last equality follows from \(xW'(x)=-2(1-e^{-x})W(x)\) and integration by parts; \(xW(x)\to0\) at both endpoints.

The tail contributes a distinct lattice boundary layer and must **not** be discarded. Put \(\eta=e^{-2\gamma}\) and \(h(y)=e^{-y}/(1-e^{-y})^2\). For \(x\ge L\), summing the geometric logarithm gives
\[
I_k(x)=e^{-2H_{k-1}}h(x/k)e^{-2R_k(x)},\qquad
0\le R_k(x)=\sum_{j=k}^\infty\frac{e^{-xj/k}}j
\le\frac{e^{-x}}{k(1-e^{-x/k})}.
\]
Moreover \(e^{-2H_{k-1}}=\eta k^{-2}(1+O(k^{-1}))\), while \(W(x)=\eta x^{-2}(1+O(e^{-x}/x))\) as \(x\to\infty\). The displayed estimates, with \(L=k^{1/4}\), imply that after multiplying by \(k\), their integrated replacement errors on \([L,\infty)\) vanish. Therefore
\[
\begin{aligned}
\lim_{k\to\infty}k\int_L^\infty(I_k-W)\,dx
&=\eta\int_0^\infty\left[h(y)-\frac1{y^2}\right]dy\\
&=-\frac\eta2.
\end{aligned}
\]
Indeed an antiderivative of the bracket is \(-1/(e^y-1)+1/y\), whose value decreases from \(1/2\) to \(0\). Combining the two regions yields
\[
\boxed{p_k=p_\infty+\frac{p_\infty-e^{-2\gamma}}{2k}+o(k^{-1}).}
\]

**4. Substitution and sign.** Insert the expansion from Step 3 into the identity of Step 2. Since \(p_k\to p_\infty\), the coefficient of \(k^{-1}\) is
\[
(1-p_s)\left[\frac{p_\infty-e^{-2\gamma}}2-sp_\infty\right]
=-(1-p_s)\left[\left(s-\frac12\right)p_\infty+\frac12e^{-2\gamma}\right].
\]
Both \(1-p_s>0\) (each finite rod length leaves a positive limiting vacancy fraction) and the bracket are positive, proving the assertion. The result is an asymptotic eventual inequality; no all-\(k\) monotonicity is asserted.

## Verification

The accompanying `checks.py` verifies the first-placement recurrence against exact enumeration of all possible accepted-placement orders at small substrate sizes, verifies further exact rational recurrence identities, and performs independent numerical quadratures for \(s\in\{2,3,4\}\) and \(k\in\{50,100,200,400\}\). It checks convergence to the derived coefficient. Run `python checks.py` using Python 3 with NumPy and SciPy. The execution completed with `PASS 276 exact and numerical assertions`. These finite checks are diagnostics, not a replacement for Steps 1–4.

## Relationship to prior work

Pinsky's 2026 paper defines precisely these sequential two-stage deposition rules (Model I), obtains the exact single-length and gap-density integrals, and proves the limit \(p_{s,k}^{\mathrm I}\to p_s+(1-p_s)p_\infty\) without a first-order correction. Klaassen and Runnenburg (2001/2003) treat multivariate fixed-length gap-count asymptotic normality, not the present two-length limit. The ordinary lattice parking convergence and an approximate first-order numerical correction for \(p_k\) are classical inputs; neither that correction alone nor Pinsky's limit gives the new staged coefficient without the short-gap boundary calculation. The conclusion concerns a rate of approach, not a new limiting density or the conjectured all-length monotonicity.

## Limitations

The theorem fixes \(s\) and takes the infinite-substrate limit first. Its \(o_s(k^{-1})\) remainder is not uniform in a growing short-rod length, and no claim is made for simultaneous competition or for all finite \(k\). The first-order coefficient is derived analytically; quadrature values are approximate. Independent external mathematical review is not part of this calculation. Historical priority cannot be ruled out for all unindexed sources.

## References

1. R. G. Pinsky, *A new look at some aspects of one-dimensional random sequential adsorption and its continuum limit*, arXiv:2608.04730v1, first posted 2026-08-05, https://arxiv.org/abs/2608.04730. In particular Theorems 1, 2, 4 and 6, pp. 2–10.
2. C. A. J. Klaassen and J. T. Runnenburg, *Discrete Spacings*, arXiv:math/0112056v1 (2001); *Statistica Neerlandica* 57 (2003), 470–483, https://arxiv.org/abs/math/0112056.
3. A. Rényi, *On a one-dimensional problem concerning space-filling*, 1958 (continuum parking constant and its integral representation, as cited by Pinsky).
4. Classical lattice random sequential adsorption formula and numerical lattice correction, https://en.wikipedia.org/wiki/Random_sequential_adsorption (secondary summary; not used as a proof).
