# A sharp terminal-sampling noise threshold for the integral of fractional Brownian motion at \(H=3/4\)

## Finding

Let \(B\) be standard fractional Brownian motion with Hurst index \(H=3/4\), normalized by
\[\mathbb E[B_sB_t]=\tfrac12(s^{3/2}+t^{3/2}-|s-t|^{3/2}),\quad 0\le s,t\le1.\]
Estimate its area \(J=\int_0^1 B_s\,ds\) from exactly one predetermined noisy reading \(Y_t=B_t+\varepsilon\), where \(\varepsilon\sim N(0,\eta)\) is independent and \(\eta\ge0\). The loss is minimum Bayes mean-square error over all measurable estimators based on this reading. Then:

1. For every \(\eta\ge1/2\), **the unique globally optimal sampling time is \(t=1\)**, and the optimal risk is
\[R_*(\eta)=\frac27-\frac{1}{4(1+\eta)}.\]
2. For every \(0\le\eta<1/2\), no terminal-time design is optimal; at least one global optimizer lies strictly in \((0,1)\).
3. Thus \(\eta=1/2\) is an **exact sharp global endpoint-switching threshold**. This result makes no claim about the uniqueness or explicit location of the interior optimizer below the threshold.

For context, for general persistent fractional Brownian motion \(1/2<H<1\), the terminal observation cannot be globally optimal below \(\eta=(1-H)/(2H-1)\), as follows from an endpoint directional derivative. This general necessary condition is not asserted to be sufficient outside \(H=3/4\).

## Assumptions and scope

The process has stationary increments and the standard Mandelbrot–Van Ness fractional Brownian covariance displayed above; it is not the Riemann–Liouville Volterra variant. Time is restricted to the closed interval \([0,1]\). Exactly one observation is allowed, with fixed nonnegative variance independent of time and process. The observation time is fixed before data are seen; the target is the **one scalar path integral**, not the entire path or a causal path reconstruction. At \(\eta=0\) the reading is noiseless. At \(t=0\) the reading contains no information; the formulas involving a zero denominator are interpreted by their continuous information limit zero.

## Proof

**Exact conditional risk.** Gaussian integration yields
\[\operatorname{Var}(J)=\frac27,\quad v(t)=\operatorname{Var}(B_t)=t^{3/2},\]
\[c(t)=\operatorname{Cov}(J,B_t)=\frac12\left[t^{3/2}+\frac{1-t^{5/2}-(1-t)^{5/2}}{5/2}\right].\]
By Gaussian conditioning the exact Bayes estimator is \(\widehat J_t=c(t)Y_t/(t^{3/2}+\eta)\) when the denominator is nonzero. Its risk is
\[R(t,\eta)=\frac27-I_\eta(t),\qquad I_\eta(t)=\frac{c(t)^2}{t^{3/2}+\eta}.\]
Set \(I_\eta(0)=0\). This is continuous also for \(\eta=0\), since \(c(t)=O(t)\) as \(t\downarrow0\).

**First prove unique endpoint optimality at \(\eta=1/2\).** At \(t=1\), \(c(1)=1/2\), hence \(I_{1/2}(1)=1/6\). For \(0\le t\le3/4\), Cauchy–Schwarz gives \(c(t)^2\le(2/7)t^{3/2}\). As \((3/4)^{3/2}=3\sqrt3/8<7/10\),
\[I_{1/2}(t)\le\frac{(2/7)t^{3/2}}{t^{3/2}+1/2}<\frac16.\]
For \(3/4\le t<1\), use the exact derivatives
\[c'(t)=\frac34\sqrt t+\frac12\bigl((1-t)^{3/2}-t^{3/2}\bigr),\]
\[c''(t)=-\frac34\left(\frac{t-1/2}{\sqrt t}+\sqrt{1-t}\right).\]
Define \(S(t)=2(t^{3/2}+1/2)c'(t)-(3/2)\sqrt t\,c(t)\). Then \(I_{1/2}'(t)\) has the sign of \(S(t)\), and
\[S'(t)=2(t^{3/2}+1/2)c''(t)+\frac32\sqrt t\,c'(t)-\frac34\frac{c(t)}{\sqrt t}.\]
The covariance is positive for \(t>0\). Also, on \([3/4,1]\),
\[c'(t)\le\left(\frac34-\frac t2\right)\sqrt t+\frac12(1-t)^{3/2}\le\frac7{16},\quad \frac32\sqrt t\,c'(t)\le\frac{21}{32}.\]
Write \(M(t)=-2(t^{3/2}+1/2)c''(t)\). On \([3/4,19/20]\), the inequalities \(t^{3/2}+1/2>11/10\), \((t-1/2)/\sqrt t\ge1/4\), and \(\sqrt{1-t}>1/5\) give
\[M(t)>\frac32\cdot\frac{11}{10}\cdot\frac9{20}=\frac{297}{400}>\frac{21}{32}.\]
On \([19/20,1]\), \(t^{3/2}+1/2>7/5\) and \((t-1/2)/\sqrt t\ge9/20\) yield
\[M(t)>\frac32\cdot\frac75\cdot\frac9{20}=\frac{189}{200}>\frac{21}{32}.\]
(The harmless strict inequality at a shared interval endpoint can equally be replaced by a non-strict lower bound; either rational bound remains strict against \(21/32\).) Since \(-3c(t)/(4\sqrt t)<0\), these estimates imply \(S'(t)<0\) on \([3/4,1]\). Direct substitution gives \(S(1)=0\). Thus \(S(t)>0\), and \(I_{1/2}(t)\) is strictly increasing for \(3/4\le t<1\). Together with the Cauchy bound this proves unique global optimality at the threshold.

**Above the threshold.** For every \(t\in(0,1)\), \(c'(t)\ge\sqrt t(3/4-t/2)>0\). Hence \(0<c(t)<c(1)=1/2\). Compare endpoint information via
\[D_\eta(t)=\frac{t^{3/2}+\eta}{4}-(1+\eta)c(t)^2.\]
The preceding result says \(D_{1/2}(t)>0\) for all \(t<1\). Moreover \(\partial D_\eta(t)/\partial\eta=1/4-c(t)^2>0\). Thus \(D_\eta(t)>0\) for every \(\eta\ge1/2\), establishing strict endpoint optimality; \(t=0\) is also inferior. The optimal risk formula follows by substituting \(t=1\).

**Below the threshold.** For \(0\le\eta<1/2\), differentiate the information at \(t=1\). Its derivative has the sign of
\[S_\eta(1)=2(1+\eta)c'(1)-\tfrac32c(1)=\frac{\eta-1/2}{2}<0.\]
Consequently \(t=1\) is strictly inferior to some nearby interior time. Since \(I_\eta(0)=0\) and \(I_\eta\) is continuous and positive somewhere, a global maximum exists and lies in \((0,1)\). This completes the global threshold theorem.

For general \(1/2<H<1\), the same covariance integration gives \(c_H(1)=1/2\) and \(c_H'(1)=H-1/2\); the sign of the terminal derivative is that of \((2H-1)\eta+H-1\), proving the necessary condition stated in the finding.

## Verification

Run `python verify.py` with the packages in `requirements.txt`. The script checks symbolic differentiation, terminal limits, the exact rational inequalities in the global proof, 25 independent numerical integrations of the covariance, and supplementary full-domain risk grids. These computations are cross-checks, not substitutes for the universal analytic proof. In particular, numerical search is **not** used to assert uniqueness of any interior optimizer.

## Relationship to prior work

Abundo and Pirozzi (2019) derive integrated fractional Brownian variance/covariance identities and discuss applications, but do not optimize noisy single-site sampling for the scalar area. Cui and Chronopoulou (2023), including their one-sample Proposition 1, optimize an integral of **pointwise causal path-prediction errors** after a noiseless observation; this is not the mean-square error of one final path integral, and their formulas do not imply the endpoint-noise threshold proved here. Blu and Unser (2006) study fractional-Brownian reconstruction from an integer lattice of noisy measurements, again with a different target and admissible design. Related single-site endpoint transitions for Riemann–Liouville Gaussian Volterra processes do not imply this statement: fractional Brownian motion here has stationary increments and a distinct covariance kernel. No published source inspected establishes the present sharp global threshold. This is a best-knowledge comparison, not a proof of historical uniqueness.

## Limitations

Only the Hurst index \(H=3/4\) has a proved sufficient global endpoint cutoff here. The general \(H>1/2\) expression is a **necessary** condition, not a full classification. Below the cutoff, neither uniqueness nor an exact interior optimum is claimed. The result does not cover multiple, adaptive, time-dependent-noise, correlated-noise, or non-Gaussian observation schemes. Earlier inaccessible or unlocated equivalent work may exist; independent mathematical and historical-priority assessment has not been performed.

## References

- M. Abundo and E. Pirozzi, “On the Integral of the Fractional Brownian Motion and Some Pseudo-Fractional Gaussian Processes,” *Mathematics* **7** (2019), 991, first public online 18 October 2019, https://doi.org/10.3390/math7100991 .
- X. Cui and A. Chronopoulou, “Optimal Sampling for Estimation of Fractional Brownian Motion,” arXiv:2304.07661, first version 16 April 2023, https://arxiv.org/abs/2304.07661 .
- T. Blu and M. Unser, “Optimal interpolation of fractional Brownian motion given its noisy samples,” IEEE 2006, https://bigwww.epfl.ch/publications/blu0601.pdf .
