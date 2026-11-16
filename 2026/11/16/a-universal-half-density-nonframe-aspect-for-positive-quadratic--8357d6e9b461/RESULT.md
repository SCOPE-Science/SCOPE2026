# A universal half-density nonframe aspect for positive quadratic-Gaussian Gabor windows

## Finding

**Theorem.** For any real \(\gamma>0\) and \(c>0\), let
\[
g_{\gamma,c}(t)=(t^2+c)e^{-\gamma t^2},\qquad t\in\mathbb R.
\]
There is an explicitly determined and unique frequency spacing \(b_*=b_*(\gamma,c)>0\) for which the alternating pre-Gramian character \(((-1)^k)_{k\in\mathbb Z}\) annihilates every row of the Gabor pre-Gramian at the origin on the lattice
\[
(a_*,b_*)=\left(\frac1{2b_*},b_*\right),\qquad a_*b_*=\frac12.
\]
In particular, \(\mathcal G(g_{\gamma,c},a_*,b_*)\) is **not a frame** for \(L^2(\mathbb R)\).

To calculate this aspect, define, for \(u>0\),
\[
S(u)=\sum_{k\in\mathbb Z}(-1)^k e^{-u k^2}
=\vartheta_4(0,e^{-u}),\qquad
\Phi(u)=u\frac{S'(u)}{S(u)}.
\]
The function \(\Phi:(0,\infty)\to(0,\infty)\) is a continuous strictly decreasing bijection. Hence the equation
\[
\boxed{\Phi(u_*)=\gamma c,\qquad b_*=\sqrt{\gamma/u_*},\quad a_*=\frac1{2b_*}}
\]
has precisely one solution. This uniqueness concerns the **specified alternating-character obstruction**, not the complete Gabor frame set; other nonframe lattice aspects are not excluded.

The counterexample persists even among **strongly log-concave**, strictly positive, even, strictly unimodal Schwartz windows: that subfamily is precisely \(\gamma c>1\). At \(\gamma c=1\), the window is still strictly log-concave and strictly unimodal, but its logarithmic second derivative vanishes at the origin. At \(0<\gamma c<1\), it has two symmetric off-origin maxima. Thus neither positivity nor strong log-concavity guarantees the frame property on *every* rectangular lattice of redundancy two.

For \(\lambda=\gamma c\), the obstruction parameter obeys the asymptotic laws
\[
\begin{aligned}
 u_*(\lambda)&=\frac{\pi^2}{4(\lambda+1/2)}(1+o(1)),&&\lambda\to\infty,\\
 u_*(\lambda)&=\log(2/\lambda)+\log\log(2/\lambda)+o(1),&&\lambda\downarrow0.
\end{aligned}
\]
In particular, the parameter law is scale-free: \(u_*\) depends only on \(\gamma c\), while \(b_*=\sqrt{\gamma/u_*}\). For example, \(\gamma=1,c=2\) gives \(b_*\approx1.006584233790839\), hence an explicit strongly log-concave nonframe example.

## Assumptions and scope

The Gabor system is normalized as
\[
\mathcal G(g,a,b)=\{e^{2\pi i mbt}g(t-ak):k,m\in\mathbb Z\},
\]
and a frame means that two strictly positive finite constants bound the sum of squared analysis coefficients above and below for every \(L^2\) function. Parameters \(\gamma,c,a,b\) are real and strictly positive. The result concerns separable rectangular lattices of product \(ab=1/2\), one constructed lattice for each window. No assertion is made about the other lattice aspect ratios, the optimal lower frame bound off the obstruction, or higher-degree polynomial factors.

Every \(g_{\gamma,c}\) is a Schwartz function, hence belongs to the Feichtinger algebra \(M^1(\mathbb R)\); its pre-Gramian at \(x\) is the matrix \((g(x+aj-k/b))_{j,k\in\mathbb Z}\). For such windows, the pre-Gramian characterization of the Gabor frame property [1, Proposition 2.1] states that a nonzero bounded sequence in the kernel at any \(x\) is sufficient to disprove the frame property.

## Proof

**Step 1: a unique theta parameter.** By Jacobi's triple product, for \(u>0\),
\[
S(u)=\prod_{n\ge1}(1-e^{-2nu})(1-e^{-(2n-1)u})^2>0.
\]
Logarithmic differentiation is valid locally uniformly in \(u>0\), and yields the absolutely convergent positive series
\[
\Phi(u)=\sum_{n\ge1}
\left[\frac{2nu}{e^{2nu}-1}
+\frac{2(2n-1)u}{e^{(2n-1)u}-1}\right].
\]
For every \(m>0\), \(u\mapsto mu/(e^{mu}-1)\) is strictly decreasing: with \(x=mu\), its derivative has numerator \(e^x(1-x)-1<0\), because this numerator is zero at zero and has derivative \(-xe^x<0\). Since the series of positive terms converges locally uniformly, \(\Phi\) is continuous and strictly decreasing. Clearly \(\Phi(u)\to0\) as \(u\to\infty\). Poisson summation gives
\[
S(u)=2\sqrt{\frac\pi u}\,e^{-\pi^2/(4u)}
\bigl(1+O(e^{-2\pi^2/u})\bigr),\qquad u\downarrow0,
\]
so \(\Phi(u)=\pi^2/(4u)-1/2+O(u^{-1}e^{-2\pi^2/u})\to\infty\). It follows that \(\Phi\) is a strictly decreasing bijection onto \((0,\infty)\), giving the unique \(u_*\) and \(b_*\).

**Step 2: an explicit bounded pre-Gramian kernel.** Set \(b=b_*\), \(a=1/(2b)\), \(u=\gamma/b^2\), and \(v_k=(-1)^k\). Then \(v\ne0\) in \(\ell^\infty(\mathbb Z)\). Every pre-Gramian row at \(x=0\) is absolutely summable, and its action on \(v\) is
\[
\begin{aligned}
(P_g(0)v)_j
&=\sum_{k\in\mathbb Z}(-1)^k g\left(\frac{j/2-k}{b}\right)\\
&=\frac1{b^2}\sum_{k\in\mathbb Z}(-1)^k
\bigl((j/2-k)^2+cb^2\bigr)e^{-u(j/2-k)^2}.
\end{aligned}
\]
If \(j\) is odd, the involution \(k\mapsto j-k\) preserves the squared distance to \(j/2\), and reverses \((-1)^k\), so the sum vanishes. If \(j=2m\) is even, shifting \(k\mapsto k+m\) gives
\[
(P_g(0)v)_{2m}=\frac{(-1)^m}{b^2}
\bigl(cb^2 S(u)-S'(u)\bigr),
\]
because \(\sum_k(-1)^k k^2e^{-uk^2}=-S'(u)\). The chosen theta equation is exactly
\[
cb^2=\frac{S'(u)}{S(u)}
\quad\Longleftrightarrow\quad
\gamma c=u\frac{S'(u)}{S(u)}=\Phi(u).
\]
Therefore \(P_g(0)v=0\) in every row. The pre-Gramian criterion [1, Proposition 2.1] implies that \(\mathcal G(g,a,b)\) is not a frame. Because \(\Phi\) is one-to-one, this particular alternating vector at this pre-Gramian fiber produces an obstruction at exactly one lattice aspect \(b\).

**Step 3: sharp shape classification.** Differentiating directly,
\[
\frac{d^2}{dt^2}\log g_{\gamma,c}(t)
=\frac{2(c-t^2)}{(c+t^2)^2}-2\gamma
\le\frac2c-2\gamma.
\]
The displayed rational term has its maximum \(2/c\) exactly at \(t=0\). Thus the logarithm has uniformly negative curvature exactly when \(\gamma c>1\). At equality, curvature vanishes only at zero and remains strictly negative elsewhere, so the logarithm is still strictly concave. Also
\[
g'_{\gamma,c}(t)
=2t e^{-\gamma t^2}(1-\gamma(t^2+c)).
\]
For \(\gamma c\ge1\), the window is strictly decreasing on \((0,\infty)\); for \(\gamma c<1\), its two maxima occur at \(\pm\sqrt{1/\gamma-c}\). This proves all stated shape claims.

**Step 4: scaling limits.** The Poisson asymptotic above gives \(\lambda=\pi^2/(4u)-1/2+o(1)\) as \(\lambda\to\infty\), proving the first asymptotic. For \(u\to\infty\), the defining theta series gives \(S(u)=1-2e^{-u}+O(e^{-4u})\), whence \(\Phi(u)=2u e^{-u}(1+O(e^{-u}))\). Taking logarithms and solving \(u-\log u=\log(2/\lambda)+o(1)\) yields \(u=\log(2/\lambda)+\log\log(2/\lambda)+o(1)\).

## Verification

The proof is analytic and applies to all \(\gamma,c>0\). The accompanying pure-Python program `CHECK.py` evaluates the product-series representation of \(\Phi\), checks monotonicity over representative samples, solves for obstruction aspects, and numerically verifies all tested pre-Gramian rows and log-curvature bounds. It passed 276 finite consistency assertions when executed. Finite checks do not prove the infinite assertions; those rest on the theta product, Poisson asymptotic, parity cancellation, and published pre-Gramian criterion. No hidden numerical certificate is required.

## Relationship to prior work

Lemvig [1] proves frame existence for all polynomial–Gaussian windows when \(ab<1\) is irrational or, for reduced rational \(ab=p/q\), when \(q-p\) exceeds the polynomial degree. At \(ab=1/2\) and polynomial degree two, neither condition applies. The present theorem supplies a window-specific *nonframe aspect* precisely within that uncovered rational case.

Horst, Lemvig and Videbæk [4, Corollary 4.3(a)(i)] supply a still closer general *conditional* Zak-transform obstruction for **any** even generator at product \(1/2\): a zero at the specified quarter-period Zak fiber implies a nonframe lattice. The present contribution does not claim this conditional implication as new; it proves that **every** window in the positive quadratic-Gaussian family must meet the condition at a unique aspect for the alternating character, including strongly log-concave windows, and derives the explicit theta/asymptotic law. Their main classifications and experiments concern individual Hermite generators rather than this all-positive-quadratic family.

Ulanovskii and Zlotnikov [2] establish a different quantifier order: for each fixed lattice at product \(1/(N+1)\), some polynomial–Gaussian window of degree at most \(N\) is nonframe. This does not imply the present statement that every window in the positive quadratic-Gaussian family has a nonframe lattice at the fixed product \(1/2\). Their parity constructions are relevant prior methodology; uniqueness of the theta obstruction and the strong log-concavity conclusion are additional conclusions here.

Classical favorable frame theorems for totally positive windows [3] concern a different hypothesis from positivity or log-concavity. In particular, \((t^2+c)e^{-\gamma t^2}\) is not a positive Gaussian-scale mixture: as a function of \(s=t^2\), its derivatives satisfy
\[
(-1)^k\frac{d^k}{ds^k}\bigl((s+c)e^{-\gamma s}\bigr)\Big|_{s=0}
=\gamma^{k-1}(\gamma c-k),\qquad k\ge1,
\]
which is negative for all integers \(k>\gamma c\), violating complete monotonicity. Thus positivity and log-concavity of the window alone cannot be substituted for total positivity or a positive Gaussian-scale mixture assumption. No claim of exhaustiveness of all previously unpublished equivalent observations is made.

## Limitations

The theorem proves existence of an explicit nonframe aspect and uniqueness *of its alternating pre-Gramian mechanism*. It does not classify all aspects or all possible bounded pre-Gramian null vectors, and does not assert that other aspects are frames. No extension is claimed for all positive or all strongly log-concave windows beyond the stated polynomial–Gaussian family. An equivalent construction in older Zak-transform or Hermite-combination literature remains a publication-priority risk; the self-review does not replace independent validation.

## References

[1] J. Lemvig, *On the Gabor frame set of polynomial-Gaussian windows*, arXiv:2611.05337, first publicly posted November 3, 2026, Proposition 2.1, Theorems 1–2. https://arxiv.org/abs/2611.05337

[2] A. Ulanovskii and I. Zlotnikov, *Periodic Non-uniqueness Sets for Shift-invariant Spaces and Parity-Based Obstructions to the Frame Property for Gabor Systems*, arXiv:2606.31450, first publicly posted June 30, 2026. https://arxiv.org/abs/2606.31450

[3] K. Gröchenig and J. Stöckler, *Gabor frames and totally positive functions*, Duke Math. J. 162 (2013), 1003–1031. Referenced for the broader distinction between Gaussian-type positive windows and polynomial-Gaussian windows.

[4] A. Horst, J. Lemvig and A. E. Videbæk, *On the non-frame property of Gabor systems with Hermite generators and the frame set conjecture*, Appl. Comput. Harmon. Anal. 76 (2025), article 101747; arXiv:2311.01547, first posted November 2, 2023, Corollary 4.3(a)(i). https://arxiv.org/abs/2311.01547
