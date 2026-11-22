# A parity-lift dichotomy for three-run scattered-subsequence Moore counters

## Finding

For positive integers \(a,b\), define the binary pattern \(p_{a,b}=0^a1^b0\). Write \(\binom{w}{p}\) for the number of increasing selections of positions of a finite word \(w\) spelling \(p\), counting different selections separately. Let
\[
F_{a,b}(w)=\binom{w}{p_{a,b}}\bmod 2.
\]
A **complete deterministic Moore machine** must output \(F_{a,b}(w)\) after every finite input \(w\), including the empty input. Its state complexity is the number of states of a smallest reachable, complete deterministic machine realizing this output function.

**Theorem.** For every pair \(a,b\ge1\), with \(h=1+\lfloor\log_2 a\rfloor\), the exact minimum number of Moore states is
\[
\boxed{\operatorname{sc}(F_{a,b})=
\begin{cases}
2^{h+b},&b=1\text{ and }a\text{ odd},\\
2^{h+b+1},&\text{otherwise}.
\end{cases}}
\]
Thus appending a final zero to a two-run parity counter doubles its minimal reachable state count **except** when the middle run has length one and the initial zero run has odd length. The result is invariant under exchanging zero and one, giving the corresponding formula for \(1^a0^b1\).

## Assumptions and scope

All inputs are finite binary words; empty input is allowed. The binomial coefficient of words counts scattered *positional occurrences*, not contiguous matches or distinct subsequence values. All parity arithmetic is in \(\mathbb F_2\). The claim concerns output-valued deterministic Moore machines and does not assert the same state count for the separate Boolean acceptor of any prescribed output residue or for nondeterministic automata.

Set
\[
P=2^h,\qquad f(z)=\binom za\bmod2\quad(z\ge0).
\]
By Lucas's theorem, \(f\) depends only on \(z\bmod P\). Its **least** positive period is \(P\): it cannot have period \(P/2\), because \(f(a)=1\) and \(f(a-P/2)=0\), and any period of a function with period \(P\) divides \(P\) after taking the gcd. Here \(P/2\le a<P\).

## Proof

**1. A finite counting machine.** After an input prefix \(w\), let \(z=|w|_0\bmod P\), let
\[
B_j=\binom{w}{0^a1^j}\bmod2\qquad(1\le j\le b),
\]
and put \(C=F_{a,b}(w)\). The initial state is \((0,\mathbf0,0)\). Reading zero and one, respectively, produces the transformations
\[
\begin{aligned}
T_0:(z,B_1,\ldots,B_b,C)&\mapsto(z+1,B_1,\ldots,B_b,C+B_b),\\
T_1:(z,B_1,\ldots,B_b,C)&\mapsto
(z,B_1+f(z),B_2+B_1,\ldots,B_b+B_{b-1},C).
\end{aligned}
\]
For \(b=1\), the middle list is just \(B_1+f(z)\). The formulas follow by partitioning subsequence embeddings according to whether their last position uses the newly read letter. Both transformations are bijections of the finite state set because their affine triangular parts have unit diagonals. The output is \(C\). This establishes the upper bound \(P2^{b+1}\).

**2. Every base state \((z,\mathbf B)\) occurs.** Ignore the coordinate \(C\) temporarily. The zero transformation advances \(z\) and leaves \(\mathbf B\) fixed. Write the one transformation as
\[
\mathbf B\longmapsto M\mathbf B+f(z)e_1,
\]
where \(M=I+N\) and \(N\) has ones immediately below the diagonal, and \(e_1\) is the first standard basis vector. On the base-state space both transformations are permutations of a finite set. Inverses are therefore positive powers and are representable by ordinary input words.

On the fiber \(z=0\), the one transformation acts as \(\mathbf B\mapsto M\mathbf B\), since \(f(0)=0\). A composition that first advances the zero phase by \(a\), reads one, and then reverses the phase advance acts as \(\mathbf B\mapsto M\mathbf B+e_1\), since \(f(a)=1\). Composing this action with the inverse of the original one transformation yields a translation \(\mathbf B\mapsto\mathbf B+M^{-1}e_1\). Conjugation by powers of the one transformation yields translations by \(M^te_1\) for every integer \(t\). The vectors
\[
M^te_1=\bigl(\tbinom t0,\tbinom t1,\ldots,\tbinom t{b-1}\bigr)^\mathsf T\bmod2,
\qquad 0\le t<b,
\]
span \(\mathbb F_2^b\), as their coordinate matrix is lower triangular with diagonal entries one. Hence the stabilizer of the zero phase reaches every \(\mathbf B\). Appending zeros reaches any other phase without changing \(\mathbf B\). Exactly \(P2^b\) base states are thus reachable.

**3. When the final parity is independent of the base.** The transitions never use \(C\) to update \((z,\mathbf B)\), and every suffix acts on \(C\) by adding a function of the base. Consequently, if two words reach the same base but opposite values of \(C\), every reachable base can be reached with both parity values: continue both words by a common input taking their base to the desired target. Such a continuation exists because the base transformations are permutations and the base orbit is transitive.

We now supply the needed pairs of words in all but one parameter regime.

- If \(a\ge2\) and \(b\ge2\), define \(v=0^a1^{b-1}0^{P-a}\). Just after \(v\), the zero phase is \(P\equiv0\pmod P\), \(B_{b-1}=1\), and \(\binom P{a-1}=0\bmod2\). Comparing \(v01\) with \(v10\), the two adjacent-letter orders change \(B_1\) by \(\binom P{a-1}=0\), leave all other base coordinates equal, and change \(C\) by \(B_{b-1}=1\). Thus they reach the same base and opposite outputs.

- If \(a=1\) and \(b\ge2\), let \(r\) be the least power of two satisfying \(r\ge b\), and use
\[
u=0\,1^{r+1}0,\qquad v=1\,0\,1^{r-1}0\,1.
\]
Both contain two zeros. For each \(1\le j\le b\), their \(01^j\) counts modulo two are, respectively, \(\binom{r+1}{j}\) and \(\binom rj+\mathbf1_{j=1}\). Pascal's identity and the power-of-two property show these are equal. Their \(01^b0\) counts are \(\binom{r+1}b\) and \(\binom{r-1}b\), which are opposite modulo two for every \(2\le b\le r\), by Lucas's theorem. Again both parity values occur above the same base.

- If \(b=1\) and \(a\) is even, compare \(0^a01\) with \(0^a10\). They have the same zero phase and the same count of \(0^a1\), since \(\binom{a+1}a=a+1\equiv\binom aa=1\pmod2\). But the count of \(0^a10\) is zero in the first word and one in the second. Hence both parity values occur over every base.

It follows that precisely \(P2^{b+1}\) states are reachable whenever \(b\ge2\) or \(a\) is even.

**4. The exceptional invariant.** Suppose \(b=1\) and \(a\) is odd. For each one-position in \(w\), write \(x\) for the number of zeros before that one and let \(Z=|w|_0\). This position contributes \(\binom xa\) to the \(0^a1\) count and \(\binom xa(Z-x)\) to the \(0^a10\) count. Lucas's theorem says \(\binom xa\equiv1\pmod2\) only when \(x\) is odd, because \(a\) is odd. Thus
\[
C=\sum_{\text{ones}}\binom xa(Z-x)
\equiv(Z-1)\sum_{\text{ones}}\binom xa
\equiv(z-1)B_1\pmod2.
\]
The final parity is uniquely determined by the base. Precisely \(P2^b=P\cdot2\) states are reachable in this exceptional case.

**5. All reachable states are distinguishable.** It remains to prove the constructed accessible states are pairwise inequivalent as Moore states. The empty suffix outputs \(C\). For each \(t=0,1,\ldots,b\), the suffix \(1^t0\) outputs
\[
C+\sum_{j=1}^b\binom t{b-j}B_j+\binom tb f(z)\pmod2.
\]
In ascending order of \(t\), these outputs recover \(B_b,B_{b-1},\ldots,B_1,f(z)\) by a unit-triangular system. Now consider suffixes \(0^r1^b0\). Their outputs are
\[
C+(r\bmod2)B_b
 +\sum_{j=1}^b\binom b{b-j}B_j+f(z+r)\pmod2.
\]
Because \(C\) and all \(B_j\) are known, these outputs recover \(f(z+r)\) for every \(r\ge0\). The exact period \(P\) of \(f\) implies that the length-\(P\) circular shift sequence \(\bigl(f(z+r)\bigr)_{0\le r<P}\) determines \(z\bmod P\) uniquely. Therefore two distinct accessible triples differ in the output of at least one finite suffix; they cannot be merged by any equivalent complete deterministic Moore machine. The number of accessible states computed in Steps 3–4 is exactly minimal. \(\square\)

## Verification

Two independent Python 3 standard-library programs accompany this result. Run `python3 check_prefix_automata.py` and `python3 check_phase_witnesses.py` from the directory containing those files.

The first program constructs the **full pattern-prefix dynamic program**, breadth-first enumerates reachable states for all \(1\le a\le11\), \(1\le b\le6\), and checks the claimed count in 66 cases. It independently minimizes 20 finite Moore machines by partition refinement and performs 65,520 direct positional-subsequence tests on short binary words. The recorded result is in `check_prefix_automata.out`.

The second program uses the separate **phase-and-conditional-count representation**, checks 4,914 explicit witness pairs, verifies that suffix signatures separate every state in 40 finite cases, and checks 877,440 instances of the exceptional parity identity. Its recorded result is in `check_phase_witnesses.out`. The computations test finite cases and supporting identities; the proof above establishes the theorem for all positive integer parameters.

## Relationship to prior work

The 2026 work of Fazekas, Huang and Mercaş [1], first publicly submitted on October 5, studies subsequence universality and pattern containment probabilities inside binary Parikh-matrix equivalence classes. It motivates the formal-language setting, but its arithmetic characterizations and approximation theorem do not give minimal modulo-two output automata for this three-run family. Fazekas and Huang [2] develop generalized Parikh matrices recording subsequence statistics; their construction does not yield the minimum reachable Moore-state count or the exceptional parity invariant.

Černý [3] develops a general algebraic description of Parikh-type mappings and congruences, rather than exact modular minimal-state formulas for these patterns. The earlier trie-automaton construction of Alazemi and Černý [4] counts general scattered subwords by a nondeterministic weighted construction. The complete text of [4] was not available for comparison; it remains a priority-risk source and is not declared disjoint on the basis of its abstract.

A published exact classification for modular \(010\) and \(101\) Moore counters [5] covers the specialization \(a=b=1\), producing four parity states, which agrees with the exceptional branch above. Exact modular results for \(0^a1\) [6] and \(0011\) [7] concern **two-run patterns** and do not determine how a *returning final zero* changes the observable state quotient. The present claim is the infinite two-parameter three-run classification and the necessary-and-sufficient condition for a new final parity degree of freedom; the special cases already known are not claimed independently.

## Limitations

The modulus is fixed at two. The theorem does not cover arbitrary positive moduli, four or more runs, the exact Boolean-DFA size for a specified residue language, nondeterministic state complexity, or restricted input families. A full text of the 2011 trie-automaton paper was not obtained, and some equivalent or stronger historical result may remain unindexed. The computational checks are finite supporting tests and not substitutes for the all-parameter proof. Independent mathematical validation has not been performed.

## References

1. S. Z. Fazekas, X. Huang, R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717, initially public 2026-10-05. https://arxiv.org/abs/2610.06717
2. S. Z. Fazekas and X. Huang, *Generalized Parikh Matrices For Tracking Subsequence Occurrences*, arXiv:2407.04462, initially public 2024-07-05. https://arxiv.org/html/2407.04462v1
3. A. Černý, *Generalizations of Parikh Mappings*, RAIRO Theoretical Informatics and Applications 44 (2010), 209–228. https://www.numdam.org/article/ITA_2010__44_2_209_0.pdf
4. H. M. K. Alazemi and A. Černý, *Counting Subwords Using a Trie Automaton*, International Journal of Foundations of Computer Science 22 (2011), 1457–1469. https://doi.org/10.1142/S0129054111008817
5. *Exact output-state complexity for modular alternating scattered triples*, published published-finding corpus mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-output-state-complexity-for-modular-alternating-scattered--f8d46c1509db
6. *Exact state complexity of modular scattered zero-power–one counts*, published published-finding corpus mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-state-complexity-of-modular-scattered-zero-power-one-count--9df1828ce330
7. *Exact Moore-state complexity of modular scattered \(0011\) counts*, published published-finding corpus mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-moore-state-complexity-of-modular-scattered-0011-counts--f0fa64081c4c
