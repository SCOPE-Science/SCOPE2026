# Ideal-product monoids and central-binomial stabilization for truncated oriented cycles

## Finding

Fix any field \(k\), integer \(n\ge 2\), and Loewy cutoff \(\ell\ge2\). Let \(Q_n\) be the consistently oriented cycle on vertices \(\mathbb Z/n\mathbb Z\). Write \(J\) for the arrow ideal of its path algebra and \(A_{n,\ell}=kQ_n/J^\ell\). The following three formulas determine **every two-sided ideal, every ordered product of two-sided ideals, and the number of ideals in each dimension**:

1. Every two-sided ideal is uniquely \(I(t)=\bigoplus_{i\in\mathbb Z/n\mathbb Z}e_iJ^{t_i}\), with \(0\le t_i\le\ell\) and \(t_{i-1}\le t_i+1\) for all \(i\). Here \(e_iJ^\ell=0\), and \(I(t)\) has dimension \(n\ell-\sum_i t_i\).
2. For all admissible profiles \(t,u\), their **ordered** ideal product satisfies \(I(t)I(u)=I(t\star u)\), where
   \[
   (t\star u)_i=\min\{\ell,\,t_i+u_{i+t_i}\}.
   \]
   All subscripts are taken modulo \(n\). This gives the entire (generally noncommutative) multiplicative monoid of two-sided ideals over every field, without field-size parameters.
3. Put \(M_\ell(T)_{a,b}=T^{\ell-b}\mathbf1_{a\le b+1}\), for \(0\le a,b\le\ell\). Then the ideal-dimension enumerator is
   \[
   Z_{n,\ell}(T)=\sum_{I\triangleleft A_{n,\ell}}T^{\dim_k I}=\operatorname{tr}(M_\ell(T)^n).
   \]
   In particular, if \(N_{n,\ell}=Z_{n,\ell}(1)\), the exact **eventual Loewy-length increment** is
   \[
   \boxed{N_{n,\ell+1}-N_{n,\ell}=\binom{2n-1}{n-1}\qquad(\ell\ge\max\{2,n-2\}).}
   \]
   The polynomial \(Z_{n,\ell}(T)\) is reciprocal of degree \(n\ell\): \(T^{n\ell}Z_{n,\ell}(T^{-1})=Z_{n,\ell}(T)\).

Thus the number of ideals is eventually **exactly linear** in the Loewy cutoff, with the central-binomial slope above. For example, \(N_{3,2}=18\), \(N_{3,3}=28\), \(N_{4,2}=47\), \(N_{4,3}=82\), and \(N_{4,4}=117\). The specialization \(\ell=2\) follows from the established radical-square-zero quiver ideal classification and is **not** claimed as a new special case in isolation.

## Assumptions and scope

The path-basis convention is \(p_i^{(d)}\), the unique path of length \(d\in\{0,\ldots,\ell-1\}\) beginning at \(i\), and \(p_i^{(d)}p_j^{(e)}=p_i^{(d+e)}\) when \(j\equiv i+d\pmod n\) and \(d+e<\ell\); otherwise the product is zero. The length-zero paths are primitive idempotents \(e_i=p_i^{(0)}\). We count actual two-sided ideals, not isomorphism classes or conjugacy orbits. No finite-field assumption is needed; in fact the ideals form the same finite abstract monoid over every field. The classification also has an elementary \(n=1\) analogue for the chain algebra \(k[x]/(x^\ell)\), but the stated result focuses on genuinely oriented cycles with at least two vertices.

## Proof

**Step 1 — uniserial Peirce rows.** The right module \(e_iA_{n,\ell}\) has the strict chain of radical submodules \(e_iJ^d\) for \(0\le d\le\ell\), each successive quotient being one-dimensional. It is uniserial: for a nonzero submodule choose its least occurring path length \(d\); right multiplication by endpoint idempotents isolates its residue class modulo \(n\), and the corresponding leading path can be multiplied by a unit in the endpoint corner algebra to eliminate longer same-endpoint terms. Consequently the submodule contains \(p_i^{(d)}A_{n,\ell}=e_iJ^d\), and minimality gives equality. Since any right ideal \(I\) decomposes as \(\bigoplus_i e_iI\), it has a **unique** threshold profile \(t_i\in\{0,\ldots,\ell\}\). Its basis consists of paths \(p_i^{(d)}\) with \(d\ge t_i\). It follows immediately that \(\dim_k I=\sum_i(\ell-t_i)\).

**Step 2 — two-sidedness.** Closure under multiplication on the left by the arrow from \(i-1\) to \(i\) requires precisely \(t_{i-1}\le t_i+1\); when \(t_i=\ell\) the condition is vacuous because \(t_{i-1}\le\ell\). Vertex idempotents preserve the path spans, and all longer left paths are products of arrows. Hence this cyclic family of inequalities is necessary and sufficient for two-sidedness. In particular, no hidden nonmonomial ideals exist over extension fields.

**Step 3 — complete ideal multiplication.** An element of \(I(t)I(u)\) supported at starting vertex \(i\) is spanned by paths of lengths \(a+b<\ell\) with \(a\ge t_i\), \(b\ge u_{i+a}\), and the index \(i+a\) reduced modulo \(n\). The admissibility inequalities for \(u\) imply \(u_{j+1}\ge u_j-1\). Hence \(a+u_{i+a}\) is nondecreasing with the integer \(a\). Its least possible value occurs at \(a=t_i\), yielding the displayed \(t\star u\) formula (and the zero threshold \(\ell\) if the sum exceeds the cutoff). The product is already a two-sided ideal, so this determines its complete path basis. This direct algebraic proof also establishes associativity of the displayed profile operation; no separate semigroup assertion is assumed. The operation is generally noncommutative: at \(n=2,\ell=2\), profiles \(t=(0,1)\) and \(u=(1,0)\) yield \(t\star u=(1,2)\) but \(u\star t=(2,1)\).

**Step 4 — transfer trace.** The cyclic condition depends only on two adjacent thresholds. Assign the right-hand state \(b\) the weight \(T^{\ell-b}\) and permit the transition \(a\to b\) precisely when \(a\le b+1\). The trace of the \(n\)-th power of this \((\ell+1)\)-state matrix sums the weights of all cyclic profiles, counting each one exactly once with its labeled vertices. This proves the full dimension polynomial, not only the total count.

**Step 5 — central-binomial stabilization.** Let \(B_{n,h}\) be the number of admissible nonnegative cyclic profiles with minimum zero and maximum at most \(h\). Subtracting one from each coordinate bijects the admissible profiles with every coordinate at least one at cutoff \(\ell+1\) with all profiles at cutoff \(\ell\), giving \(N_{n,\ell+1}-N_{n,\ell}=B_{n,\ell+1}\). In any cyclic profile with minimum zero, follow forward from a largest coordinate to a zero. The profile can decrease by at most one per step, and the path has at most \(n-1\) edges, so its maximum is at most \(n-1\). Therefore \(B_{n,h}\) is independent of \(h\) once \(h\ge n-1\). For \(n\ge3\) the bound cannot be lowered: the valid cyclic profile \(t=(0,n-1,n-2,\ldots,1)\) has minimum zero and maximum \(n-1\).

To count all such minimum-zero profiles, cut the cyclic sequence at its zero positions. A gap of \(d\ge1\) edges between consecutive zeros, with strictly positive interior, can be filled in exactly \(C_{d-1}\) ways, where \(C_j=\frac1{j+1}\binom{2j}{j}\) is the Catalan number: after reversing the interior sequence, these are the standard positive area sequences, starting at one and rising by at most one per step. Set \(C(z)=\sum_{j\ge0}C_jz^j=(1-\sqrt{1-4z})/(2z)\) and \(F(z)=zC(z)\). If there are \(r\) zero positions, choosing a distinguished zero gives \(n\) possible labels and an ordered \(r\)-tuple of gaps; division by \(r\) accounts for the distinguished choice. Thus the number \(B_n\) of all minimum-zero cyclic profiles is
\[
B_n=n[z^n]\sum_{r\ge1}\frac{F(z)^r}{r}
=n[z^n]\left(-\log\frac{1+\sqrt{1-4z}}2\right)
=\frac12\binom{2n}{n}=\binom{2n-1}{n-1}.
\]
This proves the stated threshold and exact slope, including all coincidences among zero positions.

**Step 6 — reciprocity.** The linear functional \(\lambda:A_{n,\ell}\to k\) taking the sum of coefficients of all paths of length \(\ell-1\) makes \((a,b)\mapsto\lambda(ab)\) a nondegenerate associative pairing: each basis path has a unique complementary path of total length \(\ell-1\). For a two-sided ideal \(I\), the right annihilator is its right orthogonal under this pairing (left-ideal closure permits the usual nondegeneracy argument), and has complementary dimension \(n\ell-\dim I\). The right and left annihilator maps are inverse bijections on two-sided ideals, hence the dimension-count polynomial is reciprocal. This is the standard Frobenius-annihilator argument applied to this family, not a separate novelty claim.

## Verification

The accompanying dependency-free checker `verify_cyclic_nakayama.py` independently constructs path multiplication over \(\mathbb F_2\), enumerates **all** reduced-row-echelon subspaces of the underlying vector space for the cases \((n,\ell)=(1,3),(2,2),(2,3),(3,2)\), and tests closure under left and right multiplication by all vertex idempotents and arrows. The enumerated ideal subspaces agree exactly with the threshold profiles: respectively \(4,7,10,18\) ideals among \(16,67,2825,2825\) ambient subspaces. The checker then independently multiplies representative ideal basis vectors and compares all \(16+49+100+324=489\) ordered ideal products with the profile law. It also verifies transfer-coefficient palindromicity in the displayed small cases and the stabilized central-binomial increment for \(1\le n\le7\) across tested cutoffs. This is finite corroboration only; the arbitrary-field and all-parameter statements follow from Steps 1–6.

Reproduce with `python verify_cyclic_nakayama.py`; the complete expected run output is `verification_output.txt`. No third-party mathematical software is needed.

## Relationship to prior work

The existence and uniseriality of the primitive projective modules are classical serial-ring theory; Eisenbud–Griffith (1971) and standard Nakayama-algebra treatments cover that underlying structural fact. Han (2010) investigates homological consequences of truncated oriented cycles, not their complete two-sided-ideal product table or a Loewy-length ideal census. Aliniaeifard–Behboodi–Li (2014) develops general directed annihilating-ideal graphs, not the explicit truncated-cycle ideal monoid or the central-binomial stabilization formula. General results about poset order ideals or cyclic compositions provide combinatorial machinery, but a sequence match alone does not establish that these ring-theoretic formulas were previously published.

The classical uniserial decomposition, the elementary \(\ell=2\) radical-square-zero case, and standard Frobenius annihilator duality are explicitly **not** claimed as new. The assessed combined contribution is the full **ordered ideal-product formula** for every truncation, the dimension-refined trace count, and especially the sharp eventual linear growth with its Catalan/central-binomial explanation. These are derived here rather than quoted from an established formula. An unidentified prior treatment of the same ideal semigroup or an equivalent closed enumeration may exist; historical priority is not certified.

## Limitations

The family has exactly one oriented arrow from each vertex to its successor and a uniform truncation \(J^\ell\); nonuniform Kupisch series, multiple arrows, and general quiver relations are not included. The theorem treats ordinary two-sided ideals and their products, not arbitrary one-sided-ideal module classes, ideal schemes, or deformation theory. The finite computational verification covers only the stated small cases. Claims of absolute historical uniqueness, independent mathematical validation, and publication are not made.

## References

- D. Eisenbud and P. Griffith, *Serial Rings*, Journal of Algebra **17** (1971), 389–400. Author-hosted text: https://eisenbud.github.io/papers/pdfs/1971-001.pdf.
- D. Eisenbud and P. Griffith, *The Structure of Serial Rings*, Pacific Journal of Mathematics **36** (1971), 109–121. https://doi.org/10.2140/pjm.1971.36.109.
- Yang Han, *Hochschild homology, global dimension, and truncated oriented cycles*, arXiv:1004.0748v1 (first posted 2010-04-06). https://arxiv.org/abs/1004.0748.
- F. Aliniaeifard, M. Behboodi and Y. Li, *The Annihilating-Ideal Graph of a Ring*, arXiv:1411.4159v1 (first posted 2014-11-15). https://arxiv.org/abs/1411.4159.
