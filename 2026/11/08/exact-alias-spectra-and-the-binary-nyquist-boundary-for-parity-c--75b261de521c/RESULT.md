# Exact alias spectra and the binary Nyquist boundary for parity-check Fourier sampling

## Finding

Let \(A\) be any finite abelian group of order \(q\ge2\), let \(n\ge2\) and \(0\le r<n\), and let \(\widehat A\) be its character group. Write
\[
 C=\{(x_1,\ldots,x_n)\in A^n:\sum_i x_i=0\},\quad
 F_r=\{\gamma\in\widehat A^n:|\{i:\gamma_i\ne1\}|\le r\}.
\]
Define the normalized Fourier sampling operator \(R:\mathbb C^{F_r}\to\mathbb C^C\) by
\[
 (Rc)(x)=q^{-(n-1)/2}\sum_{\gamma\in F_r}c_\gamma\prod_i\gamma_i(x_i).
\]
Put \(s=n-r\), \(J=\min\{q,\lfloor n/s\rfloor\}\), and \(E_{s-1}(z)=\sum_{a=0}^{s-1}z^a/a!\). The **complete nonzero squared-singular-value spectrum** of \(R\) is precisely the set of integers \(1,2,\ldots,J\), each strictly present, with respective multiplicities
\[
 M_j=\frac{n!}{q}\binom qj[z^n]\bigl(e^z-E_{s-1}(z)\bigr)^j E_{s-1}(z)^{q-j},\qquad1\le j\le J.
\]
The remaining \(|F_r|-\sum_{j=1}^JM_j\) squared singular values are zero, counting the Gram eigenvalues on the coefficient domain. In particular,
\[
 \operatorname{rank}R=q^{n-1}-\frac{n!}{q}[z^n]E_{s-1}(z)^q,
 \quad\kappa_+(R)=\sqrt{\min\{q,\lfloor n/(n-r)\rfloor\}},
\]
where \(\kappa_+\) uses the nonzero singular values. The operator is injective exactly when \(2r<n\) and surjective exactly when \(r\ge n-\lceil n/q\rceil\). It is square and unitary exactly when \(q=2\), \(n\) is odd, and \(r=(n-1)/2\). At the first aliasing radius \(r=n/2\) for even \(n\), all nonzero squared singular values lie in \(\{1,2\}\), and the kernel dimension is exactly
\[
 \frac{q-1}{2}\binom{n}{n/2}.
\]
This classification is independent of the isomorphism type of \(A\).

## Assumptions and scope

All assertions range over **every** finite abelian alphabet \(A\) of order \(q\ge2\), not merely elementary abelian or finite-field groups. The neutral character in \(\widehat A\) is denoted \(1\). The frequency set is a Hamming ball in \(\widehat A^n\), whereas the observation set is the **linear checksum hyperplane** \(C\), not a Hamming sphere, coordinate slab, or Cartesian rectangle. The normalization gives each restricted character column norm one. The domain dimension is \(|F_r|=\sum_{k=0}^r\binom nk(q-1)^k\), and \(|C|=q^{n-1}\). Rank and singular-value multiplicities are over \(\mathbb C\); the integers in the formulas are exact.

## Proof

**1. Character annihilator.** The annihilator of \(C\) inside \(\widehat A^n\) is the diagonal subgroup \(\Delta=\{(\eta,\ldots,\eta):\eta\in\widehat A\}\). Indeed, restriction to \(C\) annihilates precisely the characters that factor through the sum map \(A^n\to A\). By orthogonality on \(C\), the Gram entry at \(\gamma,\gamma'\in F_r\) is one exactly when \(\gamma^{-1}\gamma'\in\Delta\), and otherwise zero. Thus on each diagonal orbit \(\gamma\Delta\), the Gram block is an all-ones matrix of order \(t=|F_r\cap\gamma\Delta|\), with nonzero eigenvalue \(t\) once and zero \(t-1\) times. Orbits not meeting \(F_r\) contribute no Gram columns.

**2. Occupancy and all spectral values.** For an arbitrary \(\gamma=(\gamma_1,\ldots,\gamma_n)\) let \(N_\eta(\gamma)=|\{i:\gamma_i=\eta\}|\). The vector \(\gamma(\eta^{-1},\ldots,\eta^{-1})\) has frequency Hamming weight \(n-N_\eta(\gamma)\). Hence
\[
 t(\gamma)=\#\{\eta\in\widehat A:N_\eta(\gamma)\ge s\}.
\]
The bound \(t(\gamma)\le J\) follows because these occupancy counts sum to \(n\). For every integer \(1\le j\le J\), select \(j\) distinct symbols, use \(s\) coordinates for each of the first \(j-1\), and put the remaining \(n-(j-1)s\ge s\) coordinates on the last. Exactly \(j\) symbols occur at least \(s\) times. Thus every squared singular value \(j=1,\ldots,J\) occurs.

**3. Multiplicities.** Each diagonal orbit contains exactly \(q\) distinct words. There are \(\binom qj\) choices of symbols having occupancy at least \(s\). Multinomial enumeration of all words with exactly \(j\) such symbols is
\[
 n!\binom qj[z^n](e^z-E_{s-1}(z))^jE_{s-1}(z)^{q-j}.
\]
Dividing by orbit size \(q\) gives \(M_j\). Similarly the words with no symbol occurring at least \(s\) number \(n![z^n]E_{s-1}(z)^q\); dividing by \(q\) and subtracting from all \(q^{n-1}\) orbits gives the rank. Since the smallest positive squared singular value is always one and the largest is \(J\), the displayed condition number follows.

**4. Sharp thresholds.** Two distinct words of \(F_r\) belong to one diagonal orbit only if their Hamming distance equals \(n\), as multiplication by a nontrivial common character changes every coordinate. If \(2r<n\), the triangle inequality prohibits this. Conversely, if \(2r\ge n\), choose two distinct character symbols occupying \(s=n-r\) and \(n-s=r\) coordinates: both have an orbit representative of Hamming weight at most \(r\). Thus injectivity is equivalent to \(2r<n\). Surjectivity is equivalent to every diagonal orbit meeting \(F_r\), or every \(q\)-symbol word having a repeated-symbol count at least \(s\). Its smallest possible largest occupancy is \(\lceil n/q\rceil\), proving the surjectivity threshold. Simultaneous injectivity and surjectivity requires \(q=2\) and odd \(n\), with necessarily \(r=(n-1)/2\); in that case all Gram eigenvalues are one, so the square matrix is unitary.

**5. First singular shell.** If \(n\) is even and \(r=n/2\), at most two symbols can occur at least \(n/2\) times. Exactly two do so only when their occupancy counts are both \(n/2\), yielding \(\binom q2\binom n{n/2}/q=(q-1)\binom n{n/2}/2\) two-element blocks. Each contributes exactly one kernel dimension, completing the claim.

## Verification

`check.py` constructs the normalized character matrix directly, diagonalizes its Gram matrix, and independently enumerates diagonal orbits and symbol occupancy counts. Its recorded replay covered \(69\) cases for cyclic alphabets of orders \(2,3,4,5\), the noncyclic four-element alphabet, and a product alphabet of order six. Across all cases the largest direct spectral discrepancy was approximately \(1.03\times10^{-14}\), within finite-precision error. The proof above, not this finite enumeration, establishes all parameter ranges.

## Relationship to prior work

Character orthogonality on finite abelian groups and the annihilator correspondence for codes are classical. Cheraghchi, Guruswami, and Velingker (first public version 2012-07-04, arXiv:1207.1140) analyze random restricted Fourier matrices and their restricted-isometry implications for coding; their problem is probabilistic and sparse-vector based, rather than the exact deterministic spectrum of a low-interaction character band sampled on one checksum hyperplane. Existing harmonic restriction studies of fixed Hamming-weight observation shells and coordinate-slab observation patterns involve different observation subsets and Gram couplings. The asserted contribution is the universal complete integer spectrum with occupancy multiplicities, two sharp rank thresholds, and the precise binary odd-length unitary boundary; the foundational diagonal-annihilator lemma is not itself claimed new.

## Limitations

The theorem addresses one checksum equation with all coordinate coefficients equal to the identity and a full Hamming frequency ball. It does not classify general linear-code parity matrices, unequal coordinate alphabets, weighted Fourier sampling, missing sample sites, or noise amplification on the kernel. Exact singular values do not by themselves provide a sparse nonlinear decoder. Historical priority for an equivalent occupancy-spectral formula in older coding/harmonic-analysis literature remains an acknowledged risk, despite the bounded comparisons reported separately. Independent mathematical evaluation has not been performed.

## References

- M. Cheraghchi, V. Guruswami, and A. Velingker, *Restricted Isometry of Fourier Matrices and List Decodability of Random Linear Codes*, arXiv:1207.1140v1, posted 2012-07-04, https://arxiv.org/abs/1207.1140.
- Classical finite-abelian character orthogonality and code-annihilator duality are used as standard background, not as new results.
