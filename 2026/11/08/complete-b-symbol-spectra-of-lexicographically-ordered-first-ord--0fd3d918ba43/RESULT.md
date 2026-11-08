# Complete \(b\)-symbol spectra of lexicographically ordered first-order Reed–Muller codes

## Finding

For every integer \(m\ge2\), put \(n=2^m\). Enumerate \(\mathbb F_2^m\) in the natural binary order \(0,1,\ldots,n-1\), with the least significant binary digit changing fastest. Let \(C=\mathrm{RM}_2(1,m)\) comprise the \(2n\) evaluation words of all Boolean affine functions in this order. For \(1\le b\le n\), the cyclic \(b\)-symbol weight \(w_b(v)\) is the number of starting positions whose length-\(b\) cyclic window in \(v\) is not identically zero.

The complete \(b\)-symbol weight enumerator \(\mathcal W_{m,b}(z)=\sum_{v\in C}z^{w_b(v)}\) is
\[
\mathcal W_{m,1}(z)=1+(2n-2)z^{n/2}+z^n.
\]
For \(2\le b\le n\), let \(K\) be the **largest power of two satisfying** \(Kb\le n\), and put
\[
\boxed{\mathcal W_{m,b}(z)=1+4\sum_{k=1}^{K-1}z^{\omega_{m,b}(k)}+(2n+3-4K)z^n.}
\]
The exponents in the sum are strictly increasing, nonzero and smaller than \(n\). They are explicit: writing \((x)_+=\max\{x,0\}\), define
\[
\omega_{m,b}(1)=n-(n/2-b+1)_+.
\]
For \(2\le k\le n/2\), set \(j=\lceil\log_2 k\rceil\), \(s=2^{m-j-1}\), \(u=2(k-2^{j-1})\), and \(v=2^j-k\). Then
\[
\omega_{m,b}(k)=n-u(s-b+1)_+-v(2s-b+1)_+.
\]
In particular, for \(b=2\) the complete spectrum is \(1+4\sum_{h=n/2+1}^{n-1}z^h+3z^n\); every intermediate pair weight has multiplicity exactly four. For every \(b\ge2\), *every nonfull positive weight also has multiplicity exactly four*, and exactly \(K-1\) such weights occur.

More structurally, if \(v\) is any nonconstant affine evaluation word and \(k\) is its number of cyclic zero-runs, then the multiset of zero-run lengths is determined **only by \(k\)**: for \(k=1\) it is \(\{n/2\}\), and for \(k\ge2\) it consists of \(u\) copies of \(s\) and \(v\) copies of \(2s\), using the preceding definitions. There are exactly four affine codewords for each \(1\le k<n/2\), and exactly two for \(k=n/2\).

## Assumptions and scope

The alphabet is \(\mathbb F_2\). For coefficients \(a=(a_0,\ldots,a_{m-1})\in\mathbb F_2^m\) and \(c\in\mathbb F_2\), the coordinate at integer \(0\le x<n\), whose binary digits are \(x_i\), equals \(f_{a,c}(x)=c+\sum_{i=0}^{m-1}a_ix_i\pmod2\). The order is fixed and essential; an arbitrary permutation of coordinates need not preserve the conclusion. Every cyclic window is read modulo \(n\). The all-zero and all-one words are each counted once.

## Proof

**1. Balance and transitions.** For \(a\ne0\), the affine truth table has exactly \(n/2\) zeros and \(n/2\) ones, independently of \(c\). Write \(T\) for its number of adjacent symbol changes around the cycle. As a binary cyclic word, it has \(k=T/2\) zero-runs and \(k\) one-runs.

**2. Exact transition distribution.** Define prefix parities \(p_j=a_0+\cdots+a_{j-1}\pmod2\) for \(1\le j\le m\). For \(x<n-1\), incrementing \(x\) flips its lowest \(j\) bits for exactly \(n/2^j\) indices when \(1\le j\le m\); the extra wraparound transition from \(n-1\) to \(0\) flips all \(m\) bits. Therefore
\[
T=\sum_{j=1}^{m-1}2^{m-j}p_j+2p_m,\qquad
k=\sum_{j=1}^{m-1}2^{m-j-1}p_j+p_m.
\]
The triangular map \(a\mapsto(p_1,\ldots,p_m)\) is a bijection. The first \(m-1\) prefix bits give every integer \(h\in\{0,\ldots,n/2-1\}\) in binary, and the last bit adds either zero or one. Thus there is one coefficient vector for \(k=0\), two for every \(1\le k<n/2\), and one for \(k=n/2\). The unique \(k=0\) vector is \(a=0\). Including both constants \(c\) gives the stated multiplicities for nonconstant codewords.

**3. Only two adjacent dyadic zero-run sizes.** For \(a\ne0\), let \(t\) be the least index with \(a_t=1\) and put \(s=2^t\). The truth table is constant on each successive length-\(s\) block. Adjacent blocks numbered \(2r\) and \(2r+1\) have opposite values, because the changing digit at position \(t\) is selected and all higher digits agree. These opposite blocks preclude three successive equal blocks, even cyclically. Therefore each cyclic zero-run has length \(s\) or \(2s\).

**4. Recover all zero-runs from \(k\).** If there are \(u\) short and \(v\) long zero-runs, balance and the run count imply
\[
u+v=k,\qquad s(u+2v)=n/2,
\qquad u=2k-n/(2s),\quad v=n/(2s)-k.
\]
Consequently \(n/(4s)\le k\le n/(2s)\) whenever both scales are available, with the endpoint interpreted directly when \(t=m-1\). If \(k>1\), put \(j=\lceil\log_2 k\rceil\). For a strict inequality at the lower endpoint, necessarily \(s=2^{m-j-1}\). At the lower endpoint, every run has length \(2s\), which gives the same run multiset with the preceding dyadic scale. Substitution yields \(u=2(k-2^{j-1})\) and \(v=2^j-k\). At \(k=1\), balance forces the unique zero-run to have length \(n/2\). In particular, this multiset depends on \(k\), not on the individual affine coefficients or the constant term.

**5. Convert runs to cyclic window counts.** A zero-run of length \(r\) contributes exactly \((r-b+1)_+\) all-zero cyclic windows of length \(b\). This also holds if the run wraps around index zero. Subtracting these counts from the total \(n\) starting positions gives the formulas for \(\omega_{m,b}(k)\) and the constant-word boundary cases.

**6. Distinct nonfull weights and saturation.** Going from the canonical zero-run multiset for \(k\) to that for \(k+1\) splits one longest dyadic run of length \(2s\) into two runs of length \(s\). The decrease in the all-zero-window count equals
\[
(2s-b+1)_+-2(s-b+1)_+.
\]
For \(b\ge2\) this is strictly positive whenever the split run has length at least \(b\), and zero otherwise. The first \(k\) for which all zero-runs are shorter than \(b\) is exactly the largest power of two \(K\) with \(Kb\le n\): at \(k=K\) all zero-runs have length \(n/(2K)<b\), whereas every \(k<K\) has a zero-run of length at least \(b\). Hence \(\omega_{m,b}(1)<\cdots<\omega_{m,b}(K-1)<n\), and all \(k\ge K\) have weight \(n\).

**7. Enumerate codewords.** There is one all-zero word of weight zero. For \(1\le k<K\), exactly four words have the distinct weight \(\omega_{m,b}(k)\). Of the other \(2n-1-4(K-1)=2n+3-4K\) nonzero words, every one has full \(b\)-weight \(n\). At \(b=1\), balance gives the separate Hamming enumerator. This completes the proof.

## Verification

Run `python verify.py` from the directory containing this document. The verifier independently enumerates every affine evaluation word for \(2\le m\le9\), computes the complete cyclic-window profile directly from word bits, tests the formula at every \(b\), verifies each zero-run multiset, and checks the entire enumerator for all \(b\). It additionally tests 240 fixed-seed instances at \(m=10,11\). The successful run printed `VERIFY_OK configs=2280 individual_b_weights=1067680 full_distributions=1020`. The proof, not finite testing, establishes every \(m\) and \(b\).

## Relationship to prior work

Pan, Ling and Liu [1], Theorem 4.6, determine the **minimum** \(b\)-symbol distance of Reed–Muller codes. The minimum \(\min\{n/2+b-1,n\}\) for the first-order binary case agrees with the first nonzero weight proved here. It does not imply the multiplicities, other weights, run-length classification or complete distribution. Ma and Luo [2], Section 4, obtain symbol-window weight distributions for cyclic and modified simplex codes; their codes and coordinate orders are different, and they stress ordering dependence. Vega [3], Section 4, classifies semiprimitive irreducible cyclic code spectra; the present full-length affine evaluation code has length a power of two and is not a member of that coprime-length irreducible cyclic family. Zhu and Shi [4], Sections 1 and 3, treat Kasami codes, not the ordered first-order Reed–Muller family. The usual Hamming enumerator is standard and is not claimed as new.

## Limitations

The classification is only for binary degree-at-most-one evaluation codes, coordinates in increasing binary integer order, and the cyclic \(b\)-symbol convention. It does not assert an arbitrary-order, punctured, simplex, higher-order Reed–Muller, or general cyclic-code enumerator. Bibliographic searches can miss equivalent formulas written under Walsh-function, run-length or alternative coding terminology. Independent mathematical validation has not been performed.

## References

1. Xu Pan, San Ling, Hongwei Liu, *New bounds for b-Symbol Distances of Matrix Product Codes*, arXiv:2309.08920v1, publicly submitted 2023-09-16, Section 4 and Theorem 4.6. https://arxiv.org/abs/2309.08920
2. Junru Ma, Jinquan Luo, *Symbol-pair Weight Distributions of Some Linear Codes*, arXiv:1911.02184, publicly submitted 2019-11-06, Section 4. https://arxiv.org/abs/1911.02184
3. Gerardo Vega, *The b-symbol weight distributions of all semiprimitive irreducible cyclic codes*, *Designs, Codes and Cryptography* 91 (2023), 2213–2221, Section 4. https://doi.org/10.1007/s10623-023-01193-w
4. Hongwei Zhu, Minjia Shi, *The b-symbol weight hierarchy of the Kasami codes*, arXiv:2112.04019v1, publicly submitted 2021-12-07, especially Sections 1 and 3. https://arxiv.org/abs/2112.04019
