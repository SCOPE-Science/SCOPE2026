# Exact boundary-flip latency for a gradient-mapping adaptive proximal method

## Finding

**Theorem (exact saturation count and sharp large-gain delay).** Fix a dimension \(d\ge1\), curvature \(\lambda>0\), feasible radius \(R>0\), accumulator initialization \(\gamma>0\), and base gain \(\eta>0\). Apply the deterministic gradient-mapping-accumulation proximal-gradient update of Wang and Yurtsever [1, Algorithm 1] to the strongly convex quadratic \(f(x)=\lambda\|x\|_2^2/2\) and the indicator regularizer of the closed Euclidean ball \(B_R=\{x:\|x\|_2\le R\}\), starting from any \(x_1=Ru\) with \(\|u\|_2=1\). Define

\[
Q=\sqrt{1+\frac{4R^2}{\eta^2}},\qquad r=\frac{\lambda\eta}{2\gamma}.
\]

Then the **exact number of consecutive full boundary-to-antipode steps**, beginning at the first update, is

\[
\boxed{M=\begin{cases}0,&r<1,\\1+\left\lfloor\frac{\log r}{\log Q}\right\rfloor,&r\ge1.\end{cases}}
\]

During these \(M\) steps the objective stays exactly \(\lambda R^2/2\), and

\[
x_{k+1}=(-1)^k Ru,\qquad S_{k+1}=\gamma Q^k\quad(0\le k\le M),
\]

with \(k=0\) giving the initial point \(x_1=Ru\). At update \(M+1\), the orbit enters the open ball, never touches its boundary again, and converges geometrically to the unique optimizer \(0\).

With \(R,\lambda,\gamma\) fixed and \(\eta\to\infty\), the exact waiting time satisfies

\[
\boxed{M=\frac{\eta^2}{2R^2}\log\!\left(\frac{\lambda\eta}{2\gamma}\right)+O_{R,\lambda,\gamma}(\log\eta),\qquad\frac{M}{\eta^2\log\eta}\longrightarrow\frac{1}{2R^2}.}
\]

Thus an arbitrarily long initial period of **zero improvement in the objective** occurs even though the problem is strongly convex and constrained to a compact ball. Any positive target accuracy strictly smaller than \(\lambda R^2/2\) requires more than \(M\) updates, whereas fixed-step projected gradient with step \(1/\lambda\) terminates in one update. This is a sharp parameter-dependent startup lower bound, not an asymptotic divergence claim.

## Assumptions and scope

The deterministic scheme is exactly [1, Algorithm 1], with \(g_k=\nabla f(x_k)\), \(S_1=\gamma\), \(\eta_k=\eta/S_k\), and

\[
x_{k+1}=P_{B_R}(x_k-\eta_k\lambda x_k),\qquad
S_{k+1}^2=S_k^2\left(1+\frac{\|x_{k+1}-x_k\|_2^2}{\eta^2}\right).
\]

All parameters are strictly positive, the dimension is any positive integer, and the initial condition is on the sphere of radius \(R\). Exact mathematical arithmetic and exact Euclidean projection are assumed. The statement does not concern the accelerated variant, noisy gradients, or arbitrary initial states.

## Proof

**1. Radial invariance and saturation criterion.** Every update preserves the line through \(u\): the Euclidean projector of \(tu\) onto \(B_R\) is \(\operatorname{clip}(t,-R,R)u\). When \(x_k=\sigma Ru\), \(\sigma\in\{-1,+1\}\), put \(\theta_k=\lambda\eta/S_k>0\). The unprojected step is \((1-\theta_k)\sigma Ru\). It is projected exactly to the opposite boundary point if and only if \(\theta_k\ge2\), including equality. In that event the displacement has norm \(2R\) and the accumulator is multiplied by \(Q\).

**2. Exact number.** While full flips continue, \(S_k=\gamma Q^{k-1}\), so the \(k\)-th flip occurs if and only if \(Q^{k-1}\le r\). If \(r<1\), none occurs. If \(r\ge1\), the count of nonnegative integers \(k-1\le\log r/\log Q\) is exactly \(M=1+\lfloor\log r/\log Q\rfloor\). The strict inequality \(Q^M>r\) guarantees \(\theta_{M+1}<2\), so the next raw step has magnitude strictly below \(R\). No additional full flip is possible after that point.

**3. No later boundary contact and geometric convergence.** Put \(j=M+1\) and \(\theta_j=\lambda\eta/S_j\in(0,2)\). The first subsequent point is strictly interior, and \(S_k\) is nondecreasing. Hence \(0<\theta_k\le\theta_j<2\) for every \(k\ge j\), and \(x_{k+1}=(1-\theta_k)x_k\), without projection. In this regime

\[
S_{k+1}^2-S_k^2=\lambda^2\|x_k\|_2^2,\qquad
\|x_k\|_2^2-\|x_{k+1}\|_2^2=\theta_k(2-\theta_k)\|x_k\|_2^2.
\]

Let \(\delta=2-\theta_j>0\). The difference-of-squares identity gives

\[
\|x_k\|_2^2-\|x_{k+1}\|_2^2
\ge\frac{\lambda\eta\delta}{S_k}\|x_k\|_2^2
\ge\frac{2\eta\delta}{\lambda}(S_{k+1}-S_k).
\]

Telescoping shows the finite, explicit bound

\[
S_k\le\overline S:=S_j+\frac{\lambda R^2}{2\eta\delta}\qquad(k\ge j).
\]

Consequently \(0<\lambda\eta/\overline S\le\theta_k\le\theta_j<2\). The quantity

\[
q=\max\left\{\left|1-\frac{\lambda\eta}{\overline S}\right|,\,|1-\theta_j|\right\}<1
\]

bounds every tail contraction, and \(\|x_{j+n}\|_2\le q^n R\) for all integers \(n\ge0\). This also covers finite termination.

**4. Large-gain asymptotics.** For fixed \(R\),

\[
\log Q=\frac12\log\left(1+\frac{4R^2}{\eta^2}\right)
=\frac{2R^2}{\eta^2}+O_R(\eta^{-4}),\qquad
\frac{1}{\log Q}=\frac{\eta^2}{2R^2}+1+O_R(\eta^{-2}).
\]

Inserting into the exact floor formula gives the stated expansion, since the floor contributes at most a bounded absolute error. The dimension never enters the radial recursion.

## Verification

The standalone Python script `checker.py` independently applies the two-dimensional Euclidean projection and the source accumulator recurrence. It compares simulated flip counts with the closed formula for positive gains \(0.1,1,2,4,8,16,32,64\) at \(R=\lambda=\gamma=1\), and for three additional positive parameter tuples. It also checks exact rational certificates: \((5/4)^6\le4<(5/4)^7\) implies \(M=7\) at \(\eta=4\), and \((17/16)^{45}\le16<(17/16)^{46}\) implies \(M=46\) at \(\eta=8\). The script ran to completion with all assertions passing. The infinite claims rest on the proof, not finite simulation.

## Relationship to prior work

Wang and Yurtsever [1, Algorithm 1, Sections 3–4 and Appendix E] establish convergence rates and deterministic boundedness properties for gradient-mapping accumulation. The formula above computes the **exact** duration and large-parameter scaling of an initial plateau for that same update; it does not replace their global convergence theorem. Ene, Nguyen and Vladu [2, Appendix A] introduce a closely related movement-scaled scalar AdaGrad+ scheme for constrained optimization; their bounds do not give this exact count or coefficient, and their initialization/diameter conventions differ. Existing published analyses of adaptive-step stabilization address eventual convergence, not the present sharp initial-boundary delay. The potential derivation from standard projection and scalar accumulation identities is acknowledged; the scientific contribution is the exact, parameter-sharp startup complexity and its objective-plateau consequence.

## Limitations

The result applies to a special but natural, strongly convex radial test problem and a boundary initial state, not to general strongly convex functions, arbitrary convex feasible regions, stochastic gradients, or the accelerated algorithm. The sharp delay is a worst-case startup phenomenon as the freely chosen base gain grows, not an assertion that ordinary parameter choices perform poorly. The source scheme and projection identities are prior work. The inspected primary articles and searched records do not establish historical exclusivity; other treatments of related AdaGrad+ scalar recurrences may exist.

## References

[1] Z. Wang and A. Yurtsever, *Universal Adaptive Proximal Gradient Methods via Gradient Mapping Accumulation*, arXiv:2605.05944, first public preprint May 7, 2026. https://arxiv.org/abs/2605.05944

[2] A. Ene, H. L. Nguyen, and A. Vladu, *Adaptive Gradient Methods for Constrained Convex Optimization and Variational Inequalities*, arXiv:2007.08840, first public preprint July 17, 2020. https://arxiv.org/abs/2007.08840
