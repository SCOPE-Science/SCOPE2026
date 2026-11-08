# Primitive periodic circles and an essential component-zeta singularity in affine Jordan torus dynamics

## Finding

Let \(d\ge2\), let \(N\) be the integral nilpotent Jordan shift with \(N_{i,i+1}=1\) and all other entries zero, and let \(J_d=I_d+N\). For any translation \(a\in\mathbb T^d=\mathbb R^d/\mathbb Z^d\), consider the invertible affine toral map
\[
T_a(x)=J_dx+a\pmod{\mathbb Z^d}.
\]
Write \(\beta=a_d\in\mathbb T\). For every positive integer \(n\), let \(P_n\) be the number of connected components of \(\operatorname{Fix}(T_a^n)\), and let \(C_n\) be the number of connected components of the set of points with *least* period \(n\). These count circles, not individual periodic points.

If \(\beta\) is irrational, there are no periodic points and \(P_n=C_n=0\) for all \(n\). Otherwise, let \(q\ge1\) be the exact additive order of \(\beta\). Then
\[
\operatorname{Fix}(T_a^n)=\varnothing\quad(q\nmid n),\qquad
P_n=n^{d-1}\quad(q\mid n).
\]
Each nonempty fixed-point set is a disjoint union of exactly \(n^{d-1}\) embedded circles parallel to the first coordinate. The complete primitive-period census is
\[
C_{q\ell}=q^{d-1}J_{d-1}(\ell)
=q^{d-1}\ell^{d-1}\prod_{p\mid\ell}(1-p^{-(d-1)}),
\qquad C_n=0\quad(q\nmid n),
\]
for every integer \(\ell\ge1\), where \(J_s(\ell)=\sum_{r\mid\ell}\mu(\ell/r)r^s\) is the Jordan totient and the empty product is one.

The proportion of the fixed circles at time \(q\ell\) whose points have exact period \(q\ell\) is
\[
\frac{C_{q\ell}}{P_{q\ell}}=\prod_{p\mid\ell}(1-p^{-(d-1)}).
\]
In dimension \(d=2\), its infimum over \(\ell\ge1\) is zero. In *every* dimension \(d\ge3\), its sharp positive infimum is \(1/\zeta(d-1)\), approached through products of consecutive primes (and not attained at any finite \(\ell\)).

Define the **connected-component dynamical zeta series**, using the classical component-count convention,
\[
Z_a(z)=\exp\!\left(\sum_{n\ge1}\frac{P_n}{n}z^n\right).
\]
It is identically one when \(\beta\) is irrational. When \(\beta\) has order \(q\), its analytic expression on \(|z|<1\) is
\[
\boxed{Z_a(z)=\exp\!\left(q^{d-2}\operatorname{Li}_{2-d}(z^q)\right)},
\qquad
\operatorname{Li}_{2-d}(w)=\sum_{r\ge1}r^{d-2}w^r.
\]
The exponent is a rational function with a pole of order \(d-1\) at each \(q\)-th root of unity. Thus \(Z_a\) has an essential singularity at every one of those roots and cannot be meromorphic across them. This component-count zeta is *not* the usual Artin–Mazur point-count zeta, which is not defined here by finite periodic-point counts.

## Assumptions and scope

All statements hold simultaneously for every integer \(d\ge2\), every affine shift \(a\in\mathbb T^d\), every positive iterate \(n\), and every numerator of rational \(\beta\) relatively prime to its exact denominator \(q\). No Diophantine or regularity condition is imposed on the first \(d-1\) shift coordinates. The torus carries its usual quotient topology; a circle means a connected subtorus parallel to the first coordinate, possibly translated. Primary MSC2020: 37C25.

## Proof

**1. Exact iterates.** Since \(N^d=0\), the binomial identity gives
\[
J_d^n=\sum_{k=0}^{d-1}\binom nk N^k,
\qquad
\sum_{r=0}^{n-1}J_d^r=\sum_{k=0}^{d-1}\binom n{k+1}N^k.
\]
The latter uses \(\sum_{r=0}^{n-1}\binom rk=\binom n{k+1}\). Consequently, \(T_a^n(x)=x\) is equivalent to the final-coordinate congruence \(n\beta=0\pmod1\) and, for each \(1\le j\le d-1\), the congruence
\[
\sum_{k=1}^{d-j}\binom nk x_{j+k}
+\sum_{k=0}^{d-j}\binom n{k+1}a_{j+k}=0\pmod1.
\]
These equations do not contain \(x_1\). In the variables \((x_2,\ldots,x_d)\), their linear part is an upper-triangular integral matrix with all \(d-1\) diagonal entries equal to \(n\) and determinant \(n^{d-1}\). The associated torus endomorphism is onto with a kernel of precisely \(n^{d-1}\) points (by the lattice index of its integer matrix). Thus whenever \(n\beta=0\), the inhomogeneous equations have exactly \(n^{d-1}\) solutions in the remaining coordinates. The first coordinate is arbitrary on each solution fiber: precisely \(n^{d-1}\) disjoint circles occur. If \(n\beta\ne0\), there are no solutions. This proves the fixed-component formula and the irrational case.

**2. Exact-period components.** Let \(\Gamma\) be one of the fixed circles for time \(n\). For any \(m\mid n\), the difference \(T_a^m(x)-x\) depends on \(x_2,\ldots,x_d\) but not on \(x_1\). Hence either every point of \(\Gamma\) has period dividing \(m\) or none does. Thus all points of each fixed circle share the same least period, necessarily a divisor of \(n\). Every exact-period set is therefore a union of entire disjoint circles, and
\[
P_n=\sum_{m\mid n}C_m.
\]
For a rational last shift of exact order \(q\), the only nonzero terms have \(q\mid m\). Put \(n=q\ell\) and \(m=qr\). Because \(qr\mid q\ell\) exactly when \(r\mid\ell\), we obtain
\[
(q\ell)^{d-1}=\sum_{r\mid\ell}C_{qr}.
\]
Möbius inversion gives \(C_{q\ell}=q^{d-1}\sum_{r\mid\ell}\mu(\ell/r)r^{d-1}=q^{d-1}J_{d-1}(\ell)\), with the Euler product shown above. In particular, a positive number of primitive circles exists at each positive multiple of \(q\).

**3. Sharp dimension boundary.** Divide the exact count by \((q\ell)^{d-1}\). For \(d\ge3\), the positive convergent Euler product \(\prod_p(1-p^{-(d-1)})=1/\zeta(d-1)\) is a strict lower bound for each finite \(\ell\), and the ratios for primorial \(\ell\) decrease toward that product. For \(d=2\), the corresponding infinite product is zero (Euler's divergence of \(\zeta(1)\)), and the primorial ratios tend to zero. This yields both exact infima.

**4. Zeta and singularities.** Substitution of \(P_n=n^{d-1}\) at multiples of \(q\) gives
\[
\log Z_a(z)=\sum_{r\ge1}\frac{(qr)^{d-1}}{qr}z^{qr}
=q^{d-2}\sum_{r\ge1}r^{d-2}(z^q)^r.
\]
For every nonnegative integer \(k\), \(\sum_{r\ge1}r^k w^r=(w\,d/dw)^k[w/(1-w)]\) is a rational function with a pole of order \(k+1\) at \(w=1\). With \(k=d-2\), the exponent has a pole of order \(d-1\) wherever \(z^q=1\). The exponential of a function with a pole has an essential singularity there (its Laurent expansion contains infinitely many negative powers); hence no meromorphic extension across those points exists. The series converges for \(|z|<1\), where the displayed identity holds.

## Verification

`verify.py` is standalone Python 3 code using only the standard library. Run `python3 verify.py` in the same directory. It independently enumerates all solutions to the exact triangular fixed congruences for 36 rational parameter/dimension cases, checks by literal rational iteration that each solution circle is fixed, determines every tested least period, and compares with the Jordan-totient formula. It also checks 380 coefficients of the logarithmic zeta identity. The observed output was:

`VERIFY_OK dimensions=2..5 exact_parameter_cases=36 exact_circle_representatives=4092 zeta_coefficients=380`

The computation is a finite consistency check. The argument above, not enumeration, establishes all-dimensional claims and the analytic continuation obstruction.

## Relationship to prior work

Corrêa (2026) studies polynomial entropy and rotation sets for torus maps homotopic to the identity. The present nontrivial integral Jordan shear is not homotopic to the identity, so that theorem is motivational background, not a covering result. A related published study of the unipotent Jordan shear calculates sharp Haar volumes of Bowen balls; it does not determine periodic connected components or a component-zeta.

Banerjee, Bhattacharyya, Gongopadhyay, and Mondal (2026), arXiv:2601.15827, analyze reversibility and affine toral automorphisms in dimension two. Their fixed-point criterion (Theorem 4.7) assumes that \(1\) is not an eigenvalue, and their parabolic discussion and entropy result do not provide the all-iterate primitive-circle census. This work instead treats a single integral unipotent Jordan block in every dimension and all translations; it does not claim to improve their reversibility results.

Hasselblatt and Katok's *Handbook of Dynamical Systems* survey (Section 2.5a) already proposes counting connected components when periodic points occur in families, and Section 8.3a describes affine unipotent maps and their known polynomial entropy. Those general ideas are precedents and are not claimed as new. The explicit Jordan-totient census, sharp dimension-dependent primitive fraction, and nonmeromorphic evaluated component-zeta are the assertions tested here for prior coverage. The Byszewski–Graff–Ward survey of Dold sequences concerns systems with finite periodic-point counts in its basic counting setup, so its point-count Möbius relations are not by themselves an evaluated formula for these infinite families. The ordinary lattice-index and Möbius identities used in the proof are standard.

## Limitations

This is a complete result for a **single** integral unipotent Jordan block and arbitrary affine translation, not for general quasi-unipotent integer matrices or block sums. No statement is made about Artin–Mazur zeta functions for these maps; their fixed-point sets are uncountable whenever nonempty. The component-zeta definition follows the cited component-count convention and is not an Euler product over ordinary primitive point-orbits. The methods rely on exact lattice indices and do not establish structural stability under nonlinear perturbations. Connections with broad algebraic and Nielsen periodic-point theory may yield alternative derivations; definitive historical priority and independent validation remain open.

## References

1. H. Corrêa, “Polynomial entropy and rotation sets,” *Archiv der Mathematik* 127 (2026), 389–397, first publicly available 2026-09-12, DOI 10.1007/s00013-026-02286-3. https://doi.org/10.1007/s00013-026-02286-3
2. “Sharp Haar Bowen-ball constants for unipotent Jordan toral dynamics,” public research record first posted 2026-10-11, full mathematical result: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-haar-bowen-ball-constants-for-unipotent-jordan-toral-dynam--ab1c4e92842d
3. K. Banerjee, A. Bhattacharyya, K. Gongopadhyay, and S. Mondal, “Reversibility and symmetry of affine toral automorphisms,” arXiv:2601.15827, first submitted 2026-01-22. https://arxiv.org/abs/2601.15827
4. B. Hasselblatt and A. Katok, “Principal Structures,” *Handbook of Dynamical Systems*, Vol. 1A, Sections 2.5a and 8.3a. https://paperzz.com/doc/7088832/handbook-of-dynamical-systems-volume-1-survey-i
5. J. Byszewski, G. Graff, and T. Ward, “Dold sequences, periodic points, and dynamics,” *Bulletin of the London Mathematical Society* 53 (2021), 1263–1298, DOI 10.1112/blms.12531. https://doi.org/10.1112/blms.12531
