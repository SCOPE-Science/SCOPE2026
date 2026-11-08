# Exact state complexity for the union and intersection of opposite two-run subsequence ideals

## Finding

Let \(a,b\ge 1\) be integers, \(n=a+b\), \(\Sigma=\{0,1\}\), and \(u\preceq w\) mean that \(u\) is a scattered subsequence of \(w\). Put
\[
P=0^a1^b,\qquad Q=1^b0^a,\qquad I(T)=\{w\in\Sigma^*:T\preceq w\}.
\]
Write \(\kappa(L)\) for the number of states in the smallest *complete deterministic* finite automaton for \(L\). Then, for all positive \(a,b\),
\[
\boxed{\kappa(I(P)\cap I(Q))=\frac{n(n+3)}2+ab,\qquad
\kappa(I(P)\cup I(Q))=\frac{n(n+1)}2+ab.}
\]
The gap is exactly \(n\). Both languages have explicit minimal automata obtained from a single reachable product construction: the intersection retains all its reachable states; the union collapses precisely its accepting states into one absorbing state.

## Assumptions and scope

Words are finite; their alphabet is the **fixed binary alphabet** \(\Sigma\). The parameters \(a,b\) are independently arbitrary positive integers; there are no coprimality, parity, or asymptotic assumptions. The two component ideals are the principal *all-sided* (subsequence-upward-closed) ideals \(I(P)\) and \(I(Q)\), not contiguous-factor ideals. State complexity counts all reachable states of a complete DFA, including the accepting sink.

The length \(n\) is the common length of the two generators, not the number of automaton states. Individually, each principal ideal has \(n+1\) quotient states: greedy subsequence progress \(0,\ldots,n\) is reachable and successive progress states are distinguishable by completion suffixes.

## Proof

**1. Product automaton and reachability geometry.** Construct the complete greedy-matching DFA for each generator: at progress \(p<n\), the state increments only on the next required letter \(P_{p+1}\), and progress \(n\) is absorbing; analogously for \(Q\). Their deterministic product has states \((p,q)\), with initial \((0,0)\), and recognizes the intersection or union according to the accepting condition.

Every reachable pair belongs to exactly one of the following four disjoint regions:
\[
\begin{aligned}
D_0&=\{(p,q):0\le p\le a,\ 0\le q\le b\}\setminus\{(a,b)\},\\
D_1&=\{(a+i,q):1\le i\le b,\ i\le q\le b\},\\
D_2&=\{(p,b+j):1\le j\le a,\ j\le p\le a\},\\
D_3&=\{(a+i,b+j):1\le i\le b,\ 1\le j\le a\}.
\end{aligned}
\]
Indeed, if \(p>a\) and \(q\le b\), the word has seen at least \(p-a\) ones after the \(a\)-th zero, so \(q\ge p-a\). The symmetric implication gives \(p\ge q-b\) when \(q>b\) and \(p\le a\). The pair \((a,b)\) is unreachable: the \(a\)-th zero and \(b\)-th one occur at distinct instants, so whichever threshold is reached first forces the other progress to exceed its first-block threshold when the second is reached.

Conversely, the regions are entirely reachable. For \((p,q)\in D_0\), use \(0^p1^q\) if \(p<a\), and \(1^q0^a\) if \(p=a\) (then \(q<b\)). For \((a+i,q)\in D_1\) use \(1^{q-i}0^a1^i\). For \((p,b+j)\in D_2\) use \(0^{p-j}1^b0^j\). For \((a+i,b+j)\in D_3\) use \(1^{b-i}0^a1^i0^j\). Direct greedy matching gives the advertised coordinates in every case.

It follows that the number of reachable product states is
\[
R=((a+1)(b+1)-1)+\frac{a(a+1)}2+\frac{b(b+1)}2+ab
=\frac{n(n+3)}2+ab.
\]

**2. All intersection states are distinguishable.** From reachable state \((p,q)\), the right language for intersection requires simultaneous completion of the unmatched suffixes of \(P\) and \(Q\). The following four families of test suffixes have exact acceptance thresholds, where \((t)_+=\max(t,0)\) and \(r,s\) range over nonnegative integers:

- \(0^r1^b0^a\) is accepted exactly when \(r\ge(a-p)_+\).
- \(1^s0^a\) is accepted exactly when \(p\ge a\) and \(s\ge n-p\).
- \(1^s0^a1^b\) is accepted exactly when \(s\ge(b-q)_+\).
- \(0^r1^b\) is accepted exactly when \(q\ge b\) and \(r\ge n-q\).

For the first family, the middle ones and last zeros always complete the remaining \(Q\)-suffix; only the \(P\)-suffix can require preliminary zeros. The second family cannot complete \(P\) when \(p<a\); otherwise it needs \(n-p\) ones. If \(q\le b\) as well, reachability gives \(q\ge p-a\) when \(p>a\), so the requirement \(b-q\) for \(Q\) never exceeds \(n-p\). The third and fourth statements are the zero/one-reversed counterparts, using \(p\ge q-b\) when \(q>b\).

The first two test families recover \(p\) exactly from its threshold (distinguishing \(p<a\) from \(p\ge a\)); the last two recover \(q\) exactly. Hence no two distinct reachable states have the same right language. The complete reachable product DFA for intersection is minimal, and its size is \(R\).

**3. Exactly one union collapse.** For union, any state with \(p=n\) or \(q=n\) accepts every continuation, so all such states are equivalent to a single accepting sink. All other reachable states have both coordinates less than \(n\), and four analogous probes recover each coordinate:

- \(1^s\) is accepted exactly when \(p\ge a\) and \(s\ge n-p\).
- If \(p<a\), \(0^r1^b\) is accepted exactly when \(r\ge a-p\).
- \(0^r\) is accepted exactly when \(q\ge b\) and \(r\ge n-q\).
- If \(q<b\), \(1^s0^a\) is accepted exactly when \(s\ge b-q\).

The pure-letter probes cannot complete the other generator unless that generator is already complete, which is excluded. For the second probe, when \(q\ge b\), the \(Q\)-suffix may also finish, but the reachability inequality \(p\ge q-b\) implies \(a-p\le n-q\), so it never lowers the \(P\)-threshold; if \(q<b\), \(Q\) cannot finish on that two-run suffix. The fourth probe is symmetric. Thus the first two families recover \(p\), and the last two recover \(q\). No further union identifications occur.

Exactly \(a+1\) reachable states have \(p=n\), namely \((n,b),\ldots,(n,n)\); exactly \(b+1\) have \(q=n\), namely \((a,n),\ldots,(n,n)\). Their overlap is \((n,n)\), so the absorbing equivalence class has \(a+b+1=n+1\) states. Collapsing it removes \(n\) states, yielding \(\kappa(I(P)\cup I(Q))=R-n\), as claimed. \(\square\)

## Verification

Run \(\texttt{python3 checker.py}\) with standard Python 3. The supplied standalone checker independently constructs both greedy automata, computes reachable product states and performs iterative partition refinement, then compares the resulting minimal counts against both formulas for all \(1\le a,b\le18\). It also independently enumerates all binary words of lengths up to \(11\) for \(1\le a,b\le4\) and checks that direct subsequence containment agrees with the product automaton. Four probe families per Boolean operation are checked on reachable states for \(1\le a,b\le9\).

On replay the checker reports: `PASS: 324 parameter pairs, 65520 bounded direct-word checks, 221616 state/probe iterations`.

For example, at \(a=b=2\), both generators have length \(4\) and their individual minimal DFAs have \(5\) states; the intersection has \(18\), the union \(14\), instead of the full product size \(25\). The proof above, not this finite replay, covers all positive parameters.

## Relationship to prior work

The study of finite-automaton decompositions for shuffle ideals in Berry, Héam and Jecker (2026), originally publicly posted 2026-04-28, motivates determining exact automaton costs of natural unions and intersections. Their Section 5 focuses on union-primality, accelerating patterns, and decomposition, and does not present the two-parameter opposite-block formulas here. In particular their criterion for a union-prime ideal concerns the maximum minimal-generator length, not the exact quotient count of this conjunction/disjunction.

Héam (2002), Section 5.2, establishes \(\Theta(mn)\) worst-case behavior for union and intersection of shuffle ideals using distinct generators; its general statement does not fix the opposite-run generators. Brzozowski, Jirásková and Li (arXiv 2009; journal 2013), Section 7.1, give sharp general bounds \(\kappa(K\cap L)\le mn\), \(\kappa(K\cup L)\le mn-(m+n-2)\) for all-sided ideals of component complexities \(m,n\). Those are worst-case bounds, whereas the formulas above compute the exact values for a fixed two-parameter family of ordered generators. For this family each component has \(n+1\) states (where \(n=a+b\)); the reachable-product geometry gives the sharper counts.

These comparisons do not establish absolute historical novelty: an earlier unindexed specialization or a formula implicit in a different treatment of subsequence ideals may exist. They do distinguish the present equalities from the cited general algorithms and worst-case bounds.

## Limitations

The result applies only to \(\Sigma=\{0,1\}\) and the two generators \(0^a1^b\) and \(1^b0^a\) with \(a,b\ge1\). It does not address arbitrary antichains of subsequence generators, nondeterministic automaton minima, or state counts of automata with partially defined transitions. The finite computations are bounded consistency checks and do not certify infinite parameter ranges. No independently performed mathematical audit or exhaustive historical-priority search is claimed.

## References

1. M. Berry, P.-C. Héam and I. Jecker, *Decomposition of Automata Recognizing Ideals*, arXiv:2604.25619, first public version 2026-04-28. https://arxiv.org/abs/2604.25619 ; relevant full text Sections 1, 2 and 5 (Theorem 21).
2. P.-C. Héam, *On Shuffle Ideals*, RAIRO Theoretical Informatics and Applications **36** (2002), 359–384, DOI 10.1051/ita:2003002. https://www.numdam.org/article/ITA_2002__36_4_359_0.pdf ; especially Section 5.2.
3. J. Brzozowski, G. Jirásková and B. Li, *Quotient Complexity of Ideal Languages*, arXiv:0908.2083 (2009), later Theoretical Computer Science (2013). https://arxiv.org/pdf/0908.2083 ; especially Theorem 14, Section 7.1.
