# Sharp cost ceiling, critical exclusion, and quorum reversals in protective public-goods dynamics

## Finding

For the three-strategy, well-mixed, quorum-activated collective-risk public-goods model of Li et al. [1], the exact largest possible selective advantage of protective cooperation over ordinary cooperation is obtained on the defector–protector edge. Write \(N\ge3\) for group size, \(2\le M\le N-1\) for the protection quorum, \(n=N-1\), \(h=M-1\), \(s=N-M=n-h\), and \(0<\rho<1\) for the failure-survival factor of one defector. Define

\[
H_{N,M}(\rho)=\binom{n}{h}\left(\frac{h}{n}\right)^h\left(\frac{s}{n}\right)^s(1-\rho^s).
\]

If \(L>0\) is the collective-failure loss, \(\omega\in[0,1]\) the efficacy of protection, and \(k>0\) its additional cost, then the following **one linked sharp incentive-and-dynamics theorem** holds.

1. The maximum of \(P_S-P_C\) over all population compositions is exactly \(-k+L\omega H_{N,M}(\rho)\). The maximizer of its protection-benefit term is unique: the frequency of ordinary cooperators is zero, that of protectors is \(h/n\), and that of defectors is \(s/n\). In particular, a positive protective advantage occurs at **some strictly interior composition** if and only if \(k<L\omega H_{N,M}(\rho)\).
2. If \(k\ge L\omega H_{N,M}(\rho)\), every replicator trajectory initially containing both ordinary and protective cooperators eliminates protection **exponentially**. It converges to an equilibrium on the ordinary-cooperator–defector edge: one of the two vertices or its at most one interior saddle. The extinction conclusion includes equality in the cost threshold, despite its being a weak, rather than uniform, payoff bound over the whole simplex.
3. At fixed \(N\) and \(\rho\), the absolute incentive ceiling \(H_{N,M}(\rho)\) is uniquely greatest at the **smallest quorum** \(M=2\). Nevertheless, the ceilings are not in general decreasing with quorum: for adjacent quorums indexed by \(h\) and \(h+1\), they always strictly decrease when \(2h\le n-1\); when \(2h>n-1\), there exists a unique \(\rho_h\in(0,1)\) such that the higher quorum has the **larger** ceiling precisely for \(0<\rho<\rho_h\). This threshold is uniquely determined by
\[
\frac{1-\rho_h^{s-1}}{1-\rho_h^s}=\frac{B_{n,h}}{B_{n,h+1}},\qquad
B_{n,h}:=\binom nh\left(\frac hn\right)^h\left(1-\frac hn\right)^{n-h}.
\]
   For example, at \(N=5\), the ceiling for quorum \(M=4\) exceeds that for \(M=3\) exactly when \(\rho<1/8\). At \(\rho=1/16\) they are \(405/1024\) and \(765/2048\), respectively. Therefore with \(L\omega=1\) and \(k=3/8\), protection is exponentially eliminated from all states containing ordinary cooperators for \(M=3\), but at \(M=4\) there are strictly interior compositions where protection locally outperforms ordinary cooperation. This does **not** assert stable protective coexistence at \(M=4\).
4. When \(\rho\in(0,1)\) is fixed and \(h/n\to\theta\in(0,1)\), the incentive ceiling obeys \(H_{N,M}(\rho)\sim[2\pi n\theta(1-\theta)]^{-1/2}\). For fixed \(h\) and \(n\to\infty\), it instead tends to \(e^{-h}h^h/h!\). Thus extensive and fixed quorums have qualitatively different large-group cost scales.

## Assumptions and scope

A population has frequencies \((x,y,z)\) for ordinary cooperators \(C\), defectors \(D\), and protective cooperators \(S\), respectively, with \(x,y,z\ge0\) and \(x+y+z=1\). Each random group contains the focal player and \(n=N-1\) independent co-players. Ordinary and protective cooperators contribute the same baseline public-good cost \(c>0\), and protection costs an additional \(k>0\). The per-contribution return factor is \(r\) with \(1<r<N\). In a group with \(j\) defectors, the baseline failure probability is \(1-\rho^j\). At least \(M\) protectors, counting the focal protector when present, activate a proportional risk reduction \(\omega\). Failure causes a common loss \(L>0\). The population follows the standard smooth continuous-time three-strategy replicator equations with expected group payoffs from [1]. No mutation or strategy immigration occurs.

The assertion of extinction applies to initial states \(x(0)>0,z(0)>0\), allowing \(y(0)=0\). If \(z(0)=0\), protection is already absent. No conclusion of extinction is made for the invariant face \(x(0)=0\): on that face ordinary cooperators cannot invade if absent, and protective boundary equilibria may exist.

## Proof

**Exact pivotality and optimization.** A focal protector differs from an ordinary cooperator only in paying \(k\) and possibly completing a quorum. It is pivotal exactly when \(h=M-1\) among its \(n\) co-players are protectors. Summing all remaining co-player compositions gives the exact polynomial, already implicit in the finite sums of [1],
\[
\Psi_M(x,y,z)=\binom nh z^h\left[(x+y)^s-(x+\rho y)^s\right],
\qquad P_S-P_C=-k+L\omega\Psi_M.
\]

Holding \(z\) fixed and substituting \(y=1-x-z\), the second base in the bracket becomes \(\rho(1-z)+(1-\rho)x\). Since \(s\ge1\) and \(0<\rho<1\), the bracket is strictly decreasing in \(x\) for \(0\le x<1-z\) when \(0<z<1\). Thus its unique maximal value for each positive \(z\) is at \(x=0\). There it becomes \((1-\rho^s)\binom nh z^h(1-z)^s\). Differentiating its logarithm on \((0,1)\) gives \(h/z-s/(1-z)\), which has the unique zero \(z=h/n\) and changes from positive to negative. The endpoints give zero. The unique global maximizer is therefore \((x,y,z)=(0,s/n,h/n)\), proving the ceiling and its strict interior attainability criterion by continuity.

**Critical extinction and edge limit.** Along any replicator trajectory with \(x,z>0\), the log ratio \(R=z/x\) satisfies
\[
\frac{d}{dt}\log R=P_S-P_C=-k+L\omega\Psi_M.
\]
For \(k\ge L\omega H_{N,M}(\rho)\), this is nonpositive. Let \(R_0=z(0)/x(0)<\infty\); the trajectory stays in the compact simplex slice \(K_{R_0}=\{(x,y,z):z\le R_0x\}\). The unique maximizing composition above has \(x=0,z=h/n>0\) and thus lies **outside** this slice. Consequently \(\sup_{K_{R_0}}\Psi_M<H_{N,M}(\rho)\), and
\[
\varepsilon:=k-L\omega\sup_{K_{R_0}}\Psi_M>0
\]
(with the same conclusion when \(\omega=0\)). Therefore \(R(t)\le R_0e^{-\varepsilon t}\) and \(z(t)\le R_0e^{-\varepsilon t}\). This proves exponential extinction even at equality, not merely the standard strictly dominated case.

The full vector field is continuously differentiable on the compact simplex. Because \(z(t)\) decays exponentially, the ordinary-cooperator coordinate satisfies \(\dot x=g(x)+O(z(t))\) uniformly, where
\[
g(x)=x(1-x)\left[\frac{rc}{N}-c+L(1-\rho)\bigl(\rho+(1-\rho)x\bigr)^n\right].\]
The bracket is strictly increasing, so \(g\) has only the endpoint zeros and at most one interior zero. A bounded real trajectory obeying a scalar autonomous field plus a uniformly vanishing perturbation, with finitely many isolated field zeros, converges to one of those zeros: otherwise there would be an interval strictly between its distinct limit inferior and superior containing no zero, across which the eventual derivative has one fixed sign, contradicting repeated passages in opposite directions. Since \(z\to0\), the entire trajectory converges to the stated edge equilibrium. The interior edge zero, when present, has a positive tangential derivative and is the saddle identified by [1].

**Sharp quorum comparisons.** Put \(B_{n,h}=\binom nh(h/n)^h(s/n)^s\), so \(H_{N,M}(\rho)=B_{n,h}(1-\rho^s)\). For \(1\le h\le n-2\), direct factorial cancellation yields
\[
\frac{B_{n,h+1}}{B_{n,h}}=\frac{(1+1/h)^h}{(1+1/(s-1))^{s-1}}.
\]
The function \(u\mapsto(1+1/u)^u\) is strictly increasing for positive \(u\), so the ratio is below, equal to, or above one according as \(2h<n-1\), \(2h=n-1\), or \(2h>n-1\). In particular the sequence \(B_{n,h}\) falls toward its middle and rises symmetrically afterward, with maximum \(B_{n,1}=B_{n,n-1}\). The risk factor \(1-\rho^{n-h}\) strictly falls with \(h\), so \(M=2\) is the unique maximizer of \(H\).

For adjacent quorums, the full ratio is
\[
\frac{H_{N,M+1}(\rho)}{H_{N,M}(\rho)}=
\frac{B_{n,h+1}}{B_{n,h}}\,
\frac{1-\rho^{s-1}}{1-\rho^s}.
\]
The second factor is strictly decreasing in \(\rho\in(0,1)\), from one to \((s-1)/s\). If \(2h\le n-1\), the ratio is strictly less than one. If \(2h>n-1\), the first factor \(Q=B_{n,h+1}/B_{n,h}\) exceeds one. Nevertheless \(Q<s/(s-1)\), since \((1+1/h)^h<e<(1+1/(s-1))^s\). Hence the full ratio passes strictly from greater than one to less than one exactly once, giving the unique \(\rho_h\) and its stated orientation. When \(n=4,h=2\), the first factor is \(9/8\), and the second is \(1/(1+\rho)\), yielding \(\rho_h=1/8\). Direct substitution gives the two displayed exact values.

**Large-group scales.** The standard Stirling approximation for a binomial point mass at its mean gives \(B_{n,h}\sim[2\pi n\theta(1-\theta)]^{-1/2}\) when \(h/n\to\theta\in(0,1)\). In this regime \(\rho^{n-h}\to0\). For fixed \(h\), \(\binom nh(h/n)^h(1-h/n)^{n-h}\to e^{-h}h^h/h!\) and the risk factor again tends to one. Both limits follow.

## Verification

The bundled standard-library checker `check.py` uses exact rational arithmetic to independently sum the multinomial pivotal event over \(13{,}680\) group-size, quorum, risk and composition combinations; checks the closed formula and global ceiling for each; verifies the unique cheapest-quorum incentive envelope for group sizes \(3\) through \(11\); tests the exact reversal at \(N=5\); and checks the adjacent-quorum comparison at representative group sizes. All checks passed. Finite checks are not used to infer the general inequality, the exponential exclusion result, or the asymptotic statements: those follow from the displayed proofs.

Run `python3 check.py` using a standard Python 3 installation.

## Relationship to prior work

Li et al. [1] give the three-strategy payoffs, pivotality identity and numerical bifurcation diagrams, and distinguish rare invasion from established protective coexistence. In particular, their quorum comparison tests stability thresholds for one fixed group size; it does not provide the global payoff ceiling, the critical-cost extinction theorem, or the per-adjacent-quorum sign-reversal classification proved here. These statements refer to a maximum possible *relative selective advantage*, **not** to the critical efficacy for existence of a locally attracting protective equilibrium.

Nöldeke and Peña [2] had already proved unimodality and the maximum of an ordinary unweighted binomial pivotal probability, and its fixed-quorum large-group limit, in a different **two-action symmetric participation game**. Those ingredients are not claimed as discoveries here. The present model has three strategies, a defector-count-dependent risk weight, and a two-dimensional replicator flow. The source's binomial maximization alone does not entail the exact risk-dependent quorum reversals or the weak-threshold exponential extinction with a potential protective boundary equilibrium. Dominated-strategy extinction under replicator dynamics is also classical [3]; the proof here adds the sharp model-specific boundary and equality case.

## Limitations

The sharp threshold characterizes whether protective cooperation can ever outperform ordinary cooperation, and gives a sufficient exact condition for its global elimination when ordinary cooperators are present. When cost is below the threshold, local advantage somewhere does **not** imply that protection persists, invades from rarity, produces an equilibrium, or becomes stable. Reversals in this threshold need not reverse the stability thresholds plotted in [1]. Results assume independent random group matching, the precise saturating failure law, homogeneous costs and benefits, replicator dynamics, and no mutations. They do not establish stochastic finite-population claims or independent validation. Unindexed earlier treatments of related quorum-payoff maximization remain a literature risk.

## References

[1] S. Li, X. Li, J. He, L. Shi, A. Szolnoki, *Bifurcation and Multistability in a Collective-Risk Public Goods Game with Quorum-Activated Protection*, arXiv:2609.28132, first posted 2026-09-23, https://arxiv.org/abs/2609.28132 .

[2] G. Nöldeke and J. Peña, *Group size and collective action in a binary contribution game*, Journal of Mathematical Economics 88 (2020), 42–51, https://doi.org/10.1016/j.jmateco.2020.02.003 ; public author copy https://jorgeapenas.github.io/assets/pdf/Noeldeke2020.pdf .

[3] *Evolutionary Game Theory*, Stanford Encyclopedia of Philosophy, discussion of the classical dominated-strategy elimination theorem, https://plato.sydney.edu.au/entries/game-evolutionary/ .
