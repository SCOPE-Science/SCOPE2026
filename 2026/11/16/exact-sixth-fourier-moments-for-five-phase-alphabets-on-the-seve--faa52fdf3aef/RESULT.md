# Exact sixth Fourier moments for five phase alphabets on the seven-site hexagonal aperture

## Finding

Consider the seven-site centered hexagonal aperture
\[
\Lambda=\{(0,0),(1,0),(0,1),(-1,0),(0,-1),(1,-1),(-1,1)\}\subset\mathbb Z^2.
\]
For any integer \(q\in\{2,3,4,5,6\}\), let \(\mu_q\) be the group of \(q\)-th roots of unity. For coefficients \(a_\lambda\in\mu_q\), define
\[
P_a(z,w)=\sum_{\lambda\in\Lambda}a_\lambda z^{\lambda_1}w^{\lambda_2},\qquad M_6(a)=\int_{\mathbb T^2}|P_a|^6\,dm,
\]
where \(m\) is normalized Haar probability measure. The sharp minima, the next larger *attainable* values, and all optimizer counts are:

| Alphabet \(q\) | Sharp \(M_6\) minimum | Next value | Gauge-normalized minimizers | All minimizers |
|---|---:|---:|---:|---:|
| 2 | \(649\) | \(1081\) | 3 | 24 |
| 3 | \(913\) | \(1084\) | 6 | 162 |
| 4 | \(649\) | \(841\) | 3 | 192 |
| 5 | \(1936-519\sqrt5\) | \(1876-489\sqrt5\) | 6 | 750 |
| 6 | \(649\) | \(757\) | 3 | 648 |

In each alphabet the sharp maximum is \(5881\), attained exactly by the \(q^3\) coefficient arrays obtained by applying scalar/coordinate character modulations to the all-one array. The full list of normalized minimizers, in the four ordered remaining coefficients at \((-1,0),(0,-1),(1,-1),(-1,1)\), is as follows: for \(q=2\), exponent tuples \((0,1,0,1),(1,0,1,0),(1,1,1,1)\); for \(q=3\), \((0,0,1,1),(0,0,2,2),(0,1,2,1),(0,2,1,2),(1,0,1,2),(2,0,2,1)\); for \(q=4\), \((0,2,0,2),(2,0,2,0),(2,2,2,2)\); for \(q=5\), \((0,2,0,3),(0,3,0,2),(2,0,3,0),(2,3,3,2),(3,0,2,0),(3,2,2,3)\); and for \(q=6\), \((0,3,0,3),(3,0,3,0),(3,3,3,3)\). An exponent \(r\) means the coefficient \(\exp(2\pi i r/q)\). These are complete classifications, not representative examples.

The same minima, gaps, and optimizer counts hold for normalized discrete Fourier averages on \(\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\) for all \(m,n\ge7\). In particular the five-phase minimum lies strictly above \(649\), but below both the three-phase and its own next attainable value; its gap is exactly \(30(\sqrt5-2)\).

## Assumptions and scope

All seven coefficients have magnitude exactly one and belong to the specified finite phase alphabet. The Fourier integral is an *averaged* sixth power, without division by \(7^3\). The first three aperture coefficients, corresponding respectively to \((0,0),(1,0),(0,1)\), can be uniquely made equal to one by multiplication with \(\eta\alpha^x\beta^y\), with \(\eta,\alpha,\beta\in\mu_q\). This preserves every even moment and maps the finite alphabet to itself. Therefore the four remaining coefficients give exactly \(q^4\) gauge-normalized cases, and every such case represents exactly \(q^3\) raw arrays. The support is a genuine seven-point hexagon, not a six-vertex hexagon with its center deleted. No conclusion about the *unrestricted continuous-phase* sixth-moment minimum is asserted.

## Proof

**Fourier orthogonality and two exact coefficient constructions.** Let \(e_0,\ldots,e_6\) denote the seven ordered sites listed above, and set \(a_0=a_1=a_2=1\). For any lattice sum \(v\in\mathbb Z^2\), let
\[
F_a(v)=\sum_{\substack{(i,j,k)\in\{0,\ldots,6\}^3\\e_i+e_j+e_k=v}}a_i a_j a_k.
\]
Fourier orthogonality proves the exact identity
\[
M_6(a)=\sum_{v\in\mathbb Z^2}|F_a(v)|^2. \tag{1}
\]
There are exactly 37 distinct lattice sums of ordered triples, and precisely \(7^3=343\) ordered summands. Equation (1) is a finite integer-algebra identity, and avoids any numerical quadrature.

For an independent formula, collect unordered triples \(I\) of indices with multinomial weight \(m_I=3!/\prod_j n_j(I)!\). For each ordered pair of unordered triples \(I,J\) contributing to the same lattice sum, form the four-component exponent difference \(d_r=n_{r+2}(I)-n_{r+2}(J)\), \(r=1,\ldots,4\), and add the weight \(m_I m_J\) to a Laurent coefficient \(c_d\). Then, for \(\xi=\exp(2\pi i/q)\) and exponent tuple \(h=(h_1,\ldots,h_4)\),
\[
M_6(h)=\sum_{d\in\mathbb Z^4}c_d\xi^{d\cdot h}. \tag{2}
\]
This second construction uses only unordered multinomial triple counts, whereas (1) uses directly the ordered triple fibers.

**Exhaustive finite-alphabet proof.** The attached dependency-free `checker.py` constructs (1) and (2) separately. It evaluates both methods for every one of the \(\sum_{q=2}^{6}q^4=2274\) normalized phase assignments; it asserts exact agreement in the cyclotomic quotient \(\mathbb Z[X]/(\Phi_q(X))\). The cyclotomic polynomials used are \(X+1\), \(X^2+X+1\), \(X^2+1\), \(X^4+X^3+X^2+X+1\), and \(X^2-X+1\). Thus all comparisons are exact, without floating-point thresholds. For \(q\ne5\), the evaluated real moments are integers; for \(q=5\), their exact representation is \(A+B(\sqrt5-1)/2\) for integers \(A,B\). The checker compares these algebraic numbers by signs and integer squares. Its full enumeration yields precisely the five sharp minima, second-value gaps, maximizers and the explicit sets of minimizing exponent tuples in the Finding. The number of cases is exhausted by the finite product sets, so this is a complete finite certificate, not a sample or a probabilistic search.

**Maximizers.** For each triple-sum fiber, the triangle inequality gives \(|F_a(v)|\) at most the number of ordered triples in that fiber. Equality across every fiber holds for the all-one coefficients, giving \(M_6=5881\). The exhaustive cyclotomic computation separately proves that the normalized all-one tuple is the unique maximizer within each of the five finite alphabets. The orbit count therefore is \(q^3\). This also provides an independent upper bound for the numerical census.

**Finite grid transfer.** Every coordinate of a triple sum is in \([-3,3]\); for integers \(m,n\ge7\), the reduction map from this integer box to \(\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\) is injective. Discrete Fourier orthogonality therefore reproduces (1) exactly, including the minimizing tuples and their multiplicities. No such claim is made for smaller grids with potential aliasing.

## Verification

Run `python3 checker.py` from the same directory. It prints `HEXAGON_SEVEN_L6_ALPHABETS_PASS` only after checking all 2,274 normalized inputs with *both* independent moment constructions, the entire sharp-minimum and next-value table, exact five-phase minimizer tuples, the normalized-maximizer uniqueness, and the 37-fiber / 343-summand / 5,881-all-one checks. Arithmetic is in exact quotient rings and sign comparisons; no third-party package is needed. The proof of finite-grid transfer is analytic and is not inferred from sample grids. The computational exhaustion is finite but exhaustive for the five stated alphabets. No infinite phase-alphabet or continuous-phase optimality conclusion is drawn.

## Relationship to prior work

Ding, Noshad and Tarokh study precisely the centered seven-site hexagonal support in *Complementary Lattice Arrays for Coded Aperture Imaging* (2015/2016). Their seven-site result concerns nonexistence of two-array complementarity and constructions of sets of three and four arrays, and does not imply the sharp single-array sixth-moment minimizers, finite-alphabet gap or equality counts given here. Du and Jiang (2022) construct polyphase Golay complementary *sets*; this similarly involves summed correlation cancellation across arrays, rather than the sixth moment of a single seven-site array. Petersen, Paganin and Svalbe (2021) study scalable multidimensional Huffman-type constructions with varying magnitudes and different supports; they do not provide this exact classification.

An existing exact *fourth*-moment seven-site hexagon theorem identifies the continuous-phase fourth-moment range and its parity-dependent alphabet attainment, but does not imply the *sixth*-moment values or their five-alphabet optimizer counts. A published *sixth*-moment theorem for the six **outer** vertices of this hexagon has a different support and therefore does not imply this centered case. A further low-alphabet sixth-moment classification for the six-frequency *triangular* aperture has distinct additive triple relations. All three constitute close comparison points, rather than matching the present statement.

## Limitations

The theorem is deliberately restricted to the five explicitly listed finite phase alphabets and this exact seven-site aperture; it does not assert the continuous-phase minimum, stability against noise, or uniform behavior for other phase counts, magnitudes, supports or small aliasing grids. The result is an exact finite classification supported by an executable enumeration and independent algebraic construction. Unindexed specialist phased-array design tables may conceivably contain an equivalent result; independent historical-priority and mathematical validation have not been performed.

## References

- J. Ding, M. Noshad and V. Tarokh, *Complementary Lattice Arrays for Coded Aperture Imaging*, arXiv:1506.02160v1 (2015-06-06), https://arxiv.org/abs/1506.02160.
- C. Du and Y. Jiang, *Constructions of Polyphase Golay Complementary Arrays*, arXiv:2204.09372v1 (2022-04-20), https://arxiv.org/abs/2204.09372.
- T. C. Petersen, D. M. Paganin and I. D. Svalbe, *Extending the Known Families of Scalable Huffman Sequences*, arXiv:2106.02269v1 (2021-06-04), https://arxiv.org/abs/2106.02269.
- *Sharp fourth-moment range and phase rigidity of the seven-site hexagonal Fourier aperture*, published research (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-fourth-moment-range-and-phase-rigidity-of-the-seven-site-h--cc64dab275f8.
- *Sharp sixth-moment range and sixth-root phase rigidity on the \(A_2\) Fourier hexagon*, published research (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-sixth-moment-range-and-sixth-root-phase-rigidity-on-the-a--1a27a9f4b8a6.
- *Exact low-alphabet sixth moments and reflection breaking on the triangular Fourier aperture*, published research (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-low-alphabet-sixth-moments-and-reflection-breaking-on-the--8106ff26f0d5.
