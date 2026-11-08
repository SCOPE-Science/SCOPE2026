# A sharp price transition for continuous-time fastest mixing on complete split graphs

## Finding

Let \(G=K_p\vee\overline{K_q}\) be the complete split graph, with a \(p\)-vertex clique and a \(q\)-vertex independent set. For all integers \(p,q\ge2\), crossing-edge price \(A>0\), clique-edge price \(C>0\), and total budget \(B>0\), define the weighted Laplacian \(L_w\) for nonnegative edge rates. The optimal continuous-time convergence rate is

\[
\max_{A\sum_{\mathrm{cross}}w_e+C\sum_{\mathrm{clique}}w_e\le B}\lambda_2(L_w)=\frac{B}{H_{p,q}(A,C)},
\]

where

\[
H_{p,q}(A,C)=\begin{cases}
qA,&q\ge p,\\
\min\!\left\{pA,\ qA+\dfrac{(p-1)(p-q)}{2p}C\right\},&q<p.
\end{cases}
\]

Among class-symmetric designs, a phase change occurs at \(C/A=2p/(p-1)\) when \(q<p\). Below this threshold it is optimal to use positive clique rates, above it the clique rates are zero, and exactly at the threshold there is a full interval of class-symmetric optimal designs. All assertions concern nonnegative rates; a zero rate is an allowed omission of that edge.

## Assumptions and scope

Every one of the \(pq\) crossing edges costs \(A\) per unit rate and each of the \(p(p-1)/2\) clique edges costs \(C\) per unit rate. There is no holding-rate or discrete-time stochasticity constraint. The continuous-time evolution is \(\dot z=-L_w z\), with invariant uniform equilibrium and convergence exponent controlled by \(\lambda_2(L_w)\). Only the graph \(K_p\vee\overline{K_q}\), the stated two rate-price classes, and budgets \(B>0\) are included.

For all \(p,q\ge2\), put \(t=B/H_{p,q}(A,C)\). Write \(x\) for each crossing rate and \(y\) for each clique rate. An optimal class-symmetric design is as follows:

* If \(q\ge p\), take \(x=t/p\), \(y=0\).
* If \(q<p\) and \(C/A<2p/(p-1)\), take \(x=t/p\), \(y=(p-q)t/p^2\).
* If \(q<p\) and \(C/A>2p/(p-1)\), take \(x=t/q\), \(y=0\).
* If \(q<p\) and \(C/A=2p/(p-1)\), take any \(x\in[t/p,t/q]\) and \(y=(t-qx)/p\).

These are **all class-symmetric optimal pairs**. No uniqueness statement about nonsymmetric optimal rate matrices is claimed.

## Proof

**Reduction to two parameters.** On \(\mathbf1^\perp\), the function \(w\mapsto\lambda_2(L_w)\) is the infimum of linear Rayleigh quotients and hence concave. Averaging any feasible rate assignment under all permutations of clique vertices and, independently, all permutations of independent vertices preserves the budget and cannot decrease \(\lambda_2\). Thus some globally optimal assignment is class-symmetric.

**Exact spectrum.** For common crossing rate \(x\ge0\) and clique rate \(y\ge0\), the block Laplacian is

\[
L=\begin{pmatrix}
(qx+py)I_p-yJ_p&-xJ_{p\times q}\\
-xJ_{q\times p}&pxI_q
\end{pmatrix}.
\]

The constant vector has eigenvalue zero. Clique-internal sum-zero vectors have eigenvalue \(qx+py\) with multiplicity \(p-1\); independent-part sum-zero vectors have eigenvalue \(px\) with multiplicity \(q-1\); the vector constant on each part, with opposite weighted means, has eigenvalue \((p+q)x\). Since \((p+q)x\ge px\),

\[
\lambda_2(L)=\min\{px,qx+py\}.
\]

**Minimum cost for unit spectral gap.** By positive homogeneity, calculate the minimum budget required for \(\lambda_2\ge1\), then scale. This problem is the two-variable linear program

\[
\min_{x,y\ge0}\left(pqAx+\frac{p(p-1)}2 Cy\right)
\quad\text{subject to}\quad px\ge1,\quad qx+py\ge1.
\]

If \(q\ge p\), the first constraint implies the second at \(y=0\). The least-cost point is \(x=1/p,y=0\), at cost \(qA\).

If \(q<p\), the lower boundary of feasibility is \(1/p\le x\le1/q\), \(y=(1-qx)/p\). Its cost is

\[
\frac{p-1}{2}C+q\left(pA-\frac{p-1}{2}C\right)x.
\]

The derivative changes sign exactly when \(C/A=2p/(p-1)\). The left endpoint has cost \(qA+(p-1)(p-q)C/(2p)\); the right endpoint has cost \(pA\). If the derivative is zero, every point of the intervening line segment has the same cost. Rates with \(x>1/q\) cannot be cheaper, because \(y\ge0\) and costs are positive. This proves the optimum and all symmetric optimizers. Scaling the unit-gap rates by \(B/H\) completes the proof.

**Quantitative consequence.** In the \(q<p\) regime the best allocation without clique edges uses \(x=B/(pqA)\) and has gap \(B/(pA)\). With price \(C\) approaching zero through positive values, the achieved optimum approaches \(B/(qA)\). Thus its improvement factor over the crossing-only design tends to \(p/q\), which can grow without bound at fixed \(q\).

## Verification

Run `python3 verify.py` using Python 3 standard library only. The checker constructs exact rational Laplacians, verifies the complete decomposition on a spanning set of explicit eigenvectors, checks exact costs and claimed rates for 720 parameter instances, and checks 72,720 feasible rational class-symmetric allocations against the optimum. Exact finite checks are reproducibility evidence; the proof above establishes all quantifiers. The checker does not enumerate nonsymmetric rate assignments or certify an infinite family computationally.

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis (2006) formulate the general continuous-time fastest-mixing Markov process and its semidefinite/maximum-variance-unfolding dual. Their general method does not state the present price-dependent closed form for complete split graphs. Boyd, Diaconis, and Xiao (2004) optimize discrete-time symmetric transition SLEM, subject to stochasticity constraints, not a linear budget on continuous-time rates. Jafarizadeh (2015) treats continuous-time consensus on several structured graphs, including clique-cored stars and lollipops, but its inspected topology formulas do not directly state this all-parameter complete-split two-price transition. The exact graph and price model distinguish the claim from those problems. Those works provide the underlying established spectral optimization framework, not a claim of a new general principle.

## Limitations

The result is a special-family closed form derived from established concavity and spectral decomposition methods, not a new general algorithm. Only class-symmetric optimal assignments are fully described; nonsymmetric ties, if any, are not classified. No resilience to edge failures, nonlinear dynamics, prescribed nonuniform stationary distribution, or discrete-time fastest-mixing claim follows. Mathematical priority could be affected by specialized work not indexed in the searched records; no independent audit has been performed.

## References

1. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, “The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem,” *SIAM Review* 48(4), 681–699 (2006), DOI: 10.1137/S0036144504443821, first online November 2, 2006. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.
2. S. Boyd, P. Diaconis, and L. Xiao, “Fastest Mixing Markov Chain on a Graph,” *SIAM Review* 46(4), 667–689 (2004), DOI: 10.1137/S0036144503423264. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.
3. S. Jafarizadeh, “Optimizing the Convergence Rate of the Continuous Time Quantum Consensus,” arXiv:1509.05823 (first posted September 18, 2015), https://arxiv.org/abs/1509.05823.
