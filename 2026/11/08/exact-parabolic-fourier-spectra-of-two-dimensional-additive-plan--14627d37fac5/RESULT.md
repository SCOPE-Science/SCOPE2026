# Exact parabolic Fourier spectra of two-dimensional additive planes

## Finding

Let \(p\) be an odd prime, let \(m\ge3\), let \(q=p^m\), and let \(H\) be an arbitrary two-dimensional \(\mathbb F_p\)-subspace of \(\mathbb F_q\). For a nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C\), define the **unnormalized** parabolic Fourier transform of its indicator by
\[
S_H(a,b)=\sum_{x\in H}\psi(ax^2+bx),\qquad (a,b)\in\mathbb F_q^2.
\]
The complete magnitude distribution of \(S_H\) has **exactly two possible types**, determined by the existence of a quadratic subfield and the multiplicative form of the support.

**Generic case.** If \(H\ne u\mathbb F_{p^2}\) for every \(u\ne0\), then the exact multiplicities among the \(q^2\) frequency pairs are

| Magnitude | Multiplicity |
| :-- | --: |
| \(0\) | \(q^2(p^2-1)(p^2-p+1)/p^5\) |
| \(p\) | \(q^2(1-1/p)\) |
| \(p^{3/2}\) | \(q^2(p^2-1)/p^4\) |
| \(p^2\) | \(q^2/p^5\) |

**Subfield-line case.** If \(m\) is even and \(H=u\mathbb F_{p^2}\) for some nonzero \(u\in\mathbb F_q\), then

| Magnitude | Multiplicity |
| :-- | --: |
| \(0\) | \(q^2(p^2-1)/p^4\) |
| \(p\) | \(q^2(1-1/p^2)\) |
| \(p^{3/2}\) | \(0\) |
| \(p^2\) | \(q^2/p^4\) |

Thus the magnitude histogram itself detects precisely the scalar copies of \(\mathbb F_{p^2}\). For even \(m\), subfield-line planes are exactly the minimizers of the number of zeros, and all other planes are tied maximizers; their zero counts have the strict ratio
\[
\frac{Z_{\mathrm{generic}}}{Z_{\mathrm{subfield}}}=\frac{p^2-p+1}{p}>1.
\]
For odd \(m\), every plane is generic. The number of subfield-line planes is \((q-1)/(p^2-1)\) when \(m\) is even, and zero otherwise, among
\[
\binom{m}{2}_p
=\frac{(q-1)(q-p)}{(p^2-1)(p^2-p)}
\]
two-dimensional prime-field subspaces.

More precisely, for each fixed \(a\) let \(z_H(a)=|\{b:S_H(a,b)=0\}|\). In the generic case its complete distribution over \(a\) is
\[
\begin{array}{c|ccc}
z_H(a)&q(1-1/p^2)&q(1-1/p)&0\\ \hline
\#a&q/p^3&q(p^2-1)/p^3&q(p^3-p^2)/p^3
\end{array}.
\]
In the subfield-line case, exactly \(q/p^2\) values of \(a\) have \(z_H(a)=q(1-1/p^2)\), and all other \(a\) have \(z_H(a)=0\).

## Assumptions and scope

The field characteristic is odd; \(m\ge3\) ensures that \(|H|=p^2<q\), so the indicator is a proper partial support of the finite parabola. All coefficients on \(H\) are one; arbitrary complex coefficients are not included. The frequencies \((a,b)\) range over the full \(\mathbb F_q^2\). The transform is unnormalized, so \(S_H(0,0)=p^2\). The character may be any nontrivial additive character: every such character is \(\psi(z)=\exp(2\pi i\operatorname{Tr}(cz)/p)\) for \(c\ne0\), and replacing \((a,b)\) by \((ca,cb)\) is a bijection.

## Proof

**1. Exact Gaussian modulus, including degeneracy.** Fix \(a\in\mathbb F_q\) and write \(Q_a(x)=\operatorname{Tr}(a x^2)\) on the two-dimensional \(\mathbb F_p\)-space \(H\). Its polarized bilinear form is \(B_a(x,y)=\operatorname{Tr}(2axy)\); let \(R_a\) be its radical and \(d_a=\dim_{\mathbb F_p}R_a\). A change of variables \(h=x-y\), \(y=y\) in the squared modulus and orthogonality of additive characters give
\[
|S_H(a,b)|^2
=\sum_{h,y\in H}\psi(a(h^2+2hy)+bh)
=p^2\sum_{h\in R_a}\psi(bh),
\]
with any fixed canonical nontrivial trace character; the arbitrary-character case follows by parameter reindexing as above. Since \(p\) is odd, \(B_a(h,h)=2Q_a(h)\), so \(Q_a(h)=0\) for every \(h\in R_a\). The last sum is \(p^{d_a}\) when the linear character \(h\mapsto\psi(bh)\) is trivial on \(R_a\), and zero otherwise. The trace pairing of \(\mathbb F_q\) is nondegenerate, so exactly \(q/p^{d_a}\) values of \(b\) satisfy this condition. Therefore
\[
|S_H(a,b)|\in\{0,p^{1+d_a/2}\},\qquad
\#\{b:|S_H(a,b)|=p^{1+d_a/2}\}=q/p^{d_a}.
\tag{1}
\]
This identity is valid for every rank and is the normalization-critical step.

**2. The rank map and the exceptional support.** Choose a basis \(u,v\) for \(H\) with \(u\ne0\), and put \(r=v/u\notin\mathbb F_p\). The matrix of the bilinear form divided by the harmless nonzero scalar \(2\) is
\[
M_a=\begin{pmatrix}
\operatorname{Tr}(au^2)&\operatorname{Tr}(auv)\\
\operatorname{Tr}(auv)&\operatorname{Tr}(av^2)
\end{pmatrix}.
\]
Nondegeneracy of the field-trace pairing implies that the linear map \(a\mapsto M_a\) onto symmetric two-by-two prime-field matrices has rank \(\dim_{\mathbb F_p}\operatorname{span}\{1,r,r^2\}\). This rank is three unless \(r\) has quadratic minimal polynomial over \(\mathbb F_p\). The latter happens precisely when \(m\) is even and \(r\in\mathbb F_{p^2}\setminus\mathbb F_p\); then \(H=u\mathbb F_{p^2}\).

For a generic plane, \(a\mapsto M_a\) is surjective with each matrix having \(q/p^3\) preimages. Among the \(p^3\) symmetric two-by-two matrices, one has rank zero, exactly \(p^2-1\) have rank one (choose an image line in \(p+1\) ways and a nonzero scalar in \(p-1\) ways), and \(p^3-p^2\) have rank two. Thus the counts of parameters \(a\) with radical dimensions \(2,1,0\), respectively, are
\[
q/p^3,\qquad q(p^2-1)/p^3,\qquad q(p^3-p^2)/p^3.
\tag{2}
\]

If \(H=u\mathbb F_{p^2}\), use trace transitivity to write the restricted bilinear form as
\[
B_a(ux,uy)=\operatorname{Tr}_{\mathbb F_{p^2}/\mathbb F_p}(2\,c_a xy),\quad
c_a=\operatorname{Tr}_{\mathbb F_q/\mathbb F_{p^2}}(au^2).
\]
The relative trace is surjective and has kernel of size \(q/p^2\). For \(c_a\ne0\), the displayed pairing is nondegenerate (multiplication by \(c_a\) preserves nondegeneracy of the trace pairing), while for \(c_a=0\) it vanishes. Thus precisely \(q/p^2\) values of \(a\) have radical dimension two, and the rest have radical dimension zero; radical dimension one never occurs.

**3. Distribution and rigidity.** Insert these counts into (1). A radical of dimension zero gives \(q\) amplitudes of magnitude \(p\) and no zeros; a radical of dimension one gives \(q/p\) amplitudes of magnitude \(p^{3/2}\); a radical of dimension two gives \(q/p^2\) amplitudes of magnitude \(p^2\). The complement of those nonzero amplitudes supplies all the zeros, yielding the two tables and the fiber distributions above. In particular,
\[
Z_{\mathrm{generic}}=
\frac{q^2(p^2-1)(p^2-p+1)}{p^5},\quad
Z_{\mathrm{subfield}}=\frac{q^2(p^2-1)}{p^4}.
\]
Their ratio is strictly greater than one for every odd prime. The generic histogram contains a positive number of amplitude-\(p^{3/2}\) positions, while the subfield histogram contains none; consequently these cases are distinguished even by the unlabeled magnitude histogram. Finally, scalar copies of the multiplicative subfield are indexed by the cosets of \(\mathbb F_{p^2}^{\times}\) in \(\mathbb F_q^{\times}\), giving \((q-1)/(p^2-1)\) exceptional planes. The standard count of ordered bases divided by the number of ordered bases in a two-plane yields the stated Gaussian binomial coefficient. This completes the classification. \(\square\)

## Verification

The embedded standalone `CHECK.py` constructs finite fields directly from irreducible polynomial quotients, computes finite traces, evaluates every Fourier sum through its cyclotomic phase histogram, and compares exact cyclotomic zeros and numerically evaluated squared magnitudes with the predicted rank formulas. Tested fields are \(\mathbb F_{27}\), \(\mathbb F_{125}\), and \(\mathbb F_{81}\), including both generic and subfield planes in the latter. An exhaustive basis-independent classification also checks every prime-field two-plane in these fields: 13, 31, and 130 planes respectively, 174 in total. The checker tests Parseval's identity \(\sum_{a,b}|S_H(a,b)|^2=q^2p^2\), the zero-fiber distributions, the multiplicities of all amplitude levels (squared amplitudes rounded with a stated numerical tolerance), and the subfield-plane counts. Run with `python3 CHECK.py` using only Python's standard library. These finite examples are not substituted for the all-prime, all-extension-degree proof.

## Relationship to prior work

Li, *Sharp Total-Support Uncertainty for the Standard Complete Set of Mutually Unbiased Bases* (the first arXiv version appeared September 11, 2026 under a finite-parabola uncertainty title), studies sharp Fourier-zero bounds for arbitrary nonzero coefficients on proper subsets of the **prime field**. It does not state a prime-power extension-field two-plane classification or the exact four-level magnitude and zero-fiber distributions. The classical quadratic Gauss-sum modulus rule and counts of ranks of symmetric matrices are inputs to, not original aspects of, this result. The point requiring a separate argument is the multiplicative classification of all two-dimensional trace-quadratic restrictions and the resulting exact Fourier histograms.

Iosevich, Liu, Mayeli and Pakianathan study Fourier bandwidth, annihilating sets and affine-subspace Fourier zeros over prime-field vector spaces; the objects and the precise curved-graph spectra here differ. Iosevich and Koh establish extension inequalities on finite-field quadratic surfaces, rather than an exact spectral histogram indexed by all partial supports of this type. Biró and Lev establish general structural finite-plane uncertainty inequalities, rather than this parabolic rank classification. Schmidt classifies and counts general quadratic and symmetric forms through association schemes; the raw rank counts are prior work, whereas the distinguishing step here is the particular trace-restriction pencil associated with each plane. No claim is made that the quadratic Gaussian orthogonality identity itself is new.

## Limitations

The result is confined to **equal coefficients** on two-dimensional prime-field linear subspaces and to the full unweighted parabolic transform in **odd characteristic** with extension degree at least three. It does not characterize arbitrary equal-cardinality supports, arbitrary weights, general quadratic curves, or optimal restricted measurements. Magnitude counts alone do not recover the actual plane within each histogram type. An earlier unindexed equivalence to standard rank-weight enumerators, possibly from coding theory, remains a priority risk; the current comparisons establish originality only relative to the inspected sources.

## References

1. D. Li, *Sharp Total-Support Uncertainty for the Standard Complete Set of Mutually Unbiased Bases*, arXiv:2609.16030 (first public version 2026-09-11). https://arxiv.org/abs/2609.16030
2. A. Iosevich, A. Liu, A. Mayeli, J. Pakianathan, *Wavelet decomposition and bandwidth of functions defined on vector spaces over finite fields*, arXiv:1601.03473 (2016). https://arxiv.org/abs/1601.03473
3. A. Iosevich, D. Koh, *Extension theorems for Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505 (2008). https://arxiv.org/abs/0804.4505
4. A. Biró, V. F. Lev, *Uncertainty in finite planes*, arXiv:1808.07424 (2018; journal version 2021). https://arxiv.org/abs/1808.07424
5. K.-U. Schmidt, *Quadratic and symmetric bilinear forms over finite fields and their association schemes*, arXiv:1803.04274 (2018). https://arxiv.org/abs/1803.04274
