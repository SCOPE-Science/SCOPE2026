# Exact residue-sensitive state complexity for modular counts of distinct binary subsequences

## Finding

For a finite binary word \(w\), let \(P(w)\) be the number of **distinct** scattered subsequences of \(w\), counting the empty subsequence once. For every integer \(m\ge 2\), define the languages
\[
L_m^{(0)}=\{w\in\{0,1\}^*:P(w)\equiv 0\pmod m\},\qquad
L_m^{(-1)}=\{w\in\{0,1\}^*:P(w)\equiv-1\pmod m\}.
\]
Writing \(\operatorname{sc}(L)\) for the number of states of the minimal **complete deterministic** finite automaton of \(L\), and taking products over distinct prime divisors, we have
\[
\boxed{\begin{aligned}
\operatorname{sc}(L_m^{(0)})&=J_2(m)=m^2\prod_{p\mid m}(1-p^{-2}),\\
\operatorname{sc}(L_m^{(-1)})&=\frac{J_2(m)}{\varphi(m)}=m\prod_{p\mid m}(1+p^{-1}).
\end{aligned}}
\]
Here \(J_2\) is the second Jordan totient and \(\varphi\) is Euler's totient. In particular their exact state-complexity ratio is \(\varphi(m)\), unbounded as \(m\) varies, although the two output residues are adjacent. More strongly, the first minimal automaton has states indexed by primitive pairs modulo \(m\), while the second has states indexed by primitive pairs up to multiplication by any modular unit. The smallest deterministic Moore machine outputting \(P(w)\bmod m\) after each prefix also has exactly \(J_2(m)\) states.

## Assumptions and scope

The alphabet is the labeled binary alphabet \(\{0,1\}\); the empty input is allowed. A scattered subsequence is obtained by deleting positions without changing order. Identical resulting strings are counted only once. \(P(\epsilon)=1\), so the empty subsequence is **included**; omitting it shifts every residue class by one and must not be conflated with the present statement. Every claim holds for each integer \(m\ge2\), prime or composite, and for **unbounded** input lengths. No claim is made here for arbitrary nonzero nonunit output residues. Complete DFAs include all transitions and have no added unreachable state.

Let \(R=\mathbb Z/m\mathbb Z\), and let \(U_m=R^\times\) be its group of units. A pair \((x,y)\in R^2\) is *primitive* (or unimodular) if \(xR+yR=R\), equivalently if integer representatives satisfy \(\gcd(x,y,m)=1\). Denote the set of primitive pairs by \(V_m\).

## Proof

**1. Exact online statistic.** For any prefix \(w\), let \(a(w)\) and \(b(w)\) count the distinct nonempty subsequences ending in \(0\) and \(1\), respectively. Define \(x=a+1\), \(y=b+1\). Appending \(0\) changes the ending-in-zero set into all existing subsequences with a new last zero, whereas the ending-in-one set is unchanged. Appending \(1\) is symmetric. Consequently, with columns \(v=(x,y)^T\),
\[
T_0v=\begin{pmatrix}1&1\\0&1\end{pmatrix}v,
\qquad
T_1v=\begin{pmatrix}1&0\\1&1\end{pmatrix}v,
\quad v(\epsilon)=\binom11,
\quad P(w)=x(w)+y(w)-1.
\]
Both matrices have determinant one, so reductions of reachable vectors modulo \(m\) are primitive.

**2. Reachability and all suffix tests.** Every primitive residue pair has positive coprime integer lifts \((A,B)\): choose \(B>0\) representing its second coordinate; choose \(A=a+km>0\) and avoid divisibility by each prime divisor of \(B\) that does not divide \(m\) (possible by the Chinese remainder theorem). At primes dividing both \(B\) and \(m\), primitivity already forces \(a\not\equiv0\) modulo that prime. Hence \(\gcd(A,B)=1\). Repeatedly subtracting the smaller positive coordinate from the larger reduces \((A,B)\) to \((1,1)\). Reversing these steps builds \((A,B)\) from \((1,1)\) by \(T_0,T_1\), proving that *every* member of \(V_m\) is reachable.

For a suffix \(z\), write \(T_z\) for its product matrix acting on the prefix state, and \(\ell_z=(1,1)T_z\). The matrices are invertible, so each such row is primitive. Conversely, right multiplication by \(T_0\) and \(T_1\) acts on a row \((c,d)\) as \((c,c+d)\) and \((c+d,d)\), respectively. The same positive-lift/subtractive-Euclid argument proves that **every** primitive row \(\ell\in R^{1\times2}\) occurs as \(\ell_z\) for a finite suffix \(z\). After appending \(z\), the output is
\[
P(wz)\equiv\ell_z v(w)-1\pmod m.
\]
Thus right-language equivalence of two prefix states is decided by all primitive linear forms on their two coordinates.

**3. The zero-output language.** Membership in \(L_m^{(0)}\) after a suffix with row \(\ell\) is equivalent to \(\ell v=1\) in \(R\). We show any distinct primitive vectors \(v,w\) are distinguishable. Since \(v\) is primitive, extend it to a basis \((v,q)\) of \(R^2\); write \(w=Av+Bq\). If \(B\ne0\), the primitive rows characterized by \(\ell_t(v)=1\), \(\ell_t(q)=t\), for \(t=0,1\), satisfy \(\ell_t(w)=A+Bt\). These two values are different, so at least one is not one, giving a distinguishing suffix. If \(B=0\), primitivity of \(w\) implies \(A\in U_m\), and \(v\ne w\) implies \(A\ne1\). Any primitive row with \(\ell(v)=1\) then satisfies \(\ell(w)=A\ne1\). Thus no two states merge and \(\operatorname{sc}(L_m^{(0)})=|V_m|\).

**4. The minus-one-output language.** Membership in \(L_m^{(-1)}\) after a suffix with row \(\ell\) is equivalent to \(\ell v=0\) in \(R\). If \(w=uv\) for \(u\in U_m\), then \(\ell w=0\) if and only if \(\ell v=0\), so unit-proportional states merge. Conversely, the primitive row \(\ell=(-v_2,v_1)\) annihilates \(v\). If it also annihilates \(w\), then \(\det(v,w)=0\). Completing \(v\) to a basis shows \(w=Av\), and primitivity of \(w\) forces \(A\) to be a unit. Therefore any two vectors not related by a unit have different right languages. The quotient under the free \(U_m\)-action is exactly the minimal DFA. The action is free because a primitive vector has a linear combination of its coordinates equal to one, so \(uv=v\) implies \(u=1\).

**5. Exact counts and an output-machine corollary.** At each prime power \(p^e\) dividing \(m\), precisely \(p^{2e}-p^{2(e-1)}\) pairs are primitive. The Chinese remainder theorem therefore yields \(|V_m|=J_2(m)=m^2\prod_{p\mid m}(1-p^{-2})\). Dividing by \(|U_m|=\varphi(m)=m\prod_{p\mid m}(1-p^{-1})\) gives the second formula.

For the modular-output Moore machine, two different vectors are distinguished already by some suffix: \(0^{m-1}\) makes the output equal to \(x-1\pmod m\), and \(1^{m-1}\) makes the output equal to \(y-1\pmod m\). Hence all \(|V_m|\) states remain different even if the output rather than a single residue predicate is observed. This completes the proof.

## Verification

A standalone Python 3 checker, `check_distinct_subsequence_mod.py`, verifies for each \(m=2,\ldots,31\): all reachable modular pairs equal the primitive pairs, the unit-projective quotient has size \(J_2(m)/\varphi(m)\), and independent DFA partition refinement gives exactly the two claimed state counts. It also checks the two short distinguishing-output suffixes for every reachable pair, and recomputes distinct-subsequence counts by direct set enumeration for all \(8191\) binary words of lengths zero through twelve. The checks completed with no discrepancies. Examples (first number for output zero, second for output minus one): \(m=2:\ (3,3)\), \(m=3:\ (8,4)\), \(m=4:\ (12,6)\), \(m=5:\ (24,6)\), \(m=6:\ (24,12)\). The finite tests corroborate the theorem but do not substitute for the infinite proof above.

To reproduce: run `python3 check_distinct_subsequence_mod.py` with the Python standard library; no external dependencies or data files are needed.

## Relationship to prior work

Żak (2022, arXiv:2210.00342) established the correspondence between binary words, coprime positive integer pairs and the total number of distinct subsequences, and investigated words realizing prescribed **integer** totals. This proof credits that foundational correspondence and independently reconstructs the primitive-pair recurrence. The present theorem instead determines **minimal regular-language recognizers** for two modular total-count predicates, their exact unit-projective quotient and their unbounded ratio. Those Myhill–Nerode conclusions do not appear among the statements in the inspected full source. Biers-Ariel, Godbole and Kelley (2017/2018) study expectations under random word models, not the stated resource invariant in the accessible abstract. Related published modular automata for counts of a single fixed scattered pattern measure a distinct statistic and do not imply total-distinct-subsequence congruence automata.

## Limitations

Only the two specified output residues are classified as decision-language state counts. The exact size for other nonunit, nonzero residues is not claimed. The output-machine corollary concerns the full residue output, not the size of a nondeterministic automaton or a streaming circuit. A full-text comparison was completed for Żak's directly relevant paper; another expectation paper was checked at the abstract/bibliographic level only. Unindexed or inaccessible equivalent work may exist. This is a proof with same-document computational checks, not an independently audited result.

## References

1. R. Żak, *Finding binary words with a given number of subsequences*, Theoretical Computer Science 919 (2022), 75–79; original public arXiv submission 2022-10-01, https://arxiv.org/abs/2210.00342 ; full HTML https://arxiv.org/html/2210.00342v1 .
2. Y. Biers-Ariel, A. Godbole, E. Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, Discrete Mathematics & Theoretical Computer Science 19(2) (2018), https://arxiv.org/abs/1704.08661 .
3. Standard finite-ring facts used in the proof: Bezout identities, the Chinese remainder theorem, Jordan's and Euler's totient formulas. These are proved or reduced to elementary counting above.
