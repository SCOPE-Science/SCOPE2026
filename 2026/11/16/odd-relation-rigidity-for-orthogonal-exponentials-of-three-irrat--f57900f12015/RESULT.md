# Odd-relation rigidity for orthogonal exponentials of three irrational Bernoulli factors

## Finding

Let \(a,b,c>0\), assume that \(a/b\), \(b/c\), and \(c/a\) are irrational, and put
\[
\mu=\frac18(\delta_0+\delta_a)*(\delta_0+\delta_b)*(\delta_0+\delta_c),\qquad
A=\frac1a,\quad B=\frac1b,\quad C=\frac1c.
\]
Define \(N(\mu)\) as the supremum of the cardinalities of pairwise orthogonal families of exponentials \(\{e^{2\pi i\lambda x}:\lambda\in\Lambda\}\) in \(L^2(\mu)\). Then:

**Sharp orthogonality law.** If the rational span of \(A,B,C\) has dimension three, \(N(\mu)=2\). If the rational span has dimension two, let \((p,q,r)\in\mathbb Z^3\) denote the unique primitive integer relation, up to common sign,
\[pA+qB+rC=0,\qquad \gcd(|p|,|q|,|r|)=1.\]
Then
\[
N(\mu)=\begin{cases}3,&p,q,r\text{ all odd},\\2,&\text{otherwise}.\end{cases}
\]
In particular **four mutually orthogonal exponentials never exist** under the three irrational-ratio assumptions.

**Complete extremizer classification.** In the case of three orthogonal exponentials, after translating the frequency set and permuting the roles of the three factor zero lattices, every triple is exactly
\[
\left\{0,\frac{kpA}{2},-\frac{kqB}{2}\right\},\qquad k\in2\mathbb Z+1.
\]
Every displayed triple is orthogonal. There are no other triples, apart from the specified symmetries.

**Eight-atom witness.** Take \(A=1+\sqrt2\), \(B=\sqrt2\), \(C=1\). Then \(a=\sqrt2-1\), \(b=1/\sqrt2\), \(c=1\). All eight subset sums of \(a,b,c\) are distinct, but the largest family of orthogonal exponentials has cardinality three. One such family is
\[\left\{1,e^{\pi iAx},e^{\pi iBx}\right\}.\]
This is a finite atomic example of maximal incomplete Fourier orthogonality: its three-element orthogonal family cannot be enlarged, although \(L^2(\mu)\) has dimension eight.

## Assumptions and scope

We use \(\widehat\mu(t)=\int e^{-2\pi i tx}\,d\mu(x)\) and normalized measure \(\mu\). All three parameters are strictly positive. Pairwise irrational ratios are essential. No assertion is made for pairwise commensurable factors, for biased Bernoulli factors, or for infinite convolutions. Collisions of subset sums are permitted by the general theorem; eight distinct atoms are asserted only for the explicit example. The supremum defining \(N(\mu)\) is attained by the displayed families.

## Proof

**1. Zero lattice and edge colors.** Convolution gives
\[
\widehat\mu(t)=\frac18\prod_{s\in\{a,b,c\}}(1+e^{-2\pi ist}),
\quad \mathcal Z(\widehat\mu)=\Gamma_A\cup\Gamma_B\cup\Gamma_C,
\quad \Gamma_A=\{(2m+1)A/2:m\in\mathbb Z\},
\]
with the analogous definitions of \(\Gamma_B,\Gamma_C\). Two exponentials are orthogonal exactly when their nonzero frequency difference belongs to this union. Because \(A/B,B/C,C/A\) are irrational, these three sets are disjoint. More importantly, if two distinct edges issuing from the same vertex have both differences in \(\Gamma_A\), their other endpoints differ by a nonzero integral multiple of \(A\), which belongs to none of the three half-lattices: not to \(\Gamma_A\) by parity, and not to \(\Gamma_B,\Gamma_C\) by irrationality. Therefore **the graph of any pairwise orthogonal frequency family has a proper three-edge-coloring**, the colors being the three half-lattices. Two orthogonal exponentials always exist by taking frequencies \(0,A/2\).

**2. Triangles.** In a triangle, the edges must have three different colors. Translate one frequency to zero and reorder the colors. The three frequencies are \(0,xA/2,yB/2\), with \(x,y\) odd, and their last difference is \(zC/2\), with \(z\) odd. Equivalently,
\[xA-yB-zC=0\quad\text{for odd integers }x,y,z.\]
If the rational span has dimension three this is impossible. If its dimension is two, all integer relations are integer multiples of the unique primitive relation \((p,q,r)\) (the integer-multiple assertion follows from primitivity and Bezout). Existence of odd \((x,-y,-z)\) is therefore equivalent to all \(p,q,r\) being odd, in which case the integer multiple is odd. This proves both the existence criterion and the complete triple classification, with the displayed \(k\)-parameter.

**3. Four vertices are impossible.** Suppose four frequencies were pairwise orthogonal. The proper three-edge-coloring of their complete graph is, up to vertex and color permutations, the unique three-perfect-matching coloring of \(K_4\). After translating one vertex to zero, write the other three as \(xA/2,yB/2,zC/2\), where \(x,y,z\) are odd. The three opposite edges require odd integers \(u,v,w\) such that
\[
xA-yB-uC=0,\quad xA-vB-zC=0,\quad -wA+yB-zC=0.
\]
A four-vertex configuration already contains a triangle, so the rational span has dimension two and the unique primitive relation is \((p,q,r)\) with all entries nonzero. The three displayed relations must be respectively \(k(p,q,r)\), \(\ell(p,q,r)\), and \(m(p,q,r)\) for integers \(k,\ell,m\). Comparing the \(A\)-coefficients of the first two equations gives \(k=\ell\). Comparing the \(B\)-coefficients of the first and third gives \(m=-k\). Comparing the \(C\)-coefficients of the second and third gives \(m=\ell\), so \(k=0\), contradicting the nonzero odd coefficient \(x=kp\). Thus no four frequencies can be pairwise orthogonal. If five or more existed, four would exist, so the bound is global.

**4. Eight distinct sites.** For the explicit parameters, \(a=-1+\sqrt2\), \(b=\sqrt2/2\), \(c=1\). A collision between subset sums would give \(\epsilon a+\eta b+\zeta c=0\) with \(\epsilon,\eta,\zeta\in\{-1,0,1\}\), hence \(-\epsilon+\zeta=0\) and \(\epsilon+\eta/2=0\) by linear independence of \(1\) and \(\sqrt2\) over \(\mathbb Q\). Thus \(\eta=-2\epsilon\), forcing \(\epsilon=\eta=\zeta=0\). The eight sites are distinct. The reciprocal relation \(A-B-C=0\) has primitive coefficients \((1,-1,-1)\), all odd; hence the theorem gives \(N(\mu)=3\) and the explicit triple.

## Verification

The proof uses an exact Fourier factorization and integer linear relations; neither numerical experiments nor a finite search certify the infinite assertions. The accompanying standard-library checker verifies the eight distinct support points in \(\mathbb Q(\sqrt2)\), the exact reciprocal identity, and the three half-integral annihilation identities yielding orthogonality. Run `python3 verify.py`. The four-vertex impossibility rests solely on the analytic graph argument above.

## Relationship to prior work

Zhou's 2026 work on convolution/product spectrality gives spectral-basis characterizations when the Fourier-zero set together with zero is an additive subgroup, and different product conditions. That subgroup condition fails here: \(A/2\) is a zero but \(A/2+A/2=A\) is not a zero under pairwise irrationality. The current theorem addresses the exact maximal **partial orthogonality cardinality**, not the existence of a complete spectral basis under a subgroup hypothesis.

Kolountzakis, Lev and Matolcsi investigate maximal versus complete exponential systems for cube measures; their measure/domain and dimensional conditions differ. Baker et al. investigate the Fourier integrability and decay of *infinite random* Bernoulli convolutions, whereas the present theorem treats the arithmetic of zeros of a finite three-factor convolution. The exact relation to general existing finite-atomic Fourier orthogonality classifications remains a priority risk.

## Limitations

The classification is restricted to three equally weighted Bernoulli factors with pairwise irrational length ratios. It does not cover rationally commensurable factors, arbitrarily many factors, biased masses, perturbation stability, or spectral bases in other measure families. Publication priority is provisional; equivalent descriptions in finite Hadamard-matrix or finite-atomic spectral-measure theory have not been excluded. The comparison with Zhou's 2026 manuscript used its accessible introductory statements and a detailed indexed synopsis; full-body retrieval could not be completed at review time. No independent audit has been conducted.

## References

- Ting Zhou, *Spectrality of convolution and product measures: a block decomposition approach*, arXiv:2610.33987v1, publicly submitted October 25, 2026. https://arxiv.org/abs/2610.33987
- Mihail N. Kolountzakis, Nir Lev and Máté Matolcsi, *Maximality and completeness of orthogonal exponentials on the cube*, arXiv:2410.12387. https://arxiv.org/abs/2410.12387
- Simon Baker, Henna Koivusalo, Sascha Troscheit and Xintian Zhang, *On the Fourier transform of random Bernoulli convolutions*, Journal of the London Mathematical Society 113 (2026), e70515. https://doi.org/10.1112/jlms.70515
- Palle E. T. Jorgensen, Keri A. Kornelson and Karen L. Shuman, *Families of Spectral Sets for Bernoulli Convolutions*, Journal of Fourier Analysis and Applications 17 (2011), 431–456. https://doi.org/10.1007/s00041-010-9158-x
