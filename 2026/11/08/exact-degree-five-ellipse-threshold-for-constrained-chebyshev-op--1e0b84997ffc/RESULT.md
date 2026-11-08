# Exact degree-five ellipse threshold for constrained Chebyshev optimality

## Finding
Let \(r>1\), and let \(E_r\) denote the closed ellipse with foci \(\pm1\) and semiaxes \(a_r=(r+r^{-1})/2\), \(b_r=(r-r^{-1})/2\). For every real \(c>a_r\), consider minimizing \(\max_{z\in E_r}|p(z)|\) over all complex polynomials \(p\) of degree at most five satisfying \(p(c)=1\). Write \(t_{5,c}(z)=T_5(z)/T_5(c)\), where \(T_5(z)=16z^5-20z^3+5z\).

Define \(P(v)=256v^4+(128-64\sqrt5)v^3-(104+88\sqrt5)v^2-(56+32\sqrt5)v-(5+3\sqrt5)\). It has exactly one positive zero \(v_*\in(1,2)\). Put \(a_* = \sqrt{1+v_*}\) and \(r_* = a_*+\sqrt{a_*^2-1}\).

**Theorem.** For \(1<r\le r_*\), the polynomial \(t_{5,c}\) is the unique minimizer for **every** real \(c>a_r\). For \(r>r_*\), it is **not** a minimizer for all \(c>a_r\) sufficiently close to \(a_r\). Thus \(r_*\) is the exact critical ellipse parameter in degree five. Numerically, \(v_*\approx1.29023072795624\), \(r_*\approx2.64923406472235\), and the corresponding minor-to-major axis ratio is approximately \(0.750574959938816\). The endpoint \(r=r_*\) belongs to the all-\(c\) optimal regime.

## Assumptions and scope
All ellipses are nondegenerate, both foci are fixed at \(\pm1\), all normalizing points \(c\) are real and strictly greater than the major semiaxis, the polynomial coefficients may be complex, and the degree is **at most five**. The result concerns the specific normalized first-kind Chebyshev candidate, not an explicit formula for the minimizer when that candidate fails. Symmetry gives the analogous statements for real \(c<-a_r\).

## Proof
**1. Exact optimality criterion.** We use Fischer and Freund's published, necessary-and-sufficient criterion (Lemma 1 in *Chebyshev Polynomials Are Not Always Optimal*). Set \(A=a_r>1\), \(h=c-A>0\), \(\phi_l=l\pi/5\), and for \(1\le l\le5\) define
\[
\sigma_l(A,h)=(-1)^l\left[\frac12\left(1+(-1)^l\frac{T_5(A+h)}{T_5(A)}\right)+\sum_{k=1}^4\frac{T_k(A+h)}{T_k(A)}\cos(k\phi_l)\right].
\]
That criterion states that \(t_{5,c}\) is optimal if and only if all five \(\sigma_l\) are nonnegative; the other five symmetric contact weights coincide with these. The underlying discrete contact weights solve the dual optimality conditions for the \(2n\) alternating modulus contacts on the ellipse. Uniqueness of the minimizer for exterior \(c\) follows from uniqueness of this constrained Chebyshev problem, also established in the cited source.

**2. Positive denominator and finite exact identities.** Let \(Q(A)=2\prod_{k=1}^5 T_k(A)\). Since each \(T_k(A)>0\) for \(A>1\), we have \(Q(A)>0\). Define \(v=A^2-1>0\), expand \(Q(A)\sigma_l(A,h)=\sum_{j=1}^{5}C_{l,j}(A)h^j\); the constant term vanishes for every \(l\). Each \(C_{l,j}(A)\) is a polynomial in \(A\) of fixed parity (even for odd \(j\), odd for even \(j\)); hence \(C_{l,j}(A)=A^{\epsilon_j}D_{l,j}(v)\) with \(\epsilon_j=0\) for odd \(j\) and \(\epsilon_j=1\) for even \(j\), where each \(D_{l,j}\) is a polynomial with coefficients in \(\mathbb Q(\sqrt5)\). The *complete* coefficients are generated and exactly verified by the standalone `check.py` supplied with this theorem.

The critical identity is
\[
C_{2,1}(A)=(1-\sqrt5)A^4P(A^2-1).
\]
For the remaining \(24\) pairs \((l,j)\ne(2,1)\), **every coefficient** of \(D_{l,j}(v)\) is strictly positive. This last finite algebraic assertion is proved by exact expansion: express each coefficient as \(a+b\sqrt5\), \(a,b\in\mathbb Q\), and establish the strictly positive rational lower bound \(a+2b\) if \(b\ge0\), or \(a+9b/4\) if \(b<0\), using \(2<\sqrt5<9/4\). The supplied independent-from-numerics symbolic certificate exhaustively checks all \(161\) such positive coefficients, the zero constant terms, and the critical polynomial identity. This is a finite polynomial-identity calculation, not a numerical sampling or induction beyond the checked degree.

**3. A unique positive threshold.** The coefficients of \(P(v)\), in descending order, are \(256>0\), \(128-64\sqrt5<0\), \(-104-88\sqrt5<0\), \(-56-32\sqrt5<0\), and \(-5-3\sqrt5<0\). Descartes' rule of signs permits exactly one positive root counting multiplicity, and the inequalities \(P(1)<0<P(2)\) ensure it exists in \((1,2)\). Thus \(P(v)<0\) when \(0<v<v_*\), \(P(v_*)=0\), and \(P(v)>0\) when \(v>v_*\).

**4. The two regimes and the endpoint.** If \(0<v\le v_*\), then \(C_{2,1}(A)\ge0\), while all the other coefficients of \(Q(A)\sigma_l(A,h)\) are positive. Since \(h>0\), all five contact weights are strictly positive; the criterion proves optimality and uniqueness for every \(c>A\), including at \(v=v_*\). If \(v>v_*\), then \(C_{2,1}(A)<0\). Therefore \(Q(A)\sigma_2(A,h)=C_{2,1}(A)h+O_A(h^2)<0\) for all sufficiently small \(h>0\). The necessary part of the criterion proves nonoptimality. Finally \(A=(r+r^{-1})/2\) increases strictly with \(r>1\), so the unique threshold in \(v\) translates to the stated \(r_*\). QED.

## Verification
Run `python3 check.py` with SymPy installed. It reconstructs the five exact contact polynomials, checks all boundary constants and \(161\) coefficient lower bounds in rational arithmetic with \(\sqrt5\), verifies the exceptional quartic identity and its sign pattern, and checks \(P(1)<0<P(2)\). Expected output: `ELLIPSE_DEGREE5_THRESHOLD_PASS strict_positivity_coefficients=161 exceptional_quartic=PASS unique_positive_root=PASS`. The numerical values of \(v_*\) and \(r_*\) are approximations only; the algebraic definition is exact. The proof is the finite polynomial identity plus the cited published equivalence criterion, not a finite numerical experiment.

## Relationship to prior work
Fischer and Freund (1989 report; 1991 journal paper) already proved that Chebyshev polynomials are always optimal in degrees one through four and can fail for degrees five and higher. They also formulated the exact contact-weight criterion used here and presented the numerical estimate \(r^*(5)=2.6492\) in their Table I. The known first-failure phenomenon, general optimality criterion, and numerical estimate are **not** claimed as new. The present result converts the previously numerical degree-five threshold into a unique specified algebraic root and proves a global, sharp **if-and-only-if classification over all exterior real normalization points**, including the equality case. Fischer and Freund (1988 preprint; 1990 journal paper) treat a more general complex normalizing point and provide general conditions and large-separation results; these do not provide the exact degree-five global threshold. Charpentier, Levenberg and Wielonsky (first public July 11, 2022) relate extremal-growth polynomials to optimal prediction measures and study asymptotic exterior-point phenomena. That connection motivates the finite-degree sharpness question, but their theorem is an asymptotic statement and does not give this finite degree-five classification.

## Limitations
Historical priority is provisional: an unlocated later calculation may state the same algebraic threshold despite the sources and record searches inspected. The result does not identify the optimal polynomial in the non-Chebyshev regime and does not extend the exact classification to degree six or higher or to nonreal normalization points. The computation requires only finite exact symbolic identities; the literature comparison does not prove historical priority.

## References
1. B. Fischer and R. Freund, *Chebyshev Polynomials Are Not Always Optimal*, Stanford technical report STAN-CS-89-1264, June 1989; *Journal of Approximation Theory* **65** (1991), 261–272. Full report: https://www.mic.uni-luebeck.de/fileadmin/mic/publications/1991/1991-JAT-FR.pdf . DOI: 10.1016/0021-9045(91)90091-N .
2. R. Freund and B. Fischer, *On the Constrained Chebyshev Approximation Problem on Ellipses*, RIACS TR 88.20 (August 1988), *Journal of Approximation Theory* **62** (1990), 297–315. Public original: https://ntrs.nasa.gov/api/citations/19890003829/downloads/19890003829.pdf . DOI: 10.1016/0021-9045(90)90054-T .
3. S. Charpentier, N. Levenberg and F. Wielonsky, *An Extremal Problem for the Bergman Kernel of Orthogonal Polynomials*, arXiv:2207.04662, first submitted July 11, 2022. https://arxiv.org/abs/2207.04662 .
