# Sharp segregation threshold in a two-community opinion–public-goods game

## Finding

In the homogeneous public-goods/opinion coevolution game introduced by Davidson, Zino, Cao and Ye, a balanced two-community influence network has **exactly one, two or four strict pure Nash equilibria**, and every one is constant in each community. The full phase diagram is explicit, including a sharp homophily threshold for the birth of the two polarized equilibria.

Let \(n=2m\), where \(m\geq2\). Let \(0\leq a\leq1\) be the total fraction of each agent's opinion influence assigned to its own community (other than itself). Write
\[
c=\frac{\beta}{\beta+\lambda},\qquad d=1-c,\qquad
K=\frac{\beta\lambda}{\beta+\lambda},\qquad
\eta=\frac{\alpha(1-r/n)}{K}.
\]
Here \(\alpha,\beta,\lambda>0\), \(\alpha+\beta+\lambda=1\), and \(1<r<n\). In particular, \(0<c,d<1\), \(K>0\) and \(\eta>0\).

The strict equilibrium action patterns, with their uniquely determined equilibrium opinion vectors, are:

1. **Universal defection:** always, \((\mathbf0,\mathbf0)\).
2. **Universal cooperation:** \((\mathbf1,\mathbf1)\) precisely when \(\eta<1/2\).
3. **The two community-polarized patterns:** precisely when
\[
\eta<\frac12
\quad\text{and}\quad
a>a_{\mathrm c}:=\frac12\left(1+
\frac{2\eta}{d+2c\eta}\right).
\]
In one polarized pattern community \(A\) cooperates and \(B\) defects; in the other, their roles reverse. For the first pattern, every opinion in \(A\) is
\[
y_A=\frac12\left(1+\frac{d}{1-c(2a-1)}\right),
\quad
y_B=\frac12\left(1-\frac{d}{1-c(2a-1)}\right);
\]
the second pattern reverses these values.

Consequently the numbers of strict pure Nash equilibria are \(1\) when \(\eta\geq1/2\); \(2\) when \(\eta<1/2\) and \(a\leq a_{\mathrm c}\); and \(4\) when \(\eta<1/2\) and \(a>a_{\mathrm c}\). At exact equality in either threshold the corresponding cooperative action is only a weak best response, not a strict one. Under the paper's deterministic defection-at-ties rule, the fixed points coincide with the above strict equilibria.

For fixed benefit ratio \(r/n\), the critical homophily and equilibrium counts do not depend on community size \(m\).

## Assumptions and scope

There are \(n=2m\geq4\) individuals divided into named communities \(A,B\) of equal size \(m\). An individual chooses an action \(x_i\in\{0,1\}\), where \(1\) contributes to a public good, and an opinion \(y_i\in[0,1]\). Its payoff is
\[
\pi_i(x_i,y_i;x_{-i},y_{-i})=
\alpha\left(\frac r n\sum_{j=1}^n x_j-x_i\right)
-\frac\beta2\sum_j w_{ij}(y_i-y_j)^2
-\frac\lambda2(x_i-y_i)^2.
\]
The zero-diagonal, symmetric, row-stochastic influence matrix is
\[
w_{ij}=
\begin{cases}
a/(m-1),&i\ne j\text{ in the same community},\\
(1-a)/m,&i,j\text{ in distinct communities},\\
0,&i=j.
\end{cases}
\]
All players have common parameters; the prejudice coefficients are zero. This is a static joint action/opinion Nash analysis; the public-goods multiplier \(r\) is deterministic, and there is no randomness. Every equilibrium in the claim is *strict* in the usual game-theoretic sense: each player's stated action/opinion pair is its unique maximizer against the other players.

The identification with fixed points uses the deterministic revision rule from the motivating model, which chooses defection at exact action indifference. At ties, additional *weak* Nash equilibria may exist and are not classified here. No convergence, attraction basin, or stability property of update trajectories is claimed.

## Proof

**1. Exact best responses.** Fix the other agents' opinions and let \(z_i=\sum_jw_{ij}y_j\). Because \(w_{ii}=0\) and each row sums to one, the unique optimal opinion conditional on chosen action \(x\) is
\[
y_i^*(x)=c z_i+d x,\qquad
c=\frac\beta{\beta+\lambda},\quad
d=\frac\lambda{\beta+\lambda}.
\]
Indeed the quadratic opinion loss is strictly convex before negation, and its stationary point lies in \([0,1]\). Subtracting the optimized payoff for action \(0\) from that for action \(1\) gives
\[
\Delta_i=\alpha(r/n-1)+K(z_i-\tfrac12)
        =K(z_i-\tfrac12-\eta).
\]
The unique best action is therefore \(1\) when \(z_i>1/2+\eta\) and \(0\) when \(z_i<1/2+\eta\); equality is precisely the action tie.

**2. No within-community action heterogeneity.** In any equilibrium, \(y_i=c z_i+d x_i\). For two agents \(i,j\) in the same community, their social-influence rows agree on every other entry except the positions \(i,j\); therefore
\[
z_i-z_j=-\frac{a}{m-1}(y_i-y_j).
\]
Consequently
\[
\left(1+\frac{ca}{m-1}\right)(y_i-y_j)=d(x_i-x_j).
\]
If one of the agents cooperates and the other defects, the cooperator has strictly greater opinion but **weakly lower observed-neighbor mean** \(z\). A strict cooperative best response requires the cooperator's mean to exceed \(1/2+\eta\), whereas a defective best response requires the defector's mean not to exceed it. This contradicts the ordering of their neighbor means, even at \(a=0\). Thus every equilibrium with the stated tie convention has constant actions within each block. The displayed identity then forces constant opinions within each block.

**3. Solve the four block patterns.** With \(x_A,x_B\in\{0,1\}\) and constant opinions \(y_A,y_B\), the equilibrium opinion equations become
\[
y_A=c(ay_A+(1-a)y_B)+d x_A,\qquad
y_B=c(ay_B+(1-a)y_A)+d x_B.
\]
Their coefficient matrix is invertible because \(0<c<1\). Summing yields
\[
y_A+y_B=x_A+x_B.
\]
Subtracting, with \(h=2a-1\), gives
\[
y_A-y_B=\frac{d(x_A-x_B)}{1-ch}.
\]
For \((x_A,x_B)=(0,0)\), this gives \((y_A,y_B)=(0,0)\), and every agent strictly defects because its optimized cooperation advantage is \(-K(1/2+\eta)<0\). For \((1,1)\), opinions equal \(1\), and every agent strictly cooperates precisely when \(1>1/2+\eta\), equivalently \(\eta<1/2\).

For \((x_A,x_B)=(1,0)\), put \(q=d/(1-ch)>0\). The opinions are \(y_A=(1+q)/2\), \(y_B=(1-q)/2\); these both belong to \([0,1]\) since \(d\leq1-ch\) for \(h\leq1\). The neighbor means are
\[
z_A=\tfrac12+\tfrac{hq}{2},
\qquad
z_B=\tfrac12-\tfrac{hq}{2}.
\]
Strict cooperation in \(A\) requires \(hq/2>\eta\); since \(\eta>0\), it forces \(h>0\), in which case defection in \(B\) is automatically strict. Thus this block pattern, and by symmetry its reversal, exists precisely when
\[
\frac{hd}{2(1-ch)}>\eta
\iff
h>\frac{2\eta}{d+2c\eta}
\iff
a>a_{\mathrm c}.
\]
Since \(h\leq1\), this is feasible only if \(\eta<1/2\). At equality, the agents in the cooperating community are indifferent and the declared tie rule selects defection instead. These are the only four block action patterns; Steps 1–2 exclude every other strict equilibrium and fixed point. This proves the claimed exhaustive phase diagram. \(\square\)

## Verification

Run `python3 verify.py` using Python's standard library. The checker constructs each full influence matrix and directly solves its rational stationary opinion equations for *every* binary action profile. It then evaluates the exact optimized payoff advantage, applies strict cooperation/defection-at-tie, and compares the resulting fixed-point set with the closed formula. It covers \(864\) parameter/network cases with \(n\in\{4,6,8\}\), totaling \(96{,}768\) exhaustive action profiles, including exact critical homophily and cooperation thresholds. This is a finite regression check; the preceding proof establishes the statement for all allowed community sizes and real parameters.

An illustrative sharp threshold is \(n=4\), \(r=2\), \(\alpha=1/9\), and \(\beta=\lambda=4/9\). Then \(c=1/2\), \(\eta=1/4\), and \(a_{\mathrm c}=5/6\): at \(a=5/6\) there are two strict equilibria, while at \(a=9/10\) there are four.

## Relationship to prior work

Davidson, Zino, Cao and Ye (2026, arXiv:2604.08840v1, Sections II–IV) defined this joint public-goods/opinion model, derived its optimized best response, gave sufficient conditions for all-defection uniqueness and all-cooperation existence, and explicitly left mixed-action equilibria for later investigation. The payoff and best-response ingredients used in Step 1 are theirs. The present theorem adds an exhaustive, necessary-and-sufficient community-structure classification and a sharp coexistence threshold in a natural block family. The all-defection and all-cooperation parts overlap their established consensus statements and are not independently novel.

Dehghani Aghbolagh et al. (2023, arXiv:2206.07242v2, payoff (7), Section V-A) and Liang et al. (2025, arXiv:2505.03078v1, Sections III–V) study coevolving actions and opinions with **coordination/anti-coordination action payoffs dependent on neighbors' actions** and establish sufficient polarization criteria. In the present public-goods game, the unilateral material payoff increment is the same negative constant independent of others' actions. Their existence conditions do not imply the within-block impossibility lemma, exact equilibrium count, or critical curve here. Classical network coordination-game cohesion criteria are a broader conceptual analogue, not an identical theorem for the coupled public-goods utility.

## Limitations

The phase diagram concerns balanced uniform two-community influence with homogeneous parameters, zero prejudice, no self-weights and strict Nash equilibria/fixed points under a stated tie convention. It does not classify additional weak Nash equilibria at critical surfaces, more general network weights, heterogeneous prejudices, or the dynamics' basins of attraction. This is a mathematical extension of an idealized behavioral model, not an empirical statement. Although the literature comparisons identified no covering result, an equivalent independently derived classification might exist outside the inspected sources.

## References

1. E. C. Davidson, L. Zino, M. Cao and M. Ye, *Modelling the coevolution of opinion dynamics and decision making in social dilemmas*, arXiv:2604.08840v1 (first public version, 2026-04-10). https://arxiv.org/html/2604.08840v1
2. H. Dehghani Aghbolagh, M. Ye, L. Zino, Z. Chen and M. Cao, *Coevolutionary Dynamics of Actions and Opinions in Social Networks*, IEEE Transactions on Automatic Control 68 (2023), arXiv:2206.07242v2. https://arxiv.org/html/2206.07242v2
3. H. Liang, M. Ye, L. Zino and W. Xia, *Coevolution of Actions and Opinions in Networks of Coordinating and Anti-Coordinating Agents*, IFAC Journal of Systems and Control 33 (2025), arXiv:2505.03078v1. https://arxiv.org/html/2505.03078v1
4. F. Parise and A. Ozdaglar, *Analysis and Interventions in Large Network Games*, Annual Review of Control, Robotics, and Autonomous Systems 4 (2021), 455–486, DOI 10.1146/annurev-control-072020-084434. https://doi.org/10.1146/annurev-control-072020-084434
