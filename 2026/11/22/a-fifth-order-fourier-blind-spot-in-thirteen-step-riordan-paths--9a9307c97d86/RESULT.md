# A fifth-order Fourier blind spot in thirteen-step Riordan paths

## Finding
For Riordan excursions of length \(13\), the binary Fourier transform of horizontal-step positions vanishes at exactly \(176\) of the \(8192\) characters, all having weight at least five. The exact number of vanishing characters by Hamming weight is \(22,66,66,22\) in weights \(5,6,7,8\). Thus counting convolution has rank \(8016\), positive spectral gap \(2\), and positive-spectrum condition number \(5649\). The smallest nonempty order exhibiting a Fourier zero while **all** characters on at most four positions survive is \(13\). Its Fourier range has minimum possible endpoint projection norm \(1105/256\) in both \(\ell^1\) and \(\ell^\infty\).

## Assumptions and scope
A Riordan path of length \(n\) is a word of steps \(U=(1,1)\), \(D=(1,-1)\), and \(H=(1,0)\) that begins and ends at height zero, stays at nonnegative heights, and uses no horizontal step starting at height zero. For each path \(P\), write \(h(P)\in\mathbb F_2^n\) for its coordinatewise indicator of horizontal steps, indexed by \(1,\ldots,n\). These indicators are not required to be distinct: the counting function \(f_n(x)=|\{P:h(P)=x\}|\) has multiplicity. Its (unnormalized) Walsh transform is
\[
W_n(S)=\sum_{x\in\mathbb F_2^n} f_n(x)(-1)^{\langle S,x\rangle}=\sum_{P\in\mathcal R_n}(-1)^{\sum_{i\in S}h(P)_i}.
\]
Define \(T_n g=f_n*g\) with unnormalized convolution on \(\mathbb F_2^n\). All results are exact at \(n=13\), together with exhaustive boundary checks at every nonempty order \(2\le n\le12\); no claim is made for larger orders.

## Proof
**Exact exhaustive finite certificate.** A depth-first recursion enumerates precisely the admissible words: at each height it may take an up-step, may take a down-step only if the height is positive, and may take a horizontal step only at positive height. The terminal condition is height zero after exactly \(n\) steps. Each choice uniquely determines a Riordan path, so the exhaustive recursion gives a complete counting function \(f_n\), including multiplicities. An integer fast Walsh–Hadamard transform of this full vector returns all \(2^n\) integer multipliers, without numerical approximation. A separately implemented height-state transfer recurrence computes, for each specified frequency, the same signed sum; all \(8192\) multipliers agree at \(n=13\), and all smaller orders agree as well.

The exact census at \(n=13\) gives \(|\mathcal R_{13}|=11298\), \(176\) zeros of weights \(5,6,7,8\) with respective multiplicities \(22,66,66,22\), and \(8016\) nonzeros (\(4008\) positive and \(4008\) negative). The frequency \(S=\{2,3,4,6,7\}\) is an explicit vanishing witness. Among nonzero multipliers, the smallest magnitude is \(2\) and the largest is \(11298\). Therefore the convolution diagonalization on \(\ell^2\) gives the rank, sharp positive singular-value ratio \(11298/2=5649\), and Moore–Penrose operator norm \(1/2\).

For comparison, the exact zero counts in orders \(2,3,4,5,6,7,8,9,10,11,12\) are respectively \(0,0,0,16,0,8,0,64,0,0,0\), with minimum zero weights respectively undefined, undefined, undefined, \(1\), undefined, \(2\), undefined, \(2\), undefined, undefined, undefined. This establishes the first-order assertion without extrapolating from a partial search.

**Unrestricted projection optimality.** Let \(E=\{S:W_{13}(S)\ne0\}\). The Fourier projection \(P\) onto \(\operatorname{ran}T_{13}\) has multiplier \(1_E\) and convolution kernel
\[
p(x)=2^{-13}\sum_{S\in E}(-1)^{\langle S,x\rangle}.
\]
An exact second Walsh transform computes the numerator \(k(x)=8192p(x)\). Its absolute-value histogram (value: multiplicity) is
\[
\begin{array}{c|rrrrrrrrrrrr}
|k|&0&16&32&48&64&80&96&112&128&144&176&8016\\
\#&7412&328&208&140&40&26&16&14&4&2&1&1
\end{array}
\]
and thus \(\sum_x|k(x)|=35360\), giving \(\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=35360/8192=1105/256\). For any real or complex projection \(Q\) onto the same translation-invariant Fourier range, average \(Q\) over all translations. This gives a translation-commuting projection onto the same range with norm no greater than \(\|Q\|\); since each Fourier character is a simultaneous one-dimensional eigenspace, the unique translation-commuting projection onto this range is \(P\). Hence no unrestricted projection has smaller endpoint norm.

## Verification
Run `python3 verify.py` using Python 3.9+ and the standard library. The independently constructed path-mask enumeration, fast Walsh transform, and signed height-state recurrence are checked against each other at all frequencies for every \(2\le n\le13\). The checker additionally verifies the full finite zero census, one explicit weight-five cancellation, the exact nonzero spectral gap, both signs of the surviving frequencies, the complete absolute projection-kernel histogram, and its rational endpoint norm. All integer arithmetic is exact.

## Relationship to prior work
The Riordan-number sequence and its interpretation as Motzkin paths with horizontal steps forbidden at ground height were recorded before this calculation [1]. Chen, Deng, and Yang [2] study the path family, bijections with pattern-avoiding derangements, and ordinary unsigned counts. Their relations determine the value at the trivial character but do not state the location-dependent signed horizontal-step sums computed here. Existing global horizontal-step generating functions are not equivalent to a positionwise Walsh spectrum. In particular, the result for unrestricted Motzkin paths does not determine this different restricted path ensemble.

## Limitations
The complete Fourier census, optimal projection constant, and first-order assertion are finite, exact statements only up to path length thirteen. There is no general formula for the locationwise signed spectrum at arbitrary length, nor a claim of independent external audit. Priority cannot be established from search alone; an equivalent earlier unindexed computation remains possible.

## References
[1] OEIS Foundation, *A005043: Riordan numbers*, https://oeis.org/A005043 (entry includes a dated 2003-11-09 interpretation as Motzkin paths with no horizontal steps at level zero).

[2] W. Y. C. Chen, E. Y. P. Deng, and L. L. M. Yang, *Riordan Paths and Derangements*, arXiv:math/0602298v1, first posted 2006-02-14, https://arxiv.org/abs/math/0602298.
