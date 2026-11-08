# The fixed-two-deletion planted embedding law and its mutual-information constant

## Finding
Fix an integer alphabet size \(q\ge2\). Choose \(X\) uniformly in \(\Sigma_q^n\), choose an unordered pair \(D\subseteq\{1,\dots,n\}\) uniformly among all two-element subsets and independently of \(X\), and let \(Y=X\setminus D\) be the length-\(n-2\) subsequence. Let
\[
Z_n=\#\{D'\subseteq\{1,\dots,n\}: |D'|=2,\ X\setminus D'=Y\}.
\]
Put \(p=(q-1)/q\). Let \(L_1,L_2\) be independent random positive integers having the size-biased geometric distribution
\[
\Pr(L_i=r)=r p^2(1-p)^{r-1},\qquad r=1,2,\ldots.
\]
There is a constant \(C_q<\infty\), depending only on \(q\), such that for all \(n\ge2\),
\[
\boxed{d_{\mathrm{TV}}\bigl(\mathcal L(Z_n),\mathcal L(L_1L_2)\bigr)\le C_q/n.}
\]
In particular, \(Z_n\) converges in total variation to the nondegenerate product distribution. For the uniform two-deletion channel,
\[
\boxed{ I(X;Y)=(n-2)\log q-\log\binom n2
 +2\sum_{r=1}^{\infty}r p^2(1-p)^{r-1}\log r+o(1),\quad n\longrightarrow\infty.}
\]
Here all information quantities and logarithms use natural units (nats).

## Assumptions and scope
The source symbols are i.i.d. uniform on an alphabet of fixed size \(q\). Exactly two *distinct positions* are deleted without replacement; the deletion positions are chosen uniformly, and the receiver sees the surviving symbols in order. The multiplicity \(Z_n\) counts deletion-position pairs, not different resulting output words. The statement concerns fixed two-deletion number as \(n\) grows, not the positive deletion-density regime.

## Proof
**Run rigidity.** A run is a maximal consecutive constant-symbol block of \(X\). If the selected deletion positions belong to runs \(A,B\) with at least two complete runs strictly between them, write their lengths as \(a,b\). Then
\[
Z_n=ab. \tag{1}
\]
To prove (1), consider any alternative deletion pair \(u<v\) producing the same subsequence as the chosen pair \(i<j\). Where the two deletion histories have deleted different numbers of positions, their surviving symbols must agree under a shift by one; on any interval over which one history has deleted exactly one more position, consecutive source symbols therefore coincide. Suppose first that \(i<u\). If \(u\ge j\), the interval from \(i\) until \(j\) contains at least one symbol transition while the two deletion histories have deletion-count discrepancy one: contradiction. Thus \(u<j\), and the intervening comparison forces \(X_i=X_{i+1}=\cdots=X_u\), so \(i,u\) lie in the same run. The case \(u<i\) is symmetric, using the comparison until \(i\). Reading the words backward similarly forces \(j,v\) into the same run. The boundary cases \(u=i\) or \(v=j\) follow by the same one-deletion comparison. Conversely, deleting any one position from each of runs \(A,B\) gives the same output. There are exactly \(ab\) such pairs. (The separation hypothesis avoids the possible two-deletion compensation across a short intervening run.)

**Probability of nonseparation.** Fix a uniformly sampled source position \(U\). The length of its run has expected value bounded by \((q+1)/(q-1)\); each of its four nearest *other* runs (two on each side), if present, has conditional expected length \(q/(q-1)\). Hence the expected number of positions in runs whose run indices differ from the run of \(U\) by at most two is at most \((5q+1)/(q-1)\). Conditional on \(U\), a second uniformly sampled position distinct from \(U\) therefore falls in one of these runs with probability at most \((5q+1)/((q-1)(n-1))\). By (1), outside this event the multiplicity equals the product of the two sampled run lengths.

**Palm run lengths and coupling.** Extend the source in both directions to a doubly infinite i.i.d. \(q\)-ary word. The maximal run containing a fixed site has independent geometric left and right extensions, each with tail \(\Pr(R\ge k)=q^{-k}\). Its total length \(L=1+R_-+R_+\) therefore has probability \(r p^2(1-p)^{r-1}\). For the two uniformly sampled sites, reveal the word only as far as the first unequal symbol on each side of either site. These revealed neighborhoods have bounded expected length depending on \(q\), and hence overlap each other, or extend past an endpoint of the finite word, with probability \(O_q(1/n)\). On the complement, the two neighborhoods may be generated from disjoint independent i.i.d. words, and the two sampled finite-word run lengths have the law of independent \(L_1,L_2\). Combine this coupling with the preceding nonseparation bound to get the stated total-variation estimate, with a finite constant \(C_q\) (which need not be optimal).

**Expected logarithm and information.** Every two-deletion multiplicity is bounded by \(\binom n2\). Under the coupling in the previous paragraph, the error event has probability \(O_q(1/n)\); on it, \(|\log Z_n|\le2\log n\). The two limiting geometric-tailed run lengths have finite moments of all orders; their logarithmic contribution from the exceptional event is \(o(1)\) by Cauchy--Schwarz or exponential-tail truncation. Therefore
\[
\mathbb E\log Z_n=\mathbb E\log(L_1L_2)+o(1)=2\sum_{r\ge1}r p^2(1-p)^{r-1}\log r+o(1).
\]
Because \(Y\) is uniform on \(\Sigma_q^{n-2}\), \(H(Y)=(n-2)\log q\). For fixed \(X=x\), a received output \(y\) has probability \(Z(x,y)/\binom n2\); hence \(H(Y\mid X)=\log\binom n2-\mathbb E\log Z_n\). Subtracting proves the second boxed formula.

## Verification
The standalone `checker.py` independently enumerates two-deletion histories and checks the run-separation identity for every word over alphabets of size \(2,3\) through moderate lengths. It also compares the exact finite planted multiplicity distribution with its predicted product-law limit and validates the mutual-information identity by direct finite summation. These are finite corroborations, not replacements for the all-length run-rigidity and coupling arguments.

## Relationship to prior work
Jeong and Pernice's 2026 random-subsequence model studies the same embedding partition function and planted/null distinction primarily for a positive limiting retention density \(M/N\in(0,1)\). Their dense-limit free energy and annealed formulas do not determine the fixed-two-deletion multiplicity law or its additive mutual-information constant. Atashpendar and collaborators (2018) develop run-based enumeration and conditional supersequence embedding weights for single and double deletions; their exact finite combinatorics is relevant background, but the inspected account does not state a joint planted \(n\to\infty\) product-law limit with total-variation rate. The binary random-center two-deletion-ball variance is a different statistic (the number of *distinct* descendants from one center, not the multiplicity of one planted output). These comparison distinctions are substantive, rather than merely differences in terminology.

## Limitations
The bound leaves the alphabet-dependent constant \(C_q\) unspecified and does not claim optimality of the \(1/n\) rate. Only two uniformly random deletion sites are considered, with \(q\) fixed and uniform i.i.d. source symbols. No claim is made about positive-density deletion regimes, arbitrary source distributions or pointwise approximations for the probability of each unbounded multiplicity. Independent validation and complete historical-priority confirmation remain outstanding; an earlier implicit deduction from run-based insertion enumeration cannot be ruled out.

## References
1. R. Jeong and F. Pernice, “The Random Subsequence Model and Uniform Codes for the Deletion Channel,” arXiv:2604.07234, first posted 2026-04-08, https://arxiv.org/abs/2604.07234.
2. A. Atashpendar, M. Beunardeau, A. Connolly, R. Géraud, D. Mestel, A. W. Roscoe and P. Y. A. Ryan, “From Clustering Supersequences to Entropy Minimizing Subsequences for Single and Double Deletions,” arXiv:1802.00703, first posted 2018-02-02, https://arxiv.org/abs/1802.00703.
3. H. Mercier, M. Khabbazian and V. K. Bhargava, “On the Number of Subsequences When Deleting Symbols From a String,” IEEE Trans. Inform. Theory 54(7), 3279–3285 (2008), DOI 10.1109/TIT.2008.924730.
