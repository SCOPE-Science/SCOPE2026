# Leaf-set Walsh recovery and exact dyadic valuations for Cayley trees

## Finding

Let \(n\ge2\), and let \(\mathcal T_n\) denote all \(n^{n-2}\) unrooted labelled trees on vertex set \([n]\). Let \(L(T)\subseteq[n]\) be the degree-one vertices of \(T\), and define the integer counting kernel \(f_n:\mathbb F_2^n\to\mathbb Z_{\ge0}\) by
\[
f_n(x)=\#\{T\in\mathcal T_n:1_{L(T)}=x\}.
\]
The unnormalized Walsh multiplier of the corresponding XOR convolution is
\[
\Lambda_n(S)=\sum_{x\in\mathbb F_2^n} f_n(x)(-1)^{\sum_{i\in S}x_i},\qquad S\subseteq[n].
\]
Writing \(k=|S|\), the complete valuation classification is
\[
\Lambda_n(S)=\sum_{j=0}^{k}\binom{k}{j}(-2)^j(n-j)^{n-2},\qquad
\nu_2(\Lambda_n(S))=
\begin{cases}
0,&n\text{ odd or }n=2,\\
(n-2)\nu_2(n),&n\ge4\text{ even and }k=0,\\
1+\nu_2(k),&n\ge4\text{ even and }1\le k\le n.
\end{cases}
\]
In particular, **no multiplier vanishes** and counting convolution is invertible over \(\mathbb Q\) and \(\mathbb R\) for every \(n\ge2\). For even \(n\ge4\), exactly \(2^{n-1}\) multipliers have binary valuation one; the other valuations and their multiplicities are determined by character-weight binomial sums. The greatest common divisor of the absolute values of all multipliers is \(1\) when \(n\) is odd or \(n=2\), and \(2\) for even \(n\ge4\). For odd \(n\) and for \(n=2\), the integral convolution matrix is invertible over the 2-adic integers, whereas for even \(n\ge4\) it is not.

## Assumptions and scope

The trees are **labelled, unrooted, undirected** spanning trees of the complete graph \(K_n\); each tree contributes once before projection to its leaf set. For \(n=2\), both vertices count as leaves. The kernel is *multiplicity weighted*, not the zero-one indicator of which leaf sets are attainable. Fourier coefficients use the **unnormalized** \(\{\pm1\}\)-valued characters of \(\mathbb F_2^n\); the convolution matrix has dimension \(2^n\). We use \(\nu_2(a)\) for the exponent of two dividing a nonzero integer \(a\). The claim has no isolated-vertex convention for \(n=1\).

## Proof

**1. Exact character formula.** The Prüfer correspondence identifies \(\mathcal T_n\) with the length-\(n-2\) words on \([n]\), and a vertex is a leaf precisely when its label is absent from the word. For a fixed character set \(S\) of size \(k\), expand
\[
(-1)^{|L(T)\cap S|}=\prod_{i\in S}(1-2\,1_{\{i\in L(T)\}}).
\]
For any specified \(j\)-set of vertices required to be leaves, the number of Prüfer words avoiding them is \((n-j)^{n-2}\); the empty-word boundary uses the combinatorial convention \(0^0=1\) at \(n=j=2\). Summing over subsets of \(S\) gives the displayed character formula. This also proves that the multiplier depends only on \(k\), not on the labels in \(S\).

**2. Odd orders and the two-vertex boundary.** For odd \(n\), the term \(j=0\) is \(n^{n-2}\), an odd integer, and every term with \(j\ge1\) has a factor two. Hence all multipliers are odd. When \(n=2\), the Prüfer word is empty and both vertices are leaves, so \(\Lambda_2(S)=(-1)^{|S|}\), also always odd.

**3. Even orders.** Assume even \(n\ge4\), let \(1\le k\le n\), and put \(s=\nu_2(k)\). The \(j=1\) term is \(-2k(n-1)^{n-2}\), which has exact valuation \(s+1\), since \(n-1\) is odd. We show that every other term is divisible by \(2^{s+2}\). For \(2\le j\le k\), the identity \(j\binom{k}{j}=k\binom{k-1}{j-1}\) implies
\[
\nu_2\!\left(2^j\binom{k}{j}\right)\ge s+j-\nu_2(j).
\]
When \(j\ge3\) is odd, \(j-\nu_2(j)\ge3\), proving the needed divisibility. When \(j\ge2\) is even, \(n-j\) is even and the extra factor \((n-j)^{n-2}\) supplies at least \(n-2\ge2\) powers of two; since \(j-\nu_2(j)\ge1\), such terms actually have valuation at least \(s+3\). For the \(j=0\) term, \((n-2)\nu_2(n)\ge s+2\): this holds directly at \(n=4\), and for even \(n\ge6\) follows from \(s\le\lfloor\log_2n\rfloor\) and \(n-2\ge\lfloor\log_2n\rfloor+2\). Therefore
\[
\Lambda_n(S)\equiv-2k(n-1)^{n-2}\pmod{2^{s+2}},
\]
and its valuation is exactly \(s+1\). For \(k=0\), the multiplier is simply \(n^{n-2}\), of valuation \((n-2)\nu_2(n)\). All coefficients are nonzero, completing the invertibility assertion.

**4. Gcd, valuation counts, and mod-two invertibility.** For \(n\ge3\), the coefficients at weights zero and one are \(n^{n-2}\) and \(n^{n-2}-2(n-1)^{n-2}\), whose gcd is \(1\) at odd \(n\) and \(2\) at even \(n\), since consecutive integers are coprime. At even \(n\ge4\), all multipliers are even and those at odd \(k\) have valuation one, so the gcd is exactly two. The count of odd-weight subsets of \([n]\) is \(2^{n-1}\). More generally, for positive \(t\), the number of nontrivial frequencies with valuation \(t\) is
\[
\sum_{\substack{1\le k\le n\\\nu_2(k)=t-1}}\binom nk.
\]
The trivial frequency contributes one additional multiplier of valuation \((n-2)\nu_2(n)\). For odd \(n\) or \(n=2\), every Walsh eigenvalue is odd, so the determinant of the integer convolution matrix is odd; equivalently, the matrix is invertible over \(\mathbb Z_2\). For even \(n\ge4\), all its eigenvalues are even and the determinant is not a 2-adic unit.

## Verification

Run `python3 verify.py` from the directory containing this file. The script needs only Python's standard library. It independently constructs every Prüfer word through eight vertices; compares the resulting complete Walsh transforms with the inclusion-exclusion formula; derives character sums separately from the exact Stirling-number leaf-set count; and tests the valuations, spectral gcd, and absence of cancellation for all character weights through \(n=128\). These finite calculations supplement but **do not replace** the all-order divisibility proof above. The verifier's current result is 18,541 passing exact assertions.

## Relationship to prior work

The Prüfer encoding and the exact prescribed-leaf-set counts are classical. Lennon (2008) studies the locality of the Prüfer encoding under mutation; his paper supplies an explicitly dated account of the coding framework but not a Fourier recovery theorem. Remmel and Williamson (2010) prove that the number of trees having a prescribed leaf set of size \(r\) is \((n-r)!\,S(n-2,n-r)\), with \(S\) the Stirling number of the second kind, and develop ranking and unranking algorithms. Those exact counts determine each multiplier after an additional Krawtchouk transform but do **not** themselves assert the uniform all-order nonvanishing and sharp per-character dyadic valuations proved here. The distinction from Fourier results for *edge-incidence* distributions of spanning trees is essential: an edge-sign character is not a leaf-set character, since leafhood is a nonlinear function of the edge set. The contribution here is the exact arithmetic Fourier stratification, not a new Prüfer code or a new leaf-count formula.

## Limitations

The claim applies only to the leaf-set **counting pushforward** for Cayley trees and to the prime two. It gives no sharp real minimum magnitude or \(\ell^2\) condition number, and no conclusions for other graph families or primes. Binary valuations of Walsh eigenvalues do **not** by themselves determine the Smith normal form over \(\mathbb Z_2\), because the Walsh change-of-basis matrix is not invertible over \(\mathbb Z_2\). A possible equivalent earlier signed occupancy or leaf-enumerator specialization remains a historical priority risk; the bounded primary-literature comparisons are not a proof of global novelty. The archival source date below identifies dated supporting literature, not a date of publication of this theorem.

## References

- Craig Lennon, *On the locality of the Prüfer code*, initial public arXiv submission 24 February 2008, https://arxiv.org/abs/0802.3514.
- Jeffrey B. Remmel and S. Gill Williamson, *Ranking and unranking trees with a given number or a given set of leaves*, initial public arXiv submission 10 September 2010, https://arxiv.org/abs/1009.2060.
