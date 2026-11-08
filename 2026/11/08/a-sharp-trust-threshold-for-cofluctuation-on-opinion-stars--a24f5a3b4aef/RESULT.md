# A sharp trust threshold for cofluctuation on opinion stars

## Finding

Consider a star with one flexible central agent, \(k\ge 2\) flexible leaves, \(a\ge1\) stubborn leaves fixed at opinion \(z_0\), and \(b\ge1\) stubborn leaves fixed at a distinct opinion \(z_1\). Put \(h=a+b\). Each flexible agent activates at rate one, chooses one of its neighbours uniformly, and replaces its current opinion \(x\) by \((1-\theta)x+\theta y\), where \(y\) is the chosen neighbour's opinion and \(0<\theta\le1\). All activation processes and choices are independent. The stubborn agents never change their opinions.

The stationary opinions of all flexible agents have common mean \(m=(az_0+bz_1)/h\). Let
\[
q=\frac{ab}{h^2}(z_1-z_0)^2,\qquad
D=k(\theta^2-8\theta+8)+h(2\theta^2-8\theta+8)+2\theta-\theta^2.
\]
Then the centre variance, each flexible-leaf variance, and **every covariance between two distinct flexible agents** respectively equal
\[
V_C=\frac{q\theta[(k+2h)(2-\theta)+\theta]}{D},\quad
V_L=\frac{q\theta[k(2-\theta)+2h+\theta]}{D},\quad
C=\frac{q\theta[(k+h)(2-\theta)+\theta]}{D}.
\]
The covariance \(C\) has a sharp, size-independent sign boundary:
\[
\boxed{\theta_h=\frac{h+2-\sqrt{h^2+4}}{h}\in(0,1).}
\]
For every \(k\ge2\), adding one flexible leaf **strictly decreases** \(C\) when \(0<\theta<\theta_h\), leaves \(C\) exactly unchanged at \(\theta=\theta_h\), and **strictly increases** \(C\) when \(\theta_h<\theta\le1\). This threshold depends only on the *total* number \(h\) of stubborn leaves, not on their split \(a:b\) or their two opinion values.

In contrast, the Pearson correlation between distinct flexible leaves strictly increases with \(k\) for every \(0<\theta\le1\), and for \(0<\theta<1\) both individual variances strictly decrease as \(k\) increases. As \(k\to\infty\), all three second moments approach the same positive limit
\[
\frac{q\theta(2-\theta)}{\theta^2-8\theta+8},
\]
while the expected squared difference between two flexible leaves vanishes at order \(k^{-1}\). Thus growing the flexible periphery synchronizes *individual differences* without eliminating stationary common fluctuations.

## Assumptions and scope

The network is an undirected unweighted star; only the centre connects to every leaf. Each flexible agent has an independent unit-rate Poisson activation clock; updating is **one-sided** (the selected neighbour does not update). The receiving agent uses the same \(\theta\) for every neighbour, including stubborn ones. The stochastic dynamics are initialized arbitrarily in a bounded opinion interval containing \(z_0,z_1\), and all stated quantities concern the unique limiting stationary law. The uniqueness follows from the standard contraction/absorption argument for finite connected partially averaging networks with reachable stubborn sources, as in Acemoglu–Como–Fagnani–Ozdaglar, arXiv:1009.2653, Theorems 1 and 3. If \(z_0=z_1\) or one stubborn group is absent then \(q=0\) and the strict comparison becomes vacuous, hence these cases are excluded.

The formula uses ordinary population covariances under the invariant distribution, not temporal autocovariances, deterministic equilibrium dispersion, or the symmetric two-sided averaging protocol.

## Proof

Because each flexible leaf only listens to the centre, all flexible stationary means coincide. The centre's harmonic stationarity equation then forces every flexible mean to equal the mean \(m\) of the \(h\) stubborn values. Center opinions at \(m\): let \(Y_i=X_i-m\), and note that the sum of the stubborn centred opinions is zero, while their sum of squared centred opinions is \(hq\).

By permutation symmetry among the \(k\) flexible leaves, denote by \(v=\mathbb E[Y_C^2]\) the centre variance, by \(u=\mathbb E[Y_L^2]\) a leaf variance, by \(w=\mathbb E[Y_CY_L]\) a centre–leaf covariance, and by \(z=\mathbb E[Y_{L_1}Y_{L_2}]\) the covariance of two distinct flexible leaves. Stationary generator balance for these four second moments gives
\[
\begin{aligned}
(2-\theta)u&=\theta v+2(1-\theta)w,\\
(k+h)(2-\theta)v&=\theta(ku+hq)+2(1-\theta)kw,\\
(k+2h+1)w&=u+(k+h)v,\\
z&=w.
\end{aligned}
\]
For example, the first identity follows by replacing one leaf with \((1-\theta)Y_L+\theta Y_C\). For the second, the central neighbour has square \(u\) with probability \(k/(k+h)\), and the \(h\) stubborn neighbours contribute total squared centered value \(hq/(k+h)\). The third identity averages the two possible updating endpoints of a centre–leaf product and uses the final identity; the latter follows because either leaf in a leaf–leaf product can update toward the centre. All mixed products with stubborn centred values vanish because flexible centred means are zero. Every balance equation is exact at stationary law.

Solving this three-equation linear system yields \(V_C=v\), \(V_L=u\), and \(C=w=z\) as displayed. Its denominator is strictly positive because \(\theta^2-8\theta+8\ge1\), \(2\theta^2-8\theta+8\ge2\), and \(2\theta-\theta^2>0\) for \(0<\theta\le1\).

Writing \(D_k=D(k,h,\theta)\), direct subtraction of the two rational functions at successive sizes yields the **exact** identity
\[
C(k+1)-C(k)=
-\frac{q\theta^2\,[h\theta^2-(2h+4)\theta+4]}{D_kD_{k+1}}.
\]
The bracket is strictly decreasing on \((0,1]\), begins at \(4\), and ends at \(-h\). Its unique root in \((0,1)\) is \(\theta_h\), proving the three-way classification, including the equality case for every \(k\). Since \(q>0\), no equality is hidden by a zero amplitude. The root decreases strictly as \(h\) grows, directly from \(h\theta(2-\theta)=4(1-\theta)\).

For \(0<\theta<1\), another exact subtraction gives
\[
\begin{aligned}
V_C(k+1)-V_C(k)&=-\frac{4q\theta(1-\theta)[2h(2-\theta)+\theta]}{D_kD_{k+1}}<0,\\
V_L(k+1)-V_L(k)&=-\frac{2q\theta^2(1-\theta)[h(4-\theta)+2]}{D_kD_{k+1}}<0.
\end{aligned}
\]
At \(\theta=1\), \(V_C=V_L=q\) independently of \(k\). For two distinct flexible leaves,
\[
\operatorname{Corr}(X_{L_1},X_{L_2})=\frac{C}{V_L}
=\frac{(k+h)(2-\theta)+\theta}{k(2-\theta)+2h+\theta},
\]
whose one-unit increment is
\[
\frac{h\theta(2-\theta)}{[k(2-\theta)+2h+\theta][(k+1)(2-\theta)+2h+\theta]}>0.
\]
Finally, divide all three displayed second-moment formulas by \(k\) and let \(k\to\infty\). Their common strictly positive limit is as claimed. The leaf difference satisfies
\[
\mathbb E[(X_{L_1}-X_{L_2})^2]=2(V_L-C)=\frac{2hq\theta^2}{D_k}=\Theta(k^{-1}).
\]
These statements are about stationary fluctuations and do not imply almost-sure temporal convergence.

## Verification

The standalone `verify.py` uses full labelled stationary moment balance equations, independently of the symmetry-reduced three-equation derivation. It solves these exactly over \(48\) nontrivial parameter instances with \(k=2,3,4\), both balanced and unbalanced stubborn populations, and four trust levels, checking every labelled second moment. Separate exact rational checks cover all integer stubborn totals \(2\le h\le19\) at six trust levels; symbolic identities independently check the adjacent-size covariance difference, variance differences, and leaf-correlation derivative. Running `python verify.py` with Python 3.10+ and SymPy produces `PASS: 608 exact labelled and symbolic assertions`.

As concrete rational witnesses for \(a=b=1\), at \(\theta=1/2\) the common off-diagonal covariance falls from \(13/292\) for \(k=2\) to \(2/45\) for \(k=3\), whereas the leaf correlation rises from \(13/15\) to \(8/9\). At \(\theta=2/3\), the common covariance instead rises from \(9/128\) to \(11/156\). Exact rational checks support the derivation; the all-size theorem follows from the displayed algebraic identities, not from the finite test cases.

## Relationship to prior work

Acemoglu, Como, Fagnani and Ozdaglar (arXiv:1009.2653, 2010; published 2013) introduce this one-sided partially averaging stubborn-agent model and derive general linear equations for stationary first and second moments (Theorem 3). Their Section 5 explicitly computes means on trees and variances for the special case of full copying, \(\theta=1\). Those general equations **already encompass the model's covariance computations implicitly**; we do not claim otherwise. The result here is the fully explicit arbitrary-partial-trust star solution and, chiefly, the all-size *comparative-static* threshold at which the sign of change in covariance under adding flexible leaves reverses, alongside the strict opposite behaviour of normalized correlation.

Yildiz and colleagues (2013) study **binary** opinion copying with stubborn agents and therefore do not supply the interior-\(\theta\) averaging phase boundary. Later work by Xing and Johansson studies transient behaviour on two-community gossip networks, with a different contact and update architecture. The exact threshold was not found in the inspected source sections and searches, but the original general moment characterisation makes derivability from published equations an explicit priority risk.

## Limitations

The graph is a star, all update rates and trust weights are homogeneous, and stubborn opinions take exactly two distinct values. The result does not claim the same threshold for nonstar networks, unequal influence rates, nonlinear opinion adoption, or symmetric pairwise averaging. Covariance and correlation are ensemble statistics at stationarity, not direct causal effects observed in a population. No independent audit or historical-priority certification has been performed. General moment equations in the founding literature algebraically imply the specialized formulas after a further calculation; originality, where present, is in the exact all-size sign classification and its consequences, not the existence of a second-moment system.

## References

1. D. Acemoglu, G. Como, F. Fagnani, A. Ozdaglar, *Opinion fluctuations and disagreement in social networks*, arXiv:1009.2653 (first submitted 2010-09-14); *Mathematics of Operations Research* 38(1), 1–27 (2013). https://arxiv.org/abs/1009.2653 ; https://doi.org/10.1287/moor.1120.0570 ; freely accessible manuscript: https://economics.mit.edu/sites/default/files/publications/Opinion%20Fluctuations%20and%20Disagreement%20in%20Social%20Ne.pdf
2. E. Yildiz, A. Ozdaglar, D. Acemoglu, A. Saberi, A. Scaglione, *Binary opinion dynamics with stubborn agents*, *ACM Transactions on Economics and Computation* 1(4), Article 19 (2013). https://doi.org/10.1145/2538508
3. Y. Xing, K. H. Johansson, *Transient Behavior of Gossip Opinion Dynamics with Community Structure*, arXiv:2205.14784 (2022). https://arxiv.org/abs/2205.14784
