# Flat four-point finite-parabola Fourier zeros: a prime-field symmetry dichotomy

## Finding
For every odd prime \(p\ge5\), every four-point support \(R\subset\mathbb F_p\), and any nonzero equal-magnitude coefficients \((c_t)_{t\in R}\), define
\[
F(a,b)=\sum_{t\in R}c_t\omega^{at^2+bt},\qquad
\omega=e^{2\pi i/p},\quad (a,b)\in\mathbb F_p^2.
\]
Let \(Z(F)=|\{(a,b):F(a,b)=0\}|\). A support is **centrally symmetric** if \(R=s+\{-u,-v,v,u\}\) for distinct nonzero \(u,\pm v\) in \(\mathbb F_p\), or equivalently if its points can be paired into two pairs with the same sum. Then the **entire attainable zero-count spectrum**, for a fixed support, is
\[
\begin{array}{c|c}
\text{support geometry}&\text{attainable values of }Z(F)\\\hline
\text{centrally symmetric}&\{0,1,2,p\}\\
\text{not centrally symmetric}&\{0,1,2\}.
\end{array}
\]
The maximum \(p\) is attained precisely when \(R\) is centrally symmetric and there exists a frequency \((a_0,b_0)\) such that the two coefficient pairs become opposites after modulation \(c_t\mapsto c_t\omega^{a_0t^2+b_0t}\). In that case the zero set consists of exactly one affine line with \(p\) frequencies, and no isolated zeros occur outside it.

For the standard complete set of \(p+1\) quadratic-chirp mutually unbiased bases, a state with computational support \(R\) and four equally sized nonzero amplitudes has total basis-support size
\[
S=p^2+4-Z(F).
\]
Its sharp minimum for the prescribed four-element support is therefore \(p^2-p+4\) in the centrally symmetric case, and \(p^2+2\) otherwise.

## Assumptions and scope
The prime \(p\) is odd and at least five. The field is \(\mathbb F_p\), not a composite residue ring. Exactly four coefficients are nonzero and their **absolute values are equal**, but phases are unrestricted complex numbers. Scaling the coefficients by any common nonzero scalar has no effect on zeros, so normalize \(|c_t|=1\). The Fourier convention displayed above is unnormalized; all zero claims are invariant under nonzero scalar normalization and conjugating the sign convention.

The standard quadratic-chirp bases may be defined by their overlaps with \(\psi=(c_t)_t\): computational coordinates together with \(p\) other bases whose coordinate amplitudes, up to nonzero scalar and conjugation, are precisely \(F(a,b)\) for \((a,b)\in\mathbb F_p^2\). Their mutual unbiasedness follows by the usual odd-prime quadratic Gauss-sum evaluation. In particular, \(S=4+(p^2-Z)\) without any probabilistic approximation.

## Proof
**Four-unit cancellation.** If four complex unit numbers \(z_1,z_2,z_3,z_4\) sum to zero, they split into two opposite pairs. Indeed, the monic polynomial with those roots has first elementary symmetric coefficient \(e_1=0\). Since all roots have unit modulus, its third coefficient is \(e_3=(z_1z_2z_3z_4)\overline{e_1}=0\). The polynomial is even, so its roots can be paired as \(z,-z\). Every zero of \(F\) therefore realizes at least one of the three perfect matchings of its four support sites.

**One matching means at most one point, or a full line.** Fix a pairing \((t_i,t_j),(t_k,t_l)\). Opposite terms impose
\[
\omega^{a(t_i^2-t_j^2)+b(t_i-t_j)}=-c_{t_j}/c_{t_i},\qquad
\omega^{a(t_k^2-t_l^2)+b(t_k-t_l)}=-c_{t_l}/c_{t_k}.
\]
If either right-hand side is not a \(p\)-th root of unity, this matching contributes no zeros. Otherwise these are two linear equations modulo \(p\). Their determinant is
\[
(t_i-t_j)(t_k-t_l)\big((t_i+t_j)-(t_k+t_l)\big).
\]
Because all sites are distinct, the determinant vanishes precisely when the pair sums agree. A nonparallel matching yields exactly one frequency. A parallel matching yields either none or one entire affine line of \(p\) frequencies. At most one of the three matchings can be parallel: equality of sums for two different matchings would force two sites to coincide, since the characteristic is odd. The presence of one parallel matching is equivalent to central symmetry of \(R\).

**No three isolated zeros.** At most two different matchings can be feasible for a fixed coefficient vector. If all three were feasible, each pairwise coefficient ratio required by a matching would lie in \(-\mu_p\), where \(\mu_p\) denotes the \(p\)-th roots of unity. In particular, matching \((12)(34)\) requires \(c_1/c_2\in-\mu_p\), and matching \((13)(24)\) requires \(c_2/c_4\in-\mu_p\). Their product gives \(c_1/c_4\in\mu_p\), whereas matching \((14)(23)\) would require \(c_1/c_4\in-\mu_p\). These sets are disjoint because \(p\) is odd. Thus, whenever no complete line of zeros exists, there are at most two isolated zeros.

**A full line has no extra zero.** Suppose a matching is parallel and feasible. Translate the site variable by the common centre and modulate the coefficients by the character corresponding to one point of its zero line. This maps frequency coordinates invertibly and preserves the number of zeros. We can consequently write \(R=\{-u,-v,v,u\}\), with \(u\ne\pm v\), and take \(c_{-u}=-c_u\), \(c_{-v}=-c_v\), with \(|c_u|=|c_v|=1\). Up to the nonzero constant \(2i\), the transform becomes
\[
F(a,b)=2i\left[c_u\omega^{au^2}\sin(2\pi bu/p)
+c_v\omega^{av^2}\sin(2\pi bv/p)\right].
\]
Every point with \(b=0\) is a zero. If \(b\ne0\) were another zero, equal coefficient moduli would force \(|\sin(2\pi bu/p)|=|\sin(2\pi bv/p)|\). For odd \(p\), this implies \(bu\equiv\pm bv\pmod p\), hence \(u=\pm v\), a contradiction. Therefore exactly the \(p\) points on the line vanish. This proves the upper bounds, the absence of any other zero counts, and the stated equality characterization.

**All claimed counts occur on every fixed support.** Choose a labeling \((t_1,t_2,t_3,t_4)\) so the matchings \((12)(34)\) and \((13)(24)\) are nonparallel, which is possible because at most one matching is parallel. For zero zeros take all four coefficients equal to one: a zero would require a negative ratio between two \(p\)-th roots, impossible for odd \(p\). For exactly one zero take coefficients \((1,-1,i,-i)\): at frequency \((0,0)\) the two displayed opposite pairs cancel; crossing pairs are impossible because \(i\notin\mu_p\). The nonparallel matching then gives only that single zero. For exactly two zeros use \((1,-1,-1,\omega)\). Both matchings \((12)(34)\) and \((13)(24)\) are feasible, each producing one frequency; the third matching is infeasible. The two frequencies are distinct: coincidence would imply that the character phases at the first three sites agree, forcing the frequency to be \((0,0)\) since any three distinct points \((t^2,t)\) on the prime parabola are noncollinear. At the fourth site the extra phase \(\omega\ne1\) then prevents coincidence. Finally, for centrally symmetric \(R\), choose opposite coefficients on each of the two central pairs. Their matching is feasible along a line, yielding exactly \(p\) zeros by the preceding step. This completes the classification, including every quantifier and equality case.

## Verification
The standalone Python 3 checker `artifacts/verify.py` uses integer histograms of cyclotomic exponents, not floating-point near-zero decisions. It tests the zero-, two-, and line-witness coefficients on **every** four-element support for primes \(p\in\{5,7,11,13\}\), and checks the one-zero witness through exact modular equations. It also exhausts every coefficient phase in \(\{\pm\omega^j:0\le j<p\}\) modulo global phase for every four-element support for \(p=5\) and \(p=7\). These independent finite calculations corroborate the proof and are not a substitute for its all-primes argument. Run `python3 artifacts/verify.py`; successful output ends with `FOUR_ATOM_PARABOLA_CHECKS_PASS 104626`.

## Relationship to prior work
Fiorentino and Weigert (2022, arXiv:2209.09817v1) study total support across complete prime-dimensional mutually unbiased bases and establish sharp low-dimensional results, including \(p=5\). Their inspected theorem statements, Section 5, and Appendix do not give the equal-amplitude, fixed-four-site, all-prime zero-spectrum dichotomy. Their two-site support minimizers are distinct from this four-site theorem.

Li (arXiv:2609.16030v1, September 2026) proves a broader **unrestricted-coefficient** finite-parabola bound \(Z\le p+2\) for four sites and demonstrates sharpness over that unrestricted class. That inequality does **not** imply the present stronger restricted bound \(Z\le p\), the sharp drop to at most two on nonsymmetric four-site supports, or the complete phase-only zero spectrum. The full preprint was not accessible for detailed comparison; its precise four-site equality discussion is a residual priority risk, not a claim that the whole paper was checked.

Two closely related published mathematical records treat (a) equal-amplitude four-point Fourier sums on a **one-dimensional prime cycle** and (b) equal-amplitude four-point sums on a **Cartesian rectangle** in a finite product group. Their full mathematical statements and proofs were inspected. The former has only one frequency parameter and cannot by itself establish the all-slope parabola zero-line law. The latter factors over a parallelogram of four sites; four distinct points \((t^2,t)\) on the odd-prime parabola have **no** affine parallelogram, so its rectangular factorization does not cover this setting. The distinguishing geometric criterion and exact restricted bound remain substantive.

## Limitations
The result applies only to four **equal-magnitude** coefficients on the standard prime parabola. With unequal magnitudes, the extra off-line zeros permitted by the broader \(p+2\) bound can occur. Nothing is claimed for other support sizes, arbitrary conics, composite cyclic rings, or incomplete collections of mutually unbiased bases. Independent mathematical validation has not been performed. An equivalent equal-magnitude specialization in inaccessible sections of the September/October 2026 finite-parabola work remains the principal unresolved originality risk.

## References
1. V. Fiorentino and S. Weigert, *Uncertainty relations for the support of quantum states*, arXiv:2209.09817v1 (first public September 20, 2022), *Journal of Physics A* **55** (2022), 495305, DOI: 10.1088/1751-8121/aca9a4. Full OA journal PDF: https://eprints.whiterose.ac.uk/194248/7/Fiorentino_2022_J._Phys._A_Math._Theor._55_495305.pdf.
2. D. Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola*, arXiv:2609.16030v1 (first public September 11, 2026); revised title *Sharp Total-Support Uncertainty for the Standard Complete Set of Mutually Unbiased Bases*, arXiv:2609.16030v2 (October 3, 2026). Only available abstract and related indexed mathematical descriptions inspected for the relevant four-point implications.
3. *Phase-only four-sparse uncertainty over prime cyclic groups*, published-finding corpus scientific record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-phase-only-four-sparse-uncertainty-over-prime-cyclic-groups--def07c3297e4 (full `RESULT.md` inspected).
4. *Phase-only Fourier-zero spectrum of a four-point rectangle on cyclic product groups*, published-finding corpus scientific record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-phase-only-fourier-zero-spectrum-of-a-four-point-rectangle-on-cy--b51ecb1779fe (full `RESULT.md` inspected).
