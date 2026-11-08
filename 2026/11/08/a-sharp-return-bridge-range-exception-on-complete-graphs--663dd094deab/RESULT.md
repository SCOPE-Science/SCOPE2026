# A sharp return-bridge range exception on complete graphs

## Finding

Let \(n\ge3\) and let \(X_0,X_1,\ldots,X_t\) be simple random walk without holding on the complete graph \(K_n\), starting at any fixed vertex, where \(t\ge2\) is an integer. Let \(R_t=|\{X_0,\ldots,X_t\}|\) and let \(R_t^{\mathrm{br}}\) have the conditional distribution of \(R_t\) given \(X_t=X_0\). Write \(A=(n-1)^t\), \(B=(n-2)^t\), and \(\epsilon=(-1)^t\). Then

\[
\mathbb E R_t=n-\frac{B}{(n-1)^{t-1}},\qquad
\mathbb E R_t^{\mathrm{br}}=n-n\frac{B+(n-2)\epsilon}{A+(n-1)\epsilon}.
\]

The sign comparison is complete and strict:

\[
\mathbb E R_t^{\mathrm{br}}>\mathbb E R_t
\quad\Longleftrightarrow\quad n=3\ \text{and}\ t\ge3\ \text{is odd}.
\]

In the exceptional case the difference is exactly \(2^{1-t}\); for every other admissible pair the bridge has smaller expected range. Furthermore, when \(t\ge3\) is odd and \(n\ge t+1\), the distributions of \(R_t^{\mathrm{br}}\) and \(R_t\) are incomparable by first-order stochastic domination.

## Assumptions and scope

All vertices are distinct and every step chooses uniformly among the \(n-1\) other vertices; there is no holding probability. A bridge is the original walk conditional on returning at the prescribed, deterministic step \(t\), not the first-return process. The return-conditioning event has positive probability for all \(n\ge3,t\ge2\). Cardinalities count the starting vertex and the step-\(t\) endpoint, with repetitions counted once. No asymptotic limit is needed.

## Proof

Fix a vertex \(v\ne X_0\). For the unconditioned walk, at each step before the first hit of \(v\), exactly \(n-2\) out of the \(n-1\) possible successors avoid \(v\). Thus

\[
\Pr(v\notin\{X_0,\ldots,X_t\})=\left(\frac{n-2}{n-1}\right)^t,
\]

and summing the \(n-1\) non-starting vertex indicators gives the first expectation.

For the bridge, consider the transition matrix restricted to the \(n-1\) vertices other than \(v\), retaining the original transition probabilities. It equals \((J_{n-1}-I_{n-1})/(n-1)\), and therefore has eigenvalue \((n-2)/(n-1)\) on constants and \(-1/(n-1)\) on their orthogonal complement. Its diagonal entry after \(t\) steps is

\[
\Pr(X_t=X_0,\ v\text{ unvisited})=
\frac{(n-2)^t+(n-2)(-1)^t}{(n-1)^{t+1}}.
\]

Similarly, the full transition matrix \((J_n-I_n)/(n-1)\) gives

\[
\Pr(X_t=X_0)=\frac{(n-1)^t+(n-1)(-1)^t}{n(n-1)^t}.
\]

Division and summation of avoidance indicators yields the second expectation. Subtraction gives

\[
\mathbb ER_t^{\mathrm{br}}-\mathbb ER_t
=\frac{-AB+\epsilon((n-1)^2B-n(n-2)A)}{A(A+(n-1)\epsilon)}.
\]

The denominator is positive. Put \(d=n-1\ge2\). If \(t\) is even, the numerator is \(B(d^2-A)-(d^2-1)A<0\), because \(A=d^t\ge d^2\). If \(t\) is odd, necessarily \(t\ge3\); the numerator becomes \(A(d^2-1-B)-d^2B\). For \(d\ge3\), \(B=(d-1)^t\ge(d-1)^3\ge d^2-1\), so the numerator is negative. For \(d=2\), \(B=1\) and the numerator is \(2A-4>0\), giving \((2A-4)/(A(A-2))=2/A=2^{1-t}\). These cases prove the complete classification.

For the stochastic assertion, suppose \(t\) is odd and \(n\ge t+1\). Every closed walk of odd length on a loopless complete graph requires at least three distinct vertices, so \(\Pr(R_t^{\mathrm{br}}=2)=0\). An unrestricted walk can alternate between its start and a fixed neighbour, giving \(\Pr(R_t=2)>0\). Conversely, a bridge of length \(t\) contains at most \(t\) distinct vertices, while an unrestricted walk can follow a self-avoiding path of length \(t\), yielding \(\Pr(R_t=t+1)>0\). Consequently the two cumulative distribution functions cross, excluding stochastic domination in either direction.

## Verification

The standalone `CHECKER.py`, run under Python 3, uses exact integers and rational numbers. It independently counts paths by visited-vertex count and root-return status, verifies both expectation formulas and every strict sign, and tests the stochastic-support statement for a finite grid of \(3\le n\le16\) and \(2\le t\le26\). It reports 1,246 passing assertions. Those finite computations are diagnostics, not substitutes for the preceding all-parameter proof.

## Relationship to prior work

Sauerwald, Sun and Vagnozzi (2023) motivate the comparison of support sizes for open walks and return-conditioned walks, and prove general bounds for graph classes. Their results do not state this exact complete-graph expectation identity or its sharp three-vertex odd-time reversal. Benjamini, Izkovsky and Kesten (2007) analyze bridge ranges on infinite vertex-transitive graphs and groups, rather than the finite complete-graph exception. The two-eigenvalue decomposition of the complete graph itself is standard and is used here without a novelty claim. The contribution is the exhaustive strict comparison and the associated stochastic-order obstruction.

## Limitations

These identities concern simple no-holding random walk on finite complete graphs only. They do not establish any ordering for general graphs, lazy walks, or arbitrary return-conditioning times. In particular, a strict mean inequality does not establish stochastic domination. Historical priority remains qualified: simple finite complete-graph identities might appear in older or unindexed references. No independent mathematical audit is claimed.

## References

1. T. Sauerwald, H. Sun, D. Vagnozzi, *The Support of Open Versus Closed Random Walks*, ICALP 2023, Article 103, published 2023-07-05. https://doi.org/10.4230/LIPIcs.ICALP.2023.103
2. I. Benjamini, R. Izkovsky, H. Kesten, *On the range of the simple random walk bridge on groups*, Electronic Journal of Probability 12 (2007), 591–612. https://arxiv.org/abs/math/0605050
