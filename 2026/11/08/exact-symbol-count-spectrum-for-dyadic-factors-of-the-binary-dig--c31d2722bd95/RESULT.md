# Exact symbol-count spectrum for dyadic factors of the binary digit-sum word modulo three

## Finding
Let \(s_2(n)\) be the number of ones in the base-two representation of \(n\geq0\), and put \(t(n)=s_2(n)\bmod3\in\{0,1,2\}\). For every integer \(k\ge0\), set \(N=2^k\). Fix **any** letter \(j\in\{0,1,2\}\), and let \(Q_{k,j}(i)\) be its number of occurrences in the contiguous factor \(t(i)t(i+1)\cdots t(i+N-1)\), for \(i\ge0\).

Then the set of all attainable counts is the entire integer interval
\[
\{Q_{k,j}(i):i\ge0\}=\{L_k,L_k+1,\ldots,U_k\},
\]
where, for \(h\ge0\),
\[
\begin{aligned}
L_{2h}&=\frac{2^{2h}-1}{3}-h,& U_{2h}&=\frac{2^{2h}-1}{3}+h+1,\\
L_{2h+1}&=\frac{2^{2h+1}+1}{3}-h-1,& U_{2h+1}&=\frac{2^{2h+1}+1}{3}+h+1.
\end{aligned}
\]
In particular, **each symbol has exactly \(k+2\) attainable counts in factors of length \(2^k\)**, and the maximum difference in the number of occurrences of a fixed symbol between two such factors is exactly \(k+1\). These assertions include \(k=0\) and are independent of the chosen symbol.

## Assumptions and scope
All positions and indices are nonnegative integers; factors are contiguous, not scattered. The underlying word is the infinite fixed point of \(0\mapsto01\), \(1\mapsto12\), \(2\mapsto20\). Counts refer to a *single specified letter*, not to digit sums or to complete Parikh vectors. The result concerns precisely dyadic factor lengths; no formula for arbitrary lengths or the full two-dimensional Parikh spectrum is claimed.

## Proof
**1. Dyadic blocks and possible boundary phases.** For \(k\ge0\), define the aligned block residue counts and their prefixes by
\[
C_{k,a}=\#\{0\le v<2^k:s_2(v)\equiv a\pmod3\},\qquad P_{k,a}(r)=\#\{0\le v<r:s_2(v)\equiv a\pmod3\},
\]
with \(a\) reduced modulo \(3\), \(0\le r\le2^k\), and \(P_{k,a}(2^k)=C_{k,a}\). Write \(D_{k,a,b}(r)=P_{k,b}(r)-P_{k,a}(r)\).

Every starting index has a unique form \(i=q2^k+r\), \(0\le r<2^k\). The two aligned dyadic blocks met by its length-\(2^k\) factor have letter phases \(x=s_2(q)\bmod3\) and \(y=s_2(q+1)\bmod3\). The count of a fixed letter \(j\) in the factor is therefore
\[
C_{k,j-x}-P_{k,j-x}(r)+P_{k,j-y}(r)=C_{k,a}+D_{k,a,b}(r),\quad a=j-x,\ b=j-y\pmod3.
\]
**All nine ordered pairs \((a,b)\) really occur.** Indeed, choose nonnegative integers \(u,v\) so that \(u\equiv x-y+1\pmod3\) and \(v\equiv y-1\pmod3\), and let \(p=2^v-1\), \(q=2^{u+1}p+2^u-1\). Then \(s_2(q)=u+v\equiv x\) and \(s_2(q+1)=v+1\equiv y\). In the case \(r=2^k\), which is used in the convenient closed-prefix formulas below, the resulting count is \(C_{k,b}\); this is realized by the aligned block beginning at \((q+1)2^k\), even though the canonical offset is then zero. Hence inclusion of both prefix endpoints does not add any spurious attainable count.

**2. An exact three-letter prefix-extremum recurrence.** Put
\[
m_{k,a,b}=\min_{0\le r\le2^k}D_{k,a,b}(r),\qquad M_{k,a,b}=\max_{0\le r\le2^k}D_{k,a,b}(r).
\]
At \(k=0\), \(C_0=(1,0,0)\), and \(m_{0,a,b}=\min(0,\mathbf1_{b=0}-\mathbf1_{a=0})\), with \(M\) obtained by replacing \(\min\) by \(\max\). Since \(s_2(2^k+v)=s_2(v)+1\) for \(0\le v<2^k\), splitting a prefix at \(2^k\) proves the exact recurrences
\[
\begin{aligned}
C_{k+1,a}&=C_{k,a}+C_{k,a-1},\\
m_{k+1,a,b}&=\min\{m_{k,a,b},\ C_{k,b}-C_{k,a}+m_{k,a-1,b-1}\},\\
M_{k+1,a,b}&=\max\{M_{k,a,b},\ C_{k,b}-C_{k,a}+M_{k,a-1,b-1}\}.
\end{aligned}
\]
All residue subscripts in these expressions are modulo \(3\). We also have \(m_{k,a,b}=-M_{k,b,a}\) and \(m_{k,a,a}=M_{k,a,a}=0\). The following small table is obtained by **exact substitution into these displayed recurrences**, beginning with the stated \(k=0\) initialization. In each ordered-pair column, the displayed entry is \((m,M)\).

| \(k\) | \((C_{k,0},C_{k,1},C_{k,2})\) | \((0,1)\) | \((0,2)\) | \((1,2)\) | \((L_k,U_k)\) |
|---:|---|---|---|---|---|
| 2 | (1,2,1) | (-1,1) | (-1,0) | (-2,0) | (0,3) |
| 3 | (2,3,3) | (-1,2) | (-1,2) | (-2,0) | (1,5) |
| 4 | (5,5,6) | (-1,2) | (-1,3) | (-2,2) | (3,8) |
| 5 | (11,10,11) | (-3,2) | (-1,3) | (-2,3) | (8,14) |
| 6 | (22,21,21) | (-4,2) | (-3,3) | (-2,3) | (18,25) |
| 7 | (43,43,42) | (-4,2) | (-4,3) | (-4,3) | (39,47) |
| 8 | (85,86,85) | (-4,4) | (-4,3) | (-5,3) | (81,90) |

The two omitted base levels \(k=0,1\) give \((L_0,U_0)=(0,1)\) and \((L_1,U_1)=(0,2)\). To prove these data imply the *infinite* formula, write \(\omega=e^{2\pi i/3}\). The Fourier identity
\[
\sum_{a=0}^2C_{k,a}\omega^a=(1+\omega)^k=e^{\pi i k/3}
\]
shows that \(C_{k+6,a}=C_{k,a}+21\cdot2^k\) for each \(a\); in particular \(C_{k+6,b}-C_{k+6,a}=C_{k,b}-C_{k,a}\). The table at levels \(2\) and \(8\), together with reversed-pair symmetry, supplies
\[
m_{8,a,b}=m_{2,a,b}-3,\quad M_{8,a,b}=M_{2,a,b}+3\qquad(a\ne b).
\]
Applying the exact minimum/maximum recurrence to both sides inductively proves, for every \(k\ge2\) and every distinct \(a,b\),
\[
m_{k+6,a,b}=m_{k,a,b}-3,\qquad M_{k+6,a,b}=M_{k,a,b}+3.
\]
The case \(a=b\) is identically zero and needs no shifted relation. The six base rows \(2\le k\le7\) show that the global minimum is strictly below every aligned-block count \(C_{k,a}\), and the maximum strictly above every such count; both extrema therefore come from distinct \(a,b\). The shifted off-diagonal minima decrease by \(3\) and maxima increase by \(3\), whereas diagonal counts undergo only the common additive shift \(21\cdot2^k\), so this strict separation persists at each six-step induction. Consequently, for the global extrema over \(a,b\), we get
\[
L_{k+6}=L_k+21\cdot2^k-3,\qquad U_{k+6}=U_k+21\cdot2^k+3\quad (k\ge2).
\]
Substitution of the six base rows \(2\le k\le7\) verifies precisely the claimed parity formulas and the six-step recurrences extend them to every \(k\); the two smaller cases were checked separately.

**3. No missing integer counts.** For each fixed \((a,b)\), increasing \(r\) by one changes \(D_{k,a,b}(r)\) by \(-1\), \(0\), or \(1\). It therefore takes *every* integer from \(m_{k,a,b}\) to \(M_{k,a,b}\). This translated interval contains \(C_{k,a}\), since \(D_{k,a,b}(0)=0\). The three possible anchored values \(C_{k,0},C_{k,1},C_{k,2}\) are consecutive integers (in fact, each is either \(\lfloor2^k/3\rfloor\) or \(\lceil2^k/3\rceil\), by the same Fourier identity). Hence the union of all the translated intervals over \(a,b\) is itself a single integer interval, whose exact endpoints were evaluated above. The explicit phase construction in Step 1 ensures all those counts occur in the infinite word. This completes the proof.

## Verification
Run `python3 verify.py` with ordinary Python 3. The script independently applies the three-letter exact extremum recurrence through level \(120\), tests the six-step relation through level \(114\), compares thirteen complete finite phase enumerations at levels \(0\) through \(12\), and compares eleven direct sliding-window scans at levels \(0\) through \(10\). It raises an exception on any disagreement and prints the base table used in the proof. The finite tests do not prove the infinite claim; the recurrence identities, periodic Fourier relation, and induction supply that proof.

## Relationship to prior work
Chen, Wen, and Wu's study of the *same morphic word* (arXiv:1802.03610, first public version 2018-02-10) determines **additive** complexity, namely the number of possible sums of letters. They bound and attain the extremal differences between two letter counts. That numerical projection does not determine the individual coordinate-count spectrum proved here; their theorems do not identify these exact dyadic single-symbol extrema. Popoli, Shallit, and Stipulanti (arXiv:2410.02409, first public version 2024-10-03) reproduce the additive-complexity theorem and analyze several other ternary words, but do not give the present frequency spectrum. Chen and Wen (arXiv:1809.06554) compute the abelian complexity of **length-\(q\) substitutions on \(q\) letters**; their ternary construction has substitution length three, unlike the length-two morphism here. Their formula therefore does not cover this word.

## Limitations
The proof concerns projections of the Parikh spectrum onto any one coordinate. It does not determine which *triples* of symbol counts occur jointly, nor the full abelian complexity, nor arbitrary nondyadic lengths. Searches cannot exclude every unindexed equivalent earlier result, and independent verification has not been conducted.

## References
- Jin Chen, Zhixiong Wen, Wen Wu, *On the additive complexity of a Thue-Morse like sequence*, arXiv:1802.03610 (first submitted 2018-02-10), https://arxiv.org/abs/1802.03610.
- Jin Chen, Zhixiong Wen, *On the abelian complexity of generalized Thue-Morse sequences*, arXiv:1809.06554 (first submitted 2018-09-18), https://arxiv.org/abs/1809.06554.
- Pierre Popoli, Jeffrey Shallit, Manon Stipulanti, *Additive word complexity and Walnut*, arXiv:2410.02409 (first submitted 2024-10-03), https://arxiv.org/abs/2410.02409.
