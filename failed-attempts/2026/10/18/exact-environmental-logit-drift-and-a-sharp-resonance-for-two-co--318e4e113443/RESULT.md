# Exact environmental-logit drift and a sharp resonance for two-community feedback games

## Finding
Consider the full five-dimensional two-community eco-evolutionary replicator system of Betz, Fu, and Masuda [1]. With three positive environmental feedback strengths, write
\[
a=\frac{1+\theta_{12}}{2(1+\theta_1)},\qquad b=\frac{1+\theta_{12}}{2(1+\theta_2)},\qquad \sigma=a+b-1.
\]
On every trajectory starting in the open unit five-cube, the environmental log-odds combination
\[
H=\log\frac{n_{12}}{1-n_{12}}-a\log\frac{n_1}{1-n_1}-b\log\frac{n_2}{1-n_2}
\]
satisfies the exact law \(H(t)=H(0)+\sigma t\) for every \(t\ge0\), independently of the two payoff matrices and the cross-community mixing parameter.

If \(\sigma>0\), let \(F_+\) denote the union of the three environmental faces \(n_{12}=1\), \(n_1=0\), and \(n_2=0\). Every interior solution obeys
\[
\operatorname{dist}_{\infty}(Z(t),F_+)=\min\{1-n_{12}(t),n_1(t),n_2(t)\}
\le \exp\!\left(\frac{-H(0)-\sigma t}{1+a+b}\right).
\]
If \(\sigma<0\), let \(F_-\) denote the union of \(n_{12}=0\), \(n_1=1\), and \(n_2=1\). Every interior solution obeys
\[
\operatorname{dist}_{\infty}(Z(t),F_-)=\min\{n_{12}(t),1-n_1(t),1-n_2(t)\}
\le \exp\!\left(\frac{H(0)+\sigma t}{1+a+b}\right).
\]
Thus every such solution approaches the respective union of faces at a guaranteed exponential rate, and its omega-limit set is contained there. In particular, off resonance there are no equilibria, nonconstant periodic trajectories, or invariant probability measures entirely supported inside the open five-cube.

The transition is sharp: \(\sigma=0\) precisely when \(1+\theta_{12}\) equals the harmonic mean of \(1+\theta_1\) and \(1+\theta_2\), equivalently
\[
\theta_{12}=\frac{\theta_1+\theta_2+2\theta_1\theta_2}{2+\theta_1+\theta_2}.
\]
At this equality, \(H\) is a first integral and the payoff matrices \(A_0=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)\), \(A_1=\bigl(\begin{smallmatrix}0&0\\1&1\end{smallmatrix}\bigr)\) meet all strict payoff assumptions of [1] and produce an interior equilibrium for every choice of positive \(\theta_1,\theta_2\) and \(0<\delta<1\). Hence the off-resonance impossibility condition cannot be extended to the resonant surface.

## Assumptions and scope
Write \(Z=(x,y,n_1,n_2,n_{12})\in(0,1)^5\). Let \(\theta_1,\theta_2,\theta_{12}>0\) and \(0<\delta<1\). Source [1] uses \(A(n)=(1-n)A_0+nA_1\), where the entries of \(A_0\) and \(A_1\) are respectively \((R_0,S_0;T_0,P_0)\) and \((R_1,S_1;T_1,P_1)\), with strict inequalities \(R_0>T_0\), \(S_0>P_0\), \(R_1<T_1\), and \(S_1<P_1\). Define the cooperator-minus-defector payoff difference against an opponent with cooperation frequency \(q\) by
\[
G(n,q)=[(1-n)(R_0-T_0)+n(R_1-T_1)]q+[(1-n)(S_0-P_0)+n(S_1-P_1)](1-q).
\]
The full source system, without imposing equality between communities, is
\[
\begin{aligned}
\dot x&=x(1-x)[(1-\delta)G(n_1,x)+\delta G(n_{12},y)],\\
\dot y&=y(1-y)[(1-\delta)G(n_2,y)+\delta G(n_{12},x)],\\
\dot n_1&=n_1(1-n_1)[(1+\theta_1)x-1],\\
\dot n_2&=n_2(1-n_2)[(1+\theta_2)y-1],\\
\dot n_{12}&=n_{12}(1-n_{12})[(1+\theta_{12})(x+y)/2-1].
\end{aligned}
\]
All coordinates remain in \((0,1)\) at finite time, by the multiplicative logistic factors and bounded polynomial right-hand side, and the dynamics exist globally on the closed cube. The distance \(\operatorname{dist}_{\infty}\) is the usual sup-norm distance to the indicated union of faces within the closed cube. An invariant probability measure entirely supported in the open cube need not have compact support; the exclusion applies to all such measures.

## Proof
For \(0<u<1\), define \(\ell(u)=\log(u/(1-u))\). Since \(\frac{d}{dt}\ell(u)=\dot u/[u(1-u)]\), the three environmental equations give
\[
\begin{aligned}
\dot H&=(1+\theta_{12})\frac{x+y}{2}-1
-a[(1+\theta_1)x-1]-b[(1+\theta_2)y-1]\\
&=a+b-1=\sigma,
\end{aligned}
\]
because \(a(1+\theta_1)=b(1+\theta_2)=(1+\theta_{12})/2\). Integration proves the exact identity for every finite \(t\).

When \(\sigma>0\), exponentiation gives
\[
e^{-H(t)}=\frac{(1-n_{12})n_1^a n_2^b}{n_{12}(1-n_1)^a(1-n_2)^b}.
\]
The denominator is at most one, so
\[
(1-n_{12})n_1^a n_2^b\le e^{-H(0)-\sigma t}.
\]
Each of the three factors lies between zero and one. If \(d\) is their minimum, then \(d^{1+a+b}\le(1-n_{12})n_1^a n_2^b\), proving the asserted rate. If \(\sigma<0\), instead exponentiate \(H\):
\[
e^{H(t)}=\frac{n_{12}(1-n_1)^a(1-n_2)^b}{(1-n_{12})n_1^a n_2^b},
\]
so \(n_{12}(1-n_1)^a(1-n_2)^b\le e^{H(0)+\sigma t}\), giving the second bound. The entire phase space is compact, hence every forward limit point lies in the respective closed face union.

For completeness, suppose a probability measure \(\mu\) on the open cube is invariant under the flow. Push it forward by the continuous measurable map \(H:(0,1)^5\to\mathbb R\). The resulting finite probability measure \(\nu\) on \(\mathbb R\) must be invariant under translation by \(\sigma t\) for each \(t\ge0\), because \(H\circ\Phi_t=H+\sigma t\). If \(\sigma\ne0\), translate an interval of length smaller than \(|\sigma|\) repeatedly by integer multiples of \(\sigma\); the disjoint intervals must all have equal measure, so each has zero measure. As the chosen half-open interval can be any member of a countable partition of \(\mathbb R\) into intervals shorter than \(\lvert\sigma\rvert\), every member of that partition has zero mass, a contradiction. An interior equilibrium or periodic orbit would itself yield such a measure. An interior compact invariant set would also yield one by time averaging.

The algebraic equivalence \(\sigma=0\iff1/(1+\theta_{12})=\tfrac12(1/(1+\theta_1)+1/(1+\theta_2))\) establishes the harmonic-mean condition. For the constructive converse choose the payoff matrices above, for which \(G(n,q)=1-2n\) for all \(q\). Fix any positive \(\theta_1,\theta_2\), choose their resonant \(\theta_{12}\), and set
\[
x_*=\frac1{1+\theta_1},\quad y_*=\frac1{1+\theta_2},\quad n_{1*}=n_{2*}=n_{12*}=\frac12.
\]
The two within-community environment derivatives vanish by the definitions of \(x_*\), \(y_*\). The between-community derivative vanishes by resonance, because \((1+\theta_{12})(x_*+y_*)/2=1\). Both strategy derivatives vanish because all payoff differences \(G(1/2,q)\) vanish. This interior equilibrium satisfies the strict source conditions on payoffs. Indeed, allowing \(n_{12*}=s\) and \(n_{1*}=n_{2*}=(1/2-\delta s)/(1-\delta)\) for \(s\) in a sufficiently small open interval about \(1/2\) yields an interior one-parameter equilibrium family: every strategy payoff difference is \((1-\delta)(1-2n_{1*})+\delta(1-2s)=0\).

## Verification
The attached `verification.py` uses symbolic algebra to derive \(\dot H=\sigma\) and the harmonic resonance identity; checks 1,800 independent exact-rational states using all five differential equations; checks four exact-rational interior resonant equilibrium instances; and integrates two off-resonance trajectories and one resonant trajectory, comparing 303 time samples against the identity and face inequalities. These finite computations check transcription and numerical behavior; the proof above is the general argument.

For the source's Figure 8(c), \((\theta_1,\theta_2,\theta_{12})=(3,5,8)\) gives \(\sigma=7/8\); for its Figure 8(e,f), \((3/10,2/5,9/20)\) gives \(\sigma=55/728\). In both cases the theorem rigorously excludes an *entirely interior* periodic orbit, even when numerical time series look oscillatory.

## Relationship to prior work
Betz, Fu, and Masuda [1, Sec. 5 and App. G] enumerate equilibrium classes and their local stability in the five-dimensional system and display oscillatory trajectories. The algebraic parameter combination setting the sign of \(\sigma\) also appears in their Appendix G Table 2 local-stability conditions, so that sign expression itself is not claimed as new. The result here is a global exact identity and a uniform, quantitative boundary-selection theorem for **all** interior trajectories, plus nonexistence of entirely interior invariant probability measures, which do not follow solely from local stability tables. The authors' remark about no limit cycles of a related well-mixed model concerns a different, lower-dimensional system. Earlier environmental-feedback examples of Weitz et al. [2] and Tilman et al. [3] use different environmental state structures and do not supply these three-edge global estimates.

## Limitations
The theorem does **not** force convergence to a single boundary equilibrium and does not rule out oscillations, heteroclinic behavior, chaos, or invariant probability measures on boundary faces. At resonance, the first integral alone does not establish that all parameter choices have interior equilibria or periodic orbits; the construction proves existence for a concrete admissible payoff family. Exponential closeness to a *union* of faces does not assert a particular single face is eventually selected. The no-invariant-measure conclusion is only for measures assigning full mass to the open five-cube. Originality was checked against the cited primary literature and related indexed records, not every conceivable unindexed treatment.

## References
[1] K. Betz, F. Fu, N. Masuda, “Evolutionary game dynamics with environmental feedback in a network with two communities,” *Bulletin of Mathematical Biology* 86, 84 (2024); arXiv:2404.17082, first public version 2024-04-25. https://arxiv.org/html/2404.17082v2 ; https://arxiv.org/abs/2404.17082 .
[2] J. S. Weitz, C. Eksin, K. Paarporn, S. P. Brown, W. C. Ratcliff, “An oscillating tragedy of the commons in replicator dynamics with game-environment feedback,” *PNAS* 113, E7518–E7525 (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC5127343/ .
[3] A. R. Tilman, J. B. Plotkin, E. Akçay, “Evolutionary games with environmental feedbacks,” *Nature Communications* 11, 915 (2020). https://www.nature.com/articles/s41467-020-14531-6 .
