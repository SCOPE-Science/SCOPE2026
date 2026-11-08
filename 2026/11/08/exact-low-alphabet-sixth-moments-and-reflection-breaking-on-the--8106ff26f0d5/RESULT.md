# Exact low-alphabet sixth moments and reflection breaking on the triangular Fourier aperture

## Finding

Let
\[
\Lambda=\{(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)\}
\]
be the complete degree-two triangular frequency aperture. For \(q\in\{2,3,4,5,6\}\), let \(\mu_q\) be the complex \(q\)-th roots of unity. For all \(c_{ab}\in\mu_q\), put
\[
P_c(z,w)=\sum_{(a,b)\in\Lambda}c_{ab}z^aw^b,
\qquad M_6(c)=\int_{\mathbb T^2}|P_c(z,w)|^6\,dm(z,w),
\]
where \(dm\) is Haar probability measure. **The minimum, with all its equality arrays, is exactly as follows:**

| \(q\) | \(\min M_6\) | Normalized minimizing exponent triples \((a,b,c)\) | Number of all minimizing arrays |
|:--:|:--:|:--|--:|
| 2 | \(582\) | \((0,1,0)\) | 8 |
| 3 | \(456\) | \((1,2,1),(2,1,2)\) | 54 |
| 4 | \(582\) | \((0,2,0),(2,1,2),(2,3,2)\) | 192 |
| 5 | \(744-102\sqrt5\) | \((1,3,2),(2,3,1),(2,4,2),(3,1,3),(3,2,4),(4,2,3)\) | 750 |
| 6 | \(456\) | \((2,4,2),(4,2,4)\) | 432 |

Here an exponent triple means the normalized polynomial
\[
1+z+w+\zeta_q^a z^2+\zeta_q^bzw+\zeta_q^cw^2,
\qquad \zeta_q=e^{2\pi i/q}.
\]
All equality arrays, with no omitted arrays, are obtained from precisely these normalized triples by multiplying the coefficient at \((i,j)\) by \(\lambda\alpha^i\beta^j\), where \(\lambda,\alpha,\beta\in\mu_q\). Consequently each normalized triple contributes exactly \(q^3\) arrays. Reflection \((z,w)\mapsto(w,z)\) interchanges the first and third exponents; at five phases four of the six normalized minimizers break this symmetry (two exchanged pairs), whereas all minima for \(q=2,3,4,6\) are reflection-fixed.

The minima are **nonmonotone in the phase alphabet size**: the quaternary minimum equals the binary minimum, whereas ternary and hexaphase coefficients attain \(456\) and pentaphase coefficients attain the algebraic value \(744-102\sqrt5>456\). None of these five alphabets reaches the unrestricted continuous-phase optimum: an explicit unimodular rational-coordinate witness has
\[
M_6=\frac{89848422}{198025}<456.
\]
No exact continuous-phase optimum is claimed. The entire finite-alphabet classification also holds for normalized Fourier averages over \(\mathbb Z_m\times\mathbb Z_n\) whenever \(m,n\ge7\).

## Assumptions and scope

Every one of the six coefficients has modulus exactly one and belongs to the indicated **exact** root-of-unity alphabet. The polynomial is evaluated on the full two-torus; no terms are omitted. \(M_6\) is an integrated sixth power, not a sixth-order moment of individual autocorrelation sidelobes or a peak sidelobe objective. Classification uses common phase and two independent frequency-character modulations only; coordinate reflection is *not* quotiented out. For finite-group sampling both periods are at least seven; this avoids all aliasing among the frequencies of \(P_c^3\).

## Proof

**1. Complete normalization.** The moment is unchanged under \(c_{ij}\mapsto\lambda\alpha^i\beta^j c_{ij}\). For any \(q\)-phase coefficient array, there is exactly one such choice that sends \(c_{00},c_{10},c_{01}\) to \(1,1,1\); the three multipliers remain in \(\mu_q\). Thus it suffices to minimize over all \(q^3\) triples \((u,v,t)\in\mu_q^3\) in
\[
P_{u,v,t}(z,w)=1+z+w+uz^2+vzw+tw^2.
\]
Restoring the three independent multipliers gives \(q^3\) distinct arrays for each normalized minimizer.

**2. Exact Laurent identity.** Fourier orthogonality yields
\[
M_6(u,v,t)=\sum_{r+s\le6}\left|[z^rw^s]P_{u,v,t}^3\right|^2.
\]
Expand this finite sum and use \(\overline u=u^{-1}\), \(\overline v=v^{-1}\), \(\overline t=t^{-1}\). Collecting the constant and ten conjugate pairs gives the exact identity
\[
\begin{aligned}
M_6(u,v,t)=996+2\operatorname{Re}\big(&78u+78t+144v+9u\overline t+36ut\overline v\\
&+144(u+t)\overline v+78ut\overline v^{2}+9(u+t)\overline v^{2}\big).
\end{aligned}
\tag{1}
\]
The completely independent formal coefficient-generation routine in `checker.py` reconstructs all 21 Laurent monomials directly from the six frequencies and checks them against (1) coefficient by coefficient, over integers.

**3. Finite, exact algebraic enumeration.** Let the ordered coefficient-weight and exponent-vector pairs be
\[
\begin{split}
\mathcal T=\{&(78,(1,0,0)),(78,(0,0,1)),(144,(0,1,0)),(9,(1,0,-1)),\\
&(36,(1,-1,1)),(144,(1,-1,0)),(144,(0,-1,1)),\\
&(78,(1,-2,1)),(9,(1,-2,0)),(9,(0,-2,1))\}.
\end{split}
\]
For each integer triple \(e=(a,b,c)\in\{0,\dots,q-1\}^3\), (1) becomes
\[
4M_6(e)=3984+2\sum_{(h,r)\in\mathcal T}h\,C_q(r\cdot e),
\qquad C_q(k)=4\cos(2\pi k/q).
\tag{2}
\]
The full exact cosine tables (indexed by residues \(k=0,\ldots,q-1\)) are
\[
\begin{array}{c|l}
q& (C_q(k))_k\\\hline
2&(4,-4)\\
3&(4,-2,-2)\\
4&(4,0,-4,0)\\
5&(4,-1+\sqrt5,-1-\sqrt5,-1-\sqrt5,-1+\sqrt5)\\
6&(4,2,-2,-4,-2,2).
\end{array}
\]
Therefore (2) requires *only integer arithmetic*, and, for \(q=5\), integer pairs \((U,V)\) representing \(U+V\sqrt5\). Comparisons of such pairs are exact: if the signs of \(U\) and \(V\) differ, compare the integers \(U^2\) and \(5V^2\), using the appropriate sign. Because \(\sqrt5\) is irrational, no equality is lost. Exhausting all \(8+27+64+125+216=440\) triples gives exactly the five minima and the complete minimizing exponent sets in the finding table. These are finite exhaustive calculations, not random sampling or numerical optimization. The checker implements this entire enumeration, including all ties, and independently evaluates the formal \(P^3\) coefficient norm in \(\mathbb Z[\zeta_q]\) for every one of the 440 triples.

**4. A strict continuous-alphabet gap.** Take
\[
u=t=\frac{-3+4i}{5},\qquad v=\frac{-39-80i}{89}.
\]
These have unit modulus. Substitution in the coefficient-convolution formula gives exactly
\[
M_6(u,v,t)=\frac{89848422}{198025}
=456-\frac{450978}{198025}<456.
\]
Thus the unrestricted infimum is strictly below the best among the five enumerated phase alphabets, without any claim about its exact value or extremizers.

**5. No-aliasing discrete sampling.** The monomials of \(P^3\) have integer exponent pairs \((r,s)\) with \(r,s\ge0\) and \(r+s\le6\). For \(m,n\ge7\), distinct such pairs remain distinct modulo \((m,n)\). The sampled orthogonality relation therefore gives exactly the same coefficient-norm sum as in step 2 and every conclusion above carries over unchanged.

## Verification

Run `python3 checker.py` in the directory of this file. The standard-library-only program (a) reconstructs the formal \(P^3\) Fourier coefficients, (b) checks all 21 terms of (1) exactly, (c) enumerates precisely the 440 distinct normalized phase triples, (d) compares each exact moment independently using cyclotomic-integer reduction, and (e) verifies the minimum, equality triples, and raw array counts at every alphabet size. A successful run ends with `TRIANGULAR_SIXTH_EXACT_PASS configurations=440 formal_terms=21`. The continuous witness is a separate exact rational evaluation, not inferred from this finite census.

## Relationship to prior work

Pai and Chen (2021, arXiv:2102.04043v1) study constructions of complementary **sets** of two-dimensional polyphase arrays and the cancellation of sums of aperiodic autocorrelations. Zhang, Fan and Mesnager (2021, arXiv:2107.11599v1) construct **pairs** with large zero-correlation zones, and their Theorems 1–2 and examples concern paired arrays and correlation-zone widths. Neither directly determines the sixth Fourier moment for a *single* six-site triangular array.

*Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture* (public mathematical result, October 2026) determines the fourth moment for the **identical** support, including its cubic-root minimizers. Its identity is quadratic in aperiodic autocorrelations and does not determine the cubic-convolution energy in (1). For example, the fourth-moment lower bound \(48\) and \(\int|P|^2=6\) yield only \(\int|P|^6\ge48^2/6=384\) by interpolation, not the sharp ternary value \(456\), the pentaphase algebraic minimum or the symmetry-breaking phase census. Other published sparse Fourier sixth-moment results inspected through their indexed statements concern different support geometry, coefficient-norm normalization, or finite fields. Thus they do not imply the five-alphabet classification by a support-preserving change of variables. Bibliographic exhaustiveness is not asserted.

## Limitations

The complete classification covers only phase-alphabet orders two through six and the degree-two triangular aperture. It does not determine other alphabet orders, the exact continuously unimodular minimum, optimizing coefficients of arbitrary nonunit modulus, or grids whose dimensions are less than seven. A prior specialized polyphase-array table containing the identical sixth-order calculation remains possible; exact computational verification alone is not a guarantee of historical novelty. The result has not undergone independent mathematical or bibliographic audit.

## References

- C.-Y. Pai and C.-Y. Chen, *Two-Dimensional Golay Complementary Array Sets from Generalized Boolean Functions*, arXiv:2102.04043v1, first public 2021-02-08, https://arxiv.org/abs/2102.04043.
- H. Zhang, C. Fan and S. Mesnager, *New constructions of q-Ary 2-D Z-Complementary Array Pairs*, arXiv:2107.11599v1, first public 2021-07-24, https://arxiv.org/abs/2107.11599.
- *Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture*, publicly available mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-phase-rigidity-for-the-six-point-triangular--bea9cf2ed885.
- D. J. Katz and M. E. Ramirez, *Limiting Moments of Autocorrelation Demerit Factors of Binary Sequences*, arXiv:2307.14566v1, first public 2023-07-27, https://arxiv.org/abs/2307.14566.
