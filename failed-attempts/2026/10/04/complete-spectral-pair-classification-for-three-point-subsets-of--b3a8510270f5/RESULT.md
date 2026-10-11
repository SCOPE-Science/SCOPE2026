# Complete spectral-pair classification for three-point subsets of cyclic groups
## Finding
Let \(A=\{a_0,a_1,a_2\}\subset\mathbb Z_N\) have three distinct elements. Put \(h=\gcd(N,a_1-a_0,a_2-a_0)\), \(n=N/h\), and \(A^\ast=\{(a-a_0)/h:a\in A\}\subset\mathbb Z_n\). Then \(A\) is spectral if and only if \(3\mid n\) and \(A^\ast\) is a complete set of residues modulo \(3\). In that case the nonzero Fourier-mask zero set is exactly \(Z(A)=\{d\in\mathbb Z_N:d\bmod n\in\{n/3,2n/3\}\}\); every three-element spectrum \(B\subset\mathbb Z_N\) is characterized by the condition that \(B\bmod n\) is a coset of \(\{0,n/3,2n/3\}\subset\mathbb Z_n\); and the number of distinct spectra is exactly \(Nh^2/3\).

In particular, the theorem gives not only existence of a spectrum but the entire family of spectra and its exact cardinality. The criterion depends on the primitive reduction of the three-point set rather than on the ambient order alone.

## Assumptions and scope
Work in the additive cyclic group \\(\\mathbb Z_N\\) with characters \\(x\\mapsto e^{2\\pi i bx/N}\\). A three-element set \\(B\\subset\\mathbb Z_N\\) is called a spectrum for \\(A\\) when the \\(3\\times3\\) character matrix \\( (e^{2\\pi i ab/N})_{a\\in A,b\\in B}\\) has pairwise orthogonal columns. Equivalently, every nonzero difference of two elements of \\(B\\) belongs to the zero set of the mask sum \\(d\\mapsto\\sum_{a\\in A}e^{2\\pi i ad/N}\\).

The integer \\(h\\) is independent of the choice of integer representatives: it is the greatest common divisor of \\(N\\) and the two differences from a chosen base point. After translation and division by \\(h\\), the normalized set \\(A^\\ast\\subset\\mathbb Z_n\\) is primitive in the sense that the greatest common divisor of \\(n\\) and its two nonzero differences is \\(1\\).

## Proof
Translate so that the first element is \\(0\\), and write the normalized primitive set as \\(A^\\ast=\\{0,r,s\\}\\subset\\mathbb Z_n\\), where \\(\\gcd(n,r,s)=1\\). For \\(d\\in\\mathbb Z_N\\), translation contributes only a nonzero phase and division by \\(h\\) gives
\[
\\sum_{a\\in A}e^{2\\pi i ad/N}=0
\\quad\\Longleftrightarrow\\quad
1+e^{2\\pi i rd/n}+e^{2\\pi i sd/n}=0.
\]

Three complex numbers of modulus \\(1\\) sum to \\(0\\) exactly when, after multiplication by a common unit scalar, they are \\(1,\\omega,\\omega^2\\), where \\(\\omega^3=1\\) and \\(\\omega\\ne1\\). Hence a zero forces
\[
n\\mid 3rd,
\\qquad
n\\mid 3sd.
\]
Because \\(\\gcd(n,r,s)=1\\), Bézout gives \\(n\\mid3d\\). The case \\(d\\equiv0\\pmod n\\) is impossible because the mask sum would equal \\(3\\). Therefore \\(3\\mid n\\) and
\[
d\\equiv n/3\\quad\\text{or}\\quad d\\equiv2n/3\\pmod n.
\]
At either of these two residue classes the three phases vanish exactly when \\(0,r,s\\) represent the three distinct residue classes modulo \\(3\\). This proves both the spectrality criterion and the exact zero-set formula.

Assume now that the criterion holds and let \\(q=n/3\\). If \\(B\\) is a three-element spectrum, then every pairwise nonzero difference of its reduction modulo \\(n\\) lies in \\(\\{q,2q\\}\\). Translating one reduced element to \\(0\\), the other two must therefore be \\(q\\) and \\(2q\\). Thus \\(B\\bmod n\\) is a coset of the order-three subgroup \\(\\{0,q,2q\\}\\). Conversely, any three lifts whose reductions form such a coset have all nonzero pairwise differences in the mask zero set, so they form a spectrum.

There are \\(n/3\\) cosets of this subgroup in \\(\\mathbb Z_n\\). Each of the three residue classes in a chosen coset has exactly \\(h\\) lifts to \\(\\mathbb Z_N\\), independently. Hence the number of spectra is
\[
\\frac n3h^3=\\frac{Nh^2}3.
\]
This completes the classification.

## Verification
The standalone checker `verify_three_point_spectral.py` uses exact integer polynomial arithmetic. For each tested character value it computes the order of the relevant root of unity and decides mask vanishing by divisibility by the corresponding cyclotomic polynomial; it does not use floating-point tolerances.

The packaged replay checks every three-subset for \\(3\\le N\\le30\\), comprising \\(31{,}465\\) sets and \\(742{,}574\\) exact cyclotomic zero tests. It then checks every candidate three-element spectrum for every spectral three-subset for \\(3\\le N\\le20\\), comprising \\(468\\) spectral sets and \\(269{,}476\\) support-pair tests. It verifies the zero-set formula, the spectrality criterion, the complete parametrization of spectra, and the count \\(Nh^2/3\\), ending with `VERIFY_OK`.

The finite replay is corroborative. The theorem for arbitrary \\(N\\) follows from the unit-triangle lemma, the primitive greatest-common-divisor reduction, and the pairwise-difference argument above.

## Relationship to prior work
Łaba's 2000 preprint defines spectra of finite mask polynomials and proves, in Corollary 1.7, that the corresponding three-interval integer set is spectral exactly when it tiles. That result supplies the archive-era motivation for isolating the three-point case, but it does not state the finite-cyclic primitive criterion above, the exact mask-zero set, the parametrization of every spectrum, or the count of spectra.

Konyagin and Łaba develop the polynomial-spectrum and integer-tiling framework further for special polynomial structures. Dutkay and Lai clarify reductions among spectral and tiling statements on \\(\\mathbb Z_N\\), \\(\\mathbb Z\\), and \\(\\mathbb R\\). Malikiosis develops general finite-cyclic tools in terms of spectral pairs, difference sets, and vanishing mask values. Those results give broad structural tests, whereas the present theorem closes the cardinality-three finite-cyclic stratum in an explicit normal form and enumerates all spectra.

Lam and Leung's vanishing-sum theory is relevant background: weight-three vanishing sums of roots of unity are controlled by the prime \\(3\\). The proof here uses the sharper elementary geometric fact that three unit vectors sum to zero only as a rotated equilateral triangle, then propagates that fact through the primitive reduction and the spectral-pair difference condition.

## Limitations
The result concerns three-element subsets of cyclic groups only. It does not classify spectral sets of four or more points, and it does not settle the finite cyclic Fuglede conjecture in general. The literature search found no statement equivalent to the combined primitive criterion, exact zero-set description, all-spectra parametrization, and \\(Nh^2/3\\) count, but a differently phrased or poorly indexed prior three-point classification remains a residual originality risk.

## References
1. I. Łaba, *The spectral set conjecture and multiplicative properties of roots of polynomials*, arXiv:math/0010169, first posted 2000-10-17.
2. S. Konyagin and I. Łaba, *Spectra of certain types of polynomials and tiling of integers with translates of finite sets*, arXiv:math/0209204, 2002.
3. D. E. Dutkay and C.-K. Lai, *Some reductions of the spectral set conjecture to integers*, arXiv:1301.0814, 2013.
4. R. D. Malikiosis, *On the structure of spectral and tiling subsets of cyclic groups*, Forum of Mathematics, Sigma 10 (2022), e23, doi:10.1017/fms.2022.14.
5. T. Y. Lam and K. H. Leung, *On vanishing sums of roots of unity*, arXiv:math/9511209.
