# Idempotent retractions of binary two-run factor monoids

## Finding

For integers \(r,s\geq 1\), let \(\Sigma=\{0,1\}\), let
\[
L_{r,s}=\Sigma^*0^r1^s\Sigma^*,
\]
and let \(M_{r,s}\) be its syntactic **monoid**, including the identity represented by the empty word. Write
\(E(M)=\{t\in M:t^2=t\}\).
Then
\[
\boxed{
|E(M_{r,s})|=
\begin{cases}
\binom r2+\binom s2+2rs+3,&r,s\geq2,\\
\binom{r+s}{2}+3,&\min(r,s)=1.
\end{cases}}
\]
Every nonidentity idempotent has transformation rank at most two on the minimal recognizing DFA. Exactly one of these has rank one (the absorbing zero); all others have rank two and are explicit retractions sending a specified subset of nonabsorbing states to the sink and every remaining nonabsorbing state to a single fixed state.

For comparison, the known monoid cardinality is \((r+s)^2+rs+1\) when both parameters exceed one, and \((r+s)^2+1\) otherwise [1]. In particular, the fraction of idempotents tends to \(3/5\) along \(r=s\to\infty\) and to \(1/2\) along \(r=1,\ s\to\infty\). More generally, if both parameters grow and \(rs/(r+s)^2\to\theta\), the fraction tends to \((1/2+\theta)/(1+\theta)\).

## Assumptions and scope

The alphabet has exactly two symbols. The specified word must consist of a positive run of zeros followed by a positive run of ones. The empty word belongs to the free monoid but not the recognized language. The invariant counts composition-idempotent **elements** of the syntactic monoid, not idempotent generators, idempotent words, or states of the minimal DFA. Distinct words inducing the same map count once.

Index the minimal DFA's nonabsorbing prefix states by
\(A_i\) for \(0\leq i\leq r\) and \(B_j\) for \(1\leq j<s\); the unique absorbing accepting state is \(Z\). There are exactly \(r+s+1\) states, with \(B_j\) absent when \(s=1\). The transition rules are
\[
\begin{aligned}
A_i\cdot0&=A_{\min(i+1,r)},\\
A_i\cdot1&=\begin{cases}A_0,&i<r,\\B_1,&i=r,\ s\geq2,\\Z,&i=r,\ s=1,\end{cases}\\
B_j\cdot0&=A_1,\\
B_j\cdot1&=\begin{cases}B_{j+1},&j<s-1,\\Z,&j=s-1,\end{cases}
\end{aligned}
\]
with \(Z\cdot0=Z\cdot1=Z\). The initial state is \(A_0\). These are precisely the proper-prefix tracking transitions for recognizing an occurrence of \(0^r1^s\). Every prefix state is reachable; for two proper-prefix states with prefix lengths \(i<j\), the suffix of the pattern after position \(j\) is accepted from state \(j\), but cannot be accepted from state \(i\) because the resulting concatenation is shorter than the whole pattern. Thus the DFA is minimal and its transition monoid is \(M_{r,s}\).

## Proof

Write \(X\) for the set of its \(r+s\) nonabsorbing states. For \(D\subseteq X\) and \(p\in X\setminus D\), define the transformation
\[
T_{D,p}(x)=\begin{cases}Z,&x\in D\cup\{Z\},\\p,&x\in X\setminus D.\end{cases}
\]
It is idempotent because its only image states are the fixed points \(p\) and \(Z\). Different pairs \((D,p)\) yield different transformations whenever \(D\neq X\).

**Case \(r,s\geq2\).** All composition-idempotents are the identity, the all-to-\(Z\) transformation, and the following four disjoint types of \(T_{D,p}\):

1. \(D=\varnothing\), with any \(p\in X\), giving \(r+s\) elements.
2. \(D=H_k:=\{A_{r-k},\ldots,A_r\}\) for \(1\leq k<r\), with any \(p\in X\setminus H_k\), giving \(r+s-k-1\) for each \(k\).
3. \(D=K_k:=\{B_{s-k},\ldots,B_{s-1}\}\) for \(1\leq k<s\), with any \(p\in X\setminus K_k\), giving \(r+s-k\) for each \(k\).
4. \(D=K_*:=\{A_r,B_1,\ldots,B_{s-1}\}\), with any \(p\in\{A_0,\ldots,A_{r-1}\}\), giving \(r\) elements.

All four types occur: a long zero run \(0^r\) maps every state in \(X\) to \(A_r\), and suitable suffixes reach every \(p\in X\); \(0^k1^s\) kills precisely \(H_k\) and maps its complement to \(A_0\), which can then reach every \(p\); \(1^k0\) kills precisely \(K_k\) and maps survivors to \(A_1\); and \(1^s0\) kills precisely \(K_*\) and maps survivors to \(A_1\). Both \(A_0\) and \(A_1\) can reach every state of \(X\) when \(r,s\geq2\), so every listed admissible \(p\) is realizable. The all-to-sink transformation is induced by \(0^r1^s\).

To see that the list is exhaustive, inspect any nonempty input word. A pure zero run shorter than \(r\) is not idempotent, because its image of \(A_0\) is not fixed; a pure sufficiently long zero run belongs to type 1. A pure one run shorter than \(s\) is not idempotent, because it moves a live one-run prefix state; a pure sufficiently long one run belongs to type 4. If the first change of letter is \(0^k1\) with \(k\geq r\), all nonabsorbing states have already merged, giving type 1 or the all-to-sink map. If it is \(0^k1\) with \(1\leq k<r\), the inputs in \(H_k\) map to \(B_1\) and all other inputs in \(X\) to \(A_0\). Unless these two image classes later merge or \(H_k\) reaches the sink, the result cannot be idempotent: any surviving image of \(H_k\) is a \(B\)-state, which itself lies in the other input class and cannot be fixed. A merging result has type 1 or is zero; a killed high class has type 2. Finally, if the word starts with ones and later first contains a zero, that prefix is \(1^k0\). Its killed domain is exactly \(K_k\) for \(k<s\), or \(K_*\) for \(k\geq s\), and all surviving inputs have merged at \(A_1\). These produce types 3 and 4 or zero. All longer suffixes preserve this classification. No other idempotent is possible.

The total is
\[
2+(r+s)+\sum_{k=1}^{r-1}(r+s-k-1)
+\sum_{k=1}^{s-1}(r+s-k)+r
=\binom r2+\binom s2+2rs+3.
\]
All listed nonidentity nonzero elements have image \(\{p,Z\}\).

**Case \(s=1\), \(r\geq2\).** There are no \(B\)-states. The identity and zero occur once each. The possible nonzero nonidentity idempotents are exactly: \(T_{\varnothing,A_r}\); \(T_{H_k,p}\) with \(1\leq k<r\) and \(p\in\{A_0,\ldots,A_{r-k-1}\}\); and \(T_{\{A_r\},p}\) with \(p\in\{A_0,\ldots,A_{r-1}\}\). Words starting with \(0^k1\) provide the first killed-domain family, words starting with \(1\) provide the last, and \(0^r\) provides the no-kill map. Other words either merge all live states or are not idempotent, by the same first-letter-change argument. Their number is
\[
2+1+\sum_{k=1}^{r-1}(r-k)+r
=\binom{r+1}{2}+3.
\]

**Case \(r=1\), \(s\geq2\).** In the displayed DFA, an initial zero immediately merges all nonabsorbing states to \(A_1\). Initial ones followed by the first zero kill a terminal block of \(B\)-states and merge all survivors at \(A_1\). Inspecting the remaining all-one words gives exactly these nontrivial nonzero idempotents: \(T_{\varnothing,p}\) for any \(p\in\{A_1,B_1,\ldots,B_{s-1}\}\) (giving \(s\)); \(T_{K_k,p}\) with \(K_k=\{B_{s-k},\ldots,B_{s-1}\}\) for \(1\leq k<s\) and \(p\in\{A_1,B_1,\ldots,B_{s-k-1}\}\) (giving \(s-k\)); and \(T_{\{A_1,B_1,\ldots,B_{s-1}\},A_0}\) (giving one). Along with identity and zero the number is
\[
2+s+\sum_{k=1}^{s-1}(s-k)+1=\binom{s+1}{2}+3.
\]
This independently agrees with reversal duality: reversing the factor and interchanging alphabet symbols gives \(0^s1\), whose syntactic monoid is anti-isomorphic to the one in the previous case, preserving idempotency. All nonidentity nonzero cases again have rank two. If \(r=s=1\), its three-state automaton has five transformation elements and exactly four idempotents (identity, zero and two rank-two retractions), agreeing with the formula.

Finally, substituting the known total monoid sizes cited above into these exact counts and retaining the quadratic leading terms proves the stated density limits and their general interpolation.

## Verification

Two standalone, standard-library-only Python programs accompany this result:

- `verify_kmp.py` constructs an independently coded pattern-prefix DFA for each \(1\leq r,s\leq10\), enumerates the entire transition monoid by breadth-first closure, tests the identity \(t\circ t=t\) directly, checks the idempotent-rank assertion and checks the previously known total monoid sizes.
- `verify_forms.py` uses the explicit run-state transition rules instead of a prefix-matching routine, enumerates the entire monoid, constructs all listed \(T_{D,p}\) forms as concrete maps, and tests **set equality** between those forms and all idempotents whenever \(s=1\) or \(r,s\geq2\). It separately checks reflected parameter cases.

Both programs passed for all 100 parameter pairs in the stated range. These exhaustive finite computations test the proof's base cases, transition convention, idempotent forms and enumeration, but do not replace its all-parameter argument. Execute with `python3 verify_kmp.py` and `python3 verify_forms.py` from the package directory. No external dependencies are required.

## Relationship to prior work

Gusev, Maslennikova and Pribavkina [1] establish syntactic **semigroup cardinality** for principal ideals using prefix/suffix pairs and inner factors. In the present two-run case their result yields the known total size of \(M_{r,s}\) (after adjoining the empty-word identity), but neither their theorem nor its proof states the composition-idempotent classification, count, rank profile or density transition obtained here. The distinction is substantive: semigroup cardinality alone does not determine an idempotent subpopulation.

Brzozowski, Szykuła and Ye [2] determine maximal syntactic complexities for broad ideal-language classes and classify extremal witness semigroups; their general upper-bound witness is not the specified two-run factor automaton and does not imply these idempotent formulas. Dieck and Verwer [3] study learning syntactic monoids from finite trace samples and motivate the structural use of monoid elements, but do not classify the present principal ideals or their idempotents. These comparisons identify a specific, narrower algebraic invariant rather than claiming any new total-size theorem.

## Limitations

The count and structural classification concern binary two-run **principal** factor ideals only; no formula is claimed for arbitrary patterns, larger alphabets or multiple forbidden factors. The general size formula in the finding is credited to earlier work. The proof does not establish an optimal learning algorithm or a lower bound for arbitrary monoid inference. Literature priority remains conditional on the coverage of the inspected records and could be altered by an unindexed equivalent classification.

## References

[1] V. V. Gusev, M. I. Maslennikova and E. V. Pribavkina, *Principal ideal languages and synchronizing automata*, arXiv:1304.3307v1 (first public 2013-04-11), especially Theorem 1 and its exceptional two-run cases. https://arxiv.org/abs/1304.3307

[2] J. A. Brzozowski, M. Szykuła and Y. Ye, *Syntactic Complexity of Regular Ideals*, Theory of Computing Systems (first public online 2017-08-04). https://doi.org/10.1007/s00224-017-9803-8

[3] S. Dieck and S. Verwer, *Learning Syntactic Monoids from Samples by extending known Algorithms for learning State Machines*, Proceedings of Machine Learning Research 217:59–79 (proceedings made public 2023-07-05). https://proceedings.mlr.press/v217/dieck23a.html
