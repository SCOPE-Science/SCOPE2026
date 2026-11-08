# Exact 2-Abelian complexity of two-run periodic binary words and a phase-identifiability threshold

## Finding

Let \(a,b\geq1\) be integers, let \(L=a+b\), and let \(w=(0^a1^b)^\omega\). Write \(p_2(n)\) for the number of 2-Abelian equivalence classes of the distinct length-\(n\) contiguous factors of \(w\), for \(n\geq1\). In other words, factors are identified if they have equal counts of all words of length one or two.

For every \(n\geq1\), let \(r=1+((n-1)\bmod L)\), and set
\[
T(r)=\max\bigl(0,\min(a,r-1)-\max(1,r-b)+1\bigr).
\]
Then the **complete 2-Abelian factor-complexity profile** is
\[
\boxed{p_2(n)=[r\leq a]+[r\leq b]+2T(r)+[r\geq a+2]+[r\geq b+2],}
\]
where \([\mathcal{P}]\) is one if the condition \(\mathcal{P}\) holds and zero otherwise. Consequently the profile is periodic with period \(L\) (not necessarily least period), and
\[
\boxed{\max_{n\geq1}p_2(n)=\min\{a+b,\,2\min(a,b)+2\}.}
\]
Moreover, **there exists a length that distinguishes all \(L\) starting phases by their 2-Abelian signatures if and only if** \(\lvert a-b\rvert\leq2\). If \(\lvert a-b\rvert>2\), at least \(\lvert a-b\rvert-2\) phases necessarily collapse at every length, in the sense that at most \(L-(\lvert a-b\rvert-2)\) distinct phase signatures occur.

## Assumptions and scope

The alphabet is precisely \(\{0,1\}\), with nonempty runs of respective lengths \(a\) and \(b\). Factors are contiguous and may cross any number of period boundaries. The 2-Abelian signature of a nonempty word comprises counts of the letters \(0,1\) and of the digrams \(00,01,10,11\), counting overlapping digram occurrences. A phase is one of the \(L\) starting indices modulo \(L\). The word has minimal ordinary period \(L\), since it has exactly one cyclic transition of each orientation in a period. The counts concern distinct equivalence classes, not weighted occurrences.

## Proof

**1. Period reduction.** Fix a phase \(s\) modulo \(L\). Extending the factor starting at \(s\) from length \(n\) to length \(n+L\) appends one entire cyclic period. Its counts of \(0\) and \(1\) increase by \(a,b\), respectively, and its counts of \(00,01,10,11\) increase by \(a-1,1,1,b-1\), respectively. These increments are *independent of the phase*: the \(L\) newly included adjacent pairs traverse exactly one full cyclic period. Thus all phase-signature vectors undergo the same translation. Equality and inequality between any two phase signatures are preserved, so \(p_2(n+L)=p_2(n)\) for all \(n\geq1\). It suffices to examine \(1\leq r\leq L\).

**2. Exhaustive run shapes.** Every length-\(r\) factor with \(r\leq L\) has at most two symbol transitions. The factors with zero transitions are \(0^r\), if \(r\leq a\), and \(1^r\), if \(r\leq b\). The one-transition factors are \(0^x1^{r-x}\) and \(1^{r-x}0^x\) with
\[
\max(1,r-b)\leq x\leq\min(a,r-1).
\]
Each orientation therefore supplies \(T(r)\) different words. Different choices of \(x\) have different digram counts, and the two orientations have different first letters.

The two-transition factors are either \(0^x1^b0^y\), where \(x,y\geq1\) and \(x+y=r-b\), or \(1^x0^a1^y\), where \(x,y\geq1\) and \(x+y=r-a\). Since \(r\leq a+b\), each possible split fits the surrounding cyclic runs. The first type exists exactly when \(r\geq b+2\), the second exactly when \(r\geq a+2\). Within a type all splits have identical counts of letters and of digrams. For instance, \(0^x1^b0^y\) has \(r-b\) zeros, \(b\) ones, \(r-b-2\) occurrences of \(00\), \(b-1\) of \(11\), and one of each \(01,10\). Accordingly each type contributes exactly one class.

**3. Distinctness of the listed classes.** Equality of letter and digram counts forces equality of the first and last symbols: the initial-symbol indicator is obtained from each letter count minus the number of digrams ending at that letter; similarly the terminal indicator comes from counts minus digrams beginning at that letter. In particular the six descriptions (two constant types, two one-transition orientations, two two-transition types) are pairwise 2-Abelian-inequivalent across types whenever present, except that all split variants within a given two-transition type have just been combined. The one-transition family distinguishes its exponent choices by the \(00\) and \(11\) counts. Summing the listed contributions yields exactly the boxed formula.

**4. Sharp maximum.** Put \(m=\min(a,b)\), \(M=\max(a,b)\). For \(r\leq m\), the formula simplifies to \(p_2(r)=2r\); for \(m<r\leq M\), it is at most \(2m+2\); and for \(M<r\leq L\), the one-transition multiplicity is \(T(r)=L-r+1\leq m\), while the other contributions still give \(p_2(r)\leq2m+2\). Always \(p_2(r)\leq L\), because there are only \(L\) phases.

The upper bound \(\min\{L,2m+2\}\) is achieved: when \(M=m\), take \(r=m\) (giving \(2m=L\)); when \(M=m+1\), take \(r=m+1\) (giving \(2m+1=L\)); and when \(M\geq m+2\), take \(r=m+2\) (giving \(2m+2\)). This proves the maximum formula, including \(m=1\).

**5. Phase-identifiability threshold.** The maximum equals \(L\) exactly when \(M\leq m+2\). Equality means that all \(L\) starting phases have different 2-Abelian signatures, and strict inequality means no length can distinguish them all. When \(M>m+2\), the shortfall is \(L-(2m+2)=M-m-2=\lvert a-b\rvert-2\). The claimed threshold and quantitative loss follow.

## Verification

The standalone file `verify.py` directly builds length-\(n\) factors from a repeated period, counts their overlapping digrams directly, groups their full 2-Abelian signatures, and compares this count with the formula. It checks \(1\leq a,b\leq14\), \(1\leq n\leq2(a+b)+4\) (6,664 separate length profiles), and separately checks the sharp maximum and phase-identifiability criterion for all 196 pairs. It uses only the Python standard library. Run `python verify.py` alongside this file. These finite checks are a reproducibility aid; the proof above establishes the statement for arbitrary positive parameters.

For \((a,b)=(3,5)\), a full residue period of complexity values is \((2,4,6,7,8,7,6,4)\). For \((a,b)=(1,8)\), it is \((2,3,4,4,4,4,4,4,3)\). These illustrate the transition from full phase recovery to permanent ambiguity.

## Relationship to prior work

The notion of \(k\)-Abelian complexity and its connection to periodicity were introduced and studied by Karhumäki, Saarela, and Zamboni (2013), especially their definitions and Section 3; their general periodicity implications do not provide this two-parameter 2-Abelian complexity formula. Parreau, Rigo, Rowland, and Vandomme (2014) studied 2-Abelian complexity of the Thue–Morse and period-doubling words using automatic-sequence methods; those words and their derived complexity statements differ from the present purely periodic two-run family. The survey by Fici and Puzynina (first publicly available 20 July 2022, Section 8.1) presents 2-Abelian complexity and its known classes but does not state this exact cyclic run-family spectrum. A related published finding counts all binary adjacent-pair multispectra without fixing a cyclic source family; its global class count does not imply these phase-restricted lengths or sharp identification boundary. These are comparisons of mathematical scope, not proof of bibliographic uniqueness.

## Limitations

This theorem applies only to the alternating two-run periodic family over two letters and to 2-Abelian equivalence; it does not supply general \(k\)-Abelian formulas for \(k>2\), or formulas for periodic words with three or more runs in their primitive period. An equivalent formulation may exist under digram-count or cyclic phase reconstruction terminology that was not indexed or located.

## References

1. J. Karhumäki, A. Saarela, L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104 (first posted 22 January 2013). https://arxiv.org/abs/1301.5104
2. A. Parreau, M. Rigo, E. Rowland, E. Vandomme, *A new approach to the 2-regularity of the \(\ell\)-abelian complexity of 2-automatic sequences*, arXiv:1405.3532 (first posted 14 May 2014). https://arxiv.org/abs/1405.3532
3. G. Fici, S. Puzynina, *Abelian Combinatorics on Words: a Survey*, arXiv:2207.09937v1 (first posted 20 July 2022), Section 8.1. https://arxiv.org/abs/2207.09937
