# A five-agent asymmetric community game with exactly three strict Nash equilibria

## Finding

In the coevolutionary public-goods/opinion game of Davidson, Zino, Cao and Ye, unequal community sizes can select **one** polarized cooperation pattern without selecting its mirror. The exact strict-Nash phase diagram for all two-community complete weighted networks with common within-community and cross-community per-edge influence strengths is given below. In particular, a five-person instance has precisely three strict Nash equilibria: universal defection, universal cooperation, and cooperation only in the larger community. Five agents are the smallest possible size for such one-sided polarization within this network family. This differs qualitatively from the balanced-community phase diagram, in which polarized equilibria appear only as a symmetric pair.

Let communities \(A,B\) contain \(a,b\ge1\) agents, with \(n=a+b\ge2\). Every distinct within-community pair has raw opinion weight \(w>0\), and every cross-community pair has raw weight \(v>0\); each agent's row is normalized to sum to one, with no self-weight. Let
\[
q=\frac{\beta}{\beta+\lambda}\in(0,1),\qquad
\theta=\frac12+\frac{\alpha(1-r/n)(\beta+\lambda)}{\beta\lambda}>\frac12,
\]
where \(1<r<n\), \(\alpha,\beta,\lambda>0\) and \(\alpha+\beta+\lambda=1\). Define the within-community influence fractions and a positive denominator by
\[
p_A=\frac{(a-1)w}{(a-1)w+bv},\quad
p_B=\frac{(b-1)w}{(b-1)w+av},\quad
\Delta=1-q(p_A+p_B-1)>0.
\]
Set
\[
\begin{aligned}
L_A&=\frac{1-p_B}{\Delta},&U_A&=\frac{q(1-p_B)+(1-q)p_A}{\Delta},\\
L_B&=\frac{1-p_A}{\Delta},&U_B&=\frac{q(1-p_A)+(1-q)p_B}{\Delta}.
\end{aligned}
\]
If \(\theta\notin\{1,L_A,U_A,L_B,U_B\}\), every Nash equilibrium is strict, and the complete number of Nash equilibria is
\[
\boxed{N=1+\mathbf1_{\{\theta<1\}}+
\mathbf1_{\{L_A<\theta<U_A\}}+
\mathbf1_{\{L_B<\theta<U_B\}}.}
\]
The two indicator terms correspond respectively to cooperation in \(A\) alone and cooperation in \(B\) alone. These intervals are empty if \(p_A+p_B\le1\). If \(p_A+p_B>1\), each interval has width \((1-q)(p_A+p_B-1)/\Delta\), while the first interval lies \((p_A-p_B)/\Delta\) to the right of the second. Asymmetric influence therefore separates two polarization thresholds that coincide in balanced communities.

A sharp five-agent witness is
\[
a=3,\quad b=2,\quad w=4,\quad v=1,\quad
r=2,\quad \alpha=\frac5{101},\quad
\beta=\lambda=\frac{48}{101}.
\]
It has \(q=1/2\), \(\theta=5/8\), \(p_A=4/5\), \(p_B=4/7\), and
\[
(L_A,U_A)=\left(\frac{10}{19},\frac{43}{57}\right),\qquad
(L_B,U_B)=\left(\frac{14}{57},\frac9{19}\right).
\]
Only the first interval contains \(5/8\). The three action profiles are \((0,0,0,0,0)\), \((1,1,1,1,1)\), and \((1,1,1,0,0)\). Their equilibrium opinions are respectively the all-zero, all-one, and
\[
\left(\frac{50}{57},\frac{50}{57},\frac{50}{57},\frac5{19},\frac5{19}\right)
\]
vectors. In the polarized configuration, the observed neighbor-opinion averages are \(43/57>5/8\) for cooperators and \(10/19<5/8\) for defectors. Thus all action choices are strict best responses.

## Assumptions and scope

Each agent chooses a binary public-goods contribution \(x_i\in\{0,1\}\) and a real opinion \(y_i\in[0,1]\). The joint payoff, with \(\alpha,\beta,\lambda,r,n\) as above and row-stochastic zero-diagonal \(W\), is
\[
\pi_i=\alpha\left(\frac rn\sum_jx_j-x_i\right)
-\frac\beta2\sum_jW_{ij}(y_i-y_j)^2
-\frac\lambda2(x_i-y_i)^2.
\]
This is the zero-prejudice version of the published model. A Nash deviation may change both an agent's action and its opinion. The classification is for static pure Nash equilibria; opinions are uniquely optimized conditional on binary actions. The genericity exclusion on \(\theta\) prevents action indifference in any of the four possible group-level profiles. At excluded parameter equalities, weak equilibria require separate treatment. No dynamical convergence or basin-of-attraction assertion is made.

## Proof

**1. Best responses.** With \(z_i=\sum_jW_{ij}y_j\), and keeping all others fixed, the unique optimized opinion for an action \(x_i\) is \(y_i=qz_i+(1-q)x_i\). Maximizing over the opinion, the payoff advantage for cooperation rather than defection equals
\[
\alpha(r/n-1)+\frac{\beta\lambda}{\beta+\lambda}\left(z_i-\frac12\right)
=\frac{\beta\lambda}{\beta+\lambda}(z_i-\theta).
\]
Thus the unique optimal action is one precisely when \(z_i>\theta\); the unique optimal action is zero precisely when \(z_i<\theta\). The optimized opinion is in \([0,1]\), since it is a convex combination.

**2. Each community has one action.** Let \(d_A=(a-1)w+bv\). For two distinct individuals \(i,j\) in community \(A\), their normalized influence rows agree on every other index and differ only at the two focal indices, giving
\[
z_i-z_j=-\frac{w}{d_A}(y_i-y_j),\qquad
\left(1+\frac{qw}{d_A}\right)(y_i-y_j)=(1-q)(x_i-x_j).
\]
If \(x_i=1\), \(x_j=0\), then \(y_i>y_j\) but \(z_i<z_j\). A cooperator requires \(z_i\ge\theta\), and a defector requires \(z_j\le\theta\), impossible. The argument is identical in community \(B\). Consequently every Nash equilibrium has uniform actions within each community, even at action ties. The same displayed identity implies within-group opinions are uniform. This holds for singleton communities trivially.

**3. Resolve all four patterns.** For constant block actions \(x_A,x_B\), the two opinion equations reduce to
\[
y_A=q[p_Ay_A+(1-p_A)y_B]+(1-q)x_A,\qquad
y_B=q[(1-p_B)y_A+p_By_B]+(1-q)x_B.
\]
The coefficient matrix is invertible since its social-interaction term is stochastic and \(0<q<1\). If both actions are zero, the only opinions are zero and both actions are strictly optimal since \(\theta>1/2\). If both actions are one, the only opinions are one and both are strictly optimal iff \(\theta<1\). In the pattern \((x_A,x_B)=(1,0)\), subtracting the equations gives
\[
y_A-y_B=\frac{1-q}{\Delta}>0,\quad
y_A=\frac{1-qp_B}{\Delta},\quad
y_B=\frac{q(1-p_B)}{\Delta}.
\]
The observed means are \(z_A=U_A\) and \(z_B=L_A\). The pattern is a strict equilibrium iff \(L_A<\theta<U_A\). Reversing roles gives the condition \(L_B<\theta<U_B\). There are no other patterns by Step 2, proving the exact count and uniqueness of opinions for each equilibrium. The interval width and displacement follow by subtraction, without approximation.

**4. Sharp minimum for one-sided polarization.** If either community is a singleton, one of \(p_A,p_B\) is zero and the other is strictly below one; thus \(p_A+p_B<1\), so neither polarized pattern can be an equilibrium. If both communities have at least two agents and \(n<5\), necessarily \(a=b=2\), yielding \(p_A=p_B\) for common per-pair \(w,v\). Their two intervals coincide; hence exactly one polarized equilibrium is impossible. The five-agent witness above satisfies all inequalities strictly, proving the minimum. \(\square\)

## Verification

Run `python3 verify.py` using only the Python standard library. The checker constructs the complete rational influence matrix, solves the exact stationary opinion equations for every binary action profile, tests the optimized Nash advantage, and compares the result to the displayed four-pattern formula. It tests 2,160 parameter combinations of community sizes \(1\) through \(4\), influence weights, feedback strengths, and payoff thresholds, covering 92,736 exhaustive action profiles. The five-person example is checked with rational arithmetic, including exact equilibrium opinions and neighbor averages. This is a finite regression check; the proof establishes the all-size real-parameter theorem.

## Relationship to prior work

Davidson, Zino, Cao and Ye (2026) introduce the coupled public-goods/opinion payoff, derive its action and opinion best responses, and establish consensus-equilibrium conditions. They identify mixed-action equilibria as an open direction; neither the unequal-group exact census nor the three-equilibrium witness occurs in their analyzed results.

*Sharp segregation threshold in a two-community opinion–public-goods game* gives an exact balanced-community census with one, two or four strict equilibria, and proves a related within-group homogeneity lemma. The present claim is **not** the homogeneity lemma or the balanced case: when the community sizes differ under common per-edge weights, the normalized influence fractions become unequal and a previously absent **third count** appears. That previous balanced statement does not imply existence or minimality of an orientation-selective equilibrium, though its reduction motivates the approach.

Dehghani Aghbolagh et al. (2023) and Liang et al. (2025) study coordinated or anti-coordinated action payoffs, which depend on other agents' actions; their polarized-state conditions concern different payoff terms. Here the public-goods action increment is independent of neighbors' contributions. Consequently their convergence and polarization criteria do not supply this exact three-equilibrium classification. The full published references and related literature were compared, without asserting an exhaustive priority proof.

## Limitations

The results concern homogeneous behavioral parameters, two complete weighted communities, zero self-influence, zero prejudice, positive common within- and cross-community raw weights, and static Nash behavior. No claim is made at nongeneric payoff ties, for more arbitrary network patterns, or concerning stochastic trajectories. This idealized strategic prediction has not been validated empirically. Independent assessment of historical novelty remains outstanding.

## References

1. E. C. Davidson, L. Zino, M. Cao and M. Ye, *Modelling the coevolution of opinion dynamics and decision making in social dilemmas*, arXiv:2604.08840v1, first submitted 2026-04-10. https://arxiv.org/abs/2604.08840
2. *Sharp segregation threshold in a two-community opinion–public-goods game*, publicly indexed mathematical note (2026).
3. H. Dehghani Aghbolagh, M. Ye, L. Zino, Z. Chen and M. Cao, *Coevolutionary Dynamics of Actions and Opinions in Social Networks*, IEEE Transactions on Automatic Control 68 (2023), arXiv:2206.07242. https://arxiv.org/abs/2206.07242
4. H. Liang, M. Ye, L. Zino and W. Xia, *Coevolution of Actions and Opinions in Networks of Coordinating and Anti-Coordinating Agents*, IFAC Journal of Systems and Control 33 (2025), arXiv:2505.03078. https://arxiv.org/abs/2505.03078
