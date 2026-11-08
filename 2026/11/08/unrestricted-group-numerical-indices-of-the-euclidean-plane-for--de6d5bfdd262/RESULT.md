# Unrestricted group numerical indices of the Euclidean plane for every orthogonal subgroup

## Finding

Let \(X=\mathbb R^2\) with its Euclidean norm and let \(G\le O(2)\). Use the signed group numerical radius and unrestricted group numerical index
\[
v_G(T)=\sup_{g\in G}\ \sup_{\|x\|=1}\langle Tgx,x\rangle,\qquad
n_G(X)=\inf_{\|T\|=1}v_G(T).
\]
No absolute values are inserted in the inner product; in particular a numerical index can be negative if the group omits negative scalar multiplication. These are the definitions of Dantas, del Río and Raunig (Reference 1).

For each integer \(m\ge1\), write \(\omega=\exp(2\pi i/m)\), let \(C_m=\{z\mapsto\omega^k z:0\le k<m\}\), and let \(D_m=\{z\mapsto\omega^k z,\ z\mapsto\omega^k\bar z:0\le k<m\}\). Put \(c_m=\cos(\pi/m)\); note \(c_1=-1\). Then
\[
\boxed{n_{C_m}(\mathbb R^2)=c_m,\qquad n_{D_m}(\mathbb R^2)=\frac{1+c_m}{2}.}
\]
Every finite subgroup of \(O(2)\) is conjugate to one of these, and every infinite subgroup has \(\boxed{n_G(\mathbb R^2)=1}\). The latter value is attained by every norm-one real-linear operator.

A complete description of finite-group extremizers is as follows. Identify the plane with \(\mathbb C\), and write uniquely \(Tz=az+b\bar z\). Then \(\|T\|=|a|+|b|\). For \(C_m\), the norm-one minimizers are precisely \(b=0\), \(|a|=1\), \(\arg a\equiv\pi/m\pmod{2\pi/m}\). For \(D_m\), they are precisely \(|a|=|b|=1/2\) and \(\arg a\equiv\arg b\equiv\pi/m\pmod{2\pi/m}\). Thus all dihedral minimizers are rank one, whereas all cyclic minimizers are invertible conformal maps, except that the trivial-group case is also invertible.

There is an exact norm-deficit identity, not merely a value of an infimum. Define
\[
h_m(w)=\max_{0\le k<m}\operatorname{Re}(w\omega^k),\quad A=|a|,\quad B=|b|,
\quad d_a=h_m(a)-c_m A,\quad d_b=h_m(b)-c_m B.
\]
Both angular deficits are nonnegative. For \(T\ne0\), with \(N=A+B\),
\[
\frac{v_{C_m}(T)}N-c_m
=\frac{(1-c_m)B+d_a}{N},
\]
and
\[
\frac{v_{D_m}(T)}N-\frac{1+c_m}{2}
=\frac1N\max\left\{\frac{1-c_m}{2}(B-A)+d_a,\ 
\frac{1-c_m}{2}(A-B)+d_b\right\}
\ge\frac{1-c_m}{2}\frac{|A-B|}{N}.
\]
The inequalities are sharp and quantify why any near-minimizing dihedral sequence must have almost equal conformal and anticonformal coefficient moduli. The previously known rank-one infimum is \((1+c_m)/2\) for both groups (Reference 2); hence the exact rank-one versus unrestricted gap is \((1-c_m)/2\) for \(C_m\) and zero for \(D_m\).

## Assumptions and scope

All operators are **real-linear** bounded maps on the Euclidean real plane. All groups are arbitrary subgroups of the full real orthogonal group, not necessarily closed. A group action is by the canonical representation on \(\mathbb R^2\), and the supremum in \(v_G\) is signed rather than absolute. The index minimizes over **all** real-linear operators of norm one, including full-rank and rank-one maps. For \(m=1\), the cyclic group is trivial and the dihedral group contains a single reflection; all formulas, including \(n_{C_1}=-1\), apply without exceptions. For a finite subgroup conjugate to \(C_m\) or \(D_m\), the listed extremizers are conjugated by the same orthogonal change of coordinates.

## Proof

**1. Conformal decomposition and operator norm.** Every real-linear \(T:\mathbb C\to\mathbb C\) uniquely has \(Tz=az+b\bar z\) for complex \(a,b\). By the triangle inequality, \(\|T\|\le|a|+|b|\). On the unit circle, choose the phase of \(z^2\) so that \(az\) and \(b\bar z\) align (with zero-coefficient cases immediate); equality holds, so \(\|T\|=|a|+|b|\). Its real determinant is \(|a|^2-|b|^2\), and a nonzero \(T\) has rank one precisely when \(|a|=|b|\).

**2. Exact numerical radius.** For \(|z|=1\), direct substitution gives
\[
\langle T(\omega^kz),z\rangle=\operatorname{Re}(a\omega^k+b\omega^{-k}\bar z^2).
\]
The maximum over \(z\) is \(\operatorname{Re}(a\omega^k)+|b|\). Similarly,
\[
\langle T(\omega^k\bar z),z\rangle=\operatorname{Re}(a\omega^k\bar z^2+b\omega^{-k}),
\]
whose maximum over \(z\) is \(|a|+\operatorname{Re}(b\omega^{-k})\). The exponents \(k\) run through a symmetric set modulo \(m\). Hence the **exact, unnormalized** formulas are
\[
\boxed{v_{C_m}(T)=B+h_m(a),\qquad
v_{D_m}(T)=\max\{B+h_m(a),A+h_m(b)\}.}
\]
These formulas also handle \(m=1\), where \(h_1(w)=\operatorname{Re}w\).

**3. Angular bound and equality.** Every point of the circle lies within angular distance at most \(\pi/m\) of an \(m\)-th root of unity. Since cosine decreases on \([0,\pi]\),
\[
h_m(w)\ge c_m|w|.
\]
For nonzero \(w\), equality occurs exactly if the argument of \(w\) lies halfway between adjacent roots, namely \(\arg w\equiv\pi/m\pmod{2\pi/m}\). This remains valid for \(m=1\), since the unique root is \(1\) and the farthest angle is \(\pi\).

**4. Cyclic index and all minimizers.** By Step 3,
\[
v_{C_m}(T)\ge B+c_m A=c_m(A+B)+(1-c_m)B.
\]
Here \(1-c_m>0\) for every finite \(m\), and equality with the lower index \(c_m\) at \(A+B=1\) forces \(B=0\) and the angular equality for \(a\). These conditions conversely attain \(c_m\).

**5. Dihedral index, all minimizers and exact defect.** Step 3 yields
\[
v_{D_m}(T)\ge\max\{B+c_m A,A+c_m B\}
=\frac{1+c_m}{2}(A+B)+\frac{1-c_m}{2}|A-B|.
\]
Thus any unit-norm index minimizer has \(A=B=1/2\). At this balance both terms in the radius formula must attain their angular lower bounds, forcing the halfway-phase conditions for \(a\) and \(b\). Conversely they yield the claimed value. Retaining the two nonnegative angular defects instead of discarding them gives the asserted exact formula and sharp modulus-imbalance lower bound.

**6. Arbitrary orthogonal subgroups.** Each finite subgroup of \(O(2)\) consists of a cyclic rotation subgroup \(C_m\), possibly extended by a reflection; an orthogonal coordinate change conjugates the reflection to complex conjugation, giving \(C_m\) or \(D_m\). Conjugation does not change either \(\|T\|\) or \(v_G(T)\) after conjugating \(T\) as well. If \(G\) is infinite, its rotation subgroup is infinite, hence dense in the circle (closed subgroups of the circle are finite cyclic or the full circle). The supremum over rotations in Step 2 becomes \(B+\sup_{|\zeta|=1}\operatorname{Re}(a\zeta)=A+B=\|T\|\). Conversely \(\langle Tgx,x\rangle\le\|T\|\) for every isometry \(g\) and unit \(x\). Therefore \(v_G(T)=\|T\|\) for every \(T\), proving the infinite-group claim.

**7. Rank-one boundary, without claiming its index as new.** Rank one is equivalent to \(A=B=1/2\) under unit normalization. Both the cyclic and dihedral radius formulas then give an infimum \((1+c_m)/2\), achieved when both relevant phases are midpoint directions. This agrees with the earlier rank-one computation (Reference 2) and establishes, by comparison with the unrestricted formulas already proved, the cyclic gap and dihedral equality.

## Verification

The companion `checker.py` independently constructs each finite rotation/reflection matrix, converts arbitrary conformal coefficients to a real \(2\times2\) matrix, and computes the largest eigenvalue of the symmetric part of each composed matrix. It compares this spectral calculation with the exact scalar formulas, tests the sharp bounds and the minimizer witnesses for \(1\le m\le13\), and verifies the rank-one coefficient condition on random rank-one matrices. It passed **11,998 finite diagnostic assertions** with a fixed pseudorandom seed. The code requires Python with NumPy and runs as `python checker.py`. Its tests are not a proof for all group orders, all operators or infinite groups; Steps 1–7 above are the analytical proof.

## Relationship to prior work

Dantas, del Río and Raunig (Reference 1), Definition 4.12 and equation (4.4), introduce the group numerical radius/index; Corollary 3.6 classifies the qualitative finite-dimensional group Daugavet property, and Section 4.3 proves general implications from transitivity and the Daugavet equation. The cited paper does not give the finite cyclic/dihedral unrestricted index values or extremizer classification above. The infinite-subgroup value agrees with the qualitative transitivity mechanism and is included for a complete classification, not claimed as an independent advance.

The earlier orthogonal-action rank-one result in Reference 2 already computes the orbit-covering constant \(\cos(\pi/m)\), the **rank-one** group numerical-radius infimum \((1+\cos(\pi/m))/2\), and associated rank-one Daugavet deficits. None of those inputs is claimed new here. Crucially, the earlier claim expressly does **not** assert unrestricted indices. The present full-operator minimization produces the smaller cyclic value and shows that reflection symmetry restores the rank-one value; it also specifies all unrestricted minimizers and an exact nonnegative defect decomposition.

A related published record (Reference 3) compares rank-one and full numerical indices in regular-octagonal **non-Euclidean** norms. Its norm geometry and operator functional are different and do not imply these group-action Euclidean formulas. The novelty comparison is statement-specific, not based on distinct titles alone.

## Limitations

The result concerns the **real plane** and canonical orthogonal actions, not higher-dimensional Euclidean spaces, non-Euclidean Banach norms, or complex-linear and complex-conjugate actions. Qualitative stability is expressed through a sharp modulus-imbalance defect; no uniform sharp angular stability constant is asserted. Originality is assessed against accessible literature and existing claims; an older unlocated formulation in terms of angular orbit support functions remains a potential priority risk. Independent auditing has not been performed.

## References

1. S. Dantas, H. del Río, T. Raunig, *A group action approach to the Daugavet property*, arXiv:2606.20429 (first public 2026-06-18). https://arxiv.org/abs/2606.20429. Definition 4.12, (4.4), Corollary 3.6, Section 4.3.
2. *Simplex rigidity and exact rank-one Daugavet deficits for finite orthogonal actions*, earlier mathematical research record, claim identifier `aa8b58d9-98af-4f54-86e6-33ffd1b07441`. Rank-one and orbit-covering claims are prior; publication status not asserted.
3. *Maximal rank-one/full numerical-index separation in an octagonal plane family*, research record `2026/10/11/SCOPE-maximal-rank-one-full-numerical-index-separation-in-an-octagonal--693aeb6699ae`; applies to a non-Euclidean octagonal norm, not a group-modified Euclidean index.
