# Exact three-deck fibres for binary words with at most four runs

## Finding

For every integer \(n\ge 1\), let \(\mathcal R_{n,4}\) be the words of length \(n\) over \(\{0,1\}\) with at most four maximal constant runs. For a pattern \(s\), let \(N_s(w)\) be its number of *scattered* (not necessarily contiguous) subsequence occurrences in \(w\), and let \(\mathcal D_k(w)=(N_s(w):1\le |s|\le k)\).

**Exact fibre theorem.** Two distinct words in \(\mathcal R_{n,4}\) have the same \(\mathcal D_3\) precisely when, after possibly interchanging the two words, they have the form
\[
 w=0^a1^b0^c1^d,\qquad w'=1^d0^c1^b0^a,
 \qquad a,b,c,d\ge1,\qquad 2bc=(a+c)(b+d).
\]
All nonsingleton restricted fibres consist of exactly these two reversals. In particular, \(\mathcal D_4\) is injective on \(\mathcal R_{n,4}\), but \(\mathcal D_3\) is not injective for \(n=7\), where \(0110001\) and \(1000110\) form one collision pair. Thus the least *uniform in-class* deck order for this family is four.

Define
\[
 T_n=2\sum_{j=0}^{\min(3,n-1)}\binom{n-1}{j}
\]
and, with an empty sum understood as zero,
\[
 F_n=\sum_{A=2}^{n-2}\sum_{b=1}^{n-A-1}
 \mathbf1_{\{2b\mid A(n-A)\}}\,
 \mathbf1_{\{1\le A(n-A)/(2b)<A\}}.
\]
Then exactly \(F_n\) restricted fibres have size two, all others are singletons, and the number of distinct three-decks in this family is exactly \(T_n-F_n\). Equivalently, \(T_n-F_n\) is the maximum size of a zero-error three-deck reconstruction code **when both encoder and decoder restrict candidates to** \(\mathcal R_{n,4}\). The first nonzero value is \(F_7=2\), and the corresponding code size is \(82\).

## Assumptions and scope

All run lengths are positive integers. A run is a maximal contiguous constant block; scattered subsequence multiplicity counts increasing index selections. The observer knows \(n\) and that the source lies in \(\mathcal R_{n,4}\). When \(1\le k\le n\), equality of length-exact \(k\)-decks is equivalent to equality of all lengths up to \(k\), because summing over extensions recovers shorter pattern counts. For \(n<k\), we use the explicitly defined truncated observation \(\mathcal D_k\), which includes all available lengths; the uniform order-four statement concerns the nontrivial range \(n\ge4\). The assertion is *not* a claim of unrestricted reconstruction against candidate words with five or more runs.

## Proof

**Step 1: lower run types.** For words with at most two runs, the zero/one totals and the ordered pair counts distinguish all sources. A three-run word starting with zero has the form \(0^a1^b0^c\). It has \(N_{010}=abc>0\), \(N_{101}=0\), and \(N_{10}=bc\). The one totals give \(b\), hence \(c=N_{10}/b\) and \(a\) from the zero total. Complementing symbols handles three-run words starting with one. Every four-run word has both \(N_{010}>0\) and \(N_{101}>0\), so these types do not collide with lower-run words.

**Step 2: same starting symbol.** Write a four-run zero-start word as \(w=0^a1^b0^c1^d\), and put \(A=a+c\) and \(B=b+d\). Directly summing index selections gives
\[
 p=N_{10}(w)=bc,\quad N_{010}(w)=abc=ap,\quad N_{101}(w)=bcd=dp.
\]
Since \(p>0\), these data recover \(a\) and \(d\), then \(c=A-a\) and \(b=B-d\). Therefore there is at most one zero-start source in a three-deck fibre. The same argument after exchanging letters applies to one-start sources.

**Step 3: opposite starting symbols.** Set \(T=N_{01}(w)=AB-p>0\), and suppose a one-start four-run word \(w'=1^u0^v1^w0^x\) has the same three-deck. Its pair and triple counts force
\[
 vw=T,\quad uvw=dp,\quad vwx=ap.
\]
Put \(t=p/T\). Then \(u=dt\), \(x=at\), and from the symbol totals \(v=A-at\), \(w=B-dt\). Consequently
\[
 0=vw-T=(A-at)(B-dt)-T=ad\,t(t-1).
\]
As all quantities \(a,d,t\) are positive, \(t=1\). Thus \(p=T\), \(u=d\), \(v=c\), \(w=b\), \(x=a\); necessarily \(w'=w^{\mathrm{rev}}\). The equality \(p=T\) is exactly \(2bc=AB\).

**Step 4: sufficiency of the fair equation.** For any binary word with \(A\) zeros and \(B\) ones, double counting a third symbol attached to an ordered opposite-symbol pair gives
\[
 (A-1)N_{01}=2N_{001}+N_{010},\qquad
 (A-1)N_{10}=2N_{100}+N_{010},
\]
\[
 (B-1)N_{01}=2N_{011}+N_{101},\qquad
 (B-1)N_{10}=2N_{110}+N_{101}.
\]
Thus \(N_{01}=N_{10}\) implies \(N_{001}=N_{100}\) and \(N_{011}=N_{110}\). Reversal fixes the other four binary triples \(000,010,101,111\), and the length-one/two counts also agree under reversal. Hence every fair word has the same full three-deck as its reverse. For positive four-run lengths in the displayed equation, \(b(c-a)=d(a+c)>0\), so \(c>a\) and the two reversals are distinct.

**Step 5: four-deck separation.** For a fair four-run word, direct counting gives
\[
 N_{0010}=\binom a2bc,\qquad N_{0100}=ab\binom c2,
\]
whose difference is \(abc(a-c)/2\ne0\). Reversal exchanges these two patterns, so it cannot preserve the four-deck. By Steps 1–4 these are the only possible three-deck collisions within the source family, proving four-deck injectivity. A collision at length seven proves a uniform order of at least four; the preceding argument proves four suffices.

**Step 6: census.** A word with exactly \(j+1\) runs is specified by its first letter and a choice of \(j\) cut positions among the \(n-1\) gaps. This proves the formula for \(T_n\). Each two-element fibre contains exactly one zero-start four-run word. Fixing its total zero and one counts \(A,B=n-A\) and its first one-run length \(b\), the fair equation forces \(c=AB/(2b)\), with \(1\le c<A\); then \(a=A-c\), \(d=B-b\) are uniquely positive. The summand in \(F_n\) tests exactly those requirements. Hence the number of doubletons is \(F_n\) and the number of fibres is \(T_n-F_n\). Selecting one representative per fibre gives the claimed restricted zero-error code size.

## Verification

The accompanying `verify.py` uses a subsequence-count dynamic program independent of the algebraic formulas. It exhaustively enumerates all members of \(\mathcal R_{n,4}\) for \(1\le n\le28\), groups their three-decks, checks that every doubleton is a fair reversal pair, and checks the divisor sum and the number of classes. It independently checks four-deck injectivity for \(1\le n\le24\), checks the explicit seven-letter collision, and performs arithmetic consistency tests through \(n=300\). Run `python3 verify.py` with Python 3 standard library. The full proof is given above; finite enumeration is not used to infer infinitely many cases.

## Relationship to prior work

Angal, Ascoli, He, He, Post, Soe and Zhukova (2026), Theorem 1.3, prove the more general in-class bound \(r'(\mathcal B_2)\le4\) for words with at most two runs of ones. Because \(\mathcal R_{n,4}\subset\mathcal B_2\), that theorem **already implies the four-deck upper bound**, which is not claimed as new here. The contribution here is the exact *three-deck fibre classification*, including their multiplicities, concrete fair equation, and the length-dependent divisor census.

Richomme (2025) studies the already-known notion of fair words under two-binomial equivalence and explicitly documents nonpalindromic fair words of length seven. Neither fair words as such nor the existence of the length-seven examples is claimed as new. The above implication between fairness and three-binomial-equivalent reversal *for the four-run subfamily*, as part of the complete fibre classification, is the focus. Chrisnata et al. (2019/2021) enumerate general distinct decks; Golm et al. (2022) study a different gapped-deck observation. Neither inspected statement gives the fibre classification for the specified source class.

## Limitations

The code size and all singleton/doubleton assertions are relative to the at-most-four-run source family; three-decks may collide with words having more runs. The classification does not assert uniqueness among all binary words. The proof is mathematical and the computations are exact finite checks, not external certification or independent scientific audit. Literature search cannot exclude a differently worded or unindexed equivalent of the complete classification; further bibliographic verification would be appropriate before claiming definitive priority.

## References

- Krishna Angal, Ruben Ascoli, Simon X. He, Xiaoyu He, Logan Post, Arker Oke Soe, Olga Zhukova, *Deck Reconstruction for Restricted Word Classes*, arXiv:2610.41110 (first public 2026-10-30), https://arxiv.org/abs/2610.41110.
- Gwenaël Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159 (first public 2025-10-08), https://arxiv.org/abs/2510.07159.
- Johan Chrisnata, Han Mao Kiah, Sankeerth Rao Karingula, Alexander Vardy, Eitan Yaakobi, Hanwen Yao, *On the Number of Distinct k-Decks: Enumeration and Bounds*, ISCIT 2019 / journal version (2021), https://doi.org/10.1109/ISCIT.2019.8905191.
- Jonas Golm and collaborators, *The Gapped k-Deck Problem*, arXiv:2201.12671 (first public 2022-01-29), https://arxiv.org/abs/2201.12671.
