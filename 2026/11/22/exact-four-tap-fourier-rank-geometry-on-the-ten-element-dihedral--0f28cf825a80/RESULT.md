# Exact four-tap Fourier-rank geometry on the ten-element dihedral group

## Finding
Let \(G=D_{10}=\langle r,s\mid r^5=s^2=e,\ srs=r^{-1}\rangle\) (order ten), and let \(f:G\to\mathbb C\) have exactly four nonzero coefficients, with no restrictions on their complex values. Left convolution by \(f\) is the linear map
\[
T_fh(x)=\sum_{g\in G}f(g)h(g^{-1}x),\qquad \sigma(f)=\operatorname{rank}_{\mathbb C}T_f.
\]
This rank equals the multiplicity-weighted nonabelian Fourier support \(\sum_{\rho\in\widehat G}(\dim\rho)\operatorname{rank}\widehat f(\rho)\). Write \(H=\langle r\rangle\). For a support \(S\) with two points in each of \(H\) and \(Hs\), take the two exponent differences \(d,e\in\mathbb F_5^*/\{\pm1\}\), one from each coset. Call the pairs **parallel** when \(d=\pm e\pmod5\) and **skew** otherwise.

For **every fixed support** in each class, the complete attainable set \(\{\sigma(f):\operatorname{supp}f=S\}\) is:

| Four-point support type | Number of supports | Complete attainable convolution ranks |
|---|---:|---|
| Four points in a single coset | 10 | \(\{4,6,8,10\}\) |
| Three points in one coset, one in the other | 100 | \(\{6,7,8,9,10\}\) |
| Two points in each coset, parallel differences | 50 | \(\{4,5,8,9,10\}\) |
| Two points in each coset, skew differences | 50 | \(\{6,7,8,9,10\}\) |

These four classes exhaust all \(\binom{10}{4}=210\) supports. In particular, four-tap support geometry distinguishes a rank-five possibility exclusive to parallel two-pair supports, whereas a rank-seven possibility appears for the skew two-pair class but not the parallel class. The theorem concerns *attainability as the four complex coefficients vary*, not a distribution under a probability measure on coefficients.

## Assumptions and scope
The group has the stated presentation and cardinality ten. Both cosets contain five elements. Every stated rank is over \(\mathbb C\), with **exactly** four nonzero tap coefficients; no tap may be zero. We use the unnormalized Fourier transform and group-counting convolution. Translation, group automorphism, and reflection of the group coordinates preserve the convolution rank. The Fourier-rank interpretation does not require any Hermitian, real, positive, or unit-modulus condition on the coefficients. Distinct points within either coset are understood modulo five.

## Proof
**1. Fourier blocks.** Put \(\zeta=e^{2\pi i/5}\), and for \(f\) define the Laurent polynomials
\[
A(z)=\sum_{t=0}^{4}f(r^t)z^t,\qquad B(z)=\sum_{t=0}^{4}f(r^ts)z^t.
\]
The two one-dimensional representations contribute the scalars \(A(1)+B(1)\) and \(A(1)-B(1)\). The other two irreducible representations have dimension two and Fourier blocks, with a consistent convention,
\[
M_j=\begin{pmatrix}A(\zeta^j)&B(\zeta^j)\\B(\zeta^{-j})&A(\zeta^{-j})\end{pmatrix},\qquad j=1,2.
\]
Each two-dimensional block occurs twice in the regular representation. Hence, if \(\epsilon_+\) and \(\epsilon_-\) are indicators that the two scalars vanish, and \(\delta_j\) is the indicator of \(\det M_j=0\), then
\[
\sigma(f)=10-\epsilon_+-\epsilon_--2\delta_1-2\delta_2,\tag{1}
\]
provided each singular \(M_j\) has rank one. For any mixed-coset four-tap support this is indeed so: with a single tap in the reflected coset, both off-diagonal entries are nonzero; with two taps in each coset, \(A(\zeta^j)\) and \(A(\zeta^{-j})\) cannot vanish simultaneously. If they did, the ratio of the two nonzero rotation coefficients would force \(\zeta^{2j(u-v)}=1\) for a nonzero gap \(u-v\pmod5\), impossible. Thus at least one diagonal entry is nonzero. This proves (1) for the mixed types. In these formulas \(\zeta^{-j}\) is *not* being replaced by complex conjugation of the coefficient values.

**2. Normalization and support counts.** The group automorphisms \(r\mapsto r^k\), \(s\mapsto r^v s\) for \(k\in\mathbb F_5^*\), \(v\in\mathbb F_5\), together with left and right group translations, preserve convolution rank and the nonzero coefficient condition. A support in a single coset may be moved to \(\{e,r,r^2,r^3\}\). Any triple of the five cyclic exponents is affinely equivalent to \(\{0,1,2\}\), so a three-one support can be moved to \(\{e,r,r^2,s\}\). A two-two support can be moved to \(\{e,r,s,rs\}\) in the parallel case or \(\{e,r,s,r^2s\}\) in the skew case. Independent translations of the pair origins are available because left and right shifts produce their sum and difference, and two is invertible modulo five. For the two-two case the difference ratios are either \(\pm1\) or \(\pm2\), exhausting the classes.

There are \(2\binom54=10\) supports of pure type and \(2\binom53\binom51=100\) of three-one type. There are \(\binom52^2=100\) two-two supports. For each rotation pair, five of the ten reflection pairs have the same unoriented gap, giving fifty parallel and fifty skew supports.

**3. Pure type.** For a function supported on one cyclic coset, the regular-convolution rank is twice the number of nonzero coefficients of its length-five DFT. The prime Fourier-minor theorem implies an exactly four-supported sequence has at most three Fourier zeros, and therefore only ranks \(4,6,8,10\) are possible. All occur: for ranks \(4,6,8\), respectively, take
\[
D(z)=z-1,\quad D(z)=-3+z+2z^2,\quad D(z)=-6+z+2z^2+3z^3
\]
and assign the four tap values \(f(r^k)=D(\zeta^{k+1})\) for \(k=0,1,2,3\). The omitted cyclic position has value \(D(1)=0\). All four displayed tap values are nonzero because each nonzero polynomial \(D\) has degree at most three and cannot vanish at a primitive fifth root of unity (whose minimal polynomial has degree four). Fourier orthogonality gives exactly \(2,3,4\) nonzero cyclic Fourier coefficients, respectively. For rank ten take all four coefficients equal to one: its Fourier transform is four at frequency zero and minus a fifth-root monomial at every other frequency. Translations handle arbitrary pure supports, including the reflection coset.

**4. Three-one type.** On the normalized support write the rotation coefficients \((a,b,c)\) at exponents \(0,1,2\) and the reflection coefficient \(d\), with all four nonzero. Put
\[
q_0=a^2+b^2+c^2,\qquad q_1=b(a+c),\qquad q_2=ac,
\quad u=\frac{\sqrt5-1}{2},\quad v=-\frac{\sqrt5+1}{2}.
\]
The determinant at frequency zero is \(L_0=(a+b+c)^2-d^2\). The determinants at the two nontrivial frequencies are
\[
L_1=q_0+u q_1+v q_2-d^2,\qquad
L_2=q_0+v q_1+u q_2-d^2.\tag{2}
\]
At zero frequency, because \(d\ne0\), at most one scalar block can vanish. Thus (1) permits only ranks between five and ten. If both determinants (2) and the zero-frequency determinant vanished, their differences would give \(q_1=q_2\) and then \(5q_2=0\); but \(q_2=ac\ne0\). Therefore rank five is impossible. The remaining five ranks are attained by the following exact witnesses, ordered as \((a,b,c;d)\):

| Rank | Coefficients \((a,b,c;d)\) |
|---:|---|
| 6 | \((1,\tfrac12,1;\tfrac{\sqrt5}{2})\) |
| 7 | \((1,-\tfrac{3+\sqrt5}{4},1;\tfrac{5-\sqrt5}{4})\) |
| 8 | \((1,1,2;\sqrt{\tfrac{7+\sqrt5}{2}})\) |
| 9 | \((1,1,1;3)\) |
| 10 | \((1,1,1;2)\) |

Substitution in (2) and the two scalar conditions confirms the ranks. The two square roots are positive real numbers, so all coefficients are nonzero.

**5. Two-two type and the rank gap.** Write the nonzero rotation coefficients \((a,b)\) at exponents \(0,1\) and nonzero reflection coefficients \((c,d)\) at exponents \(0,1\) (parallel) or \(0,2\) (skew). Set
\[
X=a^2+b^2-c^2-d^2,\qquad Y=ab,\qquad Z=cd,
\qquad u=\frac{\sqrt5-1}{2},\quad v=-\frac{\sqrt5+1}{2}.
\]
Both \(Y\) and \(Z\) are nonzero. The zero-frequency determinant is \(L_0=X+2Y-2Z=(a+b)^2-(c+d)^2\); its nullity is the number \(0,1,2\) of zeros among \(a+b+c+d\) and \(a+b-c-d\).

For **parallel** pairs, the two nontrivial determinants are
\[
L_1=X+u(Y-Z),\qquad L_2=X+v(Y-Z).\tag{3}
\]
The three distinct slopes \(2,u,v\) show that if any two of \(L_0,L_1,L_2\) vanish then all three vanish; in that case \(X=Y-Z=0\), and the zero-frequency block has nullity one or two. Otherwise, if \(L_0\ne0\) at most one nontrivial determinant can vanish, and if \(L_0=0\) neither nontrivial determinant vanishes. Formula (1) yields only ranks \(4,5,8,9,10\).

For **skew** pairs, the determinants become
\[
L_1=X+uY-vZ,\qquad L_2=X+vY-uZ.\tag{4}
\]
If \(L_1=L_2=0\), their difference forces \(Z=-Y\) and either equation forces \(X=Y\). Therefore \(L_0=5Y\ne0\): both nontrivial blocks can be singular only when neither scalar block is singular. In particular three simultaneous determinant zeros are impossible. Formula (1) then gives only ranks \(6,7,8,9,10\).

The exact coefficient witnesses, ordered \((a,b;c,d)\), establish attainment of all listed ranks:

| Rank | Parallel pair coefficients | Skew pair coefficients |
|---:|---|---|
| 4 | \((1,-1;1,-1)\) | — |
| 5 | \((1,1;1,1)\) | — |
| 6 | — | \((1,-1;u,-u)\) |
| 7 | — | \((1,1;1+\sqrt u,1-\sqrt u)\) |
| 8 | \((1,-1;2,-2)\) | \((1,-1;1,-1)\) |
| 9 | \((1,1;3,-1)\) | \((1,1;1,1)\) |
| 10 | \((1,1;1,2)\) | \((1,1;1,2)\) |

Here \(0<u<1\), so every displayed coefficient is nonzero. Direct substitution in (3) or (4) and the scalar block expressions verifies the advertised ranks. Together with the normalization argument, the full classification follows.

## Verification
The accompanying `check_dihedral.py` uses exact symbolic arithmetic for all mixed-coset witnesses, including their scalar and nontrivial Fourier-block zero patterns. For the pure-coset witnesses it checks cyclotomic remainders in \(\mathbb Q[z]/(1+z+z^2+z^3+z^4)\) and Fourier coefficient counts. It returns `ALL WITNESSES PASS`.

The independent `check_regular.py` constructs each ten-by-ten left-regular convolution matrix directly from the group law, transports witnesses over all four support classes using explicit group symmetries, and tests the resulting ranks by numerical singular-value decomposition. It covers **all 210 supports and 1040 coefficient-and-support instances**, verifying that every claimed rank occurs on every fixed support. It returns `ALL 210 FOUR-ELEMENT SUPPORTS TRANSPORTED; 1040 FULL REGULAR MATRIX RANK TESTS PASS`. This second calculation is a finite-precision cross-check, not a proof that no other ranks occur. The algebraic block argument above supplies those exclusions. Run `python check_dihedral.py && python check_regular.py` with dependencies specified by `requirements.txt`.

## Relationship to prior work
Alagic and Russell, *Uncertainty Principles for Compact Groups* (2006), introduce the general rank-weighted nonabelian Fourier support and its uncertainty inequality. Their general bound does not determine attainable ranks for an exactly four-supported function or distinguish gaps within the two dihedral cosets. Arezoomand and Taeri, *On the Characteristic Polynomial of n-Cayley Digraphs* (2013), give a general representation-theoretic factorization and an index-two cyclic-subgroup spectral formula (Corollary 9); this provides a route to the two-by-two block expression but not an all-coefficient classification or the four support-dependent rank sets. The full texts of both were inspected.

A publicly available complete three-tap theorem for all odd-prime dihedral groups gives the rank spectra for *three*, not four, arbitrary complex coefficients. A balanced four-tap generalized-dihedral theorem covers unit coefficients with two taps in each coset, rather than all nonzero complex coefficients or three-one/four-zero support shapes. A finite dihedral three-tap census similarly assumes coefficient one and three positions. The new statement concerns the exact four-tap, free-coefficient case, including a parallel-versus-skew dichotomy that is not implied by the one-coefficient balanced spectrum. The common underlying Fourier-block decomposition is not claimed as new.

## Limitations
This is a complete finite classification only for the dihedral group of order ten and four exactly nonzero **complex** coefficients. It does not provide a general formula for larger dihedral groups, constrain conditioning, or classify rank multiplicities under distributions on coefficients. The numerical regular-matrix test is supplementary to the algebraic proof. An unindexed equivalent specialized weighted-Cayley computation remains a bibliographic priority risk; no independent mathematical audit has yet been performed.

## References
1. G. Alagic and A. Russell, *Uncertainty Principles for Compact Groups*, arXiv:math/0608702, publicly posted 2006-08-28, https://arxiv.org/abs/math/0608702 .
2. M. Arezoomand and B. Taeri, *On the Characteristic Polynomial of n-Cayley Digraphs*, *Electronic Journal of Combinatorics* 20(3) (2013), P57, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i3p57/pdf/ .
3. *Complete three-tap Fourier-rank spectrum on odd-prime dihedral groups*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-complete-three-tap-fourier-rank-spectrum-on-odd-prime-dihedral-g--eb09d9b17153 .
4. *Balanced four-tap generalized-dihedral convolution: three nullity strata and a sharp quadratic spectral gap*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-balanced-four-tap-generalized-dihedral-convolution-three-nullity--d4787ab578c7 .
5. *Complete ternary-convolution nullity laws on finite dihedral groups*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-complete-ternary-convolution-nullity-laws-on-finite-dihedral-gro--2bbf4bdce108 .
