# A sharp constant stabilization-time law for random-majority dynamics on complete bipartite social networks

## Finding

Consider synchronous binary random-majority updating with independent fair tie-breaking at every vertex. On every complete bipartite network \(K_{a,b}\), with arbitrary integers \(a,b\ge1\) and arbitrary initial binary coloring, the expected number of rounds before the process enters its eventual closed communicating class is at most

\[
\boxed{\frac{79}{27}}.
\]

This bound is sharp: equality holds on \(K_{2,6}\) and \(K_{6,2}\), starting with exactly half of each part blue. These are the only graph-size pairs and initial count conditions attaining equality (up to exchanging parts and permuting colors within each part). Every closed communicating class is either a monochromatic fixed point or the two-state period-two orbit that alternates the two opposite monochromatic part colorings. The result also gives an exact formula for expected stabilization from *every* initial coloring, including all parity and tie cases.

## Assumptions and scope

Let \(V=A\sqcup B\), with \(|A|=a\ge1\), \(|B|=b\ge1\), and an edge between every vertex of \(A\) and every vertex of \(B\), and no other edges. At each integer time, all vertices update simultaneously to the strict majority color in their open neighborhood. If the neighborhood has equally many vertices of both colors, the updating vertex independently chooses each color with probability \(1/2\). Choices are independent across vertices and rounds. Time zero is the given coloring. Let \(x\in\{0,\ldots,a\}\) and \(y\in\{0,\ldots,b\}\) be the initial numbers of blue vertices in the two parts.

For \(s\ge1\), define the fair-binomial tie and monochromatic probabilities

\[
p_s=\begin{cases}\binom{s}{s/2}2^{-s},&s\text{ even},\\0,&s\text{ odd},\end{cases}\qquad q_s=2^{1-s}.
\]

Write \(p=p_a\), \(q=p_b\), \(u=q_a\), \(v=q_b\), and \(D=1-pq>0\). Define

\[
T_A=\frac{2-q-v+q(2-p-u)}D,\qquad
T_B=\frac{2-p-u+p(2-q-v)}D,
\]

and

\[
T_{AB}=\frac{2-p-q+pq-uv+p(1-q)T_A+(1-p)qT_B}{D}.
\]

The exact expected time \(H_{a,b}(x,y)\) to enter a closed communicating class is

\[
H_{a,b}(x,y)=\begin{cases}
0,&x\in\{0,a\}\ \text{and}\ y\in\{0,b\},\\
T_{AB},&2x=a\ \text{and}\ 2y=b,\\
T_A,&2x=a\ \text{and}\ 2y\ne b,\\
T_B,&2y=b\ \text{and}\ 2x\ne a,\\
1,&\text{otherwise}.
\end{cases}
\]

The cases occur in the displayed order; the first case is never a tie when \(a,b\ge1\). In a graph with an odd-sized part, ties cannot occur in that part. All expressions are rational and defined at every permitted pair of sizes.

## Proof

**Step 1: reduction to a four-corner absorbing set.** In each round every vertex in \(A\) sees the same blue-neighbor count \(y\), and every vertex in \(B\) sees \(x\). If neither count is tied, both parts become monochromatic after one round. The four configurations where each part is monochromatic form exactly three closed communicating classes: all blue, all white, and the two-state orbit that alternates \(A\)-blue/\(B\)-white with \(A\)-white/\(B\)-blue. All other configurations are transient: from two tied parts there is positive probability of making both parts monochromatic at the next step; from one tied part, the other part becomes monochromatic and there is positive probability that the randomizing part does too; from no tied part, a corner is reached deterministically. Finite-state repetition therefore gives almost-sure absorption with finite mean.

**Step 2: three first-step equations.** A randomizing part of size \(s\) produces a tie with probability \(p_s\), a monochromatic coloring with probability \(q_s\), and a nonmonochromatic, nontied coloring with probability \(1-p_s-q_s\). Let \(T_A\), \(T_B\), and \(T_{AB}\) be the expectations from states in which precisely \(A\), precisely \(B\), or both parts are tied. A nontied noncorner state takes one more round; a corner takes none. Consequently

\[
\begin{aligned}
T_A&=2-q-v+qT_B,\\
T_B&=2-p-u+pT_A,\\
T_{AB}&=2-p-q+pq-uv+p(1-q)T_A+(1-p)qT_B+pqT_{AB}.
\end{aligned}
\]

Solving the first two equations and then the third gives exactly the displayed rational formulas. Since \(p_s\le1/2\), the determinant \(D\) is at least \(3/4\). The first-step system, together with the absorbing boundary, uniquely determines expected stabilization, proving the full census.

**Step 3: short exact verification of the finite parameter region.** If at least one part size is odd, its tie probability is zero; every attainable noncorner expectation is at most \(2\), so such a graph cannot maximize the bound. For even \(a,b\le40\), exact-rational evaluation of the three formulas over every one of the \(20^2=400\) ordered size pairs proves that the maximum is \(79/27\), achieved only when \((a,b)=(2,6)\) or \((6,2)\), in the doubly tied state. This is a finite, exhaustive parameter certificate on the stated rectangle, implemented without floating-point arithmetic in `verify.py`.

**Step 4: analytic bound outside the finite rectangle.** For even \(s=2m\), the central binomial probability is decreasing in \(m\), because \(p_{2m+2}/p_{2m}=(2m+1)/(2m+2)<1\). Moreover, the exact inequality \(8\binom{42}{21}<2^{42}\) gives \(p_s<1/8\) for all even \(s\ge42\). Always \(p_s\le1/2\), while \(q_s\ge0\). Suppose, without loss of generality, that \(b\ge42\) is even. The three first-step equations are monotone in the tie probabilities and antitone in the monochromatic probabilities when tested against any vector \((X,Y,Z)\) with \(X,Y\ge1\) and \(Z\ge\max(X,Y)\): for the both-tied equation, its derivatives with respect to \(p,q\) are \((1-q)(X-1)+q(Z-Y)\) and \((1-p)(Y-1)+p(Z-X)\), both nonnegative. The other two equations have the same one-sided monotonicity.

Set the worst-case majorants \(p=1/2\), \(q=1/8\), and \(u=v=0\). Their exact first-step fixed point is

\[
(X,Y,Z)=\left(\frac{11}{5},\frac{13}{5},\frac{41}{15}\right).
\]

These values meet the stated order conditions. The monotone transient Bellman operator and almost-sure absorption imply that the true expectations are no larger, componentwise, than this supersolution. In particular, \(H_{a,b}(x,y)\le41/15<79/27\) whenever an even part has size at least \(42\). The same argument applies with the parts exchanged. Combined with Step 3 and the odd-size cases, this proves the sharp global bound, including uniqueness of the equality size pairs and tie-state condition.

## Verification

The standalone Python 3 standard-library program `verify.py` checks all expected-time Bellman equations directly against the full binomial count-state transition kernel for each \(1\le a,b\le8\). It also enumerates all \(400\) ordered even-size parameter pairs with \(2\le a,b\le40\) in exact rational arithmetic, proves the central-binomial cutoff inequality by integers, and checks the exact rational Bellman supersolution on the infinite tail. The stored script prints `VERIFY_OK` only after every assertion passes.

As a worked sharpness check, on \(K_{2,6}\) the three tie-state expectations are \(T_A=7/3\), \(T_B=13/6\), and \(T_{AB}=79/27\). An initial coloring with one blue vertex in the two-vertex part and three blue vertices in the six-vertex part attains the maximum.

## Relationship to prior work

Zehmakan (2023) introduced and studied the synchronous random-majority model with independent uniform tie-breaking, showing that stabilization can be exponentially slow on unrestricted graphs and analyzing cycles. The expanded open-access 2024 article proves the same general and cycle conclusions. Neither inspected work gives the explicit complete-bipartite expected-time classification or the sharp global \(79/27\) constant. The latter cannot be inferred from either an unrestricted exponential lower-bound example or a cycle-specific asymptotic upper bound. Deterministic majority dynamics with tie retention and parity-update automata are different processes and do not imply this result.

## Limitations

This is a theorem for synchronous random-majority updating on complete bipartite graphs, not for arbitrary bipartite graphs, directed or weighted interactions, asynchronous updating, or biased tie-breaking. The sharp constant is an expectation, not a deterministic upper bound on every sample-path duration: ties can recur for arbitrarily many rounds with positive probability. The finite checker does not substitute for the analytic infinite-size tail argument. A complete bibliographic priority guarantee is unavailable; obscure unpublished or unindexed equivalent statements may exist. No independent external audit has been performed.

## References

1. Ahad N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1, publicly submitted 2023-02-14. https://arxiv.org/html/2302.06760v1
2. Ahad N. Zehmakan, *Majority opinion diffusion: when tie-breaking rule matters*, Autonomous Agents and Multi-Agent Systems 38, article 21 (2024), published 2024-05-20. https://doi.org/10.1007/s10458-024-09651-y
3. Nikolaos Fountoulakis, Mihyun Kang, Tamás Makai, *Resolution of a conjecture on majority dynamics: Rapid stabilization in dense random graphs*, Random Structures & Algorithms 57 (2020), 1134–1156. https://doi.org/10.1002/rsa.20970 (uses deterministic tie retention rather than random ties).
