# Sharp upper bound and equality classification for five-symbol adjacent-burst deletion codes

## Finding
Let \(\Sigma\) be an alphabet of \(q\ge2\) symbols. An **exact two-symbol adjacent-burst deletion** takes a length-five word and deletes exactly two consecutive positions, leaving a length-three word. A code \(C\subseteq\Sigma^5\) corrects this channel if the sets of possible length-three outputs of distinct codewords are disjoint. Define \(A_q\) to be the largest cardinality of such a code.

For every \(q\ge2\),
\[
A_q\le\frac{q^2(q+2)}3.
\]
For every \(q\ge3\) with \(q\equiv0,1\pmod3\), the earlier construction of Chee, Li and Zhang [4] attains the bound, so
\[
\boxed{A_q=\frac{q^2(q+2)}3.}
\]
Moreover, **all codes attaining this upper bound** are classified as follows: they consist of all \(q^2\) period-two words \(ababa\), together with the words \(xbybz\) arising by choosing, separately for every middle symbol \(b\in\Sigma\), a directed triple system on \(\Sigma\) and including one such word for every ordered transitive triple \((x,y,z)\) in that system. Therefore, if \(D(q)\) is the number of directed triple systems on the *labeled* set \(\Sigma\), the number of labeled maximum codes in the equality regime is exactly \(D(q)^q\).

Every equality-attaining code is also a perfect partition of the \(q^3\) possible outputs into deletion balls, although those balls have unequal cardinalities. The assertion of exact optimality is restricted to the displayed congruence classes; in particular, no exact optimal value is asserted for \(q\equiv2\pmod3\).

## Assumptions and scope
Words are linear, not circular; the four possible deletion positions are \((1,2),(2,3),(3,4),(4,5)\). Repeated deletion outcomes from one source word count only once. The alphabet is arbitrary and need not be a field, and symbols are labeled: codes are not quotiented by permutations of the alphabet. Perfect means that every word in \(\Sigma^3\) is covered by exactly one codeword's set of distinct deletion outputs. 

A **directed triple system of order \(q\)** is a collection \(\mathcal T\) of ordered triples \((x,y,z)\) of pairwise distinct alphabet elements, such that every ordered pair \((u,v)\), \(u\ne v\), occurs exactly once among the three pairs \((x,y),(x,z),(y,z)\) of a triple. Each system contains exactly \(q(q-1)/3\) ordered triples. Their existence for all \(q\ge3\) congruent to \(0\) or \(1\) modulo \(3\) is a known design-theoretic theorem [2]; it is not claimed as new here.

## Proof
For \(w=abcde\in\Sigma^5\), its exact-burst deletion output set is
\[
B(w)=\{cde,\ ade,\ abe,\ abc\}.
\]
Define a positive weight on received words \(u v z\in\Sigma^3\) by
\[
\lambda(uvz)=\begin{cases}1,&u=z,\\[2pt]1/3,&u\ne z.\end{cases}
\]
**Shadow inequality.** For every source word \(w\), \(\sum_{y\in B(w)}\lambda(y)\ge1\). If one output has equal first and last symbols, it contributes weight \(1\). Otherwise the four displayed outputs show that \(c\ne e\), \(a\ne e\), and \(a\ne c\); hence \(a,c,e\) are pairwise distinct. The outputs \(cde,ade,abc\) are then pairwise distinct; moreover none is a palindrome, so they contribute \(3(1/3)=1\). (The fourth output either coincides with \(ade\) when \(b=d\), or gives an additional contribution.) This proves the inequality.

For a correcting code \(C\) the output sets are disjoint. Therefore
\[
|C|\le\sum_{w\in C}\sum_{y\in B(w)}\lambda(y)
\le\sum_{y\in\Sigma^3}\lambda(y)
=q^2+\frac{q^3-q^2}{3}=\frac{q^2(q+2)}3.
\]
This argument uses only finite nonnegative sums and applies to every alphabet size.

**Attainment.** Fix a directed triple system \(\mathcal T_b\) on the common alphabet for each \(b\in\Sigma\). Define
\[
C=\{ababa:a,b\in\Sigma\}
\ \cup\ \{xbybz:b\in\Sigma,\ (x,y,z)\in\mathcal T_b\}.
\]
For a period-two word the set of received words is \(B(ababa)=\{aba\}\), so these codewords partition the \(q^2\) output words whose first and last symbols agree. For a word \(xbybz\) with \(x,y,z\) pairwise distinct, the output set is
\[
B(xbybz)=\{ybz,\ xbz,\ xby\}.
\]
Fixing \(b\), these outputs are exactly the ordered pairs represented by the transitive triple \((x,y,z)\), inserted around \(b\). The directed triple system property partitions all \(q(q-1)\) triples of the form \(ubv\), \(u\ne v\), without repetition. As \(b\) ranges over \(\Sigma\), all nonpalindromic outputs are covered exactly once, and none overlaps a palindromic output. Thus the code is perfect and has
\[
q^2+q\cdot\frac{q(q-1)}3=\frac{q^2(q+2)}3
\]
words. The cited directed-triple existence theorem supplies the systems whenever \(q\ge3\) and \(q\equiv0,1\pmod3\). The embedding into the length-five burst channel is a specialization of the already known lifting construction from length-three deletion codes in Chee, Li and Zhang [4]; it is included to make the matching upper/lower bound self-contained, not claimed as novel.

**Classification of equality.** Suppose \(C\) attains the weight bound. Both inequalities in the shadow sum above are equalities. Positivity of \(\lambda\) forces every output to be covered once, and each source word to have deletion-ball weight exactly \(1\). If one output is palindromic, the positive weights require its deletion ball to be a singleton. The equalities \(cde=ade=abe=abc\) force \(a=c=e\) and \(b=d\); hence the source is exactly \(ababa\). Every palindromic output requires its unique period-two parent, so all \(q^2\) such parents belong to \(C\).

Every other source word has no palindromic output. Consequently \(a,c,e\) are pairwise distinct. In this case the output set has exactly three elements when \(b=d\) and four otherwise: the only possible equality among the four expressions is \(ade=abe\). Weight exactly \(1\) forces \(b=d\), giving a source of the form \(xbybz\) with distinct \(x,y,z\). For each fixed \(b\), its three outputs are the arcs of the transitive triple \((x,y,z)\). Since the full output alphabet is partitioned, the selected ordered triples form a directed triple system \(\mathcal T_b\). Different middle symbols do not interact, so the \(q\) choices of systems are independent, establishing the complete characterization and the count \(D(q)^q\).

Finally, if the upper bound is attained, it must be an integer, which requires \(q\equiv0,1\pmod3\). The cited directed-triple existence result proves this condition sufficient for every \(q\ge3\). This integer restriction does *not* determine the optimum for other alphabets.

## Verification
The standalone `verify.py` checks explicit labeled directed triple systems of orders \(3,4,6,7,9\), verifies each ordered arc appears exactly once, constructs the claimed codes, directly computes the distinct four-position deletion outputs, and verifies disjointness and complete coverage of \(\Sigma^3\). Its construction sizes are respectively \(15,32,96,147,297\). The same checker separately verifies the weighted shadow inequality by brute-force enumeration of all source words for \(2\le q\le6\), testing \(32+243+1024+3125+7776=12200\) words. Run `python3 verify.py` from the extracted package directory; its final line is `VERIFY_OK`.

The finite checks do not prove the all-alphabet design existence theorem or the general shadow inequality; those are justified by the cited existence theorem and the complete case analysis above.

## Relationship to prior work
**Closest and decisive prior construction.** Chee, Li and Zhang [4, Section III-B] already construct perfect length-five exact-two-burst deletion codes by lifting every perfect length-three single-deletion code separately through a fixed middle letter. Their published size spectrum includes \(q\lfloor q(q+2)/3\rfloor\) as an achievable size; in the congruence classes of this theorem it equals the optimum claimed here. The present work does **not** claim that lifting construction, the perfect codes it produces, or directed triple systems are new. The additional results are a universal sharp upper bound against *all* length-five burst codes, not just the previously constructed families, and the proof that *every* code attaining this bound must decompose into the indicated directed-triple systems, giving the complete equality-case classification and count \(D(q)^q\). Chee–Li–Zhang determine inclusions in the perfect-code size spectrum and a minimum for even alphabets but do not prove this global maximum or its rigidity. Ye and Ge [1] provide general fixed-error asymptotic redundancy results, not finite-length sharpness. Schoeny et al. [3] provide binary bounds, not this arbitrary-alphabet case. Kreher et al. [2] prove design existence, not the burst shadow equality conditions.

## Limitations
The channel deletes *exactly* one block of two consecutive positions from a length-five word. The proof does not apply unchanged to at-most-two-deletion, two arbitrary deletion, insertion, noisy-output, or cyclic channels. It does not determine \(A_q\) for \(q\equiv2\pmod3\), where the rational upper bound is nonintegral. The quantity \(D(q)\) counts labeled directed triple systems; no explicit numerical closed formula for this number is asserted. Finite checker tests are corroborative and independent external validation has not been performed. Unindexed priority remains a general risk.

## References
1. Z. Ye and G. Ge, *Substring Edit Correcting Codes and Optimal Single Burst-Deletion Correcting Codes*, arXiv:2610.05696, first posted 2026-10-05. https://arxiv.org/abs/2610.05696
2. D. L. Kreher, D. R. Stinson, and S. Veitch, *Block-avoiding point sequencings of directed triple systems*, Discrete Mathematics 343 (2020), article 111773; arXiv:1907.11186, first posted 2019-07-25. See Section 2.1, Corollary 2.2 for existence. https://arxiv.org/abs/1907.11186
3. C. Schoeny, A. Wachter-Zeh, R. Gabrys, and E. Yaakobi, *Codes Correcting a Burst of Deletions or Insertions*, arXiv:1602.06820, 2016. https://arxiv.org/abs/1602.06820
4. Y. M. Chee, Y. Li, and X. Zhang, *Spectrum of sizes for perfect burst deletion-correcting codes*, IEEE International Symposium on Information Theory (ISIT), 1931–1935 (2015), DOI:10.1109/ISIT.2015.7282792. Section III-B contains the previously known length-three-to-length-five lifting construction. https://doi.org/10.1109/ISIT.2015.7282792
