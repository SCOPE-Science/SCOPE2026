# Variable-free LoopPDL separates every finite functional orbit: exact bounded expressivity spectra

## Finding

Fix \(n\ge1\). A pointed finite model has at most \(n\) worlds, no propositional variables, and one atomic program \(a\), interpreted as a partial function: each world has zero or one \(a\)-successor. It may contain unreachable worlds. Programs are built forward from \(a\) with composition, union, Kleene star and tests of formulas; modalities are Boolean connectives, \(\langle\pi\rangle\), and optionally \(\operatorname{loop}(\pi)\), where loop asserts return to the present world by a \(\pi\)-path. Converse, program intersection, extra actions and universal modalities are excluded.

Each root's forward orbit is either a terminating chain with \(h\ge0\) edges or a lasso with preperiod \(t\ge0\) and unique cycle length \(d\ge1\). **Two roots have the same variable-free LoopPDL theory if and only if their terminating lengths coincide, or their lasso pairs \((t,d)\) coincide.** There are exactly

\[
 L_n=n+\sum_{d=1}^n(n-d+1)=\frac{n(n+3)}2
\]

pointed types, and the Boolean algebra of formula meanings has exactly \(2^{L_n}\) elements. Plain PDL without the loop operator has exactly \(n+1\) types and \(2^{n+1}\) meanings: the \(n\) terminating distances, plus one universal nonterminating type. In particular for \(n=6\), LoopPDL has \(27\) types and \(134{,}217{,}728\) meanings, against plain PDL's \(7\) types and \(128\) meanings.

## Assumptions and scope

Standard PDL path semantics is used: \(a^k\) means \(k\)-fold composition, \(a^0\) abbreviates the identity test \(\top?\), and \(a^+=a;a^*\). The formula \(\operatorname{loop}(\pi)\) holds at \(w\) iff \((w,w)\) is in the interpreted program relation. Formula tests \(\varphi?\) are permitted even when \(\varphi\) itself contains a loop; each syntax tree remains finite. No propositions, converse or global actions occur. A terminating type \(\operatorname{end}(h)\) has \(h+1\) distinct worlds and is realizable precisely when \(h+1\le n\). A lasso type \(\operatorname{cycle}(t,d)\) has \(t+d\) distinct worlds and is realizable precisely when \(t+d\le n\). Unreachable worlds do not influence formula truth in this forward-only language.

## Proof

**Structure.** Iterating a partial function from a root either reaches a world without a successor after \(h\) steps, or first repeats a previously visited world. In the latter case the forward-generated pointed structure is a transient chain of \(t\) worlds feeding into a unique simple directed cycle of \(d\) worlds. All types listed under the size bounds occur, and different type labels have nonisomorphic rooted forward components.

**Separating formulas.** For terminating roots define

\[
 \Theta_h=\langle a^h\rangle\top\wedge\neg\langle a^{h+1}\rangle\top.
\]

This is true exactly when the path stops after \(h\) edges. For \(d\ge1\), define

\[
 P_d=\operatorname{loop}(a^d)\wedge \bigwedge_{\substack{e\mid d\\1\le e<d}}\neg\operatorname{loop}(a^e).
\]

An empty conjunction means \(\top\). Since a finite partial-function orbit returns to its present point in \(d\) steps iff that point lies on a cycle whose least period divides \(d\), \(P_d\) holds exactly on the cycle vertices of least period \(d\). Put

\[
 \Lambda_{0,d}=P_d,\qquad
 \Lambda_{t,d}=\langle a^t\rangle P_d\wedge\neg\langle a^{t-1}\rangle\operatorname{loop}(a^+)\quad(t\ge1).
\]

For \(t\ge1\), the first conjunct says that the vertex at time \(t\) lies on a cycle of period \(d\); the second says that the vertex at time \(t-1\) is not on any cycle. Thus \(\Lambda_{t,d}\) defines exactly the lasso type \((t,d)\). The listed characteristic formulas distinguish every pair of different types.

**Invariance.** Equal types have isomorphic pointed forward-generated components. Structural induction on mutually defined programs and formulas shows that the relation of every permitted regular program (including tests) and the truth of every Boolean/diamond/loop formula are preserved under the isomorphism. Therefore neither unseen worlds nor additional syntactic nesting can distinguish roots of the same type.

**Comparison without loops.** Each terminating type remains characterized by \(\Theta_h\). Every forward-generated nonterminating component is serial, and any two such components are bisimilar via the full Cartesian relation on their reachable worlds: all related worlds have exactly one successor and no atom labels. Standard bisimulation invariance, proved by simultaneous structural induction (including stars and tests), gives the same PDL theory at all such roots. Nonterminating roots alone satisfy \([a^*]\langle a\rangle\top\), separating them from terminating roots. Hence precisely \(n+1\) PDL types exist.

**Counting meanings.** The characteristic formulas for the respective finite type sets, combined by arbitrary finite disjunction, define every subset of that set. Formulas cannot distinguish points within a type. Therefore the meaning algebras have exactly \(2^{L_n}\) and \(2^{n+1}\) elements.

## Verification

Run the standalone standard-library program `verification/checker.py`. It evaluates the relations of program composition, star, tests, and loop directly, and checks that every characteristic formula uniquely recognizes its intended canonical orbit through eight worlds. Independently it exhaustively enumerates \((n+1)^n\) labelled partial functions and all their roots for each \(1\le n\le5\), establishing the expected finite orbit-type census. The five-world enumeration tests \(7{,}776\) functions and \(38{,}880\) roots. The general proof does not depend on this finite experiment.

## Relationship to prior work

Bednarczyk and Swoboda's 2026 study establishes restricted finite-satisfiability results for dynamic logic with a loop operator and gives the precise semantics of return tests. Its main results concern cactus-like unravellings and finite model construction, not an exact semantic quotient for bounded finite partial functions. Standard PDL bisimulation invariance accounts for the ordinary PDL collapse but does not itself imply the LoopPDL period/preperiod isolating formulas or the formula-algebra count. The deterministic orbit decomposition is elementary prior mathematical structure and is not presented as a newly discovered general fact.

## Limitations

The theorem concerns only finite forward partial-function models with one action and no propositional variables. Branching frames, converse, intersections, extra actions, minimal formula length, and unrestricted finite satisfiability remain outside scope. An equivalent treatment of this exact special case in unindexed historical literature cannot be ruled out; novelty is a conclusion relative to inspected sources, not an independent priority certificate.

## References

1. Bartosz Jan Bednarczyk and Mikołaj Swoboda, *Towards Finite Satisfiability of PDL with Loops*, arXiv:2610.15632v1 (first public version October 11, 2026). https://arxiv.org/abs/2610.15632
2. *Propositional Dynamic Logic*, Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/logic-dynamic/
