# Sharp support-free arcs for circle measures with vanishing first and fourth Fourier moments

## Finding

Let \(\mu\) be a nonzero finite positive Borel measure on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) such that \(\widehat\mu(1)=\widehat\mu(4)=0\). The largest length of an open circular arc disjoint from \(\operatorname{supp}\mu\), optimized over all such measures, is exactly
\[
G_*=2\pi-2\arccos(c)=2.56935610063168\ldots,
\quad y=\frac{2+\sqrt{10}}{12},\quad
b=\sqrt y,\quad s=\sqrt{1-2y},\quad c=s-b.
\]
Every equality measure is, up to positive scaling and common rotation, the following unique four-atomic probability measure. Define \(A=\arccos c\), \(B=\arccos b\). Then
\[
\mu_* = \frac{b}{2(b-c)}(\delta_A+\delta_{-A})
 +\frac{-c}{2(b-c)}(\delta_B+\delta_{-B}).
\]
The four atoms are distinct and have strictly positive weights. In particular, the sharp sparse-notch gap is larger than \(2\pi/3\), the gap of the regular three-point rule that also annihilates both moments.

## Assumptions and scope

We use \(\widehat\mu(k)=\int_{\mathbb T}e^{-ikt}\,d\mu(t)\), with vanishing as *complex* coefficients. The closed support of \(\mu\) need not be finite, symmetric or absolutely continuous. An empty arc is an open connected circular arc missing that closed support. Angular lengths are measured in radians, with the full circle of length \(2\pi\). Only frequencies \(1\) and \(4\) are required to vanish; all other coefficients are unrestricted. Normalizing the total mass to one and rotating the measure preserve the hypotheses and arc lengths.

## Proof

**1. Exact trigonometric dual certificate.** Let \(T_4(x)=8x^4-8x^2+1\), and introduce \(e=-s-b\) and \(k=16bs^2>0\). From \(24y^2-8y-1=0\), direct polynomial expansion gives the exact identity
\[
P(x):=T_4(x)+kx=8(x-b)^2(x-c)(x-e).
\tag{1}
\]
The bounds \(5/12<y<4/9\) follow from \(3<\sqrt{10}<10/3\). Hence \(b>s>0\), while \(4s^2>y\) implies \(b+s>1\). It follows that
\[
 e<-1<c<0<b<1.
\]
Consequently \(P(x)\ge0\) for every \(x\in[c,1]\), with equality exactly at \(x=c\) or \(x=b\). Because both cosine moments at \(1\) and \(4\) vanish, equation (1) yields
\[
\int_{\mathbb T} P(\cos t)\,d\mu(t)=0.
\tag{2}
\]

**2. Universal gap bound.** Suppose an admissible positive measure had a support-free arc of length strictly greater than \(G_*\). Rotate its complementary closed arc into \([ -\alpha,\alpha]\), with \(\alpha<A=\arccos(c)\). Thus \(\cos t>c\) on its support. By (1)–(2) the cosine pushforward must be concentrated on the single point \(b\); but then \(\int\cos t\,d\mu(t)=b\mu(\mathbb T)>0\), contrary to \(\widehat\mu(1)=0\). This proves no longer empty arc exists.

**3. Sharpness and positive weights.** At the boundary \(\alpha=A\), the support of the cosine pushforward is contained in \(\{c,b\}\). For a probability measure its total masses on these two cosine fibers must be
\[
 w_c=\frac{b}{b-c},\qquad w_b=\frac{-c}{b-c},
\]
by normalization and the vanishing first cosine moment. Both are strictly positive, their sum is one, and \(w_cc+w_bb=0\). Since \(P(c)=P(b)=0\), equation (1) gives \(w_cT_4(c)+w_bT_4(b)=0\). Symmetrically splitting the two fiber masses between their antipodal-angle sites \(\pm A\) and \(\pm B\) kills the two imaginary moments as well, so \(\widehat\mu_*(1)=\widehat\mu_*(4)=0\). The arc \((A,2\pi-A)\) is support-free and has length \(2\pi-2A=G_*\).

**4. Rigidity without a symmetry assumption.** For an arbitrary equality measure, the cosine-fiber totals are the unique \(w_c,w_b\) above. Write \(\Delta_c\) and \(\Delta_b\) for the differences between masses at positive and negative angles on each fiber. Vanishing of the imaginary Fourier moments at \(1\) and \(4\) gives
\[
\begin{pmatrix}
\sin A&\sin B\\
\sin(4A)&\sin(4B)
\end{pmatrix}
\begin{pmatrix}\Delta_c\\\Delta_b\end{pmatrix}=0.
\]
For \(x=\cos\theta\), the ratio \(\sin(4\theta)/\sin\theta\) is \(U_3(x)=4x(2x^2-1)\). Since \(c<0\), \(c^2<1/2\), \(b>0\), and \(b^2=y<1/2\), one has \(U_3(c)>0>U_3(b)\). Thus the displayed matrix is nonsingular, so \(\Delta_c=\Delta_b=0\). All equality measures are precisely the stated symmetric rule, up to rotation and scaling.

## Verification

The standalone `CHECK.py` uses exact SymPy algebra to verify the polynomial factorization, the quadratic relation for \(y\), rational inequalities bounding the roots, the positive-mass moment identities, and the signs used in the sine-system determinant. Run `python CHECK.py` with the version bounds in `requirements.txt`. A separate numerical approximation checks decimal display only; neither a finite test nor a symbolic log replaces the universal positive-measure integral proof.

## Relationship to prior work

Di Dio and Kummer (arXiv:1903.00598, first public March 2, 2019) investigate truncated moment problems with missing monomials and bounds for representing-atom counts, especially their Section 3, Theorem 3.7. Those bounds do not specify the maximal support-free circular arc for the complex notch set \(\{1,4\}\) or classify equality measures. Peherstorfer (arXiv:1001.2451, Section 1 and the characterization theorem) studies positive circle quadratures exact for entire consecutive Fourier frequency bands; the present measure is constrained by only two nonconsecutive Fourier zeros. A published sparse-notch result for \(\{1,2,6\}\) supplies a different sharp gap and six-atom equality measure: its stronger assumptions at frequencies 2 and 6 do not follow from zeros at 1 and 4, and conversely its hypotheses do not force the fourth coefficient to vanish. Thus its conclusion does not imply the present bound.

The proof technique uses classical moment duality and Chebyshev polynomials. The precise sparse-notch algebraic constant and full four-atom rigidity were not located in the inspected sources; this is a best-knowledge originality assessment, not a universal historical-priority certificate.

## Limitations

The theorem is specific to the vanishing Fourier coefficients at \(1\) and \(4\) and makes no claim for arbitrary sparse notch sets, approximate zeros, or quantitative near-extremal stability. The exact algebraic dual construction is verified, but no independent external mathematical audit has been performed. Older broadly titled trigonometric-polynomial extremal papers (Gilbert–Smyth, 2000, and Goldstein–McDonald, 1984) could not be read in full and remain priority risks; their metadata and abstracts are not substitutes for full proofs.

## References

- Philipp J. di Dio and Mario Kummer, *The multidimensional truncated Moment Problem: Carathéodory Numbers from Hilbert Functions*, arXiv:1903.00598, first version March 2, 2019. https://arxiv.org/abs/1903.00598
- Franz Peherstorfer, *Positive trigonometric Quadrature Formulas and quadrature on the unit circle*, arXiv:1001.2451, January 14, 2010, especially Introduction and Section 3. https://arxiv.org/html/1001.2451v1
- *A sharp sparse Fourier-notch gap on the circle*, published mathematical record for the different zero set \(\{1,2,6\}\), November 16, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-a-sharp-sparse-fourier-notch-gap-on-the-circle--6a5a2c4b54f3
- A. D. Gilbert and C. J. Smyth, *Zero-Mean Cosine Polynomials which are Non-Negative for as Long as Possible*, J. London Math. Soc. 62 (2000), 489–504. https://doi.org/10.1112/S0024610700001216
- M. Goldstein and J. N. McDonald, *An Extremal Problem for Non-Negative Trigonometric Polynomials*, J. London Math. Soc. 29 (1984), 81–88. https://doi.org/10.1112/jlms/s2-29.1.81
