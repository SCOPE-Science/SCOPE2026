# A four-per-side switch for second-order leader placement after one bipartite link failure

## Finding

Let \(n\ge3\) be an integer. From the unit-weight complete bipartite graph \(K_{n,n}\), remove precisely one edge \(u_*v_*\), with \(u_*\) in the left class \(A\) and \(v_*\) in the right class \(B\). Choose exactly two distinct vertices as perfectly pinned (noise-free) leaders, denoted by \(S\); all others are followers. Write \(L_{FF}(S)\) for the principal submatrix of the **original, ungrounded graph Laplacian** on the followers \(F=V\setminus S\), retaining full degrees in its diagonal. Minimize

\[
J_2(S)=\operatorname{tr}\big(L_{FF}(S)^{-2}\big).
\]

**Complete classification.** For \(n=3\), the unique optimal pair is \(\{u_*,v_*\}\), the two ends of the failed edge. For every \(n\ge4\), the complete collection of optimal pairs consists of any two vertices in \(A\setminus\{u_*\}\), or any two vertices in \(B\setminus\{v_*\}\). Thus there are exactly \(2\binom{n-1}{2}\) optimal pairs for \(n\ge4\). All other pairs are strictly suboptimal, including every mixed-part pair and every pair containing an endpoint of the missing edge. There are no parameter ties.

The exact minimal second-order costs are

\[
J_2^*(3)=\frac{284}{225}, \qquad
J_2^*(n)=\frac{n^6-3n^5-2n^4+23n^3-35n^2+22n-5}{n^2(n-1)^4}\quad(n\ge4).
\]

For the *first-order* objective \(J_1(S)=\operatorname{tr}(L_{FF}(S)^{-1})\) on the same graph, the known fault-aware transition occurs at \(n=6\), rather than \(n=4\). Consequently the first- and second-order objectives select **disjoint classes of optimal leader pairs** for \(n=4,5\). This contrast is a statement about two different noise models, not a corollary of the first-order ordering.

## Assumptions and scope

All graph edges present have conductance exactly one. There are no tunable edge conductances, no extra leader gains, and no additional link failures. The graph is connected for every \(n\ge3\), and any nonempty leader set has a positive-definite grounded principal Laplacian. In particular, \(J_2\) is finite.

A control interpretation is provided by second-order unit-white-noise follower dynamics with matched relative-position and relative-velocity feedback,

\[
\ddot x_F(t)=-L_{FF}x_F(t)-L_{FF}\dot x_F(t)+\dot W_F(t),
\]

with the leaders fixed at the reference position and velocity. For an eigenmode of stiffness \(\lambda>0\), its stationary position variance is \(1/(2\lambda^2)\), as the \(2\times2\) Lyapunov equation shows directly. Therefore the total stationary follower position variance equals \(J_2(S)/2\). The classification applies exactly to this specified model; it does not assume the same expression under unmatched or absolute-velocity damping.

## Proof

**1. Exhaustive orbit types.** Permutations of the healthy vertices within each bipartition class and interchange of the two classes preserve the defective graph. Every unordered two-leader set lies in exactly one of five types:

- `DD`: both missing-link endpoints;
- `DS`: a missing-link endpoint plus a healthy vertex in its own part;
- `DX`: a missing-link endpoint plus a healthy vertex in the opposite part;
- `SS`: two healthy vertices in one part;
- `SX`: two healthy vertices in opposite parts.

It therefore suffices to evaluate these five costs. This classification covers *all* allowed vertex pairs, with no assumed symmetry of the decision variables.

**2. Base inverse and rank-one failure.** Suppose \(a\in\{0,1,2\}\) leaders lie in \(A\), and \(2-a\) lie in \(B\). Set \(r=n-a\), \(s=n-2+a\), and \(D=n^2-rs>0\). Before removing the defective edge, the follower principal Laplacian of \(K_{n,n}\) is

\[
X=\begin{pmatrix}nI_r&-J_{r,s}\\-J_{s,r}&nI_s\end{pmatrix},
\quad
H=X^{-1}=\begin{pmatrix}
\frac1n I_r+\frac{s}{nD}J_r&\frac1D J_{r,s}\\
\frac1D J_{s,r}&\frac1n I_s+\frac{r}{nD}J_s
\end{pmatrix}.
\]

Here \(J\) denotes an all-ones matrix of the indicated size. If an endpoint of the defective edge is a leader, its corresponding follower coordinate is absent. Write \(z=e_{u_*}-e_{v_*}\), restricted to follower coordinates (an omitted coordinate contributes zero). Removing the edge gives

\[
L_{FF}=X-zz^{\mathsf T},\qquad
L_{FF}^{-1}=H+\frac{Hzz^{\mathsf T}H}{1-z^{\mathsf T}Hz}.
\]

The denominator is positive because the defective graph remains connected and hence its grounded principal Laplacian is positive definite. If both endpoints are leaders, \(z=0\). In general, with \(h=Hz\), the exact trace identity is

\[
\operatorname{tr}(L_{FF}^{-2})=
\operatorname{tr}(H^2)+
\frac{2h^{\mathsf T}Hh}{1-z^{\mathsf T}Hz}+
\frac{(h^{\mathsf T}h)^2}{(1-z^{\mathsf T}Hz)^2}.
\]

Moreover \(\operatorname{tr}(H^2)=(2n-4)/n^2+(4n^2-2D)/D^2\). These identities require only block multiplication and the rank-one inverse formula.

**3. Exact five-class evaluations.** Substitution and reduction produce the following functions of the integer \(n\):

\[
\begin{aligned}
J_{DD}&=\frac{2(n-1)(2n^3+4n^2-7n+2)}{n^2(2n-1)^2},\\
J_{DS}&=\frac{4n^6-4n^5-22n^4+76n^3-105n^2+68n-20}{n^2(2n^2-3n+2)^2},\\
J_{DX}&=\frac{4n^6-4n^5-28n^4+108n^3-147n^2+88n-20}{4n^2(n-1)^4},\\
J_{SS}&=\frac{n^6-3n^5-2n^4+23n^3-35n^2+22n-5}{n^2(n-1)^4},\\
J_{SX}&=\frac{2(2n^6-6n^5-7n^4+67n^3-134n^2+116n-40)}{n^2(2n^2-5n+4)^2}.
\end{aligned}
\]

**4. Infinite-domain sign proof.** For every \(n\ge3\), all the denominators in the rational differences are strictly positive. The numerators of \(J_{DS}-J_{DD}\), \(J_{DX}-J_{DD}\), and \(J_{SX}-J_{DD}\), when expanded in \(t=n-3\), have, respectively, the following polynomial coefficients in decreasing power order:

\[
\begin{aligned}
&(32,372,1718,3929,4432,1961),\\
&(16,300,2460,11352,31648,53065,49394,19649),\\
&(64,712,3156,6956,7604,3284).
\end{aligned}
\]

Every coefficient is strictly positive and \(t\ge0\), so these three differences are positive. The sole remaining comparison is

\[
J_{DD}-J_{SS}=\frac{Q(n)}{n^2(n-1)^4(2n-1)^2},
\]

where

\[
Q(n)=4n^7-19n^6+17n^5+14n^4-35n^3+25n^2-8n+1.
\]

Direct substitution gives \(Q(3)=-581<0\). For every \(n\ge4\), expand in \(t=n-4\):

\[
Q(t+4)=4t^7+93t^6+905t^5+4754t^4+14429t^3+24885t^2+21808t+6833>0.
\]

Thus `DD` is uniquely best at \(n=3\), whereas `SS` is strictly better than `DD` and every other type for all \(n\ge4\). The finite cases and all integer boundaries are included. Inserting \(n=3\) in \(J_{DD}\) and leaving \(J_{SS}\) symbolic proves the displayed minimal values.

## Verification

The attached standalone `verify.py` reconstructs each of the five rational costs independently from the inverse-block and rank-one identities. It checks every displayed polynomial sign certificate **symbolically** using exact integers; those finite algebraic identities, together with positivity of the coefficients for \(t\ge0\), establish the assertions for infinitely many integers. Independently it constructs the unweighted defective graph from scratch and checks every possible two-leader set by direct eigenvalue calculation for \(3\le n\le14\), including all class costs and optimizer classes. To replay, run `python verify.py` with Python 3, SymPy, and NumPy installed. The replay in the packaged environment passed **1,947 checks**. The finite eigenvalue sweeps are diagnostics, not substitutes for the symbolic infinite-domain proof.

## Relationship to prior work

Classical noise-free leader-selection work studies grounded inverse-Laplacian traces. Patterson and Bamieh (2010), Clark, Bushnell and Poovendran (2012), and Lin, Fardad and Jovanović (2013) provide first-order coherence and general leader-selection frameworks; Patterson, McGlohon and Dyagilev (2014) give optimal algorithms on one-dimensional formations. For the **same defective complete-bipartite graph**, the previously indexed result *A six-per-part transition in fault-aware two-leader coherence* determines the first-order optimum: missing-edge endpoints for \(3\le n\le5\), and two healthy same-part vertices for \(n\ge6\). The present theorem evaluates the **different inverse-square spectral functional** and proves that its sharp switch already occurs at \(n=4\). The prior first-order minimizer characterization alone does not imply any inverse-square ordering. Another indexed result treating the defective \(K_{p,q}\) family likewise states inverse-*first*-power costs, not the result here. A separate indexed result on unmodified near-balanced bipartite graphs handles inverse-square coherence but does not account for a missing link.

## Limitations

The result is restricted to a single missing edge of \(K_{n,n}\), exactly two perfectly pinned leaders, identical unit weights, and the stated second-order relative-damping model. It does not optimize leader gains, arbitrary numbers of leaders, weighted or multiple failures, or transient covariance. The proof is complete for this stated graph family, but independent peer evaluation and comprehensive publication-priority verification have not been performed. In particular, indexed summaries of closely related published findings were available, while their complete repository manuscripts could not be retrieved during this review; an unindexed equivalent formulation could alter the originality assessment.

## References

1. S. Patterson and B. Bamieh, *Leader Selection for Optimal Network Coherence*, 49th IEEE Conference on Decision and Control (2010), https://webee.technion.ac.il/Sites/People/stacyp/papers/patterson_cdc10_leader.pdf .
2. A. Clark, L. Bushnell and R. Poovendran, *A Supermodular Optimization Framework for Leader Selection under Link Noise in Linear Multi-Agent Systems*, arXiv:1208.0946, first posted 2012-08-04, https://arxiv.org/abs/1208.0946 .
3. F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for leader selection in stochastically forced consensus networks*, arXiv:1302.0450, first posted 2013-02-03, https://arxiv.org/abs/1302.0450 .
4. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, first posted 2014-12-20, https://arxiv.org/abs/1412.6595 .
5. *A six-per-part transition in fault-aware two-leader coherence*, published research record 2026/10/25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-six-per-part-transition-in-fault-aware-two-leader-coherence--414fa67c152f .
6. *Sharp two-leader phase diagram for \(K_{p,q}\) with one missing edge*, published research record 2026/11/08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-leader-phase-diagram-for-k-p-q-with-one-missing-edge--042a25838168 .
7. *Exact cubic all-leader phase transition for second-order coherence on \(K_{m,m+1}\)*, published research record 2026/11/02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-cubic-all-leader-phase-transition-for-second-order-coheren--2a6d4bf0a7f2 .
