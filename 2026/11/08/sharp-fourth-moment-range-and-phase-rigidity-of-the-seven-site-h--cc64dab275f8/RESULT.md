# Sharp fourth-moment range and phase rigidity of the seven-site hexagonal Fourier aperture

## Finding

Let \(\Lambda=\{(0,0),\pm(1,0),\pm(0,1),\pm(1,1)\}\subset\mathbb Z^2\). For a coefficient family \(c=(c_\lambda)_{\lambda\in\Lambda}\) satisfying \(|c_\lambda|=1\), put
\[
P_c(z,w)=\sum_{\lambda\in\Lambda}c_\lambda z^{\lambda_1}w^{\lambda_2},\qquad
M(c)=\int_{\mathbb T^2}|P_c(z,w)|^4\,dm(z,w),
\]
where \(m\) is normalized Haar probability measure. Then
\[
\boxed{\{M(c):|c_\lambda|=1\}=[63,175].}
\]

There are exactly **three minimum orbits** and **one maximum orbit** under the transformations \(c_{(j,k)}\mapsto\eta\alpha^j\beta^k c_{(j,k)}\), with \(\eta,\alpha,\beta\in\mathbb T\). In the unique gauge \(c_{(0,0)}=c_{(1,0)}=c_{(0,1)}=1\), order the other coefficients as
\[
(U,V,W,T)=(c_{(-1,0)},c_{(0,-1)},c_{(1,1)},c_{(-1,-1)}).
\]
The complete set of **minimum** tuples is
\[
\boxed{(-1,-1,1,1),\quad(-1,1,-1,1),\quad(1,-1,-1,1),}
\]
and the **only maximum** tuple is \((1,1,1,1)\). For coefficients restricted to the \(q\)-th roots of unity, \(q\ge2\), the sharp unrestricted minimum \(63\) is attained if and only if \(q\) is even, in which case exactly \(3q^3\) raw arrays attain it. These statements also hold for discrete Fourier averages on \(\mathbb Z_m\times\mathbb Z_n\) whenever \(m,n\ge5\).

## Assumptions and scope

The support is precisely the **center and six nearest neighbors** of a triangular/hexagonal integer lattice under the displayed coordinates; all seven coefficients have magnitude one. The fourth-power norm uses Haar **probability** measure. The finite-grid result averages the same Laurent polynomial over all pairs of \(m\)-th and \(n\)-th roots of unity with \(m,n\ge5\). The stated orbits quotient only common phase and two coordinate character modulations; reflections or permutations are not additionally identified. The precise phase-alphabet statement concerns attainability of the unrestricted bound, not the exact minimum for odd \(q\).

## Proof

**Autocorrelation identity and gauge.** Put \(C(d)=\sum_{\lambda-\mu=d}c_\lambda\overline{c_\mu}\), summing ordered pairs from \(\Lambda\). Fourier orthogonality gives
\[
M(c)=\sum_{d\in\Lambda-\Lambda}|C(d)|^2.
\]
The zero shift contributes \(49\). There are nine unordered nonzero shift-pairs; precisely three representatives have one contributing ordered pair, three have two pairs, and three have four pairs. Conjugate shifts have equal squared modulus. Multiplication by \(\eta\alpha^j\beta^k\) preserves all these moduli and uniquely normalizes the three designated coefficients to one.

**Exact autocorrelation reduction.** For the four remaining unimodular coefficients write
\[
x=\overline U,\qquad y=\overline V,\qquad z=\overline{WT},\qquad s=x+y+z,
\qquad e_2=xy+xz+yz,\quad R=|s|^2.
\]
The sum of squared magnitudes of the three two-pair autocorrelations is exactly \(3+R\). Up to permutation of the three four-pair shifts, their autocorrelations are of the form \(A_j+W B_j\), where
\[
A=(1+x,1+y,x+y),\qquad
B=(1+z\overline y,1+z\overline x,1+z).
\]
Set \(L=\sum_{j=1}^3|A_j+WB_j|^2\). The following exact identities follow by expansion, using \(|x|=|y|=|z|=1\):
\[
\sum_j(|A_j|^2+|B_j|^2)=R+9+2\operatorname{Re}s,
\qquad
\sum_j\overline{A_j}B_j=\frac{2(s+e_2)}{xy}.
\]
Consequently
\[
M(c)=61+2(R+L),\qquad
L\ge R+9+2\operatorname{Re}s-4|s+e_2|.
\]
Since \(e_2=xyz\overline s\), one has \(|s+e_2|\le2|s|\) and \(\operatorname{Re}s\ge-|s|\). With \(t=|s|\in[0,3]\),
\[
R+L\ge2t^2+9-10t.
\]
If \(0\le t\le1\), the right-hand side is at least \(1\), since \(2t^2+8-10t=2(t-1)(t-4)\ge0\). If \(t\ge1\), the trivial inequality \(R+L\ge R=t^2\ge1\) applies. Therefore \(M(c)\ge63\) for every unimodular coefficient family.

**All minimum cases.** At equality \(R+L=1\), the preceding two regimes force \(t=1\) and \(L=0\). The chain of inequalities for \(t=1\) forces \(s=-1\) and \(|s+e_2|=2\); as \(e_2=xyz\overline s\), it follows that \(xyz=1\) and \(e_2=-1\). Hence \(x,y,z\) are exactly the roots of
\[
X^3-sX^2+e_2X-xyz=X^3+X^2-X-1=(X-1)(X+1)^2.
\]
Thus \(\{x,y,z\}=\{1,-1,-1\}\). Substituting into \(A+WB=0\), the necessary condition \(L=0\), yields precisely the three displayed normalized tuples for \((U,V,W,T)\), and direct substitution confirms that each gives equality. No other cases exist.

**Sharp maximum, rigidity, and full interval.** For every shift \(d\), the triangle inequality bounds \(|C(d)|\) by its number of contributing pairs. Therefore
\[
M(c)\le49+2(3\cdot1^2+3\cdot2^2+3\cdot4^2)=175.
\]
The all-one coefficients attain \(175\). If equality holds, the four-term autocorrelation at shift \((1,1)\), equal to \(W+\overline U+\overline V+\overline T\), must have modulus four. Thus \(W=\overline U=\overline V=\overline T\). The shift \((1,0)\) then has correlation \(2+2W\), whose modulus is four only for \(W=1\). This forces all four normalized coefficients to be one. Finally the coefficient torus \(\mathbb T^7\) is connected and the moment is continuous; its image is the entire real interval between the attained sharp endpoints.

**Phase alphabets and finite tori.** The three normalized minimizers require the value \(-1\), and are the only continuous-phase minimizers. Therefore \(q\)-th-root coefficients attain \(63\) precisely for even \(q\); undoing the gauge gives exactly \(q^3\) arrays per normalized minimum, or \(3q^3\) in total. For \(m,n\ge5\), each difference in \(\Lambda-\Lambda\subset[-2,2]^2\) has a distinct image modulo \((m,n)\). Character orthogonality on the finite grid therefore reproduces the same autocorrelation identity without aliasing, preserving all bounds and equality classifications.

## Verification

The accompanying dependency-free `checker.py` enumerates all seven-site support differences and their multiplicities, constructs exact formal Laurent-polynomial autocorrelations, and verifies each nonstandard symbolic identity used above. It separately evaluates all \(2^4\) normalized binary patterns and all normalized \(q\)-phase patterns for \(q\in\{2,3,4,5,6\}\) as finite consistency tests. A successful run emits `HEXAGON_SEVEN_L4_PASS`. The infinite continuum theorem, phase rigidity, and full interval are justified by the analytical arguments above, not finite testing.

## Relationship to prior work

Ding, Noshad and Tarokh's *Complementary Lattice Arrays for Coded Aperture Imaging* studies **this same seven-point hexagonal support** (Section 2D). Its central result for that support concerns nonexistence of a complementary **pair** and constructions of **three or four jointly complementary arrays**. Neither the nonexistence of a complementary pair nor a construction involving multiple arrays entails the sharp **single-array** fourth-moment minimum \(63\) or the three complete continuous-phase equality classes proved here. This same-support comparison is particularly relevant and limits any broad claim of novelty for the object itself.

Petersen, Paganin and Svalbe (2021) investigate scalable and multidimensional Huffman-type sequences and autocorrelation concentration, generally with nonuniform or signed weights and different designs; the cited construction does not supply this exact unimodular seven-site classification. Du and Jiang (2022) and Gu and collaborators (2021) construct complementary pairs or larger sets; their cancellation objectives concern *sums* of correlations rather than minimization of one seven-site array. A published result on the six-frequency degree-two triangular aperture determines its fourth-moment interval \([48,102]\), but has a different support and cardinality. A published nine-mode square-aperture result classifies finite-alphabet fourth moments when all nine modes are present; its estimates do not imply those for this seven-mode nonrectangular subaperture.

## Limitations

The conclusion applies to fixed unimodular magnitudes on this seven-site support, fourth moments, and specified nonaliasing finite grids. It does **not** assert an unrestricted coefficient-\(\ell^2\) to \(L^4\) operator norm, a sharp bound for larger supports, phase-restricted minima for odd alphabet sizes, or optical performance beyond this autocorrelation measure. A possibly unindexed equivalent calculation in polyphase array or coded-aperture literature remains a bibliographic risk. Independent validation and independent bibliographic review have not been performed.

## References

- J. Ding, M. Noshad and V. Tarokh, *Complementary Lattice Arrays for Coded Aperture Imaging*, arXiv:1506.02160v1 (2015-06-06); *J. Opt. Soc. Am. A* 33 (2016), 863–881, DOI:10.1364/JOSAA.33.000863. https://arxiv.org/abs/1506.02160.
- T. C. Petersen, D. M. Paganin and I. D. Svalbe, *Extending the Known Families of Scalable Huffman Sequences*, arXiv:2106.02269v1 (first public 2021-06-04), https://arxiv.org/abs/2106.02269.
- C. Du and Y. Jiang, *Constructions of Polyphase Golay Complementary Arrays*, arXiv:2204.09372v1 (first public 2022-04-20), https://arxiv.org/abs/2204.09372.
- Z. Gu et al., *New Constructions of Golay Complementary Pair/Array with Large Zero Correlation Zone*, arXiv:2108.05657v1 (first public 2021-08-12), https://arxiv.org/abs/2108.05657.
- *Sharp Fourth-Moment Phase Rigidity for the Six-Point Triangular Fourier Aperture*, published 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-phase-rigidity-for-the-six-point-triangular--bea9cf2ed885.
- *Sharp Phase-Alphabet Fourth Moments for the Nine-Mode Square Fourier Aperture*, published 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-phase-alphabet-fourth-moments-for-the-nine-mode-square-fou--f31c28437f0d.
