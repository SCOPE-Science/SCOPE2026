# Exact pseudo-Frobenius classification for Lucas-incremented numerical semigroups

## Finding
For \(a\ge3\), let \(L_0=2\), \(L_1=1\), \(L_{n+2}=L_{n+1}+L_n\), and
\[S_a=\langle L_a,L_a+L_0,L_a+L_1,\ldots,L_a+L_{a-1}\rangle.\]
For \(B\subseteq\{0,\ldots,a-1\}\), write \(x_B=\sum_{j\in B}L_j\), and \(P_B=(|B|-1)L_a+x_B\).
The complete pseudo-Frobenius set \(\operatorname{PF}(S_a)\) consists of the \(P_B\) for the following **disjoint** families of index sets:

1. \(B=(1=i_1<i_2<\cdots<i_r)\), consecutive differences all \(2\) or \(3\), and final index in \(\{a-2,a-1\}\). The singleton \(B=\{1\}\) is included when \(a=3\).
2. \(B=(0,3=i_2<i_3<\cdots<i_r)\), remaining consecutive differences all \(2\) or \(3\), and final index in \(\{a-2,a-1\}\).
3. Only if \(a\) is odd: \(B=\{2,4,\ldots,a-1\}\), or \(B=\{0,4,6,\ldots,a-1\}\); at \(a=3\), the latter means \(\{0\}\).

Let \(c(0)=1\), \(c(n)=0\) when \(n<0\), and \(c(n)=c(n-2)+c(n-3)\) for \(n\ge1\). Then the **exact type** is
\[
\boxed{t(S_a)=c(a-2)+c(a-3)+c(a-4)+c(a-5)+2\mathbf 1_{a\text{ odd}}.}
\]
In particular it grows exponentially at the plastic-constant rate, the real root \(\rho>1\) of \(\rho^3=\rho+1\).

## Assumptions and scope
The integer \(a\ge3\). The semigroup \(S_a\) contains zero. An integer \(z\notin S_a\) is pseudo-Frobenius if \(z+s\in S_a\) for every positive \(s\in S_a\); it suffices to check the minimal generators. In this text Lucas subscripts are the **original** subscripts, with \(L_0=2\), \(L_1=1\), not the interchanged increasing order used in the cited source. An index set is called *admissible* when it contains no consecutive integers and does not contain both \(0\) and \(2\). The Lucas-Zeckendorf theorem gives a unique admissible representation \(x=x_B<L_a\), for each \(0\le x<L_a\).

## Proof
**1. Apéry criterion.** Robles-Pérez–Rosales, Lemma 4.1 and Theorem 4.6, prove that the minimal number \(\beta(x)\) of Lucas summands in \(x\) is \(|B|\), and that the Apéry representative modulo \(m=L_a\) is \(w(x)=m\beta(x)+x\) for \(0\le x<m\). Their Lemma 4.5 also proves that if a sum of \(r\) Lucas numbers from \(L_0,\ldots,L_{a-1}\) is at least \(m\), then subtracting \(m\) yields a sum of at most \(r-1\) such numbers. Thus if \(x+L_j\ge m\), the element \(w(x)+L_j\) belongs to \(S_a\). If \(x+L_j<m\), then \(w(x)+L_j\in S_a\) precisely when \(\beta(x+L_j)\le\beta(x)\). Consequently, \(w(x)-m\) is pseudo-Frobenius exactly when for all \(j<a\) with \(x+L_j<m\), \(\beta(x+L_j)\le\beta(x)\).

**2. Admissible indices and maximal independent sets.** Regard the indices \(0,\ldots,a-1\) as vertices of a graph with edges between consecutive indices and also between \(0\) and \(2\). Admissible sets are precisely independent sets of this graph. If \(B\) is not maximal independent, adjoining an undominated index \(j\) gives another admissible set. Its sum is \(x_B+L_j<m\), with minimal summand count \(|B|+1\); hence \(w(x_B)-m\) is not pseudo-Frobenius. All maximal independent sets have final index \(a-2\) or \(a-1\), all gaps after the first at most three, and initial possibilities \(0\) followed by \(3\) or \(4\), \(1\) followed by \(3\) or \(4\), or \(2\) followed by \(4\) or \(5\). With only one index, the same boundary conditions apply. The graph description proves this by checking the first undominated index after each selected vertex.

**3. Excluding unwanted maximal independent sets.** Write all identities using original Lucas indices. For every even \(j\ge2\), induction from the Lucas recurrence gives
\[
2L_j+L_{j-2}+L_{j-4}+\cdots+L_2
=L_{j+1}+L_{j-1}+L_{j-3}+\cdots+L_3+L_0.
\]
For every even \(j\ge4\), it similarly gives
\[
2L_j+L_{j-2}+\cdots+L_4+L_0
=L_{j+1}+L_{j-1}+\cdots+L_3+L_1.
\]
Each right side is an **admissible** expansion containing exactly one more summand than the corresponding selected prefix (before adding the duplicate \(L_j\)). If \(B\) starts \(2,5\), then adding \(L_0\) replaces \(L_0+L_2=L_1+L_3\); the resulting entire expansion is admissible and gains one summand, so the Apéry criterion fails. If \(B\) starts \(2,4,6,\ldots\) and contains a first gap of size \(3\), add the duplicate \(L_j\) at the selected index \(j\) just before that gap; the first displayed identity, followed by untouched later indices, is admissible and has one more summand. If there is no gap \(3\) but the last selected index is \(a-2\), duplicate that index and use the same identity. If \(B\) starts \(0,4,6,\ldots\), the second identity gives the identical exclusion, using the index before the first later gap \(3\) or the final index \(a-2\). In each case the rewritten expansion has indices smaller than \(a\), hence its sum is below \(L_a\); the increase in \(\beta\) is genuine.

Only two exceptions survive these exclusions. If \(a=2k+1\), the Lucas recurrence gives
\[\sum_{j=1}^k L_{2j}=L_a-1,\qquad L_0+\sum_{j=2}^k L_{2j}=L_a-2.\]
The first exceptional \(B\) has \(x_B=m-1\), so every addition wraps. The second has \(x_B=m-2\); all additions wrap except \(L_1=1\), and the latter changes the canonical digit set from \(\{0,4,6,\ldots,a-1\}\) to \(\{2,4,\ldots,a-1\}\), **without changing its cardinality**. Both therefore are maximal Apéry elements.

**4. Showing all other listed sets are maximal.** Fix a family-(1) or family-(2) set \(B\). Any absent index \(j\) is adjacent to a selected index (here the exceptional edge \(0,2\) is not needed); hence the Lucas recurrence \(L_j+L_{j\pm1}=L_{\max(j,j\pm1)+1}\) replaces those two summands by one. Thus adding an absent \(L_j\) never increases the minimum number of summands. For a selected index \(j\), duplicate \(L_j\). Whenever the preceding selected index is \(j-2\), use \(2L_j=L_{j+1}+L_{j-2}\), and push the duplicate two places backward. At a preceding gap \(3\), the identity \(2L_j+L_{j-3}=L_{j+1}+L_{j-1}\) reduces the summand count by one. If the duplicate reaches the first index, it terminates by \(2L_0=L_3\) or \(2L_1=L_0\), or by one of the base relations \(2L_3+L_0=L_4+L_2\), \(2L_3+L_1=L_4+L_0\), and \(2L_4+L_1=L_5+L_3\). The net effect is a representation with **at most the original number \(|B|\) of summands**, proving \(\beta(x_B+L_j)\le|B|\) whenever no wrap occurs. For a wrap, step 1 applies. Therefore all and only the listed \(P_B\) are pseudo-Frobenius numbers.

**5. Counting.** Compositions of an integer into parts \(2\) and \(3\) number \(c(n)\). Families (1) and (2) contribute respectively \(c(a-2)+c(a-3)\) and \(c(a-4)+c(a-5)\). The two exceptional digit sets occur exactly for odd \(a\). This proves the exact type formula. The characteristic equation of \(c(n)\) is \(r^3-r-1=0\), and its unique positive dominant root \(\rho\) yields exponential growth.

## Verification
The accompanying `verify.py` implements two independent computations: Dijkstra on the semigroup residue graph to reconstruct its Apéry set, and direct composition enumeration of the proposed Lucas index sets. For every \(3\le a\le17\), it compares all pseudo-Frobenius numbers, not just their counts, and also checks the stipulated type formula. This is a finite independent check, not the proof of the infinite classification. The symbolic argument above proves all \(a\ge3\).

## Relationship to prior work
Robles-Pérez–Rosales, arXiv:2211.01436v1 (2 November 2022), obtain the generating set, Lucas-Zeckendorf Apéry parametrization, Frobenius number, genus and Wilf inequality. Their results are used explicitly, but their paper does not formulate the pseudo-Frobenius set or the type sequence. López-Medel–Robles-Pérez–Rosales (2025) determine types for **shifted \(r\)-Fibonacci semigroups**, a different family; in particular its \(r=1\) case describes Fibonacci rather than Lucas shifts. Independent results on generic pseudo-Frobenius bounds do not directly give this explicit Lucas digit-set classification. Targeted literature and indexed-record searches found no identical formula. Failure to locate a result is not a uniqueness or priority certificate.

## Limitations
The classification is for the exact Lucas-incremented family and \(a\ge3\), not all shifted linear recurrences or semigroups of fixed embedding dimension. The proof uses the published Lucas coin-count minimality and wrap-reduction lemmas, and does not reprove those foundational lemmas. Independent scientific audit has not been performed. Possible unindexed equivalent literature remains an originality risk.

## References
Robles-Pérez, A. M., and Rosales, J. C. *The extended Frobenius problem for Lucas series incremented by a Lucas number.* arXiv:2211.01436v1 (2022), https://arxiv.org/abs/2211.01436 ; Quaestiones Mathematicae 48 (2025), DOI 10.2989/16073606.2024.2422517.

López-Medel, J. M., Robles-Pérez, A. M., and Rosales, J. C. *The extended Frobenius problem for r-Fibonacci sequences shifted by r-Fibonacci numbers.* Arabian Journal of Mathematics 14 (2025), DOI 10.1007/s40065-025-00513-3.
