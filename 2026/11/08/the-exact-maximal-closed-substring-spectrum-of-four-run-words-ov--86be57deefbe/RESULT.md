# The exact maximal closed-substring spectrum of four-run words over arbitrary alphabets

## Finding

Let \(\Sigma\) be a labeled alphabet of \(q\ge2\) symbols. For a word \(w\), write \(\rho(w)\) for its number of maximal constant-letter runs, and let \(\kappa(w)\) count the **occurrences** (rather than distinct contents) of maximal closed substrings. Define
\[
F_q(z,u)=\sum_{w\in\Sigma^*,\,\rho(w)=4} z^{|w|}u^{\kappa(w)}.
\]
Then the exact bivariate series is
\[
\begin{aligned}
F_q(z,u)={}&q(q-1)(q-2)(q-3)\frac{u^4z^4}{(1-z)^4}\\
&+3q(q-1)(q-2)\frac{u^5z^4(1+z)}{(1-z)^3(1-uz^2)}\\
&+q(q-1)\frac{u^5z^4(1+uz)^2}{(1-z)^2(1-uz^2)^2}.
\end{aligned}
\]
The coefficient of \(z^nu^k\) is the exact number of length-\(n\) four-run words having \(k\) maximal closed-substring occurrences. Thus it gives a complete finite-length distribution for every alphabet size, including binary and ternary alphabets. At \(u=1\) it specializes to \(q(q-1)^3z^4/(1-z)^4\), the ordinary count of four-run words.

## Assumptions and scope

A nonempty substring is *closed* if it has length one, or possesses a nonempty proper border (a word occurring as its prefix and suffix) that has no occurrence strictly inside the substring. A closed occurrence at positions \([i,j]\) is *maximal* when neither \([i-1,j]\) (if available) nor \([i,j+1]\) (if available) is closed. End positions and equal-content occurrences are distinct. We use zero-based indices in the accompanying checker. All run lengths are positive integers; adjacent run letters differ. No condition is imposed on nonadjacent letters. A run of a repeated letter is not automatically a closed substring larger than one symbol; all closures are considered according to the preceding definition.

## Proof

**Local classification.** Write an arbitrary four-run word as \(X^aY^bZ^cT^d\), where \(a,b,c,d\ge1\), \(X\ne Y\), \(Y\ne Z\), and \(Z\ne T\). Every whole constant-letter run is a maximal closed occurrence: it is closed, while extending across either adjacent run boundary cannot give a closed substring of this one-run type. The remaining possibilities arise by choosing two occurrences of the same letter in nonadjacent runs as endpoints of a minimal recurring border.

If the four letters are distinct, no border can cross a run boundary, hence the four whole runs are the entire list: \(\kappa=4\). If exactly one nonadjacent run-letter pair agrees, say positions 1 and 3, each \(t\) with \(1\le t\le\min(a,c)\) yields one additional maximal closed occurrence \(X^tY^bX^t\), with its two boundary pieces chosen from the ends of the respective runs. Its unary border \(X^t\) occurs exactly at the ends. The analogous construction applies to the pair in positions 2 and 4, and to the pair in positions 1 and 4 (then the middle two runs lie between the borders). Each produces precisely the minimum of the two equal-letter run lengths; a second border occurrence would require a third run carrying the same letter, impossible under the present assumptions. Thus \(\kappa=4+\min(r,s)\) in all three single-repeat configurations.

If there are two nonadjacent equalities, adjacency inequalities force the alternating pattern \(X=Z=A\), \(Y=T=B\), \(A\ne B\). In addition to the four runs, the potential \(A\)-border occurrences are \(A^tB^bA^t\) for \(1\le t\le\min(a,c)\); the terminal one is not maximal when \(t=c\le a\), since it extends to the right with a closed border involving the last \(B\)-run. Similarly, the potential \(B\)-border occurrences are \(B^tA^cB^t\) for \(1\le t\le\min(b,d)\); discard \(t=b\le d\), since it extends to the left with a closed border involving the first \(A\)-run. Finally, exactly one additional maximal closed occurrence has a nonunary border crossing the central \(B\)-to-\(A\) boundary; its initial border uses the final \(\min(a,c)\) copies of \(A\) from the first run and the first \(\min(b,d)\) copies of \(B\) from the second run, with the corresponding suffix in the last two runs. Its interval is uniquely fixed by these minimum lengths. No other nonunary border can repeat, because four runs contain only two occurrences of an \(AB\) transition and only one occurrence of a \(BA\) transition. Consequently,
\[
\kappa(A^aB^bA^cB^d)=5+\min(a,c)+\min(b,d)-\mathbf1_{c\le a}-\mathbf1_{b\le d}.
\]
These candidate lists exhaust maximal closed occurrences: a repeated border spanning at least two letter transitions would force two distinct copies of a transition not available among four runs; unary borders must pair two nonadjacent runs; the all-equal borders are contained in a whole run. The possibility of a single-character extension being closed is covered by the two boundary exclusions above.

**Summation.** The label assignments of the three mutually exclusive classes are \(q(q-1)(q-2)(q-3)\), \(3q(q-1)(q-2)\), and \(q(q-1)\), respectively. In the single-repeat class, the two repeated run lengths have the weighted sum
\[
\sum_{r,s\ge1}z^{r+s}u^{\min(r,s)}=\frac{uz^2(1+z)}{(1-z)(1-uz^2)}.
\]
The two other run lengths each contribute \(z/(1-z)\), and one extra unit exponent of \(u\) accounts for the four base runs, giving the second term. In the alternating case, the exponents separate into independent pairs \((a,c)\) and \((b,d)\). A direct split into \(c\le a\) and \(c>a\) shows
\[
\sum_{a,c\ge1} z^{a+c}u^{\min(a,c)-\mathbf1_{c\le a}}
=\frac{z^2(1+uz)}{(1-z)(1-uz^2)}.
\]
The same formula applies to \((d,b)\) with the corresponding boundary indicator, so multiplying both factors and the extra \(u^5\) gives the third term. Finally, the four-distinct class has four independent positive run lengths and exponent four, yielding the first term. All identities are formal power-series identities, establishing every coefficient simultaneously.

## Verification

The included standalone script `verify_four_run.py` independently enumerates each substring, tests the defining closed-border condition, checks maximality by adjacent extension, and compares every occurrence interval against the above structural list. It passed 17,484 parameter instances over alphabets of sizes 2, 3, and 4. It separately enumerated all four-run words over alphabet sizes 2 through 5 for lengths 4 through 14 and matched every coefficient of the stated rational series, including the normalization at \(u=1\). Run `python3 verify_four_run.py` with standard Python 3. No external datasets or packages are required. These finite checks complement, but do not replace, the all-parameter symbolic classification and summation.

## Relationship to prior work

Umezaki, Shibata, Nakashima and Inenaga (2026) give general output-sensitive enumeration of maximal closed substrings in run-length encoded strings, including characterization by valid matching border occurrences. Fischer and Köppl (2026) further study output-sensitive enumeration in linear space. Those results apply to each four-run word and provide a general way to find its maximal closed substrings; they do not explicitly state the global all-alphabet, all-length generating function derived here, nor the exact three-way distribution by run-letter equality type. The present statement is an enumerative refinement of that general framework, not a new output-sensitive algorithm. Kosolobov (2024) studies closed repeats in a broader setting.

## Limitations

The formula applies to exactly four maximal constant-letter runs and counts maximal closed occurrences, not all closed factors, not distinct substring contents and not arbitrary run counts. It does not improve the known general enumeration algorithms. The published general valid-pair framework may permit equivalent calculations; the priority comparison is limited to the accessible material and indexed records. Independent mathematical evaluation has not been performed.

## References

- T. Umezaki, T. Shibata, Y. Nakashima and S. Inenaga, *Compact Enumeration of Maximal Closed Substrings in Run-Length Encoded Strings*, arXiv:2607.02838v1 (2026-07-03), https://arxiv.org/abs/2607.02838.
- J. Fischer and D. Köppl, *Output-Sensitive Enumeration of Maximal Closed Substrings in Linear Space*, arXiv:2610.38114v1 (2026-10-28), https://arxiv.org/abs/2610.38114.
- D. Kosolobov, *Closed Repeats*, arXiv:2410.00209v1 (2024-09-30), https://arxiv.org/abs/2410.00209.
