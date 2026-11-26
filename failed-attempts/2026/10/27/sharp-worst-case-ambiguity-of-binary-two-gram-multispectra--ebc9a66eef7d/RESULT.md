# Sharp worst-case ambiguity of binary two-gram multispectra

## Finding
For a binary linear word \(w=w_1\cdots w_n\), let \(M_2(w)\) be the multiset of its \(n-1\) adjacent ordered pairs. Two words are observationally indistinguishable when their multispectra agree. Let
\[
A(n)=\max_{P}|\{w\in\{0,1\}^n:M_2(w)=P\}|.
\]
For all \(n\ge3\), writing the four residue classes separately, the exact maximum fiber size is
\[
\begin{aligned}
A(4m+1)&=\binom{2m}{m}^{2} &&(m\ge1),\\
A(4m+3)&=\frac{4m+2}{m+1}\binom{2m}{m}^{2} &&(m\ge0),\\
A(4m)&=\frac{4m-1}{m}\binom{2m-2}{m-1}\binom{2m-1}{m-1} &&(m\ge1),\\
A(4m+2)&=\frac{4m+1}{m}\binom{2m-1}{m-1}\binom{2m}{m-1} &&(m\ge1).
\end{aligned}
\]
The boundary values are \(A(1)=2\) (the two one-letter words have the same empty observation) and \(A(2)=1\). In particular,
\[
A(n)\sim\frac{2}{\pi}\frac{2^n}{n}.
\]

The maximizing profiles are also completely classified. Put \((a,u,v,b)=(c_{00},c_{01},c_{10},c_{11})\). For every \(n\ge7\), *all* maximizing profiles satisfy \(u=v\), and they are exactly:
\[
\begin{array}{c|l}
 n & (a,u,v,b)\\\hline
4m+1 & (m,m,m,m)\\
4m+3 & (m,m+1,m+1,m)\\
4m & (m-1,m,m,m),\ (m,m,m,m-1)\\
4m+2 & (m,m,m,m+1),\ (m+1,m,m,m),\ (m-1,m+1,m+1,m),\ (m,m+1,m+1,m-1).
\end{array}
\]
The small cases \(3\le n\le6\) have additional ties: at \(n=3\) the unique maximizing profile is \((0,1,1,0)\); at \(n=4\) the two maximizers have \(u=v=1\) and \(a+b=1\); at \(n=5\) the three maximizers have \(u=v=1\) and \(a+b=2\); and at \(n=6\) all six maximizers have either \(u=v=1,a+b=3\) or \(u=v=2,a+b=1\). In these descriptions \(a,b\) range over all nonnegative solutions.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). Words are *linear*, not cyclic. Multiplicities and the orientations of \(01\) and \(10\) are retained, but endpoints are not separately observed. The fiber consists of all length-\(n\) words, with no quotient by reversal, complementation, or rotation.

For each \(w\), let \(c_{ij}\) denote its number of adjacent occurrences of \(ij\), so \(a+u+v+b=n-1\). Let \(F(a,u,v,b)\) be the fiber cardinality of the corresponding profile.

## Proof
**Exact fibers.** Telescoping along a word shows \(u-v\in\{-1,0,1\}\). Conversely, a profile with \(u+v>0\) and \(|u-v|\le1\) is realized by alternating positive runs with the indicated numbers of transitions.

When \(u=v=r\ge1\), the word may begin/end in either symbol. For endpoints \(00\), there are \(r+1\) zero-runs and \(r\) one-runs, with the \(a\) and \(b\) equal-letter edges distributed as nonnegative excesses across these runs. The \(11\)-endpoint case interchanges the run counts. The positive-composition count gives
\[
\begin{aligned}
F(a,r,r,b)&=\binom{a+r}{r}\binom{b+r-1}{r-1}
+\binom{a+r-1}{r-1}\binom{b+r}{r}\\
&=\frac{a+b+2r}{r}\binom{a+r-1}{r-1}\binom{b+r-1}{r-1}.
\end{aligned}
\]
In particular, the numerator \(a+b+2r\) equals \(n-1\).

When \(\{u,v\}=\{r,r-1\}\), where \(r\ge1\), endpoints differ, and there are \(r\) runs of each symbol. Thus
\[
F(a,r,r-1,b)=F(a,r-1,r,b)
=\binom{a+r-1}{r-1}\binom{b+r-1}{r-1}.
\]
The only zero-transition profiles for \(n\ge2\) are those of the two constant words, each a singleton. For \(n=1\), the single empty multispectrum has fiber size two.

**Balancing the loop counts.** For fixed \(r\ge2\), both products above are maximized by distributing the available value \(a+b\) as evenly as possible. Indeed, when \(a\ge b+2\), replacing \((a,b)\) by \((a-1,b+1)\) strictly increases the product, with multiplicative ratio
\[
\frac{a(b+r)}{(a+r-1)(b+1)}>1,
\]
since the numerator minus the denominator is \((r-1)(a-b-1)>0\). At \(r=1\), the products are constant as \((a,b)\) varies with fixed sum; this accounts for the boundary ties.

**Balanced-transition maxima.** For odd lengths \(n=2t+1\), a balanced-transition profile with \(u=v=r\) has \(a+b=2(t-r)\). Its best possible cardinality is
\[
B_r=\frac{2t}{r}\binom{t-1}{r-1}^{2},\quad 1\le r\le t,
\qquad \frac{B_{r+1}}{B_r}=\frac{(t-r)^2}{r(r+1)}.
\]
The ratio crosses one exactly once, strictly: the maximum is at \(r=m\) if \(t=2m\), and at \(r=m+1\) if \(t=2m+1\). For \(r\ge2\), its loop counts must be \(a=b=t-r\). When \(r=1\), all feasible \((a,b)\) give the same value.

For even lengths \(n=2t+2\), the maximizing loop counts at fixed \(r\) are \(\{a,b\}=\{t-r,t-r+1\}\), and
\[
B_r=\frac{2t+1}{r}\binom{t-1}{r-1}\binom{t}{r-1},\quad 1\le r\le t,
\qquad \frac{B_{r+1}}{B_r}=\frac{(t-r)(t-r+1)}{r(r+1)}.
\]
This ratio is at least one exactly when \(2r\le t\). Therefore the maximum occurs only at \(r=m\) for \(t=2m-1\), or at the two adjacent values \(r=m,m+1\) for \(t=2m\). Again, \(r=1\) may have additional loop-count ties. Substitution gives precisely the displayed four formulas and balanced maximizers.

**Excluding endpoint-imbalanced profiles.** At odd length \(n=2t+1\), the maximal fiber among imbalanced profiles having \(\{u,v\}=\{r,r-1\}\) is
\[
U_r=\binom{t-1}{r-1}\binom{t}{r-1},\qquad
\frac{U_{r+1}}{U_r}=\frac{(t-r)(t-r+1)}{r^2}.
\]
The sequence reaches its peak at \(r_* =\lfloor(t+2)/2\rfloor\) (possibly with an adjacent tie). At that same \(r_*\), compare
\[
\frac{B_{r_*}}{U_{r_*}}=\frac{2(t-r_*+1)}{r_*}.
\]
This is strictly greater than one for \(t=1\) and all \(t\ge3\). At \(t=2\), it equals one but the balanced maximum at \(r=1\) is larger: \(B_1=4>U_2=2\). Thus every imbalanced fiber is strictly smaller than the global balanced maximum for odd \(n\ge3\).

At even length \(n=2t+2\), the imbalanced maximum at fixed \(r\) is
\[
U_r=\binom{t}{r-1}^{2}.
\]
Its peak occurs at \(r_* =\lfloor t/2\rfloor+1\) (possibly tied), and comparison at this parameter gives
\[
\frac{B_{r_*}}{U_{r_*}}=\frac{(2t+1)(t-r_*+1)}{r_*t}>1
\]
for every \(t\ge1\). Hence balanced-transition profiles are the only global maximizers whenever \(n\ge3\). The zero-transition singleton profiles cannot compete. Direct inspection handles \(n=1,2\).

**Asymptotic.** Stirling's approximation \(\binom{2m}{m}\sim4^m/\sqrt{\pi m}\), together with the four exact formulas, gives \(A(n)\sim(2/\pi)2^n/n\).

## Verification
The included `verify.py` requires only the Python standard library. Running `python3 verify.py` independently enumerates every binary word at lengths \(1\) through \(16\), grouping words by literal adjacent-pair profiles; checks exact fiber formulas and sharp extrema; and compares all maximizing profiles with the stated classification. It examines \(131070\) words and \(1083\) observed profiles. A separate all-parameter pass checks another \(2004266\) feasible profiles through length \(200\). The final output begins `VERIFY_OK`. These finite tests are corroborative rather than replacements for the all-length proof.

## Relationship to prior work
The 2016 work of Karhumäki, Puzynina, Rao, and Whiteland gives a general Euler-path method to calculate \(k\)-abelian equivalence-class sizes. Such classes fix endpoint information as well as factor counts. The present observable drops the separate endpoint condition and, for balanced transition counts, combines two endpoint orientations; its object is an exact *global maximization*, including every optimizer and its four residue classes, rather than merely an individual prescribed-type count.

Gabrys and Milenkovic study reconstruction codes from multisets of fixed-length substrings and supply the natural ordered multispectrum model. A published binary read-length-two profile census counts distinct observations and characterizes singleton fibers, but does not determine the largest fiber over those observations. A related length-two *composition* observation merges \(01\) with \(10\) and therefore has different fibers. Jacquet, Knessl, and Szpankowski count cyclic Markov *types* and restrict their binary analysis to balanced cyclic frequency matrices; their type-counting result is distinct from this linear maximal type-*size* problem.

## Limitations
The exact maximum concerns binary linear length-two ordered substring multispectra only. It does not address larger alphabets, longer read lengths, errors, multiplicity-free spectra, or reconstruction algorithms. The structural formula for individual fixed-profile fibers is standard run-composition counting; the asserted contribution is the sharp all-length optimization and classification of every maximal profile. Earlier unindexed work on extremal Markov type classes or independent derivations from known enumeration formulas remains a genuine priority risk. No independent external audit has been performed.

## References
1. J. Karhumäki, S. Puzynina, M. Rao, and M. A. Whiteland, *On cardinalities of k-abelian equivalence classes*, arXiv:1605.03319v1 (first publicly posted 2016-05-11).
2. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548v1 (first publicly posted 2018-04-12).
3. P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI:10.46298/dmtcs.2768.
4. *Exact binary two-multispectrum code size and singleton classification*, public research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-binary-two-multispectrum-code-size-and-singleton-classific--13779c08da71.
5. *Exact binary r=2 length-limited composition reconstruction*, public research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-binary-r-2-length-limited-composition-reconstruction--a98561a7f27e.
