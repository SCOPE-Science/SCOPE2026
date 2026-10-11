# Congruence orbit witnesses and an index-two jump for rim-surgery extendable groups
## Finding
Let \(g\ge3\), let \(a\subset\Sigma_g\) be an oriented nonseparating curve, and put
\[
H=\operatorname{Stab}_{\operatorname{Mod}(\Sigma_g)}(q_0),
\]
where \(q_0\) is the Rokhlin quadratic form of the standard unknotted embedding in \(S^4\). For ordinary untwisted rim surgery along \(a\) using a nontrivial knot \(J\), define
\[
E_+(a)=H\cap\operatorname{Stab}([a]),
\qquad
E_{\pm}(a)=H\cap\operatorname{Stab}(\{[a],-[a]\}).
\]
Niu's exact extendability theorem has the following two quantitative consequences.

First, the marked extendable group is exactly \(E_+(a)\) when \(\Gamma_\mu(J)=\{1\}\), and exactly \(E_{\pm}(a)\) when \(\Gamma_\mu(J)=\{\pm1\}\). These two possibilities differ by a split index-two extension:
\[
E_{\pm}(a)\cong E_+(a)\rtimes C_2.
\]

Second, for every odd prime \(p\), reduction of the rim class modulo \(p\) gives explicit finite congruence witnesses
\[
[H:E_+(a)]\ge p^{2g}-1,
\qquad
[H:E_{\pm}(a)]\ge\frac{p^{2g}-1}{2}.
\]
Equivalently, the \(H\)-orbit of the nonzero class \([a]\bmod p\) is all of \(H_1(\Sigma_g;\mathbb F_p)\setminus\{0\}\), while the orbit of the unordered pair \(\{\pm[a]\bmod p\}\) is the set of all antipodal nonzero pairs.

Thus the longitude-reversal symmetry of the knot exterior contributes exactly one split \(C_2\) to the marked extendable group, and every odd prime yields a finite obstruction to extendability whose orbit size grows as \(p^{2g}\).

## Assumptions and scope
The surface is the ordinary untwisted single-rim-surgery surface \(\Sigma_{g,a,J}\subset S^4\) of Niu's theorem, with \(g\ge3\), \(a\) oriented and nonseparating, and \(J\subset S^3\) nontrivial. All mapping classes are taken under the canonical marking by the standard genus-\(g\) surface.

The group \(\Gamma_\mu(J)\subset\{\pm1\}\) records whether a meridian-preserving diffeomorphism of the knot exterior preserves or reverses the preferred longitude. Since the identity diffeomorphism contributes \(+1\), there are exactly two possibilities:
\[
\Gamma_\mu(J)=\{1\}
\quad\text{or}\quad
\Gamma_\mu(J)=\{\pm1\}.
\]

The congruence statement uses odd primes. The factor \(2\) from squared Dehn twists must be invertible modulo \(p\), and the antipodal pairs \(\{v,-v\}\) must have two distinct elements.

## Proof
Niu's Theorem A states
\[
E(\Sigma_{g,a,J})
=
H\cap\operatorname{Stab}(\Gamma_\mu(J)\cdot[a]).
\]
The two possible values of \(\Gamma_\mu(J)\) therefore give precisely \(E_+(a)\) and \(E_{\pm}(a)\).

For the index-two statement, define
\[
\epsilon:E_{\pm}(a)\longrightarrow\{\pm1\}
\]
by
\[
f_*[a]=\epsilon(f)[a].
\]
This is a homomorphism, and its kernel is \(E_+(a)\). A hyperelliptic involution \(\iota\) of \(\Sigma_g\) acts as \(-I\) on integral first homology. Hence it acts as the identity on \(H_1(\Sigma_g;\mathbb F_2)\), so it preserves \(q_0\), while
\[
\iota_*[a]=-[a].
\]
Thus \(\iota\in E_{\pm}(a)\), \(\epsilon(\iota)=-1\), and \(\iota^2=1\). The sequence
\[
1\longrightarrow E_+(a)
\longrightarrow E_{\pm}(a)
\stackrel{\epsilon}{\longrightarrow} C_2
\longrightarrow1
\]
therefore splits.

Now fix an odd prime \(p\), and write
\[
V=H_1(\Sigma_g;\mathbb F_p).
\]
Every even power of a Dehn twist acts trivially on first homology modulo \(2\), hence lies in \(H\). If \(c\) is a nonseparating curve with homology class \(v\), then modulo \(p\),
\[
T_c^{2k}(x)=x+2k\langle x,v\rangle v.
\]
Because \(2\) is invertible in \(\mathbb F_p\), powers of squared twists realize every symplectic transvection coefficient. Every nonzero vector of \(V\) has a primitive integral lift represented by a nonseparating curve, so the reduction of \(H\) contains all transvections of \(V\).

These transvections act transitively on \(V\setminus\{0\}\). Indeed, if nonzero \(u,w\in V\) satisfy \(\langle u,w\rangle\ne0\), then the transvection with direction \(w-u\) and coefficient \(\langle u,w\rangle^{-1}\) sends \(u\) to \(w\). If \(\langle u,w\rangle=0\) and \(u\ne w\), choose \(z\) outside the union of the two symplectic hyperplanes orthogonal to \(u\) and \(w\); then \(u\) can be sent to \(z\) and \(z\) to \(w\) by two such transvections. Therefore
\[
|H\cdot([a]\bmod p)|=p^{2g}-1.
\]
Since \(E_+(a)\) fixes \([a]\) integrally, it is contained in the stabilizer of \([a]\bmod p\). Orbit--stabilizer for this finite action gives
\[
[H:E_+(a)]\ge p^{2g}-1.
\]

For the reversible group, \(E_{\pm}(a)\) preserves the antipodal pair \(\{\pm[a]\}\), so it is contained in the stabilizer of \(\{\pm[a]\bmod p\}\). Since \(p\) is odd, each nonzero antipodal class has exactly two elements. Transitivity on nonzero vectors therefore gives
\[
\left|H\cdot\{\pm[a]\bmod p\}\right|
=
\frac{p^{2g}-1}{2},
\]
and hence
\[
[H:E_{\pm}(a)]\ge\frac{p^{2g}-1}{2}.
\]

## Verification
The source's Definition 1.1 and Theorem A were checked directly for the longitude-sign group and the exact extendable-subgroup formula. Corollary 9.1 and its proof were also inspected: the source proves infinite index by following the integral orbit \([a]+2n[b]\) under even Dehn twists, but does not state finite odd-prime congruence orbit sizes.

The split index-two step uses the standard fact that a hyperelliptic involution acts as \(-I\) on integral first homology. Because \(-I\) reduces to the identity modulo \(2\), it preserves the Rokhlin quadratic form \(q_0\).

The bundled verifier constructs the mod-\(p\) symplectic transvection action generated by squared-twist coefficients and exhaustively checks representative finite cases. It returns:

`VERIFY_OK g2_p3=80/80,pairs=40 g2_p5=624/624,pairs=312 g3_p3=728/728,pairs=364`

The finite calculation is only a regression check. The general orbit statement is proved symbolically by the transvection argument above.

## Relationship to prior work
Niu computes the marked extendable subgroup exactly and proves that it has infinite index in the unknotted extendable group. The inspected paper does not state the split index-two relation between the two possible longitude-sign cases, nor odd-prime finite congruence orbit sizes or the displayed quantitative index bounds.

Baykur--Sunukjian study loss of homological symmetry under iterated rim surgeries using projective symplectic stabilizers and relative Seiberg--Witten invariants. Their construction gives a different, multi-step symmetry-breaking mechanism and does not supply these exact single-rim congruence orbit witnesses.

Birman--Hilden theory supplies the standard hyperelliptic involution used to split the sign extension. Targeted searches for finite-congruence, odd-prime, antipodal-orbit, and index-two formulations for Niu's rim-surgery subgroup did not locate an equivalent theorem.

## Limitations
The theorem concerns the marked extendable subgroup of Niu's ordinary untwisted single-rim-surgery surfaces. It does not claim analogous formulas for twist rim surgery or arbitrary knotted surfaces.

The congruence inequalities are lower bounds on subgroup index obtained from finite actions. They are not exact finite indices: the actual subgroups have infinite index in \(H\), as already proved by Niu.

No claim is made that the odd-prime congruence action detects every nonextendable mapping class. It supplies an explicit family of finite obstructions, not a complete finite quotient classification.

## References
1. W. Niu, *Extendable mapping classes of knotted surfaces obtained by rim surgery in \(S^4\)*, arXiv:2605.31383v1, first posted 2026-05-29.
2. R. I. Baykur and N. Sunukjian, *Exotic knottings and symmetries of surfaces in 4-manifolds*, arXiv:2607.27751v1.
3. D. Margalit and R. R. Winarski, *Braid groups and mapping class groups: The Birman--Hilden theory*, Bulletin of the London Mathematical Society 53 (2021), 643--659.
