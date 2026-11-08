# A sharp two-parameter rate barrier for skew golden-ratio iterations

## Finding
For every even integer \(d\ge2\), let \(J\in\mathbb R^{d\times d}\) satisfy \(J^{\mathsf T}=-J\) and \(J^2=-I\). Consider the fixed-step unconstrained extended golden-ratio iteration on \(F(x)=LJx\), where \(L>0\), \(c>1\), and \(\lambda>0\):
\[
\bar x^{k}=\frac{c-1}{c}x^k+\frac1c\bar x^{k-1},\qquad
x^{k+1}=\bar x^k-\lambda LJx^k,\qquad \bar x^{-1}=x^0.
\]
Set \(t=\lambda L\). Its full real state-transition spectral radius \(\rho(c,t)\) satisfies the **sharp universal inequality**
\[
\boxed{\rho(c,t)\ge 1/\sqrt2}\quad\text{for every }c>1,\ t>0,
\]
with equality **if and only if** \(c=2\) and \(t=1\). Thus the unique globally rate-optimal pairing of convex-combination parameter and step is \((c,\lambda L)=(2,1)\), including when the enlarged theoretically admissible range \(1<c<3\) is imposed.

At this unique optimum, the state recurrence has a double nonsemisimple complex root and, for every \(x^0\in\mathbb R^d\) and every integer \(k\ge0\),
\[
\boxed{x^k=(k+1)2^{-k/2}\left[\cos(k\pi/4)I-\sin(k\pi/4)J\right]x^0,\qquad
\|x^k\|=(k+1)2^{-k/2}\|x^0\|.}
\]
In particular the *greatest transient Euclidean amplification* over all integer iterations is exactly \(3/2\), attained at \(k=2\); the iterates first become strictly smaller than their initial norm at \(k=6\). The best asymptotic spectral rate therefore does not imply one-step descent.

## Assumptions and scope
The arithmetic is exact. \(d\) is any positive even dimension at least two, \(J\) is a real orthogonal complex structure, \(L>0\), \(c>1\), and \(\lambda>0\). The operator \(F=LJ\) is monotone (with zero symmetric part) and \(L\)-Lipschitz; its unique zero is the origin. The objective minimized is the spectral radius of the full linear state transition, **not** a worst-case finite-horizon operator norm nor a general monotone-operator rate. The initialization \(\bar x^{-1}=x^0\) is needed for the explicit transient formula, not for the spectral-radius bound.

## Proof
Write \(t=\lambda L\). The recurrence implies \(\bar x^0=x^0\), \(x^1=(I-tJ)x^0\) and, eliminating the auxiliary state for every \(k\ge1\),
\[
 x^{k+1}=(I-tJ)x^k+(t/c)Jx^{k-1}.
\]
Since \(J^2=-I\) and \(J^{\mathsf T}=-J\), its complex eigenvalues are \(+\mathrm i\) and \(-\mathrm i\). On any \(+\mathrm i\) eigenspace, the characteristic polynomial is
\[
P(z)=z^2+az+b,\quad a=-1+\mathrm it,\quad b=-\mathrm it/c.
\]
The conjugate polynomial handles the other eigenspaces. Their maximum root modulus is precisely \(\rho(c,t)\).

We use the elementary *necessary* condition for the roots of \(w^2+Aw+B\) to lie in the closed unit disk:
\[
|B|\le1,\qquad |A-\overline A B|\le1-|B|^2.\tag{1}
\]
Indeed, if the roots are \(w_1,w_2\) with \(r_j=|w_j|\le1\), then
\[
 A-\overline A B=-w_1(1-r_2^2)-w_2(1-r_1^2),
\]
and \(r_1(1-r_2^2)+r_2(1-r_1^2)\le1-r_1^2r_2^2\), since the difference factors as \((1-r_1)(1-r_2)(1-r_1r_2)\ge0\).

Suppose both roots of \(P\) have modulus at most \(R=1/\sqrt2\). Apply (1) to \(P(Rw)/R^2\), and introduce the positive quantities
\[
q=\frac1{cR^2}=\frac2c,\qquad u=(qt)^2\le1.
\]
Direct substitution gives the *necessary* inequality \(D\le0\), where
\[
\begin{aligned}
D&=(1-u/q)^2+\frac{u}{q^2}(1-q)^2-\frac12(1-u)^2\\
 &=u(1+u)\left(\frac1q-\frac2{1+u}\right)^2
 +\frac{(1-u)^3}{2(1+u)}.\tag{2}
\end{aligned}
\]
Every term on the right is nonnegative for \(q>0\) and \(0<u\le1\). Equality requires \(u=1\) and \(q=1\), which force \(c=2\), \(t=1\). Therefore no parameter pair produces a spectral radius less than \(R\), and a pair attaining \(R\) must be this unique pair. For \((c,t)=(2,1)\),
\[
P(z)=\left(z-\frac{1-\mathrm i}{2}\right)^2,
\]
so both eigenvalue moduli equal \(R\) and the bound is attained.

For this pair let \(r=(1-\mathrm i)/2=2^{-1/2}e^{-\mathrm i\pi/4}\). The scalar recurrence has the double-root form \(z_k=(A+Bk)r^k\); the compatible initial conditions \(z_0=z_{\mathrm{init}}\), \(z_1=(1-\mathrm i)z_{\mathrm{init}}=2rz_{\mathrm{init}}\) give \(A=B=z_{\mathrm{init}}\). Combining conjugate eigenspaces yields the claimed real formula. Because \(\cos(\theta)I-\sin(\theta)J\) is orthogonal, it yields the exact norm equality. Finally the ratio of successive amplification factors is \((k+2)/[(k+1)\sqrt2]\), greater than one only for \(k=0,1\), establishing the maximum \(3/2\) at \(k=2\). Direct comparison at \(k=5,6\) gives \(6/\sqrt{32}>1\) and \(7/8<1\), after which the sequence decreases.

## Verification
The standalone file `verify.py` checks identity (2) symbolically, the repeated-root polynomial and recurrence in exact symbolic arithmetic, 1,309 nonnegative exact-rational certificates on a parameter grid, 9,120 independent numerical spectral cases, and 20 iterations on a six-dimensional orthogonal complex structure. These are supplementary diagnostics; the proof for all real parameters is the elementary root condition (1) together with the exact sum-of-nonnegative-terms identity (2). Execute `python verify.py` with Python 3, SymPy and NumPy.

## Relationship to prior work
Soe–Tam–Vetrivel (2026), Section 2.1, studies precisely this skew rotation and proves instability for \(c\ge3\) using a Schur–Cohn calculation; Theorem 2.3 provides a general sufficient fixed-step range for \(1<c<3\). The present conclusion is **not** the known \(c\ge3\) instability threshold, nor a restatement of that sufficient guarantee: it solves the two-parameter minimum-spectral-radius problem over *all* \(c>1\) and *all* positive steps and identifies the exact transients at the optimizer. For the optimal \(c=2\), the dimensionless step \(t=1\) exceeds that paper's general sufficient bound \(\mu(2)=2/3\), without contradicting it.

Earlier analyses of standard reflected-gradient/FRB skew rotations establish the sharp stability ceiling and the best step **for the fixed conventional reflection weight**. In particular, the known fixed-reflection optimal factor \(1/\sqrt2\) is acknowledged as prior work; the new point is that even permitting every GRAAL mixing parameter cannot improve it, together with the exact all-dimensional transient overshoot. The earlier variable-reflection stability-ceiling problem on split-skew examples optimizes a different quantity. All comparisons concern the mathematical statements and their logical scope, not keyword differences.

## Limitations
This theorem is restricted to skew-isometric linear operators and constant steps with no proximal term. It does not show that \((2,1/L)\) converges for arbitrary monotone \(L\)-Lipschitz operators; in fact the source paper's uniform sufficient bound is smaller. The spectral radius is an asymptotic criterion and is not a finite-time minimax guarantee. The square identity gives mathematical correctness, not historical uniqueness: the complete older reflected-gradient literature may contain equivalent parameter-optimization formulations, so independent literature review remains valuable. No finite-precision or perturbation robustness is established.

## References
- Santanu Soe, Matthew K. Tam, V. Vetrivel, *GRAAL for variational inequalities revisited: sharp parameter range and adaptive step sizes*, arXiv:2610.34975v1, 2026-10-26. https://arxiv.org/html/2610.34975v1
- Yekini Shehu, *The sharp step-size constant for one-call reflection splittings on monotone inclusions*, arXiv:2609.18373v1, 2026-09-16. https://arxiv.org/abs/2609.18373
- Yura Malitsky, *Golden ratio algorithms for variational inequalities*, Mathematical Programming 184 (2020), 383–410; arXiv:1803.08832. https://arxiv.org/abs/1803.08832
- *Exact rate-optimal steps for FRB/RFB on the skew-rotation family* (public mathematical record, 2026-09-19). https://github.com/published-finding corpus/2026/tree/main/2026/9/19/SCOPE-rate-optimal-frb-skew-rotations--689d5e743c56
