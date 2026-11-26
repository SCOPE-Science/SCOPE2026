# Sharp worst-case ambiguity and extremal profiles of binary length-two multispectra

## Finding
For each integer \(n\ge1\), let the linear length-two multispectrum of \(w\in\{0,1\}^n\) be the multiset of its \(n-1\) overlapping adjacent pairs. Let \(M_n\) denote the largest number of binary length-\(n\) words realizing one such multiset.

We have \(M_1=2,\ M_2=1\). For every \(n\ge3\), put \(h=\lfloor(n-3)/4\rfloor\), \(A=\lfloor(n-3)/2\rfloor\), and \(B=\lceil(n-3)/2\rceil\). Then
\[
M_n=\frac{n-1}{h+1}\binom{A}{h}\binom{B}{h},\qquad
M_n\sim\frac{2}{\pi}\frac{2^n}{n}.
\]
All maximizing spectra have the same counts of `01` and `10`. For \(n\ge7\), write \(N=n-1\), \(q=\lfloor N/2\rfloor\), and \(r=\lceil N/2\rceil\). The maximizing quadruples of counts in order (`00`,`01`,`10`,`11`) are exactly
\[
(q-t,t,t,r-t),\quad(r-t,t,t,q-t),
\]
with \(t=h+1\), together with the same two possibilities for \(t=h+2\) when \(n\equiv2\pmod4\). Duplicates are counted once. Hence the numbers of maximizing spectra as \(n\equiv3,0,1,2\pmod4\) are respectively \(1,2,1,4\) for \(n\ge7\). For \(3\le n\le10\), the maxima are \(2,3,4,5,12,21,36,54\). Ranks \(3\) through \(6\) have some additional off-center equality profiles.

## Assumptions and scope
The alphabet is \(\{0,1\}\), the word is *linear*, all length-two factors are contiguous, and multiplicities are retained. This is a worst-fiber theorem, not a count of distinct spectra or an optimum reconstruction code. No longer reads, incomplete observations, or nonbinary alphabets are claimed.

## Proof
Write \(a=c_{00}\), \(d=c_{11}\), \(N=n-1\). A word with \(c_{01}=c_{10}=t\ge1\) starts and ends with the same bit. If this bit is zero, it has \(t+1\) nonempty zero-runs and \(t\) nonempty one-runs, so distributing the additional \(a\) zero and \(d\) one adjacencies gives \(\binom{a+t}{t}\binom{d+t-1}{t-1}\) words. Starting and ending with one gives \(\binom{a+t-1}{t-1}\binom{d+t}{t}\). Writing \(q=a+t\), \(r=d+t\) and noting \(q+r=N\) gives the balanced-fiber formula
\[
F_{\mathrm{bal}}(a,d,t)=\frac{N}{t}\binom{q-1}{t-1}\binom{r-1}{t-1}. \tag{1}
\]
When the two transition counts differ by one, write their minimum as \(t\). The opposite endpoints force \(t+1\) nonempty runs of each bit. Thus, with \(q=a+t\), \(r=d+t\), \(q+r=N-1\), the fiber size is
\[
F_{\mathrm{trail}}(a,d,t)=\binom qt\binom rt.\tag{2}
\]
Transition counts can differ only by zero or one, because their signed difference telescopes to the last bit minus the first bit. With no transitions, only the two constant words are realizable, each in its own singleton profile.

For any fixed \(t\ge1\), the product \(\binom{q-1}{t-1}\binom{r-1}{t-1}\) at \(q+r=N\) is maximized at \(q=\lfloor N/2\rfloor\), \(r=\lceil N/2\rceil\): the binomial coefficient, as a function of the top index, is log-concave and its product is symmetric. For \(t\ge2\), the maximizer is unique up to exchanging \(q,r\); for \(t=1\), the fiber is the constant \(N\). Consequently, with \(k=t-1\), \(A=\lfloor(N-2)/2\rfloor\), \(B=\lceil(N-2)/2\rceil\), the balanced optimum at that \(k\) is
\[
B_n(k)=\frac{N}{k+1}\binom Ak\binom Bk.\tag{3}
\]

Unequal-transition spectra cannot beat this. At any fixed \(t\), formula (2) is similarly largest for \(q=\lfloor(N-1)/2\rfloor\), \(r=\lceil(N-1)/2\rceil\). The product \(\binom qt\binom rt\) has a maximizing mode satisfying \(t\le r/2\): when \(q=r\), choose the lower binomial mode; when \(r=q+1\), this follows from the ratio of consecutive terms. If the optimum has \(t=0\), its fiber has size one. Otherwise, choose the feasible balanced spectrum with \(t'=t+1\), \(q'=q+1\), \(r'=r\). Dividing its size (1) by (2) gives
\[
\frac{N}{t+1}\frac{r-t}{r}\ge\frac{r}{t+1}\ge\frac{2t}{t+1}\ge1,
\]
where \(N=q+r+1\ge2r\). Equality in all these bounds can only occur for \(t=1,r=2,q=1\), at length five, where the balanced optimum is four and the imbalanced optimum two. Hence an imbalanced profile never maximizes globally.

The ratio of the successive quantities in (3) is
\[
\frac{B_n(k+1)}{B_n(k)}=\frac{(A-k)(B-k)}{(k+1)(k+2)}.
\]
Its numerator minus denominator is \(AB-(A+B+3)k-2\), strictly decreasing in \(k\). Checking the four residue classes of \(n\) modulo four shows that its mode is \(k=h=\lfloor(n-3)/4\rfloor\), uniquely except that \(k=h+1\) ties when \(n\equiv2\pmod4\). This includes the small boundary ranks \(3\) through \(6\). Formula (3) proves the closed expression. For \(n\ge7\), the optimal \(k\ge1\), so the strict log-concavity assertion also proves exactly the claimed equality-profile classification.

For asymptotics, at \(n=4m+5\) formula (3) simplifies to \(M_{4m+5}=4\binom{2m+1}{m}^2\). Stirling's formula yields \(M_{4m+5}\sim (2/\pi)2^{4m+5}/(4m+5)\). The other three residue classes have the same limiting coefficient by the identical central-binomial estimates in (3), proving the complete asymptotic.

## Verification
The standalone `verify.py` independently enumerates literal binary words of lengths one through seventeen and checks the exact maxima, every observed profile-fiber count, and all maximizing spectra for lengths at least seven. An additional exact-arithmetic census checks all feasible profiles through length one hundred twenty. Run `python verify.py` using Python 3.9 or later with no third-party packages. Finite checks corroborate, but do not establish, the infinite theorem.

## Relationship to prior work
Huova and Karhumäki's 2011 paper defines \(2\)-Abelian equivalence in terms of adjacent-factor counts and endpoints. The linear multispectrum equivalence is **coarser** than \(2\)-Abelian equivalence because balanced transition profiles may merge the two possible endpoint orientations; this distinction is essential to the maximum. Jacquet, Knessl, and Szpankowski count Markov types of cyclic words. Gabrys and Milenkovic define linear substring multispectra and reconstruction codes, concentrating chiefly on larger read lengths.

The closest accessible prior mathematical result, *Exact binary two-multispectrum code size and singleton classification*, gives the number of feasible profiles and the full formulas for *each given profile's fiber size*. Those underlying local counts are therefore not claimed as new. The present contribution is the all-length **global maximization** of those counts, strict balanced-versus-trail domination, complete maximizing-profile classification, and sharp \(2/\pi\) asymptotic constant. None of these optimized conclusions appears in the inspected earlier result. An equivalent optimization under a different name remains an originality risk.

## Limitations
The theorem does not address noisy or partial spectra, longer reads, or larger alphabets. Its starting run-composition formulas are known; the additional claim concerns their nontrivial global extremal optimization. Independence has not been established and no independent audit has been performed.

## References
1. M. Huova and J. Karhumäki, *Observations and Problems on k-Abelian Avoidability*, arXiv:1104.4273, initially posted April 21, 2011.
2. P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI:10.46298/dmtcs.2768; publisher metadata shows December 31, 2009.
3. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548 (2018).
4. *Exact binary two-multispectrum code size and singleton classification*, publicly accessible mathematical note, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-binary-two-multispectrum-code-size-and-singleton-classific--13779c08da71/RESULT.md .
