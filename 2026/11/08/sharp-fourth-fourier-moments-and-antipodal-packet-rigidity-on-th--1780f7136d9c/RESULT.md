# Sharp fourth Fourier moments and antipodal packet rigidity on the prime-square modular hyperbola

## Finding
For every odd prime \(p\), put \(R=\mathbb Z/p^2\mathbb Z\) and let \(R^\times\) be its units. Define the modular hyperbola \(H=\{(x,x^{-1}):x\in R^\times\}\subset R^2\). Given arbitrary complex coefficients \(a=(a_x)_{x\in R^\times}\), define the unnormalized extension polynomial
\[
E_a(u,v)=\sum_{x\in R^\times}a_x\exp\!\left(\frac{2\pi i(ux+vx^{-1})}{p^2}\right),\qquad (u,v)\in R^2,
\]
and let the output use probability counting measure \(p^{-4}\sum_{u,v\in R}\). Then the following sharp fourth-moment inequality holds:
\[
\boxed{\frac1{p^4}\sum_{u,v\in R}|E_a(u,v)|^4\le\frac{3p}{2}\left(\sum_{x\in R^\times}|a_x|^2\right)^2.}
\]
**All nonzero equality cases are completely classified.** There is a residue representative \(r\in\{1,\ldots,(p-1)/2\}\), a frequency \(\ell\in\mathbb F_p\), and constants \(A,B\in\mathbb C\) with \(|A|=|B|>0\) such that
\[
a_{r+pk}=A\exp(2\pi i\ell k/p),\quad
 a_{-r+pk}=B\exp(2\pi i\ell k/p)\qquad(k\in\mathbb F_p),
\]
where the subscripts are interpreted modulo \(p^2\), and \(a_x=0\) outside these two opposite residue classes. Conversely all these vectors attain equality. Distinct choices of the antipodal residue pair and the within-packet frequency determine disjoint projective optimizer families; the relative phase \(B/A\) is free on the unit circle.

There is also a quantitative coarse deficit, obtained without an asymptotic limit. For \(r\in\mathbb F_p^\times\) set \(t_r=\sum_{k\in\mathbb F_p}|a_{r+pk}|^2\); index antipodal pairs by \(j\) and write \(T_j=t_r+t_{-r}\). With \(S=\sum_r t_r\),
\[
\boxed{\frac{3p}{2}S^2-\frac1{p^4}\sum_{u,v}|E_a(u,v)|^4
\ge\frac p2\sum_{\{r,-r\}}(t_r-t_{-r})^2+(3p-6)\sum_{i<j}T_iT_j.}
\]
Thus any near-maximizer must concentrate on one opposite pair and nearly balance the squared masses in that pair; the full equality analysis additionally enforces a common single Fourier mode.

## Assumptions and scope
The modulus is exactly the square of any odd prime; the ring is not the field \(\mathbb F_{p^2}\). All complex coefficient arrays are allowed, including those with zeros and those of nonconstant magnitude. The output norm is a normalized average; the input \(\ell^2\) norm is unnormalized counting measure. The signed indices \(\pm r+pk\) in the optimizer formula are taken in \(R\), so the negative residue block is indexed from \(-r\), not from the canonical positive integer \(p-r\). The zero coefficient vector satisfies the inequality but is excluded from the nonzero equality classification.

## Proof
**1. Fourier orthogonality and pair-sum geometry.** Let \(M=\frac1{p^4}\sum_{u,v}|E_a(u,v)|^4\). Orthogonality of additive characters on \(R^2\) gives the exact identity
\[
M=\sum_{(s,z)\in R^2}\left|\sum_{\substack{x,y\in R^\times\\x+y=s,\ x^{-1}+y^{-1}=z}}a_xa_y\right|^2.\tag{1}
\]
If \(x+y\) is a unit, then the sum \(s=x+y\) and inverse-sum \(z=s/(xy)\) uniquely determine \(xy=s/z\), also a unit. The unordered pair of residues of \(x,y\) modulo \(p\) is therefore determined by the quadratic polynomial with these sum and product. If the residues are different, its discriminant is a unit; the two roots are uniquely lifted to modulo \(p^2\) in their respective residue classes. Thus any distinct, nonopposite residue pair produces only the two ordered representations \((x,y),(y,x)\), and its total contribution equals \(4t_rt_s\). (If the residues coincide, that fiber is distinguished by discriminant zero modulo \(p\) and is counted below.)

For a fixed nonzero residue \(r\), define \(u_r(k)=a_{r+pk}\) for \(k\in\mathbb F_p\), with signed representatives allowed. The ring identity
\[
(r+pk)^{-1}\equiv r^{-1}-pk r^{-2}\pmod{p^2}
\]
shows that two inputs in the same residue class \(r\) have both coordinate sums determined precisely by \(k+l\in\mathbb F_p\). Their aggregate contribution is \(\|u_r*u_r\|_2^2\), where \(*\) is cyclic convolution on \(\mathbb F_p\).

For one antipodal pair represented by \(r,-r\), the sum of the associated hyperbola points is
\[
(r+pk, (r+pk)^{-1})+(-r+pl,(-r+pl)^{-1})
=(ph,-pr^{-2}h),\quad h=k+l\in\mathbb F_p.
\]
For \(h\ne0\) these sum fibers are distinguished by \(r^2\), so different antipodal pairs do not collide. For \(h=0\), **every antipodal pair meets at the common zero fiber**, independently of \(r\). Moreover a sum is a nonunit in its first coordinate only for antipodal residues, and same-residue and different-nonopposite fibers cannot collide by the quadratic discriminant. These observations partition every ordered pair in (1).

Choose one representative \(r_j\) of each opposite pair, set \(C_j=u_{r_j}*u_{-r_j}\), and \(T_j=t_{r_j}+t_{-r_j}\). The complete exact collision identity is
\[
\boxed{M=\sum_{r\in\mathbb F_p^\times}\|u_r*u_r\|_2^2
+4\sum_{j}\sum_{h\ne0}|C_j(h)|^2
+4\left|\sum_j C_j(0)\right|^2
+4\sum_{i<j}T_iT_j.}\tag{2}
\]
The coefficient four comes from exchanging the two members of each distinct ordered pair. There is no double counting: the squared-norm of \(u_r*u_r\) already includes the two orders within a same-residue pair.

**2. Sharp optimization.** For any sequences \(u,v:\mathbb F_p\to\mathbb C\), unnormalized Fourier inversion and Parseval imply
\[
\|u*v\|_2^2=\frac1p\sum_{\ell\in\mathbb F_p}|\widehat u(\ell)|^2|\widehat v(\ell)|^2
\le p\|u\|_2^2\|v\|_2^2.\tag{3}
\]
Also \(|C_j(0)|\le\sqrt{t_{r_j}t_{-r_j}}\le T_j/2\) by Cauchy--Schwarz and arithmetic--geometric mean. Expanding the zero-fiber term in (2), its cross-terms are bounded by \(8\sum_{i<j}|C_i(0)||C_j(0)|\le2\sum_{i<j}T_iT_j\). Inserting (3) in (2) yields
\[
\begin{aligned}
M&\le p\sum_{\{r,-r\}}\bigl(t_r^2+t_{-r}^2+4t_rt_{-r}\bigr)+6\sum_{i<j}T_iT_j\\
&=\frac{3p}{2}S^2-\frac p2\sum_{\{r,-r\}}(t_r-t_{-r})^2-(3p-6)\sum_{i<j}T_iT_j.
\end{aligned}\tag{4}
\]
The coefficient \(3p-6\) is strictly positive for every odd prime. Dropping the two nonnegative terms establishes the sharp estimate and the stated coarse deficit.

**3. All equality cases and attainment.** Suppose \(a\ne0\) and equality holds in the sharp bound. The strictly positive residual coefficients in (4) force exactly one opposite pair to have nonzero mass, and within it the two masses must be equal and positive. Equality in each self-convolution estimate \(\|u_r*u_r\|_2^2\le p t_r^2\) forces \(|\widehat u_r|^2\) to be supported at a single Fourier frequency: by (3), \(\sum |\widehat u_r|^4\le(\sum|\widehat u_r|^2)^2\), with equality exactly when at most one Fourier coefficient is nonzero. Hence \(u_r(k)\) and \(u_{-r}(k)\) are scalar multiples of additive characters. Equality in the mixed-convolution bound \(\|u_r*u_{-r}\|_2^2\le p t_rt_{-r}\) requires their unique Fourier frequencies to agree. Their scalar amplitudes have equal modulus by the balancing condition. This is precisely the displayed optimizer family.

Conversely, for a fixed antipodal residue pair with \(u_r(k)=A e^{2\pi i\ell k/p}\), \(u_{-r}(k)=B e^{2\pi i\ell k/p}\), and \(|A|=|B|>0\), every inequality used above is an equality: there is no cross-pair interaction, and all three cyclic convolutions lie in one frequency. Thus \(M=(3p/2)S^2\). This also proves sharpness and the full classification. \(\square\)

## Verification
Run `python3 CHECK.py` using Python 3 and its standard library. The checker forms the full hyperbola pair-sum convolution over \(\mathbb Z/p^2\mathbb Z\) for \(p\in\{3,5,7\}\), recomputes (2) independently with residue-class convolutions, checks the sharp inequality on deterministic complex-integer data, and verifies all predicted packet types for each tested prime, including nonzero character frequencies. It prints `PRIME_SQUARE_HYPERBOLA_PASS` on success. Because its residue representatives are the positive integers \(1,\ldots,p-1\), the code correctly places the common zero fiber at convolution index \(p-1\) instead of zero; that shift is absent in the signed-representative formulas in the proof. These finite checks do not replace the all-prime analytical argument.

## Relationship to prior work
González-Riquelme and Oliveira e Silva (2024) develop sharp Fourier extension inequalities on **finite fields** for parabola, paraboloid, hyperbolic paraboloid, and cone surfaces; their results establish a motivating sharp-extension framework, but do not treat the modular hyperbola over the nonfield ring \(\mathbb Z/p^2\mathbb Z\). A sharp fourth-moment result for the multiplicative hyperbola **over a finite field** has constant-modulus full-support optimizers, whereas the present prime-square ring theorem forces precisely two antipodal residue packets. This difference is arithmetic, not a renormalization or a field extension.

Iosevich, Murphy, and Pakianathan (2014) study the same modular hyperbola over finite rings through Fourier decay, Kloosterman sums, and the square-root law. Their inspected statement and theory concern exponential-sum size, not the supremum of the *coefficient-weighted* fourth Fourier moment or its equality cases. Hickman and Wright (2018) develop restriction estimates over composite residue rings, principally for parabolic and moment-curve geometries, without this sharp hyperbola identity. An existing sharp parabolic result over \(\mathbb Z/p^2\mathbb Z\) has one-residue-class Fourier-packet optimizers, in contrast with the paired opposite-class optimizers here. A separate modular-hyperbola result classifies orthogonal restrictions of additive characters, rather than fourth-power extension operator extremizers; its character-packing theorem does not imply (2)--(4).

## Limitations
The bound, mass-defect inequality, and equality classification are proved only for odd-prime-square moduli, not prime cubes, general composite rings, finite fields of order \(p^2\), or higher even moments. The coarse displayed deficit does not quantify the within-packet Fourier dispersion; that rigidity is captured by the equality argument. Literature comparisons do not certify historical priority, particularly against unindexed work on weighted Kloosterman sums. No independent mathematical audit has been performed.

## References
1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, first public 2024-05-26 (Theorems 1.1--1.3 and finite-field scope).
2. A. Iosevich, B. Murphy, and J. Pakianathan, *The square root law and structure of finite rings*, arXiv:1405.7657, first public 2014-05-29 (modular hyperbolas and Kloosterman Fourier decay).
3. J. Hickman and J. Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo \(N\)*, arXiv:1801.03176, first public 2018-01-09 (Sections 2 and 7, ring restriction and moment curves).
4. *Sharp fourth-moment extension on the finite-field multiplicative hyperbola*, published mathematical statement at https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-fourth-moment-extension-on-the-finite-field-multiplicative--0835fe791166 .
5. *Exact parabolic Fourier deficit and extremizer rigidity over prime-square rings*, published mathematical statement at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-parabolic-fourier-deficit-and-extremizer-rigidity-over-pri--227e3af3978b .
6. *Sharp orthogonal exponential capacity and digit-tree rigidity of prime-power modular hyperbolas*, published mathematical statement at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-orthogonal-exponential-capacity-and-digit-tree-rigidity-of--debdea61056e .
