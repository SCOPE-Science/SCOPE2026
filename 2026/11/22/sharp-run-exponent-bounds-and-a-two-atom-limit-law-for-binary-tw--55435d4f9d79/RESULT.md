# Sharp run-exponent bounds and a two-atom limit law for binary two-marker words

## Finding
A **run** is a maximal interval with least positive period \(p\), length at least \(2p\), and no one-symbol extension of the same period. Its exponent is its length divided by \(p\). Write \(E(w)\) for the sum of exponents of all runs of a finite word \(w\), counting occurrences rather than distinct factor spellings.

Every binary word with exactly two ones has the unique form
\[
w=0^a1\,0^b1\,0^c,\qquad a,b,c\in\mathbb Z_{\ge0},\qquad n=a+b+c+2.
\]
For \(g\ge0\), put \(h(g)=g\) for \(g\ge2\) and \(h(g)=0\) for \(g\le1\). If \(b=0\), then
\[
E(w)=h(a)+2+h(c).
\]
If \(b\ge1\), put \(p=b+1\) and \(L=p+1+\min(a,b)+\min(c,b)\). Then the exact all-parameter formula is
\[
\boxed{E(w)=h(a)+h(b)+h(c)+\mathbf1_{\{L\ge2p\}}\frac{L}{p}.}
\tag{1}
\]
In particular, for every \(n\ge8\), with \(P=\lfloor(n+1)/3\rfloor\),
\[
\boxed{\max_{|w|=n,\,|w|_1=2} E(w)=n+1-\frac1P.}
\tag{2}
\]
All maximizers, and no others, have gap parameters
\[
\boxed{(a,b,c)=(P-1+i,\ P-1,\ P-1+R-i),\quad 0\le i\le R,\quad R=n-3P+1.}
\tag{3}
\]
Here \(R\in\{0,1,2\}\), so precisely \(R+1\) distinct words attain the maximum. For \(4\le n\le7\), the maximum instead equals \(n\).

For uniform random \(W_n\) among the \(\binom n2\) binary length-\(n\) words with exactly two ones, put \(Y_n=E(W_n)-n\). Then \(Y_n\) converges in distribution to \(Y\) with two atoms and one absolutely continuous part:
\[
\boxed{\mathbb P(Y=-2)=\frac14,\quad \mathbb P(Y=1)=\frac13,\quad f_Y(y)=\frac6{(2+y)^3}\ \ (0<y<1).}
\tag{4}
\]
There is no other mass. Equivalently \(\mathbb P(Y\ge t)=3/(2+t)^2\) for \(0<t<1\). In particular, \(\mathbb E Y_n\to0\) and \(\operatorname{Var}(Y_n)\to6\log(3/2)-1\). The atom at one is a **limit** atom; finite words cannot attain the limiting upper excess of exactly one in the regime \(n\ge8\).

## Assumptions and scope
The alphabet is \(\{0,1\}\), words are finite and linear, and the symbol one occurs exactly twice, including the possibility of adjacent ones or zero-length outer gaps. The least period and maximality are essential: ordinary maximal constant runs, distinct squares, and nonmaximal periodic factors are different statistics. All bounds and rational exponents are exact. The weak limit uses a uniform distribution on labeled position pairs, not on reversal equivalence classes. The parent literature studies the same sum-of-exponents statistic for unrestricted words, but (1)–(4) are restricted fixed-content statements.

## Proof
**1. Exhaustion of all runs.** A run of least period one is a maximal constant block of length at least two. Thus each zero gap \(g\in\{a,b,c\}\) contributes exponent \(h(g)\); if \(b=0\), the adjacent pair of ones contributes a period-one run of exponent two. Suppose \(b\ge1\) and a run has least period \(p\ge2\). Any periodic factor of length at least \(2p\) consists of two equal consecutive \(p\)-blocks plus possibly a tail. Consequently, any symbol one present in the factor occurs at least twice in positions separated by exactly \(p\). Since the host contains only two ones, both must lie in the factor, and their separation forces \(p=b+1\). There can be no additional non-unary run of another period. The resulting maximal interval has least period \(p\): any smaller period \(q<p\) in an interval of length at least \(2p\) would force a second one at displacement \(q\) from a one, contradicting that the only two ones are separated by \(p\).

**2. Exact maximal non-unary interval.** The span from the first one to the second inclusive has length \(p+1\). Period \(p\) may be extended to the left by exactly \(\min(a,p-1)=\min(a,b)\) zeroes and to the right by exactly \(\min(c,p-1)=\min(c,b)\) zeroes. Extension by a further zero, if available, would require a third one at the corresponding translated position, so this span is maximal. Its length is \(L\). It qualifies as a run precisely when \(L\ge2p\). This proves (1); if \(b=0\), the period-one classification gives the separate formula.

**3. Sharp extremum.** Assume \(n\ge8\) and set \(P=\lfloor(n+1)/3\rfloor\ge3\). Cases without a non-unary run have \(E(w)\le n-2\) when \(b\ge1\), while \(b=0\) gives \(E(w)\le n\); both are strictly smaller than (2). In the remaining cases write \(p=b+1\), \(x=\min(a,p-1)\), \(z=\min(c,p-1)\), and let \(\delta\) be the number of gaps among \(a,b,c\) equal to one. The total length in nontrivial zero runs is \(n-2-\delta\). Hence
\[
E(w)=n-1-\delta+\frac{1+x+z}{p},\qquad x+z\le\min\{2p-2,n-p-1\}.
\tag{5}
\]
For \(p\le P\), (5) yields \(E(w)\le n+1-1/p\le n+1-1/P\). For \(p>P\), use \(n\le3P+1\) and \(p\ge P+1\) to obtain
\[
E(w)\le n-2+\frac np\le n-2+\frac{3P+1}{P+1}=n+1-\frac2{P+1}<n+1-\frac1P.
\]
Equality is therefore possible only for \(p=P\), \(\delta=0\), and \(x=z=p-1\), i.e. \(b=P-1\) and \(a,c\ge P-1\). Since \(a+c=n-P-1\), all and only the triples in (3) occur. Conversely, these triples yield \(L=3P-1\ge2P\) and equality in (5). For \(4\le n\le7\), a non-unary run can only have period \(p=2\) or \(p=3\). Period two means \(b=1\), so \(\delta\ge1\) and (5) gives \(E(w)<n\). Period three requires \(n\ge6\); when \(n=6\), (5) gives \(E(w)\le6\). When \(n=7\), the outer gaps sum to three: if both are nonzero then \(\delta\ge1\) and (5) gives \(E(w)<7\), while if one is zero then \(L\le6\), and the other zero gap and the middle gap contribute at most five in total, so \(E(w)\le7\). If there is no non-unary run, or \(b=0\), then \(E(w)\le n\) directly. The word \(11\,0^{n-2}\) attains \(n\) for each of these lengths.

**4. Geometric limit.** For a uniform position pair, the gaps \((a,b,c)\) are uniformly distributed over nonnegative integer triples summing to \(n-2\). Dividing by \(n-2\) gives convergence to the uniform distribution on the simplex \(A+B+C=1\), \(A,B,C\ge0\), with planar density two in coordinates \((A,B)\). The probability of any gap being zero or one tends to zero. Away from boundaries, the condition \(L\ge2p\) converges to \(\min(A,B)+\min(C,B)\ge B\), equivalent to \(B\le\frac12\). Thus the limiting excess is
\[
Y=\begin{cases}-2,&B>\frac12,\\-1+\dfrac{\min(A,B)+\min(C,B)}{B},&0<B<\frac12.\end{cases}
\tag{6}
\]
These piecewise-continuous expressions establish weak convergence since the partition boundaries have zero simplex area. The region \(B>1/2\) has area probability \(2\int_{1/2}^1(1-B)\,dB=1/4\). The region \(A\ge B\) and \(C\ge B\) gives \(Y=1\), with probability \(2\int_0^{1/3}(1-3B)\,dB=1/3\).

For \(0<t<1\), the condition \(Y\ge t\) in (6) is equivalent to
\[
0<B\le\frac1{2+t},\qquad tB\le A\le1-(1+t)B.
\]
The allowable interval of \(A\) has length \(1-(1+2t)B\). Consequently
\[
\mathbb P(Y\ge t)=2\int_0^{1/(2+t)}\big(1-(1+2t)B\big)\,dB=\frac3{(2+t)^2}.
\]
Its derivative gives the stated density on \((0,1)\). The continuous mass is \(5/12\), so together with the two atoms it sums to one. Direct integration gives \(\mathbb EY=0\) and \(\mathbb EY^2=6\log(3/2)-1\). Since (1)–(2) bound the centered quantities uniformly for \(n\ge8\), weak convergence implies convergence of the first two moments. This completes the proof.

## Verification
The included standalone `verify.py` checks the exact run decomposition with an independent direct interval/least-period enumerator for **all 2,600** binary words with exactly two ones and lengths two through twenty-five. It verifies (2) and the complete equality cases exhaustively for lengths eight through twenty-five, and also checks 873 seeded random gap triples of length at most seventy-five. It enumerates the exact formula for lengths 60, 120, 240, 480, and 960 to illustrate convergence; those finite numerical comparisons are not the infinite proof. Run `python3 verify.py` with Python 3 standard library only. The actual captured output is `verification_output.txt`.

## Relationship to prior work
The problem of estimating the maximum sum of exponents of maximal repetitions over **unrestricted** binary words is studied by Czarkowski (CPM 2026), which establishes the global bound \(E(w)\le2.2|w|\). Earlier general bounds and constructions were given by Crochemore, Kubica, Radoszewski, Rytter and Waleń (2010/2012). These bounds do not specify the exact two-one-constrained maximum, its maximizers, or a random fixed-weight limit. Glen and Simpson (2013) study the **sum of run lengths**, not exponents, and their general average does not imply (4). A publicly indexed result on the complete **number of runs** for words of weight three supplies a different statistic and input class; its claim does not imply the length-over-period sum. The proof here is elementary and self-contained; no priority assertion stronger than the comparisons actually made is implied.

## Limitations
The theorem does not solve unrestricted run-exponent extremization, nor does it treat binary words of greater fixed weight or cyclic words. It assumes ordinary exact periodicity, not approximate runs. The continuous law is a large-length fixed-content limit; its atoms need not occur as exact finite-length excess values. Exhaustive testing is supplementary to, and not a substitute for, the proof. Unindexed equivalent earlier classifications remain a residual priority risk.

## References
1. A. Czarkowski, *Improved Bounds on the Sum of Exponents of Runs in a String*, CPM 2026, DOI:10.4230/LIPIcs.CPM.2026.23. Public proceedings dated 2026-06-08. https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.23/LIPIcs.CPM.2026.23.html
2. M. Crochemore, M. Kubica, J. Radoszewski, W. Rytter and T. Waleń, *On the Maximal Sum of Exponents of Runs in a String*, arXiv:1003.4866, first posted 2010-03-25. https://arxiv.org/abs/1003.4866
3. A. Glen and J. Simpson, *The total run length of a word*, arXiv:1301.6568, first posted 2013-01-28. https://arxiv.org/abs/1301.6568
4. *Exact run spectrum of binary words with three marked ones*, publicly indexed research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-run-spectrum-of-binary-words-with-three-marked-ones--195f68bb7ba1 .
