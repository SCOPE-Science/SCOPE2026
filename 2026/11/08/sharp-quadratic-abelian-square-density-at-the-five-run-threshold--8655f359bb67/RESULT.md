# Sharp quadratic Abelian-square density at the five-run threshold

## Finding

An *Abelian square* is a nonempty even-length linear word whose first and second halves have the same number of occurrences of every letter. Count distinct contiguous Abelian-square **factors as literal words**, not occurrences and not only Abelian-equivalence classes. Let \(S(w)\) be this count for a binary word \(w\), and let \(M_5(n)\) be the maximum \(S(w)\) among binary words of length \(n\) with exactly five maximal constant-letter runs (\(n\ge5\)). Then

\[
M_5(n)=\frac{n^2}{16}+O(n),\qquad \lim_{n\to\infty}\frac{M_5(n)}{n^2}=\frac1{16}.
\]

By contrast, every binary word of length \(n\) with at most four runs has \(S(w)\le5n\). Thus five is the smallest fixed number of runs permitting quadratically many distinct Abelian-square factors.

More precisely, for positive integers \(a,b,c,d,e\) and \(w=0^a1^b0^c1^d0^e\), the number \(Q(w)\) of distinct Abelian-square factors having **all five runs** is exactly

\[
Q(w)=\begin{cases}
\displaystyle\sum_{i=1}^a\sum_{j=1}^e
\mathbf1_{\{|i-j|\le c,\;c+j-i\equiv0\pmod2\}},& b=d,\\[3pt]
0,&b\ne d,\ b+d\text{ odd},\\
\max\{0,\min(e,a-c)\},&b>d,\ b+d\text{ even},\\
\max\{0,\min(a,e-c)\},&b<d,\ b+d\text{ even}.
\end{cases}
\]

The five-run factors are uniquely encoded by their two end-run lengths. These equations count distinct words, without counting repeated occurrences twice.

## Assumptions and scope

All words are finite, linear (not circular), and over the labeled alphabet \(\{0,1\}\). A run is a maximal consecutive block of identical symbols. The empty word and the empty-half square are excluded. The five-run assertion is invariant under reversing or complementing a word, so it suffices to use the displayed \(0,1,0,1,0\) orientation. The sharp coefficient is an asymptotic statement; no exact finite-length formula for \(M_5(n)\) is asserted.

## Proof

**1. Factors with fewer than five runs cost only \(O(n)\).** Pure-symbol Abelian squares have the form \(0^{2h}\) or \(1^{2h}\), with at most \(n\) distinct choices in total. An Abelian square cannot have exactly two runs: its two halves could not each contain the same positive number of both letters. A three-run factor is \(\sigma^i\tau^u\sigma^j\), with \(i,j,u>0\) and \(\sigma\ne\tau\); it is an Abelian square precisely when \(u\) is even and \(i=j\). The central run is a complete run of the ambient word, so each possible central run contributes at most \(n\) choices. A four-run factor is \(\sigma^i\tau^u\sigma^v\tau^j\), with complete middle runs. If its midpoint is within the second run, equal letter counts force \(i=v\); if within the third, they force \(j=u\). The boundary cases are included. Each choice of its two middle runs therefore permits at most \(2n\) distinct squares. At most four ambient runs yield at most two three-run interiors and one four-run interior: \(S(w)\le n+2n+2n=5n\). With five ambient runs, at most three three-run interiors and two four-run interiors give at most \(8n\) squares whose factors have fewer than five runs.

**2. Exact five-run classification.** Every factor with five runs is uniquely \(0^i1^b0^c1^d0^j\), where \(1\le i\le a\) and \(1\le j\le e\); all three interior runs are complete. Both halves of an Abelian square must contain some ones. If \(b=d\), equality of the one counts forces the midpoint into the middle zero-run (allowing its two boundaries). Writing \(x\) for zeros of this middle run lying in the first half, equality of zero counts says \(i+x=(c-x)+j\), so \(2x=c+j-i\). The constraint \(0\le x\le c\) is equivalent to \(|i-j|\le c\), with the additional parity condition \(c+j-i\equiv0\pmod2\). Conversely those conditions split the factor into two halves with exactly the same Parikh vector. If \(b>d\), equality of one counts places the midpoint strictly inside the first one-run, with \((b+d)/2\) ones to its left. This requires \(b+d\) even, and equality of zero counts then forces \(i=c+j\), giving \(\max\{0,\min(e,a-c)\}\) choices. The case \(b<d\) is symmetric and forces \(j=c+i\). Odd \(b+d\) cannot be split equally. This proves the exact displayed formula.

**3. Continuous band bound.** Let
\[
B(A,E,C)=\operatorname{area}\{(x,y):0\le x\le A,\;0\le y\le E,\;|x-y|\le C\},
\]
for nonnegative real \(A,E,C\), and set \(T=A+E+C\). We claim
\[
B(A,E,C)\le T^2/8.
\]
By symmetry take \(A\ge E\). When \(C\ge E\), \(B\le AE\le E(T-2E)\le T^2/8\). Otherwise \(C<E\le A\). Direct integration of the two excluded triangles gives
\[
B=\begin{cases}
C(A+E)-C^2-\tfrac12(A-E)^2,&A-E\le C,\\
2CE-\tfrac12C^2,&A-E\ge C.
\end{cases}
\]
In both cases \(B\le C(A+E)-C^2=CT-2C^2\le T^2/8\). This proves the claim. Equality in the positive-area case occurs at \(A=E=3T/8\), \(C=T/4\).

**4. Sharp upper coefficient.** If \(b\ne d\), step 2 gives \(Q(w)\le n\). For \(b=d\), let \(H\) count all integer pairs \((i,j)\) with \(1\le i\le a\), \(1\le j\le e\), and \(|i-j|\le c\), before imposing parity. The unit squares attached to these pairs lie in the real band of width \(c+1\), so
\[
H\le B(a,e,c+1)\le (a+e+c+1)^2/8.
\]
For each fixed \(i\), the permissible \(j\)'s form one consecutive integer interval. At most half its elements, rounded upward, have the required parity. Hence \(Q(w)\le (H+a)/2\). As \(a+e+c=n-2b\le n-2\),
\[
Q(w)\le\frac{(n-1)^2}{16}+\frac a2
\le\frac{n^2}{16}+\frac n2.
\]
Adding at most \(8n\) factors with fewer runs gives \(S(w)\le n^2/16+9n\) for every exactly-five-run word.

**5. Sharp lower coefficient.** For every integer \(m\ge1\) take the explicit five-run word
\[
w_m=0^{3m}1\,0^{2m}1\,0^{3m},\qquad |w_m|=8m+2.
\]
Step 2 says its five-run Abelian squares are indexed by ordered pairs \(1\le i,j\le3m\), of the same parity, with \(|i-j|\le2m\). Elementary counting by even differences gives exactly \(4m^2+m\) such pairs (the identity holds for both parities of \(m\)). Thus \(M_5(8m+2)\ge4m^2+m\). For arbitrary large \(n\), choose \(m=\lfloor(n-2)/8\rfloor\) and append \(n-(8m+2)\) zeros to the first run. This retains all earlier square factors and exactly five runs. The lower estimate is \(n^2/16-O(n)\). Combined with step 4, the limit is \(1/16\).

## Verification

The included standalone Python 3 script `verify_abelian_five_run.py` needs no external dependencies. Running `python3 verify_abelian_five_run.py` independently enumerates literal Abelian-square factors of every five-run binary word of length 5 through 19 (11,628 words), checks the exact formula and the \(8n\) residual bound, tests 16,807 additional five-run parameter tuples, checks the explicit family for \(1\le m\le50\), and checks the \(5n\) bound for all words of up to four runs through length 18. Its successful output is `VERIFY_OK five_run_words=11628 grid_cases=16807 construction_cases=50`. These checks are finite corroboration; steps 1–5, not the script, prove the all-length result.

## Relationship to prior work

Kociumaka, Radoszewski, Rytter and Waleń (2016, arXiv:1604.02238, §2 Fact 2.1) established that the unrestricted maximum number of distinct Abelian squares grows quadratically, and their explicit witness \(0^k1\,0^k1\,0^{2k}\) already has exactly five runs. They did not state a five-run sharp leading constant or classify all five-run-square factors. Their §3 Theorem 3.6 bounds the number of **Abelian-inequivalent** squares at a fixed length in terms of the number of runs; it is not an upper bound on the number of distinct literal factors counted here. Fici and Mignosi (2015, arXiv:1506.03562, §3 Proposition 1), and Fici, Mignosi and Shallit (2017, arXiv:1701.00948, §3 Proposition 1), also use \(0^k1\,0^k1\,0^k\) to establish quadratic existence, but not the restricted optimum. The present sharp leading coefficient is a distinct extremal statement, though independent priority verification remains open.

## Limitations

No exact finite-\(n\) formula for the unrestricted five-run maximum or all finite-\(n\) maximizers is proved. The coefficient \(1/16\) concerns binary words with exactly five runs only; no claim is made that this is sharp for unrestricted binary words. The classification concerns factors having all five ambient runs; factors with fewer runs enter only through explicit linear bounds. Historical equivalence in unindexed publications remains possible. No independent audit or certification has been performed.

## References

1. T. Kociumaka, J. Radoszewski, W. Rytter, T. Waleń, *Maximum Number of Distinct and Nonequivalent Nonstandard Squares in a Word*, arXiv:1604.02238, first posted 2016-04-08, https://arxiv.org/abs/1604.02238. In particular §2, Fact 2.1 and §3, Theorem 3.6.
2. G. Fici, F. Mignosi, J. Shallit, *Abelian-Square-Rich Words*, arXiv:1701.00948, first posted 2017-01-04, https://arxiv.org/abs/1701.00948. In particular §3, Proposition 1.
3. OEIS A262249, *Maximum possible number of distinct abelian squares occurring in a binary word of length n*, https://oeis.org/A262249 (unrestricted finite table; not a five-run table).
4. G. Fici, F. Mignosi, *Words with the Maximum Number of Abelian Squares*, arXiv:1506.03562, first posted 2015-06-11, https://arxiv.org/abs/1506.03562. In particular §3, Proposition 1.
