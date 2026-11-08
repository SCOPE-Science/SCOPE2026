# Prime-power state spectrum for separating two-block reversals

## Finding
For any positive integers \(a,b\), let \(u=0^{a}1^{b}\) and \(v=1^{b}0^{a}\). A *permutation automaton* means a complete deterministic binary automaton in which each letter acts as a permutation of the state set. Let \(s(a,b)\) be the least number of states of such an automaton that accepts exactly one of \(u,v\). Put
\[
 d(t)=\min\{j\in\mathbb Z:j\ge2,\ j\nmid t\}.
\]
Then
\[
\boxed{\ s(a,b)=\max\{d(a),d(b)\}+\mathbf{1}_{\{d(a)=d(b)\in\{2,3,4\}\}}.\tag{1}
\]
Furthermore, the *entire attainable state-count spectrum*, as \(a,b\) range over positive integers, is precisely
\[
\boxed{\ \{s(a,b):a,b\ge1\}=\{p^e:p\text{ prime},\ e\ge1,\ p^e\ge3\}.\ }\tag{2}
\]
In particular no two-block reversal pair requires exactly six, ten, twelve, or any other non-prime-power number of states in this model.

## Assumptions and scope
The alphabet is fixed as \(\{0,1\}\); \(a,b\) are independently arbitrary positive integers. Automata may have any designated initial state and arbitrary accepting subset; every transition must be a bijection. The size measures *all states of a complete DFA*, whether reachable or not, and the optimum can always be realized using a start state that distinguishes the two words. Equation (1) is not a claim about arbitrary deterministic or nondeterministic automata, nor about two nonconjugate block patterns.

## Proof
**1. Reduction to a symmetric-group commutator.** For an \(n\)-state permutation automaton the two letters induce \(x,y\in S_n\). The evaluations of the words are \(x^a y^b\) and \(y^b x^a\). If they differ as permutations, a point has different images, so declaring exactly one of the images accepting separates the words. Conversely equal evaluations can never be separated. Thus the words are separable at size \(n\) exactly when some \(a\)-th power and some \(b\)-th power in \(S_n\) do not commute.

**2. Power-generated normal subgroups.** Define
\[
H_t(n)=\langle x^t:x\in S_n\rangle.
\]
This is a normal subgroup. It is nontrivial if and only if \(d(t)\le n\): the order of every permutation of \(n\) points divides \(L_n=\operatorname{lcm}(1,\ldots,n)\), and \(L_n\mid t\) exactly when every integer \(1\le j\le n\) divides \(t\). If \(j\le n\) does not divide \(t\), a \(j\)-cycle has a nonidentity \(t\)-th power.

For \(n\ge5\), every nontrivial normal subgroup of \(S_n\) contains \(A_n\). For completeness, this familiar consequence of the simplicity of \(A_n\) follows because \(N\cap A_n\) is either \(1\) or \(A_n\). In the first case, \([N,A_n]\subseteq N\cap A_n\) is trivial, but the centralizer of \(A_n\) in \(S_n\) is trivial: a permutation commuting with all three-cycles preserves every three-element support and therefore fixes every point. Hence \(N=1\). Since \(A_n\) is nonabelian, the two subgroups \(H_a(n)\) and \(H_b(n)\) cannot centralize each other when both are nontrivial. Therefore, for every \(n\ge5\), separation occurs exactly when
\[
n\ge\max\{d(a),d(b)\}.\tag{3}
\]
Indeed, if all \(a\)-th and \(b\)-th powers commuted, their generated normal subgroups would centralize one another, contradicting their shared nonabelian subgroup \(A_n\).

**3. Exact low-degree exceptions.** The groups \(S_1,S_2\) are abelian. For \(S_3\), the power-generated subgroup \(H_t(3)\) is \(S_3\) if \(t\) is odd, is \(A_3\) if \(t\) is even but \(3\nmid t\), and otherwise is trivial. Two nontrivial such subgroups fail to centralize exactly when at least one is \(S_3\). In terms of \(d\), separation in degree three occurs exactly for \((d(a),d(b))\in\{(2,2),(2,3),(3,2)\}\).

For \(S_4\), the successive possibilities for \(H_t(4)\) are \(S_4\), \(A_4\), the normal Klein four-group \(V_4\), and \(1\), according as \(d(t)\) is \(2\), \(3\), \(4\), or at least \(5\). Among pairs of nontrivial such subgroups the only mutually centralizing pair is \((V_4,V_4)\): \(V_4\) is abelian, while an appropriate transposition or three-cycle fails to commute with a double transposition, and the groups containing \(A_4\) do not centralize \(A_4\). Consequently, separation in degree four occurs iff \(\max\{d(a),d(b)\}\le4\) and \((d(a),d(b))\ne(4,4)\). Combining these cases with (3) gives (1), including the coincident exceptional pairs \((2,2),(3,3),(4,4)\).

**4. Exact spectrum.** Every least nondivisor \(d(t)\) is a prime power. For if \(d(t)\) had at least two distinct prime factors, its maximal prime-power factors would be proper smaller divisors of \(d(t)\). Each would divide \(t\), hence so would their least common multiple \(d(t)\), a contradiction. The correction in (1) only changes values \(2\mapsto3\), \(3\mapsto4\), and \(4\mapsto5\), which are all prime powers. All outputs are therefore prime powers at least three.

Conversely, degrees three and four are obtained by choosing \((a,b)=(1,1)\) and \((a,b)=(2,2)\), respectively. For any prime power \(q\ge5\), set \(a=b=\operatorname{lcm}(1,\ldots,q-1)\). Every positive integer below \(q\) divides this exponent, whereas \(q\) does not: if \(q=p^e\), the largest power of \(p\) below \(q\) contributes at most \(p^{e-1}\) to that least common multiple. Thus \(d(a)=d(b)=q\), and (1) yields \(s(a,b)=q\). This proves (2).

## Verification
A standalone, Python-standard-library-only checker is supplied in `checker.py`. Run `python3 checker.py` from the extracted package directory. It independently enumerates all permutations of degrees one through five for every exponent pair from one through twenty-four, evaluates both power products and tests commutation. It also checks nine degree-six boundary cases and 19,999 direct arithmetic instances. The actual replay produced `PASS: all 2889 symmetric-group cases and 19,999 arithmetic cases`. These finite tests are checks of the implementation and low-degree boundaries, not substitutes for the infinite proof above.

## Relationship to prior work
The word-separation problem and its equivalence with symmetric-group identities are established in Demaine, Eisenstat, Shallit, and Wilson (2011), Section 8, and Bulatov, Karpova, Shur, and Startsev (2016/2017). Bulatov et al. explicitly record the classical \(S_3\) identity \(x^2y^2=y^2x^2\). Their Proposition 15 treats the distinct alternating-block identities \((xy)^a(yx)^b=(yx)^b(xy)^a\), not a general exact state formula for the pure-block pair in (1). Xu and Regan (2026) improve asymptotic worst-case lower bounds using positive identities and covers of permutation orders; its inspected results do not give (1)–(2). The 2021 Karpova–Shur article characterizes other numerical classes of positive identities, but its entire text was not available in the inspected sources, so implicit prior coverage there remains a priority risk.

## Limitations
The exact result concerns precisely two swapped homogeneous letter blocks and permutation DFAs. It does not resolve worst-case separation over unrestricted word pairs, non-permutation automata, or arbitrary longer run patterns. The argument uses standard simplicity of alternating groups for degree at least five. Historical priority beyond the inspected full texts, especially any unexamined classification in the 2021 literature, is not certified; no independent validation was performed.

## References
- C. Xu and K. Regan, *An Improved Lower Bound for Separating Words by Permutation Automata*, arXiv:2610.11098, first public 2026-10-08. https://arxiv.org/abs/2610.11098
- A. A. Bulatov, O. Karpova, A. M. Shur, and K. Startsev, *Lower Bounds on Words Separation: Are There Short Identities in Transformation Semigroups?*, arXiv:1609.03199, 2016. https://arxiv.org/html/1609.03199v1
- E. D. Demaine, S. Eisenstat, J. Shallit, and D. A. Wilson, *Remarks on Separating Words*, arXiv:1103.4513, 2011. https://arxiv.org/html/1103.4513v1
- O. Karpova and A. M. Shur, *Words Separation and Positive Identities in Symmetric Groups*, Journal of Automata, Languages and Combinatorics **26** (2021), 67–89. Publisher abstract: https://jalc.de/issues/2021/issue_26_1-2/abs-067.pdf
