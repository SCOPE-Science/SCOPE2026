# Two-scale harmonic-trinomial zeros and the parity-sharp outer-radius defect

## Finding
For fixed coprime integers \(n>k\ge1\) with \(n\ge3\), consider the complex-valued harmonic trinomial
\[
F_c(z)=z^n+c\overline z^{\,k}-1,\qquad c>0.
\]
Put \(M=n+k\), \(a=c^{-1/k}\), \(R=c^{1/(n-k)}\), \(\epsilon_i=c^{-n/k}\), and \(\epsilon_o=c^{-n/(n-k)}\). For all sufficiently large \(c\), its entire zero set consists of exactly \(k\) simple sense-reversing inner zeros and \(M\) simple sense-preserving outer zeros. They admit the following complete, individually labelled expansions, with constants in the error terms depending only on the fixed integers \(n,k\):
\[
\begin{aligned}
 z^{\mathrm{in}}_j&=a\left(\omega_j-\frac{\epsilon_i}{k}\omega_j^{1-n}+O_{n,k}(\epsilon_i^2)\right),
 &\omega_j&=\exp(2\pi i j/k),\quad 0\le j<k,\\
 z^{\mathrm{out}}_j&=R\zeta_j\left[1+\epsilon_o\left(\frac{\Re(\zeta_j^{-n})}{n-k}
 +i\frac{\Im(\zeta_j^{-n})}{n+k}\right)+O_{n,k}(\epsilon_o^2)\right],
 &\zeta_j&=\exp((2j+1)\pi i/M),\quad 0\le j<M.
\end{aligned}
\]
All of these branches depend real-analytically on their respective small positive parameters near zero. In particular, each limiting inner and outer regular-polygon vertex contains exactly one zero after the stated rescalings.

Define \(\rho_c\) as the unique positive solution of \(\rho_c^n+c\rho_c^k=1\), and \(U_c\) as the unique positive solution of \(U_c^n-cU_c^k=1\). For **every** \(c>0\), \(\rho_c\) is the unique zero of least modulus, and every zero has modulus at most \(U_c\). If \(n\) is even, \(-U_c\) is the unique zero of greatest modulus, so the upper bound is globally exact. If \(n\) is odd, the bound \(U_c\) is never attained, and for all sufficiently large \(c\) exactly two conjugate nonreal zeros attain the greatest modulus. Their limiting rays are
\[
\zeta_\pm=\exp(\pm d\pi i/M),
\]
where \(d\) is any odd integer satisfying \(nd\equiv1\pmod{2M}\). Thus, writing \(Z_c=\max\{|z|:F_c(z)=0\}\),
\[
Z_c=R\left[1+\frac{\sigma_{n,k}}{n-k}\epsilon_o+O_{n,k}(\epsilon_o^2)\right],\qquad
\sigma_{n,k}=\begin{cases}1,&n\text{ even},\\\cos(\pi/M),&n\text{ odd}.
\end{cases}
\]
The **sharp parity-dependent deficit** from the elementary outer radius bound is
\[
U_c-Z_c=\begin{cases}0,&n\text{ even and }c>0,\\
\displaystyle\frac{1-\cos(\pi/(n+k))}{n-k}\,c^{-(n-1)/(n-k)}
+O_{n,k}\!\left(c^{-(2n-1)/(n-k)}\right),&n\text{ odd, }c\to\infty.
\end{cases}
\]
For odd \(n\), the displayed leading coefficient is strictly positive. The last formula is an asymptotic, not a claim that a specified finite \(c\) is already in the final two-root regime.

## Assumptions and scope
The parameter \(c\) is positive real; \(n,k\) are fixed coprime integers with \(n>k\ge1\), \(n\ge3\). The terms \(O_{n,k}\) are uniform over the indicated finite vertex index sets as \(c\to\infty\). A zero is *simple* when the real Jacobian determinant of \(F_c:\mathbb R^2\to\mathbb R^2\) is nonzero. Its sign distinguishes sense-preserving from sense-reversing zeros. The statements concerning the global nearest zero, the elementary upper bound, and the even-\(n\) extremizer hold at **every** positive parameter, including parameters where other zeros may be singular; only the complete polygonal zero census and odd-\(n\) farthest-root uniqueness require sufficiently large \(c\).

## Proof
**1. Two compact rescalings and exhaustion.** The equation \(F_c(z)=0\) implies
\[
\big|r^n-cr^k\big|\le1\le r^n+cr^k,\qquad r=|z|.
\]
If \(r^{n-k}\le c/2\), then \(cr^k-r^n\ge cr^k/2\), so \(r\le(2/c)^{1/k}\). Setting \(z=aw\) gives the inner equation
\[
\epsilon_i w^n+\overline w^{\,k}=1,\qquad |w|\le2^{1/k}.
\]
For any sequence of its solutions with \(\epsilon_i\to0\), every limit lies among the \(k\) distinct roots \(\omega_j\) of unity. At each root the limiting real map \(w\mapsto\overline w^k-1\) has nonzero Jacobian \(-k^2\); hence the real-analytic implicit-function theorem gives exactly one nearby zero, real-analytic in \(\epsilon_i\).

In the complementary region \(r^{n-k}>c/2\), put \(z=Rw\). Its equation is
\[
w^n+\overline w^{\,k}=\epsilon_o,\qquad |w|>2^{-1/(n-k)}.
\]
The modulus inequality \(\big||w|^n-|w|^k\big|\le\epsilon_o\) bounds \(w\) above independently of sufficiently small \(\epsilon_o\): for \(|w|\ge2\), the left side is at least \(2^n-2^k>0\). Every subsequential limit therefore has modulus one and solves \(w^n+\overline w^k=0\). Multiplication by \(w^k\) on the unit circle shows that the limiting solutions are exactly the \(M\) distinct points \(\zeta_j\), characterized by \(\zeta_j^M=-1\). At each one, the Jacobian of \(w^n+\overline w^k\) is \(n^2-k^2>0\); hence the implicit-function theorem gives exactly one solution nearby, again real-analytic. Compactness of both rescaled regions excludes all additional zeros for sufficiently large \(c\). The inner Jacobian is negative and outer Jacobian positive by continuity. This proves the exhaustive \(k+M=n+2k\) census, independently of a finite numerical search.

**2. First-order individual locations.** Write the inner solution as \(w=\omega+\delta\). Since \(\overline\omega^{k-1}=\omega\), the first-order equation is \(k\omega\overline\delta+\epsilon_i\omega^n=0\), whence \(\delta=-\epsilon_i\omega^{1-n}/k+O(\epsilon_i^2)\). For an outer solution write \(w=\zeta(1+h)\). Since \(\zeta^n=-\overline\zeta^k\), its linearized equation reads
\[
n h-k\overline h=\epsilon_o\zeta^{-n}+O(|h|^2).
\]
Writing real and imaginary parts gives exactly the two coefficients in the announced outer expansion. Real analyticity supplies the quadratic remainders. In particular,
\[
|z_j^{\mathrm{out}}|=R\left[1+\frac{\epsilon_o}{n-k}\Re(\zeta_j^{-n})+O_{n,k}(\epsilon_o^2)\right].
\]

**3. Globally sharp nearest radius and even-degree farthest radius.** The triangle inequality yields \(1\le r^n+cr^k\), so \(r\ge\rho_c\). The positive point \(z=\rho_c\) is a zero. Equality requires both nonzero summands to have argument zero: \(e^{in\theta}=e^{-ik\theta}=1\). Coprimality forces \(\theta\equiv0\pmod{2\pi}\), proving uniqueness. The reverse triangle inequality gives \(r^n-cr^k\le1\). The function \(r^n-cr^k\) is strictly increasing for \(r\ge R\) and equals zero at \(R\); thus every zero has \(r\le U_c\). If \(n\) is even, coprimality forces \(k\) odd, and \(F_c(-U_c)=U_c^n-cU_c^k-1=0\). Equality in the reverse triangle inequality requires \(e^{in\theta}=1\), \(e^{-ik\theta}=-1\); coprimality and parity force \(\theta\equiv\pi\pmod{2\pi}\). If \(n\) is odd, these phase equations would equate an even integer \(2ak\) to an odd integer \(n(2b+1)\), an impossibility. Hence \(U_c\) is never attained in that case.

**4. Angular arithmetic and the sharp parity defect.** For even \(n\), \(M\) is odd, and among the \(M\) numbers \(\zeta_j^{-n}\) precisely one is \(1\); all are the \(M\)-th roots of unity. For odd \(n\), \(n\) is invertible modulo \(2M\), and the \(\zeta_j^{-n}\) range through the \(M\) equally spaced odd half-step roots. Their maximal real part equals \(\cos(\pi/M)\), attained at exactly the two values \(e^{\pm i\pi/M}\); the associated \(\zeta\)'s are the stated conjugate pair. The fixed positive gap between this maximal real part and all others, together with the uniform \(O(\epsilon_o^2)\) remainder, proves exact farthest-root uniqueness for even \(n\), or conjugate-pair extremality for odd \(n\), once \(c\) is large. Finally, writing \(U_c=R(1+h)\) in \(U_c^n-cU_c^k=1\) gives \(U_c=R[1+\epsilon_o/(n-k)+O(\epsilon_o^2)]\). Subtraction yields the displayed, strictly positive odd-degree deficit and its precise power of \(c\).

## Verification
Run \(\texttt{python3 CHECK.py}\) (Python 3 standard library only). The script solves the independently rescaled real-analytic equations using their exact Wirtinger Jacobians at several values of \(c\) for thirteen coprime exponent pairs. It tests the first-order vertex expansions, predicted counts of constructed branches, simple separation of the constructed roots, and the parity of the farthest branches. This is a finite diagnostic and is **not** evidence that the finite numerical search exhausts all complex zeros. Exhaustion, uniqueness, and the asymptotic remainder are proved in the preceding compactness and implicit-function arguments.

## Relationship to prior work
Brilleslyper, Brooks, Dorff, Howell and Schaubroeck (2020) establish the parameter-dependent number of zeros of the same harmonic trinomial and, explicitly in their Section 3, leave their locations as a question. Therefore the \(n+2k\) *count itself is prior work*, not the new assertion. Geleta and Alemu (first preprint 2021; publication 2022) give annular inclusions, while Gao, Gao and Liu (first online 2022) give geometric inclusion sectors. Barrera, Barrera and Navarrete (2024) classify equivalence of complete trinomial root sets under rotation and reflection, and also state exact root-modulus-equality implications; those statements do not provide the two-scale large-parameter expansions or sharp odd-degree outer-radius defect. Harrat (2025), whose complete six-page text was inspected, gives the coefficient-dependent root-count trichotomy rather than individual asymptotic root locations. The global minimum radius and even-degree equality case here follow elementary triangle equality and are not asserted as independent novel contributions. The present statement instead identifies every high-parameter zero individually to first order, proves exhaustive two-scale regular-polygon localization, and gives a sharp modulus gap with a parity-dependent extremizing configuration. Melman's related 2025 location-sector study and potentially equivalent classical asymptotic constructions remain priority risks; its complete text was not accessible for a decisive passage-by-passage comparison.

## Limitations
No uniform lower bound on the parameter at which the polygonal asymptotics become branchwise valid is claimed, and no classification of singular transition parameters or small-parameter zero locations is attempted. The outer radius formula is sharp only to the displayed asymptotic order for odd \(n\). The paper does not establish historical priority or independent validation. An inaccessible but relevant 2025 location paper could contain an equivalent angular asymptotic, which would require reassessing the originality claim.

## References
- M. Brilleslyper, J. Brooks, M. Dorff, R. Howell and L. Schaubroeck, *Zeros of a one-parameter family of harmonic trinomials*, Proceedings of the American Mathematical Society, Series B **7** (2020), 82–90, first public 2020-06-17, https://doi.org/10.1090/bproc/51 ; open complete PDF https://pdfs.semanticscholar.org/e1be/17dcd3e27784b5ba170c14e1ed7de09c5681.pdf .
- H. L. Geleta and O. A. Alemu, *Location of the Zeros of Certain Complex-Valued Harmonic Polynomials*, first preprint https://arxiv.org/abs/2106.15162 ; published 2022, https://doi.org/10.1155/2022/4886522 .
- L. Gao, J. Gao and G. Liu, *Location of the Zeros of Harmonic Trinomials*, first online 2022-11-29, https://doi.org/10.1007/s40840-022-01416-8 .
- G. Barrera, W. Barrera and J. P. Navarrete, *Egerváry’s theorems for harmonic trinomials*, Acta Mathematica Hungarica **172** (2024), 170–186, open full text https://doi.org/10.1007/s10474-024-01403-4 .
- C. Harrat, *Zeros of harmonic trinomials with complex parameter*, Boletim da Sociedade Paranaense de Matemática **43** (2025), 1–6, open complete article https://doi.org/10.5269/bspm.66200 and PDF https://periodicos.uem.br/ojs/index.php/BSocParanMat/article/download/66200/751375160858/ .
- A. Melman, *Zero location for analytic and harmonic trinomials*, Journal of Mathematical Analysis and Applications **544** (2025), 129078, https://doi.org/10.1016/j.jmaa.2024.129078 (complete text inaccessible during this review).
