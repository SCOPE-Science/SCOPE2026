# Universal sharp conditioning of two quadratic-chirp rows on any prime-field three-site aperture

## Finding
For every prime \(p\ge5\) and every set \(R=\{x_0,x_1,x_2\}\subset\mathbb F_p\) of three distinct sites, put \(\omega=e^{2\pi i/p}\). Select two distinct labels \(\lambda=(a,b)\), \(\lambda'=(a',b')\) from \(\mathbb F_p^2\), and form the \(2\times3\) evaluation matrix
\[
A_{\lambda,\lambda';R}=
\begin{pmatrix}
\omega^{a x_0^2+b x_0}&\omega^{a x_1^2+b x_1}&\omega^{a x_2^2+b x_2}\\
\omega^{a' x_0^2+b' x_0}&\omega^{a' x_1^2+b' x_1}&\omega^{a' x_2^2+b' x_2}
\end{pmatrix}.
\]
All such matrices have **full row rank two**. Let \(\kappa_+(A)\) be the ratio of the two positive singular values (not a condition number for reconstructing arbitrary three-coordinate inputs). Define
\[
k=\left\lfloor\frac{p+1}{3}\right\rfloor,\qquad
\rho_p=\left|1+2\cos(2\pi k/p)\right|,\qquad
\tau_p=\sqrt{5+4\cos(2\pi/p)}.
\]
Then the exact extrema over all unordered pairs of different labels are
\[
\boxed{\min\kappa_+(A)=\sqrt{\frac{3+\rho_p}{3-\rho_p}},\qquad
\max\kappa_+(A)=\sqrt{\frac{3+\tau_p}{3-\tau_p}}.}
\]
For **each fixed first label**, exactly six choices of the second label attain the minimum and exactly six attain the maximum. Consequently there are exactly \(3p^2\) unordered minimizing pairs and \(3p^2\) unordered maximizing pairs. These formulas and counts are **independent of the locations of the three distinct sites**. The minimum is realized by nearly equally spaced three-phasor positions, while the maximum occurs when two phasors coincide and the third lies one root-of-unity step away. As \(p\to\infty\) through primes,
\[
\min\kappa_+(A)=1+\frac{2\pi\sqrt3}{9p}+O(p^{-2}),\qquad
\max\kappa_+(A)\sim\frac{3p}{\sqrt2\pi}.
\]

## Assumptions and scope
Here \(\mathbb F_p\) is identified with integer residues modulo \(p\), and all quadratic phases are evaluated modulo \(p\). Rows are **not** normalized by \(p^{-1/2}\), since that common normalization has no effect on \(\kappa_+\). Both labels may have the same quadratic coefficient \(a\) but must not be identical; thus we optimize over all distinct pairs from the complete family of \(p^2\) finite quadratic-chirp outcomes, not solely cross-basis pairs. Matrix singular values use the usual Euclidean norms over \(\mathbb C\). As a \(2\times3\) matrix, \(A\) cannot recover arbitrary three-dimensional inputs. The result instead characterizes the nonzero singular spectrum and the stability on the two-dimensional observable row space.

## Proof
**1. Every two-label difference produces every nonzero phasor pair.** Write \(\Delta a=a'-a\), \(\Delta b=b'-b\) in \(\mathbb F_p\). Dephase the second row relative to the first and the site \(x_0\), and define
\[
u=\Delta a(x_1^2-x_0^2)+\Delta b(x_1-x_0),\quad
v=\Delta a(x_2^2-x_0^2)+\Delta b(x_2-x_0).
\]
The determinant of this linear map from \((\Delta a,\Delta b)\) to \((u,v)\) is
\[
(x_1-x_0)(x_2-x_0)(x_1-x_2)\ne0
\]
(up to the immaterial sign according to row order). Hence the nonzero label differences correspond bijectively to all \((u,v)\in\mathbb F_p^2\setminus\{(0,0)\}\), regardless of \(R\). In particular, a fixed first label has exactly one second label for each nonzero phasor pair.

**2. Gram spectrum.** Direct multiplication yields
\[
AA^*=\begin{pmatrix}3&\overline S\\S&3\end{pmatrix},\qquad
|S|=|1+\omega^u+\omega^v|.
\]
Thus the squared positive singular values are \(3+|S|\) and \(3-|S|\). Equality \(|S|=3\) would force \(1=\omega^u=\omega^v\), contradicting \((u,v)\ne(0,0)\); thus full row rank holds. The ratio \(\sqrt{(3+s)/(3-s)}\) strictly increases in \(0\le s<3\). It remains to find the exact minimum and maximum of \(|1+\omega^u+\omega^v|\) over all nonzero phasor pairs.

**3. Largest phasor sum.** Put \(c=\cos(2\pi/p)\). For every nonzero residue \(j\), \(\cos(2\pi j/p)\le c<1\), with equality exactly for \(j=\pm1\). Moreover at least two of the differences \(u\), \(v\), and \(u-v\) are nonzero. Since
\[
|1+\omega^u+\omega^v|^2
=3+2\bigl(\cos(2\pi u/p)+\cos(2\pi v/p)+\cos(2\pi(u-v)/p)\bigr),
\]
we obtain \(|S|^2\le 3+2(1+2c)=5+4c\). Equality holds only if exactly one of these three differences is zero and the other two are \(\pm1\). Thus the **six** maximizing pairs are
\[
(u,v)=(0,\pm1),\quad(\pm1,0),\quad(\pm1,\pm1)
\]
with matching signs in the final pair. Their common modulus is \(\tau_p\).

**4. Smallest phasor sum.** If two of \(1,\omega^u,\omega^v\) coincide, then \(|S|=|2+\omega^j|>1\), unless all three coincide (which is excluded). Balanced triples of distinct roots give modulus less than one, so every minimizer consists of distinct roots. For distinct roots, order them counterclockwise and let \(r,s,t\) be the three positive integer cyclic gaps. Then \(r+s+t=p\). The elementary triangle cosine identity gives
\[
|S|^2=1-8\cos(\pi r/p)\cos(\pi s/p)\cos(\pi t/p).
\]
If one gap is at least \(p/2\), its cosine is nonpositive, so \(|S|\ge1\); again this cannot minimize. For the remaining triples all three cosines are positive. On \((0,\pi/2)\), the function \(\log\cos z\) has strictly negative second derivative \(-\sec^2z\). If two integer gaps differ by at least two, replacing the larger by one less and the smaller by one more strictly **increases** their product of cosines. Thus the unique minimizing gap multiset has all gaps differing by at most one. For \(p=3q+1\) it is \(\{q,q,q+1\}\); for \(p=3q+2\), \(\{q,q+1,q+1\}\). Choosing representatives \(1,\omega^k,\omega^{2k}\), where \(k=\lfloor(p+1)/3\rfloor\), shows that the minimal modulus is exactly \(\rho_p<1\), completing the bound.

**5. All equality pairs and asymptotic scaling.** As \(p\) is not divisible by three, a balanced three-root configuration has one exceptional cyclic gap; its starting root determines the configuration uniquely. The \(p\) translates of this configuration give \(p\) distinct unordered three-root sets. Exactly three of these contain the distinguished root \(1\), and ordering the other two roots gives exactly six minimizing \((u,v)\) pairs. Step 3 gives exactly six maximizing \((u,v)\) pairs. By Step 1 the label-difference map is bijective for every \(R\), so the corresponding second-label counts are six for each first label. Dividing the ordered totals \(6p^2\) by two gives \(3p^2\) unordered pairs of each type.

Finally, expansion of the nearest-to-\(2\pi/3\) angle gives \(\rho_p=2\pi\sqrt3/(3p)+O(p^{-2})\), while \(\tau_p=3-4\pi^2/(3p^2)+O(p^{-4})\). Substituting into the singular-value ratios gives the displayed asymptotic laws.

## Verification
The standalone `checker.py`, executable with standard Python 3, independently evaluates every nonzero phasor pair for 24 primes from 5 through 101, comparing both sharp formulas and the six optimizer pairs. For every three-site support in primes at most 13, and four representative supports in larger primes, it checks that the quadratic phase-difference map is bijective and transfers the six-by-six optimizer counts. Direct complex Gram comparisons corroborate the two singular-value formulas. Run `python checker.py` and expect `CHECK_PASS primes=24 phasor_comparisons=75960; all support and Gram checks passed`. These tests are finite diagnostics: Steps 1–5 supply the proof for every prime.

## Relationship to prior work
Dongwei Li's 2026 finite-parabola uncertainty paper introduces the same quadratic-chirp family and establishes sharp **zero counts** for sparse sums, including three-site supports. Its main result concerns support, not optimal row-pair conditioning, and its full text has no singular-value or condition-number theorem. A published result on the exact Riesz conditioning of **three-by-three** Fourier matrices with consecutive spatial rows finds nearly equilateral optimal frequency triples; its root-of-unity balancing geometry is strongly related, but it does not give these **two-by-three** chirp-sampling singular values, support universality, six-per-label extrema or worst-case law. A published classification of three-column Bargmann phases in full prime MUB families studies Gram matrices of **three full-length vectors**, not sampling two rows on a three-site aperture. The present theorem is a quantitative, partial-row counterpart to these distinct settings; it is not a claim that equidistributed phasors themselves are newly discovered.

## Limitations
This classification concerns two distinct **finite quadratic-chirp outcomes** sampled on exactly three spatial sites, with any prime dimension at least five. It does not optimize only pairs from different bases, cover prime-power fields, establish stable reconstruction of three independent unknown coefficients from two samples, or treat more than two outcome rows. The result uses elementary phasor geometry, potentially known in other terminology, and literature searches cannot exclude an older equivalent restricted-frame classification. An older equivalent restricted-frame theorem could still supersede the asserted novelty.

## References
1. D. Li, *Sharp Total-Support Uncertainty for the Standard Complete Set of Mutually Unbiased Bases*, arXiv:2609.16030, first submitted 2026-09-11, https://arxiv.org/html/2609.16030v2 .
2. *Sharp Riesz conditioning for consecutive triples on finite cycles*, public published-finding corpus research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-riesz-conditioning-for-consecutive-triples-on-finite-cycle--1200745c9cae .
3. *Exact Bargmann-phase histograms and three-column spectra for prime quadratic-chirp bases*, public published-finding corpus research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-bargmann-phase-histograms-and-three-column-spectra-for-pri--11239821c1c5 .
