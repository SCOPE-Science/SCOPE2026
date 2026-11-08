# Parity-split complete Gabor lifting spectrum of the symmetric cubic Boolean phase

## Finding

For every integer \(n\ge5\), put \(V=\mathbb F_2^n\) and \(N=|V|=2^n\). Consider the canonical completely symmetric cubic Boolean phase
\[
 f(x)=\sum_{1\le i<j<k\le n} x_ix_jx_k \quad\text{in }\mathbb F_2,
 \qquad g(x)=(-1)^{f(x)}.
\]
Let \(W_{a,b}h(x)=(-1)^{b\cdot x}h(x+a)\) and define the complex-linear rank-one-projector measurement operator
\[
 \mathcal L:H\longmapsto\bigl(\operatorname{Tr}(P_{a,b}H)\bigr)_{a,b\in V},\qquad
 P_{a,b}=(W_{a,b}g)(W_{a,b}g)^*.
\]
Here the operator acts on all complex matrices with the Hilbert--Schmidt norm, and the output has the Euclidean norm. No normalization is applied to \(g\); it has squared norm \(N\).

**Exact complete singular spectrum.** For odd \(n\), the nonzero singular values and their multiplicities are
\[
\begin{array}{c|c}
 N^{3/2}&1\\
 N^{3/2}/2&2N-4\\
 \sqrt N\,2^{(n+1)/2}&N^2/4
\end{array}
\]
so \(\operatorname{rank}\mathcal L=N^2/4+2N-3\). For even \(n\), the corresponding table is
\[
\begin{array}{c|c}
 N^{3/2}&2\\
 N^{3/2}/2&2N-8\\
 \sqrt N\,2^{(n+2)/2}&N^2/8
\end{array}
\]
so \(\operatorname{rank}\mathcal L=N^2/8+2N-6\). The remaining \(N^2-\operatorname{rank}\mathcal L\) singular values vanish. In the stated range \(n\ge5\), the three positive values are distinct. In both parity branches,
\[
 \kappa_+(\mathcal L)=2^{\lfloor(n-1)/2\rfloor}.
\]
The rank density converges to \(1/4\) for odd \(n\) and \(1/8\) for even \(n\): an exact parity jump in the fraction of recoverable complex matrix directions.

## Assumptions and scope

All arithmetic in the phase polynomial and all dot products is over \(\mathbb F_2\). The complex Hilbert space \(\ell^2(V)\) has counting measure. The \(N^2\) time-frequency shifts range independently over \(V\times V\). Define the unnormalized self-ambiguity function
\[
 A(a,b)=\sum_{x\in V}g(x+a)\overline{g(x)}(-1)^{b\cdot x}.
\]
The polar rank of a quadratic polynomial \(q\) on \(V\) is the rank over \(\mathbb F_2\) of \(B_q(x,y)=q(x+y)+q(x)+q(y)+q(0)\). The result describes linear operator recovery on all complex matrices, **not** global nonlinear phase-retrieval uniqueness of arbitrary vectors and not sharp weighted Fourier extension.

## Proof

**1. Weyl diagonalization.** The \(N^2\) matrices \(W_{a,b}/\sqrt N\) form an orthonormal Hilbert--Schmidt basis. Conjugation by any \(W_{u,v}\) multiplies \(W_{a,b}\) by the phase \((-1)^{u\cdot b+v\cdot a}\). Thus the column of \(\mathcal L\) corresponding to \(W_{a,b}/\sqrt N\), viewed as a function of \((u,v)\), is an additive character times \(A(a,b)/\sqrt N\), up to a unit scalar. Distinct columns are orthogonal. Since a character on \(V^2\) has Euclidean norm \(N\), the complete singular values are exactly
\[
 \sigma_{a,b}=\sqrt N\,|A(a,b)|\qquad(a,b\in V).
\]

**2. Quadratic derivatives.** Write \(D_af(x)=f(x+a)+f(x)\), and put \(t=\sum_i a_i\pmod2\). Since \(f\) is the third elementary symmetric Boolean polynomial, the quadratic part of \(D_af\) has coefficient \(t+a_i+a_j\) on \(x_ix_j\) for every \(i<j\). Its alternating polar matrix, with \(\mathbf1=(1,\ldots,1)^T\) and \(J=\mathbf1\mathbf1^T\), is
\[
 B_a=t(J+I)+a\mathbf1^T+\mathbf1a^T.
\]
If \(t=0\), then \(B_a=a\mathbf1^T+\mathbf1a^T\). It has rank zero exactly when \(a=0\), or when \(n\) is even and \(a=\mathbf1\); otherwise it has rank two. If \(t=1\), then
\[
 B_ax=x+s(\mathbf1+a)+u\mathbf1,
 \qquad s=\mathbf1\cdot x,\quad u=a\cdot x.
\]
Every kernel element therefore has form \(x=s(\mathbf1+a)+u\mathbf1\). Because \(a\cdot(\mathbf1+a)=0\) and \(a\cdot\mathbf1=1\), the equation for \(u\) is automatic. The equation for \(s\) is \(s=s(n+1)+un\pmod2\). If \(n\) is odd this gives \(s=u\), so \(\ker B_a=\langle a\rangle\), of dimension one. If \(n\) is even it imposes no condition, and \(\mathbf1\) and \(\mathbf1+a\) are linearly independent (odd-weight \(a\) is neither \(0\) nor \(\mathbf1\)); hence \(\dim\ker B_a=2\). Summarizing, for each \(a\) the polar rank \(r(a)\) is
\[
\begin{array}{c|c}
 \text{shift class}&r(a)\\
 a=0,\ \text{and }a=\mathbf1\text{ if }n\text{ even}&0\\
 |a|\text{ even, otherwise}&2\\
 |a|\text{ odd, }n\text{ odd}&n-1\\
 |a|\text{ odd, }n\text{ even}&n-2.
\end{array}
\]
The notation \(|a|\) here means Hamming weight, not vector-space cardinality.

**3. Complete Walsh support lemma.** For any Boolean polynomial \(q\) of degree at most two and polar rank \(r\), its unnormalized Walsh transform \(\widehat{(-1)^q}(b)=\sum_x(-1)^{q(x)+b\cdot x}\) has precisely \(2^r\) nonzero values, all of absolute magnitude \(2^{n-r/2}\). Indeed, a variable change \(y=x+u\) gives
\[
 |\widehat{(-1)^q}(b)|^2
 =\sum_{u\in V}(-1)^{q(u)+q(0)+b\cdot u}
 \sum_{x\in V}(-1)^{B_q(x,u)}.
\]
The inner sum vanishes unless \(u\) lies in the radical \(K\), in which case it equals \(N\). Because \(q(u)+q(0)\) is linear on \(K\), the remaining sum is either \(|K|\) or zero. The nonzero squared modulus is therefore \(N|K|=2^{2n-r}\). Parseval yields \(2^r\) nonzero frequencies. Taking \(q=D_af\) proves that a shift \(a\) contributes exactly \(2^{r(a)}\) nonzero ambiguity coefficients, each of modulus \(2^{n-r(a)/2}\).

**4. Counting all coefficients.** Half of the \(N\) shifts have odd Hamming weight. For odd \(n\) there is one rank-zero even-weight shift, \(N/2-1\) other even-weight shifts of polar rank two, and \(N/2\) odd-weight shifts of rank \(n-1\). Their ambiguity moduli and multiplicities are respectively \((N,1)\), \((N/2,4(N/2-1)=2N-4)\), and \((2^{(n+1)/2},(N/2)2^{n-1}=N^2/4)\). For even \(n\), there are two rank-zero even-weight shifts, \(N/2-2\) other even-weight shifts of rank two, and \(N/2\) odd-weight shifts of rank \(n-2\). Their moduli and multiplicities are \((N,2)\), \((N/2,2N-8)\), and \((2^{(n+2)/2},N^2/8)\). Multiplication by \(\sqrt N\) gives every singular value and the rank formulas above. The ratio of greatest to least positive ambiguity modulus is \(2^{\lfloor(n-1)/2\rfloor}\), proving the stated condition number.

## Verification

The standalone exact script `check.py`, using only the Python standard library, calculates \(D_af\), its polar rank by binary elimination, and its entire Walsh transform for every \(a,b\) at each dimension \(3\le n\le9\). All values, zero counts, and multiplicities match the theorem's formulas, including the predicted collapse of equal levels at dimensions three and four outside the claimed range. The same checker verifies Parseval's total \(\sum_{a,b}|A(a,b)|^2=N^3\) and the positive-subspace condition number. Independent direct projector-matrix singular-value checks at dimensions three and four also agreed with the factor \(\sqrt N\), and are described in `VERIFICATION.md`. Execute `python3 check.py` from this directory. Finite checks are supplementary to the all-dimensional proof.

## Relationship to prior work

Bojarovska and Flinth [1] formulate Gabor phase-retrieval lifting, explain why the full ambiguity spectrum controls linear lifting, and give general sufficient conditions. They do not state this dimension- and parity-resolved singular spectrum for the complete symmetric cubic Boolean phase. Lyons et al. [2] study exactly the same complete symmetric three-uniform hypergraph state from the perspective of its *local Pauli stabilizers*. Their results recover the special existence of one nontrivial unit-modulus Pauli stabilizer at even \(n\) (the second maximal ambiguity coefficient) and its absence at odd \(n\); those facts are **credited as covered**. Their paper does not give the support and amplitudes for all non-stabilizing Pauli coefficients. Nöller, Gühne and Gachechiladze [3] study symmetric hypergraph-state entanglement and nonlocality and reuse the stabilizer classification; the inspected results do not give this all-\(n\) complex-linear Gabor singular spectrum. The quadratic Boolean Walsh-support lemma is standard; the claimed contribution is the complete polar-rank counting for this canonical cubic state and the resulting lifting spectrum, not that lemma or the general Weyl diagonalization.

## Limitations

The theorem concerns the phase window \(g(x)=(-1)^{e_3(x)}\) and the **full** set of Boolean translations and modulations, with the unnormalized conventions stated. The rank concerns the lifted complex matrix map; it does not imply phase-retrieval injectivity for arbitrary vectors, nor does it study measurement subsampling, noisy nonlinear reconstruction, or general cubic Boolean functions. Priority searches are bounded; an uncatalogued all-Pauli-correlation table for symmetric hypergraph states might imply the result. Independent external mathematical audit is not performed.

## References

1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1, first public 19 March 2015; https://arxiv.org/abs/1503.05800.
2. D. W. Lyons et al., *Local Pauli stabilizers of symmetric hypergraph states*, arXiv:1609.01306v1, first public 5 September 2016, https://arxiv.org/abs/1609.01306 (the v4 full text was inspected).
3. J. Nöller, O. Gühne and M. Gachechiladze, *Symmetric hypergraph states: Entanglement quantification and robust Bell nonlocality*, arXiv:2302.01695v1, first public 3 February 2023; https://arxiv.org/abs/2302.01695 (v2 full text inspected).
