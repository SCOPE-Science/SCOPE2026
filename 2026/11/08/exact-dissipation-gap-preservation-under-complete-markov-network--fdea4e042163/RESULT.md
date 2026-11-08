# Exact dissipation-gap preservation under complete Markov-network refinement

## Finding

A finite irreducible nonequilibrium continuous-time Markov chain can be refined to arbitrarily large, **fully connected** chains without changing either its stationary entropy-production rate or its global minimum over probability distributions. More precisely, let \(Q=(q_{ij})\) be a generator on \(m\geq 3\) states, with every off-diagonal rate strictly positive. For any integer \(n\geq1\) and \(c>0\), form \(mn\) states \((i,a)\), \(1\leq i\leq m\), \(1\leq a\leq n\), with rates

\[
k_{(i,a),(j,b)}=\begin{cases}q_{ij}/n,&i\ne j,\\c/n,&i=j,\ a\ne b.\end{cases}
\]

The diagonal is minus the exit rate. For positive probability vectors \(p=(p_{ia})\) define \(P_i=\sum_a p_{ia}\), \(u_a=1/n\) and \(\mu_i(a)=p_{ia}/P_i\). Write \(\sigma_Q(P)\) for the total Schnakenberg entropy-production rate. The **exact** off-stationary identity is

\[
\begin{aligned}
\sigma_{K^{(n)}}(p)=\sigma_Q(P)
&+\sum_{i=1}^m P_i(c+q_i^{\rm out})D(\mu_i\Vert u)\\
&+\sum_{i=1}^m(cP_i+q_i^{\rm in}(P))D(u\Vert\mu_i),
\end{aligned}
\tag{1}
\]

where \(q_i^{\rm out}=\sum_{j\ne i}q_{ij}\), \(q_i^{\rm in}(P)=\sum_{j\ne i}P_jq_{ji}\), and \(D(\cdot\Vert\cdot)\) is ordinary finite-alphabet relative entropy. Hence

\[
\inf_{p\in\Delta_{mn}}\sigma_{K^{(n)}}(p)=\min_{P\in\Delta_m}\sigma_Q(P),\qquad
\sigma_{K^{(n)}}(\pi_i/n)=\sigma_Q(\pi),
\tag{2}
\]

for the stationary law \(\pi\) of \(Q\), and every minimizer is uniform within each block. The exact EPR excess of nonuniform microscopic conditional distributions is the two-sided relative-entropy penalty in (1).

The construction is not restricted to interchangeable clones. More generally choose **any** strictly positive probability law \(\nu_i\) on the clones of macrostate \(i\) and constants \(c_i>0\), and assign the rates \(k_{(i,a),(j,b)}=q_{ij}\nu_j(b)\) between blocks and \(k_{(i,a),(i,b)}=c_i\nu_i(b)\) within blocks. Identity (1) remains exact with \(u\) replaced by \(\nu_i\) in each divergence and \(c\) replaced by \(c_i\) in the corresponding block coefficient. The stationary law is \(\pi_i\nu_i(a)\), the minimum still equals the coarse minimum, and all off-diagonal rates are strictly positive. Choosing nonuniform \(\nu_i\) makes microscopic stationary occupations and incoming transition rates heterogeneous, while preserving the same explicit gap bound (3). This larger destination-weighted class, rather than mere indistinguishable duplication, is the principal refinement statement.

For a concrete three-state seed take the strictly positive off-diagonal rates

\[
Q=\begin{pmatrix}-21&1&20\\19&-25&6\\1&4&-5\end{pmatrix},\qquad
\pi=\frac1{692}(101,85,506).
\]

With \(P^*=(9,7,84)/100\), one has the rigorously certified inequality

\[
\frac{\sigma_{K^{(n)}}(\pi_i/n)}{\min_p\sigma_{K^{(n)}}(p)}-1
\geq\frac{\sigma_Q(\pi)}{\sigma_Q(P^*)}-1
>\frac9{50}\qquad\text{for every }n\geq1.
\tag{3}
\]

The seed comparison is approximately \(0.1889584033\), and the exact ratio to the true minimum is at least this large. Thus **complete graph density and arbitrarily large state count alone do not force near-minimum entropy production**. This is a deterministic boundary on graph-size implications, not a statement about the typical random ensemble studied in the motivating paper.

## Assumptions and scope

The state space is finite and all off-diagonal rates are positive. Both forward and reverse transitions exist, all states are invariant under kinematic time reversal, and the dimensionless EPR is

\[
\sigma_Q(P)=\sum_{i<j}(P_iq_{ij}-P_jq_{ji})\log\frac{P_iq_{ij}}{P_jq_{ji}}.
\]

The same expression is used for \(K^{(n)}\). At boundary distributions containing zero probabilities, its value is defined as the lower-semicontinuous extension, possibly \(+\infty\); because all rates are positive, every such boundary distribution has infinite EPR. The rate \(c\) is an arbitrary fixed positive constant. The vertex set is a complete directed graph for every \(n\), and exit rates are \(q_i^{\rm out}+c(n-1)/n\), uniformly bounded in \(n\). The result concerns mathematical finite-state Markov thermodynamics, not a conservation-constrained physical chemical network.

## Proof

**1. Coarse-grained currents.** For distinct macrostates \(i,j\), the flux from clone \((i,a)\) to clone \((j,b)\) is \(x_{ab}=P_i\mu_i(a)q_{ij}/n\). The reverse flux is \(y_{ab}=P_j\mu_j(b)q_{ji}/n\). Their sums over all clone pairs are \(A=P_iq_{ij}\) and \(B=P_jq_{ji}\). Applying the logarithmic chain rule to the two directed flux sums gives the pairwise entropy contribution

\[
(A-B)\log(A/B)+A\{D(\mu_i\Vert u)+D(u\Vert\mu_j)\}+B\{D(\mu_j\Vert u)+D(u\Vert\mu_i)\}.
\tag{4}
\]

To check the coefficients directly, the normalized forward flux law on clone pairs is \(\mu_i\otimes u\) and the normalized reverse flux law is \(u\otimes\mu_j\); relative entropy is additive under tensor products. Summing (4) over unordered macrostate pairs yields the first term in (1), the outgoing-weighted forward conditional divergences, and the incoming-weighted reverse conditional divergences.

**2. Within-block currents.** Every within-block unordered pair contributes \((cp_{ia}/n-cp_{ib}/n)\log(p_{ia}/p_{ib})\). Summing yields

\[
\sum_{a<b}\frac{c}{n}(p_{ia}-p_{ib})\log\frac{p_{ia}}{p_{ib}}
=cP_i\{D(\mu_i\Vert u)+D(u\Vert\mu_i)\}.
\tag{5}
\]

This identity follows by expanding the double sum \(\frac{c}{n}\sum_{a,b}p_{ia}\log(p_{ia}/p_{ib})\). Combining (4) and (5) proves (1), exactly, for all strictly positive \(p\).

For general target weights \(\nu_i\), the normalized forward clone-pair law in (4) is \(\mu_i\otimes\nu_j\) and the reversed law is \(\nu_i\otimes\mu_j\). The same KL chain rule produces the stated replacements. Within block \(i\), the normalized directed exchange flux law is \(\mu_i\otimes\nu_i\) with reverse \(\nu_i\otimes\mu_i\), yielding \(c_iP_i[D(\mu_i\Vert\nu_i)+D(\nu_i\Vert\mu_i)]\). The inequalities and equalities therefore hold with arbitrary positive \(\nu_i\), and uniform lift becomes the weighted lift \(p_{ia}=P_i\nu_i(a)\). This proof uses no rapid intrablock equilibration assumption.



**3. Minimization and stationary distribution.** All conditional relative entropies are nonnegative, and both their coefficients are strictly positive. Thus \(\sigma_{K^{(n)}}(p)\geq\sigma_Q(P)\), with equality precisely when \(\mu_i=u\) for every \(i\). Every macrovector \(P\) admits that uniform lift, so taking infima gives the first equality of (2). The macrochain \(Q\) is irreducible and has a unique stationary distribution \(\pi\). Directly substituting \(p_{ia}=\pi_i/n\) into the microscopic balance equation shows it is stationary: interblock inflow is \(n^{-1}\sum_{j\ne i}\pi_jq_{ji}\) and interblock outflow is \(n^{-1}\pi_iq_i^{\rm out}\); intrablock exchanges cancel. Irreducibility gives uniqueness. The divergence terms then vanish, establishing the second equality in (2).

**4. A certified finite seed.** For the displayed \(Q\), rational stationarity is verified by the three equations \(\pi Q=0\). The seed EPR is

\[
\sigma_Q(\pi)=\frac{757}{346}\log\frac{760}{3}.
\]

At the rational trial law \(P^*\), the EPR equals

\[
\sigma_Q(P^*)=\frac{31}{25}\log\frac{133}{9}+\frac{24}{25}\log\frac{15}{7}+\frac{147}{50}\log 8.
\]

The standalone `check_lift.py` evaluates rigorously enclosing **rational** intervals for each logarithm. To bound \(\log x\), it writes \(x=2^k y\) with \(1\le y<2\), then uses \(z=(y-1)/(y+1)\), with \(0\le z<1/3\):

\[
\log y=2\sum_{j=0}^{M-1}\frac{z^{2j+1}}{2j+1}+R_M,
\quad 0\le R_M\le\frac{2z^{2M+1}}{(2M+1)(1-z^2)}.
\]

The same interval scheme evaluates \(\log 2\) at \(z=1/3\); for negative integer \(k\), interval endpoints are reversed when multiplying. With \(M=32\) and exact rational arithmetic the resulting lower interval endpoint for \(50\sigma_Q(\pi)-59\sigma_Q(P^*)\) is strictly positive (numerically above \(4.56\)). Therefore \(50\sigma_Q(\pi)>59\sigma_Q(P^*)\). Because the true minimum is at most \(\sigma_Q(P^*)\), this proves (3). The cycle products \(q_{12}q_{23}q_{31}=6\) and \(q_{21}q_{32}q_{13}=1520\) differ; consequently no positive vector has zero EPR, the minimum is strictly positive, and the ratio is defined.

## Verification

Run `python3 check_lift.py` using Python's standard library. The script checks the exact rational stationary balance and certified logarithmic inequality. It separately constructs microstate transition currents for block multiplicities \(n\in\{1,2,3,5,8\}\) and exchange rates \(c\in\{1/10,1,7\}\), confirms stationary EPR preservation, compares independently computed direct EPR with both sides of (1) for randomly chosen strictly positive rational microscopic distributions, and confirms the positivity of the conditional penalty. The additional nonuniform target-law tests use arbitrary strictly positive normalized geometric weights and block-dependent exchange rates, checking both exact stationarity and the extended all-distributions identity. The test suite completed 385 internal checks. These finite tests are not substituted for the arbitrary-\(n\) proof above.

## Relationship to prior work

Ray and Boyd (arXiv:2507.10476, initially public July 14, 2025) derive the finite-CTMC minimum-entropy-production problem, exhibit a three-state NESS/MEPS discrepancy, and observe near-minimum behavior in their *sampled* large complete networks. Their figures and discussion do not establish universality in graph size. Equations (1)–(3) give a distinct constructive theorem: all-state EPR decomposition, exact minimum-preserving complete-state refinement, and a fixed explicit positive scaled excess for arbitrarily large dense networks. It does **not** contradict the paper's ensemble-specific numerical trend.

Teza and Stella (arXiv:2003.08674), Puglisi et al. (arXiv:1002.4520), and Busiello et al. (doi:10.1088/1367-2630/ab29c0) study entropy-production preservation and loss under coarse graining. Their reported conclusions establish that some coarse-grainings can preserve stationary EPR and some lose it. The assertion here specifically concerns a fully positive rate-matrix refinement that preserves a **global** EPR optimizer and gives an exact conditional-information penalty for **all** nonequilibrium distributions; neither stationary EPR invariance alone nor the abstract log-sum inequality by itself specifies the quantitative complete-graph construction and seed bound. The relative-entropy identity is a specialization of the general coarse-graining decomposition already developed by Esposito (arXiv:1112.5410, Sec. IV.2); **the identity itself is not claimed as original**. The new target is the destination-weighted complete-network persistence of the global MEPS and a certified, fixed NESS/MEPS gap at arbitrarily large state count. Its derivability from established coarse-graining machinery is the chief originality risk.

## Limitations

The constructed rates have an exact three-block lumpability structure, even for nonuniform clone weights; these are not independently sampled random complete-network rates. The theorem supplies a deterministic boundary and does not disprove concentration under specific stochastic sampling assumptions. The microscopic state count grows without increasing independent coarse dynamic degrees of freedom. The certificate proves a strict bound using a nonoptimal trial distribution, not the exact three-state minimizing law or its uniqueness beyond blockwise uniformity. This work is self-reviewed only; no independent audit or comprehensive priority determination has been performed.

## References

1. K. J. Ray and A. B. Boyd, *Large Interconnected Thermodynamic Systems Nearly Minimize Entropy Production*, arXiv:2507.10476, first submitted July 14, 2025. https://arxiv.org/abs/2507.10476
2. G. Teza and A. L. Stella, *Exact Coarse Graining Preserves Entropy Production out of Equilibrium*, arXiv:2003.08674. https://arxiv.org/abs/2003.08674
3. A. Puglisi, S. Pigolotti, L. Rondoni, and A. Vulpiani, *Entropy production and coarse-graining in Markov processes*, arXiv:1002.4520. https://arxiv.org/abs/1002.4520
4. D. M. Busiello, J. Hidalgo, and A. Maritan, *Entropy production for coarse-grained dynamics*, New J. Phys. 21 (2019) 073004. https://arxiv.org/abs/1810.01833
5. M. Esposito, *Stochastic thermodynamics under coarse-graining*, Phys. Rev. E 85 (2012) 041125. https://arxiv.org/abs/1112.5410
