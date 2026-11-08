# Exact finite-tooth comb search-time crossover under stochastic resetting

## Finding
For the symmetric continuous-time nearest-neighbor random walk on the finite-tooth comb defined below, with target at backbone distance \(L\) and Poisson resetting rate \(r\), the *entire* mean first-passage time has the exact form
\[
\mathbb E T_{L,H}(r)=\frac{\exp[L\gamma_H(r)]-1}{r},\quad
\gamma_H(r)=\operatorname{arcosh}\frac{r+3-a_H(r)}{2},
\]
where \(\theta(r)=\operatorname{arcosh}(1+r/2)\) and
\[
a_H(r)=\frac{\cosh[(H-1/2)\theta(r)]}{\cosh[(H+1/2)\theta(r)]}.
\]
The new scaling consequence is a *mesoscopic crossover* for any sequence of positive integer tooth lengths satisfying \(H_L/L^2\to\kappa\in(0,\infty)\): at the reset rate \(r_L=u/L^4\), for every fixed \(u>0\),
\[
\boxed{\lim_{L\to\infty}\frac{\mathbb E T_{L,H_L}(u/L^4)}{L^4}
=G_\kappa(u):=\frac{\exp\!\left[u^{1/4}\sqrt{\tanh(\kappa\sqrt u)}\right]-1}{u}.}
\]
The two iterated limiting profiles are
\[
\lim_{\kappa\to\infty}G_\kappa(u)=\frac{e^{u^{1/4}}-1}{u},\qquad
\lim_{\kappa\downarrow0}\frac{G_\kappa(v/\kappa)}{\kappa}
=\frac{e^{\sqrt v}-1}{v}\quad(u,v>0).
\]
Thus the search-time law crosses between fourth-power anomalous-comb scaling and the normal-diffusive \(L^2H\) scale. For each \(\kappa>0\), the function \(G_\kappa\) attains a strictly positive finite global minimum at some \(u>0\); no uniqueness of the intermediate-\(\kappa\) minimizer is asserted.

## Assumptions and scope
For each integer \(H\ge1\), the graph has vertices \((x,y)\), \(x\in\mathbb Z\), \(0\le y\le H\), undirected vertical edges between consecutive \(y\) at fixed \(x\), and horizontal edges only between \((x,0)\) and \((x+1,0)\). This is an infinite backbone with uniformly capped, one-sided reflecting teeth. From every vertex, the particle jumps along *each* incident edge at rate one (so the total jump rate is its degree). It starts at \((0,0)\) and is removed upon first reaching \((L,0)\), \(L\in\mathbb Z_{\ge1}\). Before removal, an independent Poisson clock of rate \(r>0\) returns it instantaneously to \((0,0)\), from anywhere on the graph. A reset while already at the starting vertex has no effect. The target is the single backbone vertex, not an absorbing vertical line. The first displayed identity holds for every integer \(L,H\ge1\) and every real \(r>0\). The asymptotic identity is pointwise in fixed \(u>0\) and \(\kappa\in(0,\infty)\) and does not claim uniform convergence at moving endpoints.

## Proof
1. Let \(\tau\) be the target hitting time without resets, and \(\phi_{L,H}(s)=\mathbb E_{(0,0)}e^{-s\tau}\), \(s>0\). To solve the backward Laplace problem on a single tooth with boundary value one at \(y=0\), put \(\theta=\operatorname{arcosh}(1+s/2)>0\). For \(1\le y\le H\) the bounded solution is
\[
b_y=\frac{\cosh[(H+1/2-y)\theta]}{\cosh[(H+1/2)\theta]}.
\]
Indeed, the interior backward equation is \((s+2)b_y=b_{y-1}+b_{y+1}\); at the tip it is \((s+1)b_H=b_{H-1}\); and \(b_0=1\). The last two equations follow from \(2\cosh\theta=2+s\) and the reflecting ghost condition \(b_{H+1}=b_H\). In particular the first-tooth ratio is \(b_1=a_H(s)\) above.

2. For backbone coordinates \(x<L\), the Laplace transform of the target hitting time, denoted \(f_x\), satisfies
\[
(s+3-a_H(s))f_x=f_{x-1}+f_{x+1},\qquad f_L=1.
\]
The solution bounded by one and tending to zero as \(x\to-\infty\) is \(f_x=\exp[\gamma_H(s)(x-L)]\), where \(2\cosh\gamma_H=s+3-a_H(s)\). Consequently \(\phi_{L,H}(s)=e^{-L\gamma_H(s)}\). Uniqueness follows from the maximum principle for the backward resolvent on the connected graph at \(s>0\). No finite-box cutoff is used in this argument.

3. Under resetting, each attempt is the original walk up to either the independent rate-\(r\) reset or the hitting event. The success probability of one attempt is \(p=\mathbb P(\tau<R)=\phi_{L,H}(r)\), where \(R\sim\operatorname{Exp}(r)\). The mean duration of one attempt is \(\mathbb E\min(\tau,R)=(1-p)/r\). The renewal equation \(\mathbb E T=(1-p)/r+(1-p)\mathbb E T\) gives \(\mathbb E T=(1-p)/(rp)\), establishing the exact identity.

4. For \(s=u/L^4\), the tooth characteristic exponent obeys \(\theta(s)=\sqrt u/L^2+O(L^{-6})\). The exact identity
\[
1-a_H(s)=\frac{2\sinh(H\theta)\sinh(\theta/2)}{\cosh[(H+1/2)\theta]}
\]
and \(H_L/L^2\to\kappa\) therefore give
\[
L^2[1-a_{H_L}(u/L^4)]\longrightarrow\sqrt u\tanh(\kappa\sqrt u).
\]
Since \(\cosh\gamma=1+[s+1-a_H(s)]/2\), the small-argument expansion of \(\operatorname{arcosh}\) yields
\[
L\gamma_{H_L}(u/L^4)\longrightarrow
u_\kappa(u)=u^{1/4}\sqrt{\tanh(\kappa\sqrt u)}.
\]
Substituting this in the exact reset identity proves the mesoscopic limit.

5. The limits \(\kappa\to\infty\) and \(\kappa\downarrow0\) are obtained from \(\tanh z\to1\) and \(\tanh z\sim z\), respectively. More precisely, with \(u=v/\kappa\), the exponent \(u^{1/4}\sqrt{\tanh(\kappa\sqrt u)}\to\sqrt v\). For fixed \(\kappa>0\), as \(u\downarrow0\), \(G_\kappa(u)\sim\sqrt\kappa/\sqrt u\to\infty\), while as \(u\to\infty\), \(G_\kappa(u)\sim e^{u^{1/4}}/u\to\infty\). Continuity and positivity imply attainment of an interior global minimum. The proof does not assert uniqueness or convergence of finite-system global optimizers.

## Verification
The standalone `verification.py` checks the exact formula against independently assembled finite-state continuous-time Markov backward Poisson equations on truncated combs, with the truncation far to the left of the starting point; it also checks the exact tooth recurrence by an independent continued fraction and verifies numerical convergence in six positive double-scaling regimes plus the two endpoint profiles. Executing `python3 verification.py` produced `PASS 21 independent finite and asymptotic checks`. The finite cutoffs in this computational check approximate the infinite backbone; they are *not* used as an infinite proof, which is supplied above. All computations use only the Python standard library.

## Relationship to prior work
Méndez, Iomin, Campos, and Horsthemke, arXiv:1509.01670 (first posted September 5, 2015), derive mesoscopic transport and effective waiting-time laws on combs, including finite teeth and the distinction between diffusive and anomalous spreading. That work does not state the reset-to-origin first-hitting transform or the joint \(H/L^2\) scaling law above. Singh, Sandev, Iomin, and Metzler, arXiv:2105.08112 (2021), derive reset first-passage formulas on a *continuum* comb with *infinitely long, confining-potential* branches. Their first-passage law is built from a different tooth impedance (confining potential rather than reflecting cap) and does not furnish the hyperbolic-tangent mesoscopic profile by specialization. The 2023 work *Random Walks on Comb-like Structures under Stochastic Resetting* examines mean-square displacement under resetting mechanisms, but accessible text does not establish the present capped-tooth first-hitting crossover. The renewal identity itself is standard and is not claimed as new. The contribution being evaluated is the simultaneous finite-tooth/long-range/reset-rate crossover.

## Limitations
This theorem concerns a single symmetric noninteracting searcher with equal edge jump rates and perfect first-hit absorption at one backbone vertex. It is not a finite-dimensional diffusion model, does not establish any bulk thermodynamic phase transition, and does not assert a universal law for arbitrary comb geometries or reset protocols. The explicit finite-case identity follows a standard resolvent-plus-renewal method; novelty is attributed only to its stated joint-limit profile, pending independent historical-priority review. Search cannot exclude unindexed equivalent results; 2023 full-text inspection was limited by access restrictions. The model uses the order \(L\to\infty\) at fixed \(\kappa>0\) before the separate \(\kappa\)-endpoint limits.

## References
- V. Méndez, A. Iomin, D. Campos, W. Horsthemke, *Mesoscopic description of random walks on combs*, arXiv:1509.01670 (2015), https://arxiv.org/abs/1509.01670 .
- R. K. Singh, T. Sandev, A. Iomin, R. Metzler, *Backbone diffusion and first-passage dynamics in a comb structure with confining branches under stochastic resetting*, arXiv:2105.08112 (2021), https://arxiv.org/abs/2105.08112 .
- *Random Walks on Comb-like Structures under Stochastic Resetting*, Entropy 25, 1529 (2023), https://doi.org/10.3390/e25111529 .
