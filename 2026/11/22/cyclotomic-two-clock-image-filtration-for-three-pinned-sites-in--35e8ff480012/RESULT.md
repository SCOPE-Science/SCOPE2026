# Cyclotomic two-clock image filtration for three pinned sites in Rule 150

## Finding

Let \(X=\mathbb F_2^{\mathbb Z}\), and let \(F:X\to X\) be the additive cellular automaton
\[
(Fx)_i=x_i+x_{i+1}+x_{i+2}\pmod 2.
\]
This is the elementary Rule 150 map composed with a spatial translation. For an arbitrary triple of distinct positions \(S=\{a,b,c\}\subset\mathbb Z\), \(a<b<c\), and any assignment \(v:S\to\mathbb F_2\), let
\[
C_S(v)=\{x\in X:x_s=v(s)\text{ for all }s\in S\}.
\]
For each integer \(n\ge1\), the compact affine subgroup \(F^n(C_S(v))\) is a coset of a subgroup of index \(2^{d_n(S)}\), where the exponent \(d_n(S)\in\{0,1,2\}\) depends only on the positions, not on \(v\). Its complete formula is as follows. Put \(r_{uv}=2^{\nu_2(v-u)}\) for each pair \(u<v\) in \(S\), with \(\nu_2\) the exponent of two dividing a positive integer.

**Three different residues modulo three.** If \(a,b,c\) represent all three residue classes, define
\[
r=\min\{r_{ab},r_{bc},r_{ac}\}.
\]
Then
\[
d_n(S)=\mathbf1_{\{n\le r\}}.
\]
**Exactly two equal residues modulo three.** For the unique pair \(u<v\) with \(u\equiv v\pmod 3\), put \(r=r_{uv}\). Then again
\[
d_n(S)=\mathbf1_{\{n\le r\}}.
\]
**All three residues equal modulo three.** Put \(r_{\min}=\min\{r_{ab},r_{bc},r_{ac}\}\) and \(r_{\max}=\max\{r_{ab},r_{bc},r_{ac}\}\). Then
\[
d_n(S)=\mathbf1_{\{n\le r_{\min}\}}+\mathbf1_{\{n\le r_{\max}\}}.
\]
Thus the all-equal-residue case has **two distinct loss times**: its image index falls from four to two immediately after \(r_{\min}\), and from two to one immediately after \(r_{\max}\).

In particular, the first full-image time, defined by
\[
T(S)=\min\{n\ge0:F^n(C_S(v))=X\},
\]
is independent of the assigned bits and is exactly \(1+r\) in either of the first two cases, and \(1+r_{\max}\) in the third case. For any two distinct pinned sites \(u<v\), the first full-image time is \(1\) if \(3\nmid(v-u)\), and \(1+2^{\nu_2(v-u)}\) otherwise.

For every integer \(L\ge2\), the sharp universal worst-case three-site time for masks of diameter at most \(L\) is
\[
\max_{a<b<c,\;c-a\le L}T(\{a,b,c\})
=1+2^{\lfloor\log_2(L/2)\rfloor}.
\]
Equality is attained by the equally spaced triple \(\{0,2^s,2^{s+1}\}\), where \(s=\lfloor\log_2(L/2)\rfloor\). For this family every two-site submask is already fully controllable after one update, while the joint three-site mask remains non-full through time \(2^s\).

## Assumptions and scope

The configuration space is the **bilateral infinite** binary full shift with the product topology. Times \(n\) are synchronous nonnegative integers; in all index formulas \(n\ge1\). Finite masks have distinct integer coordinates and prescribed input values, while target configurations range over all of \(X\). Spatially periodic rings, bounded output windows, and finite-volume inverse degrees are not substituted for infinite-configuration full-image exactness. Every index statement applies equally to all eight possible assignments on a three-site mask. The empty or one-site mask has index one after any positive time.

## Proof

**1. Character-dual criterion for the full image and its index.** Write \(P(z)=1+z+z^2\in\mathbb F_2[z]\). A finite-support character is represented by a Laurent polynomial \(g(z)=\sum_j g_jz^j\) acting as \((-1)^{\sum_jg_jx_j}\). Its pullback under \(F^n\) corresponds to multiplication by \(P(z)^n\). Since \(P\) is nonzero and the Laurent-polynomial ring is an integral domain, the dual map is injective, and hence \(F^n\) is surjective on \(X\).

Let \(K_S=\{x:x_s=0\text{ for }s\in S\}\). The annihilator of the closed subgroup \(F^n(K_S)\) consists precisely of those finite characters \(g\) for which \(P^ng\) is supported in \(S\). Thus its dimension over \(\mathbb F_2\) is
\[
d_n(S)=\dim_{\mathbb F_2}\Big(\{h\in\mathbb F_2[z,z^{-1}]:\operatorname{supp}h\subseteq S,\ P^n\mid h\}\Big).
\]
The displayed divisibility is in the Laurent-polynomial ring. By character separation of compact subgroups, \([X:F^n(K_S)]=2^{d_n(S)}\). The image \(F^n(C_S(v))\) is a coset of \(F^n(K_S)\), proving independence from \(v\). More constructively, for each \(h=P^ng\) supported in \(S\) the corresponding output equation is
\[
\sum_j g_jy_j=\sum_{s\in S}h_s v(s)\pmod2.
\]
These equations describe the *entire* image: their common solution space is the above affine coset.

**2. Cyclotomic valuation of sparse polynomials.** Let \(\zeta\in\mathbb F_4\) be a primitive cube root of unity. Then \(P\) is the minimal polynomial of \(\zeta\) over \(\mathbb F_2\). For a binomial \(z^u+z^v\), \(u<v\), its valuation \(\operatorname{ord}_P\) is zero if \(3\nmid(v-u)\), and otherwise equals
\[
\operatorname{ord}_P(z^u+z^v)=2^{\nu_2(v-u)}=r_{uv}.
\]
Indeed, write \(v-u=2^e d\) with \(d\) odd. The identity \(1+z^{2^ed}=(1+z^d)^{2^e}\) reduces the question to whether \(\zeta^d=1\); when it does, the derivative \(d z^{d-1}\) is nonzero at \(\zeta\), so the root is simple before raising to the Frobenius power.

For the triple polynomial \(h(z)=z^a+z^b+z^c\), evaluating at \(\zeta\) gives zero **if and only if** the three exponents represent distinct classes modulo three: if two coincide their two root powers cancel, leaving the third; if all coincide, three copies leave one nonzero term. Assume they are distinct and set
\[
e=\min\{\nu_2(b-a),\nu_2(c-a),\nu_2(c-b)\}.
\]
After factoring out \(z^a\) and a \(2^e\)-th Frobenius power, we obtain \(1+z^u+z^v\) with distinct exponents modulo three and at least one of \(u,v\) odd. Its derivative at \(\zeta\) is nonzero: one odd exponent produces one nonzero term, while two odd exponents produce two *distinct* nonzero powers of \(\zeta\), which cannot cancel. Its \(P\)-valuation is therefore one, and
\[
\operatorname{ord}_P(z^a+z^b+z^c)=2^e=\min\{r_{ab},r_{bc},r_{ac}\}.
\]
If the residues are not all distinct, the triple polynomial has valuation zero. Every nonzero polynomial supported on three sites has exactly one, two, or three monomials, and single monomials have valuation zero.

**3. Exact index at each positive time.** At a fixed \(n\ge1\), the divisibility subspace from Step 1 is spanned by the eligible nonzero one-, two- and three-term polynomials. If the three residues are distinct, only the full trinomial qualifies, and it qualifies precisely for \(n\le r\), giving dimension one or zero. If exactly two residues agree, only their binomial qualifies, again giving dimension one or zero.

If all three residues agree, each of the three pair-binomial polynomials qualifies precisely until its own clock \(r_{uv}\); the trinomial never qualifies. The three binomials have a single linear dependence (their sum is zero), and any two are independent. In the two-adic metric on three different integers, the minimum of their valuations occurs for exactly two pairs, and the maximum for the remaining pair. Accordingly, all three binomials qualify for \(n\le r_{\min}\), just one qualifies for \(r_{\min}<n\le r_{\max}\), and none qualifies after \(r_{\max}\). This proves all asserted index and first-full-time formulas.

**4. Sharp diameter bound.** Suppose \(T(S)>1+2^{\lfloor\log_2(L/2)\rfloor}\). In the all-distinct-residue case, divisibility to order \(2^e\) requires all three distinct positions to be congruent modulo \(2^e\), so their span is at least \(2^{e+1}\). In either repeated-residue case, the controlling pair differs by a positive multiple of \(3\cdot2^e\), so the span is at least \(3\cdot2^e\). In every case a clock larger than the claimed power forces a diameter greater than \(L\). Conversely, \(\{0,2^s,2^{s+1}\}\) has three distinct residues modulo three, diameter \(2^{s+1}\le L\), and its full trinomial is \(P(z)^{2^s}\) by Frobenius. It therefore has exact first full-image time \(1+2^s\), proving sharpness.

## Verification

The standalone Python program `verify_cyclotomic_clocks.py` uses exact integer-encoded polynomial long division over \(\mathbb F_2\) to compare the theoretical first-full-time formula with all seven possible nonzero sparse polynomial valuations for 8,910 three-site masks. Separately, it constructs explicit time-\(n\) binary linear maps from pinned inputs to finite output windows and compares their rank deficiencies with the exact three-case index formula in 3,002 checks. It also checks every two-site spacing through 80 and the sharp span law through 120 (exhaustively for spans through 55). These are independent, finite corroborations; the unbounded statements are proved in Steps 1–4 and do not rely on extending sample calculations to infinity.

Run with `python3 verify_cyclotomic_clocks.py`. The verifier has no external package dependencies and raises an assertion on a mismatch.

## Relationship to prior work

Castronuovo, Dennunzio and Margara's 2026 study classifies *qualitative* topological transitivity of group cellular automata and develops Laurent-polynomial criteria, but does not give a three-site, all-time cylinder-image index law. Dennunzio, Formenti, Grinberg and Margara's 2019 analysis establishes structural properties of additive cellular automata, including strong transitivity invariance, not these sharp finite-time indices. Martin, Odlyzko and Wolfram's 1984 algebraic treatment underlies polynomial methods for additive automata, primarily on finite periodic rings; the present problem concerns all target configurations on the bilateral infinite lattice with input constraints at three sparse positions.

The published inverse-degree classification of **cyclic Rule 150 necklaces** concerns one synchronous update on finite rings modulo rotation. That setting has a related modulo-three phenomenon but does not imply the distinct two-adic index clocks for bilateral sparse cylinders or the sharp diameter law. The use of finite characters and elementary cyclotomic factorization is standard; the claim of contribution is the exact three-site index filtration and its sharp temporal extremizers, not those basic tools.

## Limitations

The theorem concerns the bilateral binary Rule 150 map with exactly three pinned sites (and the stated two-site corollary). It does not classify arbitrary larger masks, cyclic-ring predecessor populations, or temporal orbit periods. The image index is a *finite codimension* in the full infinite configuration group, not the size of a finite output-word set. Published historical priority is not exhaustively established: equivalent formulations might be hidden in older additive-automaton, polynomial-code, or cyclotomic-factor literature. No independent mathematical audit has been performed.

## References

1. N. Castronuovo, A. Dennunzio and L. Margara, *Topological transitivity of group cellular automata is decidable*, first released 22 January 2026, arXiv:2601.16243. https://arxiv.org/abs/2601.16243
2. A. Dennunzio, E. Formenti, D. Grinberg and L. Margara, *Additive Cellular Automata Over Finite Abelian Groups: Topological and Measure Theoretic Properties*, MFCS 2019, Article 68. https://doi.org/10.4230/LIPIcs.MFCS.2019.68
3. O. Martin, A. M. Odlyzko and S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics **93** (1984), 219–258. https://doi.org/10.1007/BF01223745
4. *The exact inverse-degree spectrum of cyclic Rule 150 necklaces*, 2026, public record: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-exact-inverse-degree-spectrum-of-cyclic-rule-150-necklaces--89cc648da7e1
