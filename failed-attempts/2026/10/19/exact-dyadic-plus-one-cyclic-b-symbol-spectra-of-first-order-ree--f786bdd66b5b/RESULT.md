# Exact dyadic-plus-one cyclic \(b\)-symbol spectra of first-order Reed–Muller codes

## Finding
For integers \(m\ge2\) and \(0\le s<m\), put \(n=2^m\), \(L=2^s\), \(t=m-s\), \(K=2^{t-1}\), and \(b=L+1\). The binary first-order Reed–Muller code, with coordinates enumerated in increasing binary-integer order, has the exact **cyclic** \(b\)-symbol weight enumerator

\[W_{m,s}(Z)=1+4\sum_{r=1}^{2^{m-s-1}-1}Z^{2^{m-1}+2^sr}+\bigl(2^{m+1}-2^{m-s+1}+3\bigr)Z^{2^m}.\]

Here each nonzero weight strictly below \(n\) occurs exactly four times, and the full-weight coefficient is \(2^{m+1}-4K+3\). The distinct positive weights are exactly \(n/2+Lr\), for \(1\le r\le K\), and the minimum nonzero \(b\)-symbol weight is \(n/2+L\). This includes \(K=1\), when all nonzero codewords have full \(b\)-symbol weight. The same enumerator holds when coordinates are enumerated in binary-reflected Gray order.

## Assumptions and scope
The code is \(C_m=\mathrm{RM}(1,m)\) over \(\mathbb F_2\), of length \(n=2^m\) and dimension \(m+1\). For each position \(i\in\{0,\ldots,n-1\}\), let \(i_j\) be bit \(j\) of its binary expansion, where \(0\le j<m\). The evaluation word of \(a=(a_0,\ldots,a_{m-1})\in\mathbb F_2^m\) and \(c\in\mathbb F_2\) is \(x_i=c+\sum_{j=0}^{m-1}a_ji_j\) over \(\mathbb F_2\), in increasing order of \(i\). For any length-\(n\) binary word \(x\), its cyclic \(b\)-symbol weight \(w_b(x)\) equals the number of starts \(i\in\{0,\ldots,n-1\}\) for which \((x_i,\ldots,x_{i+b-1})\) is not all zero; indices are reduced modulo \(n\). The enumerator counts codewords, not code equivalence classes.

## Proof
**1. Transition spectrum for affine binary-integer words.** Fix \(t\ge1\) and a nonconstant affine evaluation word \(v=(v_i)_{i=0}^{2^t-1}\), where \(v_i=c+\sum_{j=0}^{t-1}a_ji_j\) with \(a\ne0\). All such words are balanced: exactly \(2^{t-1}\) positions contain zero. Let \(R\) denote the number of cyclic runs of zeros. By balance and nonconstancy, the number of zero-to-one transitions and one-to-zero transitions both equal \(R\), so the total cyclic transition count is \(2R\).

Set \(p_j=\sum_{h=0}^j a_h\pmod2\) for \(0\le j<t\). In the cyclic list of integers, for each \(0\le j\le t-2\) exactly \(2^{t-j-1}\) edges flip precisely bits \(0,\ldots,j\), while the two remaining edges flip all \(t\) bits (the carry across \(2^{t-1}\) and the wrap-around). Consequently
\[
R=\sum_{j=0}^{t-2}2^{t-j-2}p_j+p_{t-1}.
\]
The transformation \(a\mapsto(p_0,\ldots,p_{t-1})\) is bijective. The first \(t-1\) bits express every integer from zero to \(2^{t-1}-1\) uniquely in binary, while \(p_{t-1}\) adds either zero or one. Excluding the zero mask gives the following complete distribution of \(R\): each value \(1,\ldots,2^{t-1}-1\) arises from exactly two nonzero masks, and \(2^{t-1}\) from exactly one. Each mask has two offsets \(c\), so the corresponding multiplicities among affine words are four and two, respectively. The argument includes \(t=1\), where the sum is empty and \(R=p_0\).

**2. Nonconstant low-bit part forces full window weight.** Put \(L=2^s\) and partition the length-\(n\) word into consecutive aligned blocks of \(L\) positions. When at least one of \(a_0,\ldots,a_{s-1}\) is nonzero, the restriction to every block is either a fixed nonconstant balanced binary word \(V\) or its complement. Thus no all-zero run contains a whole block. A run crossing a boundary between equal blocks has length at most \(L-1\), because a suffix of zeros and a prefix of zeros longer than \(L-1\) would cover every position of the nonconstant word \(V\). For complementary neighboring blocks, a zero suffix of \(V\) of length \(u\) and a zero prefix of its complement of length \(v\) satisfy \(u+v\le L\): otherwise some index belongs both to a zero suffix and a one prefix of \(V\). These bounds also apply at the cyclic wrap-around. Therefore every cyclic zero run has length at most \(L\). Each window of length \(b=L+1\) has at least one nonzero symbol, so \(w_b(x)=n\).

**3. Zero low-bit part gives exactly the displayed spectrum.** Suppose \(a_0=\cdots=a_{s-1}=0\). The length-\(n\) word consists of \(L\) repeated copies of each symbol of an affine evaluation word \(v\) in \(t=m-s\) bits. When \(v\) is nonconstant, let its cyclic zero runs have lengths \(k_1,\ldots,k_R\). Balance gives \(\sum k_j=2^{t-1}\). After repetition, their lengths become \(Lk_j\). Such a zero run contains exactly \(Lk_j-(L+1)+1=L(k_j-1)\) all-zero cyclic windows of length \(L+1\). Hence
\[
w_b(x)=n-\sum_{j=1}^R L(k_j-1)=n-L(2^{t-1}-R)=n/2+LR.
\]
By Step 1, for every \(1\le R<K\) exactly four codewords have that weight. The endpoint \(R=K\) has weight \(n\) and two codewords. The zero word contributes \(1\) and the all-one word contributes \(Z^n\). Of the \(2^{m+1}\) distinct codewords, exactly \(4(K-1)\) have weight below \(n\) but above zero, so the full-weight multiplicity is \(2^{m+1}-1-4(K-1)=2^{m+1}-4K+3\). This proves the stated polynomial and all its corollaries.

**4. Reflected Gray order.** The reflected Gray permutation of the \(m\)-bit indices is \(g(i)=i\oplus(i\gg1)\), with bitwise XOR and shift. This is invertible and linear over \(\mathbb F_2\). As \(a\) and \(c\) range over all affine functions, so do the compositions \(c+a\cdot g(i)\). Their evaluation words constitute precisely the same codeword set in the index coordinate order. Therefore the enumerator is unchanged.

## Verification
The standalone Python checker `verify_spectrum.py` enumerates all \(2^{m+1}\) affine words for every \(2\le m\le9\). It computes each cyclic window weight directly with prefix sums on doubled words and verifies the predicted complete histogram for each \(b=2^s+1\), \(0\le s<m\). It separately constructs the binary-integer and binary-reflected Gray indexing, and all comparisons pass. The finite census corroborates, but does not replace, the proof for all \(m\).

For reproducibility: `python3 verify_spectrum.py` requires only Python 3.10+. Example: for \(m=3\), \(s=0\), the result is \(1+4Z^5+4Z^6+4Z^7+3Z^8\); at \(m=4\), \(s=2\), it is \(1+4Z^{12}+27Z^{16}\).

## Relationship to prior work
General cyclic \(b\)-symbol weight and generalized symbol weight definitions and run-based identities appear in Liu and Pan (2021), and Shi, Zhu and Helleseth (2021). Zhu and collaborators (2024) give code-independent restrictions on the cardinality of the symbol-weight spectrum. Zhu and Liao (2023) determine distributions for MDS codes, a class that only intersects the present first-order family in the small case \(m=2\). Ordinary Hamming weight enumerators of first-order Reed–Muller codes are standard; they do not encode the cyclic run arrangement and so do not alone imply the displayed \(b\)-symbol coefficients. The present proof specializes transition combinatorics to the natural binary-integer/Gray coordinate ordering and the dyadic-plus-one windows.

## Limitations
The formula is proved for first-order binary Reed–Muller codes only, with the stated coordinate order and \(b=2^s+1\). Other orderings need not preserve cyclic window weights; no formula for other window widths or higher-order Reed–Muller codes is asserted. Previous unindexed equivalent results cannot be ruled out from literature searches alone. Finite checker runs are supporting evidence and not a substitute for the infinite proof.

## References
- Liu and Pan, *Generalized \(b\)-Symbol Weights of Linear Codes and \(b\)-Symbol MDS Codes*, arXiv:2103.16299 (version 1 publicly posted 2021-03-30). https://arxiv.org/abs/2103.16299
- Shi, Zhu and Helleseth, *Connections among Hamming metric, \(b\)-symbol metric, and \(r\)th generalized Hamming metric*, arXiv:2109.13764 (2021). https://arxiv.org/abs/2109.13764
- Zhu, Li, Shi, Xia and Solé, *Some bounds on the cardinality of the \(b\)-symbol weight spectrum of codes*, arXiv:2404.02471 (2024). https://arxiv.org/abs/2404.02471
- Zhu and Liao, *The \(b\)-weight distribution for MDS codes*, Advances in Mathematics of Communications, DOI:10.3934/amc.2023028 (2023). https://doi.org/10.3934/amc.2023028
