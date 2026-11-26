# Extreme-value laws for adaptively selected two-compartment fusion

## Finding

Consider \(C\geq2\) independently loaded compartments, each containing independent \(\operatorname{Poisson}(\lambda)\) counts of two complementary species, with \(\lambda>0\). Each compartment first undergoes complete local one-to-one reaction, and then exactly one pair of compartments is selected, using observed residual species identities and counts, and fused for complete secondary reaction. Let \(J_{C,\lambda}\) be the maximum possible number of additional pairs produced by selecting that pair.

Write \(\Delta_i=A_i-B_i\) and \(p_k(\lambda)=\Pr\{\Delta_1\geq k\}=e^{-2\lambda}\sum_{j=k}^{\infty}I_j(2\lambda)\), for integers \(k\geq1\), where \(I_j\) is the modified Bessel function. The complete finite-pool tail law is
\[
\Pr\{J_{C,\lambda}\geq k\}=1-2(1-p_k(\lambda))^C+(1-2p_k(\lambda))^C.
\]
For each fixed \(\lambda>0\), as \(C\to\infty\),
\[
\frac{J_{C,\lambda}}{\log C/\log\log C}\longrightarrow1\quad\text{in probability},\qquad
\frac{\mathbb E J_{C,\lambda}}{\log C/\log\log C}\longrightarrow1.
\]
In contrast, under the iterated high-loading limit, first let \(\lambda\to\infty\) at fixed \(C\), obtaining \(Y_C=\min\{\max_i Z_i^+,\max_i(-Z_i)^+\}\), for independent standard normal \(Z_i\). Then, with
\[
a_C=\sqrt{2\log C},\qquad
u_C=\sqrt{2\log C}-\frac{\log\log C+\log(4\pi)}{2\sqrt{2\log C}},
\]
one has the nondegenerate extreme law
\[
\lim_{C\to\infty}\Pr\{a_C(Y_C-u_C)\leq x\}
=2e^{-e^{-x}}-e^{-2e^{-x}},\qquad x\in\mathbb R.
\]
The limit is the minimum of two independent standard Gumbel variables. The fixed-loading and sequential high-loading results describe different, explicitly ordered regimes, not a uniform joint limit.

## Assumptions and scope

The counts \((A_i,B_i)\), for \(1\leq i\leq C\), are jointly independent Poisson random variables of common mean \(\lambda\). Each individual compartment first consumes \(\min(A_i,B_i)\) pairs locally. Residual species are neither lost nor exchanged before the second stage. At the second stage, counts and signs of the remaining imbalances can be measured without altering them, any two distinct compartments can be selected, and the selected pair reacts to completion. The quantity optimized is **the increment at that single pair-fusion stage**, not the total yield after many fusions or the product per initial molecule. The protocol assumes ideal kinetics to completion, as a count-capacity model, and ignores measurement and selection costs.

## Proof

**1. Pathwise optimization.** A locally reacted compartment with \(\Delta_i>0\) retains \(\Delta_i\) copies of species A and no B; for \(\Delta_i<0\), it retains \(-\Delta_i\) copies of B and no A. Fusing compartments \(i\neq j\) produces
\[
J_{ij}=\min\{(\Delta_i)^+,(-\Delta_j)^+\}+\min\{(-\Delta_i)^+,(\Delta_j)^+\}.
\]
Only opposite-sign imbalances produce a positive increment. Consequently, for every realized vector of imbalances,
\[
J_{C,\lambda}=\max_{i<j}J_{ij}=\min\{M_+,M_-\},\quad
M_+=\max_i(\Delta_i)^+,\quad M_-=\max_i(-\Delta_i)^+.
\]
Both maxima use distinct compartments when positive, because a single imbalance cannot have both signs.

**2. Exact finite-pool distribution.** The differences are independent symmetric Skellam variables. For any integer \(k\geq1\), a given compartment has positive imbalance at least \(k\) with probability \(p_k\), negative imbalance at most \(-k\) with probability \(p_k\), and neither with probability \(1-2p_k\). By inclusion–exclusion, existence of at least one compartment of each extreme sign has probability \(1-2(1-p_k)^C+(1-2p_k)^C\). By step 1 this event is exactly \(\{J_{C,\lambda}\geq k\}\). The Skellam series follows directly by conditioning on two independent Poisson counts and summing their difference probabilities.

**3. Fixed-loading extrema.** For fixed \(\lambda>0\) and every integer \(k\geq1\), bounding the right-tail event by the A count and below by the single configuration \(A=k,B=0\) gives
\[
e^{-2\lambda}\frac{\lambda^k}{k!}\leq p_k(\lambda)
\leq\Pr\{\operatorname{Poisson}(\lambda)\geq k\}.
\]
For \(k>\lambda\), the Chernoff upper bound is \((e\lambda/k)^k\). Stirling's formula therefore implies \(\log p_k=-k\log k+O_\lambda(k)\). Put \(b_C=\log C/\log\log C\). For any fixed \(0<\varepsilon<1\), taking integer thresholds asymptotic to \((1-\varepsilon)b_C\) and \((1+\varepsilon)b_C\) shows respectively \(Cp_k\to\infty\) and \(Cp_k\to0\). In the first case the probability of failing to find either sign is at most \(2(1-p_k)^C\to0\); in the second case the probability of finding the positive sign is at most \(Cp_k\to0\). Hence \(J_{C,\lambda}/b_C\to1\) in probability.

For expectations, the lower bound follows from the same lower threshold. For the upper bound, \(J_{C,\lambda}\leq\max_i A_i\). If \(K_C\) is an integer asymptotic to \((1+\varepsilon)b_C\), then
\[
\sum_{k\geq K_C}\Pr\{J_{C,\lambda}\geq k\}
\leq C\sum_{k\geq K_C}\Pr\{A_1\geq k\}
\leq\frac{C\Pr\{A_1\geq K_C\}}{1-\lambda/(K_C+1)}\longrightarrow0.
\]
The last inequality follows term by term from the Poisson ratio \(\Pr(A=j+1)/\Pr(A=j)=\lambda/(j+1)\), while the limit follows from the same Stirling bound. The tail-sum formula for nonnegative integer expectations then yields \(\limsup \mathbb E J_{C,\lambda}/b_C\leq1+\varepsilon\). Letting \(\varepsilon\downarrow0\) and combining with the lower bound proves the stated mean asymptotic.

**4. Sequential high-loading Gaussian limit.** The moment-generating function of a rescaled imbalance is
\[
\mathbb E\exp\left(t\frac{\Delta_i}{\sqrt{2\lambda}}\right)
=\exp\left(2\lambda\left[\cosh\left(\frac{t}{\sqrt{2\lambda}}\right)-1\right]\right)
\longrightarrow e^{t^2/2}.
\]
For fixed \(C\), independence and the continuous mapping theorem give \(J_{C,\lambda}/\sqrt{2\lambda}\Rightarrow Y_C\). If \(\Phi\) is the standard normal distribution function, the same sign-count argument gives, for every \(y>0\),
\[
\Pr\{Y_C>y\}=1-2\Phi(y)^C+[2\Phi(y)-1]^C.
\]
The standard normal tail equivalent \(\overline\Phi(u_C+x/a_C)\sim e^{-x}/C\), obtained by Mills' ratio with the displayed constants, implies
\[
\Pr\{a_C(Y_C-u_C)>x\}\longrightarrow
1-2\exp(-e^{-x})+\exp(-2e^{-x})
=(1-\exp(-e^{-x}))^2.
\]
Subtracting this survival probability from one proves the displayed CDF and its independent-Gumbel interpretation. This is an iterated limit: no triangular-array statement with \(\lambda\) varying simultaneously with \(C\) is asserted.

## Verification

The standalone `VERIFY.py` in this package uses exact rational arithmetic to enumerate independent finite symmetric imbalance laws and verify the pathwise optimizer and inclusion–exclusion identity. It also uses two independently evaluated Poisson/Skellam series and multinomial sign-count sums for numerical consistency checks. Invocation: `python3 VERIFY.py`. In the completed checks the script reported 131 passed deterministic comparisons. These finite tests supplement the proof; neither an infinite-size asymptotic nor the absence of prior coverage is inferred from them.

## Relationship to prior work

Rubinovich and Polak, *Intrinsic Matching Frustration in Fluctuating Finite Systems* (arXiv:2607.03549, first posted July 3, 2026) established the general pathwise fusion-capacity identity for a fixed grouping, the symmetric Skellam loading law, and mean hidden-capacity formulas. **None of those ingredients is claimed as new.** The present theorem asks a different, adaptive one-pair resource-allocation question: after observing all local residual populations, which two compartments maximize the single next reaction burst, what is its exact law for finite candidate pools, and how does selection change its order of growth in two loading regimes?

Sorting and selective droplet pairing are experimentally motivated by deterministic co-encapsulation approaches (for example, DOI:10.1039/C7LC00745K); the current theorem is an idealized mathematical capacity model, not a validated experimental protocol. Normal extreme-value norming and its Gumbel limit are classical and are used rather than newly asserted. The originality claim is confined to the coupling of adaptive complementary fusion selection to the exact two-sign tail law and its contrasting fixed-load and sequential high-load asymptotics.

## Limitations

The strategy assumes ideal non-destructive composition readout and unrestricted choice of exactly one pair; it does not optimize costs, finite reaction rates, imperfect measurements, simultaneous multiple pairings, arbitrary dependent loading or an adaptive multistage fusion tree. With \(\lambda\) fixed and \(C\) increasing, the total available inventory also grows: the gain is relative to a randomly predetermined pair in the same pool, not a free increase at fixed total inventory. The fixed-load scaling has slow logarithmic convergence. The Gumbel law uses an explicitly **sequential** limit and does not claim a sharp crossover for simultaneous large \(\lambda\) and \(C\). Classical extreme-value theory supplies the limiting normal maxima, and uninspected portions of related papers remain an originality risk.

## References

1. L. Rubinovich and M. Polak, *Intrinsic Matching Frustration in Fluctuating Finite Systems*, arXiv:2607.03549v1 (2026-07-03), revised v2 (2026-09-18). https://arxiv.org/abs/2607.03549 ; https://arxiv.org/html/2607.03549 .
2. *Deterministic droplet-based co-encapsulation and pairing of microparticles via active sorting and downstream merging*, *Lab on a Chip* (2017), DOI:10.1039/C7LC00745K. https://doi.org/10.1039/C7LC00745K .
3. A. Gasull, M. Jolis and F. Utzet, *On the norming constants for normal maxima*, arXiv:1308.5541 (2013), https://arxiv.org/abs/1308.5541 .
