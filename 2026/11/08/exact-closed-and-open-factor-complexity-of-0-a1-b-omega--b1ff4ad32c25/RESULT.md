# Exact closed and open factor complexity of \((0^a1^b)^\omega\)

## Finding

For arbitrary integers \(a,b\ge1\), set \(p=a+b\) and let \(X=(0^a1^b)^\omega\). Let \(C_{a,b}(n)\) be the number of **distinct, nonempty closed contiguous factors** of \(X\) having length \(n\). A word of length one is closed; a longer word is closed when some nonempty proper border occurs exactly twice, as prefix and suffix. Write \([P]\) for the indicator of a proposition \(P\).

For every integer \(1\le n\le p\),
\[
C_{a,b}(n)=[n\le a]+[n\le b]
 +[\exists r\in\mathbb Z:1\le r\le\lfloor a/2\rfloor,\ n=b+2r]
 +[\exists s\in\mathbb Z:1\le s\le\lfloor b/2\rfloor,\ n=a+2s].
\]
For every integer \(n>p\), put \(h=n-p\). Then
\[
C_{a,b}(n)=\min(a,h-1)+\min(b,h-1)
 +[1\le h\le a,\ h\equiv a\pmod2]
 +[1\le h\le b,\ h\equiv b\pmod2].
\]
The total number of distinct length-\(n\) factors is \(P_{a,b}(n)=\min(n,a)+\min(n,b)\). Therefore the exact *open* complexity is \(O_{a,b}(n)=P_{a,b}(n)-C_{a,b}(n)\). In particular, the sharp eventual all-closed threshold is
\[
O_{a,b}(n)=0\ \text{for every }n\ge p+\max(a,b),
\qquad O_{a,b}(p+\max(a,b)-1)>0.
\]
Thus the entire closed/open complexity profile and the last length at which an open factor exists are determined explicitly by the two run lengths. For example \((a,b)=(3,4)\) gives \((C(7),C(8),C(9),C(10),C(11))=(1,1,3,5,7)\); every factor of length at least \(11\) is closed.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), \(a,b\ge1\), and \(X\) is the one-sided purely periodic infinite word beginning with \(0^a\). Factors are *contiguous* and distinct words are counted once, independently of occurrences. Only positive lengths \(n\) are counted. Although the empty word is sometimes called closed, it is not included in \(C_{a,b}\). The period \(p=a+b\) is primitive because its cyclic word has exactly two symbol transitions, whereas a nontrivial power would have at least four. Consequently all \(p\) cyclic phases yield different factors whenever \(n\ge p\).

## Proof

**First-return lemma.** Fix a phase \(i\) inside a run of symbol \(s\), of total length \(d\in\{a,b\}\). Number its offset from the beginning of that run by \(j\), where \(0\le j<d\), and let \(r=d-j\) be the number of \(s\)'s remaining in the current run. For the prefix \(u_\ell=X[i:i+\ell]\), let \(R_i(\ell)\) be the smallest positive shift \(q\) with \(X[i+q:i+q+\ell]=u_\ell\). Then for every integer \(\ell\ge1\),
\[
R_i(\ell)=
\begin{cases}
1,&1\le\ell<r,\\
p-j,&\ell=r,\\
p,&\ell>r.
\end{cases}
\]
For \(\ell<r\), the next starting position still has at least \(\ell\) copies of \(s\). For \(\ell=r\), no later position within the current run can start \(s^r\), so the next copy begins at the next run of \(s\), at shift \(p-j\). For \(\ell>r\), the prefix begins \(s^r\bar s\). Exactly one \(s\)-to-\(\bar s\) transition occurs per primitive period and its location within this prefix fixes the starting phase uniquely, so the next occurrence starts at shift \(p\). These cases are exhaustive, including \(r=1\).

**Closed-length criterion.** For \(n>1\), the length-\(n\) factor at phase \(i\) is closed exactly when there exists an integer \(1\le\ell<n\) such that \(n=\ell+R_i(\ell)\). Indeed, the suffix beginning at displacement \(n-\ell\) must equal its length-\(\ell\) prefix and must be its first positive recurrence; conversely this first-return equality means that the border occurs precisely at the two endpoints. This remains valid for overlapping border occurrences.

**Lengths above a period.** Let \(n=p+h>p\) with \(h\ge1\). At a phase with run length \(d\) and remainder \(r=d-j\), the case \(\ell<r\) gives \(n=\ell+1\le d<p+h\), so cannot occur. The case \(\ell>r\) gives \(\ell=h\) and contributes exactly the remainders \(1\le r\le\min(d,h-1)\). The case \(\ell=r\) gives \(h=2r-d\), contributing one more phase exactly when \(1\le h\le d\) and \(h\equiv d\pmod2\). These two types cannot overlap: the exceptional remainder \(r=(d+h)/2\) is strictly greater than \(h-1\) when \(h\le d\). Summing over both runs and using distinctness of the \(p\) phases proves the second displayed formula.

**Lengths at most a period.** A length-\(n\le p\) factor contains at most two changes of symbol: crossing three changes requires a full \(0\)-run and a full \(1\)-run between nonempty endpoint segments and therefore length at least \(p+2\). The constant factors are precisely \(0^n\) if \(n\le a\) and \(1^n\) if \(n\le b\); both are closed. A factor with exactly one change has different first and last letters, and has no nonempty border. A factor with exactly two changes is of the form \(0^r1^b0^s\) or \(1^r0^a1^s\) with positive endpoint-run lengths. Its only possible border is unary. Such a factor is closed if and only if its endpoint lengths agree, because otherwise the shorter-end border occurs at least twice inside the longer endpoint run, in addition to its occurrence at the opposite end. Thus the remaining closed factors are exactly \(0^r1^b0^r\) with \(1\le2r\le a\), and \(1^s0^a1^s\) with \(1\le2s\le b\). Their lengths and different starting letters make them distinct. This proves the first formula, including \(n=p\).

**Total factor complexity.** Each phase of the primitive period produces a distinct factor whenever the factor contains both symbols, because the location of its first transition is fixed. Identical starting-phase factors can arise only from all-zero or all-one factors. The unary length-\(n\) blocks account for excess phase multiplicities \(\max(a-n,0)\) and \(\max(b-n,0)\), respectively. Hence \(P_{a,b}(n)=p-\max(a-n,0)-\max(b-n,0)=\min(n,a)+\min(n,b)\) for every \(n\ge1\). Subtracting the closed formula gives the open formula.

**Sharp threshold.** Put \(M=\max(a,b)\). If \(h\ge M\), both run contributions for \(n=p+h\) equal their full run lengths (at \(h=M\), the run of length \(M\) contributes \(M-1\) from the first term and one from parity). Hence \(C_{a,b}(p+h)=p\) for all \(h\ge M\). If \(M\ge2\), at \(h=M-1\) a length-\(M\) run contributes only \(M-2\), and the other run contributes at most its full length; therefore \(C_{a,b}(p+M-1)<p\). If \(M=1\) then \(a=b=1\); at length \(p=2\) both factors are open. Thus the threshold is sharp in every case.

## Verification

Run the standalone standard-library program `verify_closed_complexity.py` with `python3 verify_closed_complexity.py`. It independently generates all distinct factors of the relevant period lengths, decides closedness by testing every possible proper border and all its occurrences, and compares the resulting profile with the displayed formulas. The default run covers all parameter pairs \(1\le a,b\le12\) and every length \(1\le n\le2(a+b)+\max(a,b)+2\). A larger independent pre-package exploration covered all pairs \(1\le a,b\le15\) and 10,010 factor-length comparisons. These computations test finitely many cases and are not proofs of the universally quantified result; the proof above supplies the infinite argument.

## Relationship to prior work

The complete-first-return definition and general theory appear in Badkobeh–Fici–Lipták (2013). Parshina–Postic (2020) study closed and open complexity and its characterization of aperiodicity; their results do not supply this two-run periodic full-length profile. Parshina–Puzynina (2021) prove asymptotic extremal statements about closed-rich finite and infinite words, including eventual closedness of sufficiently long periodic factors via general power properties. The present result computes every length and every positive pair \((a,b)\), and identifies the sharp saturation length \(a+b+\max(a,b)\). No assertion of a general periodic-word classification is made.

## Limitations

The theorem is restricted to exactly one positive \(0\)-run and one positive \(1\)-run per primitive period. It does not classify arbitrary periodic words with three or more cyclic runs, nor does it enumerate distinct closed factors across all lengths inside a fixed finite prefix. Existing results already imply eventual closedness from sufficiently large powers; the new mathematical content is the full exact two-parameter length profile and the earlier sharp cutoff. Bibliographic searches cannot exclude unindexed or differently formulated equivalents. Independent validation has not been performed.

## References

1. O. Parshina and M. Postic, *Open and closed complexity of infinite words*, arXiv:2005.06254 (initial public version 2020-05-13), https://arxiv.org/abs/2005.06254.
2. O. Parshina and S. Puzynina, *Finite and infinite closed-rich words*, arXiv:2111.00863 (2021), https://arxiv.org/abs/2111.00863.
3. G. Badkobeh, G. Fici and Z. Lipták, *On the Number of Closed Factors in a Word*, arXiv:1305.6395 (2013), https://arxiv.org/abs/1305.6395.
