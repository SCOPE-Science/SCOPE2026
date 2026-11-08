# Entropy-barrier selection and exponential consensus latency in two-layer coordination games

## Finding

Consider a completely overlapping pair of complete social-network layers with two opposed coordination incentives. When individuals independently choose which layer's game to best-respond to, finite populations ultimately agree, but disagreement can persist for an expected number of updates exponential in population size. In a natural integer-threshold family, both the exact finite-population winner probability and the exact mean consensus time admit finite binomial formulas. Their large-population behavior has a sharp activity-selection transition governed by two binary relative-entropy barriers.

Precisely, let \(N\ge4\), \(1\le a<b\le N-2\), and \(0<p<1\). The two payoff matrices, with row/column strategies \(A,B\), are
\[
M_a=\begin{pmatrix}1&-a/(N-1)\\a/(N-1)&0\end{pmatrix},\qquad
M_b=\begin{pmatrix}1&-b/(N-1)\\b/(N-1)&0\end{pmatrix}.
\]
At every discrete update, select the \(M_a\) environment with probability \(p\), otherwise \(M_b\); then select one uniformly random person and let them best-respond to all other people in the selected complete layer, retaining their action on an exact payoff tie. Both layers contain the same \(N\) people, with actions synchronized between layers. Assume initially \(i\in\{a+1,\ldots,b\}\) people play \(A\). Write \(P_i\) for the probability of eventual unanimous \(A\), and \(E_i\) for the expected number of updates until unanimity.

Set, for \(0\le k\le N\) and \(a\le j\le b\),
\[
\pi_k=\binom Nk p^k(1-p)^{N-k},\qquad
r_j=\frac{N}{\pi_j p(N-j)},\qquad
L_k=\sum_{j=a}^{k-1}r_j,\quad L_a=0,\quad R=L_{b+1}.
\]
Then
\[
\boxed{P_i=\frac{L_i}{R}},\qquad
\boxed{E_i=\sum_{k=a+1}^{b}\pi_k\frac{L_{\min(i,k)}(R-L_{\max(i,k)})}{R}+(1-P_i)NH_a+P_iNH_{N-b-1}},
\]
where \(H_t=\sum_{j=1}^{t}1/j\), with \(H_0=0\). In particular, unanimity is almost sure for all finite \(N\). By contrast, if either environment is permanently selected, every initial state reaches unanimity in expected time at most \(NH_N=O(N\log N)\); the exponential latency below is a genuine effect of alternating opposed incentives.

For a sequence of instances with \(a_N/N\to\alpha\in(0,1/2)\), \(b_N/N\to\beta\in(1/2,1)\), fixed \(p\in(\alpha,\beta)\), and \(i_N/N\to p\), define the binary relative entropy and binary entropy (natural logarithms)
\[
D(x\Vert p)=x\log\frac{x}{p}+(1-x)\log\frac{1-x}{1-p},\qquad
H(x)=-x\log x-(1-x)\log(1-x).
\]
The exact logarithmic consensus-time rate and the losing-side rates are
\[
\boxed{\lim_{N\to\infty}\frac{\log E_{i_N}}N=\min\{D(\alpha\Vert p),D(\beta\Vert p)\}},
\]
\[
\lim_{N\to\infty}\frac{\log P_{i_N}}N=-\bigl[D(\beta\Vert p)-D(\alpha\Vert p)\bigr]_+,\qquad
\lim_{N\to\infty}\frac{\log(1-P_{i_N})}N=-\bigl[D(\alpha\Vert p)-D(\beta\Vert p)\bigr]_+.
\]
There is one \(p_*\in(\alpha,\beta)\) at which the two barriers agree:
\[
\boxed{p_*=\frac{1}{1+\exp((H(\beta)-H(\alpha))/(\beta-\alpha))}}.
\]
For fixed \(p<p_*\) in the stated interval, unanimous \(B\) occurs with probability tending to one; for \(p>p_*\), unanimous \(A\) does. No universal limiting winner probability is asserted at \(p=p_*\), where subexponential factors and integer rounding can matter.

## Assumptions and scope

The payoff matrices are coordination games, because their off-diagonal \(S=-t/(N-1)<0\) and \(T=t/(N-1)<1\). The additional asymptotic restrictions put \(M_a\) on the \(A\)-risk-dominant side and \(M_b\) on the \(B\)-risk-dominant side. One update means one independent choice of environment and focal person; the total clock is not rescaled by \(N\). Every tie is resolved by retaining the focal person's previous action. The finite formulas hold for all displayed \(N,a,b,p,i\), without requiring a symmetric pair of thresholds. The asymptotic formulas require a fixed interior activity probability \(p\) and a starting fraction tending to \(p\).

## Proof

A focal person facing \(j\) opponents currently playing \(A\) has payoff difference \(u(A)-u(B)=j-t\) under \(M_t\). Thus, if \(X\) is the number playing \(A\), every update at an interior state \(a+1\le X\le b\) selects a uniformly random person and resets their action to \(A\) in environment \(a\), to \(B\) in environment \(b\). Consequently, \(X\) has transition probabilities
\[
\Pr(X_{s+1}=i+1\mid X_s=i)=p\frac{N-i}{N},\qquad
\Pr(X_{s+1}=i-1\mid X_s=i)=(1-p)\frac{i}{N}.
\]
The remaining probability is a self-loop. At \(X\le a\) no update can increase \(X\) and a selected \(A\)-person switches to \(B\); at \(X\ge b+1\), no update can decrease \(X\) and a selected \(B\)-person switches to \(A\). Therefore the process first exits the interior at \(a\) or \(b+1\), then finishes monotonically, in conditional mean times \(NH_a\) and \(NH_{N-b-1}\), respectively.

The interior birth-death chain is reversible relative to the binomial weights \(\pi_i\), since \(\pi_i p(N-i)/N=\pi_{i+1}(1-p)(i+1)/N\). Introduce edge conductances \(c_j=\pi_j p(N-j)/N\), and their reciprocal resistances \(r_j\), including the fictitious endpoint edges of the corresponding unrestricted heat-bath chain. Solving the harmonic equation with boundary values zero at \(a\) and one at \(b+1\) gives \(P_i=L_i/R\).

For the exit time \(t_i\), the Poisson equation on \(a+1\le i\le b\) is \(1=\pi_i^{-1}[c_{i-1}(t_i-t_{i-1})+c_i(t_i-t_{i+1})]\), with zero boundary values. Its Dirichlet Green kernel is
\[
G(i,k)=\pi_k\frac{L_{\min(i,k)}(R-L_{\max(i,k)})}{R}.
\]
This formula follows by checking that it is zero on both boundaries, linear in resistance coordinate away from \(i=k\), and its conductance flux has unit jump at \(i=k\). Summation over \(k\) yields \(t_i=\sum_kG(i,k)\), and adding the two conditional monotone cleanup times gives the exact expression for \(E_i\). All states have a positive-probability path to a boundary, so absorption is almost sure. Under either fixed environment the count also moves only in one direction, and the expected duration is bounded by the full coupon-collector sum \(NH_N\).

For the limit, Stirling's formula, uniformly on the compact interval between the two limiting cutoffs, yields
\[
\frac1N\log r_{\lfloor Nt\rfloor}=D(t\Vert p)+o(1).
\]
The convexity and unique minimum of \(D(\cdot\Vert p)\) at \(t=p\) imply, when \(i_N/N\to p\),
\[
\frac{\log L_{i_N}}N\to D(\alpha\Vert p),\quad
\frac{\log(R-L_{i_N})}N\to D(\beta\Vert p),\quad
\frac{\log R}N\to\max\{D(\alpha\Vert p),D(\beta\Vert p)\}.
\]
These three limits prove the two fixation-probability exponents. In the Green sum, each summand is at most \(\pi_k L_i(R-L_i)/R\), so \(t_i\le L_i(R-L_i)/R\) because \(\sum\pi_k\le1\). The single term \(k=i\) gives the reverse exponential-order bound \(t_i\ge \pi_i L_i(R-L_i)/R\), and \(N^{-1}\log\pi_{i_N}\to0\). Hence \(N^{-1}\log t_{i_N}\to\min(D(\alpha\Vert p),D(\beta\Vert p))\). The cleanup time is at most \(NH_N=O(N\log N)\), and both barriers are strictly positive, so the same exponent holds for \(E_{i_N}\).

Finally,
\[
D(\beta\Vert p)-D(\alpha\Vert p)=H(\alpha)-H(\beta)+(\beta-\alpha)\log\frac{1-p}{p}.
\]
It is strictly decreasing in \(p\), positive at \(p=\alpha\) and negative at \(p=\beta\). Solving its unique zero gives the displayed \(p_*\) and the selection alternatives.

## Verification

The standalone `verify.py` implements the exact binomial/resistance formulas with rational arithmetic and independently constructs every labeled single-update transition from the pairwise payoff matrices. Running `python verify.py` checked 249 parameter cases over \(3\le N\le8\), with 33,270 labeled nonabsorbing-state Bellman identities for the winner probability and expected time. It also checked, for \((N,a,b,p,i)=(10,2,7,1/2,5)\), the exact results \(P_i=1/2\) and \(E_i=151/3\) updates. These finite tests support, but do not replace, the all-size proof and asymptotic argument.

## Relationship to prior work

Raducha and San Miguel introduced a two-layer coordination-game model with a shared binary action and asynchronous layer-selected best response; they analyzed the dependence on layer overlap and game asymmetry mainly through numerical simulations [1]. The present theorem takes complete layers with full overlap and allows a nonuniform layer-activity probability. It identifies a finite-size heat-bath representation and supplies exact outcome probabilities, expected consensus times, a large-deviation lifetime, and a unique activity-selection threshold not established in the inspected main text of [1]. Their observed long-lived mixing regimes in sparse networks are not asserted here to be identical to the complete-graph regime.

Arditti, Como, Fagnani, and Vanelli developed qualitative robust-consensus results for time-varying-threshold network games [2]. Such qualitative reachability does not determine the two-barrier entropy exponent, selection probabilities, or the activity crossover in this particular randomly switching complete-network model. Classical Ehrenfest/heat-bath chains and hitting-time theory [3] underlie the resistance calculation; the generic reversible-chain identity itself is not claimed as new.

## Limitations

The result is for fully overlapping complete layers, a specific payoff-normalized threshold family, independent layer sampling, asynchronous myopic best response, and deterministic tie retention. It does not establish exponential lifetime on sparse layers, partial overlap, other updating rules, or non-Markovian environment selection. The asymptotic analysis assumes the initial fraction is close to the interior heat-bath mean. The cited model's separate supplementary PDF was identified but could not be materially inspected, leaving a priority risk for unrecognized equivalent analysis; an unindexed exact result is also possible. No independent external validation has been performed.

## References

[1] T. Raducha and M. San Miguel, "Evolutionary games on multilayer networks: coordination and equilibrium selection," arXiv:2212.08877v1 (first public release 2022-12-17), Scientific Reports 13, 11818 (2023). https://arxiv.org/abs/2212.08877 ; full public text https://arxiv.org/html/2212.08877v2

[2] L. Arditti, G. Como, F. Fagnani, M. Vanelli, "Robust Coordination of Linear Threshold Dynamics on Directed Weighted Networks," arXiv:2109.12685 (2021). https://arxiv.org/abs/2109.12685

[3] C. Xin, E. Cui, M. Zhao, Q. Yao, "On the distribution of the hitting time for the N-urn Ehrenfest model," arXiv:1810.04219 (2018). https://arxiv.org/abs/1810.04219

[4] T. Raducha and M. San Miguel, "Coordination and equilibrium selection in games: the role of local effects," arXiv:2110.10036 (2021), Scientific Reports 12, 3373 (2022). https://arxiv.org/abs/2110.10036
