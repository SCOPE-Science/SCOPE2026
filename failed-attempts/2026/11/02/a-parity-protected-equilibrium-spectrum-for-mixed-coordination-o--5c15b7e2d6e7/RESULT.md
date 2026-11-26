# A parity-protected equilibrium spectrum for mixed coordination on complete bipartite networks

## Finding
Consider the binary-action mixed coordination/anti-coordination game on a unit-weight complete bipartite network \(K_{a,b}\), for arbitrary integers \(a,b\ge1\), with common confidence/payoff threshold \(r=1/2\). Every individual either prefers to match the majority action of the opposite part (a coordinator) or prefers the minority action (an anti-coordinator); ties make both actions best responses. Fix any assignment of the two roles, with \(c_A\) coordinators in the part of size \(a\) and \(c_B\) coordinators in the part of size \(b\). Set
\[
 d_A=2c_A-a,\quad d_B=2c_B-b,\qquad
 q(t)=\begin{cases}\binom{t}{t/2},&t\text{ even},\\0,&t\text{ odd}.\end{cases}
\]
The **exact number of labeled pure Nash equilibria**, with the given individual roles held fixed, is
\[
 \boxed{E(a,b;c_A,c_B)=q(a)q(b)+2\mathbf1_{d_A d_B>0}
 +\mathbf1_{d_B=0}\bigl(2^a-q(a)\bigr)
 +\mathbf1_{d_A=0}\bigl(2^b-q(b)\bigr).}
\]
There is no dependence on the positions of the individual role labels within a part, only on their counts. In particular, **every** role assignment has a pure Nash equilibrium if and only if both part sizes are even. In that case the sharp minimum and maximum equilibrium counts over all assignments of roles are, respectively,
\[
 \boxed{\min_{c_A,c_B}E=q(a)q(b),\qquad
 \max_{c_A,c_B}E=q(a)q(b)+2^a-q(a)+2^b-q(b).}
\]
Finally, if each player's role is drawn independently and fairly, the exact probability that the resulting game has at least one pure Nash equilibrium is
\[
 \boxed{\Pr(E>0)=\begin{cases}
 1,&a,b\text{ even},\\
 \tfrac12,&a,b\text{ odd},\\
 \tfrac12+q(e)/2^{e+1},&\text{exactly one of }a,b\text{ even, of size }e.
 \end{cases}}
\]

## Assumptions and scope
The graph is the simple, loopless, unweighted \(K_{a,b}\). Each labeled vertex plays \(x_i\in\{0,1\}\) and has a fixed type \(\delta_i\in\{-1,+1\}\), where \(+1\) denotes a coordinator. For a profile \(x\), the individual utility is
\[
 u_i(x)=\frac{\delta_i}{2}\sum_{j\sim i}
 \bigl[x_i x_j+(1-x_i)(1-x_j)\bigr].
\]
This is the \(r=1/2\), unit-edge-weight specialization of equation (1) in Arditti et al. [1]; the harmless overall factor does not affect equilibria. A pure Nash equilibrium permits indifferent players to retain either action; no strict-equilibrium convention or tie-breaking rule is imposed. Counts distinguish action assignments to labeled vertices, not just the pair of community action totals. All statements hold for every indicated integer size, including a singleton side.

## Proof
Write \(S_A=\sum_{i\in A}(2x_i-1)\) and \(S_B=\sum_{i\in B}(2x_i-1)\). A coordinator in the first part strictly prefers action \(1\) if \(S_B>0\), strictly prefers action \(0\) if \(S_B<0\), and is indifferent when \(S_B=0\). For an anti-coordinator these two strict preferences are reversed; the second part is analogous. This follows directly by subtracting the two utilities, obtaining \(u_i(1,x_{-i})-u_i(0,x_{-i})=\delta_i S_B/2\) in the first part and \(\delta_i S_A/2\) in the second.

Partition the equilibrium profiles into four **disjoint and exhaustive** possibilities according to whether the two integer magnetizations vanish.

1. **Neither vanishes.** When \(S_B>0\), all players in the first part have their uniquely prescribed action, making \(S_A=d_A\); when \(S_B<0\), they instead yield \(S_A=-d_A\). Similarly \(S_B=d_B\operatorname{sgn}(S_A)\) when \(S_A\ne0\). Hence \(\operatorname{sgn}(S_A)\operatorname{sgn}(S_B)=\operatorname{sgn}(d_A)=\operatorname{sgn}(d_B)\). This is possible precisely when \(d_A d_B>0\). In that case there are exactly two action profiles, exchanged by flipping all actions. If either role imbalance is zero, no profile belongs to this case.

2. **\(S_A\ne0\), \(S_B=0\).** The strict majority in the first part uniquely determines all actions in the second, and their magnetization is \(S_B=d_B\operatorname{sgn}(S_A)\). It can vanish exactly when \(d_B=0\). In that event the first part sees a tie and can adopt any of its \(2^a-q(a)\) nonbalanced profiles, each of which fixes a unique equilibrium action profile in the second part.

3. **\(S_A=0\), \(S_B\ne0\).** By symmetry the number is \(\mathbf1_{d_A=0}(2^b-q(b))\).

4. **Both vanish.** Both sides see a tie, so every vertex is indifferent; the number of profiles balanced in each part is precisely \(q(a)q(b)\).

Summing the mutually exclusive cases establishes the exact counting formula. For even \(a,b\), the last term is positive regardless of types, proving universal existence. If at least one side is odd, take every vertex of the first part to be a coordinator and every vertex of the second part to be an anti-coordinator. This gives \(d_A=a>0\) and \(d_B=-b<0\), neither zero, while \(q(a)q(b)=0\), hence no equilibrium. This proves the if-and-only-if parity assertion.

For even \(a,b\), the counting formula is its positive constant term plus nonnegative additions, so the minimum is \(q(a)q(b)\), achieved by the opposite-type assignment just described. The maximum is attained at \(d_A=d_B=0\), where both free-part contributions are present. To check it is globally maximal, note that if only one of these imbalances vanishes, only one of the two free-part terms can appear, and if neither vanishes then the sole possible addition is \(2\), whereas \(2^a-q(a)\ge2\) and \(2^b-q(b)\ge2\) for positive even \(a,b\). Thus no other role assignment gives a larger count.

For the random-role assertion, role imbalance \(d_A\) is symmetric about zero and vanishes with probability \(q(a)/2^a\); the analogous statement holds for \(d_B\), independently. If both sizes are even there is a balanced profile regardless of the role assignment. If both are odd neither imbalance vanishes, and existence is exactly the event that their signs agree, of probability \(1/2\). If exactly one size is even, say \(a=e\), the odd-side imbalance never vanishes: existence happens whenever \(d_A=0\), or with conditional probability \(1/2\) when \(d_A\ne0\). Hence \(\Pr(E>0)=q(e)/2^e+(1-q(e)/2^e)/2=1/2+q(e)/2^{e+1}\). This completes the proof.

## Verification
The standalone standard-library Python script `verify_bipartite_equilibria.py` checks Nash equilibria directly from the two unilateral payoff options for each labeled player, rather than using the magnetization classification for its oracle. Exhaustive enumeration covers every role composition on every \(K_{a,b}\) with \(1\le a,b\le5\). It independently evaluates \(102400\) labeled action profiles in \(400\) composition cases; all count comparisons pass. It also verifies \(25\) sharp minimum/maximum and parity-existence assertions and \(25\) rational probability assertions. Run using `python3 verify_bipartite_equilibria.py`. These finite checks support the construction; the proof above handles arbitrary positive sizes.

## Relationship to prior work
Arditti, Como, Fagnani and Vanelli [1] define the general mixed coordination/anti-coordination game and give graph-theoretic **sufficient** conditions for equilibrium existence and learning convergence. They do not state an all-role equilibrium-count formula for the unweighted complete-bipartite specialization. The earlier all-to-all paper [2] analyzes fully connected populations, whose within-part edges change the best-response structure and therefore do not imply the bipartite formula. Vanelli's earlier thesis [3], including its mixed-game chapter, gives cohesive sufficient conditions and examples on complete graphs or a single anti-coordinator, not the stated bipartite spectrum. The pure-type convergence literature [4] does not cover arbitrary mixed role configurations. The later signed-edge generalization [5] provides conditional cohesive-core existence and best-response stability theorems; neither theorem counts all equilibria of a fixed complete bipartite mixed-role game. The balanced two-coloring count appearing in separate combinatorial work is compatible with the \(q(a)q(b)\) term, but it does not characterize the additional role-dependent equilibrium strata. The novelty claimed here is the **joint exact four-stratum spectrum, sharp role-robust parity boundary, and role-randomized existence law**, not the binomial identity or the general game's definitions.

## Limitations
The result assumes unit edge weights, no within-part edges, uniform threshold \(1/2\), and the standard weak best-response convention at ties. It is not an enumeration for arbitrary bipartite graphs, weighted graphs, heterogeneous thresholds, or dynamically stable equilibria under a specified update rule. The four-stratum proof is elementary; independent priority verification across every specialist source is not established. The exact bibliographic priority of potentially uncatalogued related studies remains uncertain.

## References
[1] L. Arditti, G. Como, F. Fagnani, M. Vanelli, *Equilibria and learning dynamics in mixed network coordination/anti-coordination games* (2021), arXiv:2109.12692v1, first public 2021-09-26. https://arxiv.org/abs/2109.12692

[2] M. Vanelli, L. Arditti, G. Como, F. Fagnani, *On games with coordinating and anti-coordinating agents* (2019 preprint; 2020 journal paper), arXiv:1912.02000. https://arxiv.org/abs/1912.02000

[3] M. Vanelli, *On network games with coordinating and anti-coordinating agents*, Politecnico di Torino master's thesis (2019), https://webthesis.biblio.polito.it/11996/

[4] J. Riehl, P. Ramazi, M. Cao, *Networks of conforming or nonconforming individuals tend to reach satisfactory decisions*, PNAS (2016), https://doi.org/10.1073/pnas.1610244113

[5] M. Vanelli, L. Arditti, G. Como, F. Fagnani, *On Signed Network Games with Binary Actions* (2025 preprint, revised 2026), arXiv:2505.09799, https://arxiv.org/abs/2505.09799
