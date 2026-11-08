# Exact singular and arithmetic strata in a Frobenius-twisted cubic linear system

## Finding

Let \(q\) be any prime power, \(k=\mathbb F_q\), and \(K=\mathbb F_{q^3}\). Choose a normal element \(\theta\in K\): its conjugates \(\theta,\theta^q,\theta^{q^2}\) form a \(k\)-basis of \(K\). On \(\mathbb P^2_k\) with coordinates \([X:Y:Z]\), set
\[
\ell=\theta X+\theta^qY+\theta^{q^2}Z,\qquad
\ell_i=\ell^{(q^i)}\quad(i=0,1,2),
\]
where \(\ell^{(q^i)}\) means **Frobenius applied to coefficients**, not the \(q^i\)-th power as a polynomial. For \(a\in K\) and \(d\in k\), put
\[
C_{a,d}:\quad F_{a,d}=
\operatorname{Tr}_{K/k}(a\ell_0^2\ell_1)+d\operatorname{N}_{K/k}(\ell_0)=0.
\]
This is the explicit, Frobenius-descended four-dimensional vector space of cubics from the construction of Asgarli–Ghioca. The projective parameters are \([a:d]\in\mathbb P(K\oplus k)(k)\cong\mathbb P^3(k)\), with simultaneous scaling by \(k^*\).

**Theorem.** The complete distribution of its \(q^3+q^2+q+1\) rational projective members is

| Geometric type | Number of \(k\)-members | Number of \(k\)-points on each member |
|---|---:|---:|
| Smooth, geometrically integral cubic | \(q^3-1\) | Not constant in general |
| Geometrically integral with exactly one ordinary node, \(\operatorname{char}(k)\ne3\), \(q\equiv1\pmod3\) | \(q^2+q+1\) | \(q\) |
| Geometrically integral with exactly one ordinary node, \(\operatorname{char}(k)\ne3\), \(q\equiv2\pmod3\) | \(q^2+q+1\) | \(q+2\) |
| Geometrically integral with exactly one ordinary cusp, \(\operatorname{char}(k)=3\) | \(q^2+q+1\) | \(q+1\) |
| Three distinct conjugate lines, geometrically reducible | \(1\) | \(0\) |

Exactly **one** of the three mutually exclusive singular-integral rows applies for a given \(q\). All geometrically integral singular members have their **unique singular point rational over \(k\)**. For the node rows, the tangent cone has two \(k\)-rational branches precisely when \(q\equiv1\pmod3\).

More explicitly, the only geometrically reducible rational member is \(C_{0,1}\). For \(a\ne0\), a member is geometrically singular exactly when
\[
\boxed{d^3+27\operatorname{N}_{K/k}(a)=0.}
\]
This is a **set-theoretic** equation for rational parameters; no scheme-theoretic multiplicity assertion about the full discriminant is made. It cuts out \(q^2+q+1\) rational points. Together with \([0:1]\), these give precisely the \(q^2+q+2\) singular members.

## Assumptions and scope

Everything is over the finite field \(k=\mathbb F_q\), with \(q\ge2\) any prime power. All geometric singularities and geometric irreducibility are taken over \(\overline{k}\). The defining map \(K\oplus k\to k[X,Y,Z]_3\) is an injective \(k\)-linear map, because after extending scalars to \(K\), the three forms \(\ell_0^2\ell_1,\ell_1^2\ell_2,\ell_2^2\ell_0\) and \(\ell_0\ell_1\ell_2\) are linearly independent and the three \(\ell_i\) are independent linear forms. Thus every projective \([a:d]\) gives one nonzero cubic, with no repeated projective parameters.

The smooth members have genus one. Each geometrically integral singular member has geometric genus zero. The unique geometrically reducible member is a triangle of three \(K\)-lines cyclically conjugated by \(\operatorname{Gal}(K/k)\).

## Proof

**1. Descent and geometric irreducibility.** Make the invertible linear change of coordinates over \(K\)
\[
U=\ell_0,\quad V=\ell_1,\quad W=\ell_2.
\]
Because Frobenius cyclically permutes these linear forms, the defining polynomial becomes
\[
f=aU^2V+bV^2W+cW^2U+dUVW,
\qquad b=a^q,\ c=a^{q^2},\quad abc=\operatorname{N}_{K/k}(a).
\]
If \(a=0\), its zero locus is \(UVW=0\). The three coordinate lines are distinct and conjugate under the descent, with no \(k\)-rational point: if a \(k\)-point annihilates any one \(\ell_i\), applying Frobenius shows that it annihilates all three, contradicting invertibility of the coordinate change.

Suppose \(a\ne0\). Then \(abc\ne0\). The elementary reducibility lemma for cyclic cubics (Asgarli–Ghioca, Lemma 8) says that a geometrically reducible cubic of the displayed form must have \(abc=0\). Hence every such \(C_{a,d}\) is geometrically integral. This published lemma is used only for irreducibility, not for the singularity or point-count calculations below.

**2. Complete singularity criterion.** Because \(abc\ne0\), a singular geometric point cannot lie on a coordinate axis: a point on \(U=0\) lying on the cubic is one of the coordinate vertices, each of which has a nonvanishing partial derivative (and similarly cyclically). Thus any singular point satisfies \(UVW\ne0\).

Write \(A=aU^2V\), \(B=bV^2W\), \(C=cW^2U\), and \(T=dUVW\). Multiplying the three partial derivatives by \(U,V,W\), respectively, gives
\[
2A+C+T=0,\qquad A+2B+T=0,\qquad B+2C+T=0.
\]
The equation of the cubic is \(A+B+C+T=0\). When the characteristic is not three, the coefficient matrix of the first three equations has determinant \(9\ne0\). The unique solution is
\[
A=B=C=-T/3.
\]
All four quantities satisfy the cubic equation. Since \(ABC=abc(UVW)^3\) and \(T=dUVW\), this requires \(d^3=-27abc\). Conversely, that identity forces \(d\ne0\); direct substitution shows that
\[
[U:V:W]=\left[1:-\frac{d}{3b}:-\frac{3a}{d}\right]
\]
is a singular point. It is the unique one, because the derivative equations force the two displayed coordinate ratios.

In characteristic three, the derivative equations give \(B=A+T\) and \(C=A+2T\). In the cubic equation, \(A+B+C+T=T\); hence a singular point forces \(T=0\), so \(d=0\). Conversely, when \(d=0\), the derivative equations reduce to \(A=B=C\), and they possess exactly one solution in the geometric torus up to projective scaling: after setting \(U=1\), this is a cube-root system, and the cube map is bijective in characteristic three. At this point the cubic equation is \(A+B+C=3A=0\). Thus the unique-singularity criterion is again precisely \(d^3+27abc=0\), now interpreted as \(d=0\).

The singular point of every geometrically integral singular member is unique over \(\overline{k}\), so it is fixed by the \(q\)-Frobenius and is \(k\)-rational.

**3. Local geometry and the arithmetic splitting test.** If the characteristic is not three, the three cyclic monomials at the unique singular point all have the same nonzero value \(M\), while \(dUVW=-3M\). Rescaling the local coordinates by their values at the singular point and taking \(W\) as the nonzero projective coordinate, write \(U=U_0(1+s)\), \(V=V_0(1+t)\), \(W=W_0\). Dividing the local equation by \(M\) gives the *exact* identity
\[
(1+s)^2(1+t)+(1+t)^2+(1+s)-3(1+s)(1+t)
=s^2-st+t^2+s^2t.
\]
The quadratic part \(s^2-st+t^2\) factors into distinct lines over \(\overline{k}\) in every characteristic other than three, so the singular point is an ordinary node. The two tangent directions are defined over a field precisely when it contains the primitive cube roots of unity. The local coordinate change is defined over \(K\), an extension of **odd degree three**; therefore a quadratic splitting field over \(k\) is not erased by passage to \(K\). The node is split over \(k\) exactly when \(q\equiv1\pmod3\), including in characteristic two.

In characteristic three, a diagonal coordinate scaling over \(\overline{k}\) makes \(a=b=c=1\) for the singular member \(d=0\), and carries its unique singularity to \([1:1:1]\). In the affine chart \(W=1\), with \(U=1+s\), \(V=1+t\), the local equation is
\[
(1+s)^2(1+t)+(1+t)^2+(1+s)=(s+t)^2+s^2t.
\]
Putting \(r=s+t\) makes it \(r^2+s^2r-s^3\). Its completed-square form is \(r'^2-s^3\cdot\text{unit}\), so it has one branch, multiplicity two and delta invariant one: an ordinary cusp. This also proves geometric genus zero in every singular-integral case, since a plane cubic has arithmetic genus one.

**4. Exact parameter counts.** There are \(|\mathbb P^3(k)|=q^3+q^2+q+1\) rational parameters, with one parameter \([0:1]\) having \(a=0\). If the characteristic is not three, the singular-integral equation forces \(d\ne0\), allowing the unique projective normalization \(d=1\). It becomes
\[
\operatorname{N}_{K/k}(a)=-1/27.
\]
The norm homomorphism \(K^*\to k^*\) is surjective with kernel size \((q^3-1)/(q-1)=q^2+q+1\). In characteristic three the equation forces \(d=0\), and the allowed projective classes are exactly \(K^*/k^*\), again \(q^2+q+1\). Therefore there are \(q^2+q+1\) singular geometrically integral cubics and \(1\) reducible cubic. The remaining number is
\[
(q^3+q^2+q+1)-(q^2+q+1)-1=q^3-1.
\]
Every one of these is smooth by Step 2.

**5. Exact point counts.** The normalization of a geometrically integral singular cubic is a smooth genus-zero curve over \(k\), hence is \(\mathbb P^1_k\), with \(q+1\) rational points. A split rational node identifies two \(k\)-rational preimages, giving \(q+1-2+1=q\) rational points. A nonsplit rational node identifies two nonrational conjugate preimages to one rational singular point, giving \(q+1+1=q+2\). A rational cusp identifies one rational preimage with one rational point, preserving \(q+1\). The geometric triangle \(UVW=0\) has no \(k\)-rational points, as proved in Step 1. This completes all counts.

## Verification

Run \(\texttt{python3 verify\_members.py}\) for exact, exhaustive checks over the prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\). The program constructs a cubic extension and normal element in each case, expands the descended cubic, enumerates all rational projective parameters and plane points, checks the norm criterion, and checks every rational singular point and singular-member point count. Its observed strata are:

| \(q\) | Smooth | Geometrically integral singular | Reducible | Rational points per integral singular member |
|---:|---:|---:|---:|---:|
| 2 | 7 | 7 | 1 | 4 |
| 3 | 26 | 13 | 1 | 4 |
| 5 | 124 | 31 | 1 | 7 |
| 7 | 342 | 57 | 1 | 7 |

Run \(\texttt{python3 verify\_local.py}\) for separate symbolic polynomial identities concerning the singular point, local node and cusp forms, and the determinant-nine derivative system (requires SymPy). The exhaustive finite-field checks are corroborative examples, **not** an exhaustive proof over every prime power: that proof is Steps 1–5.

## Relationship to prior work

Asgarli and Ghioca, *Linear system of geometrically irreducible plane cubics over finite fields*, arXiv:2407.18104, first public July 25, 2024, construct exactly this Frobenius-twisted family. Their Lemma 8 proves the geometric-irreducibility criterion, and their Theorem 5 establishes that only the unique norm-of-linear-form member is geometrically reducible. Those are prior results. The present finding distinguishes *smooth*, *nodal*, and *cuspidal* members, gives a closed norm equation for the singular-integral parameters and exact counts for every \(q\), and determines the rational point counts and branch splitting of every singular member. Neither the singularity stratification nor its arithmetic point-count profile is asserted in the inspected source.

The earlier Asgarli–Ghioca–Reichstein work *Linear system of hypersurfaces passing through a Galois orbit*, arXiv:2310.10361, provides broader Galois-orbit and irreducibility constructions, not these singularity and rational point distributions. The related later work of Asgarli–Love–Yip, arXiv:2501.01906, extends the Galois-orbit existence theorem, but does not state this Frobenius-twisted cubic discriminant computation. Elementary general facts about cyclic cubics, norms and genus-zero normalizations are used openly, not claimed as novel.

## Limitations

The theorem concerns this **specific** four-dimensional Frobenius-twisted cubic system; it is not a classification of all four-dimensional cubic systems, and it does not prove the broader conjecture that systems with every rational member geometrically irreducible exist for arbitrary \(q\). No uniform rational-point count is asserted for the smooth members. The displayed discriminant criterion is only set-theoretic on \(k\)-rational parameters, not a full scheme-theoretic discriminant-multiplicity calculation. The proof identifies the singular integral members up to geometric singularity type and finite-field point count, not their complete projective isomorphism classes or zeta functions.

## References

1. Shamil Asgarli and Dragos Ghioca, *Linear system of geometrically irreducible plane cubics over finite fields*, arXiv:2407.18104 (first public July 25, 2024), https://arxiv.org/abs/2407.18104. Especially Lemma 8, Theorem 5, Section 3 and Appendix A.
2. Shamil Asgarli, Dragos Ghioca and Zinovy Reichstein, *Linear system of hypersurfaces passing through a Galois orbit*, arXiv:2310.10361 (first public October 16, 2023), https://arxiv.org/abs/2310.10361.
3. Shamil Asgarli, Jonathan Love and Chi Hoi Yip, *Hypersurfaces passing through the Galois orbit of a point*, arXiv:2501.01906 (first public January 3, 2025), https://arxiv.org/abs/2501.01906.
