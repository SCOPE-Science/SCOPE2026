# Fixed-composition deletion spectra and parity bias for alternating binary words

## Finding
For integers \(m\ge1\) and \(t\ge0\), let \(A_{m+t}=0101\cdots\) be the length-\(m+t\) binary word beginning with \(0\). Let \(B_{m,t,k}\) be the number of **distinct** length-\(m\) words containing exactly \(k\) ones that are obtainable from \(A_{m+t}\) by deleting exactly \(t\) positions, with \(0\le k\le m\). These are counts of distinct outputs, not counts of deletion-position choices.

The complete fixed-composition spectrum has rational generating function
\[
\sum_{m,t,k\ge0} B_{m,t,k}s^m h^t u^k
=\frac{1+s-sh}{(1-h)\bigl(1-sh(1+u)-s^2u(1-h^2)\bigr)},
\]
where the sole extension to \(m=0\) uses \(B_{0,t,0}=1\). Equivalently, if \(P_0(u,z)=1\) and for \(m\ge1\)
\[
P_m(u,z)=(1,uz)
\begin{pmatrix}z&u\\1&uz\end{pmatrix}^{m-1}
\binom11,
\]
then
\[
B_{m,t,k}=[u^k]\sum_{j=0}^t[z^j]P_m(u,z).
\]
The exact support threshold is
\[
B_{m,t,k}>0\quad\Longleftrightarrow\quad
 t\ge \max\{0,m-2k-1,2k-m\}.
\]
For \(m\ge1\), the entire fixed-weight class is present exactly when \(t\ge m-1\) if \(k<m\), and exactly when \(t\ge m\) if \(k=m\). In particular, at \(t=m-1\) precisely the all-one word is missing, while at \(t\ge m\) every length-\(m\) word occurs.

There is an additional sharp and explicitly signed complement asymmetry. Put \(r=m-t\) and \(\Delta_{m,t,k}=B_{m,t,k}-B_{m,t,m-k}\). If \(r\le0\) or \(r\) is even, \(\Delta_{m,t,k}=0\) for every \(k\). If \(r=1\), the only nonzero values are \(\Delta_{m,t,0}=1\) and \(\Delta_{m,t,m}=-1\). If \(r=2a+1\ge3\), then for \(1\le k\le m-1\)
\[
\Delta_{m,t,k}=\frac{m-2k}{a}
\binom{m-k-1}{a-1}\binom{k-1}{a-1},
\]
with zero difference at the endpoints. Here a binomial coefficient is zero unless its lower argument lies between zero and its upper argument. Thus for even \(m+t\), the complete composition spectrum is symmetric; for odd \(m+t\), its possible imbalance always favors the smaller number of ones because the host starts with \(0\).

## Assumptions and scope
The host positions are indexed from \(0\). Every result is exact for each finite \(m\ge1\), deletion count \(t\ge0\), and \(0\le k\le m\). Deleted positions are not observable, so multiple embeddings of the same query count once. The empty-word extension in the rational series is a formal convention; no claim about negative deletion counts is made. Every equation depends on the specified left-end phase of the alternating host. A host starting with \(1\) has the reflected weight distribution.

## Proof
**1. Earliest embedding and a Boolean-ball bijection.** For nonempty binary \(v=v_1\cdots v_m\), define
\[
c(v)=v_1+\sum_{i=1}^{m-1}{\bf1}_{v_i=v_{i+1}}.
\]
The first selected host index for its lexicographically earliest embedding is \(v_1\). From a selected \(0\) or \(1\), the next unequal bit occurs one position later and the next equal bit occurs two positions later. Inductively, the last earliest-embedding index is exactly \(m-1+c(v)\). Greedy earliest embedding is optimal among all embeddings, so
\[
v\preceq A_{m+t}\quad\Longleftrightarrow\quad c(v)\le t.
\]
The change of variables \((v_1,\ldots,v_m)\mapsto(v_1,{\bf1}_{v_1=v_2},\ldots,{\bf1}_{v_{m-1}=v_m})\) is an affine bijection over \(\mathbb F_2\): given the first bit and each equality indicator, one recovers all later bits uniquely. Consequently the accepted set is an affine image of a Hamming ball, and the known unweighted size is \(\sum_{j=0}^{\min(m,t)}\binom mj\). This unweighted enumeration is *not* asserted as new.

**2. The fixed-weight transfer matrix.** Give every one a factor \(u\) and every unit of \(c(v)\) a factor \(z\). The first bit contributes row vector \((1,uz)\). A transition from previous bit \(0\) or \(1\) to next bit \(0\) or \(1\) contributes, respectively,
\[
M=\begin{pmatrix}z&u\\1&uz\end{pmatrix}.
\]
Summing over the final bit proves the expression for \(P_m\). Its two-state recurrence is
\[
P_m=z(1+u)P_{m-1}+u(1-z^2)P_{m-2}\quad(m\ge2),
\]
with \(P_0=1\) and \(P_1=1+uz\). Therefore
\[
\sum_{m\ge0}P_m(u,z)s^m
=\frac{1+s-sz}{1-sz(1+u)-s^2u(1-z^2)}.
\]
By step 1, allowing excess at most \(t\) introduces the factor \(\sum_{t\ge j}h^t=h^j/(1-h)\). Substitution \(z=h\) and division by \(1-h\) yield the asserted rational trivariate generating function.

**3. Sharp support and saturation.** If a word with \(k\) ones starts with \(0\), its successive runs alternate between the \(m-k\) zero symbols and \(k\) one symbols. The largest possible number of runs, accounting separately for the starting bit, gives
\[
\min_{|v|=m,\,|v|_1=k}c(v)
=\max\{0,m-2k-1,2k-m\}.
\]
For completeness this can be checked directly: beginning with \(0\), an alternating run decomposition uses at most one more zero-run than one-run; beginning with \(1\) has the symmetric restriction but costs one extra unit in \(c\). For any allowed run counts, one may distribute positive block sizes among the available zeros and ones, so these bounds are attained. On the other hand, \(c(v)\le m-1\) for every word other than \(1^m\), whereas \(c(1^m)=m\). For each \(0\le k<m\), the explicit word \(1^k0^{m-k}\) has \(c=m-1\): when \(k=0\) all \(m-1\) adjacencies are equal, and when \(k>0\) the initial-one penalty is one and there are \(m-2\) equal adjacencies. Thus every non-all-one weight class becomes complete first at \(t=m-1\), and the all-one class becomes complete at \(t=m\).

**4. Parity and the explicit imbalance.** Pair each binary word \(v\) with its bitwise complement \(\bar v\). Their equality-transition counts are the same, and their starting bits are opposite, so \(c(\bar v)=c(v)+1\) precisely when \(v\) begins with \(0\). The pair contributes to the composition difference only when it has exactly \(t\) equal adjacent transitions. Let \(C_{m,k,r}\) denote the number of words of length \(m\), weight \(k\), starting with \(0\), having exactly \(r\) runs. Since equality transitions number \(m-r\), pairing gives
\[
\Delta_{m,t,k}=C_{m,k,m-t}-C_{m,m-k,m-t}.
\]
For \(r=2a\ge2\), the \(a\) zero-runs and \(a\) one-runs have positive compositions, so
\[
C_{m,k,2a}=\binom{m-k-1}{a-1}\binom{k-1}{a-1};
\]
this is symmetric under swapping \(k\) with \(m-k\). For \(r=2a+1\ge3\), the starting-zero word has \(a+1\) zero-runs and \(a\) one-runs, giving
\[
C_{m,k,2a+1}=\binom{m-k-1}{a}\binom{k-1}{a-1}.
\]
Subtract its counterpart with \(k\) and \(m-k\) interchanged. Factoring the common product and using
\[\binom{j}{a}=\frac{j-a+1}{a}\binom{j}{a-1}\]
proves the stated signed defect. The special case \(r=1\) has only the all-zero word starting with \(0\). For \(r\le0\), both sides of the complement pairing are already present because \(t\ge m\). This exhausts all cases.

A second coefficient-free exact formula, useful for verification, follows from run compositions. Let \(H(S,p)=\binom{S-1}{p-1}\) for \(p\ge1\) and \(S\ge p\), \(H(0,0)=1\), and \(H(S,p)=0\) otherwise. Write \(r_0=\lceil r/2\rceil\), \(r_1=\lfloor r/2\rfloor\). Then
\[
B_{m,t,k}=\sum_{r=1}^{m}\left(
{\bf1}_{m-r\le t}H(m-k,r_0)H(k,r_1)
+{\bf1}_{m-r+1\le t}H(m-k,r_1)H(k,r_0)
\right).
\]
This directly counts words beginning with \(0\) and with \(1\), and agrees with the generating function.

## Verification
Run \(\texttt{python3 verify.py}\) with standard Python 3. The standalone verifier directly constructs distinct sets of deletion outputs for all host lengths \(1\) through \(17\) and checks \(1{,}122\) fixed-weight cells against the transfer polynomial. For each output length \(1\) through \(64\), it independently derives every exact penalty coefficient by positive run compositions and compares it with the transfer recurrence. Its checks cover \(2{,}336\) total-count identities and \(100{,}096\) parity/support comparisons. All checks passed. The finite checks are not exhaustive for unbounded lengths; steps 1–4 give the general proof.

## Relationship to prior work
Flaxman, Harrow, and Sorkin (2004), Theorem 2 and Theorem 5, establish the maximal distinct-subsequence property of periodic alternating words and the unweighted length-based enumerator. The greedy embedding observation is standard and explicitly credited to that source. The present fixed-composition enumerator tracks the number of ones in each distinct received word and the exact complement-symmetry defect, which are not determined by the unweighted enumerator alone. Alon, Bourla, Graham, He, and Kravitz (2022) study deletion-code bounds and common subsequences of pairs of hosts, while Menon and Singh (2023) count occurrence multiplicities of prescribed subsequences in collections of hosts. Neither inspected formulation gives this one-host output-composition census.

## Limitations
The host must be an alternating binary word starting with \(0\). No optimality among all sources at fixed output composition is asserted. The unweighted subsequence count and greedy criterion are established prior results. The review found no equivalent weight-refined formula or signed parity law in the inspected primary sources and indexed research records, but an unindexed or differently expressed earlier result remains possible. Independent mathematical validation has not been performed.

## References
- A. Flaxman, A. W. Harrow, and G. B. Sorkin, *Strings with Maximally Many Distinct Subsequences and Substrings*, Electron. J. Combin. 11 (2004), R8. DOI: https://doi.org/10.37236/1761.
- N. Alon, G. Bourla, B. Graham, X. He, and N. Kravitz, *Logarithmically Larger Deletion Codes of All Distances*, arXiv:2209.11882 (first posted 2022-09-23). https://arxiv.org/abs/2209.11882.
- K. Menon and A. Singh, *Subsequence Frequency in Binary Words*, arXiv:2306.07870 (first posted 2023-06-13). https://arxiv.org/abs/2306.07870.
