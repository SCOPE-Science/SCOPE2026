# Square-root path-variation instability and an exact random-mask law for Walsh–Hadamard soft thresholding

## Finding
For each integer \(d\ge2\) let \(n=2^d\) and \(H_n\) be the orthonormal real Sylvester Walsh–Hadamard matrix in natural binary order. Fix any \(\lambda>0\). Preserve the constant transform coefficient, soft-threshold all other coefficients at \(\lambda\), and invert the transform, obtaining \(T_\lambda\). Equip the input and output with **open-path** adjacent total variation \(V(h)=\sum_{i=0}^{n-2}|h_{i+1}-h_i|\). The sharp, attained two-input sensitivity
\[
 K_n=\sup_{V(f-g)>0}\frac{V(T_\lambda f-T_\lambda g)}{V(f-g)}
\]
is independent of \(\lambda\) and satisfies
\[
 \boxed{\frac12+\frac{n-2}{2}\frac{\binom{n/2}{n/4}}{2^{n/2}}\le K_n\le \frac{2(\sqrt n-1)}{\sqrt2-1}.}
\]
Consequently \(K_n=\Theta(\sqrt n)\) for dyadic lengths. For \(n=2\), the exact coefficient is \(K_2=1\). Exhaustive exact-mask calculations give \(K_4=3/2\) and \(K_8=11/4\).

A companion **exact random-mask theorem**, with no unproved numerical approximation, states the following. Let \(A\) select each nonconstant Walsh character independently with probability \(1/2\), let \(P_A\) project onto those characters and the constant, and let \(e_0\) be the coordinate unit impulse at the first entry. For every dyadic \(n\ge4\),
\[
 \boxed{\mathbb E_A V(P_A e_0)=\frac12+\frac{n-2}{2}\frac{\binom{n/2}{n/4}}{2^{n/2}}\sim\sqrt{\frac n\pi}.}
\]
Thus the observed amplification under random spectral selection and the worst two-input amplification have the same sharp **growth exponent**, although the precise leading constant for the worst case is not determined.

## Assumptions and scope
The signal index set is \(\{0,\ldots,n-1\}\) with its ordinary integer order, **not** the Boolean-cube adjacency relation. Encode an index \(i\) as \(d\) binary bits, set \(\chi_r(i)=(-1)^{r\cdot i}\) with dot product modulo two, and use \(H_n(r,i)=n^{-1/2}\chi_r(i)\). Every real input is permitted; positivity, random inputs and noise models are not assumed. For \(r\ne0\), its transformed coefficient \(c_r\) is mapped to \(\operatorname{sgn}(c_r)(|c_r|-\lambda)_+\); \(c_0\) is unchanged. The fixed positive threshold is identical across nonconstant frequencies. A mask \(A\subseteq\{1,\ldots,n-1\}\) means retaining the constant and exactly those frequencies in \(A\). Randomness pertains solely to the independent Bernoulli mask, not the input or the filter. The stated \(K_n\) is a global two-input seminorm Lipschitz constant, not a one-input variation ratio.

## Proof
**1. Strict affine chambers and a cut identity.** On a strict soft-threshold chamber, the derivative of \(T_\lambda\) is \(P_A\), the orthogonal projection onto the constant and a selected set of nonconstant Walsh characters. Every mask occurs on a nonempty open chamber: choose transform coordinates equal to \(2\lambda\) for active frequencies and zero for inactive frequencies. Along any input segment, integration of the piecewise affine derivative and the variation triangle inequality give
\[
 K_n=\max_A\|P_A\|_{V\to V}.
\]
For a step \(h_k(i)=\mathbf1_{i\ge k}\) with \(1\le k<n\), every vector can be written as \(h=h(0)\mathbf1+\sum_{k=1}^{n-1}(h(k)-h(k-1))h_k\). Projections \(P_A\) preserve constants, hence
\[
 \|P_A\|_{V\to V}=\max_{1\le k<n}V(P_Ah_k).
\]
One of finitely many masks and steps maximizes this expression. Choosing a sufficiently small multiple of that step within its strict chamber realizes the **global** ratio by an actual pair of finite inputs. This establishes attainment and threshold independence, rather than only a derivative supremum.

**2. Haar-band decomposition and the dimension-uniform upper bound.** Walsh characters whose least significant set bit is at binary position \(d-1-j\), namely \(r=2^{d-1-j}(2q+1)\) with \(0\le q<2^j\), span the standard discrete Haar detail space \(W_j\), with \(2^j\) dyadic blocks of common length \(\ell_j=n/2^j\), for \(0\le j<d\). A function \(u\in W_j\) takes value \(a_b\) on the left half of block \(b\) and \(-a_b\) on its right half. Therefore, including the between-block edges,
\[
 V(u)\le 4\sum_{b=1}^{2^j}|a_b|\le4\sqrt{\frac{2^j}{\ell_j}}\,\|u\|_2.
\]
For a single step \(h_k\), its orthogonal component in \(W_j\) lies along at most **one** normalized block Haar function: the only block containing the step changes internally. Its normalized coefficient has absolute value at most \(\sqrt{\ell_j}/2\). The projection onto any subcollection of Walsh characters in the band is an \(\ell^2\) contraction on \(W_j\). It follows that the band contribution to a masked step has variation at most \(2\sqrt{2^j}\). Since the constant component has zero variation,
\[
 V(P_Ah_k)\le\sum_{j=0}^{d-1}2\sqrt{2^j}=\frac{2(\sqrt n-1)}{\sqrt2-1}.
\]
This holds for every mask and cut, proving the global upper bound. In particular the argument uses the **natural binary order of the path** and not a Boolean-cube graph-gradient commutation identity.

**3. Exact random spectral-mask mean.** Set \(e_0=(1,0,\ldots,0)\) and write \(\eta_r\in\{0,1\}\) for independent fair selection of \(r\ne0\), with the constant coefficient always present. Walsh inversion gives
\[
 (P_Ae_0)(i)=\frac1n\left(1+\sum_{r\ne0}\eta_r\chi_r(i)\right).
\]
At the first edge, the difference is nonnegative:
\[
 (P_Ae_0)(0)-(P_Ae_0)(1)=\frac2n\sum_{r:\chi_r(1)=-1}\eta_r,
\]
whose expected absolute value is \(1/2\). At each other edge \((i,i+1)\), with \(i\ge1\), the mean term cancels by Walsh orthogonality, and writing \(\eta_r=(1+\varepsilon_r)/2\) gives a sum \(n^{-1}S_m\) in distribution, where \(m=n/2\) and \(S_m\) is a sum of \(m\) independent Rademacher signs. The key point is that exactly \(n/2\) characters distinguish any two different vertices, and the two vertices are both nonzero, so the deterministic contribution vanishes. For \(m\) even the elementary binomial identity
\[
 \mathbb E|S_m|=m\frac{\binom m{m/2}}{2^m}
\]
follows by splitting the symmetric binomial distribution at its central term (equivalently, telescoping \((2j-m)\binom mj\)). Summing the \(n-2\) remaining edges proves
\[
 \mathbb E_A V(P_Ae_0)=\frac12+\frac{n-2}{n}\mathbb E|S_{n/2}|=\frac12+\frac{n-2}{2}\frac{\binom{n/2}{n/4}}{2^{n/2}}.
\]
For every mask, \(V(P_Ae_0)\le \|P_A\|_{V\to V}V(e_0)=\|P_A\|_{V\to V}\), so the expectation bounds \(K_n\) below. Stirling's formula \(\binom m{m/2}/2^m\sim\sqrt{2/(\pi m)}\) yields the claimed exact asymptotic \(\mathbb E V(P_Ae_0)\sim\sqrt{n/\pi}\), completing \(K_n=\Theta(\sqrt n)\). At \(n=2\) direct projection onto DC or all frequencies gives \(K_2=1\).

## Verification
Run `python3 verify.py` with Python 3 and its standard library. The checker completely enumerates all masks and all input steps for \(n=2,4,8\), tests the exact random-mask mean by exhaustive averaging, and verifies the displayed small-dimensional coefficients. It also evaluates 560 independently sampled higher-dimensional masks and their strict nonlinear chambers at \(n=16,32,64,128\) against the universal upper bound. The asymptotic and all-dimensional claims are proved by Steps 1–3 above, not by finite numerical tests. The computational checker uses the unnormalized fast Walsh transform with its required inverse \(1/n\), and applies soft threshold \(\lambda\sqrt n\) to unnormalized coefficients; this is exactly the stated orthonormal convention.

## Relationship to prior work
The Walsh–Hadamard transform and spectral methods are classical; Cheraghchi and Indyk (2015, arXiv:1504.07648) study its sparse computational recovery, not path variation after coefficient soft thresholding. Chen and collaborators (2014, arXiv:1411.7414) study graph signal recovery using a graph-shift variation functional and optimization; their full text does not derive this two-input open-path sensitivity or its exact random-mask impulse law. Related published work on Walsh spectral soft thresholding proves a \(\Theta(\sqrt n)\) bound for **Boolean-cube graph edge variation**; its commuting coordinate-difference bound does not transfer to an ordered path, where adjacent integers can differ in several binary digits. Separately, published analyses of **DCT-II** spectral shrinkage obtain square-root path-variation growth by a sine-transform projection identity, which does not control Walsh spectral masks. For **Haar** shrinkage on the same finite path, prior work obtains logarithmic rather than square-root growth because a cut couples to only one Haar wavelet per scale; the present proof instead exploits nontrivial Walsh spectral selection within each Haar band. None of the closely inspected statements determines the exact binomial random-mask variation mean on the ordered path or the present all-dimensional Walsh path bound. More remote or unindexed equivalent results may exist.

## Limitations
The leading asymptotic constant of \(K_n/\sqrt n\), and whether that ratio converges, are not determined. No characterization of all maximizing spectral masks is given, and random-mask expected variation is **not** asserted equal to the worst-case coefficient. Exhaustive enumeration covers only the displayed small dyadic dimensions. The theorem assumes real data, natural Sylvester binary ordering, full unweighted open-path total variation, and a fixed uniform strictly positive threshold. It does not cover sequency-ordered inputs, nonuniform weights, hard thresholding, time-varying threshold choices, or Boolean-cube graph variation. Although the relevant indexed and full-text comparisons were checked, complete historical priority cannot be certified from accessible sources alone.

## References
1. S. Chen, A. Sandryhaila, J. M. F. Moura, J. Kovačević, *Signal Recovery on Graphs: Variation Minimization*, arXiv:1411.7414v1, first public 2014-11-26, https://arxiv.org/abs/1411.7414 .
2. M. Cheraghchi and P. Indyk, *Nearly Optimal Deterministic Algorithm for Sparse Walsh-Hadamard Transform*, arXiv:1504.07648v1, first public 2015-04-28, https://arxiv.org/abs/1504.07648 .
3. D. Tisserand and C. Berviller, *Original structure for Walsh–Hadamard transform on sliding window*, Electronics Letters (2015), DOI: 10.1049/el.2015.1246, https://doi.org/10.1049/el.2015.1246 .
4. *Walsh spectral soft thresholding has sharp Boolean-cube variation amplification of order \(2^{d/2}\)*, related mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-walsh-spectral-soft-thresholding-has-sharp-boolean-cube-variatio--0b2aff0e8d4f .
5. *Square-root variation instability of discrete-cosine soft thresholding*, related mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-square-root-variation-instability-of-discrete-cosine-soft-thresh--5000fe7c11db .
6. *Exact nine-state computation and logarithmic path-variation instability of finite Haar soft thresholding*, related mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-nine-state-computation-and-logarithmic-path-variation-inst--8271a7c110ab .
