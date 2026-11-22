# First even-Bell Fourier recovery for block-opener profiles of set partitions

## Finding
For every integer \(1\le n\le8\), let \(\Pi_n\) be the set of set partitions of \([n]\) and let \(O(\pi)\) be the set of minimum elements of their blocks (the *block openers*). On \(G_n=(\mathbb Z/2\mathbb Z)^n\), define \(f_n(x)=\#\{\pi\in\Pi_n:1_{O(\pi)}=x\}\) and unnormalized XOR convolution \(T_nh=f_n*h\).

The exact convolution ranks for orders \(n=1,2,3,4,5,6,7,8\) are respectively
\[
2,\ 2,\ 8,\ 16,\ 30,\ 64,\ 128,\ 256.
\]
Thus the **only singular orders through eight are two and five**. At order two the vanishing Fourier characters have supports \(\{2\}\) and \(\{1,2\}\); at order five they have supports \(\{2,3,4\}\) and \(\{1,2,3,4\}\). The respective nullities are two and two.

The eighth order is the **first Fourier-invertible order with an even Bell number**: the earlier even Bell numbers occur at orders two and five, and both corresponding convolutions are singular. At order eight there are no zero frequencies, and
\[
\min_{A\subseteq[8]}|\widehat f_8(A)|=8,
\qquad \|T_8^{-1}\|_{2\to2}=\frac18,
\qquad \kappa_2(T_8)=\frac{1035}{2}.
\]
The minimum is attained at exactly eight frequencies (four pairs related by toggling the first coordinate). At order five the least possible operator norm of any projection onto \(\operatorname{ran}T_5\), not just a translation-invariant projection, is exactly \(15/8\) on both \(\ell^1(G_5)\) and \(\ell^\infty(G_5)\).

These are **finite-cutoff results for \(n\le8\)**; no claim about the singularity classification or sharp gaps at larger orders is made.

## Assumptions and scope
Coordinates of \(G_n\) are indexed by \([n]\). Each set partition is counted once. The first coordinate of every opener vector equals one. Fourier characters are \(\chi_A(x)=(-1)^{\sum_{i\in A}x_i}\), with no averaging in the Fourier transform: \(\widehat f_n(A)=\sum_{x\in G_n}f_n(x)\chi_A(x)\). Convolution uses counting measure, and operator norms use unnormalized counting \(\ell^p\) norms. The smallest nonzero absolute multiplier is reported, not the smallest signed multiplier.

The restricted-growth encoding lists blocks by their smallest elements. A coordinate is an opener exactly when its letter starts a new previously unseen block. The independent spectral coordinates after the forced first opener are indexed by masks \(a\in\{0,\ldots,2^{n-1}-1\}\), whose low bit records position two.

## Proof
For a proposed opener set \(S\subseteq[n]\) containing one, write \(b_{i-1}(S)=|S\cap[i-1]|\). When reading a restricted-growth word from left to right, the letter at each opener position is forced to introduce the new block, whereas at each nonopener \(i\) there are exactly \(b_{i-1}(S)\) existing blocks available. Therefore
\[
f_n(1_S)=\prod_{i\in[n]\setminus S}b_{i-1}(S),
\qquad f_n(x)=0\text{ if }x_1=0.
\]
This is a closed exact formula without a recursive or heuristic approximation.

Set \(g_n(a)=f_n(1_S)\), where \(S=\{1\}\cup\{j+2: a_j=1\}\), and let
\[
L_n(m)=\sum_{a=0}^{2^{n-1}-1}(-1)^{\operatorname{popcount}(a\mathbin{\&}m)}g_n(a).
\]
For each full Fourier support, the multiplier is either \(L_n(m)\) or \(-L_n(m)\), according as position one is absent or present. Thus each reduced zero produces precisely two full zeros and each reduced minimum absolute value is attained twice.

The attached exact integer certificate lists every \(g_n(a)\) and every \(L_n(m)\) for each \(1\le n\le8\). Its independent checker first generates restricted-growth words recursively (rather than using the product), compares the resulting histograms with the product formula, and computes every reduced Walsh value twice: by direct signed sums and by the integer butterfly transform. All \(2^{n-1}\) masks are covered for each \(n\). The complete lists have zero-mask sets \(\{1\}\) at order two, \(\{7\}\) at order five, and empty sets at all other orders through eight. At order eight the least absolute entry is eight, occurring for reduced masks \(4,54,111,122\). The Bell total is \(B_8=4140\), which is the maximum absolute Fourier multiplier by the triangle inequality (attained at the trivial character). This proves the finite rank and inverse-norm assertions and \(\kappa_2=4140/8=1035/2\).

At order five the two null characters are \(\chi_{\{2,3,4\}}\) and \(\chi_{\{1,2,3,4\}}\). The canonical Fourier range projection \(P\) is convolution by
\[
p(x)=1_{\{0\}}(x)-2^{-5}\big(\chi_{\{2,3,4\}}(x)+\chi_{\{1,2,3,4\}}(x)\big).
\]
The parenthesized sum is zero when \(x_1=1\), and has absolute value two when \(x_1=0\). Hence \(p(0)=15/16\), it has exactly fifteen further nonzero values of absolute value \(1/16\), and \(\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=15/8\). Given *any* projection \(Q\) onto \(\operatorname{ran}T_5\), average its conjugates under all thirty-two translations. Their average is a translation-invariant projection with range \(\operatorname{ran}T_5\). In Fourier coordinates the only such projection is \(P\); convexity and isometry of translations imply \(\|P\|\le\|Q\|\). This proves unrestricted optimality of \(15/8\).

## Verification
Run `python3 checker.py certificate.json` with Python 3.8 or later. It independently enumerates every restricted-growth word through order eight, verifies exact integer histograms, performs direct character summation and a separate Walsh butterfly, checks every tabulated spectrum and all stated gaps/zero masks. There are no network dependencies or floating-point operations. The certificate uses a reduced \((n-1)\)-bit coordinate system solely because position one is always an opener; the proof above reconstructs the full \(n\)-bit spectrum.

## Relationship to prior work
The standard restricted-growth encoding and the bijection with set partitions are classical, explicitly used by Sagan in 2006 and by Shattuck in 2010. Neither examined source calculates the Walsh spectrum of the block-opener *set*, the first even-Bell recovery, the sharp eighth-order inverse norm, or the fifth-order endpoint projection constant. Other work on partition co-block *edge* incidence and on singleton-block incidence uses mathematically different embeddings and does not imply this statement. The elementary enumeration itself is not claimed as new; the new mathematical content is its exact Fourier information-loss and stability behavior at the first parity-obstruction failure.

## Limitations
No general theorem is asserted for orders nine and above. Exhaustive finite integer enumeration is sufficient here because the theorem is explicitly restricted to eight vertices; it does not imply an infinite recurrence. The novelty assessment remains bounded by the sources and searchable records actually compared; unindexed prior calculations remain possible. No independent audit has been performed.

## References
- B. E. Sagan, *Pattern Avoidance in Set Partitions*, first public arXiv version 12 April 2006, https://arxiv.org/abs/math/0604292; Section 4 introduces restricted-growth encodings.
- M. Shattuck, *Recounting the Number of Rises, Levels, and Descents in Finite Set Partitions*, *Integers* 10 (2010), 179–185, published 20 April 2010; https://doi.org/10.1515/INTEG.2010.013.
