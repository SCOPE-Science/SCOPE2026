# Rational trace enumerators for proper words under a commuting marker

## Finding

Let \(h\ge 2\) be an integer, \(A\) an alphabet of size \(h\), and \(b\notin A\). On \(\Sigma=A\cup\{b\}\), let the independence relation consist precisely of \((b,a)\) and \((a,b)\), for \(a\in A\). Thus \(b\) can be commuted past any letter of \(A\), whereas the relative order of letters from \(A\) cannot be changed.

Let \(L_h\) be the language consisting of the empty word and all nonempty words with *unequal consecutive letters*. Let \(K_h\subseteq L_h\) consist of the empty word and words of length at least two for which the first and last letters are also unequal. Write \(t_h(n)\) and \(c_h(n)\) for the numbers of Mazurkiewicz-trace classes having at least one representative of length \(n\) in \(L_h\) and \(K_h\), respectively. These are counts of **classes intersecting the languages**, not counts of words or cyclic-rotation classes.

For every \(h\ge2\), their ordinary generating functions are exactly

\[
F_h(z)=\sum_{n\ge0}t_h(n)z^n
=1+z+\frac{h}{1-z}\left(\frac{z}{1-(h-1)z-z^2}-\frac{z^4}{1-hz^2}\right)
\]

and

\[
G_h(z)=\sum_{n\ge0}c_h(n)z^n
=1+\frac{1}{1-z}\left(\frac{z(h-1+z)}{1-z(h-1+z)}+\frac{(h-1)z(z-1)}{1-z(z-1)}-\frac{hz^3}{1-hz^2}\right).
\]

Both trace closures \([L_h]\) and \([K_h]\) are **nonregular languages**, although both trace-class counting series are rational. The closure means the union of all trace classes meeting the original regular language.

## Assumptions and scope

All generating-function identities are formal power-series identities over the rationals, and hold for every coefficient index \(n\ge0\) and every integer \(h\ge2\). For the cyclic constraint the empty word is explicitly included and words of length one are excluded, so \(c_h(0)=1\) and \(c_h(1)=0\). We do not identify words under rotation, and the independence relation is irreflexive. The nonregularity statements concern the trace closures as ordinary word languages, not the original languages, which are regular.

## Proof

**Trace coordinates.** In a word \(w\), delete all occurrences of \(b\) and call the remaining word \(u\in A^*\); let \(r\) be the number of occurrences of \(b\). Repeated swaps of adjacent independent letters move every \(b\) through every non-\(b\) letter, without changing the \(A\)-subsequence or \(r\). Conversely, all placements of \(r\) identical copies of \(b\) around a given \(u\) are related by such swaps. Therefore the pair \((u,r)\) is a *complete* invariant of a trace.

**Linear gap criterion.** For nonempty \(u=u_1\cdots u_m\), set

\[
e(u)=\#\{1\le j<m:u_j=u_{j+1}\}.\]

There are exactly \(m+1\) linear gaps before, between, and after the letters of \(u\). To obtain a word in \(L_h\), no gap may contain two copies of \(b\), and every gap between equal consecutive letters of \(u\) must contain one copy. This is feasible if and only if

\[e(u)\le r\le m+1.\]

When \(u\) is empty the permitted values are \(r=0,1\). The weighted count of nonempty words \(u\in A^m\), where each equal adjacent pair contributes a factor of \(z\), is

\[P_m(z)=\sum_{u\in A^m}z^{e(u)}=h(h-1+z)^{m-1},\]

since the first letter has \(h\) choices, and each successor has \(h-1\) unequal choices or one equal choice. For each \(u\) the permitted lengths \(m+r\) contribute

\[
\sum_{r=e(u)}^{m+1}z^{m+r}=\frac{z^{m+e(u)}-z^{2m+2}}{1-z}.
\]

Consequently, summing over \(m\ge1\) and adding the two empty-projection traces gives

\[
F_h(z)=1+z+\frac1{1-z}\sum_{m\ge1}\left(z^mP_m(z)-h^m z^{2m+2}\right).
\]

The two geometric series in this expression are \(hz/[1-(h-1)z-z^2]\) and \(hz^4/(1-hz^2)\). This proves the first formula.

**Circular gap criterion.** For nonempty \(u\in A^m\), set

\[
e_\circ(u)=\#\{1\le j\le m:u_j=u_{j+1}\},\quad u_{m+1}=u_1.\]

The cyclic order of the \(A\)-letters has \(m\) gaps, and an admissible cyclic representative is obtained precisely by placing zero or one \(b\) in each such gap, including the gap crossing the chosen linear boundary; all equal-letter gaps must be occupied. Thus

\[e_\circ(u)\le r\le m.\]

This also works for \(m=1\): its sole cyclic gap must contain one \(b\). For \(u=\epsilon\), only the empty word is cyclically proper.

Consider the \(h\times h\) matrix whose diagonal entries equal \(z\) and whose off-diagonal entries equal \(1\). Its eigenvalues are \(z+h-1\) once and \(z-1\) with multiplicity \(h-1\). The trace of its \(m\)-th power therefore counts weighted closed walks of length \(m\), so

\[
Q_m(z)=\sum_{u\in A^m}z^{e_\circ(u)}=(h-1+z)^m+(h-1)(z-1)^m.
\]

The admissible powers of \(z\) for each \(u\) sum to

\[
\sum_{r=e_\circ(u)}^m z^{m+r}=\frac{z^{m+e_\circ(u)}-z^{2m+1}}{1-z}.
\]

Therefore

\[
G_h(z)=1+\frac{1}{1-z}\sum_{m\ge1}\left(z^mQ_m(z)-h^m z^{2m+1}\right).
\]

Evaluating the three geometric series gives the displayed second formula.

**Nonregularity.** Fix \(a\in A\). Intersect the trace closures with the regular language \(a^*b^*\). From the two gap criteria, their intersections are respectively

\[
\{\epsilon,b\}\cup\{a^m b^r:m\ge1,\ m-1\le r\le m+1\}
\]

and

\[
\{\epsilon\}\cup\{a^m b^m:m\ge1\}.
\]

Both are nonregular: in each case the prefixes \(a^m\), for increasing \(m\), have pairwise distinguishable right contexts (or use the regular-language pumping lemma with \(a^p b^p\) and sufficiently many pumps of the initial \(a\)'s). Since regular languages are closed under intersection, neither trace closure is regular. This completes the theorem.

## Verification

Run `python3 checker.py` from a directory containing this file and the script. The checker computes the two length sequences three ways: independently by enumeration of original words and trace signatures, by enumeration of projected words with their mandatory marker gaps, and by integer coefficient recurrences from the two rational formulas. It checks nontrivial alphabet sizes \(h=2,3,4\) and additional parameter values \(1\le h\le7\); \(h=1\) is used only as an auxiliary regression case, outside the theorem's principal scope. For \(h=2\) the sequences through index nine are

\[
(t_2(0),\ldots,t_2(9))=(1,3,4,8,12,22,34,60,94,162)
\]

and

\[
(c_2(0),\ldots,c_2(9))=(1,0,4,2,12,8,34,26,94,78).
\]

These computations are finite consistency checks; the all-length conclusion follows from the preceding symbolic argument.

## Relationship to prior work

The general problem of counting trace classes intersecting a regular language, including languages not closed under trace equivalence, is studied by de Colnet, Meel, and Mathur (2025 preprint; POPL 2026). Their complexity and approximation results do not give the two exact all-alphabet generating functions above. Their Example 5.3 uses the three-letter independence relation corresponding to \(h=2\), but the illustrated automaton accepts words with adjacent equal symbols, so it does not calculate the present proper-word or circular-proper-word counts.

Maarand and Uustalu (2019) develop derivatives of trace closures and explain that a regular source language can have a nonregular trace closure. That general phenomenon alone does not give the explicit trace-coordinate criteria or these rational enumerators. Both comparisons concern mathematical implications, not mere title differences. No claim of definitive historical priority is made.

## Limitations

The independence graph has precisely one marker commuting with all other letters, whose mutual pairs do not commute. No statement is made for arbitrary independence graphs, additional local forbidden patterns, rotational equivalence, or efficient trace sampling. Rationality here does not assert that either closure is regular. Earlier implicit specializations in classical trace-monoid or constrained-coloring literature cannot be ruled out without independent historical validation.

## References

1. A. de Colnet, K. S. Meel, and U. Mathur, *Counting and Sampling Traces in Regular Languages*, arXiv:2512.00314, first public 2025-11-29, Proc. ACM Program. Lang. 10 (POPL 2026), Article 81. https://arxiv.org/abs/2512.00314; https://doi.org/10.1145/3776723.
2. H. Maarand and T. Uustalu, *Reordering Derivatives of Trace Closures of Regular Languages*, CONCUR 2019, Article 40. https://doi.org/10.4230/LIPIcs.CONCUR.2019.40; https://arxiv.org/abs/1908.03551.
