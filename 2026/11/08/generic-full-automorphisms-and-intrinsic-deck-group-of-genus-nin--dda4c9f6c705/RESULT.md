# Generic full automorphisms and intrinsic deck group of genus-nine hyperelliptic Klein covers

## Finding

For five pairwise distinct parameters \(a_1,\ldots,a_5\in\mathbb C\setminus\{0,1\}\), let \(C_a\) be the smooth projective model of
\[
 y^2=F_a(t):=\prod_{j=1}^5\big((t^2+1)^2-4a_jt^2\big).
\]
There is a nonempty Zariski-open subset of this parameter space on which the **full geometric automorphism group** is
\[
 \operatorname{Aut}_{\mathbb C}(C_a)=\langle\kappa,s,r\rangle\cong(\mathbb Z/2\mathbb Z)^3,
\]
where
\[
\kappa(t,y)=(t,-y),\qquad s(t,y)=(-t,-y),\qquad r(t,y)=(1/t,-y/t^{10}).
\]
The subgroup \(K=\langle s,r\rangle\) is then **intrinsically characterized** as the subgroup consisting of the identity together with all fixed-point-free involutions. In particular, the unmarked genus-nine curve uniquely determines its unramified degree-four Klein quotient of genus three, and the corresponding forgetful map from this component of the moduli of unramified Klein covers to \(\mathcal M_9\) is generically injective onto its image.

This is an exact geometric statement on a nonempty Zariski-open set, **not** an assertion for every parameter tuple, and not an assertion about the smaller locus of curves lying on very general polarized abelian surfaces.

An explicit rational point of that open set is \(a=(2,3,4,5,6)\): this particular curve also has geometric automorphism group exactly \((\mathbb Z/2)^3\).

## Assumptions and scope

The base field is \(\mathbb C\); curves are smooth projective and automorphisms are geometric. The parameter space is the complement of coordinate diagonals and the hyperplanes \(a_i=0,1\) in \(\mathbb A^5\). Smoothness follows because \(x(t)=(t^2+1)^2/(4t^2)\) is a degree-four quotient of \(\mathbb P^1_t\) branched only over \(x=0,1,\infty\), while the five \(a_i\) are distinct and avoid these branch values. Thus \(F_a\) has twenty distinct roots and \(C_a\) has genus nine.

The étale Klein covering is explicitly given by
\[
H_a:\ v^2=x(x-1)\prod_{j=1}^5(x-a_j),\qquad
x=\frac{(t^2+1)^2}{4t^2},\quad
v=\frac{(t^4-1)y}{128t^7}.
\]
The genus of \(H_a\) is three. The formulas for \(s\) and \(r\) preserve both \(x\) and \(v\), are commuting involutions and have no fixed points on the smooth model. Therefore \(C_a\to H_a\) is a degree-four unramified Galois covering with deck group \(K\).

## Proof

**1. Explicit octic symmetry.** Every factor \((t^2+1)^2-4a_jt^2\) is even and reciprocal of degree four. Hence \(F_a(-t)=F_a(t)\) and \(F_a(1/t)=t^{-20}F_a(t)\). The three specified maps extend to involutions of the smooth compactification, commute, and generate a subgroup of order eight. A direct substitution in \(x,v\) gives their asserted action on the quotient.

**2. Fixed-point profile and the free Klein subgroup.** The hyperelliptic involution \(\kappa\) fixes exactly the twenty branch points. The involution \(s\) has no fixed point: over \(t=0,\infty\) it exchanges the two points in each fiber; similarly \(r\) has fixed base points \(t=\pm1\) but exchanges the two points there, while \(sr\) has fixed base points \(t=\pm i\) and exchanges the two points there. Since \(a_i\notin\{0,1\}\), these are all unramified fibers. Conversely \(\kappa s,\kappa r,\kappa sr\) each fix exactly four points, above \(0,\infty\), \(\pm1\), and \(\pm i\), respectively. Thus, **provided the full automorphism group equals this eight-element group**, its precisely three nonidentity fixed-point-free involutions are \(s,r,sr\). This identifies \(K\) without marked involutions and identifies \(H_a\) as the intrinsic quotient.

**3. A characteristic-719 full-stabilizer certificate.** Specialize \(a=(2,3,4,5,6)\) and reduce modulo \(719\). The twenty branch points of \(F_a\) split into twenty distinct \(\mathbb F_{719}\)-points; the exact complete list is
\[
\{9,22,58,62,80,98,313,317,323,325,394,396,402,406,621,639,657,661,697,710\}.
\]
A projective linear transformation over \(\overline{\mathbb F}_{719}\) preserving this set is completely determined by the images of any ordered three distinct points. Since all twenty branch points are rational, the image triple consists of rational points; therefore the unique projectivity lies in \(\operatorname{PGL}_2(\mathbb F_{719})\). Enumerating all \(20\cdot19\cdot18=6840\) image triples with exact modular arithmetic and testing the entire set gives exactly the four projectivities
\[
 t\longmapsto t,\quad -t,\quad1/t,\quad-1/t.
\]
The accompanying `verify.py` replays the exhaustive enumeration (it reconstructs each projectivity from its three prescribed images using a four-variable kernel and tests all twenty roots). Thus the geometric reduced automorphism group of the characteristic-719 curve is \((\mathbb Z/2)^2\) and its full hyperelliptic automorphism group has order \(8\).

**4. Lifting the bound and generization.** Smoothness and branch separability at \(719\) provide a smooth proper genus-nine model with good reduction over \(\mathbb Z_{(719)}\). After any finite extension of its fraction field, the reduction map on geometric automorphism groups has a kernel of \(719\)-power order. The characteristic-zero Hurwitz bound is \(84(9-1)=672<719\), hence this kernel is trivial; the geometric characteristic-zero group of the specialized curve embeds into the reduction group of order eight. It already contains the eight explicit automorphisms, so its full group is exactly eight.

The automorphism functor of a smooth proper family of stable genus-nine curves is finite and unramified in characteristic zero. Consequently the order of the geometric automorphism group is upper semicontinuous under specialization. Since all members contain the displayed eight-element group and the rational point \(a=(2,3,4,5,6)\) has order eight, a nonempty Zariski-open neighborhood has automorphism group of order exactly eight. As the parameter space is irreducible, this establishes the claimed Zariski-generic equality. The intrinsic recovery of \(K\) then proves generic injectivity of forgetting the Klein action.

## Verification

Run `python3 verify.py` using only the Python standard library. The verifier constructs all branch roots in \(\mathbb F_{719}\), checks that there are twenty, enumerates all ordered image triples, solves every three-point projectivity and tests every root. It confirms the four reduced transformations and prints `CERTIFICATE_OK`. This is a complete finite-field stabilizer computation; the characteristic-zero and generic conclusions use the mathematical specialization and semicontinuity arguments above, not numerical extrapolation.

## Relationship to prior work

Borówka–Grossi–Shatsila (2026, Theorem 1.5) exhibit genus-nine hyperelliptic curves as étale Klein coverings of genus-three curves on polarized abelian surfaces. The present statement concerns the **full five-parameter type-I.1 covering family**, and does not assert a generic result on the smaller abelian-surface subfamily. Borówka–Ortega (2026) classify the four types of Klein covers over genus-three hyperelliptic curves and prove injectivity of their **Prym map**; the full automorphism group and the curve-only forgetful map are different invariants. Borówka–Ortega (2023/2024, Proposition 2.5 and Remark 6.1) supply the Klein involution framework and an equivalent quartic-factor equation; these are acknowledged inputs, not new. Gutierrez–Shaska (2005) develop dihedral invariants and the general locus with extra involutions. The claimed addition is a **proved exact full-automorphism-group statement for this explicit genus-nine family**, including a reproducible single-point characteristic-719 certificate and the resulting intrinsic deck-group reconstruction. The full classical automorphism-group classification is a relevant residual priority risk.

## Limitations

The generic equality is not extended to all parameters; special curves can have extra automorphisms. The genus-nine family does not exhaust the curves embedded in very general \((1,12)\)-polarized abelian surfaces, and the proof does not characterize the automorphism group along that particular sublocus. The finite-field computation is exhaustive only for the named specialization and finite field. Historical priority is provisional, particularly relative to general classification results for hyperelliptic automorphism groups. There has been no independent mathematical validation.

## References

1. P. Borówka, P. Grossi, A. Shatsila, *Hyperelliptic curves on (1,d) abelian surfaces for d≤15*, arXiv:2610.40989v1, 2026-10-29. https://arxiv.org/pdf/2610.40989
2. P. Borówka, A. Ortega, *Klein coverings over hyperelliptic genus 3 curves*, arXiv:2602.18969, 2026-02-21. https://arxiv.org/abs/2602.18969
3. P. Borówka, A. Ortega, *Involutions on hyperelliptic curves and Prym maps*, arXiv:2302.13041v2, 2024-10-30 revision of 2023 original. https://arxiv.org/html/2302.13041v2
4. J. Gutierrez, T. Shaska, *Hyperelliptic curves with extra involutions*, LMS J. Comput. Math. 8 (2005), 102–115. https://doi.org/10.1112/S1461157000000917
