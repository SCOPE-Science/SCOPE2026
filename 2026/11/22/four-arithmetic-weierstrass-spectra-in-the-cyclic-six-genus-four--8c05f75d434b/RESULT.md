# Four arithmetic Weierstrass spectra in the cyclic-six genus-four hyperelliptic family

## Finding

Fix an odd prime power \(q\equiv2\pmod3\), necessarily of characteristic at least five. For each coefficient pair \((a,b)\in\mathbb F_q^2\), set
\[
 h_{a,b}(t)=t^3+t^2+at+b,\qquad
 C_{a,b}:y^2=x^{10}+x^7+ax^4+bx=xh_{a,b}(x^3).
\]
Let \(U_q\) consist of the coefficient pairs for which the indicated polynomial is squarefree; equivalently \(b\ne0\) and \(h_{a,b}\) is separable. These curves have genus four. Denote the geometric hyperelliptic branch locus (equivalently, the ten geometric Weierstrass points) by \(W_{a,b}\). We write \(1^r2^s\) for a Frobenius permutation having \(r\) fixed points and \(s\) two-cycles.

**Theorem.** Exactly the following four Frobenius cycle types occur on \(W_{a,b}\), with the displayed numbers of coefficient-marked smooth curves:

| Frobenius cycles on \(W_{a,b}\) | Number of \((a,b)\in U_q\) | \(|W_{a,b}(\mathbb F_q)|\) | \(|\operatorname{Jac}(C_{a,b})[2](\mathbb F_q)|\) |
|:--|--:|--:|--:|
| \(1^4 2^3\) | \((q^2-6q+11)/6\) | \(4\) | \(32\) |
| \(1^2 2^4\) | \((q^2-4q+7)/6\) | \(2\) | \(16\) |
| \(1^2 2^1 6^1\) | \((q-2)(q+1)/3\) | \(2\) | \(4\) |
| \(1^1 3^1 6^1\) | \((q^2-1)/3\) | \(1\) | \(2\) |

All four counts are positive for every permitted \(q\), and their sum is \(|U_q|=q^2-2q+2\). Hence the branch scheme has exactly one, two, or four rational points; the complete scheme zeta function is \(\prod_{d\in\{1,2,3,6\}}(1-T^d)^{-c_d}\) when its Frobenius cycle multiplicities are \(c_d\) as in the table. Its least common splitting-field degree is two for the first two types, and six for the last two. The table counts ordered literal parameter pairs, **not** geometric or rational isomorphism classes, and it concerns all smooth members, not merely superspecial ones.

## Assumptions and scope

The field is any finite field \(\mathbb F_q\) of odd characteristic with \(q\equiv2\pmod3\), including nonprime fields. The polynomial \(h_{a,b}\) has discriminant
\[
 \Delta(a,b)=a^2-4a^3-4b-27b^2+18ab.
\]
The precise smooth locus is \(U_q=\{(a,b):b\Delta(a,b)\ne0\}\). As \(h(0)=b\) and the map \(x\mapsto x^3\) is separable away from zero, this is exactly the condition that \(xh(x^3)\) have ten simple geometric roots. The resulting smooth completion has genus four. Since the degree is even, its two points at infinity are unramified; the ten roots are precisely the geometric hyperelliptic branch points.

No congruence class for \(q\equiv1\pmod3\) is asserted. The degree-six automorphism is understood geometrically; it need not be rational over the base field.

## Proof

**1. Kummer blocks and the four possible Frobenius types.** The root \(x=0\) is rational. For each nonzero geometric root \(t\) of \(h(t)\), the corresponding three roots of the degree-ten branch polynomial satisfy \(x^3=t\). Since the cube map is bijective on \(\mathbb F_{q^m}\) whenever \(m\) is odd, and \(\mu_3\) first enters \(\mathbb F_{q^2}\), a rational root \(t\) produces one fixed branch point and one Frobenius pair. Three rational roots of \(h\) therefore give \(1^4 2^3\).

If \(h\) has one rational root and an irreducible quadratic factor, its rational root contributes \(1^1 2^1\), in addition to the fixed point \(x=0\). Let \(\alpha\in\mathbb F_{q^2}\setminus\mathbb F_q\) be a root of the irreducible quadratic. If \(\alpha\in(\mathbb F_{q^2}^*)^3\), all six corresponding branch roots are defined over \(\mathbb F_{q^2}\) and form three Frobenius pairs. Otherwise their smallest common field is \(\mathbb F_{q^6}\) and they form one six-cycle. The total types are respectively \(1^2 2^4\) and \(1^2 2^1 6^1\).

If \(h\) is irreducible cubic, its roots belong to \(\mathbb F_{q^3}\). The cube map is bijective there, giving one degree-three orbit of lifts. Their other six lifts use nontrivial cube roots of unity and form one degree-six orbit. Together with \(x=0\) the type is \(1^1 3^1 6^1\). This is exhaustive since a separable cubic has factor degrees \((1,1,1)\), \((1,2)\), or \((3)\).

**2. Count the smooth cubic parameters.** The discriminant-zero cubics with nonzero constant term are exactly \((t-r)^2(t-s)\) with \(r,s\in\mathbb F_q^*\) and \(2r+s=-1\), giving \(q-2\) distinct coefficient pairs (including the triple-root polynomial once). Thus \(|U_q|=q(q-1)-(q-2)=q^2-2q+2\).

Three distinct nonzero roots of \(h\) must sum to \(-1\). The number of ordered nonzero triples with this sum is \(q^2-3q+3\). Among them \(3(q-2)-2\) have at least two equal entries, by inclusion-exclusion (the unique all-equal triple is counted three times). Division by six therefore gives
\[
 N_{111}=\frac{q^2-6q+11}{6}.
\]
For a cubic of type \((1,2)\), choose its nonzero rational root \(r\) in \(q-1\) ways. The remaining irreducible quadratic is uniquely of the form
\[
 t^2+(1+r)t+v,
\]
whose coefficient of \(t^2\) in \((t-r)(t^2+(1+r)t+v)\) is \(1\). Its two roots have trace \(-(1+r)\). For any prescribed trace there are exactly \((q-1)/2\) monic irreducible quadratic polynomials. Hence
\[
 N_{12}=\frac{(q-1)^2}{2},\qquad
 N_3=|U_q|-N_{111}-N_{12}=\frac{q^2-1}{3}.
\]

**3. A cubic-trace lemma.** Let \(k=\mathbb F_q\) and \(K=\mathbb F_{q^2}=k(\sqrt d)\) with \(d\) a nonsquare in \(k\). Since \(q\equiv2\pmod3\), the polynomial \(z^2+3\) is irreducible over \(k\), so \(-3d\) is a square in \(k\). For \(\beta=u+v\sqrt d\),
\[
 \operatorname{Tr}_{K/k}(\beta^3)=2u(u^2+3dv^2).
\]
The homogeneous cubic on the right splits into three distinct rational linear factors. Therefore its zero fiber has \(3q-2\) points. Because cubes on \(k^*\) are bijective, scaling \(\beta\) shows every nonzero trace fiber has the same cardinality. Summing over traces gives \((q^2-(3q-2))/(q-1)=q-2\) points in every nonzero fiber.

Every nonzero cube in \(K\) has exactly three cube roots. At trace zero, the number of *nonzero* cubic residues is \((3q-3)/3=q-1\), all nonrational since the only element of \(k\) of trace zero is zero. At each nonzero trace \(s\), the number of cubic residues is \((q-2)/3\), of which precisely one is in \(k\), namely \(s/2\). Conjugate nonrational elements occur in pairs and have equal cubic character. Consequently, the number of irreducible quadratics with cubic-residue roots and prescribed trace \(s\) is
\[
 C(s)=\begin{cases}
 (q-1)/2,&s=0,\\
 (q-5)/6,&s\ne0.
 \end{cases}
\]
The complementary irreducible quadratics with noncube roots number zero when \(s=0\), and \((q+1)/3\) when \(s\ne0\).

**4. Refine the \((1,2)\) count.** In Step 2, the quadratic trace is \(s=-(1+r)\). Since \(r\in k^*\), there is precisely one value \(r=-1\) for which \(s=0\), and the other \(q-2\) values give \(s\ne0\). Hence the count in which its two roots are cubes in \(K\) is
\[
 N_{12,\mathrm{cube}}=\frac{q-1}{2}+(q-2)\frac{q-5}{6}=\frac{q^2-4q+7}{6};
\]
its complement is
\[
 N_{12,\mathrm{noncube}}=(q-2)\frac{q+1}{3}.
\]
Combining the four cases proves the Frobenius spectrum and parameter-count table.

**5. Rational Jacobian two-torsion.** For a hyperelliptic genus-four curve in odd characteristic, the geometric two-torsion is the vector space of even subsets of its ten branch points modulo complementation. If a class is rational, its representative \(S\) satisfies either \(F(S)=S\) or \(F(S)=S^c\). The latter is impossible because \(x=0\) is a rational branch point. The Frobenius-invariant subset representatives are unions of its \(c\) cycles. Since there is an odd-length cycle, the parity condition is one independent linear equation; quotienting by the full ten-point subset removes one more dimension, leaving \(c-2\). The four displayed cycle types have respectively \(c=7,6,4,3\), yielding rational two-torsion cardinalities \(32,16,4,2\). The zeta and exact extension-degree assertions follow immediately by writing a finite étale scheme as its Frobenius orbits.

## Verification

Two standalone Python-standard-library programs accompany this result. Run `python3 verify_frobenius.py` and `python3 verify_trace.py` from a directory containing both files. The first enumerates every smooth coefficient pair over each prime field \(\mathbb F_p\) with \(p\in\{5,11,17,23,29,41\}\), independently computes the Frobenius orbit degrees of the full degree-ten polynomial via polynomial gcds with \(x^{p^n}-x\), and checks all four exact parameter frequencies. The second independently enumerates the elements of each quadratic field \(\mathbb F_{p^2}\) and checks the cubic-residue trace lemma, including the exceptional zero-trace fiber. Both were executed successfully, with terminal markers `CUBIC_BRANCH_SPECTRA_VERIFIED` and `CUBIC_TRACE_DISTRIBUTION_VERIFIED`.

The proof covers all odd prime powers in the stated congruence class; prime-field experiments alone are not used to prove the infinite-family statement. No external computer-algebra library, precomputed table, or stale run artifact is required.

## Relationship to prior work

Kudo, Nakagawa and Takagi introduced the exact family \(C_{a,b}\), developed its Cartier-Manin matrix and superspeciality enumeration, and classified its relevant automorphisms; they did not give the uniform branch-divisor Frobenius-frequency table. Their construction and automorphism facts are prior work. Existing specific arithmetic stratifications for this same family in characteristics seven, eleven and seventeen concern Cartier ranks, Hasse divisors and Newton data, not the four root-cycle types for all \(q\equiv2\pmod3\). A closely related arithmetic theorem classifies five branch-cycle types for the differently normalized family \(y^2=x^{10}+ux^7+vx^4+x\) over \(q\equiv1\pmod3\); the base-field congruence classes are disjoint, the cube-root-of-unity action differs, and that result neither contains nor implies the present four frequencies. A published four-type branch table for the distinct Bruin–Kulkarni genus-four Jacobian-square family depends on quadratic rather than cubic lifting and likewise does not give the frequencies here. General finite-field cubic-residue counting, including the related but distinct results of a 2025 paper on selected quadratic/cubic pairs, is not claimed as a new technique. The new assertion is the complete exact arithmetic classification across this specific cyclic-six hyperelliptic family, with all four frequencies and their rational two-torsion consequences.

## Limitations

The theorem counts coefficient-marked smooth members only and does not identify which of them are superspecial, classify isomorphism or twist classes, compute the zeta functions of the curves themselves, or address fields with \(q\equiv1\pmod3\). The zeta functions asserted are for their *reduced ten-point Weierstrass support*, not for the curves. Novelty is based on direct comparisons with accessible scientific sources; a mathematically equivalent unindexed or unavailable calculation remains possible. A historical file beyond the accessible ledger set was unavailable for comparison and is not assumed to contain or exclude an overlapping result.

## References

1. M. Kudo, T. Nakagawa and T. Takagi, *Efficient search for superspecial hyperelliptic curves of genus four with automorphism group containing* \(\mathbb Z_6\), arXiv:2210.14822v1 (public 2022-10-26), especially §§1, 3.1–3.3 and Appendix A, https://arxiv.org/abs/2210.14822.
2. R. Ohashi and M. Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858v1 (public 2023-12-28), §§1–3, https://arxiv.org/html/2312.16858v1.
3. N. Bruin and A. Kulkarni, *On (2,2)-decomposable genus 4 Jacobians*, arXiv:2309.01959v1 (public 2023-09-05), Example 7.3, https://arxiv.org/abs/2309.01959.
4. *A note on some quadratics and cubics over finite fields*, *Bulletin of the Australian Mathematical Society* (2025), Theorem 1.1 and §2, https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/note-on-some-quadratics-and-cubics-over-finite-fields/6B2F227573881D91E17CD5B93028900E.
