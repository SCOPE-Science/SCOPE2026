# Sharp logarithmic replacement and linear subteam budgets for equality–constancy types

## Finding

Fix a finite pure-equality structure \(M\) of cardinality \(m\ge2\), an integer \(k\ge1\), and a nonempty team \(X\subseteq M^k\). Regard each variable \(x_i\) as the coordinate function \(f_i:X\to M\), \(f_i(s)=s(x_i)\). Define the **equality–constancy type** of \(X\) to be the data of (i) which pairs of functions \(f_i,f_j\) are identical and (ii) which individual \(f_i\) are constant. Let \(r=r(X)\) be the number of distinct nonconstant coordinate functions; repeated nonconstant columns count once. Let a profile-equivalent replacement be a nonempty \(Y\subseteq M^k\) with the same type, and a profile-equivalent subteam additionally satisfy \(Y\subseteq X\).

**Theorem (two sharp budgets).** The exact least size of a profile-equivalent replacement is

\[
\tau_m(r)=\begin{cases}
1,&r=0,\\
\min\{t\ge1:m^t-m\ge r\}=\lceil\log_m(m+r)\rceil,&r\ge1.
\end{cases}
\]

Every \(X\) has a profile-equivalent subteam of size at most \(r+1\), and this bound is the smallest uniform bound as a function of \(r\). By the equality–constancy invariance lemma for \(\mathsf{FOT}^{-}\), each of these replacements or subteams satisfies exactly the same formulas of that logic in the empty signature as \(X\). In particular, when \(\varphi(x_1,\ldots,x_k)\) is satisfied by a **nonempty** team on \(M\), it has such a witness with no more than \(\lceil\log_m(m+k)\rceil\) rows; this last uniform bound is sharp for every \(k\ge1\).

## Assumptions and scope

The underlying alphabet has exactly \(m\ge2\) elements; all formulas are in the empty relation signature and have at most the displayed \(k\) free variables. The logic \(\mathsf{FOT}^{-}\) is the inclusion- and disequality-atom-free fragment of elementary first-order team logic: its equality atoms, weak Boolean connectives, and single-value weak quantifiers use the semantics fixed in Engström–Kontinen. Nonempty teams are essential: the empty-team property makes the usual unrestricted satisfiability question degenerate. A formula may quantify additional bound variables, but has free variables among \(x_1,\ldots,x_k\). No order, arithmetic, other relations, inclusion atoms, full splitting quantifiers, or intuitionistic implication are permitted.

Two coordinate functions are 'equal' here if they agree for **every** assignment, i.e. if the team satisfies the ordinary atom \(x_i=x_j\). A constant function is one satisfying the definable constancy formula \(C(x_i)=\exists^1 z\,(x_i=z)\), where \(z\) is fresh. Thus this is precisely the type described by Lemma 3.3 and Proposition 3.4 of Engström–Kontinen, not a pointwise tuple equality pattern.

## Proof

**1. Minimum unrestricted replacement.** Suppose a profile \(P\) has \(r\) nonconstant equivalence classes of coordinates and \(c\) distinct constant classes. Its realizability implies \(c\le m\). On a team of \(t\) assignments, each variable has a column word in \(M^t\). Exactly \(m\) of the \(m^t\) words are constant, and there must be at least \(r\) *distinct* nonconstant words. Hence \(m^t-m\ge r\), unless \(r=0\), in which case one assignment is necessary and sufficient.

Conversely, if \(r\ge1\), let \(t\) be the least positive integer with \(m^t-m\ge r\). Pick \(r\) distinct nonconstant words in \(M^t\), one for each nonconstant class, and \(c\) distinct constant words, one for each constant class. Assign to each variable the word belonging to its class. Reading those words by positions defines \(t\) candidate assignments in \(M^k\). They are in fact all distinct: if two positions gave identical assignments, removing one duplicated position from every column would produce \(r\) distinct nonconstant words of length \(t-1\), contradicting minimality. Therefore these are exactly \(t\) team members and realize the required profile. The case \(r=0\) is obtained with a single row and \(c\) distinct constant values. This proves the exact formula.

**2. Extracting actual rows.** Consider the \(k\) variable functions on \(X\) together with all \(m\) constant functions \(u_a(s)=a\), for \(a\in M\). Exactly \(m+r\) distinct functions occur. Choose an arbitrary first row \(s_0\in X\). At that row the constants already occupy \(m\) distinct value classes. If any pair of originally distinct functions is still indistinguishable by the selected rows, pick such a pair and add a row of \(X\) on which they differ. Each addition strictly refines the partition of these functions, increasing the number of presently distinct restrictions by at least one. The initial partition has \(m\) parts; the final partition has \(m+r\) parts. At most \(r\) additions are possible. The chosen subteam therefore has at most \(r+1\) rows, and distinguishes exactly the original coordinate classes, their equality to any constant, and hence their constancy. For \(r=0\), the first row alone suffices.

**3. Sharpness of actual-row extraction.** Let \(r\ge1\), take any \(M\) containing \(0,1\), and form the staircase team with rows \(s_0,\ldots,s_r\) and coordinates \(i=1,\ldots,r\), defined by \(s_j(x_i)=1\) exactly when \(j\ge i\). Every coordinate is nonconstant and all \(r\) coordinate functions are distinct. Deleting row \(s_0\) makes the first coordinate constant \(1\); deleting \(s_r\) makes the last coordinate constant \(0\); deleting an interior row \(s_j\) makes coordinate functions \(x_j\) and \(x_{j+1}\) equal. Each deletion irreversibly alters the profile, and therefore no proper subteam preserves it. Thus \(r+1\) is necessary in the worst case.

**4. Sharpness for all formulas.** The formula

\[
\Phi_k=\bigwedge_{i=1}^{k}\mathop{\dot{\sim}}C(x_i)\;\land\!
\bigwedge_{1\le i<j\le k}\mathop{\dot{\sim}}(x_i=x_j)
\]

The pairwise conjunction is vacuous when \(k=1\). This formula holds on a nonempty team exactly when all \(k\) coordinate functions are nonconstant and pairwise distinct. Hence a model with \(m\) elements must have at least \(\tau_m(k)\) rows to satisfy \(\Phi_k\), and the construction in step 1 realizes equality. The staircase team satisfies \(\Phi_r\) but none of its proper subteams does, proving semantic sharpness of the extracted-row bound as well. The expressions above are weak/Boolean negations, *not* primitive pointwise disequality atoms.

**5. Logical preservation.** Engström–Kontinen, Lemma 3.3, establishes that on the same pure-equality model the equality–constancy type of a nonempty team determines the truth of every \(\mathsf{FOT}^{-}\) formula, including weak quantified formulas. Steps 1 and 2 preserve exactly that type, so both constructions preserve all such formulas at once. No finite-case enumeration is used in this implication.

## Verification

The accompanying standalone Python 3 checker, `verify_team_bounds.py`, exhaustively enumerates all nonempty teams over binary alphabets with \(1\le k\le4\), ternary alphabets with \(1\le k\le2\), and four-element alphabets with \(1\le k\le2\). It independently computes the equality–constancy profile, dynamic-programs the minimum profile-preserving subteam size, collects the smallest replacement size for each profile, and checks the greedy construction against the two proved bounds. It also tests staircase sharpness at \(1\le r\le11\) for three alphabet sizes.

The success marker is `SHARP_SMALL_TEAM_BOUNDS_VERIFY_OK`. Finite enumeration is a check on the constructions, not a proof of the unrestricted theorem, which follows from the counting and separation arguments above.

## Relationship to prior work

Engström–Kontinen, *Intuitionistic Implication in Elementary Team Logics* (first public version September 14, 2026), proves the invariant equality–constancy normal form and decidability of \(\mathsf{FOT}^{-}\) in the empty signature. Their Section 3 provides the essential semantic reduction used here, and remarks that large enough domains realize each formal type. It does not state either exact minimum-team-size formula or the sharp profile-preserving subteam extraction bound. The present result quantifies the resource costs of realizations and separates replacement from extraction.

Kontinen–Yang develops the expressive foundations of elementary team properties. Kontinen–Mahmood–Meier–Vollmer studies team-size constraints for dependence, independence, and inclusion logics, in a different syntax and complexity setting. Elementary separation of finite functions is standard; what is supplied here is the simultaneous exact sharp pair of finite budgets for this specific semantic type invariant.

## Limitations

The model size \(m\) is fixed, finite, and at least \(2\). The one-element domain and teams with no free variables are deliberately outside the theorem. Replacement teams need not be contained in the input team; subteam compression cannot generally reach the logarithmic replacement size. The logic must exclude primitive disequality/inclusion atoms and intuitionistic implication, which can detect additional information. Historical priority for a different terminology (separating systems, database column profiles) cannot be excluded by targeted literature searches. Neither the checker nor the self-review constitutes independent formal verification.

## References

1. F. Engström and J. Kontinen, *Intuitionistic Implication in Elementary Team Logics*, arXiv:2609.15216, first submitted 2026-09-14, especially Section 3, Lemma 3.3 and Proposition 3.4. https://arxiv.org/abs/2609.15216
2. J. Kontinen and F. Yang, *Complete logics for elementary team properties*, arXiv:1904.08695 (initial version 2019). https://arxiv.org/abs/1904.08695
3. J. Kontinen, Y. Mahmood, A. Meier, H. Vollmer, *Parameterized complexity of weighted team definability*, *Mathematical Structures in Computer Science* 34 (2024), 375–389, doi:10.1017/S0960129524000033.
