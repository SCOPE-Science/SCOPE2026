# Sharp universal minimax smoothing of reference leverage scores under rank-one drift

## Finding

Let \(m\ge2\) and \(0\le\theta\le\pi/2\). A reference unit vector \(u\in\mathbb R^m\) is known; an unknown current unit vector \(w\in\mathbb R^m\) satisfies \(|\langle u,w\rangle|\ge\cos\theta\). A sampler commits to a probability vector \(p(u)\) before learning \(w\). Define the row-importance inflation
\[
\Gamma(w,p)=\max_{i:w_i\ne0}\frac{w_i^2}{p_i},
\]
with the quotient interpreted as \(+\infty\) when \(w_i\ne0\) and \(p_i=0\). The universal robust design problem, allowing **arbitrary** reference-dependent probability policies, has exact value
\[
\mathcal R_m(\theta):=\inf_{p(\cdot)}\sup_{\substack{\|u\|_2=\|w\|_2=1\\|\langle u,w\rangle|\ge\cos\theta}}\Gamma(w,p(u))
=\begin{cases}
(\cos\theta+\sqrt{m-1}\sin\theta)^2,&0\le\theta\le\arctan\sqrt{m-1},\\
m,&\arctan\sqrt{m-1}\le\theta\le\pi/2.
\end{cases}
\]
In particular, no nonlinear or discontinuous choice of probabilities from the reference can improve this bound. A universally minimax rule is the leverage/uniform mixture
\[
p_i^*(u)=(1-\eta_*)u_i^2+\frac{\eta_*}{m},\qquad
\eta_*=\begin{cases}
0,&\theta=0,\\
\dfrac{m\sin\theta}{\sqrt{m-1}\cos\theta+(m-1)\sin\theta},&0<\theta<\arctan\sqrt{m-1},\\
1,&\theta\ge\arctan\sqrt{m-1}.
\end{cases}
\]
The mixing weight is unique among **uniform/leverage mixtures** in the open low-angle range. No uniqueness among all reference-dependent policies is asserted. For any positive uncertainty radius, an unsmoothed reference-only leverage distribution has infinite universal inflation; above the sharp angular cutoff uniform sampling is minimax.

## Assumptions and scope

All vectors and probabilities are real. The reference and current subspaces are rank-one, represented by unit vectors; the absolute inner product makes the condition independent of orientation. The sampler sees \(u\) and a guaranteed upper bound \(\theta\), not \(w\), and may select any probability distribution on the \(m\) rows. The objective is the *worst coordinate reweighting ratio*, not expected least-squares error, a tail-optimized design, or the computational cost of evaluating reference leverage scores. An arbitrary small angle is admitted, as are exact zero entries of the reference. At \(\theta=0\), zero sampling probabilities are permitted only at coordinates where the current vector must also vanish; for positive \(\theta\), the proposed rule has full support.

## Proof

**1. An exact envelope for each mixture.** Fix \(0<\eta\le1\), put \(a=1-\eta\), \(b=\eta/m\), and \(p_i=a u_i^2+b\). By reversing the sign of \(w\) if needed, every admissible pair has a representation \(w=\cos\varphi\,u+\sin\varphi\,z\) with \(z\perp u\), \(\|z\|_2=1\), and \(0\le\varphi\le\theta\); the case \(\varphi=0\) can use any such \(z\). Orthogonality gives \(|z_i|\le\sqrt{1-u_i^2}\). With \(t=|u_i|/\sqrt{1-u_i^2}\), including endpoints by continuity,
\[
\frac{w_i^2}{p_i}\le
\frac{(t\cos\varphi+\sin\varphi)^2}{(a+b)t^2+b}
\le \frac{\cos^2\varphi}{a+b}+\frac{\sin^2\varphi}{b}.
\]
The second inequality is weighted Cauchy--Schwarz. Since \(b\le a+b\), the final expression is nondecreasing on \([0,\pi/2]\). Hence the sharp candidate envelope is
\[
F_{m,\theta}(\eta)=\frac{\cos^2\theta}{1-\eta+\eta/m}
+\frac{m\sin^2\theta}{\eta}.
\]
This envelope is **attained**, not merely bounded. For \(0<\theta<\pi/2\), take
\[
t=\frac{b\cos\theta}{(a+b)\sin\theta},\quad
x=\frac{t}{\sqrt{1+t^2}},\quad
\rho=\sqrt{\frac{1-x^2}{m-1}},
\]
\[
u=(x,\rho,\ldots,\rho),\qquad
z=\left(\sqrt{1-x^2},-\frac{x}{\sqrt{m-1}},\ldots,-\frac{x}{\sqrt{m-1}}\right),
\qquad w=\cos\theta\,u+\sin\theta\,z.
\]
Here \(u\) and \(z\) are orthonormal; coordinate one attains equality in both displayed inequalities. The limiting cases \(\theta=0\) and \(\theta=\pi/2\) follow using respectively \(u=w=e_1\) and \(u\perp w=e_1\). Therefore the worst-case ratio for the mixture is **exactly** \(F_{m,\theta}(\eta)\).

**2. Optimizing the mixture.** Set \(k=(m-1)/m\), \(c=\cos\theta\), and \(s=\sin\theta\). The weighted Cauchy inequality gives
\[
F_{m,\theta}(\eta)=\frac{c^2}{1-k\eta}+
\frac{(\sqrt{m-1}\,s)^2}{k\eta}
\ge(c+\sqrt{m-1}\,s)^2.
\]
Equality requires \(\eta=m s/[\sqrt{m-1}c+(m-1)s]\), which lies in \([0,1]\) precisely when \(\tan\theta\le\sqrt{m-1}\). In the open low-angle range strict convexity gives uniqueness among mixtures. Above the cutoff the unconstrained equality point lies beyond one; direct differentiation, or convexity and the location of the unconstrained minimizer, shows that \(F\) decreases up to \(\eta=1\). Since \(F_{m,\theta}(1)=m\), the claimed mixture achieves the stated piecewise bound. At \(\theta=0\), \(p_i=u_i^2\) gives ratio exactly one for \(w=\pm u\).

**3. Universal lower bound against every policy.** Fix the uniform reference \(u=(1,\ldots,1)/\sqrt m\). Any proposed probability vector \(p(u)\) has some coordinate \(j\) with \(p_j\le1/m\). For \(\theta\le\arctan\sqrt{m-1}\), take
\[
z=\frac{e_j-u_j u}{\sqrt{1-1/m}},\qquad
w=\cos\theta\,u+\sin\theta\,z.
\]
Then \(\|w\|_2=1\), \(\langle u,w\rangle=\cos\theta\), and
\[
\frac{w_j^2}{p_j}\ge m w_j^2
=(\cos\theta+\sqrt{m-1}\sin\theta)^2.
\]
For \(\theta\ge\arctan\sqrt{m-1}\), choose instead \(w=e_j\), whose angle from \(u\) is exactly \(\arctan\sqrt{m-1}\). Then \(w_j^2/p_j\ge m\). This lower bound holds for **every** reference-dependent sampling policy and matches step 2, proving the global minimax theorem.

**4. Why positive smoothing is essential and a limited sampling consequence.** For any \(\theta>0\), the pair \(u=e_1\), \(w=\cos\varphi\,e_1+\sin\varphi\,e_2\) with \(0<\varphi\le\theta\) makes the unmodified leverage distribution \(p_i=u_i^2\) assign zero probability to an active current coordinate. Thus its universal inflation is infinite. If \(I_1,\ldots,I_s\) are independent draws from the minimax distribution and \(\widehat g=s^{-1}\sum_{t=1}^s w_{I_t}^2/p^*_{I_t}\), then for \(\theta>0\), \(\mathbb E\widehat g=1\), each summand lies in \([0,\mathcal R_m(\theta)]\), and \(\operatorname{Var}(w_I^2/p_I^*)\le\mathcal R_m(\theta)\). Consequently, the standard bounded-variable Bernstein inequality gives, for every \(\varepsilon>0\),
\[
\Pr\bigl\{|\widehat g-1|\ge\varepsilon\bigr\}
\le2\exp\left[-\frac{s\varepsilon^2}{2\mathcal R_m(\theta)(1+\varepsilon/3)}\right].
\]
This is a consequence of controlling the worst one-draw inflation; optimality of this Bernstein upper-bound input is **not** a theorem about optimality of the actual tail probability or sample complexity.

## Verification

A supplementary, standalone Python standard-library script, `check_minimax.py`, checks the analytic envelope, low-angle witness construction, uniform-reference lower-bound witnesses, random admissible vectors, and boundary values. Run `python check_minimax.py`. The code checks 11,050 numerical/algebraic assertions; it is **not** used as a substitute for proof over real parameters. All displayed formulae follow independently from steps 1--4. In particular, the proof checks both endpoint angles, all integers \(m\ge2\), the zero-probability convention, and the equality threshold.

## Relationship to prior work

Fakih, Grigori and Pierce (2026) introduce sampling based on target tensor leverage scores for alternating least squares and analyze a current-versus-target leverage ratio in their subproblem sampling bound. Their reported current-reference ratio motivates guarding against even small subspace drift where reference scores vanish. Here the object is deliberately simpler and separate: **rank-one**, exact reference scores, an explicit principal-angle uncertainty set, and arbitrary probability policies. The contribution is the exact robust minimax ratio and sharp mix/uniform transition, not a theorem for their higher-rank tensor iteration. Larsen and Kolda (2020) develop leverage sampling and deterministic inclusion for tensor decomposition. Derezinski, Clarkson, Mahoney and Warmuth (2019) develop a different minimax experimental-design criterion for estimator errors and combination sampling rules, not this reference-uncertainty importance-ratio game. Classical weighted Cauchy and Bernstein inequalities are used as established tools, not claimed new. No directly implying result was found in the inspected relevant portions of these sources; unexamined literature may still contain an equivalent characterization.

## Limitations

The angle bound must be known; learning or estimating it is outside scope. The theorem does not cover higher-rank subspaces, nonuniform row costs, approximate reference leverage scores, correlated sampling, or an end-to-end CP-ALS guarantee. Mixture uniqueness is established only *within* that one-parameter family. The bound controls a maximal coordinate weight; it need not minimize actual estimator variance, tails, or a final least-squares residual. The literature comparison is a best-knowledge priority assessment, not proof of global uniqueness.

## References

1. I. Fakih, L. Grigori and K. Pierce, *Accelerating the Canonical Polyadic Alternating Least Squares Optimization via a Randomized Interpolative Decomposition*, arXiv:2607.22194v1, first public 2026-07-24. https://arxiv.org/abs/2607.22194
2. B. W. Larsen and T. G. Kolda, *Practical Leverage-Based Sampling for Low-Rank Tensor Decomposition*, arXiv:2006.16438, 2020. https://arxiv.org/abs/2006.16438
3. M. Derezinski, K. L. Clarkson, M. W. Mahoney and M. K. Warmuth, *Minimax experimental design: Bridging the gap between statistical and worst-case approaches to least squares regression*, Proceedings of Machine Learning Research 99 (2019), pp. 1--20. https://proceedings.mlr.press/v99/derezinski19b.html
4. A. Raj, C. Musco and L. Mackey, *Importance Sampling via Local Sensitivity*, arXiv:1911.01575, 2020. https://arxiv.org/abs/1911.01575
