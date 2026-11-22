# Congruence-cut spectra and the limiting simplicity law for finite Gödel strict implications

## Finding

Fix an integer \(n\ge 2\), and the labelled \(n\)-element Gödel (Heyting) chain \(G_n=\{c_0<c_1<\cdots<c_{n-1}\}\) with its ordinary lattice operations and Heyting implication. Adjoin an independent binary **flat strict implication** \(\Rightarrow\) satisfying the four weak-Heyting identities listed below. Put \(h_j=c_{j+1}\Rightarrow c_j\), \(0\le j\le n-2\). The previously established adjacent-edge representation makes the \(h_j\) arbitrary members of \(G_n\), so there are \(n^{n-1}\) such expansions.

For \(0\le k\le n-1\), let \(\theta_k\) identify exactly the terminal interval \(\{c_k,\ldots,c_{n-1}\}\) and leave the smaller elements singleton. Then the congruences of the expanded algebra are **exactly** \(\theta_0\), \(\theta_{n-1}\), and those \(\theta_k\), \(1\le k\le n-2\), for which
\[
\boxed{\quad \min_{k\le j\le n-2}h_j\ge c_k.\quad}\tag{1}
\]
The comparison means the order of \(G_n\); equivalently, if \(h_j=c_{s_j}\), then \(s_j\ge k\) for every \(j\ge k\). In particular, the congruence lattice is a chain, the expansion is simple precisely when no interior \(k\) satisfies (1), and **every** prescribed subset of the \(n-2\) interior Heyting congruences occurs as the exact surviving congruence set of some expansion.

Here is a complete all-sizes enumeration, not only a classification of possible congruence lattices. Let \(K_n=\{1,\ldots,n-2\}\), and for \(T\subseteq K_n\) and \(1\le j\le n-2\) define
\[
q_T(j)=\max(\{0\}\cup\{k\in T:k\le j\}).
\]
If \(P_n(z)\) counts expansions by their number of *interior* congruences, then
\[
\boxed{\quad P_n(z)=n\sum_{T\subseteq K_n}(z-1)^{|T|}
\prod_{j=1}^{n-2}\bigl(n-q_T(j)\bigr).\quad}\tag{2}
\]
All empty products and sums use their standard conventions. The coefficient of \(z^r\) counts expansions with **exactly** \(r+2\) congruences, for \(0\le r\le n-2\). More finely, the number with *exactly* the interior-cut set \(S\subseteq K_n\) is
\[
\boxed{\quad N_n(S)=n\sum_{T\supseteq S}(-1)^{|T\setminus S|}
\prod_{j=1}^{n-2}\bigl(n-q_T(j)\bigr).\quad}\tag{3}
\]
For uniformly and independently chosen adjacent-edge values, the simple-expansion probability has the nontrivial limit
\[
\boxed{\quad \Pr(G_n,\Rightarrow\text{ is simple})
=1-e^{-1}+O(n^{-1})\qquad(n\to\infty).\quad}\tag{4}
\]
The first five polynomials are \(P_2(z)=2\), \(P_3(z)=3+6z\), \(P_4(z)=20+20z+24z^2\), \(P_5(z)=200+175z+130z^2+120z^3\), and \(P_6(z)=2616+2094z+1422z^2+924z^3+720z^4\).

## Assumptions and scope

The chain and its underlying Heyting implication are fixed and labelled; no quotient by order isomorphisms changes the count, since a finite chain has only the identity order automorphism. The independent strict connective obeys, for all \(a,b,c\in G_n\),
\[
\begin{aligned}
a\Rightarrow a&=c_{n-1},\\
a\Rightarrow(b\wedge c)&=(a\Rightarrow b)\wedge(a\Rightarrow c),\\
(a\vee b)\Rightarrow c&=(a\Rightarrow c)\wedge(b\Rightarrow c),\\
(a\Rightarrow b)\wedge(b\Rightarrow c)&\le a\Rightarrow c.
\end{aligned}
\]
These are the weak-Heyting identities for the flat Lewis-style arrow, without additional persistence, reflexivity, transitivity, sharp antecedent-distribution, or paired weak-difference axioms. The ordinary Heyting arrow remains distinct from \(\Rightarrow\). A congruence must respect **both** the ordinary Heyting structure and the extra strict arrow. A simple algebra here has exactly the identity and universal congruences; all \(n\ge2\) cases are nontrivial.

## Proof

**1. Edge representation (established background, recalled).** The four identities imply that \(a\Rightarrow b\) is antitone in the first argument, isotone in the second, and equals top when \(a\le b\). On an ordered chain, transitivity forces its below-diagonal values to be the meets of the adjacent values:
\[
c_a\Rightarrow c_b=
\begin{cases}
c_{n-1},&a\le b,\\
\bigwedge_{j=b}^{a-1}h_j,&a>b.
\end{cases}\tag{5}
\]
Conversely, (5) for arbitrary \(h_j\in G_n\) satisfies all four identities: monotonicity yields the two distribution identities on a chain, the diagonal is top, and the interval underlying a long arrow is contained in the union of the two intervals underlying its two short arrows, yielding transitivity. The adjacent values recover their own parameters, giving a bijection. This representation and raw \(n^{n-1}\) count are not proposed as new; see Reference 2.

**2. Underlying Heyting congruences.** Each \(\theta_k\) as defined above is a Heyting congruence. Conversely, if a Heyting congruence identifies \(c_a<c_b\), then comparison of \(c_a\to c_a\) and \(c_b\to c_a\) forces it to identify \(c_a\) with top, hence the entire terminal interval beginning at \(c_a\). Thus each Heyting congruence is one of the \(\theta_k\). The endpoints \(k=0\) and \(k=n-1\) are universal and identity respectively and survive any expansion.

**3. Exact interior-cut test.** Fix \(1\le k\le n-2\). If \(h_j<c_k\) for some \(j\ge k\), the congruent input pairs \((c_{j+1},c_j)\) and \((c_j,c_j)\) have strict-arrow outputs \(h_j\) and top, which are not \(\theta_k\)-equivalent. This proves necessity of (1).

Conversely, assume all \(h_j\ge c_k\) for \(j\ge k\). If both arguments lie below the collapsed interval, each class is singleton. If the first argument is below \(c_k\) but the second is in the collapsed interval, (5) always returns top. If both arguments lie in the collapsed interval, (5) returns a value in that same interval. Finally, if the first argument lies in the collapsed interval and the second is a fixed \(c_b<c_k\), (5) gives
\[
 c_a\Rightarrow c_b=\min\left(\bigwedge_{j=b}^{k-1}h_j,
                                  \bigwedge_{j=k}^{a-1}h_j\right)
 \quad(a\ge k),
\]
where the second meet is top when \(a=k\). The first meet is independent of \(a\), and the second is at least \(c_k\); thus either all values are the same singleton below \(c_k\), or all values lie in the collapsed interval. These cases exhaust pairs of congruent arguments. Hence \(\theta_k\) preserves \(\Rightarrow\), proving (1). A subset of a chain of congruences is itself ordered as a chain.

**4. Every cut pattern occurs.** Let \(S\subseteq K_n\) be prescribed. In ordinal indices set \(s_0=0\), and for each \(1\le j\le n-2\) choose \(s_j=n-1\) if \(j\in S\), and \(s_j=j-1\) otherwise. For \(k\notin S\), the value \(s_k=k-1\) violates (1). For \(k\in S\), every later index satisfies \(s_j\ge k\), so (1) holds. Thus the surviving interior congruences are exactly \(S\), proving realizability without assuming monotone or independent cut events.

**5. Exact enumerators.** Write \(E_k\) for the event (1) under the uniform independent choice of the \(n-1\) edge indices. Requiring every \(E_k\) with \(k\in T\) forces \(s_j\ge q_T(j)\) at each \(j\ge1\), leaving \(n-q_T(j)\) choices. The initial edge \(s_0\) has \(n\) unrestricted choices. Hence the number of expansions satisfying all events in \(T\) is exactly
\[
A_n(T)=n\prod_{j=1}^{n-2}(n-q_T(j)).\tag{6}
\]
For each edge vector, \(z^{\#\{k:E_k\}}=\prod_{k\in K_n}(1+(z-1)\mathbf1_{E_k})\). Summing over edge vectors and expanding proves (2). Inclusion–exclusion on the forbidden additional events \(E_k\), \(k\notin S\), proves (3).

**6. Limiting simplicity law.** For all \(n\ge3\),
\[
\Pr(E_1)=(1-1/n)^{n-2}=e^{-1}+O(n^{-1}).\tag{7}
\]
For \(2\le k\le n-2\), \(\Pr(E_k)=((n-k)/n)^{n-1-k}\). If \(E_k\) holds but \(E_1\) fails, at least one of the independent indices \(s_1,\ldots,s_{k-1}\) must equal zero. Therefore
\[
\Pr(E_k\setminus E_1)\le\frac{k-1}{n}
 \left(1-\frac{k}{n}\right)^{n-1-k}.\tag{8}
\]
For \(2\le k\le n/2\), the last power is at most \(e^{-k/3}\) for all sufficiently large \(n\), so the sum of (8) over these indices is \(O(1/n)\). For \(k>n/2\), set \(r=n-k\); then \(2\le r<n/2\) and
\[
\sum_{k>n/2}^{n-2}\Pr(E_k)
=\sum_{2\le r<n/2}\left(\frac rn\right)^{r-1}
\le\frac1n\sum_{r\ge2}r\,2^{-(r-2)}=O(n^{-1}).\tag{9}
\]
Consequently \(\Pr(\bigcup_{k\in K_n}E_k)=\Pr(E_1)+O(n^{-1})=e^{-1}+O(n^{-1})\). Taking complements proves (4). This is a genuine all-sizes proof, not an extrapolation from finite counts.

## Verification

The standalone Python 3 program `verify.py` uses only the standard library. It independently enumerates **all** binary operation tables on the two- and three-element chains and checks that the tables satisfying the four defining axioms coincide with (5). It checks all \(n^{n-1}\) adjacent-edge expansions for \(2\le n\le6\), directly tests the cut criterion against operation-table congruence compatibility, enumerates every equivalence partition for \(n\le4\), and independently computes the polynomial (2) by binomial expansion. It checks that all \(2^{n-2}\) cut patterns are realizable for every \(2\le n\le13\). Successful execution prints `VERIFY_OK`. These finite computations are corroborative; the general theorem is proved above.

## Relationship to prior work

De Groot and Litak [1] introduce the flat strict-implication semantics, its axioms and relational representations. The previously published exact box-reduct theorem [2] supplies (5), the \(n^{n-1}\) total and the different problem of reconstructing an arrow from its box. The **congruence test**, all exact congruence-cut fibers, complete polynomial (2), arbitrary-cut realizability and limiting simple fraction are not claimed or implied as numbered results in [2] or in the inspected flat-semantics manuscript [1]. They are the additional results examined here; the edge-normal-form input is explicitly not rebranded as novel.

San Martín's full open-access general paper [3] studies principal congruences of weak Heyting algebras, not the explicit congruence-spectrum enumeration for arbitrary fixed Gödel chains or its random-expansion limit. Alizadeh and Joharizadeh [4] give an algorithm for counting weak Heyting structures on general finite distributive lattices; the accessible abstract does not determine whether its full text contains a congruence-refined chain census, so it remains a concrete priority risk. Previously published finite-chain **weak Heyting–Brouwer** congruence counts [5] require an additional weak-difference connective and have Boolean congruence lattices and a simplicity probability tending to one; they are not a stronger theorem for the present one-connective family. A flat **relation-induced** partial-injection census [6] covers a different subfamily, not all abstract edge-parametrized expansions. General tense-chain congruence results use other operators and restrictions.

## Limitations

The result applies only to an arbitrary weak-Heyting/flat strict arrow on the fixed finite chain, *not* to all finite distributive lattices, a sharpened or persistent Lewis logic, or an arbitrary strict arrow induced by a relation on the fixed dual chain. The asymptotic refers to the uniform distribution on independent labelled edge parameters, not a distribution on relational frames or box reducts. The exact polynomial is exponential-time in its displayed subset expansion; no uniform polynomial-time algorithm for every coefficient is claimed. The 2015 counting paper was available only in abstract and through bibliographic descriptions; its full text was not inspected. No independent validation or historical-priority certification is claimed.

## References

1. J. de Groot and T. Litak, *Relational Semantics for Flat Heyting-Lewis Logic*, arXiv:2603.28402 (first posted 2026-03-30); https://arxiv.org/abs/2603.28402 .
2. *Exact box-reduct fibers of finite-chain Heyting–Lewis implication*, published mathematical finding (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-box-reduct-fibers-of-finite-chain-heyting-lewis-implicatio--7dc46cf75da9 .
3. H. J. San Martín, *Principal congruences in weak Heyting algebras*, Algebra Universalis 75 (2016), 405–418, doi:10.1007/s00012-016-0381-4; lawful OA https://sedici.unlp.edu.ar/handle/10915/138934 .
4. M. Alizadeh and N. Joharizadeh, *Counting weak Heyting algebras on finite distributive lattices*, Logic Journal of the IGPL 23 (2015), 247–258, doi:10.1093/jigpal/jzu033 (abstract available, full text not inspected).
5. *Congruence-rank spectrum and unary reconstruction of finite weak Heyting–Brouwer chains*, published mathematical finding (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-congruence-rank-spectrum-and-unary-reconstruction-of-finite-weak--9bb111bd5f63 .
6. *Last-occurrence matchings and exact realization fibers for finite flat Heyting–Lewis chains*, published mathematical finding (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-last-occurrence-matchings-and-exact-realization-fibers-for-finit--4c5d5d5150e4 .
