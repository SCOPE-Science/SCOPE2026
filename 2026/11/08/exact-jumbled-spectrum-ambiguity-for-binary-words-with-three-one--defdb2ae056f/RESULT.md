# Exact jumbled-spectrum ambiguity for binary words with three ones

## Finding

Let \(n\ge3\), let \(\mathcal W_{n,3}\) be the indexed binary words of length \(n\) having exactly three ones, and let \(\Pi(w)\) be the **set**, not multiset, of Parikh vectors \((|u|_0,|u|_1)\) of all nonempty contiguous factors \(u\) of \(w\). Two words are equivalent precisely when these sets agree. Reversal always preserves \(\Pi\).

Write \(w=0^a1\,0^b1\,0^c1\,0^d\), where \(a,b,c,d\) are nonnegative integers with \(a+b+c+d=n-3\). Put \(A=\max(a,d)\), \(D=\min(a,d)\), \(B=\max(b,c)\), and \(C=\min(b,c)\). The equivalence class of \(w\) contains a word other than \(w\) or its reversal **if and only if**

\[
A>D,\qquad B>C,\qquad C\ge A.
\]

In this event its class has exactly four distinct indexed words, obtained by independently assigning the two endpoint gaps and the two interior gaps in either order. In all other cases the class consists precisely of the reversal orbit, of size one or two. In particular there are no classes of size three or more than four.

Let \(J_n\) count the distinct Parikh sets \(\Pi(w)\) arising from \(\mathcal W_{n,3}\), and let \(p_{\le4}(k)\) count partitions of \(k\) into parts of sizes at most four (set this to zero for \(k<0\)). Then, for every \(n\ge3\),

\[
J_n=\frac12\left(\binom n3+\mathbf 1_{n\text{ odd}}\frac{n-1}{2}\right)-p_{\le4}(n-7).
\]

Equivalently,

\[
\sum_{n\ge3}J_nz^n
=\frac12\left(\frac{z^3}{(1-z)^4}+\frac{z^3}{(1-z^2)^2}\right)
-\frac{z^7}{(1-z)(1-z^2)(1-z^3)(1-z^4)}.
\]

There are exactly \(p_{\le4}(n-7)\) four-element classes. Furthermore,

\[
J_n\sim\frac{11}{144}n^3,
\qquad
\lim_{n\to\infty}\Pr_{W\sim\mathrm{Unif}(\mathcal W_{n,3})}
\!\left[\exists V\notin\{W,\operatorname{rev}(W)\}:\Pi(V)=\Pi(W)\right]=\frac16.
\]

The first non-reversal ambiguity occurs at \(n=7\): the words `0100101` and `0101001` have the same Parikh set but are not reversals.

## Assumptions and scope

The alphabet is the labeled alphabet \(\{0,1\}\). Words are linear, not cyclic, and their positions are indexed. Factors are contiguous and nonempty. Parikh-vector multiplicities, order among factors, and original factor locations are discarded; thus these measurements are weaker than a complete multiset of substring compositions. The full word's Parikh vector is observable, so the Hamming-weight-three subfamily is intrinsically identifiable. Including the empty factor would add one common vector and not change equivalence. All statements quantify over every integer \(n\ge3\) and every word of that length and weight.

## Proof

**1. The five extremal statistics determine the observation.** Fix \(w=0^a1\,0^b1\,0^c1\,0^d\). For each prescribed number \(j\) of ones in a substring, the possible substring lengths form an interval of integers. Indeed, for a fixed length \(k\), the one-counts of successive length-\(k\) windows change by at most one, so every integer between their minimum \(m_k\) and maximum \(M_k\) occurs. Both \(m_k\) and \(M_k\) are nondecreasing in \(k\): each longer window contains a shorter one, while any shorter window can be extended. Therefore the lengths satisfying \(m_k\le j\le M_k\) form an integer interval. Thus it suffices to know the minimum and maximum length of a factor with each \(j\in\{0,1,2,3\}\) ones. The nontrivial endpoints are

\[
\begin{aligned}
L_0&=\max(a,b,c,d),\\
L_1&=1+\max(a+b,\ b+c,\ c+d),\\
\ell_2&=2+\min(b,c),\\
L_2&=2+b+c+\max(a,d),\\
\ell_3&=3+b+c.
\end{aligned}
\]

Here the possible lengths are \([1,L_0]\) for zero ones when \(L_0>0\), \([1,L_1]\) for one one, \([\ell_2,L_2]\) for two ones, and \([\ell_3,n]\) for three ones. The formula for \(L_1\) comes from the longest factors containing only the first, only the middle, or only the last one. The formula for \(L_2\) comes from the two longest factors containing exactly the first two or the last two ones. Every interval assertion is valid when a gap is zero, including the all-ones word.

**2. Unordered gaps are forced.** From \(\ell_3\) one recovers \(b+c\), from \(\ell_2\) one recovers \(\min(b,c)\), and hence the unordered pair \(\{b,c\}\). Since \(n\) is known, \(a+d=n-3-b-c\); from \(L_2\) one recovers \(\max(a,d)\), and hence \(\{a,d\}\). Therefore equivalent words must differ only by independent permutations of the two outer gaps and the two inner gaps. These permutations preserve \(L_0\), \(\ell_2\), \(L_2\), and \(\ell_3\). It remains to compare \(L_1\).

**3. Exact ambiguity criterion.** If either \(a=d\) or \(b=c\), the four permutations give at most one reversal orbit. Otherwise choose the canonical inequalities \(A>D\ge0\) and \(B>C\ge0\). Modulo reversal the only two candidates have gap quadruples \((A,B,C,D)\) and \((A,C,B,D)\). Their values of \(L_1-1\) are respectively

\[
\begin{aligned}
T_\mathrm{aligned}&=\max(A+B,\ B+C,\ C+D)=B+\max(A,C),\\
T_\mathrm{crossed}&=\max(A+C,\ B+C,\ B+D).
\end{aligned}
\]

If \(C\ge A\), then \(B\ge C\ge A>D\); both displayed maxima equal \(B+C\). Thus both reversal orbits have exactly the same observation and form one four-element class. If \(C<A\), then \(T_\mathrm{aligned}=A+B\), while each of \(A+C\), \(B+C\), and \(B+D\) is strictly smaller than \(A+B\), using \(B>C\), \(A>C\), and \(A>D\). The two observations differ. This proves the characterization and complete class-size assertion.

**Minimality of the weight threshold.** For a word with exactly two ones write \(0^a1\,0^b1\,0^c\). Its shortest factor with two ones has length \(b+2\), while its longest factor with exactly one one has length \(b+1+\max(a,c)\). With known length these recover \(b\) and the unordered pair \(\{a,c\}\), hence the word up to reversal. For zero or one one, the same claim is immediate. Thus weight three is the least binary Hamming weight with non-reversal Parikh-set ambiguity.

**4. Exact class count.** Each four-element class has exactly one canonical representative with \(A>D\), \(B>C\), and \(C\ge A\). Write uniquely

\[
D=t,\quad A=t+1+u,\quad C=A+v,\quad B=C+1+r,
\qquad t,u,v,r\in\mathbb Z_{\ge0}.
\]

The length identity reduces to

\[
n=7+4t+3u+2v+r.
\]

Consequently the number of four-element classes is exactly the coefficient of \(z^{n-7}\) in \(((1-z)(1-z^2)(1-z^3)(1-z^4))^{-1}\), namely \(p_{\le4}(n-7)\). Reversal has one fixed word for each palindromic weight-three word. Such a palindrome exists only for odd \(n=2m+1\), with a central one and one reflected pair of ones; there are exactly \(m\) of them. By Burnside's elementary orbit count, the number of reversal orbits is \(\frac12(\binom n3+\mathbf1_{n\text{ odd}}(n-1)/2)\). Each four-element class merges exactly two of these orbits, reducing the count by exactly one. This yields \(J_n\) and its generating function.

**5. Limiting laws.** The partition generating function has a pole of order four at \(z=1\), with leading local term \(1/(24(1-z)^4)\); all other roots-of-unity poles have lower orders. Hence \(p_{\le4}(n-7)\sim n^3/144\). Since \(\binom n3\sim n^3/6\) and the palindromic correction is only linear, \(J_n\sim n^3/12-n^3/144=11n^3/144\). Exactly four words belong to each four-element class, so the fraction of ambiguous indexed weight-three words tends to \((4/144)/(1/6)=1/6\). This is a consequence of the proved exact classification, not of finite sampling.

## Verification

The standard-library Python program `VERIFY.py` computes factor Parikh sets directly, without using the five-statistic shortcut, for every weight-three binary word of lengths \(3\) through \(21\) inclusive (7,315 indexed words). It groups actual sets, checks that class sizes are only one, two, or four, verifies the gap criterion for every member, and compares both the exact number of classes and four-element classes with the partition formula. It separately checks the canonical-gap parameterization through length \(100\). Run `python VERIFY.py` from the directory containing the script. Expected terminal line: `VERIFY_OK words=7315 lengths=3..21 transform=3..100`. These finite tests corroborate, but do not substitute for, the preceding unrestricted proof.

## Relationship to prior work

Fici and Lipták introduced prefix-normal forms and proved that equality of the two binary prefix-normal forms characterizes equality of sets of factor Parikh vectors. That general equivalence theorem is the conceptual foundation, not a new result here. Burcsi, Fici, Lipták, Ruskey, and Sawada developed enumeration and generation of prefix-normal words, including explicit fixed-density generating functions. Those count **prefix-normal representatives for one statistic**, not the joint pair of normal forms or the complete Parikh-set equivalence classes of fixed weight three. Cunha and Medina's subsequent binary jumbled-index work concerns query-index construction rather than the classification of inverse images. The contribution here is the explicit all-length four-gap equivalence criterion, the exact fiber-size spectrum, the partition correction to reversal-orbit enumeration, and the asymptotic fraction of intrinsically ambiguous observations. These are stronger than a direct restatement of the general normal-form characterization, but prior-unindexed equivalences remain possible.

## Limitations

No uniqueness beyond reversal is asserted for larger Hamming weights. The theorem concerns only the set of substring compositions, not the multiset, and not scattered subsequences. The probability is conditional on exactly three ones, not an unconditional random binary word. The standard partitions into parts at most four are classical; novelty is not claimed for the partition sequence itself. Historical priority has not been independently certified, and literature comparisons cannot exclude unindexed equivalent results. The finite checker is not an independent proof of the infinite statements.

## References

1. G. Fici and Z. Lipták, *On Prefix Normal Words*, Developments in Language Theory (2011), pp. 228–238, DOI: https://doi.org/10.1007/978-3-642-22321-1_20; accessible author's version: https://arxiv.org/pdf/1805.12405 (2018 upload of 2011 work).
2. P. Burcsi, G. Fici, Z. Lipták, F. Ruskey, and J. Sawada, *On Combinatorial Generation of Prefix Normal Words*, arXiv:1401.6346, first submitted January 24, 2014, https://arxiv.org/pdf/1401.6346.
3. P. Burcsi, G. Fici, Z. Lipták, F. Ruskey, and J. Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017, first submitted November 28, 2016, https://arxiv.org/pdf/1611.09017.
4. L. Cunha and M. Medina, *Binary jumbled indexing: suffix tree histogram*, Journal of Combinatorial Optimization 51 (2026), article 32, https://doi.org/10.1007/s10878-026-01407-6.
