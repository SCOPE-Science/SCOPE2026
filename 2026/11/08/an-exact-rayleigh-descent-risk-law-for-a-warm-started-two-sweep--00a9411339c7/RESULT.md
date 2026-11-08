# An exact Rayleigh-descent risk law for a warm-started two-sweep power step

## Finding

Let \(a>b>0\), \(A=\operatorname{diag}(a,b)\), and choose a unit vector \(x_0=(c,s)^\mathsf T\) with \(cs\ne0\). Form one ordinary power warm-start and then one parameterized two-sweep step:
\[
u=\|Ax_0\|_2,\quad x_1=Ax_0/u,\qquad
x_2=\frac{Ax_1+\beta x_0}{\|Ax_1+\beta x_0\|_2},\qquad
\mu_i=x_i^\mathsf T A x_i,
\]
where \(\beta\in\mathbb R\). Then the second normalization is always defined and
\[
\boxed{\mu_2<\mu_1\ \Longleftrightarrow\ |\beta|u>ab.}
\]
Equality of the two Rayleigh quotients holds precisely when \(|\beta|u=ab\); otherwise the inequality is reversed. Consequently, \(\mu_2\ge\mu_1\) for *every* non-eigenvector start if and only if \(|\beta|\le b\), whereas \(\mu_2<\mu_1\) for *every* such start if and only if \(|\beta|\ge a\).

For a Haar-uniform \(x_0\) on the unit circle, the exact chance \(P_{a,b}(\beta)\) of strict Rayleigh decrease is
\[
\boxed{
P_{a,b}(\beta)=\begin{cases}
0,&|\beta|\le b,\\[2pt]
\dfrac2\pi\arccos\sqrt{\dfrac{b^2(a^2/\beta^2-1)}{a^2-b^2}},&b<|\beta|<a,\\[7pt]
1,&|\beta|\ge a.
\end{cases}}
\]
For an allowable risk \(0\le\alpha<1\), the exact necessary and sufficient parameter cap is
\[
\boxed{P_{a,b}(\beta)\le\alpha\quad\Longleftrightarrow\quad
|\beta|\le\frac{ab}{\sqrt{b^2+(a^2-b^2)\cos^2(\pi\alpha/2)}}.}
\]
At the two critical magnitudes the probability has a square-root onset and saturation: as \(\varepsilon\downarrow0\),
\[
P_{a,b}(b(1+\varepsilon))\sim\frac{2\sqrt2\,a}{\pi\sqrt{a^2-b^2}}\sqrt\varepsilon,
\qquad
1-P_{a,b}(a(1-\varepsilon))\sim\frac{2\sqrt2\,b}{\pi\sqrt{a^2-b^2}}\sqrt\varepsilon.
\]

## Assumptions and scope

All computations are in real exact arithmetic. Both eigenvalues of \(A\) are strictly positive and distinct; the initial vector has unit Euclidean norm and nonzero components along both eigenvectors. The warm start \(x_1\) is one ordinary power iteration. Only the subsequent step \(x_2\) uses the two-sweep update with one fixed, freely chosen real coefficient \(\beta\); neither a longer iteration nor a trained parameter rule is assumed. Eigenvectors, which have probability zero under Haar sampling, trivially require separate treatment. Since \(u^2=a^2c^2+b^2s^2\), non-eigenvector starts satisfy \(b<u<a\).

## Proof

Set \(t=\beta u\). Since \(x_1=(ac,bs)^\mathsf T/u\), the two-sweep vector is proportional to
\[
\big((a^2+t)c,(b^2+t)s\big)^\mathsf T.
\]
It cannot vanish: if both coordinates vanished, \(a^2+t=b^2+t=0\), contradicting \(a>b\). The Rayleigh quotient of a nonzero vector \(v=(v_1,v_2)\) is \(b+(a-b)v_1^2/(v_1^2+v_2^2)\). Direct common-denominator subtraction gives the exact identity
\[
\mu_2-\mu_1=
\frac{(a-b)(a^2-b^2)c^2s^2(a^2b^2-t^2)}
{(a^2c^2+b^2s^2)\,[c^2(a^2+t)^2+s^2(b^2+t)^2]}.
\]
The denominator and the factors other than the final parenthesis are strictly positive. This proves the sign statement and its equality boundary. Because \(b<u<a\), the largest possible \(u\) is approached as \(|c|\to1\) and the smallest as \(|c|\to0\). Hence the universal safe cap is exactly \(|\beta|\le b\), while all non-eigenvector starts decrease exactly when \(|\beta|\ge a\). Sharpness outside each cap follows by choosing \(|c|\) sufficiently near its relevant endpoint.

For Haar-uniform \(x_0\), its leading-eigenvector squared mass \(W=c^2\) has the arcsine law \(\operatorname{Beta}(1/2,1/2)\). For \(b<|\beta|<a\), the sign identity is equivalent to
\[
W>q,\qquad q=\frac{b^2(a^2/\beta^2-1)}{a^2-b^2}\in(0,1).
\]
The arcsine tail is \(\Pr(W>q)=2\arccos(\sqrt q)/\pi\), yielding the three branches and endpoint continuity. Inverting this monotone branch proves the risk cap for \(\alpha<1\); at \(\alpha=1\) every real parameter is allowed and the displayed finite cap is not claimed. Finally, expanding \(q\) near \(|\beta|=b\) and \(|\beta|=a\), and using \(\arccos\sqrt{1-z}\sim\sqrt z\) and \(\arcsin\sqrt z\sim\sqrt z\), yields the stated square-root constants.

## Verification

Run `python verify.py` with the bundled standalone Python standard-library checker. It verifies 8,000 exact rational instances of the critical factorization, 40,000 randomized direct normalized two-sweep updates against the sign condition, 36 parameter-and-spectrum cases against a 20,000-angle deterministic circular quadrature, and the two critical asymptotic constants at three scales. Successful execution prints `VERIFY_OK`. The symbolic exact identity and the analytic arcsine tail, not the finite numerical tests, prove the universal and probabilistic assertions.

As an exact benchmark, for \((a,b,|\beta|)=(2,1,3/2)\), one has \(q=7/27\) and
\[
P_{2,1}(3/2)=\frac2\pi\arccos\sqrt{7/27}.
\]
This benchmark gives a reproducible nontrivial probability strictly between zero and one.

## Relationship to prior work

Sun, Peng, Zhang and Vong introduce the two-sweep parameterized power update \(y_{k+1}=Ax_k+\beta_{k-1}x_{k-1}\) and establish convergence criteria and a regression-based parameter-selection scheme. Their paper does not state this exact first-step, two-eigenvalue Rayleigh-monotonicity classification or the Haar-start risk law. Earlier momentum-based power-method analyses by Rabbani and collaborators and by Austin, Pollock and Zhu study acceleration, parameter estimation and convergence, with different normalization or coefficient constructions. The present statement concerns *the particular normalized two-sweep update with one ordinary-power warm-start*, rather than a general assertion about all momentum eigensolvers. Exact algebra for two spectral modes and the classical arcsine law are known ingredients; novelty, if any, lies in their sharp joint algorithmic risk classification and its tuning inversion.

## Limitations

The result covers only two distinct positive eigenvalues, two ambient dimensions, one prescribed warm start and one two-sweep update. A larger number of eigenmodes, different initialization, adaptively chosen coefficients, all-step monotonicity, convergence speed, robustness to roundoff, and the complete regression-enhanced algorithm remain unproved. The displayed decline is relative to the warmed iterate, not necessarily relative to the original vector. The statement does not challenge the originating paper's asymptotic convergence theorems, whose parameter hypotheses differ. The priority comparison cannot eliminate all unpublished or unindexed equivalent formulas.

## References

- T. Sun, X. Peng, J. Zhang and S. Vong, *A Gaussian Process Regression-Enhanced Two-Sweep Parameterized Power Method for Computing Extreme Eigenpairs*, arXiv:2610.41627 (initial public posting October 30, 2026), https://arxiv.org/abs/2610.41627.
- T. Rabbani, A. Jain, A. Rajkumar and F. Huang, *Practical and Fast Momentum-Based Power Methods*, arXiv:2108.09264 (2021), https://arxiv.org/abs/2108.09264.
- C. Austin, S. Pollock and Y. Zhu, *Dynamically accelerating the power iteration with momentum*, arXiv:2403.09618 (2024), https://arxiv.org/abs/2403.09618.
