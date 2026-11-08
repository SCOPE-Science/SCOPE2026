# Exact maximizers of order-preserving two-state probabilistic automata

## Finding
Let \(\Sigma\) be a finite alphabet of size \(q\ge 2\), and let \(n\ge1\). Call a two-state probabilistic finite automaton **order-preserving** if every letter has a row-stochastic transition matrix with nonnegative determinant. A word \(w\in\Sigma^n\) is *isolated* by the automaton if its acceptance probability is strictly larger than that of every other word in \(\Sigma^n\).

**Theorem.** A word is isolated by some order-preserving two-state probabilistic finite automaton if and only if all of its maximal constant runs have *pairwise distinct* symbols. Every such word admits an isolating automaton whose transition matrices have strictly positive entries, strictly positive determinants, rational entries, a deterministic initial state, and a single accepting state.

Consequently, the exact number of length-\(n\) isolatable words over a fixed \(q\)-letter alphabet is
\[
N_q(n)=\sum_{m=1}^{\min(q,n)}\frac{q!}{(q-m)!}\binom{n-1}{m-1}.
\]
In the unrestricted probabilistic automatic complexity of Gill, each of these words has \(A_P(w)=2\); the converse is **not** asserted for unrestricted machines, which may have negative-determinant transitions.

## Assumptions and scope
A two-state machine has row-stochastic matrices
\[
P_a=\begin{pmatrix}p_a&1-p_a\\q_a&1-q_a\end{pmatrix},\qquad 0\le p_a,q_a\le1,
\]
with initial probability distribution over the states and a nonempty, proper set of accepting states. If \(x\) is the probability of state 1, reading \(a\) gives the affine update
\[
f_a(x)=q_a+(p_a-q_a)x,
\]
and \(\det P_a=p_a-q_a\). Thus order preservation is precisely \(f_a\) being nondecreasing. Acceptance is either \(x\) or \(1-x\). The word length and finite input alphabet are fixed when comparing acceptance probabilities; an isolating machine may depend on the target word. The empty word is excluded.

## Proof
**Necessity.** For acceptance in state 1, define \(F(x)=\max_{a\in\Sigma}f_a(x)\). Since all \(f_a\) are nondecreasing, \(F\) is nondecreasing. Any input of length \(j\) produces a state-1 probability at most \(F^{\circ j}(x_0)\); equality is reached by greedily selecting a maximizing letter at each step. If a word uniquely attains the final maximum, then at every point on its trajectory its chosen letter is the *unique* maximizer: otherwise replacing that letter by a larger-valued alternative (or a tied one) yields an equal or better final result, violating uniqueness. Therefore its trajectory is \(x_j=F(x_{j-1})\).

The orbit \((x_j)_{j=0}^{n}\) is monotone: the sign of \(x_1-x_0\), together with monotonicity of \(F\), inductively fixes the sign of all subsequent steps. The graph of \(F\) is the upper envelope of affine functions. When distinct affine functions are uniquely active at \(x<y\), their slopes are strictly increasing in the order of their active positions: the inequalities \(f_a(x)>f_b(x)\) and \(f_b(y)>f_a(y)\) imply \(\operatorname{slope}(f_a)<\operatorname{slope}(f_b)\). In a decreasing orbit the slope order reverses. Thus the sequence of active letter slopes is monotone and different active letters have different slopes. A letter cannot recur after a different letter has intervened. If state 2 is accepting, replace \(F\) by the lower envelope \(H(x)=\min_a f_a(x)\). Its orbit is again monotone, and the analogous inequalities reverse the slope ordering, with the same conclusion. Selecting both or neither state as final would yield constant acceptance and cannot isolate a word over \(q\ge2\).

**Sufficiency, with an explicit rational witness.** Write
\[
w=a_1^{r_1}a_2^{r_2}\cdots a_m^{r_m},\qquad r_i\ge1,\quad a_i\ne a_j\ (i\ne j),\quad \sum_i r_i=n.
\]
Set \(\kappa=1/(4n)\), \(c=\kappa/2\), \(r=1-\kappa\), and \(\epsilon=1/(10000n^4)\). Let
\[
B_j=\frac{1-r^j}{2}\quad(0\le j\le n),\qquad Q_i=\sum_{h=1}^i r_h\quad(1\le i<m),
\]
and place the switch thresholds at
\[
T_i=\frac{B_{Q_i-1}+B_{Q_i}}2\qquad(1\le i<m).
\]
For each used symbol \(a_i\), define
\[
f_{a_i}(x)=\left(r+(i-1)\epsilon\right)x+c-\epsilon\sum_{h<i}T_h.
\]
For each unused alphabet symbol choose \(f_*(x)=(c/8)(1+x)\). These are legitimate two-state stochastic transitions: every map is strictly increasing, its value at \(0\) is positive, and its value at \(1\) is less than \(1\). Indeed \(0<T_h<1/2\), so each used map has intercept at least \(c-\epsilon n/2>c/2\), and its value at \(1\) is at most \(1-\kappa/2+\epsilon n<1\); the unused maps take values between \(c/8\) and \(c/4\). Set the initial state-1 mass to \(0\) and accept state 1.

Adjacent used maps satisfy
\[
f_{a_{i+1}}(x)-f_{a_i}(x)=\epsilon(x-T_i).
\]
Because \(T_1<\cdots<T_{m-1}\), the upper envelope has \(f_{a_i}\) as its unique active line on \((T_{i-1},T_i)\), with the first and last intervals unbounded on the appropriate side. The unused maps are strictly below all used maps on \([0,1]\).

The common baseline \(g(x)=rx+c\), starting at \(0\), reaches \(B_j\) after \(j\) letters. Its consecutive spacings satisfy
\[
B_j-B_{j-1}=\frac{\kappa r^{j-1}}2\ge\frac{3}{32n}\quad(1\le j\le n),
\]
using \(r^n\ge1-n\kappa=3/4\). Each used map differs from \(g\) by at most \(2\epsilon n\) on \([0,1]\), so the greedy orbit \(x_j\) satisfies
\[
|x_j-B_j|\le2\epsilon n^2=\frac{1}{5000n^2}<\frac{3}{64n}.
\]
Each threshold lies midway between consecutive baseline points. The displayed strict error bound therefore places \(x_{j-1}\) inside the unique active interval for the symbol occupying position \(j\) in \(w\), for every \(1\le j\le n\). Thus greedy maximization spells precisely \(w\), with strict inequality against every alternative at its first deviation; strict monotonicity of the upper envelope preserves this inequality to the end. Hence \(w\) is uniquely isolated. All construction data are rational, and the associated stochastic matrices have strictly positive entries and determinants.

**Counting.** For precisely \(m\) distinct runs, there are \(q!/(q-m)!\) ordered choices of distinct run labels and \(\binom{n-1}{m-1}\) compositions of \(n\) into positive run lengths. Summing over \(m\) gives the stated expression.

## Verification
The included `checker.py` reconstructs the rational affine witnesses, checks stochastic endpoints and strict active-letter optimality at every step for 162 distinct run-length profiles of total length at most eight, and compares against every competing word for each of those profiles of length at most six. The checker also verifies the exact enumerator in 28 small alphabet-length cases. A separate exact rational grid audit samples 1,750 length-and-machine cases of three-letter two-state order-preserving machines (both possible single accepting states), of which 1,027 have unique maximizers; all satisfy the necessary run condition. These are finite corroborations. The all-length statements follow from the inequalities and envelope proof above, not extrapolation.

Run `python checker.py` with Python 3.10+; only standard-library packages are required for the checker.

## Relationship to prior work
Gill, *Probabilistic automatic complexity of finite strings* (arXiv:2402.13376; first posted February 20, 2024), introduces the statistic and classifies binary words admitting arbitrary two-state witnesses. That binary classification includes two-block words but also certain alternating patterns, compatible with negative-determinant transitions. Its §4.4 discusses embedding binary witnesses into larger ambient alphabets; that is distinct from classifying words which use three or more symbols.

Kjos-Hanssen, *Every string has probabilistic automatic complexity at most three* (arXiv:2607.26275; first posted July 28, 2026), proves a universal three-state upper bound for arbitrary alphabets. It does not in the accessible portions examined establish this order-preserving two-state classification. The present statement classifies an explicitly defined restricted two-state model, provides strictly positive rational witnesses, and enumerates its attainable words; it is not a claimed classification of unrestricted two-state machines over three or more symbols.

## Limitations
No classification is claimed when some transition determinants are negative; the two-state unrestricted case can isolate additional words. For example, the word \(\mathtt{aba}\) is impossible for this order-preserving class, although the unrestricted binary two-state classification permits it. The maximal gap and fixed-precision complexity of the constructed witnesses are not optimized. The comparison with earlier literature is based on inspected accessible text and searches; an implicit earlier envelope argument cannot be excluded. Independent mathematical assessment has not been performed.

## References
- Kenneth Gill, *Probabilistic automatic complexity of finite strings*, arXiv:2402.13376, first public February 20, 2024. https://arxiv.org/abs/2402.13376
- Bjørn Kjos-Hanssen, *Every string has probabilistic automatic complexity at most three*, arXiv:2607.26275, first public July 28, 2026. https://arxiv.org/abs/2607.26275
