# Sharp cross-community switching threshold for an attracting public-goods/opinion two-cycle

## Finding

For every even population size \(n=2m\) with \(m\ge2\), consider the simultaneous best-response public-goods/opinion game specified below. If the opinion-influence network has two equal communities, with total influence weight \(p\) assigned to an agent's own community and \(1-p\) to the opposite community, there is a **sharp, explicitly computable threshold** for a period-two orbit that alternates the two communities' cooperation decisions. The periodic orbit exists, is unique in this alternating-community class, and is locally exponentially attracting exactly when \(0\le p<p_*\), where

\[
 p_* = \frac{(1-c)(1-q)}{2(1-c+cq)},\qquad
 c=\frac{\beta}{\beta+\lambda},\qquad
 q=\frac{2\alpha(1-r/n)(\beta+\lambda)}{\beta\lambda}.
\]

The assumptions include \(0<q<1\), so the all-defection and all-cooperation consensus equilibria are also locally attracting. Consequently, for every \(0<p<p_*\), **two consensus attractors coexist with a third attractor that is a genuine two-cycle**, even though the undirected network is connected and every pair of distinct agents has a positive influence weight. This cycle and the two consensus attractors persist under sufficiently small admissible perturbations of network weights and game coefficients. No community-alternating two-cycle with the stated action pattern exists at or above \(p_*\). The exclusion applies to this patterned class, not to all possible periodic trajectories.

## Assumptions and scope

Fix \(n=2m\ge4\), \(1<r<n\), and \(\alpha,\beta,\lambda>0\) with \(\alpha+\beta+\lambda=1\). Players have actions \(x_i\in\{0,1\}\), opinions \(y_i\in[0,1]\), zero prejudice, and common payoffs

\[
 \pi_i=\alpha\left[\frac rn\sum_{j=1}^{n}x_j-x_i\right]
 -\frac\beta2\sum_{j=1}^{n}w_{ij}(y_i-y_j)^2
 -\frac\lambda2(x_i-y_i)^2.
\]

This is the social-dilemma payoff and joint best-response rule of Davidson, Zino, Cao and Ye [1]. All agents update simultaneously at integer times, taking the defection action at an exact action tie. The influence matrix \(W=(w_{ij})\) is symmetric, nonnegative, row-stochastic, with \(w_{ii}=0\), and has two labeled blocks \(A,B\) of size \(m\):

\[
 w_{ij}=\begin{cases}
 p/(m-1),& i\ne j\text{ in the same block},\\
 (1-p)/m,&i,j\text{ in different blocks},\\
 0,&i=j.
 \end{cases}
\]

Initially allow \(0\le p<1\); the case \(0<p<p_*\) has strictly positive weights on **every** off-diagonal pair and so is a connected complete weighted graph. Set \(c=\beta/(\beta+\lambda)\), \(d=1-c=\lambda/(\beta+\lambda)\), \(k=\beta\lambda/(\beta+\lambda)\), \(h=\alpha(1-r/n)\), \(q=2h/k\), and assume \(0<q<1\). The tie threshold is \(\theta=(1+q)/2\in(1/2,1)\).

Let \(\mathbf{0}_m,\mathbf{1}_m\) denote constant length-\(m\) blocks. A *community-alternating two-cycle* is a prime period-two state with actions alternating exactly between \((\mathbf{0}_m,\mathbf{1}_m)\) and \((\mathbf{1}_m,\mathbf{0}_m)\), allowing arbitrary opinions in its definition. This definition neither presupposes constant opinions within blocks nor rules out other kinds of cycle elsewhere in the state space.

## Proof

**1. Exact best response.** Write \(z_i=(Wy)_i\). For fixed action \(a\in\{0,1\}\), the opinion maximizing the player's payoff is \((\beta z_i+\lambda a)/(\beta+\lambda)\). The optimized payoff advantage of cooperation over defection, after cancelling action-independent terms, is

\[
 \Delta_i=-h+k\left(z_i-\frac12\right).
\]

Since \(k>0\), the action \(s_i(y)=1\) precisely when \(z_i>\theta\). The simultaneous map is therefore

\[
 x_i(t+1)=s_i(y(t)),\qquad
 y(t+1)=cWy(t)+d\,s(y(t)). \tag{1}
\]

The map preserves \([0,1]^n\) because \(W\) is row-stochastic and \(c+d=1\).

**2. Unique candidates for alternating actions.** Prescribe alternating action blocks \(x^{(0)}=(\mathbf{0}_m,\mathbf{1}_m)\), \(x^{(1)}=(\mathbf{1}_m,\mathbf{0}_m)\). Any corresponding opinions must satisfy

\[
 y^{(1)}=cWy^{(0)}+dx^{(1)},\qquad
 y^{(0)}=cWy^{(1)}+dx^{(0)}. \tag{2}
\]

Substitution gives a two-step affine map with linear part \(c^2W^2\), whose infinity-norm is at most \(c^2<1\). Thus (2) has a unique solution. The network and prescribed actions are invariant under permutations within either block, and the equations are invariant under simultaneously swapping the blocks and shifting one time step; uniqueness forces both blockwise constancy and a swapped phase. Hence for some \(0\le L<H\le1\),

\[
 y^{(0)}=(L\mathbf{1}_m,H\mathbf{1}_m),\qquad
 y^{(1)}=(H\mathbf{1}_m,L\mathbf{1}_m).
\]

Adding the two scalar equations gives \(L+H=1\). Subtracting yields

\[
 D:=H-L=\frac{d}{d+2cp},\qquad L=\frac{1-D}{2},\quad H=\frac{1+D}{2}. \tag{3}
\]

**3. The sharp existence cutoff.** At phase zero, the block currently at opinion \(L\) receives neighbor mean

\[
 M_H=pL+(1-p)H=\frac{1+(1-2p)D}{2},
\]

and the other block receives \(M_L=[1-(1-2p)D]/2\). For the next action to be \((\mathbf{1}_m,\mathbf{0}_m)\), it is necessary and sufficient that \(M_H>\theta\) and \(M_L\le\theta\). Because \(\theta>1/2\), the first strict inequality implies \(p<1/2\) and makes the second inequality automatic. By (3), the first inequality is equivalent to

\[
 (1-2p)\frac{d}{d+2cp}>q
 \quad\Longleftrightarrow\quad
 p<\frac{d(1-q)}{2(d+cq)}=p_*. \tag{4}
\]

The other phase is symmetric. When (4) holds, (2) is indeed an exact cycle of (1), with distinct action phases. When (4) fails, the unique affine candidate violates the cooperative strict-threshold rule; equality is excluded because ties select defection. Thus the stated *patterned-cycle* existence boundary is necessary and sufficient, including the boundary case.

**4. Stability, coexistence and robustness.** Under (4), both threshold comparisons are strict. In an open neighborhood of each phase, the same action block is therefore selected. On the corresponding two-step chamber, opinion perturbations obey exactly

\[
 e(t+2)=c^2W^2e(t),\qquad
 \|e(t+2)\|_\infty\le c^2\|e(t)\|_\infty.
\]

Choosing the neighborhood sufficiently small to keep the inequalities strict proves local exponential attraction in the full action–opinion state space; the next action is determined solely by the current opinions. Meanwhile, \((x,y)=(\mathbf{0}_n,\mathbf{0}_n)\) is a strict fixed point since \(0<\theta\), and \((\mathbf{1}_n,\mathbf{1}_n)\) is a strict fixed point since \(\theta<1\). The same \(cW\) contraction proves that both consensus equilibria attract open neighborhoods.

Finally, the uniquely forced period-two opinions in (2) are obtained by the inverse of \(I-c^2W^2\), which exists in a neighborhood of the given parameters since \(c<1\). Strict inequalities and exponential contraction survive sufficiently small admissible changes in \(W\) and the game coefficients (including small player-specific changes). Therefore the three attracting invariant sets are robust, not artifacts of equality constraints within the network.

**5. Rational four-player witness.** Take

\[
 n=4,\quad r=3,\quad \alpha=\frac1{10},\quad
 \beta=\lambda=\frac9{20},\quad p=\frac14.
\]

Then \(c=d=1/2\), \(q=2/9\), \(\theta=11/18\), and \(p_*=7/22>1/4\). Let the within-pair edge weight be \(1/4\) and each cross-pair edge weight \(3/8\). The orbit is

\[
 \begin{aligned}
 (x^{(0)},y^{(0)})&=\left((0,0,1,1),(\tfrac16,\tfrac16,\tfrac56,\tfrac56)\right),\\
 (x^{(1)},y^{(1)})&=\left((1,1,0,0),(\tfrac56,\tfrac56,\tfrac16,\tfrac16)\right).
 \end{aligned}
\]

The phase-zero neighbor means are exactly \((2/3,2/3,1/3,1/3)\), straddling \(11/18\) with minimum strict margin \(1/18\). The two-step opinion-Jacobian eigenvalues are \(1/4,1/16,1/64,1/64\). Both consensus fixed points also attract open neighborhoods.

## Verification

The accompanying standalone `CHECK.py` uses symbolic optimization to rederive the discriminant, verifies the two-block affine equations and exact cutoff algebra, and reconstructs both phases and two-step eigenvalues of the four-player witness with rational arithmetic. It also checks the cutoff equivalence and affine equations at 360 seeded rational parameter triples. Run `python CHECK.py` with SymPy installed. All checks passed. These computations validate the identities and finite witness; the general infinite family and local stability are established by the proof above, not by sampling.

## Relationship to prior work

Davidson, Zino, Cao and Ye [1] introduce the exact social-dilemma best-response model and analyze consensus and equilibrium existence, with global convergence only under a sufficient global-defection condition. Their model explicitly permits synchronous updating; the strict, attractive two-cycle here lies outside that sufficient condition and is not asserted by their equilibrium theorems. Kuhlman, Mortveit, Murrugarra and Kumar [2] show the possibility and general upper-period restrictions for *Boolean* symmetric threshold networks, but their state is purely binary, without the continuous opinion-memory equation (1), the public-goods parameters or the sharp nonzero-cohesion cutoff (4). Liang, Ye, Zino and Xia [3] treat a different action–opinion game based on coordination or anti-coordination payoffs and study equilibrium convergence; their stated conclusions do not directly give the periodic orbit in the public-goods payoff (1). The exact cutoff, formula (3), three-attractor coexistence and full-state attraction here require the model-specific two-step calculation.

## Limitations

The cutoff is complete **only for the prescribed opposite-community period-two action pattern**. There is no assertion that all trajectories converge to one of the three identified attractors, that longer cycles are impossible for other parameters or update schedules, or that all attractors have been classified. For this model, asynchronous revision can behave differently from simultaneous revision; this theorem concerns synchronous updates alone. No claim is made about stochastic agent behavior, finite sampling error, or real-world epidemic or social outcomes. Prior work on Boolean threshold dynamics shows that period-two behavior is not itself a novel general phenomenon; the contribution is its sharp and robust realization in the coupled game with nontrivial continuous opinions.

## References

[1] E. C. Davidson, L. Zino, M. Cao, M. Ye, *Modelling the coevolution of opinion dynamics and decision making in social dilemmas*, arXiv:2604.08840v1, first public April 10, 2026. https://arxiv.org/html/2604.08840 ; https://arxiv.org/abs/2604.08840

[2] C. J. Kuhlman, H. S. Mortveit, D. Murrugarra, V. S. A. Kumar, *Bifurcations in Boolean Networks*, Discrete Mathematics and Theoretical Computer Science, 2012, pp. 29–46. https://doi.org/10.46298/dmtcs.2975 ; https://dmtcs.episciences.org/2975/pdf

[3] H. Liang, M. Ye, L. Zino, W. Xia, *Coevolution of Actions and Opinions in Networks of Coordinating and Anti-Coordinating Agents*, arXiv:2505.03078v1, May 6, 2025. https://arxiv.org/html/2505.03078
