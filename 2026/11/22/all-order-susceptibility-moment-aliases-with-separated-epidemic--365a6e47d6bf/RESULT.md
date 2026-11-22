# All-order susceptibility moment aliases with separated epidemic final sizes

## Finding

In a closed deterministic SIR epidemic with persistent individual susceptibility and homogeneous infectiousness, **even every nonnegative integer susceptibility moment, together with every one-sided time derivative of the initial epidemic trajectory, need not identify the final attack fraction**. This failure is robust in the initial infectious fraction and can be quantitatively macroscopic.

Let \(Z\sim N(0,9)\), let \(\omega=2\pi/9\), and, for \(-1<a<1\), define the strictly positive probability density on \((0,\infty)\)
\[
f_a(x)=\frac{e^{-(\log x)^2/18}}{3\sqrt{2\pi}\,x}\left[1+a\sin(\omega\log x)\right].
\]
All these distinct laws have **exactly the same moments of every integer order**:
\[
\int_0^\infty x^n f_a(x)\,dx=e^{9n^2/2},\qquad n=0,1,2,\ldots.
\]

For each fixed \(\beta,\gamma>0\) and fixed \(a\in(0,1)\), the epidemics corresponding to \(f_a\) and \(f_{-a}\), with the same initially infectious fraction \(r\in(0,1)\), have different final attack fractions for **every \(r\) except a discrete subset of \((0,1)\)**. Nevertheless all derivatives, of every finite order at time zero, of their cumulative pressure, susceptible fraction, infectious fraction and removed fraction coincide. These trajectories are smooth but not analytic at time zero.

There is also an explicit parameter construction with an order-one discrepancy. Set \(\beta=1\), \(r=1/5\), \(a=9/10\), and
\[
\gamma=2\left[\frac15+\frac45\left(1-L_0(1/2)\right)\right],\qquad
L_0(q)=\int_0^\infty e^{-qx}f_0(x)\,dx.
\]
If \(A_a\) denotes the final fraction of the entire population newly infected after time zero, then
\[
\boxed{A_{9/10}-A_{-9/10}>0.16056.}
\]
Numerical quadrature, **not used to establish the strict inequality**, gives approximately \(A_{9/10}=0.549002\) and \(A_{-9/10}=0.221692\). Both populations have the same initial infected fraction and all susceptibility moments, including the same initial reproduction factor.

## Assumptions and scope

Use population fractions and a fixed conditional susceptibility distribution \(f_a\) among initially susceptible individuals. Each susceptibility \(x>0\) has infection hazard \(\beta xI(t)\). Removal is exponential at rate \(\gamma>0\), infectivity is not susceptibility-dependent, and there are no births, reinfections or behavioral changes. Initially \(I(0)=r\in(0,1)\), \(R(0)=0\), and the susceptible density is \(s(x,0)=(1-r)f_a(x)\). The total population is normalized to one. The statements concern the deterministic fluid equations, rather than a finite-population stochastic outbreak.

Write
\[
\partial_t s(x,t)=-\beta x I(t)s(x,t),\qquad
\dot I(t)=\beta I(t)\int_0^\infty xs(x,t)\,dx-\gamma I(t),\qquad
\dot R(t)=\gamma I(t).
\]
The source's Laplace-transform limit motivates this class; all conclusions here are proved directly for these displayed equations.

## Proof

**1. An exact all-moment alias.** Changing variables \(x=e^z\), and using the Gaussian exponential formula,
\[
\operatorname{Im}\mathbb E[e^{(n+i\omega)Z}]
=e^{(9n^2-9\omega^2)/2}\sin(9n\omega)=0
\]
for every integer \(n\ge0\). This proves the moment formula and normalization. Strict positivity holds for \(|a|<1\). The laws are distinct because their sinusoidal factors differ on intervals of positive Lebesgue measure.

**2. The scalar epidemic pressure and its unique endpoint.** Define \(q(t)=\beta\int_0^t I(u)\,du\), and
\[
L_a(q)=\int_0^\infty e^{-qx}f_a(x)\,dx=L_0(q)+aH(q),\quad
H(q)=\mathbb E[e^{-q e^Z}\sin(\omega Z)].
\]
Exact integration and conservation of population give
\[
S(t)=(1-r)L_a(q(t)),\quad R(t)=\frac\gamma\beta q(t),\quad
\dot q=\beta F_a(q;r),\quad
F_a(q;r)=1-(1-r)L_a(q)-\frac\gamma\beta q.
\]
Here \(F_a(0;r)=r>0\), \(F_a(\beta/\gamma;r)<0\), and \(F_a''(q;r)=-(1-r)L_a''(q)<0\). Consequently \(F_a\) has exactly one root \(Q_a(r)\in(0,\beta/\gamma)\), with \(F_a'(Q_a;r)<0\). Standard positive scalar dynamics show \(q(t)\uparrow Q_a(r)\) and \(I(t)\downarrow0\) eventually. The final new-infection fraction is
\[
A_a(r)=\frac\gamma\beta Q_a(r)-r.
\]

**3. A generic final-size separation.** The signed measure with density \(f_0(x)\sin(\omega\log x)\) is not zero. Uniqueness of Laplace transforms implies \(H\not\equiv0\); \(H\) is real analytic for \(q>0\), hence its positive zeros form a discrete set. If \(Q_a(r)=Q_{-a}(r)=Q\), subtraction of their root equations forces \(H(Q)=0\), and averaging forces \(Q=Q_0(r)\). Implicit differentiation at the root yields
\[
\frac{dQ_0}{dr}=-\frac{L_0(Q_0)}{\partial_qF_0(Q_0;r)}>0.
\]
Thus \(Q_0\) is strictly increasing on \((0,1)\), and the exceptional seeds are a subset of the discrete inverse image of the positive zeros of \(H\). All other seeds give distinct final attacks for the *same* \(\beta,\gamma\).

**4. Every initial time derivative is identical, but the curves are not analytic.** The smooth functions \(L_a\) have
\[
L_a^{(n)}(0)=(-1)^n e^{9n^2/2}\qquad(n\ge0).
\]
Therefore the scalar vector fields \(F_a\) have identical complete one-sided derivative jets at \(q=0\). Repeated differentiation of \(\dot q=\beta F_a(q)\), starting at \(q(0)=0\), shows equality of all derivatives of \(q_a(t)\) at \(t=0\); the formulas for \(S,I,R\) give the corresponding equality for every compartment. Yet the Taylor series of \(L_a\) has radius zero because \(e^{9n^2/2}/n!\) grows faster than every exponential in \(n\). Were \(q_a\) analytic at zero, its nonzero derivative \(\dot q_a(0)=\beta r\) would yield an analytic local inverse; the identity expressing \(L_a(q_a(t))\) through \(q_a\) and \(\dot q_a\) would make \(L_a\) analytic at zero, a contradiction. Nor can the two trajectories agree on any nontrivial initial time interval: their common increasing pressure would force \(H\) to vanish on a positive interval.

**5. A proved quantitative gap.** In the stated parameter construction, the unperturbed root is \(Q_0=1/2\). Let \(\varphi(z)=e^{-z^2/18}/(3\sqrt{2\pi})\), \(\omega=2\pi/9\), and \(d(z)=e^{-e^{-z}/2}-e^{-e^z/2}\). By Gaussian symmetry,
\[
H(1/2)=-\int_0^\infty\varphi(z)\sin(\omega z)d(z)\,dz.
\]
On \([0,9/2]\), the sine is nonnegative; \(\varphi\) decreases and \(d\) increases. Divide this interval into 18 subintervals \([j/4,(j+1)/4]\). Concavity of sine on \([0,\pi]\) gives the exact lower bound
\[
\sum_{j=0}^{17}\frac14\varphi\!\left(\frac{j+1}{4}\right)
\min\!\left\{\sin\!\left(\frac{j\omega}{4}\right),
\sin\!\left(\frac{(j+1)\omega}{4}\right)\right\}
 d\!\left(\frac j4\right)>0.1979.
\]
For the remaining tail, the Gaussian Mills bound gives \(\int_{9/2}^\infty\varphi(z)\,dz<2\varphi(9/2)<0.0864\). Hence \(H(1/2)<-0.1115\). Since \(F_{9/10}(1/2)>0>F_{-9/10}(1/2)\), their roots straddle \(1/2\). Finally, \(F_a'(q)=(1-r)\int xe^{-qx}f_a(x)\,dx-\gamma\ge-\gamma\), so integrating from the baseline pressure to the two roots yields
\[
A_{9/10}-A_{-9/10}=\gamma(Q_{9/10}-Q_{-9/10})
\ge 2\cdot\frac45\cdot\frac9{10}\,[-H(1/2)]
>1.44\cdot0.1115=0.16056.
\]
The finite numerical constants in this proof follow from elementary exponential and trigonometric bounds; the included standalone arithmetic checker evaluates their strictly separated margins. The infinite-dimensional assertions do not rely on numerical quadrature.

## Verification

Execute `python3 checker.py` alongside this file (Python standard library only). It checks the explicit 18-term lower bound and Gaussian-tail upper bound at high decimal precision, prints the resulting certified-margin inequality, and separately illustrates the two final-size roots by numerical quadrature. The fixed-coefficient analytic proof covers all infinite moment orders, all positive transmission/removal rates, the discrete-exception statement and the identical time-derivative jets. A finite program cannot certify those quantifiers by sampling.

## Relationship to prior work

Izyumtseva, KhudaBukhsh, Gomes and Rempala (2026, arXiv:2608.22122v1) establish a stochastic-to-deterministic heterogeneous SIR limit with susceptible fraction described by the Laplace transform of its susceptibility law. Their public abstract supports this modeling starting point; their full manuscript was not accessible for a complete proposition-by-proposition comparison. Miller (2012, Section 3.2, PMCID PMC3506030) proves a general heterogeneous-susceptibility final-size equation in terms of the Laplace transform. The Stieltjes/lognormal moment problem is classical and is **not** claimed as a new probability distribution construction. The contribution assessed here is the combined sharp epidemic consequence: a fixed, explicit family with all moments and complete initial trajectory jets identical, a generic-seed final-size separation, and a rigorously bounded order-one gap.

Muslim (2026, arXiv:2608.04943v1) studies finite-moment equivalences for *group-size* transmission mechanisms whose entire dynamics agree when the relevant finite moments coincide. The present susceptibility-Laplace model has the opposite phenomenon: all moments may agree while actual dynamics differ. Mohammed, Robertson and Gomes (2026, arXiv:2606.08693v1) compare gamma and lognormal susceptibility models matched only on mean and variation, not an entire moment sequence. Neither statement is asserted to be historically unique; inaccessible and unindexed literature remains a priority risk.

## Limitations

The counterexample uses an unbounded lognormal susceptibility support with all finite moments but no finite positive moment-generating function. On compact support, the complete moment sequence uniquely determines the distribution, so this infinite-moment ambiguity cannot occur. The theorem is not about finite sampling, bounded-support populations, numerical error, clinical prognosis, structural nonidentifiability from a full observed trajectory, or finite-population stochastic events. The full text of the 2026 initiating preprint could not be examined; its abstract alone cannot exclude prior discussion of the exact phenomenon. The arithmetic bounds are conservative and do not characterize the largest possible final-size separation.

## References

1. O. Izyumtseva, W. R. KhudaBukhsh, M. G. M. Gomes and G. A. Rempala, *From Individual-Based Stochastic Epidemics to Heterogeneous SIR Equations*, arXiv:2608.22122v1 (first submitted 2026-08-22). https://arxiv.org/abs/2608.22122
2. J. C. Miller, *A Note on the Derivation of Epidemic Final Sizes*, Bulletin of Mathematical Biology **74** (2012), 2125–2141, doi:10.1007/s11538-012-9749-6; complete text: https://pmc.ncbi.nlm.nih.gov/articles/PMC3506030/
3. C. Kleiber, *The generalized lognormal distribution and the Stieltjes moment problem*, arXiv:1301.1277 (2013). https://arxiv.org/abs/1301.1277
4. R. Muslim, *Exact moment equivalence and structural nonidentifiability in nonlinear epidemics*, arXiv:2608.04943 (2026). https://arxiv.org/abs/2608.04943
5. I. Mohammed, C. Robertson and M. G. M. Gomes, *An exploration into how susceptibility distribution misspecifications impact epidemic forecasting*, arXiv:2606.08693 (2026). https://arxiv.org/abs/2606.08693
