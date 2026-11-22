# A sharp cross-majority criterion for persistent strategic opinion switching

## Finding

**Theorem (exact complementary-switching criterion).** Consider the finite synchronous strategic-CODA opinion update [1] with a nonnegative row-stochastic influence matrix \(W\) having zero diagonal and a nonzero entry in every column, individual inertias \(0<\alpha_i<1\), strictly positive persuasion drives, independent uniform priors on \([-1,1]\), and the stationary two-bin Bayesian communication equilibrium at every agent. Fix any sign vector \(s\in\{-1,1\}^n\) with both signs present and define the fraction of agent \(i\)'s influence received from the opposing sign camp by
\[
c_i(s)=\sum_{j:s_j\ne s_i}w_{ij}.
\]

There exists a **strict complementary public-sign period-two orbit** with alternating public profiles \(s/2\) and \(-s/2\) **if and only if**
\[
\boxed{c_i(s)>\frac12\quad\text{for every }i.}
\]
It is the only period-two orbit with those two prescribed alternating public profiles and is given exactly by
\[
\boxed{x_i^{+}=\frac{1-\alpha_i}{2(1+\alpha_i)}(2c_i(s)-1)s_i,
\qquad x_i^{-}=-x_i^{+}.}
\]
The orbit is genuinely period two, lies strictly inside the opinion cube, and attracts full-dimensional open neighborhoods of both its states geometrically. The criterion is sharp at equality: if any \(c_i(s)\le1/2\), no such *strict complementary-sign* orbit exists. This is not a claim about all possible recurrent trajectories.

In particular, let four agents form two pairs and let
\[
W=\begin{pmatrix}
0&1/4&3/8&3/8\\
1/4&0&3/8&3/8\\
3/8&3/8&0&1/4\\
3/8&3/8&1/4&0
\end{pmatrix},\qquad s=(1,1,-1,-1)^{\mathsf T}.
\]
All off-diagonal influences are positive, so the directed network is strongly connected and primitive. For **every** common inertia \(0<\alpha<1\), the two attracting, alternating opinion states are
\[
\boxed{x^{\pm}=\pm\frac{1-\alpha}{4(1+\alpha)}(1,1,-1,-1)^{\mathsf T}.}
\]
Their amplitude tends to zero but remains nonzero as \(\alpha\uparrow1\). Thus no fixed inertia threshold can force public-signal convergence from every initial condition on this fixed primitive network with this fixed two-bin code. This directly contradicts the unrestricted high-inertia convergence conjecture in [1, Section 7.2], while remaining consistent with its proven convergence results under monotone trajectories.

## Assumptions and scope

The model is deterministic, finite, synchronous and discrete-time. Let \(n\ge2\), \(W=(w_{ij})\in[0,1]^{n\times n}\) have row sums one, \(w_{ii}=0\), and strictly positive column sums (each sender has an audience). Each agent's inertia is \(\alpha_i\in(0,1)\); every persuasion drive \(\beta_i>0\). Agents initially have independent uniform priors on \([-1,1]\), as in [1]. They choose the **two-bin** credible signaling equilibrium and reuse that communication convention at every step (the stationary-protocol assumption of [1]). The equilibrium bin count is selected, not deduced to be uniquely socially selected.

Writing \(D=\operatorname{diag}(\alpha_1,\ldots,\alpha_n)\), the repeated update is
\[
F(x)=Dx+(I-D)Wq(x).
\]
The audience leverage factors in [1, Eq. (7)] are
\[
\xi_j=\frac{\sum_i (1-\alpha_i)w_{ij}}
{\sum_i(1-\alpha_i)^2w_{ij}^2}>1.
\]
Indeed, every positive effective audience weight is strictly between zero and one, and at least one exists in each column. Under the uniform prior, [1, Theorem 4] gives the unique two-bin equilibrium thresholds \(-1,0,1\) and reconstruction levels \(-1/2,+1/2\), regardless of the numerical value of \(\xi_j>1\). Consequently
\[
q_j(z)=\begin{cases}1/2,&z>0,\\-1/2,&z<0,\end{cases}
\]
with an arbitrary deterministic choice of adjacent reconstruction level at \(z=0\). Every orbit constructed here avoids all thresholds, so tie-breaking is immaterial.

For a prescribed \(s\in\{-1,1\}^n\), *strict complementary public-sign switching* means a pair of distinct states \(x^+,x^-\) satisfying \(F(x^+)=x^-\), \(F(x^-)=x^+\), \(q(x^+)=s/2\), \(q(x^-)=-s/2\), with no zero coordinate. The condition is on *the two specified public profiles*, not every possible two-cycle of the discontinuous map.

## Proof

**1. Reduction of a two-cycle to one linear identity.** Let \(b=(I-D)Ws/2\). If the public profiles alternate as prescribed, the two transition equations necessarily are
\[
x^-=Dx^++b,\qquad x^+=Dx^--b.
\]
Eliminating \(x^-\) gives
\[
(I-D^2)x^+=(D-I)b=-(I-D)b.
\]
Since every \(\alpha_i<1\), both \(I-D\) and \(I+D\) are invertible. Therefore the *only possible* corresponding pair is
\[
x^+=-(I+D)^{-1}b,
\qquad x^-=(I+D)^{-1}b=-x^+.
\]
This is an exact solution of the branch equations, not a numerical candidate.

**2. Exact sign-consistency test.** Because the rows of \(W\) sum to one,
\[
(Ws)_i=s_i\left(\sum_{j:s_j=s_i}w_{ij}-\sum_{j:s_j\ne s_i}w_{ij}\right)
=s_i(1-2c_i(s)).
\]
Substitution yields
\[
x_i^+=\frac{1-\alpha_i}{2(1+\alpha_i)}(2c_i(s)-1)s_i.
\]
The positive prefactor shows that \(s_ix_i^+>0\) for all \(i\) **if and only if** every cross-camp influence exceeds one-half. When this holds, the pair solves the branch equations and belongs strictly to the required quantizer cells. Conversely, if some cross-weight is at most one-half, the unique branch solution has a zero or wrong-sign coordinate, contradicting strict membership in the prescribed cells. This proves existence, uniqueness relative to the alternating public profiles, and sharp necessity. Since the coordinates of \(x^+\) are nonzero and \(x^-=-x^+\), the orbit has prime period exactly two.

**3. An explicit open basin and rate.** Assume all \(c_i(s)>1/2\), set \(u_* = \min_i |x_i^+|>0\) and \(\rho=\max_i\alpha_i<1\). For any \(0<\delta<u_*\), the \(\ell^\infty\) ball of radius \(\delta\) around \(x^+\) lies in the same quantizer cell as \(x^+\); on this ball
\[
F(x)-x^-=D(x-x^+),\qquad
\|F(x)-x^-\|_\infty\le\rho\|x-x^+\|_\infty.
\]
The image lies in the \(\delta\) ball around \(x^-\), where the quantizer is likewise constant. Repeating yields, for every \(t\ge0\),
\[
\|F^t(x)-x^{(-1)^t}\|_\infty\le\rho^t\|x-x^+\|_\infty,
\]
where \(x^{(-1)^t}\) denotes \(x^+\) at even steps and \(x^-\) at odd steps. The analogous statement holds near \(x^-\). These open balls establish local attraction in the **full \(n\)-dimensional state space**, not merely within the sign-symmetric subspace. The strict inequality on each \(c_i\) is open under admissible small changes of \(W\) and \(\alpha\), so the attracting orbit persists under those changes.

**4. Primitive-network witness at every inertia.** In the displayed four-vertex matrix, the two cross-community weights sum to \(3/4\) at every vertex. Hence \(2c_i-1=1/2\), and the formula gives amplitude \(u(\alpha)=(1-\alpha)/(4(1+\alpha))>0\). Every off-diagonal entry is positive; in particular every entry of \(W^2\) is positive, proving primitivity. The common audience exaggeration factor is \(\xi=32/[11(1-\alpha)]>1\), so the two-bin credible code is valid for every \(0<\alpha<1\). At \(\alpha=99/100\) the orbit states are exactly \(\pm(1,1,-1,-1)/796\). As \(\alpha\uparrow1\), \(u(\alpha)\sim(1-\alpha)/8\): the switching basin shrinks, but never vanishes for any allowed inertia. Thus arbitrarily strong inertia does **not** guarantee eventual public-signal stabilization from all initial states.

## Verification

Execute `python3 check.py` using Python 3 and its standard library. The exact-rational script verifies the four-node witness and its primitive stochastic matrix, the audience factors, the two transitions, the local contraction neighborhood, and the cross-majority criterion for 1,579 finite cases including heterogeneous inertias, asymmetric matrices and near-unit inertia. It prints `VERIFY_OK` upon success. The all-parameter result follows from the displayed linear identities and strict sign test; the finite checker is not an exhaustive infinite proof.

## Relationship to prior work

Munif et al. [1] derive the endogenous network-dependent credible quantizer, prove that two-bin codes exist under their assumptions, and show a numerical period-two trajectory at relatively low inertia. Their Section 7.2 then conjectures that sufficiently high inertia guarantees settling of public signals from every initial state for each fixed topology and quantizer profile. The present theorem resolves that specific conjecture **negatively**: the fixed primitive four-node topology supports a strict, locally attracting cycle for every inertia below one. Their proved monotone-trajectory convergence proposition is not contradicted, because the constructed cycle is not monotone componentwise.

Chowdhury, Morărescu, Martin and Srikant [2] previously exhibit oscillations in a CODA model with **state-dependent** update coefficients \(p_i(1-p_i)\), rather than [1]'s constant individual inertia and game-derived posterior means. Their oscillatory examples do not supply the present necessary-and-sufficient cross-majority criterion, the arbitrarily-high-inertia conclusion in [1]'s specific model, or the refutation of its stated conjecture. Ceragioli and Frasca [3] analyze a **continuous-time** quantized-opinion system with generalized differential-equation solution notions; their results do not imply a discrete-time prime-two orbit here.

A separately published four-person **opinion–action public-goods best-response** construction [4] has an attracting two-cycle on a primitive network, but with different payoffs and a different branch map; that fact does not imply the present uniform-prior Bayesian-communication theorem. Likewise, a published node–group mean-field two-cycle classification [5] studies different nonlinear aggregate variables. **The generic possibility of oscillations in quantized opinions is not claimed as new.** The contribution here is the exact sharp cut criterion and a direct all-inertia contradiction of [1]'s open convergence prediction.

## Limitations

The analysis covers synchronous discrete-time dynamics with *fixed* stationary two-bin Bayesian signaling, independent uniform priors at protocol formation, strictly positive inertias below one, and a network meeting [1]'s audience assumptions. It classifies only cycles with **complementary** public-sign profiles; other cycles may exist without such a cut, and the theorem makes no general convergence assertion outside the strict cut condition. The construction gives positive-size attraction neighborhoods for each fixed inertia, not a lower bound on their size as inertia approaches one; indeed their radii shrink to zero in the displayed family. It does not address asynchronous updating, strategic readjustment of beliefs or quantizers during evolution, stochastic noise, or empirical social networks. The claim is literature-bounded; an unindexed equivalent statement may exist, and independent mathematical review has not been performed.

## References

1. H. Munif, A. Couthures, V. S. Varma, S. Lasaulce, and T. Başar, *Network-Induced Strategic Communication in Opinion Dynamics*, arXiv:2607.16036, first public 2026-07-17, especially Theorem 4, Equations (4) and (7), Section 6 and Section 7.2. https://arxiv.org/abs/2607.16036
2. N. R. Chowdhury, I.-C. Morărescu, S. Martin, and S. Srikant, *Continuous opinions and discrete actions in social networks: a multi-agent system approach*, arXiv:1602.02098, first public 2016-02-05, Equations (1)–(3) and Sections IV–VI. https://arxiv.org/abs/1602.02098
3. F. Ceragioli and P. Frasca, *Consensus and Disagreement: The Role of Quantized Behaviors in Opinion Dynamics*, SIAM Journal on Control and Optimization 56 (2018), 1058–1080, DOI:10.1137/16M1083402. https://doi.org/10.1137/16M1083402
4. *Stable period-two switching on a complete network in an opinion–action public-goods game*, public result and proof, 2026-10-12. https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-stable-period-two-switching-on-a-complete-network-in-an-opinion--173bd96ccffc
5. *A sign-selective two-cycle obstruction for coupled node–group opinions*, public result and proof, 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-sign-selective-two-cycle-obstruction-for-coupled-node-group-op--40c6dc082b82
