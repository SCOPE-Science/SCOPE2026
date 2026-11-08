# Sharp pure-privacy frontier for alternating quadratic gradient tracking

## Finding

The alternating local/communication gradient-tracking mechanism of Maithripala, Qiu and Lin (2026), with independent Laplace perturbations on both transmitted primal and tracking states, admits a **necessary and sufficient** infinite-transcript pure differential-privacy criterion on arbitrary positive-curvature scalar quadratic objectives, including heterogeneous local curvatures. It holds for any finite connected undirected network with a symmetric doubly stochastic mixing matrix, independently of its spectrum.

Fix the protected agent \(i\) and abbreviate its own curvature as \(h=h_i>0\). Write \(\alpha>0\) for the common step, \(t=\alpha h_i\), and \(r=q_i^2\in(0,1)\) for its squared per-update noise-decay factor. Set

\[
\lambda_+(t)=\frac{t^2+\sqrt{t^4+4t(1-t)}}2
\quad(0<t<1).
\]

For each changed agent with adjacency bound \(\delta_i>0\), and finite positive primal/tracker Laplace scales \(d_{x,i},d_{y,i}\), the **smallest valid pure privacy parameter** of the complete communication transcript is finite if and only if

\[
\boxed{0<t<1\quad\text{and}\quad r>\lambda_+(t).}
\]

Within this region it is exactly

\[
\boxed{
\varepsilon_i^{\mathrm{sharp}}=
\frac{\delta_i}{r^2-r t^2+t^2-t}
\left(\frac{\alpha r(r+1-t)}{d_{x,i}}+
\frac{r^2(1-t)}{d_{y,i}}\right).
}
\]

If either condition fails, no finite pure privacy parameter is valid for the infinite transcript, despite every individual release having positive Laplace density. Thus each agent has the sharp scalar quadratic privacy-feasibility step threshold \(\alpha h_i<1\), a much larger region than the motivating paper's general sufficient condition \(\alpha L<(\sqrt{17}-3)/4\). The entire network is pure \(\varepsilon\)-private under arbitrary single-agent adjacency exactly when every agent satisfies its own conditions, with smallest network-wide parameter \(\varepsilon=\max_i\varepsilon_i^{\mathrm{sharp}}\). This is a privacy statement, **not** a convergence or optimization-accuracy guarantee.

## Assumptions and scope

Fix an integer \(n\ge2\), one real decision variable per agent, and any symmetric, entrywise nonnegative, connected, doubly stochastic \(n\times n\) mixing matrix \(W\). Agent \(j\) has \(f_j(x)=h_jx^2/2+b_jx+c_j\), with arbitrary individual curvatures \(h_j>0\) and intercepts. In the single-agent comparison below \(h=h_i\) abbreviates the changed agent's curvature; other curvatures need not match it. Initialize \(x_j^0=0\), \(y_j^0=f'_j(0)\). At even steps, perform \(x^{k+1}=x^k-\alpha y^k\) and \(y^{k+1}=y^k+g^{k+1}-g^k\). At odd steps, release \(\widetilde x_j^k=x_j^k+\xi_j^k\), \(\widetilde y_j^k=y_j^k+\nu_j^k\) and update \(x^{k+1}=W\widetilde x^k-\alpha y^k\), \(y^{k+1}=W\widetilde y^k+g^{k+1}-g^k\). Here \(g_j^k=f'_j(x_j^k)\).

All noise coordinates, channels, agents and rounds are independent; \(\xi_j^k\) and \(\nu_j^k\) are centered real Laplace variables of scales \(d_{x,j}q_j^{k-1}\) and \(d_{y,j}q_j^{k-1}\), respectively, with \(d_{x,j},d_{y,j}>0\) and \(0<q_j<1\). Objective adjacency at agent \(i\) means \(f'_i(x)\) can be shifted by a fixed constant \(a\), \(|a|\le\delta_i\), equivalently the objective can be changed by \(a x+b\); all other functions, scales, initial primal states and network parameters remain fixed. The released object is the complete sequence of both message channels from every agent at all odd times. Privacy is the ordinary, unsmoothed, infinite-horizon pure \(\varepsilon\)-differential-privacy inequality over every measurable transcript event. The statement assumes exact real arithmetic and no clipping or post-processing of messages.

## Proof

**1. Exact conditional sensitivity.** Condition the two adjacent problems on precisely the same previous public messages. All unchanged agents then have identical internal states, since their objectives and initial states agree. Only the changed agent contributes to the conditional likelihood ratio. Orient the pair so its gradient offset \(a>0\), and let \(\Delta x^k=x_i^k-x_i^{\prime k}\), \(\Delta y^k=y_i^k-y_i^{\prime k}\). The first local update gives \(\Delta x^1=\alpha a\), \(\Delta y^1=(t-1)a\).

At an odd step \(k\), equality of the released messages yields

\[
\Delta x^{k+1}=-\alpha\Delta y^k,\qquad
\Delta y^{k+1}=h(\Delta x^{k+1}-\Delta x^k).
\]

The following local update consequently gives

\[
\Delta x^{k+2}=t\Delta x^k+\alpha(t-1)\Delta y^k,\qquad
\Delta y^{k+2}=h(t-1)(\Delta x^k+\alpha\Delta y^k).
\]

For \(0<t<1\), at \(k=2m+1\) write \(\Delta x^k=\alpha a X_m\), \(\Delta y^k=-aZ_m\). Then

\[
\binom{X_{m+1}}{Z_{m+1}}=
S(t)\binom{X_m}{Z_m},\qquad
S(t)=\begin{pmatrix}t&1-t\\t(1-t)&-t(1-t)\end{pmatrix},\quad
\binom{X_0}{Z_0}=\binom1{1-t}.
\]

The cone \(X\ge Z\ge0\) is invariant: \(Z'=t(1-t)(X-Z)\ge0\) and \(X'-Z'=t^2X+(1-t^2)Z\ge0\). Therefore \(X_m,Z_m\ge0\) for every \(m\), so no absolute-value cancellations are being ignored.

**2. Exact privacy loss, including necessity.** For any real Laplace release of scale \(s>0\), whose conditional means differ by \(d\), the supremum log-density ratio is exactly \(|d|/s\). One realizes the supremum on a whole open tail beyond both means. Because the mean differences above do not depend on the previously fixed public messages, one can choose these tails successively to attain all such suprema simultaneously for every *finite* transcript prefix. The minimal valid privacy parameter through the first \(M\) communication rounds is consequently exactly

\[
\varepsilon_{i,M}=\delta_i\sum_{m=0}^{M-1}r^{-m}
\left(\frac{\alpha X_m}{d_{x,i}}+\frac{Z_m}{d_{y,i}}\right).
\]

The sign-reversed adjacent pair has the same absolute shifts, and \(|a|=\delta_i\) attains the worst adjacency. The complete infinite transcript is private with finite parameter exactly when this nonnegative series converges; the uniform finite-prefix bound extends to the sigma-algebra generated by the countable transcript. Conversely, if the series diverges, some finite prefix violates any proposed finite privacy parameter.

**3. Sharp spectral boundary and summation.** The characteristic polynomial of \(S(t)\) is \(\lambda^2-t^2\lambda-t(1-t)\). Its roots satisfy \(\lambda_-<0<\lambda_+<1\) and \(|\lambda_-|<\lambda_+\) for \(0<t<1\). The first component has a strictly positive \(\lambda_+\)-coefficient because \(X_0=1\), \(X_1=1-t+t^2>0\) and \(\lambda_-<0\). Hence the privacy series converges if and only if \(r>\lambda_+\). When it converges, the two component sums solve

\[
\binom{\sum_{m\ge0}r^{-m}X_m}{\sum_{m\ge0}r^{-m}Z_m}
=(I-S(t)/r)^{-1}\binom1{1-t}
=\frac1{r^2-r t^2+t^2-t}
\binom{r(r+1-t)}{r^2(1-t)}.
\]

Substitution proves the displayed sharp privacy parameter. For \(t=1\), the conditional primal shift remains exactly \(\alpha a\) at every communication round, giving infinite loss as the noise scale decays. For \(t>1\), the initial primal and tracker shifts are positive and their two-step update matrix has nonnegative entries and primal diagonal multiplier \(t>1\); the primal shift grows at least geometrically, again giving infinite loss. This proves the full necessity and sufficiency result.

## Verification

The standalone `verify.py` runs exact-rational grid checks of the cone recurrence and generating functions; it independently constructs two three-agent executions conditioned on the same public messages, and attains the finite-prefix Laplace likelihood-ratio supremum in a two-agent example. It also verifies the following exact certificate:

\[
 h=1,\ \alpha=\tfrac12,\ r=\tfrac45,\ d_{x,i}=d_{y,i}=\delta_i=1
\quad\Longrightarrow\quad
\sum r^{-m}X_m=\tfrac{104}{19},\quad
\sum r^{-m}Z_m=\tfrac{32}{19},\quad
\varepsilon_i^{\mathrm{sharp}}=\tfrac{84}{19}.
\]

At this parameter the general comparison matrix in the motivating paper has spectral radius greater than one and cannot certify the privacy guarantee, whereas the exact quadratic criterion does. The checker is supplementary: the proof of the infinite-horizon statement is analytic and does not infer convergence from a finite simulation.

## Relationship to prior work

Maithripala, Qiu and Lin introduce precisely the alternating noisy algorithm, the affine adjacency model and a general sufficient privacy criterion based on the nonnegative matrix \(B(\alpha)\); their sufficient threshold is \(\alpha L<(\sqrt{17}-3)/4\). The present result retains their actual message release model but replaces a general worst-case sensitivity upper bound by an exact, signed, conditional sensitivity recurrence for an arbitrary-curvature scalar quadratic network class. It classifies all noise-decay parameters, proves exact optimality of the resulting pure privacy budget, and identifies a provably feasible region omitted by that sufficient certificate. Standard sequential Laplace composition supplies the density mechanism but neither the exact two-step recurrence nor its sharp phase boundary.

Earlier differential-private distributed optimization studies by Ding et al. and Xuan–Wang discuss noisy state/direction or gradient tracking schemes, respectively. They do not, in the material inspected, establish this exact scalar-quadratic criterion for the particular alternating full-transcript mechanism. Access to the complete earlier IEEE text was unavailable, so exact historical priority beyond accessible literature remains open to independent examination.

## Limitations

This result permits heterogeneous scalar quadratic curvatures, but requires scalar objectives, a fixed common step and geometric noise-decay schedules. Nonquadratic curvatures, vector objectives, correlated noise, altered observation models, non-Laplace perturbations and a changing schedule are not covered. The privacy parameter is exact for the **complete released transcript**, not necessarily the information obtainable by a more restricted observer. The sharp feasibility test and budget apply separately to each agent's local curvature. The theorem does not imply convergence of the optimization iterates for every step in its privacy-feasible region. The mathematical novelty assessment is literature-limited and has not undergone independent external validation.

## References

1. M. Maithripala, C. Qiu, Z. Lin, *Communication-Efficient Differentially Private Gradient Tracking for Distributed Optimization via Local Updates*, arXiv:2610.04854v1, first public version October 4, 2026. https://arxiv.org/abs/2610.04854
2. T. Ding, S. Zhu, J. He, C. Chen, X. Guan, *Differentially Private Distributed Optimization via State and Direction Perturbation in Multiagent Systems*, IEEE Transactions on Automatic Control 67 (2022), 722–737. https://doi.org/10.1109/TAC.2021.3059427
3. Y. Xuan, Y. Wang, *Gradient-tracking Based Differentially Private Distributed Optimization with Enhanced Optimization Accuracy*, arXiv:2212.05364, 2022. https://arxiv.org/abs/2212.05364
