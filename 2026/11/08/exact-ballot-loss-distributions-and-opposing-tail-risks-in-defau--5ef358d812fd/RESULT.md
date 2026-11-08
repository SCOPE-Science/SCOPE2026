# Exact ballot-loss distributions and opposing tail risks in default delegation networks

## Finding

A fixed delegation network can be assessed by the **distribution** of unrepresented ballots, not only its expected loss. The theorem below provides an exact polynomial recursion for this distribution, classifies the networks with the worst expected loss and the worst probability of any loss, and exhibits a strict reversal between expected loss and a three-ballot tail event. The latter shows that optimizing the mean is not the same as controlling all severe-loss risks.

**Theorem (distribution and extremal risk).** Let \(n\ge2\), let \(f:V\to V\) satisfy \(f(v)\ne v\) for every voter, and let every voter independently cast a ballot with probability \(1-p\), for a common \(0<p<1\). An abstaining voter transfers her unit voting weight along \(f\) until the first casting voter is reached. If the walk encounters a cycle without a casting voter, the unit ballot is lost. Write \(L\) for the number of lost unit ballots.

For each directed cycle \(C\) of the functional graph, write \(c=|C|\), and let \(R_C\) be the set of non-cycle vertices with their unique outgoing edge entering \(C\). For a non-cycle vertex \(u\), define the polynomial

\[
F_u(z)=(1-p)+pz\prod_{w\in\operatorname{child}(u)}F_w(z),
\]

where \(\operatorname{child}(u)=\{w\notin\bigcup C:f(w)=u\}\), and the product over no children is \(1\). Then

\[
\boxed{\mathbb E[z^L]=\prod_{C}\left(1-p^{|C|}+p^{|C|}z^{|C|}\prod_{u\in R_C}F_u(z)\right).}
\]

All coefficients are the exact probabilities of their corresponding loss counts. In particular,

\[
\Pr(L>0)=1-\prod_C(1-p^{|C|}),\qquad
\mathbb E L=\sum_{v\in V}p^{|C(v)|+d(v,C(v))}.
\]

Here \(C(v)\) is the unique cycle reached from \(v\), and \(d(v,C(v))\) is the number of edges from \(v\) to that cycle (zero on a cycle).

Over **all** loopless functional graphs on \(n\) labelled vertices, the sharp bounds are

\[
\boxed{\max\mathbb E L=\begin{cases}np^2,&n\text{ even},\\(n-1)p^2+p^3,&n\text{ odd},\end{cases}}
\]

and

\[
\boxed{\max\Pr(L>0)=1-(1-p^2)^{\lfloor n/2\rfloor}.}
\]

For either maximum, equality holds **if and only if** the graph consists of \(n/2\) isolated directed 2-cycles when \(n\) is even, or \((n-1)/2\) directed 2-cycles and one additional vertex pointing to a cycle vertex when \(n\) is odd.

The two optimized criteria cannot be conflated with upper-tail control. On six vertices, let \(A\) be a disjoint union of three directed 2-cycles and \(B\) a disjoint union of two directed 3-cycles. Then

\[
L_A\overset{d}=2\,\operatorname{Binomial}(3,p^2),\qquad
L_B\overset{d}=3\,\operatorname{Binomial}(2,p^3).
\]

Consequently \(\mathbb E L_A=6p^2>6p^3=\mathbb E L_B\), whereas

\[
\Pr(L_B\ge3)-\Pr(L_A\ge3)
=p^3(1-p)^2(p+2)>0.
\]

## Assumptions and scope

Every voter has exactly one default delegate distinct from herself. The delegation graph is finite, directed, and functional, with no self-loops, but it may contain disconnected components and arbitrarily directed in-trees. Only **unit ballot representation** is measured; the ballots' preferences, election winner, and strategic incentives do not enter the theorem. Decisions to cast are independent and have one common probability \(1-p\), strictly between zero and one. A casting voter represents herself and everyone whose delegation path first reaches her. The count \(L\) includes absent as well as casting voters only when their voting weight finds no casting endpoint. The theorem does not address heterogeneous turnout, graphs permitting self-loops, or correlated participation.

## Proof

**1. Component event.** A finite functional component has exactly one directed cycle, with rooted in-trees feeding its cycle vertices. If any cycle voter casts, every vertex's path eventually reaches a casting voter—possibly before reaching the cycle—so no ballot in that component is lost. If all \(c\) cycle voters abstain, all \(c\) cycle ballots are lost, while an off-cycle ballot is lost precisely when all voters on its path into the cycle also abstain. The full-cycle-abstention event has probability \(p^c\) and is independent of all off-cycle casting decisions. Thus the component polynomial has the asserted mixture of zero loss and the conditional loss polynomial.

**2. Subtree recursion.** Conditional on a failed cycle, consider a rooted off-cycle subtree at \(u\). If \(u\) casts, the entire subtree is represented at \(u\) or an earlier casting descendant, giving polynomial \(1\). This case has probability \(1-p\). If \(u\) abstains, \(u\)'s own ballot is lost (a factor \(z\)); independently, each incoming child subtree contributes its own loss count, with the same conditional rule. This yields \(F_u(z)=(1-p)+pz\prod_wF_w(z)\). Distinct subtrees and components depend on disjoint sets of independent casting decisions, so their generating polynomials multiply. This proves the complete-distribution formula. All products have degree at most \(n\), so tree dynamic programming plus polynomial convolution computes every coefficient in polynomial time.

**3. First moment and any-loss probability.** At least one ballot is lost if and only if some cycle has no casting voter. Independent cycle failures give \(1-\prod_C(1-p^{|C|})\). A particular voter \(v\) loses her ballot exactly when all distinct voters from \(v\) along her path to and around \(C(v)\) abstain. That event has probability \(p^{|C(v)|+d(v,C(v))}\). Summing its indicator gives the displayed expectation. This last first-moment identity is also readily obtainable from the previously published individual-loss/path-probability formulas; it is included here for deriving the new maximum, not claimed as an independently new formula.

**4. Sharp mean maximum.** Let \(m\) be the number of vertices lying on directed 2-cycles; \(m\) is even. Their individual loss probabilities are \(p^2\). Every other vertex has a cycle-and-path length at least \(3\), hence loss probability at most \(p^3\), with strict inequality if its length exceeds \(3\). Therefore \(\mathbb E L\le mp^2+(n-m)p^3\). Because \(p^2>p^3\), equality with the universal maximum requires the largest feasible \(m\): namely \(m=n\) for even \(n\), and \(m=n-1\) for odd \(n\). In the even case, all vertices form 2-cycles and attain \(np^2\). In the odd case, there are \((n-1)/2\) 2-cycles and one remaining vertex; its only allowed edge enters a 2-cycle, giving path-and-cycle length \(3\), so the upper bound \((n-1)p^2+p^3\) is attained. Conversely, strictness of \(p^2>p^3\) forces exactly these structures in all equality cases.

**5. Sharp any-loss maximum.** Suppose the graph has \(k\) distinct cycles of lengths \(c_1,\ldots,c_k\). Since every \(c_j\ge2\) and cycles are disjoint, \(k\le\lfloor n/2\rfloor\). For \(0<p<1\), one has \(1-p^{c_j}\ge1-p^2\), with equality precisely when \(c_j=2\). Hence \(\prod_j(1-p^{c_j})\ge(1-p^2)^k\ge(1-p^2)^{\lfloor n/2\rfloor}\). Both inequalities attain equality exactly when there are \(\lfloor n/2\rfloor\) cycles and all have length two. The single leftover vertex when \(n\) is odd is necessarily off-cycle and at distance one. Taking complements proves the second extremal theorem and all equality cases.

**6. Tail-risk reversal.** In disjoint all-cycle components, either the entire cycle fails (all its ballots are lost) or none fails. The component-failure events are independent. Thus the two six-voter distributions in the statement are exact. Direct binomial calculation gives \(\Pr(L_A\ge3)=3p^4-2p^6\) and \(\Pr(L_B\ge3)=2p^3-p^6\). Their difference factors as \(p^3(1-p)^2(p+2)\), strictly positive for the stipulated parameter range, even though the means have the opposite strict order.

## Verification

The accompanying `verify_cycle_loss.py` is a standalone Python 3 checker relying only on the standard library. Run `python verify_cycle_loss.py`. It uses `fractions.Fraction` to verify the distribution recursion against independent exhaustive enumeration over all casting/abstention subsets, and checks sharp expectation/any-loss bounds and equality structures for every labelled loopless functional graph with \(2\le n\le6\). Actual observed results: 16,739 graphs; 33,478 graph–probability bound cases; 133,912 bound/equality assertions; 2,534 full-distribution brute comparisons; and a verified strict six-voter tail inversion. Two distinct rational turnout probabilities are used for the bound checks. These finite computations test the equations and implementations but do **not** constitute proof for unbounded \(n\); the six analytic steps above provide that proof.

## Relationship to prior work

Brill et al. [1] introduce and analyze probabilistic default delegations. Their Appendix B.4 derives recursive **expected** lost voting power and their Proposition 19 states the *minimizing* topology: a single Hamiltonian directed cycle. Thus the model, individual-loss/first-moment method, and minimization direction are already established. The present theorem addresses a different question: the **entire loss distribution**, exact **maximizers** of mean and any-loss probability, and the strict conflict between mean and a nonzero-loss upper tail. These three features were not located in the inspected full text of [1]. Grossi et al. [2] investigate expected voting weight via random-walk-decay centrality and selection of powerful representatives, not the distribution of the total number of lost ballots. Christoff and Grossi [3] discuss delegation cycles and abstentions in a different binary aggregation framework. The mathematical formula can be viewed as a probability-generating-function refinement of known component-path expectations; no novelty is claimed for elementary probability-generating-function algebra by itself.

## Limitations

This is a homogeneous independent-casting model; heterogeneity or correlations can change the extremizers. The theorem is about representational failures rather than welfare, fairness of election outcomes, or equilibrium incentives. The mean maximizer is easy to infer once the known individual path probabilities are available; the scientific contribution is the unified full-distribution and risk-shape characterization, especially the exact upper-tail reversal. Although targeted literature and mathematical-record searches found no identical theorem, unindexed equivalents and alternative random-reliability formulations are possible. No independent external audit of the proof or computations has been performed.

## References

1. Markus Brill, Rachael Colley, Anne-Marie George, Grzegorz Lisowski, Georgios Papasotiropoulos, and Ulrike Schmidt-Kraepelin, *Cycles in Liquid Democracy: A Game-Theoretic Justification*, arXiv:2607.12610, first submitted 14 July 2026, especially Section 2 and Appendix B.4, Proposition 19. https://arxiv.org/abs/2607.12610
2. Davide Grossi, Andreas Nitsche, Georgios Papasotiropoulos, Oskar Skibski, Piotr Skowron, and Tomasz Wąs, *Power in Liquid Democracy: A Network Centrality Approach*, arXiv:2608.13188, first submitted 13 August 2026. https://arxiv.org/abs/2608.13188
3. Zoé Christoff and Davide Grossi, *Liquid Democracy: An Analysis in Binary Aggregation and Diffusion*, arXiv:1612.08048, 2016. https://arxiv.org/abs/1612.08048
