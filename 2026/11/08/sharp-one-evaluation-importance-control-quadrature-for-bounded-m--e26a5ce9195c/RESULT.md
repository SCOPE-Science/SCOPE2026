# Sharp one-evaluation importance-control quadrature for bounded monotone functions

## Finding
Let \(\mathcal F\) be all nondecreasing measurable functions \(f:[0,1]\to[0,1]\). Consider one-evaluation, absolutely-continuous importance-control rules
\[
X\sim p(x)\,dx,\qquad Q_{p,h}(f)=\frac{f(X)}{p(X)}+h(X),\qquad \int_0^1p=1,\quad \int_0^1ph=0,
\]
with strictly positive probability density \(p\) almost everywhere and finite second moments for all \(f\in\mathcal F\). Then
\[
\inf_{p,h}\sup_{f\in\mathcal F}\operatorname{Var}(Q_{p,h}(f))
=V_*:=\frac{\coth(1)-1}{4}=0.07825882137483287\ldots.
\]
The minimizer is unique up to Lebesgue-null sets. Write \(c=(4\sinh^2(1))^{-1}\). It is
\[
p_*(x)=\frac1{2\sqrt{(x-1/2)^2+c}},\qquad
h_*(x)=1-x-\sqrt{(x-1/2)^2+c}.
\]
Equivalently, the optimal unbiased rule is
\[
Q_*(f)=1-X+2\sqrt{(X-1/2)^2+c}\left(f(X)-\frac12\right),\qquad X\sim p_*.
\]
Every unit step \(f_\theta(x)=\mathbf{1}_{\{x\ge\theta\}}\), \(0\le\theta\le1\), has variance exactly \(V_*\). In particular the optimal rule improves the published uniform-sampling linear control-variate rule's worst-case variance \(1/12\) by \(6.0894\ldots\%\). This is a minimax statement **within the stated importance-control class**, not among arbitrary single-evaluation nonlinear or singularly sampled algorithms.

## Assumptions and scope
Only one function evaluation is allowed, and \(p,h\) are fixed independently of \(f\). Integrals use Lebesgue measure on \([0,1]\). The density is positive almost everywhere and normalized; the deterministic control \(h\) is centered under \(p\). The expectation is \(\mathbb E Q_{p,h}(f)=\int_0^1f\), so the mean-square error equals the variance. If a competitor has infinite worst-case variance it cannot improve the finite optimum. No continuity of \(f\) is required; monotone versions differing at countably many jump locations have identical laws under the considered densities.

## Proof
**Normalization and equal risk.** Set \(t=x-1/2\), \(q(x)=\sqrt{t^2+c}\), and \(p_*=1/(2q)\). Since \(1/(2\sqrt c)=\sinh(1)\),
\[
\int_0^1p_*(x)\,dx=\operatorname{arsinh}\left(\frac1{2\sqrt c}\right)=1.
\]
By symmetry \(\int xp_*=1/2\). Thus \(\int p_*h_*=\int p_*(1-x)-\int 1/2=0\). For a unit step \(f_\theta\), let \(H=\int p_*h_*^2\). The second moment is
\[
\mathbb E Q_*(f_\theta)^2=H+\int_\theta^1\left(2h_*(x)+\frac1{p_*(x)}\right)dx=H+\int_\theta^1 2(1-x)\,dx=H+(1-\theta)^2.
\]
Because \(\mathbb E Q_*(f_\theta)=1-\theta\), all steps have variance \(H\). A direct symmetric integral yields
\[
H=2\int_0^1p_*(x)(x-1/2)^2dx+c-\frac14
=\frac12\sqrt{\frac14+c}-\frac14=\frac{\coth(1)-1}{4}.
\]
Every \(f\in\mathcal F\) is, up to changes on a countable set, a mixture of unit steps including the constant endpoints \(0\) and \(1\): the mixing distribution is its Stieltjes increment measure plus endpoint masses. Since \(Q_*(f)-\int f\) is linear in \(f\), convexity of the squared \(L^2\) norm (or Jensen's inequality) bounds its variance by the mixture of step variances, hence by \(H\). Consequently its worst-case variance equals \(H\).

**A least-favorable distribution and the minimax lower bound.** Define a probability law \(\pi\) on \([0,1]\) whose interior cumulative distribution is
\[
F(x)=\pi([0,x])=\frac12+(x-\tfrac12)p_*(x)\quad(0<x<1).
\]
Its atoms at \(0\) and \(1\) both have mass \((1-\tanh(1))/2\); its interior density is \(c/[2((x-1/2)^2+c)^{3/2}]\), positive everywhere. In particular \(F(1-F)=c p_*^2\), \(\int_0^1F=1/2\), and
\[
\mathbb E_\pi(1-\theta)^2=\frac12-\frac{\coth(1)}4+c.
\]
For any admissible \((p,h)\), average the error variances over step inputs \(f_\theta\) under \(\pi\). Fubini's theorem and \(\int ph=0\) give
\[
\begin{aligned}
\int\operatorname{Var}(Q_{p,h}(f_\theta))\,\pi(d\theta)
&=\int_0^1\left(ph^2+2Fh+\frac Fp\right)dx-\mathbb E_\pi(1-\theta)^2\\
&=\int_0^1p\left(h+\frac Fp-\frac12\right)^2dx+\frac14
+\int_0^1\frac{F(1-F)}p\,dx-\mathbb E_\pi(1-\theta)^2.
\end{aligned}
\]
Cauchy--Schwarz and \(\int p=1\) imply
\[
\int_0^1\frac{F(1-F)}p\,dx\ge
\left(\int_0^1\sqrt{F(1-F)}\,dx\right)^2
=c\left(\int_0^1p_*\right)^2=c.
\]
Therefore the prior-average risk, and hence the worst-case risk, is at least
\[
\frac14+c-\left(\frac12-\frac{\coth(1)}4+c\right)=V_*.
\]
Equality in Cauchy--Schwarz forces \(p\) proportional to \(\sqrt{F(1-F)}\), thus \(p=p_*\) after normalization; equality in the square forces \(h=1/2-F/p_*=h_*\). Hence the minimizing density and control are unique almost everywhere. This completes the proof.

## Verification
The standalone `check.py` uses midpoint integration over smooth pieces to check normalization, centering, the least-favorable identities, 61 separately integrated step-risk values, six non-step monotone powers, and five alternative sampling densities. Running `python3 check.py` passed 79 checks on a standard Python interpreter and reports \(V_*=0.07825882137483287\ldots\). The program is a finite numerical cross-check; all universal assertions, exact constants and uniqueness follow from the analytic argument above. No external package or data is required.

## Relationship to prior work
Basak, Bect and Vazquez (arXiv:2203.00423, Sections 3--5) show that the **uniform** one-point control-variate rule \(f(U)-U+1/2\) has worst-case variance \(1/12\), and that an optimal one-point design among all unbiased nonsequential algorithms was not then known. Their result does not optimize the importance-sampling density simultaneously with its zero-mean control. The present result strictly improves that benchmark and proves a sharp constant only within the explicitly defined importance-control class. The 2023 overview of integration complexity by Novak concerns broad deterministic and randomized information complexity; the material reviewed does not give this one-point saddle calculation. No claim of global optimality among arbitrary nonlinear algorithms is made.

## Limitations
The theorem is one-dimensional and one-evaluation only. It makes no claim about sequential algorithms, multiple samples, arbitrary nonlinear estimators, singular sampling distributions, worst-case absolute error, or nonmonotone function classes. The exact sharpness is conditional on the rule class stated above. A literature search cannot establish global publication novelty, and independent scientific validation has not been performed.

## References
1. S. Basak, J. Bect and E. Vazquez, *Integration of bounded monotone functions: Revisiting the nonsequential case, with a focus on unbiased Monte Carlo (randomized) methods*, arXiv:2203.00423 (first public 2022-03-01), Sections 2--5, https://arxiv.org/pdf/2203.00423 .
2. E. Novak, *Optimal Algorithms for Numerical Integration: Recent Results and Open Problems*, arXiv:2307.06787 (2023-07-13), https://arxiv.org/pdf/2307.06787 .
