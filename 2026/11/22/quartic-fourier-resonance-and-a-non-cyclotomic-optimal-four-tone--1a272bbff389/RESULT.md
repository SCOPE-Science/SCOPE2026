# Quartic Fourier resonance and a non-cyclotomic optimal four-tone eighth moment

## Finding
For every integer \(m\ge4\) and every four unit complex numbers \(a,b,c,d\), define
\[
P_{m}(z)=a+bz+cz^{m}+dz^{m+1},\qquad
\mathcal M_m(a,b,c,d)=\frac1{2\pi}\int_0^{2\pi}|P_m(e^{it})|^8\,dt.
\]
The value is unchanged by multiplying all four coefficients by the same unit scalar or by replacing \(P_m(z)\) with \(P_m(\eta z)\), \(|\eta|=1\). Hence every coefficient quadruple is uniquely normalized to \((a,b,c,d)=(1,1,U,V)\) using these operations.

Let \(\rho\) be the unique root in \((0,2)\) of
\[
6\rho^3-\rho^2+76\rho-1=0,
\]
and let
\[
\mathcal L=676+36\rho^4-8\rho^3+912\rho^2-24\rho
   =675.842088113977\ldots.
\]
Then the exact sharp moment ranges are
\[
\boxed{\ \mathcal M_4\in[\mathcal L,5012],\qquad
       \mathcal M_m\in[676,4900]\quad(m\ge5).\ }
\]
Both endpoints in each interval are attained, and all intermediate values occur. In particular, \(\mathcal L<676\): the first fourth-convolution resonance lowers the optimum strictly below the separated-block value.

All equality cases can be stated after the normalization \((1,1,U,V)\). For \(m=4\), the maximum occurs only at \(U=V=1\). For the minimum, choose either of the two conjugate numbers \(w\in\mathbb T\) satisfying \(|1+w|=\rho\), and set
\[
K(w)=4(1+w^{-1})(1+5w^{-1}+w^{-2}),\qquad
U=-\frac{\overline{K(w)}}{|K(w)|},\qquad V=Uw.
\]
These are the only two normalized minimizers. For every \(m\ge5\), the maxima are exactly \(V=U\) and the minima are exactly \(V=-U\), with arbitrary \(|U|=1\).

No finite root-of-unity phase alphabet, of any order, contains a minimizer at \(m=4\). Binary phases achieve exactly \(676\), not \(\mathcal L\).

## Assumptions and scope
The coefficient magnitudes are exactly one and the exponent \(m\) is an integer at least four. The moment is with normalized Haar measure on the circle; neither arbitrary coefficient magnitudes nor \(m=2,3\) are included. The same eighth-moment formulas hold for uniform sampling at \(N\)-th roots of unity when \(N>4(m+1)\), since no nonzero Fourier frequency in \(|P_m|^8\) is divisible by such an \(N\).

## Proof
**Step 1 (convolution block separation).** Write \(P_m(z)=(1+z)+z^m(U+Vz)\) after normalization. Its fourth power is
\[
P_m(z)^4=\sum_{j=0}^{4}{4\choose j}z^{mj}
     (1+z)^{4-j}(U+Vz)^j.
\]
The \(j\)-th block has exponents in \([mj,mj+4]\). Parseval states that \(\mathcal M_m\) is the sum of the squared moduli of the coefficients of \(P_m^4\). For \(m\ge5\), these blocks are disjoint. Expanding their squared coefficients with binomial coefficients, and writing \(w=V/U\), gives exactly
\[
\mathcal M_m=2716+1056(w+w^{-1})+36(w^2+w^{-2}),\qquad m\ge5.
\]
Equivalently, for \(x=\operatorname{Re}w\in[-1,1]\),
\[
\mathcal M_m=2644+2112x+144x^2.
\]
The derivative \(2112+288x\) is strictly positive on \([-1,1]\); the unique relative phases at the minimum and maximum are therefore \(w=-1\) and \(w=1\). Their moment values are \(676\) and \(4900\).

**Step 2 (exact fourth-order overlap).** At \(m=4\), adjacent blocks meet at exactly one exponent \(4(j+1)\) for each \(j=0,1,2,3\). The two corresponding coefficient contributions are \({4\choose j}V^j\) and \({4\choose j+1}U^{j+1}\). Adding their four interference cross terms to the separated-block expression gives
\[
\mathcal M_4=2716+1056(w+w^{-1})+36(w^2+w^{-2})
 +2\operatorname{Re}\left[U K(w)\right],
\]
with \(K(w)\) as in the finding. The coefficients \(4,24,24,4\) arise from the products \({4\choose j}{4\choose j+1}\). This is an exact coefficient identity, not an asymptotic or finite numerical test.

**Step 3 (one-dimensional sharp optimization).** Set \(h=|1+w|\in[0,2]\). Since \(w+w^{-1}=h^2-2\) and \(|K(w)|=4h(h^2+3)\), Step 2 becomes
\[
\mathcal M_4=676+912h^2+36h^4+2\operatorname{Re}[UK(w)].
\]
For each \(h>0\), either extremal phase of the final term can be selected by choosing \(U\), so the sharp lower and upper envelopes are
\[
F_-(h)=676+36h^4-8h^3+912h^2-24h,
\quad F_+(h)=676+36h^4+8h^3+912h^2+24h.
\]
The function \(F_+\) is strictly increasing on \([0,2]\), with \(F_+(2)=5012\). Moreover,
\[
F_-'(h)=24(6h^3-h^2+76h-1),
\]
whose parenthetical factor is strictly increasing on \([0,2]\), because its derivative \(18h^2-2h+76\) is strictly positive. It changes sign between \(0\) and \(1/75\), hence has exactly one zero \(\rho\); this is the unique global minimum. Evaluating at \(h=1/76\) already proves \(F_-(h)<676\). The phase conditions in the finding follow from equality in \(\operatorname{Re}(UK)\ge-|K|\). For \(h=\rho\in(0,2)\), exactly two conjugate \(w\) are possible and neither makes \(K(w)=0\); therefore the normalized minimizers are precisely the two stated. The maximum requires \(h=2\), hence \(w=1\), then \(U=1\). Continuity on the connected phase torus establishes every intermediate moment value.

**Step 4 (no cyclotomic minimizer).** The polynomial \(6X^3-X^2+76X-1\) has no rational root among the rational-root-theorem possibilities \(\pm1,\pm1/2,\pm1/3,\pm1/6\), so it is irreducible over \(\mathbb Q\). Its positive root \(\rho\) is not an algebraic integer because its primitive irreducible polynomial is not monic. If a minimizing relative phase \(w\) were a root of unity, then \(\rho^2=2+w+w^{-1}\) would be an algebraic integer. Thus \(\rho\) would also be an algebraic integer, a contradiction. Global phase and argument-rotation normalization preserve any finite root-of-unity alphabet; hence no such coefficient alphabet attains \(\mathcal L\). For binary phases, the normalized pairs satisfy \(U,V\in\{1,-1\}\). Checking these four cases in the exact formula shows the minimum is \(676\), attained at \(V=-U\); thus binary phases cannot attain \(\mathcal L\).

## Verification
The accompanying standard-library Python program `check.py` independently computes all nonzero Laurent coefficients by expanding \(P_m^4\) as a dictionary indexed by the Fourier exponent and the two phase exponents, then summing the squared coefficients. Exact integer identities were checked at \(m=4,5,6,7,9,12\). It also verifies that the fourth and sixth moments agree as Laurent polynomials between \(m=4\) and \(m=5\), whereas the eighth moments differ; checks a rational strict-improvement witness; evaluates the explicitly constructed minimizer; and checks 180 independent unit-circle quadratures. Run with `python3 check.py` (no dependencies beyond the standard library). The infinite-family assertion and the phase-alphabet obstruction follow from the proof, not from these finite computations.

## Relationship to prior work
Fourier moments and additive structure are developed, for example, by Iosevich, Li and Yu (2026), including general Fourier-moment and extension principles, but not this four-tone phase-only eighth-moment optimization. Existing sixth-moment comparisons for the same adjacent-pair frequency support distinguish \(m=3\) from \(m\ge4\); they do not determine the first order-four overlap occurring at \(m=4\). The two-torus four-character rectangle has a general phase-order law, but its nonaliasing geometry applies to the separated case \(m\ge5\), not to this resonant one-dimensional case. The upper endpoint is consistent with classical alignment-of-phases principles for even moments; it is not the principal originality claim. The contribution here is the exact resonant lower endpoint, the cubic minimizer, equality rigidity, and the obstruction for every finite phase alphabet.

## Limitations
Historical priority beyond the inspected primary work and indexed records is not guaranteed. The theorem concerns four prescribed frequencies with unit-modulus coefficients, not general sparse Fourier supports or arbitrary magnitudes. The comparison is at eighth moment; higher moments and other separations are not classified.

## References
1. A. Iosevich, Z. Li and K. Yu, *Spectral synthesis, Fourier extension, and arithmetic in* \(\mathbb Z_N^d\), arXiv:2609.25404 (first submitted September 21, 2026), Sections 8.2 and 9.1, https://arxiv.org/abs/2609.25404.
2. *The first cubic-resonance threshold for phase-only two-block Fourier polynomials* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-the-first-cubic-resonance-threshold-for-phase-only-two-block-fou--6989b70094e0.
3. *A sharp phase-order transition for the four-character Fourier rectangle* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-phase-order-transition-for-the-four-character-fourier-re--b28d10ed4d3f.
4. *Sharp eighth-moment norm at the first fourth-order resonance* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-eighth-moment-norm-at-the-first-fourth-order-resonance--5598303b6ef1. These are statements of related mathematical results and are not used as premises for the calculations.
