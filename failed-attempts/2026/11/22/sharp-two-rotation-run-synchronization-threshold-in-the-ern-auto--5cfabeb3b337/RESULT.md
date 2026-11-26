# Sharp two-rotation-run synchronization threshold in the Černý automata

## Finding
For every integer \(n\ge3\), the classical \(n\)-state Černý automaton can be synchronized by a word containing no run of three consecutive rotation letters, but cannot be synchronized by a word containing no run of two consecutive rotation letters. Hence the smallest allowed maximum rotation-run length is **exactly two**, independently of the number of states.

A constructive refinement gives the explicit no-\(aaa\) reset word
\[
N=n-1,\qquad x=ab,\qquad e=aab(ab)^{N-2},\qquad W_n=b\,e\,(xe)^{N-2},
\]
with length \(2n^2-5n+1\). The essential mechanism is that the words \(x,e\) induce a cyclic shift and a predecessor-collapse on the \(n-1\) states left after the first \(b\).

## Assumptions and scope
The state set is \(Q=\{0,1,\ldots,n-1\}\), the alphabet is \(\{a,b\}\), and transitions act left to right:
\[
a(i)=i+1\pmod n,\quad b(0)=1,\quad b(i)=i\text{ for }i\ne0.
\]
A reset word maps all of \(Q\) to a singleton. A run of \(a\)'s is a maximal contiguous string of \(a\)'s. The claim holds for all integer \(n\ge3\), with no parity restriction. An empty run has length zero. The small case \(n=2\) is excluded because \(b\) already synchronizes there.

## Proof
**1. The sharp obstruction with no \(aa\).** Write \(S=\{1,\ldots,n-1\}\) and \(T=Q\setminus\{1\}\). The full state set has \(Qa=Q\) and \(Qb=S\). Moreover \(Sb=S\), \(Sa=T\), and \(Tb=S\), the last equality holding because the zero state is replaced with the missing state one. If a word contains no \(aa\), every application of \(a\) to the image \(S\) must be followed by \(b\) before another \(a\). Therefore along any such word the image is always one of \(Q,S,T\). Its cardinality is at least \(n-1\), which is bigger than one for \(n\ge3\). Thus a reset word must contain \(aa\).

**2. A constrained block action on \(S\).** Let \(N=n-1\) and identify \(S=\{1,\ldots,N\}\). For the block \(x=ab\), direct evaluation gives
\[
i x=\begin{cases}i+1,&1\le i<N,\\1,&i=N.\end{cases}\]
Thus \(x\) is a cyclic permutation of \(S\) of order \(N\). For \(y=aab\), direct evaluation gives \(iy=ix^2\) whenever \(i<N\), while \(Ny=1\) rather than \(Nx^2=2\). Hence, on \(S\), the block \(e=yx^{N-2}=aab(ab)^{N-2}\) fixes all states \(1,\ldots,N-1\), and maps \(N\) to \(N-1\). (At \(N=2\) the exponent is zero and the same identities hold.) This is an opposite-direction collapse relative to the cyclic increment: it is **not** a claim that the induced two-letter automaton is isomorphic to a smaller classical Černý automaton.

**3. Finite induction and word length.** The initial \(b\) maps \(Q\) to \(S\). Applying \(e\) sends \(S\) to the interval \(\{1,\ldots,N-1\}\). If the current image is \(\{j,\ldots,N-1\}\) with \(1\le j\le N-2\), then applying \(xe\) sends it to \(\{j+1,\ldots,N-1\}\): \(x\) rotates it to \(\{j+1,\ldots,N\}\), then \(e\) identifies \(N\) with \(N-1\). After exactly \(N-2\) such blocks the image is the singleton \(\{N-1\}\). Every occurrence of \(a\) is part of \(ab\) or \(aab\), so \(W_n\) contains no \(aaa\). Since \(|x|=2\) and \(|e|=2N-1\),
\[
|W_n|=1+(2N-1)+(N-2)(2N+1)=2n^2-5n+1.
\]
Together with step 1 this proves the exact run threshold two.

**4. Growth of constrained reset length.** Let \(\ell_2(n)\) be the shortest reset-word length when \(aaa\) is forbidden. The classical exact shortest unrestricted reset length of the Černý automaton is \((n-1)^2\), so
\[
(n-1)^2\le\ell_2(n)\le2n^2-5n+1.
\]
Thus \(\ell_2(n)=\Theta(n^2)\). Neither endpoint equality nor an exact formula for \(\ell_2(n)\) is asserted.

## Verification
The standalone `verify.py` computes each transition directly from the displayed definitions. For each integer \(3\le n\le100\), it checks the action of both blocks on every state of \(S\), verifies the length and forbidden factor of \(W_n\), and confirms the resulting image is a singleton. For \(3\le n\le15\), a separately enumerated product of the power-set automaton and a two-state word-constraint monitor explores **all reachable** no-\(aa\) configurations and asserts image rank at least \(n-1\). Run `python3 verify.py` (standard library only). These finite tests supplement, but do not replace, the all-integer proof above.

## Relationship to prior work
Hoffmann (2021, first public version 6 September 2021) studies constrained synchronization of automata with simple idempotents, explicitly including the Černý family, and proves general decision algorithms for small regular constraint automata. Its inspected Section 4 and appendix do not state this precise no-\(aa\)/no-\(aaa\) boundary or the predecessor-collapse block construction. Fernau et al. (2019) establish the general regular-constraint synchronization framework, but not this parameterized threshold. Published related results on optimal unconstrained Černý reset words, weighted letter costs and partial-rank thresholds do not imply existence of a reset word avoiding \(aaa\), because subsequence restrictions and letter-count bounds do not constrain contiguous rotation runs. The precise negative statement under no \(aa\) and constructive positive statement under no \(aaa\) are compared at the level of their mathematical assertions, not merely their keywords.

## Limitations
The bound \(2n^2-5n+1\) is an explicit construction length, **not** a proved optimum under the \(aaa\)-free constraint. The theorem is restricted to the specified standard Černý transition convention and all \(n\ge3\); it is not a classification of other synchronizing automata. Relevant existing algorithms may decide particular constrained-synchronization instances without explicitly supplying this uniform characterization. Unknown earlier equivalent formulations, including under cyclic-monoid or prescribed-input-pattern terminology, remain a historical-priority risk. No independent mathematical audit has been performed.

## References
1. Stefan Hoffmann, *Constrained Synchronization for Commutative Automata and Automata with Simple Idempotents*, arXiv:2109.02743v1, first public 2021-09-06. https://arxiv.org/pdf/2109.02743
2. Henning Fernau, Vladimir V. Gusev, Stefan Hoffmann, Markus Holzer, Mikhail V. Volkov, and Petra Wolf, *Computational Complexity of Synchronization under Regular Constraints*, MFCS 2019, DOI:10.4230/LIPIcs.MFCS.2019.63. https://doi.org/10.4230/LIPIcs.MFCS.2019.63
3. Published related mathematical-record comparisons: `2026/11/8/SCOPE-uniform-weighted-reset-optimality-in-the-ern-automata--6527a70965c4` and `2026/10/13/SCOPE-a-mandatory-reset-subsequence-and-exact-one-step-multiplicity-fo--8a725fd1702c` (published-finding corpus index, statements compared by implication, not assumed independent verification).
