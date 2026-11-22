# Exact reinforcement-induced consensus slowdown on a five-agent hyperstar

## Finding

Consider the asynchronous binary group-driven voter process on the five-vertex, three-uniform hypergraph with hyperedges \(\{0,1,2\}\) and \(\{0,3,4\}\). Starting from the polarized profile \((0,0,0,1,1)\), let \(\tau_q\) be the number of attempted individual updates before the first unanimous state. For every integer \(q\geq1\), put \(u=2^{-q}\). Then

\[
\mathbb E\tau_q=\frac{5(30u^4+128u^3+109u^2+32u+3)}{2u(5u+1)(u^2+7u+3)}.
\]

This expectation is strictly increasing in \(q\), and

\[
\lim_{q\to\infty}2^{-q}\mathbb E\tau_q=\frac52.
\]

Thus strengthening unanimity preference slows consensus exponentially on the smallest possible connected three-uniform hypergraph exhibiting unbounded mean consensus time as \(q\to\infty\). On every connected three-uniform hypergraph with at most four vertices, every initial state's mean consensus time stays bounded uniformly for \(q\geq1\).

## Assumptions and scope

There are five fixed agents with opinions in \(\{0,1\}\), with no changes to hyperedges. At each discrete attempt, one agent is chosen uniformly from the five. That agent selects one of its incident hyperedges uniformly. Let \(k\in\{0,1,2\}\) be the number of other members of the selected triple with the opposite opinion. The chosen agent independently flips with probability \((k/2)^q\), with \(q\in\{1,2,3,\ldots\}\). In particular, the flip probabilities for \(k=0,1,2\) are \(0,u,1\), respectively. A rejected flip counts as an attempt. Consensus means either all zeros or all ones. The model is a fixed-network, with-replacement version of group-driven voter dynamics; no mean-field or large-population limit is assumed.

## Proof

For \(u>0\), every nonconstant state admits a positive-probability finite sequence of updates reaching a unanimous state: use any opinion that is present and propagate it through a connected chain of overlapping hyperedges, flipping individual dissenters where needed. Consequently the finite-state chain is absorbing with finite expected absorption time. More directly for this hypergraph, the transition equations below produce finite nonnegative expectations for all \(u>0\).

The update law is invariant under interchanging agents \(1,2\), interchanging agents \(3,4\), swapping the two leaf pairs, and complementing every opinion. Under these symmetries, the thirty nonconsensus states form five classes represented, in order, by \(00001\), \(00011\), \(00101\), \(00111\), and \(01111\). Let \(T_j\) be the mean remaining number of attempts for the corresponding class. The exact first-step equations are \(A(u)T=\mathbf 1\), where

\[
A(u)=\frac1{10}\begin{pmatrix}
2+3u&-2u&0&-u&0\\
-4u&4u&0&0&0\\
-4&0&4+4u&-4u&0\\
-1-u&-2&-4u&3+7u&-2u\\
0&0&0&-8u&2+8u
\end{pmatrix}.
\]

Here each diagonal entry is the sum of accepted-flip probabilities leading out of its class, including absorption, and each off-diagonal entry is minus the probability of moving to the corresponding nonabsorbing class. All rates include the uniform \(1/5\) choice of vertex and the hub's uniform \(1/2\) choice of incident triple. Inverting the five-state system or verifying its rational-polynomial identity gives the formula for \(T_2=\mathbb E\tau_q\) displayed above. A standalone verifier checks all five polynomial first-step identities exactly and independently constructs the full thirty-state transition equations for rational parameter values.

Differentiating \(T_2\) with respect to \(u\) gives a positive denominator and numerator proportional to

\[
440u^6+230u^5-1318u^4-1596u^3-701u^2-132u-9.
\]

On \(0<u\leq1/2\), its first two terms satisfy \(440u^6+230u^5\leq225u^4\), so the numerator is strictly negative. As \(u=2^{-q}\) decreases with \(q\), the mean is strictly increasing with \(q\). Reading the constant terms of the displayed rational expression gives \(\lim_{u\downarrow0}uT_2(u)=5/2\). For example, \(\mathbb E\tau_1=95/7\) and \(\mathbb E\tau_2=12755/693\).

To establish minimality, consider any connected three-uniform hypergraph with three or four vertices, using the same update rule. At the limiting rule \(u=0\), if there is one dissenter, it can select an incident triple containing two agreeing agents and flip directly to unanimity. A nonunanimous four-vertex configuration with a two–two split has, in every hyperedge, a two–one split; selecting the lone minority member of any edge yields a three–one split. Thus from every state on at most four vertices there is a path of at most two positive-probability flips to unanimity, and the probabilities of these particular updates are independent of \(u\). Since there are finitely many states and hypergraphs of each order, the mean absorption times are uniformly bounded for \(0\leq u\leq1/2\). On the five-vertex hypergraph in the theorem, the \(u=0\) dynamics instead contain the closed nonconsensus two-state class \(\{(0,0,0,1,1),(1,0,0,1,1)\}\): only the hub can flip, while all four leaves remain fixed. For finite \(q\), rare majority-agent flips unblock this class, yielding the exact exponential consensus delay above. This completes the sharp-minimum assertion.

## Verification

Run \(\texttt{python3 verify.py}\) with Python 3 and its standard library. The verifier evaluates exact rational-polynomial identities for the complete five-class system, independently constructs and solves the thirty-transient-state equations at five rational values of \(u\), checks all twelve labeled connected hypergraphs of order three and four, checks that the five-vertex limiting chain has a nonconsensus closed class, and checks the monotonicity inequality, sample expectations, and limiting coefficient. Its computations are auxiliary to the complete symbolic proof, not a substitute for it.

## Relationship to prior work

Kim, Lee and Goh (arXiv:2604.17689v1, first publicly posted April 20, 2026) discuss optimization of group-driven opinion consensus on hypergraphs, including the \(q\)-sample, with-replacement flip rule, largely through annealed-network and mean-field arguments. The group-driven voter rule was introduced in an earlier paper by Kim and coauthors (arXiv:2407.11261; published 2025). The present calculation concerns an exact finite fixed-overlap network, where the high-reinforcement limit produces a metastable polarized pair of states rather than a mean-field consensus acceleration. A published mathematical finding on the limiting three-person majority process for loose hyperstars already describes polarized recurrent classes; the recurrent class itself is therefore not claimed as new. The contribution assessed here is the **finite-reinforcement exact consensus-time law, its monotonicity, the precise \(2^q\) prefactor, and the minimum-vertex boundedness boundary**. These differences concern claims and implications, not title similarity.

## Limitations

The exact formula pertains to one specified initial profile and one two-triple hypergraph, not every hypergraph or every initial distribution. The lower-order boundedness assertion addresses fixed networks of at most four vertices; the theorem does not classify all larger hypergraphs. The expected attempt count is not physical elapsed time without specifying the attempt rate. The proof concerns idealized binary social imitation, not observed human behavior. Although related abstracts and a detailed public model synopsis were inspected, full originals of the most closely relevant 2025 and 2026 group-driven voter papers could not be accessed for this comparison; historical priority therefore remains a residual risk. No independent scientific validation has been performed.

## References

1. J. Kim, D.-S. Lee and K.-I. Goh, *Optimality in group-driven social dynamics on hypergraphs*, arXiv:2604.17689v1 (2026), https://arxiv.org/abs/2604.17689.
2. J. Kim, D.-S. Lee, B. Min, M. A. Porter, M. San Miguel and K.-I. Goh, *Competition between group interactions and nonlinearity in voter dynamics on hypergraphs*, Physical Review E **111**, L052301 (2025), https://doi.org/10.1103/PhysRevE.111.L052301; preprint https://arxiv.org/abs/2407.11261.
3. *Exact recurrent classes and consensus probability for majority voting on a loose hyperstar*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-recurrent-classes-and-consensus-probability-for-majority-v--d8865592de87.
4. N. Papanikolaou, G. Vaccario, E. Hormann, R. Lambiotte and F. Schweitzer, *Consensus from group interactions: An adaptive voter model on hypergraphs*, Physical Review E **105**, 054307 (2022), https://doi.org/10.1103/PhysRevE.105.054307.
