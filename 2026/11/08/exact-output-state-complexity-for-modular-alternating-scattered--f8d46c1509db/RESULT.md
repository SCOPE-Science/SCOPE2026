# Exact output-state complexity for modular alternating scattered triples

## Finding

Let \(m\ge 2\) be any integer. For a finite binary word \(w\), let \(\binom{w}{v}\) denote the number of strictly increasing selections of positions in \(w\) spelling the word \(v\), with different position selections counted separately. Consider the residue-valued function
\[
f_m(w)=\binom{w}{010}\pmod m.
\]
A deterministic Moore machine for \(f_m\) reads the input left to right, starting in a designated initial state, and after reading any complete input \(w\) outputs \(f_m(w)\in\mathbb Z/m\mathbb Z\). The output after the empty word is included. Two prefixes are equivalent precisely when every common continuation produces equal output residues.

**Theorem.** The exact minimum number of reachable states of such a machine is
\[
\boxed{\operatorname{sc}_{\mathrm{out}}(f_m)=\frac{m^3}{\gcd(m,2)}.}
\]
In particular, it is \(m^3\) for odd \(m\), and \(m^3/2\) for even \(m\). The same statement holds for the pattern \(101\), by exchanging the letters. This is an output-machine theorem: it does **not** assert the same number of states for any individual Boolean language \(\{w:f_m(w)=r\}\), which can admit additional identifications.

## Assumptions and scope

All words, including the empty word, are over the ordered binary alphabet \(\{0,1\}\). The integer modulus \(m\) ranges over all \(m\ge2\), whether prime, prime-power or composite. Counts are ordinary scattered-subsequence multiplicities, not contiguous substring counts or counts of distinct subsequence *values*. A Moore machine emits the current residue after every prefix; its state complexity counts reachable states, not transitions or bits of memory. All arithmetic on machine states below is modulo \(m\), unless stated otherwise.

## Proof

**Step 1: An explicit sufficient state.** Assign to each prefix \(w\) the triple
\[
(a,b,c)=\left(\binom{w}{0},\binom{w}{01},\binom{w}{010}\right)\pmod m.
\]
Appending a zero creates one new occurrence of \(0\) and one new occurrence of \(010\) for every existing \(01\) subsequence. Appending a one creates one new occurrence of \(01\) for every existing zero. Hence the transitions are
\[
T_0(a,b,c)=(a+1,b,c+b),\qquad
T_1(a,b,c)=(a,b+a,c).
\]
The start state is \((0,0,0)\), and the output is \(c\). In particular, the machine is complete and computes \(f_m\) for every binary word.

**Step 2: The parity restriction.** Fix a word and write \(Z\) for its *integer* number of zeros. For each occurrence of one, let \(\ell_j\) count the zeros before it. Its contribution to the total number of \(01\) subsequences is \(\ell_j\), and its contribution to the total number of \(010\) subsequences is \(\ell_j(Z-\ell_j)\). Thus
\[
\binom{w}{01}=\sum_j\ell_j,\qquad
\binom{w}{010}=Z\sum_j\ell_j-\sum_j\ell_j^2.
\]
Every integer \(\ell_j^2-\ell_j\) is even, so
\[
\binom{w}{010}\equiv (Z-1)\binom{w}{01}\pmod 2.
\]
Set \(\delta=\gcd(m,2)\). Every reachable triple must therefore satisfy \(c\equiv(a-1)b\pmod\delta\). For each of the \(m^2\) pairs \((a,b)\), there are exactly \(m/\delta\) possible values of \(c\). Consequently there are at most \(m^3/\delta\) reachable triples.

**Step 3: Every permitted triple is reachable.** The maps \(T_0,T_1\) are bijections of the finite residue cube, each with \(m\)-th power equal to the identity. Therefore their inverse maps are positive powers of the original letter maps, and any finite composition involving inverses is realized by an ordinary binary word.

Read compositions from left to right and define
\[
C=T_0T_1T_0^{-1}T_1^{-1},\qquad
D=CT_0C^{-1}T_0^{-1}.
\]
Direct substitution into the displayed transition formulas gives
\[
C(a,b,c)=(a,b+1,c-a-1),\qquad D(a,b,c)=(a,b,c+2).
\]
For clarity, a positive word realizing \(C\) is \(01\,0^{m-1}1^{m-1}\). Since \(C^m\) is also the identity, a positive word realizing \(D\) is the word for \(C\), followed by \(0\), followed by \(m-1\) copies of the word for \(C\), followed by \(0^{m-1}\). No formal inverse letters are added to the input alphabet.

Starting from \((0,0,0)\) and applying \(T_0^a C^b D^t\) gives
\[
(a,b,-b(a+1)+2t)\pmod m.
\]
Here \(a,b\) may be chosen as representatives in \(\{0,\ldots,m-1\}\). The congruence
\[
2t\equiv c+b(a+1)\pmod m
\]
has a solution exactly when \(\delta\mid(c+b(a+1))\). But this condition is equivalent to \(c\equiv(a-1)b\pmod\delta\), because the two right-hand expressions differ by \(2ab\). Hence every permitted triple is reachable. There are exactly \(m^3/\delta\) of them.

**Step 4: No reachable states can be merged.** Let a reachable triple be \((a,b,c)\). Its outputs after appending the three fixed suffixes \(\varepsilon\), \(0\) and \(10\) are, respectively,
\[
c,\qquad c+b,\qquad c+b+a\pmod m.
\]
These three residues uniquely recover first \(c\), then \(b\), then \(a\). Thus distinct reachable triples are separated by at least one of these three suffixes. The Moore right-congruence consequently has exactly \(m^3/\delta\) classes. This proves the claimed exact state count.

**Step 5: Complementary alternating pattern.** Replacing each zero by a one and each one by a zero is a bijection on binary words and their continuation sets. It carries occurrences of \(010\) to occurrences of \(101\), preserving multiplicities. Therefore their minimal residue-output state complexities coincide. \(\square\)

## Verification

`checker.py` independently constructs the residue-state machine and breadth-first searches its reachable states for every modulus from \(2\) through \(23\). It verifies that the reachable count agrees with \(m^3/\gcd(m,2)\), and that the three-suffix output signature is injective on reachable states. For every binary input of length at most \(13\) and each modulus from \(2\) through \(10\), it directly counts index triples and compares with the transition output. A separate Moore partition-refinement minimization is performed for moduli \(2\) through \(10\). Finally, for moduli \(2\) through \(8\) it independently replays the positive-word generators \(C,D\) and their constructive reaching witnesses. Run `python3 checker.py` from the directory containing the file. The replayed test reports 147447 word-count comparisons, 22 modular reachability checks, 58751 distinguishability checks and 2685 generator/witness checks, and 9 independent output-automaton minimizations. These finite calculations are supporting checks; the proof covers every integer modulus.

## Relationship to prior work

Fazekas, Huang and Mercaş (arXiv:2610.06717, first publicly submitted 2026-10-05) study subsequence universality and containment probabilities for binary languages with exact Parikh-matrix statistics. Their investigated variables include letter counts and the count of \(01\), but their results do not give the minimum deterministic output-state count for the modular \(010\)-counting map. Černý (2010) develops a general algebraic formal-power-series construction for scattered-subword statistics. That construction motivates the finite transition system, but its stated results do not determine the precise modular reachable-orbit cardinality or the parity loss for the present output map. Alazemi and Černý (2011) provide a trie-automaton construction for counting scattered subwords; a complete comparison to their unavailable full text remains a historical-priority risk.

The 2018 paper of Colbourn, Dougherty, Lidbetter and Shallit investigates regularity of languages defined by comparisons between counts of *contiguous* subwords, not this scattered-subsequence residue-output minimization. The distinction between computing all residues and recognizing a single residue is material. The exact count here is also not a consequence of merely enumerating words with a fixed, unbounded number of \(010\) subsequences.

## Limitations

This classification is for modular counts of the two alternating binary patterns of length three, interpreted as output functions over all prefixes. It is not a theorem about the Boolean minimal DFA for a fixed target residue; such an automaton may be smaller. No result is asserted for arbitrary longer patterns, an arbitrary alphabet, or a compressed input encoding. The findings have not undergone independent mathematical validation, and a historical priority claim beyond the sources actually inspected would be unwarranted.

## References

1. S. Z. Fazekas, X. Huang, R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717, first submitted 2026-10-05. https://arxiv.org/abs/2610.06717
2. A. Černý, *Generalizations of Parikh Mappings*, RAIRO Theor. Inform. Appl. 44 (2010), 209–228. https://doi.org/10.1051/ita/2009021 (open text: https://www.numdam.org/article/ITA_2010__44_2_209_0.pdf)
3. H. M. K. Alazemi, A. Černý, *Counting Subwords Using a Trie Automaton*, Int. J. Found. Comput. Sci. 22 (2011), 1457–1469. https://doi.org/10.1142/S0129054111008817
4. C. J. Colbourn, R. E. Dougherty, T. F. Lidbetter, J. Shallit, *Counting Subwords and Regular Languages*, arXiv:1804.11175 (2018). https://arxiv.org/abs/1804.11175
