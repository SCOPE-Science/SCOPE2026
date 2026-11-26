# Exact delay and defect spectra for two-shift pseudoperiods of distinct-run cyclic words

## Finding

Let \(q\geq 2\), let \(a_0,\ldots,a_{q-1}\) be pairwise distinct letters, and let \(r_0,\ldots,r_{q-1}\geq1\) be integers. Write
\[
P=a_0^{r_0}a_1^{r_1}\cdots a_{q-1}^{r_{q-1}},\qquad
p=\sum_{j=0}^{q-1}r_j,\qquad r=\min_j r_j,
\]
and let \(w=P^{\omega}\) be the infinite right-periodic word. A pair \((s,t)\), where \(1\leq s<t\), is a *two-shift pseudoperiod* if for every integer \(i\geq0\), at least one of \(w_{i+s},w_{i+t}\) equals \(w_i\).

**Exact defect and classification theorem.** For any \(1\leq s<t<p\), put \(u=p-t\) and let \([x]_+=\max\{x,0\}\). The number \(F(s,t)\) of residues \(i\in\{0,\ldots,p-1\}\) for which *both* shifted letters differ from \(w_i\) is exactly
\[
F(s,t)=\sum_{j=0}^{q-1}
\bigl[r_j-[r_j-s]_+-[r_j-u]_+\bigr]_+.
\]
In particular,
\[
\boxed{(s,t)\text{ is a two-shift pseudoperiod}
\iff s+(p-t)\leq r.}
\]
Thus the complete set of pseudoperiod pairs with both shifts shorter than the primitive period is
\[
\mathcal P_{<p}=
\{(s,p-u):s,u\geq1,\ s+u\leq r\}.
\]
It has cardinality \(\binom r2\). For every integer delay budget \(1\leq B<p\), the exact number of such pairs satisfying \(t\leq B\) is
\[
\boxed{N(B)=\binom{1+[B-p+r]_+}{2}.}
\]
If \(r=1\), no such pair exists. If \(r\geq2\), the smallest attainable maximum shift is \(p-r+1\), achieved by exactly one pair, \((1,p-r+1)\).

The same classification holds for a finite word consisting of at least **two full copies** of \(P\), using the finite-word pseudoperiod definition with indices restricted to where both shifted letters exist.

## Assumptions and scope

The period contains at least two runs with pairwise different letters, and each letter occurs in exactly one contiguous run per period. All run lengths are positive. The theorem concerns distinct positive shifts strictly below \(p\); a shift equal to \(p\) would be an ordinary period and would make the two-shift condition trivial. The periodic word has least ordinary period \(p\): the ordered boundary \(a_0\to a_1\) occurs exactly once per period and must be preserved by every ordinary period.

The finite-word statement concerns \(P^k\) for every integer \(k\geq2\) and shifts \(1\leq s<t<p\). The result is not asserted for arbitrary words in which the same letter occurs in several separate runs. For example, the primitive-period binary word \((00101)^\omega\) admits \((2,3)\) although its minimum run length is one.

The failure number \(F(s,t)\) is a count of residue classes, not a probability; the fraction of failing indices in any full period is exactly \(F(s,t)/p\).

## Proof

**Step 1: Count matching positions within a single run.** Fix a run of symbol \(a_j\) of length \(R=r_j\), and number its sites by \(x=0,1,\ldots,R-1\). Because every letter occurs in exactly one run per period, a shift \(h\), with \(1\leq h<p\), matches the symbol at site \(x\) precisely when the shifted site falls in this *same* run modulo \(p\).

Since \(0\leq x<R<p\), the integer \(x+h\) is strictly below \(2p\). Consequently a match is possible only in two ways: either \(x+h<R\), or \(p\leq x+h<p+R\). The first possibility is an initial interval of run sites having length \([R-h]_+\). The second is a terminal interval having length \([R-(p-h)]_+\). There are no other matches.

**Step 2: Combine two shifts.** Assume \(s<t\). Of the two initial matching intervals, that for \(s\) contains that for \(t\), because \(R-s>R-t\). Of the two terminal matching intervals, that for \(t\) contains that for \(s\), because \(p-t<p-s\). Thus the positions within this run having at least one match are the union of an initial interval of length \([R-s]_+\) and a terminal interval of length \([R-(p-t)]_+\). The uncovered interval has length
\[
\bigl[R-[R-s]_+-[R-(p-t)]_+\bigr]_+.
\]
Summation over the disjoint runs proves the stated exact formula for \(F(s,t)\). It counts failures in every residue class exactly once.

**Step 3: Characterize zero defect.** Put \(u=p-t\geq1\). For any run length \(R\geq1\), the two intervals in Step 2 cover the entire run if and only if \(s+u\leq R\). Indeed, if \(s\geq R\) or \(u\geq R\), one interval is empty and the other has length strictly less than \(R\), so coverage fails. Otherwise both are nonempty and coverage is equivalent to
\[
(R-s)+(R-u)\geq R\quad\iff\quad s+u\leq R.
\]
Therefore \(F(s,t)=0\) exactly when \(s+u\leq r_j\) for *every* run, equivalently \(s+u\leq r=\min_j r_j\). This proves the pseudoperiod classification.

**Step 4: Enumerate and optimize.** Every solution is uniquely \((s,p-u)\), where \(s,u\) are positive and \(s+u\leq r\). These pairs automatically satisfy \(s<p-u\), because \(p\geq2r\) and \(s+u\leq r\). For each \(u\in\{1,\ldots,r-1\}\), exactly \(r-u\) values of \(s\) are allowed, so
\[
|\mathcal P_{<p}|=\sum_{u=1}^{r-1}(r-u)=\binom r2.
\]
With a delay budget \(t=p-u\leq B\), one must also impose \(u\geq p-B\). If \(B<p-r+1\) there are no solutions. Otherwise set \(h=B-p+r\), so \(1\leq h\leq r-1\); summing the last \(h\) contributions gives \(1+2+\cdots+h=h(h+1)/2\), which is the displayed \(N(B)\). The first allowable budget is \(B=p-r+1\), at which \(u=r-1\) and \(s=1\) are forced. This proves existence and uniqueness of the optimal pair.

**Step 5: Two finite periods suffice.** For \(P^k\), \(k\geq2\), and \(t<p\), the admissible initial positions \(0\leq i<kp-t\) contain all residues \(0,\ldots,p-1\). Each finite shift comparison is periodic in \(i\) with period \(p\). Therefore the finite-word pseudoperiod condition is equivalent to \(F(s,t)=0\), proving the final assertion.

## Verification

The standalone file `verify.py` uses only the Python standard library. It constructs literal cyclic words and independently compares all valid shift pairs against the closed defect formula, the pair classification, the exact delay-budget count, and the two-copy finite-word condition. Run it from this directory with `python3 verify.py`.

Its exhaustive parameter grid comprises \(2{,}537\) run-length tuples, \(157{,}381\) shift pairs, \(28{,}563\) delay-budget cases, and \(157{,}381\) two-copy comparisons, all passing. These finite tests are consistency checks: the proof above, not the tests, establishes the infinite-parameter theorem.

For a concrete nonbinary illustration, let the run lengths be \((3,5,4)\). Then \(p=12\) and \(r=3\), and the complete qualifying set is \(\{(1,10),(1,11),(2,11)\}\). The unique least-maximum-delay choice is \((1,10)\). No pair with larger delay forbidden by the displayed classification has zero defect.

## Relationship to prior work

Meleshko, Ochem, Shallit and Shan introduced and studied the relevant forward-shift definition of pseudoperiodicity, established basic bounds, and proved a general finite-word pseudoperiod decision problem NP-complete (arXiv:2207.10171, first submitted July 20, 2022). Their Proposition 3 bounds run lengths in the binary case; their Theorem 5 bounds alphabet size by the largest pseudoperiod shift; and their Remark 11 gives a general finite-factor checking principle. These results do not provide the complete delay-budget count or phasewise failure spectrum for the present distinct-run cyclic family.

The finite two-copy observation is a direct periodicity consequence of the checking principle and is not asserted as an independently new theorem. The claim assessed here is the *complete numerical and structural classification*: exact bad-phase counts for every pair, all admissible subperiod pairs, their triangular delay-budget enumeration, and the unique optimum. The older notion named pseudoperiodicity in Blondin Massé and collaborators (2012) is explicitly distinguished from the forward-shift definition in Meleshko and collaborators (2022); no identification of the notions is assumed.

## Limitations

Pairwise distinct run symbols are essential; repeated symbols in different runs can produce new shift matches. The formulas concern **two** shifts shorter than \(p\), not arbitrary-sized shift sets, different observation models, nonperiodic texts, or general smallest-pseudoperiod algorithms. Exact finite testing is not exhaustive over all positive parameters. Related results in uncatalogued periodic-word literature may contain an equivalent specialization; the literature comparison is not independent validation.

## References

1. J. Meleshko, P. Ochem, J. Shallit, and S. L. Shan, *Pseudoperiodic Words and a Question of Shevelev*, arXiv:2207.10171v1 (public July 20, 2022), subsequently *Discrete Mathematics & Theoretical Computer Science* 25:2 (2023), DOI: 10.46298/dmtcs.9919. Available at https://arxiv.org/html/2207.10171v3.
2. A. Blondin Massé, S. Gaboury, and S. Hallé, *Pseudoperiodic words*, DLT 2012, Lecture Notes in Computer Science 7410, pp. 308–319. Cited only to distinguish its differently defined notion; not used in the proof.
