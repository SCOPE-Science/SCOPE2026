# Arithmetic cusps and explicit rational \(2\)-torsion on the genus-\(1777\) modular curve

## Finding
Let \(N=4800\), and let \(H\subset(\mathbb Z/N\mathbb Z)^\times\) consist of elements congruent to \(\pm1\) modulo \(5\). Work over \(\mathbb Q\) with the canonical modular-curve model \(X=X_H(N)\) and \(Y=X_0(N)\), with the natural degree-two map \(\rho:X\to Y\). Let \(\nu:Y\to X_0(5)\) be the degeneracy map, and let
\[
t(z)=\left(\frac{\eta(z)}{\eta(5z)}\right)^6
\]
be the Hauptmodul of \(X_0(5)\); its simple pole is at the cusp \(\infty\), and it vanishes at the cusp \(0\). Then the following three assertions hold.

**Explicit quadratic function field.** The function field of \(X\), over the stated \(\mathbb Q\)-model, is
\[
\mathbb Q(X)=\mathbb Q(Y)(w),\qquad w^2=t^2+22t+125.
\]
Here \(t\) on \(Y\) denotes \(\nu^*t\). The cover \(\rho\) is geometrically connected and étale.

**Complete arithmetic cusp spectrum.** For each positive divisor \(d\mid N\), put \(g_d=\gcd(d,N/d)\) and \(K_d=\mathbb Q(\zeta_{g_d})\), with \(\zeta_1=1\). The unique closed cusp orbit of \(Y\) of denominator \(d\) has residue field \(K_d\). Its inverse image on \(X\) consists of exactly two closed cusps, both with residue field \(K_d\), if \(5\mid d\), and exactly one closed cusp with residue field \(K_d(\sqrt5)\) if \(5\nmid d\). Therefore the numbers of closed cusps of \(X\), indexed by their residue degrees over \(\mathbb Q\), are

| Residue degree | \(1\) | \(2\) | \(4\) | \(8\) | \(16\) |
|---|---:|---:|---:|---:|---:|
| Closed cusps | 16 | 16 | 24 | 10 | 4 |

In particular, \(X\) has exactly **70 closed cusps**, **16 rational cusps**, and \(288\) geometric cusps.

**Explicit two-torsion class.** Let \(Q(t)=t^2+22t+125\), let \(D\) be the reduced effective divisor on \(Y\) supported on the preimages of the two zeros of \(Q\) on \(X_0(5)\), and put \(B=\nu^*(\infty)\). Both \(D\) and \(B\) have degree \(1920\); \(D\) is supported on \(1920\) distinct geometric points. There is a principal-divisor identity
\[
\operatorname{div}_Y(Q(t))=2D-2B.
\]
Consequently \(\mathcal O_Y(D-B)\) is a **nonzero rational point of order two** on \(\operatorname{Jac}(Y)\), and its associated connected étale double cover is \(\rho\).

## Assumptions and scope
All curves are smooth, projective, connected modular curves over \(\mathbb Q\). The phrase *closed cusp* means one closed scheme point, and its residue degree is the cardinality of its geometric Galois orbit. The rational model is specifically Auffarth's \(X_H(4800)\), not an arbitrary descent of the underlying complex Riemann surface. The two-torsion statement concerns the Jacobian of \(Y=X_0(4800)\), not that of \(X\).

## Proof
**1. Identify the quadratic extension over \(\mathbb Q\).** The subgroup \(H\) is the kernel of the quadratic character induced by \((\mathbb Z/5\mathbb Z)^\times/\{\pm1\}\). The standard forgetful maps of canonical modular curves over \(\mathbb Q\) show that \(X_H(4800)\to X_0(4800)\) is obtained by base change, followed by normalization, from \(X_1(5)\to X_0(5)\). The relevant character modulo \(5\) is nontrivial on \(\Gamma_0(4800)\), so this function-field base change is connected and has degree two.

For the Rogers–Ramanujan continued fraction \(R(q)\), the classical modular identity is
\[
R(q)^{-5}-R(q)^5=t(z)+11,\qquad q=e^{2\pi i z}.
\]
The function \(r=R(q)^5\) generates \(\mathbb Q(X_1(5))\) over \(\mathbb Q(X_0(5))\): the order-five translation quotient of the level-five modular function \(R\) is precisely \(X_1(5)\). Thus
\[
r^2+(t+11)r-1=0,
\qquad
w=r+r^{-1},
\qquad
w^2=(t+11)^2+4=Q(t).
\]
The identity is normalized over \(\mathbb Q\) by its rational \(q\)-expansion at \(\infty\); it is not merely a statement after extending scalars to \(\mathbb C\). Pulling it back to \(Y\) proves the claimed field equation.

**2. Show étaleness and identify the divisor.** The polynomial \(Q\) has two distinct roots (discriminant \(-16\)); they are the two order-two elliptic points of \(X_0(5)\). One way to see this is the standard degree-six \(j\)-formula and its exact factorization
\[
j=\frac{(t^2+250t+3125)^3}{t^5},\quad
(t^2+250t+3125)^3-1728t^5
=(t^2-500t-15625)^2Q(t).
\]
There are no elliptic points of order two on \(Y=X_0(4800)\), since \(4\mid4800\). Thus \(\nu\) has local ramification index two over both order-two elliptic points of \(X_0(5)\). Its degree is
\[
\deg(\nu)=\frac{[\mathrm{SL}_2(\mathbb Z):\Gamma_0(4800)]}{[\mathrm{SL}_2(\mathbb Z):\Gamma_0(5)]}
=\frac{11520}{6}=1920.
\]
Each elliptic point consequently has \(960\) distinct preimages, so \(D\) has \(1920\) distinct geometric supports, all of multiplicity one. The rational function \(Q(t)\) has exactly double zeros along \(D\) and double poles along \(B\). It follows that \(\operatorname{div}_Y(Q(t))=2D-2B\), and the quadratic cover is unramified at every point of \(Y\). Its connectedness implies \(D-B\) cannot be principal: otherwise \(Q(t)\) would be a square in \(\overline{\mathbb Q}(Y)\). Since \(D\) and \(B\) are rational divisors, \(\mathcal O_Y(D-B)\) represents a nontrivial \(\mathbb Q\)-rational two-torsion point.

**3. Determine residue fields at every cusp.** On \(X_0(N)\), the geometric cusps of denominator \(d\mid N\) form one Galois orbit of size \(\varphi(g_d)\), with residue field \(K_d\). Reduction of the denominator to level \(5\) maps a cusp to \(\infty\) precisely when \(5\mid d\), and to \(0\) otherwise.

At \(t=\infty\), the equation \(w^2=Q(t)\) has two rational local branches because \(w/t\) tends to \(\pm1\); each geometric cusp on \(Y\) therefore lifts to two cusps with the same residue field. At \(t=0\), its reduction is \(w^2=125\), hence the residue extension is adjoining \(\sqrt5\). If \(5\nmid d\), then \(g_d\) is a power of two, so \(K_d\) does not contain \(\sqrt5\); the latter quadratic extension is genuinely nonsplit. These rules yield exactly the claimed residue fields.

Finally enumerate the \(42\) divisors of \(4800\). For each \(d\), add two closed orbits of degree \(\varphi(g_d)\) when \(5\mid d\), or one orbit of degree \(2\varphi(g_d)\) otherwise. This produces the displayed table. Its orbit-count sum is \(16+16+24+10+4=70\), while its degree-weighted sum is \(16+32+96+80+64=288\), compatible with the known geometric cusp count.

## Verification
The standalone `check_modular_cusps.py` evaluates the cusp-degree enumeration over all \(42\) divisors of \(4800\), asserts the five counts and weighted total, and verifies the exact polynomial factorization at \(j=1728\) using integer polynomial arithmetic. It additionally compares the two classical modular identities by exact truncated \(q\)-products through order \(15\). The program prints `PASS`. The finite \(q\)-comparison is a cross-check, not a proof of the infinite modular identity, which is classical and separately cited. The function-field and ramification arguments above are proofs independent of a finite enumeration.

## Relationship to prior work
Auffarth proves the genus \(1777\), defines this specific rational model, realizes its double cover of \(X_0(4800)\), and counts \(288\) geometric cusps. The classical Rogers–Ramanujan modular identity and level-five modular-curve description supply the small-level equation; the standard theory of cusps of \(X_0(N)\) supplies the cyclotomic base fields. The statement here adds the **specific quadratic equation on this large curve**, the full arithmetic splitting fields and Galois orbit spectrum of all its cusps, and a concrete rational two-torsion divisor on \(X_0(4800)\). A previously reported three-point covering passport for the same complex curve concerns complex ramification and cusp widths, not these arithmetic fields or the divisor class.

## Limitations
This statement does not classify noncuspidal rational points, compute the full Mordell–Weil torsion of \(\operatorname{Jac}(Y)\), or give a decomposition of the Prym. The rational cusp fields refer to the stated canonical \(X_H(4800)\)-model; another rational twist of the same complex curve may have different fields of definition. The calculations are not an independent priority determination for all unpublished modular-curve computations.

## References
- R. Auffarth, *A completely decomposable modular Jacobian of dimension 1777*, arXiv:2611.16963v1 (first public 2026-11-12), especially Section 2, https://arxiv.org/html/2611.16963v1.
- B. Cais and B. Conrad, *Modular curves and Ramanujan's continued fraction* (2006), especially Sections 1–2, https://virtualmath1.stanford.edu/~conrad/papers/J5final.pdf.
- Computational Algebra Group, *Magma Handbook*, “Cusps and Rational Points,” https://magma.maths.usyd.edu.au/magma/handbook/text/1670.
- E. W. Weisstein, “Rogers–Ramanujan Continued Fraction,” MathWorld, https://mathworld.wolfram.com/Rogers-RamanujanContinuedFraction.html.
