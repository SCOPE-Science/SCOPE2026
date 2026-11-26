# Universal group complexity of binary two-run periodic words

## Finding

For every pair of positive integers \(a,b\), let
\[
  w_{a,b}=(0^a1^b)^\omega
\]
be the one-sided infinite periodic binary word. At each positive factor length \(n\), let \(F_w(n)\) be its set of distinct length-\(n\) factors, let \(p_w(n)=|F_w(n)|\), and let \(p_w^G(n)\) count the intersections of \(F_w(n)\) with the orbits of a subgroup \(G\le S_n\) acting by permutation of word coordinates. Let \(p_w^{\mathrm{ab}}(n)=p_w^{S_n}(n)\). The word has *universal group complexity* when, for all \(n\ge1\), every integer between \(p_w^{\mathrm{ab}}(n)\) and \(p_w(n)\), inclusive, is realized as \(p_w^G(n)\) by a suitable subgroup \(G\le S_n\).

**Theorem (complete two-run classification).** For all positive integers \(a,b\), \(w_{a,b}\) has universal group complexity **if and only if** \(\min(a,b)=1\). More precisely, when \(a,b\ge2\), put \(c=\mathbf 1_{a\ge3}+\mathbf 1_{b\ge3}\). Then the entire attainable group-complexity spectrum at length three is exactly
\[
  \{p_{w_{a,b}}^G(3):G\le S_3\}=\{2+c,4+c\}.
\]
The integer \(3+c\), which lies strictly between the abelian and ordinary factor complexities, is absent. When \(\min(a,b)=1\), every intermediate value occurs for every factor length, and the proof gives explicit coordinate-permutation groups realizing it.

## Assumptions and scope

The alphabet is the labelled binary alphabet \(\{0,1\}\); \(a,b\) are arbitrary positive integers. Factors are contiguous blocks of the infinite periodic word, with starting positions taken modulo its (primitive) period \(a+b\). Only coordinates within a factor are permuted; alphabet letters are not permuted by \(G\). A \(G\)-class means an ambient \(G\)-orbit on \(\{0,1\}^n\) intersected with \(F_w(n)\); the group is **not** required to preserve \(F_w(n)\) setwise. Interchanging the alphabet letters and cyclically rotating a period preserve the property.

## Proof

**1. Obstruction when both circular runs have length at least two.** Suppose \(a,b\ge2\). The length-three factor set consists of the four words
\[
 \{001,100,011,110\}
\]
and, in addition, \(000\) if \(a\ge3\), and \(111\) if \(b\ge3\). The two words of weight one are \(001,100\); those of weight two are \(011,110\). Consequently \(p_w(3)=4+c\) and \(p_w^{\mathrm{ab}}(3)=2+c\).

All six subgroups of \(S_3\) can be handled explicitly. The trivial subgroup and the two transposition groups \(\langle(12)\rangle,\langle(23)\rangle\) identify none of the four displayed nonconstant factors with another displayed factor, so each yields \(4+c\) classes. The transposition group \(\langle(13)\rangle\), the three-cycle group \(\langle(123)\rangle\), and the whole \(S_3\) identify \(001\) with \(100\), and independently \(011\) with \(110\), so each yields \(2+c\) classes. Constant factors form separate singleton classes for every coordinate-permutation group. Thus \(3+c\) is not attained, proving that universal group complexity fails.

**2. Reduction to the sparse periodic case.** Suppose \(\min(a,b)=1\). By interchanging \(0,1\) and rotating the period if necessary, the factor language is that of
\[
  W_m=(0^{m-1}1)^\omega,\qquad m=a+b\ge2.
\]
Fix a positive factor length \(n\). Each phase of this word is identified by the position of the unique \(1\) in its first complete period whenever \(n\ge m\).

**3. Short factors \(1\le n<m\).** There is one all-zero factor and one factor with a single \(1\) in each of the \(n\) possible positions. Therefore
\[
 p_{W_m}(n)=n+1,\qquad p_{W_m}^{\mathrm{ab}}(n)=2.
\]
For an arbitrary desired number \(k\in\{2,\ldots,n+1\}\), let \(G\) be the full symmetric group on the first \(n-k+2\) positions, fixing all other positions. This group has exactly \(k-1\) position-orbits. Its action on the one-hot factors has precisely those \(k-1\) classes, and the all-zero factor contributes one more class. Thus \(p_{W_m}^G(n)=k\).

**4. Factors with at least one full period.** Write uniquely \(n=tm+r\), with integers \(t\ge1\) and \(0\le r<m\). Its \(m\) distinct factors are indexed by the residue \(j\in\{1,\ldots,m\}\) of the unique \(1\) in the first \(m\) positions. Each factor has a \(1\) at position \(j\) of **every** complete length-\(m\) block, and also in the final incomplete block exactly when \(j\le r\).

When \(r=0\), all \(m\) factors have the same weight, so the lower and upper complexities are \(1\) and \(m\). For any desired \(k\in\{1,\ldots,m\}\), choose a permutation group \(H\le S_m\) with exactly \(k\) orbits on \(\{1,\ldots,m\}\), such as the full symmetric group on the first \(m-k+1\) indices, fixing the rest. Embed \(H\) diagonally into \(S_n\), applying the same index permutation in each length-\(m\) block. This maps phase \(j\) to phase \(h(j)\), so \(p_{W_m}^G(n)=k\).

When \(0<r<m\), the first \(r\) phases have weight \(t+1\), and the remaining \(m-r\) phases have weight \(t\). Hence \(p_{W_m}^{\mathrm{ab}}(n)=2\) and \(p_{W_m}(n)=m\). Given any \(k\in\{2,\ldots,m\}\), select integers \(\alpha,\beta\) satisfying
\[
 1\le\alpha\le r,\qquad 1\le\beta\le m-r,\qquad \alpha+\beta=k.
\]
Such a pair exists because the interval sum \([1,r]+[1,m-r]\) is exactly \([2,m]\). Choose \(H\le S_r\times S_{m-r}\) with \(\alpha\) orbits on the first \(r\) indices and \(\beta\) on the last \(m-r\) indices (each obtained by permuting one initial block and fixing the other indices). Apply its permutations identically on every complete length-\(m\) block and on the final \(r\)-position block. This is well-defined because \(H\) preserves the first \(r\) indices. Its orbits on the distinct factors coincide exactly with its \(\alpha+\beta=k\) orbits on phase indices. Hence \(p_{W_m}^G(n)=k\).

All factor lengths and both sides of the claimed dichotomy have now been covered. \(\square\)

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It independently constructs the periodic factor sets and the indicated permutation groups; it calculates equivalence classes by the ambient action rather than assuming that a generator preserves the factor language. It checks each desired intermediate complexity for every period \(2\le m\le12\), every length \(1\le n\le3m+2\), and every admissible target value (1,662 target checks). It also enumerates all six subgroups of \(S_3\) for all \(2\le a,b\le8\) (49 further parameter checks). All checks passed when run directly from the embedded file. The infinite parameter statement follows from the preceding proof, not these finite tests.

Run `python3 verify.py` beside this file. `verification_output.txt` records the expected stdout.

## Relationship to prior work

Launer, Puzynina, and Voloshinova (2026) introduced the all-intermediate-values universal-group-complexity property, proved it for Sturmian words, and in Section 6 provided an algorithmic finite-check criterion for eventually periodic words. Their Section 6 example treats a specific ternary periodic word; the complete uniform classification of binary two-run periods and its length-three obstruction are not stated there. The result here gives an explicit all-parameter classification and explicit realizing groups, rather than applying the prior criterion separately to each period.

Charlier, Puzynina, and Zamboni (2015/2017) developed the earlier group-complexity formalism and Morse–Hedlund-type bounds, especially for aperiodic words; the cited earlier formalism does not give the present universality classification. Their Section 2 discusses one-hot factor sets as examples of group actions, an antecedent to the positive construction above.

## Limitations

The theorem applies to periods with exactly two maximal monochromatic circular runs, one of each symbol. It does not classify arbitrary binary periodic words, all ultimately periodic words, or aperiodic words. The analytic result is independent of the scope of the finite checker. No external independent mathematical audit or validation is claimed. Searches cannot exclude differently formulated or unindexed earlier uniform classifications.

## References

1. M. Launer, S. Puzynina, E. Voloshinova, *On possible values of the group complexity function of infinite words*, arXiv:2607.07620v1 (first public 2026-07-08), particularly Sections 2, 6, 7; https://arxiv.org/html/2607.07620v1 .
2. E. Charlier, S. Puzynina, L. Q. Zamboni, *On a group theoretic generalization of the Morse–Hedlund theorem*, arXiv:1505.03848 (2015), Proc. Amer. Math. Soc. 145 (2017), 3381–3394, particularly Sections 1–2; https://arxiv.org/abs/1505.03848 .
