# A regular \((3,40,40)\) Belyi tower on a genus-\(1777\) modular curve

## Finding

**Theorem.** Let \(\Gamma\subset\operatorname{SL}_2(\mathbb Z)\) be the congruence subgroup defined by
\[
\gamma\equiv\lambda I\pmod8,\qquad
\gamma\equiv\pm\begin{pmatrix}1&b\\0&1\end{pmatrix}\pmod3,\qquad
\gamma\equiv\pm I\pmod5,
\]
where the three local choices are independent. Let \(X_\Gamma\) be its compactified complex modular curve. Put
\[
Z_8=\{\lambda I:\lambda\in(\mathbb Z/8\mathbb Z)^\times\},
\qquad Q_8=\operatorname{SL}_2(\mathbb Z/8\mathbb Z)/Z_8.
\]
Then \(\Gamma\) is normal in \(\Gamma_0(3)\), and its inclusion yields a **regular three-point cover**
\[
\pi:X_\Gamma\longrightarrow X_0(3)\simeq\mathbb P^1
\]
of degree \(5760\), with exact deck group
\[
\operatorname{Deck}(\pi)\cong Q_8\times A_5,
\qquad |Q_8|=96.
\]
The three branch points are the unique elliptic point of order \(3\) of \(X_0(3)\) and its two cusps. Their inertia indices are \((3,40,40)\), respectively, and the three fibers consist of \(1920\), \(144\), and \(144\) points. Thus \(X_\Gamma\) is quasiplatonic (admits a regular Belyi map).

The *canonical* modular \(j\)-cover obtained from \(\Gamma\subset\operatorname{SL}_2(\mathbb Z)\), not the different \(j\)-coordinate arising after conjugating \(\Gamma\) to a subgroup of level \(4800\), factors as
\[
X_\Gamma\xrightarrow[5760]{\pi}X_0(3)
\xrightarrow[4]{j}\mathbb P^1.
\]
Its geometric branch-cycle partitions over \(j=0\), \(j=1728\), and \(j=\infty\) are, respectively,
\[
3^{7680},\qquad 2^{11520},\qquad 40^{144}120^{144}.
\]
Its full geometric monodromy group is
\[
Q_8\times A_4\times A_5
\]
of order \(69120\). The regular Galois closure of the canonical \(j\)-cover is a modular curve of genus \(5473\).

## Assumptions and scope

All modular curves, covers, ramification groups, and automorphism groups in this theorem are over \(\mathbb C\). The subgroup \(\Gamma\), its genus \(1777\), its index \(23040\), and the geometric complete decomposability of its Jacobian are taken from Auffarth's construction. The new claims concern its regular Belyi quotient, geometric monodromy, branch-cycle partitions and Galois closure. No arithmetic descent of the particular Belyi quotient and no determination of the *full* automorphism group of the abstract curve are asserted.

## Proof

**1. The normal quotient.** By reduction modulo \(120\) and the Chinese remainder theorem,
\[
\operatorname{SL}_2(\mathbb Z/120\mathbb Z)
\simeq S_8\times S_3\times S_5,
\qquad S_n=\operatorname{SL}_2(\mathbb Z/n\mathbb Z).
\]
The image of \(\Gamma\) is \(H_8\times H_3\times H_5\), where
\[
H_8=Z_8,\quad
H_3=\left\{\pm\begin{pmatrix}1&b\\0&1\end{pmatrix}:b\in\mathbb F_3\right\},\quad
H_5=\{\pm I\}.
\]
The image of \(\Gamma_0(3)\) is \(S_8\times H_3\times S_5\). Both \(H_8\) and \(H_5\) are central in their local groups. Therefore \(\Gamma\triangleleft\Gamma_0(3)\), with quotient
\[
(S_8/H_8)\times(S_5/H_5)
\cong Q_8\times\operatorname{PSL}_2(\mathbb F_5)
\cong Q_8\times A_5.
\]
Using \(|S_8|=384\), \(|H_8|=4\), \(|S_5|=120\), and \(|H_5|=2\) gives degree \((384/4)(120/2)=5760\). Normality makes the covering regular, including after compactification.

**2. The three branch values.** The group \(\Gamma_0(3)\) has index \(4\) in \(\operatorname{SL}_2(\mathbb Z)\), exactly two cusps, and no elliptic point of order \(2\). The matrix \(\begin{pmatrix}-1&-1\\3&2\end{pmatrix}\) lies in \(\Gamma_0(3)\), has trace \(1\), and supplies an elliptic point of order \(3\). The modular genus formula forces exactly one such point and genus zero: \(X_0(3)\cong\mathbb P^1\).

Every \(\gamma\in\Gamma\) has trace congruent modulo \(8\) to \(2\lambda\) for odd \(\lambda\); thus it has no elliptic elements, whose possible traces in \(\operatorname{SL}_2(\mathbb Z)\) are \(0\) and \(\pm1\). The unique base elliptic point consequently has ramification index \(3\) in \(\pi\).

For a cusp represented by the first column \((a,c)^\mathsf T\) of \(g\in\operatorname{SL}_2(\mathbb Z)\), the conjugate of the translation \(T^k\) is
\[
g\begin{pmatrix}1&k\\0&1\end{pmatrix}g^{-1}
=\begin{pmatrix}1-kac&ka^2\\-kc^2&1+kac\end{pmatrix}.
\]
Primitivity of \((a,c)\) forces \(8\mid k\) for the matrix to be scalar modulo \(8\), and \(5\mid k\) for it to be scalar modulo \(5\). The upper-triangular condition modulo \(3\) adds \(3\mid k\) precisely when \(c\not\equiv0\pmod3\). Therefore the \(\Gamma\)-cusp widths are \(40\) for \(c\equiv0\pmod3\) and \(120\) otherwise. The corresponding \(\Gamma_0(3)\)-cusp widths are \(1\) and \(3\), respectively. Both relative ramification indices equal \(40\). Since \(\pi\) has degree \(5760\), each cusp has \(5760/40=144\) points above it and the elliptic point has \(5760/3=1920\) points. No other branch points exist: the interior uniformization is unramified away from elliptic stabilizers. Thus the branch partition is \((3^{1920},40^{144},40^{144})\), proving regular Belyi structure.

The Riemann--Hurwitz computation is
\[
2g(X_\Gamma)-2
=-2(5760)+1920(3-1)+2\cdot144(40-1)
=3552,
\]
so \(g(X_\Gamma)=1777\), independently reproducing the known genus.

**3. Canonical \(j\)-monodromy and Galois closure.** The canonical modular \(j\)-cover has degree \(4\cdot5760=23040\). Because \(\Gamma\) has no elliptic elements, the ramification indices over the order-three and order-two orbifold points of the \(j\)-line are \(3\) and \(2\) everywhere. Its two cusp families give the third partition in the theorem.

The geometric monodromy of the coset action of \(\operatorname{SL}_2(\mathbb Z)\) is the finite quotient by the normal core of \(\Gamma\). Locally, the subgroups \(H_8\) and \(H_5\) are central; the core of \(H_3\) in \(\operatorname{SL}_2(\mathbb F_3)\) is exactly \(\{\pm I\}\): conjugating upper to lower unipotents makes the intersection scalar. Hence the core has image \(H_8\times\{\pm I\}\times H_5\), of order \(4\cdot2\cdot2=16\), in the group of size \(1105920\). Its quotient is
\[
Q_8\times\operatorname{PSL}_2(\mathbb F_3)
\times\operatorname{PSL}_2(\mathbb F_5)
\cong Q_8\times A_4\times A_5,
\]
of order \(96\cdot12\cdot60=69120\). The index-\(69120\) normal-core curve gives the regular Galois closure. It has no elliptic points and all cusp widths \(120\) (each local scalar constraint forces translation exponents divisible by \(8\), \(3\), and \(5\)). Thus its number of cusps is \(69120/120=576\), and its genus is
\[
1+\frac{69120}{12}-\frac{576}{2}=5473.
\]
This also verifies the three branch partitions by Riemann--Hurwitz for the original \(j\)-cover. \(\square\)

## Verification

The standalone file `verify_modular_belyi.py` enumerates the exact finite matrix groups \(S_8\), \(S_3\), and \(S_5\) without external packages. It checks the local subgroup and normal-core sizes \((4,6,2)\) and \((4,2,2)\), respectively; enumerates primitive vectors, local orbits and their cusp widths; checks the \(40^{144}120^{144}\) distribution; and verifies both genus formulas, the regular-cover Riemann--Hurwitz identity, and the monodromy/core orders. All assertions pass under Python 3. The infinite modular-curve statements are established by the group-theoretic proof, not by sample computations.

## Relationship to prior work

Auffarth, *A completely decomposable modular Jacobian of dimension 1777* (arXiv:2611.16963v1, November 12, 2026), defines this exact subgroup and establishes its index \(23040\), cusp count \(288\), genus \(1777\), and completely decomposable geometric Jacobian. The regular \(X_0(3)\)-quotient, signature \((3,40,40)\), precise deck group, full \(j\)-monodromy, and genus of its Galois closure are not stated there. Their derivation uses classical modular-cover theory and does not replace any part of the author's Jacobian-isogeny proof.

Paulhus and Sutherland, *Completely decomposable modular Jacobians* (arXiv:2502.16007, 2025), concerns a much broader search for modular curves with decomposable Jacobians; it does not give the precise three-point regular quotient of the newly defined genus-\(1777\) curve. General modular Belyi and regular-dessin constructions provide background, but the exact quotient and numerical signature here require the subgroup and normal-core calculation.

## Limitations

The displayed group is the exact deck group **of this specific regular map**, not a determination of the full automorphism group of \(X_\Gamma\). The theorem does not assert a \(\mathbb Q\)-model for this particular Belyi map or for its Galois closure, does not construct explicit rational-function equations for the three-point map, and does not supply an independent verification of the previously published Jacobian decomposition. Older modular-curve tables or unpublished subgroup computations could contain an equivalent Belyi signature, so absolute publication priority is not certified.

## References

1. Robert Auffarth, *A completely decomposable modular Jacobian of dimension 1777*, arXiv:2611.16963v1 (first posted November 12, 2026), https://arxiv.org/html/2611.16963v1.
2. Jennifer Paulhus and Andrew V. Sutherland, *Completely decomposable modular Jacobians*, arXiv:2502.16007 (first posted February 21, 2025), https://arxiv.org/abs/2502.16007.
3. LMFDB reviewed knowledge entry, *Modular curve*, https://www.lmfdb.org/knowledge/show/modcurve.
