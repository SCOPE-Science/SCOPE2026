# Sharp intrinsic-growth onset of positive two-cycles in a quadratic plankton map

## Finding
Consider the quadratic discrete-time plankton map
\[
F_{R,r,\gamma}(x,y)=\bigl(x(R-x-y),\ y(1-r+\gamma x)\bigr),
\]
where \(R>1\), \(0<r<1\), and \(\gamma>0\). A *positive primitive two-cycle* is a pair of distinct points \((x,y),(u,v)\in(0,\infty)^2\) interchanged by \(F_{R,r,\gamma}\). Its existence depends sharply on the prey's intrinsic growth parameter:
\[
\boxed{\text{No positive primitive two-cycle exists for any }r,\gamma
\quad\Longleftrightarrow\quad R\le3.}
\]
The right-to-left existence assertion means that **for each** \(R>3\) suitable admissible \(r,\gamma\) give a positive primitive two-cycle; it does not say that all predator parameters do so.

In fact all positive primitive two-cycles, up to swapping their two states, have the following exact parameterization. Choose
\[
p>1,\qquad R>p+1+\frac1p,\qquad \frac1{\sqrt p}<q<1,
\]
and put
\[
\begin{aligned}
x&=\frac{R-q(R-p)-p^{-1}}{p-q},&
y&=\frac{(p-1)(R-p-1-p^{-1})}{p-q},\\
u&=px,&v&=qy,\\
\gamma&=\frac{q^{-1}-q}{(p-1)x},&
r&=1-q+\gamma x.
\end{aligned}
\]
Then \(x,y,u,v>0\), \(0<r<1\), \(\gamma>0\), and \(F(x,y)=(u,v)\), \(F(u,v)=(x,y)\). Conversely every admissible positive primitive two-cycle has this form after relabeling its states.

## Assumptions and scope
The statement concerns the exact polynomial map on positive pairs, not a numerical Euler approximation to a continuous flow, and only two-periodic orbits lying entirely in \((0,\infty)^2\). The map need not preserve the whole positive quadrant for arbitrary starting values. Restricting \(0<r<1\) ensures the predator survival multiplier \(1-r+\gamma x\) is positive for all nonnegative prey populations; the nonexistence half actually only needs positivity of the multipliers at the two cycle states. The normalization of prey self-competition and predation coefficients to one is achieved by positive population rescaling in the standard two-coefficient variant.

## Proof
Let \((x,y)\mapsto(u,v)\mapsto(x,y)\) be a positive primitive two-cycle. If \(x=u\), the prey equation and \(x>0\) give \(y=v\), contradicting primitivity. Exchange the two states if necessary so that \(u>x\) and define \(p=u/x>1\), \(q=v/y>0\). The two predator multipliers \(1-r+\gamma x\) and \(1-r+\gamma u\) have product one; the latter is strictly greater because \(\gamma>0\) and \(u>x\). Hence the first multiplier is less than one and therefore \(0<q<1\).

The prey equations, divided by their positive prey coordinates, give
\[
x+y=R-p,\qquad u+v=R-p^{-1}.
\]
On the other hand, \(u+v=px+qy<p(x+y)=p(R-p)\), since \(y>0\) and \(q<p\). Rearranging yields
\[
R>p+1+p^{-1}\ge3,
\]
which proves nonexistence when \(R\le3\), including the critical equality \(R=3\). No dynamics outside the proposed cycle are needed.

To see sharpness for every \(R>3\), continuity of \(p+1+p^{-1}\) at \(p=1\) permits some \(p>1\) with \(R>p+1+p^{-1}\). Choose any \(q\) between \(p^{-1/2}\) and one. Solving the two linear prey relations \(x+y=R-p\) and \(px+qy=R-p^{-1}\) gives exactly the formulas displayed above. Their denominators are positive and \(y>0\) by the strict inequality on \(R\). Furthermore
\[
R-q(R-p)-p^{-1}=R(1-q)+pq-p^{-1}>0,
\]
so \(x>0\), and thus \(u=px\) and \(v=qy\) are positive.

Choose \(\gamma\) and \(r\) as displayed. Since \(q<1\), \(\gamma>0\). A calculation gives
\[
1-r=q-\gamma x=\frac{pq^2-1}{q(p-1)}.
\]
The assumption \(q>p^{-1/2}\) shows \(1-r>0\), while \(1-r<q<1\) shows \(0<r<1\). The predator multipliers at \(x\) and \(u\) are respectively
\[
1-r+\gamma x=q,
\qquad
1-r+\gamma u=q+\gamma(p-1)x=q^{-1}.
\]
Consequently the predator coordinates interchange as required, and the prey coordinates do so by their defining linear equations. As \(p>1\), the states are distinct.

Finally, for any positive primitive two-cycle the first argument supplies \(p>1\), \(0<q<1\) and \(R>p+1+p^{-1}\). Solving the prey equations forces the formulas for \(x,y\). Solving the two predator multiplier equations forces \(\gamma=(q^{-1}-q)/[(p-1)x]\) and \(1-r=(pq^2-1)/[q(p-1)]\). Thus \(0<r<1\) forces \(q>p^{-1/2}\), so the parameterization is exhaustive. This proves the theorem.

## Verification
A fully rational witness at \(R=4\) is
\[
(x,y)=\left(\frac85,\frac25\right),\quad
(u,v)=\left(\frac{16}5,\frac3{10}\right),\quad
r=\frac56,\quad\gamma=\frac{35}{96}.
\]
Direct exact substitution verifies both cycle equations. The accompanying standalone Python checker, `cycle_checker.py`, uses rational arithmetic to recheck that witness and a deterministic sample of further parameters in the permitted region. The proof above, rather than these finite tests, establishes the universal claims.

## Relationship to prior work
Shoyimardonov's 2025 paper fixes \(R=2\), establishing the model's equilibria, local and selected global stability, and a Neimark–Sacker transition. Its period-two calculation concerns the predator-free invariant axis. A published published-finding corpus finding, *Global exclusion of prime-two coexistence cycles in the discrete linear-response plankton model*, already proves no biologically nonnegative prime-two cycle in the **fixed** \(R=2\) map. The present result does not reclaim that exclusion. It determines the **sharp growth boundary** in the varying-\(R\) family and constructs and parameterizes all positive two-cycles above it. The published published-finding corpus summary was accessible, but its complete record was not; unindexed broader theorems are a residual priority risk.

## Limitations
This is a universal *existence frontier* over the predator parameters, not a stability criterion or a full orbit classification at fixed parameters. It does not constrain higher primitive periods, invariant circles, or globally admissible invariant regions. Near \(R=3\), the constructed cycles require a parameter choice with \(p\) and \(q\) close to one. The unavailability of a highly relevant published record's complete text leaves a historical novelty risk, not a gap in the algebraic proof.

## References
1. S. K. Shoyimardonov, *Stability and Bifurcation Analysis of a Phytoplankton-Zooplankton Model with Linear Functional Responses*, arXiv:2505.09968 (first public version 2025-05-15), https://arxiv.org/abs/2505.09968.
2. *Global exclusion of prime-two coexistence cycles in the discrete linear-response plankton model*, published-finding corpus, published 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-global-exclusion-of-prime-two-coexistence-cycles-in-the-discrete--8dd374b0e558.
