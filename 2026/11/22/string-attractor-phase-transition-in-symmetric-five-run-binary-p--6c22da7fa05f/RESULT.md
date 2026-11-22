# String-attractor phase transition in symmetric five-run binary palindromes

## Finding

Let \(a,b,c\) be arbitrary positive integers and let
\[
W_{a,b,c}=0^a1^b0^c1^b0^a.
\]
A **string attractor** of a finite word is a set of positions such that every distinct nonempty *contiguous* factor has an occurrence containing at least one selected position. Write \(\gamma(W)\) for the minimum number of positions in a string attractor. Then
\[
\boxed{\gamma(W_{a,b,c})=3\quad\Longleftrightarrow\quad
 a\ge2,\ b\ge2,\ c<a,}
\]
and \(\gamma(W_{a,b,c})=2\) otherwise. The statement holds for every positive parameter triple, without a length cutoff, and also after swapping \(0\) and \(1\).

Let \(E_n\) count binary words of length \(n\) belonging to this symmetric five-run family with attractor number three, counting the two choices for the starting symbol separately. Then
\[
\boxed{\sum_{n\ge5}E_nz^n=\frac{2z^9}{(1-z^2)^2(1-z^3)}.}
\]
The corresponding generating function for **all** symmetric five-run binary words is
\[
\sum_{n\ge5}T_nz^n=\frac{2z^5}{(1-z^2)^2(1-z)}.
\]
Consequently, the proportion requiring three positions has the limit
\[
\boxed{\lim_{n\to\infty}\frac{E_n}{T_n}=\frac13.}
\]
The shortest words requiring three positions have length nine, namely \(001101100\) and its bitwise complement. Thus the theorem describes a genuine two-to-three attractor-size transition controlled by the middle zero-run, not merely an example-specific upper bound.

## Assumptions and scope

Each exponent is a positive run length. The word is linear (not circular) and contains exactly five maximal constant runs; complementing all symbols gives the other starting-symbol orientation. Attractors are sets of **symbol positions**, not cuts. Proof indices begin at zero: the first zero-run occupies \([0,a-1]\), the first one-run \([a,a+b-1]\), the central zero-run \([a+b,a+b+c-1]\), the second one-run \([a+b+c,a+2b+c-1]\), and the final zero-run \([a+2b+c,2a+2b+c-1]\). Intervals are inclusive. All factors are nonempty contiguous substrings; different occurrences of the same factor are interchangeable for attraction.

## Proof

**Gap principle.** Let \(\Gamma\) be selected positions. Any factor occurrence avoiding \(\Gamma\) lies completely in a maximal contiguous unselected interval (gap). Therefore \(\Gamma\) attracts every factor if, for every gap, each factor wholly contained in that gap has *some* occurrence meeting \(\Gamma\). We use this elementary equivalence throughout; checking the gap factors suffices to check all factors of every length.

**Case I: \(c\ge a\).** Choose the two zero-based positions
\[
\Gamma=\{a+b-1,\ a+b+c-1\},
\]
namely the last one of the first one-run and the last zero of the central zero-run. The three unselected gaps are, in order, \(0^a1^{b-1}\), \(0^{c-1}\), and \(1^b0^a\), with empty powers interpreted as empty gaps. A pure zero factor in any gap can be placed to end at the selected last central zero, because its length is at most \(c\). A pure one factor can be placed to end at the selected last one of the first one-run, because its length is at most \(b\). A mixed factor from the first gap has form \(0^i1^j\) with \(1\le i\le a\le c\), \(1\le j\le b-1\). Place it at the boundary from the central zeros to the second one-run: this occurrence includes the selected last central zero. A mixed factor from the final gap has form \(1^i0^j\) with \(1\le i\le b\), \(1\le j\le a\le c\); place it at the first one-to-central-zero boundary, where it includes the selected last first-run one. The middle gap contains only zeros. Thus \(\Gamma\) is an attractor of cardinality two.

**Case II: \(c<a\) and \(b=1\).** Choose
\[
\Gamma=\{a-1,\ a+c+1\},
\]
namely the final zero of the first run and the unique one of the second one-run. The gaps are \(0^{a-1}\), \(10^c\), and \(0^a\). All pure-zero gap factors fit across the first selected zero. A mixed factor in the middle gap is \(10^i\) for some \(1\le i\le c<a\); it has an occurrence starting at the second selected one and proceeding into the final zero-run. The lone one is selected. Again the two positions attract every factor.

**Case III: \(c<a\) and \(b\ge2\).** Necessarily \(a\ge2\). The three positions
\[
\Gamma=\{a-1,\ a+b,\ a+2b+c-1\}
\]
are the last initial zero, first central zero, and last second-run one. Their four gaps are \(0^{a-1}\), \(1^b\), \(0^{c-1}1^{b-1}\), and \(0^a\). A pure-zero factor of length at most \(a\) can be placed to end at the selected last initial zero. A pure-one factor of length at most \(b\) can be placed to end at the selected last second-run one. A mixed factor in the third gap is \(0^i1^j\), where \(1\le i\le c-1<a\) and \(1\le j\le b-1\). Its occurrence at the first zero-to-one transition contains the selected last initial zero. Hence three positions suffice.

They are also **necessary**. In this regime the following three factors each have exactly one occurrence in the word:
\[
A=0^a1,\qquad B=1^{b-1}0^c1,\qquad C=10^a.
\]
Their unique occurrence intervals are, respectively,
\[
[0,a],\qquad [a+1,a+b+c],\qquad
[a+2b+c-1,2a+2b+c-1].
\]
The first and third factors cannot use the middle zero-run because \(c<a\); the factor \(B\) must cross the unique pair of consecutive one-runs separated by the entire central zero-run and begin at the second one of the first one-run. The three intervals are pairwise disjoint: the first ends before the second begins, and the second ends before the third begins because \(b\ge2\). Every attractor must hit every uniquely occurring factor interval, so it has at least three positions.

Finally, the word contains both symbols. A one-position set cannot meet an occurrence of each of the different single-letter factors \(0\) and \(1\). Therefore \(\gamma(W)\ge2\) in all cases, and the three cases establish the entire classification.

**Exact enumeration.** In the three-position regime uniquely parameterize
\[
a=2+r+t,\quad b=2+s,\quad c=1+r,
\qquad r,s,t\ge0.
\]
Then \(2a+2b+c=9+3r+2s+2t\). The two possible initial symbols contribute the factor two, giving
\[
\sum_{n\ge5}E_nz^n
=2\sum_{r,s,t\ge0}z^{9+3r+2s+2t}
=\frac{2z^9}{(1-z^3)(1-z^2)^2}.
\]
All positive parameter triples similarly give \(2z^5/((1-z^2)^2(1-z))\). Near \(z=1\), these generating functions have leading terms \(\frac16(1-z)^{-3}\) and \(\frac12(1-z)^{-3}\), respectively. Other unit-circle poles have order at most two, so coefficient extraction gives \(E_n=n^2/12+O(n)\) and \(T_n=n^2/4+O(n)\). Their ratio tends to \(1/3\), completing the proof.

## Verification

Two self-contained Python programs reproduce independent finite tests of the theorem. `verify_exhaustive.py` forms occurrence-position masks for **all** distinct factors, searches every possible two-position set in every triple \(1\le a,b,c\le6\), checks the displayed witness positions, and verifies that no one-position set can work. Its recorded output is in `verify_exhaustive.out`. `verify_independent.py` does not use factor-occurrence masks: it scans literal occurrences of every factor, checks the proposed attracting positions for 305 parameter triples (including larger randomly chosen triples with a fixed seed), checks the exact uniqueness and disjointness of all three lower-bound factors in the applicable cases, and compares coefficients of the rational generating function with direct length-composition counts for every length from 5 through 110. Its output is in `verify_independent.out`.

Run `python3 verify_exhaustive.py` and `python3 verify_independent.py` from the directory containing the files. These calculations are finite corroboration. The all-parameter claims are proved above by the gap method and disjoint unique-factor certificates; the computations are not treated as an infinite proof.

## Relationship to prior work

String attractors were introduced as a repetitiveness measure by Prezza [1] and explored on standard Sturmian, conjugate, and other combinatorial word families by Mantaci et al. [2]. The 2026 Banbara–Bannai–Guo–Köppl–Mieno–Okamoto paper [3] characterizes all minimum attractors for Fibonacci and period-doubling words; a later version additionally treats Thue–Morse words. The October 2026 Thue–Morse study [4] addresses factor-coverage certificates on another structured family. None of these results, as inspected, gives the exact minimum-attractor phase boundary for arbitrary symmetric five-run palindromes.

The accessible published four-run classification [5] determines minimum attractors of \(0^a1^b0^c1^d\); it is not a statement about the five-run words here, and appending a final zero-run can create new uniquely occurring factors. Another published five-run result [6] treats \(0\,1^b0^c1\,0^e\) and identifies when **four** attractor positions are necessary. Its fourth run has length one, its first run has length one, and its parameter domain does not cover the present three-parameter symmetric family except degenerate intersections. Our theorem supplies the exact two-versus-three classification for the palindrome family instead. A separately studied maximal-closed-substring count for the same symmetric word family concerns a different invariant and supplies no attractor-size implication.

The new claim is the sharp all-positive-triples phase transition, explicit minimal-size witnesses, disjoint unique-factor obstruction, rational exception enumerator, and limiting one-third density. Generic exact algorithms for minimum string attractors do not themselves evaluate these formulas. Priority against unindexed statements cannot be established by search alone.

## Limitations

Only symmetric binary five-run palindromes are classified; no assertion is made for arbitrary five-run words, circular attractors, larger alphabets, or the enumeration of *all individual optimal position sets*. The limiting density is conditional on uniform choice among words of the specified five-run family at each length, not among all binary palindromes. Finite scripts check only their stated parameter ranges. Published and indexed searches may miss equivalent earlier statements. No independent mathematical audit is claimed.

## References

[1] N. Prezza, *String Attractors*, arXiv:1709.05314, first public version 2017-09-15, https://arxiv.org/abs/1709.05314.

[2] S. Mantaci, A. Restivo, G. Romana, G. Rosone, M. Sciortino, *String Attractors and Combinatorics on Words*, arXiv:1907.04660, first public version 2019-07-10, https://arxiv.org/abs/1907.04660.

[3] M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, Y. Okamoto, *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, arXiv:2602.16152v1, first public version 2026-02-18 (later versions add Thue–Morse words), https://arxiv.org/abs/2602.16152; CPM 2026 open-access version https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2026.33.

[4] S. Faro, F. P. Marino, A. Pavone, *Smallest String Attractors and Minimal Coverage Certificates of Thue–Morse Words*, arXiv:2610.10950, first public version 2026-10-07, https://arxiv.org/abs/2610.10950.

[5] *Two-versus-three string attractors for every four-run binary word* (2026), public mathematical result at https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-two-versus-three-string-attractors-for-every-four-run-binary-wor--7e2d386038d9.

[6] *Sharp four-position attractor criterion for a five-run binary family* (2026), public mathematical result at https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-four-position-attractor-criterion-for-a-five-run-binary-fa--199f2b51eb0f.
