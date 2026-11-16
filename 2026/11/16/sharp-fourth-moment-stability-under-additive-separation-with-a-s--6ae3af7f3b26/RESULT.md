# Sharp fourth-moment stability under additive separation, with a seven-satellite transition

## Finding
Let \(A=\{0,1,2\}\), let \(T\subset\mathbb Z\) have cardinality \(m\ge1\), and assume the additive separation conditions below. For a complex Fourier polynomial \(f(z)=\sum_{j=0}^2 a_jz^j+\sum_{u\in T}b_uz^u\), on \(\mathbb T\) with probability Haar measure, define total coefficient energy \(E=\sum_{j=0}^2|a_j|^2+\sum_{u\in T}|b_u|^2\) and satellite energy \(R=\sum_{u\in T}|b_u|^2\). Then
\[
\|f\|_{L^4(\mathbb T)}^4\le \frac{15}{7}E^2,
\qquad
\frac{15}{7}E^2-\|f\|_{L^4}^4\ge\delta_mER,
\qquad
\delta_m=\min\left\{\frac27,\frac17+\frac1m\right\}.
\]
Both constants are sharp. For nonzero \(f\), equality in the first occurs precisely when all \(b_u=0\) and, for some \(\lambda\ne0\) and real \(\theta\),
\[
(a_0,a_1,a_2)=\lambda(\sqrt2,\sqrt3e^{i\theta},\sqrt2e^{2i\theta}).
\]
For the stability coefficient: if \(m<7\), it is approached as \(R/E\downarrow0\) and is not attained with \(R>0\); at \(m=7\), equality with \(R>0\) holds for any energy split if the nonzero core, when present, is extremal and all satellite powers coincide; if \(m>7\), equality with \(R>0\) forces all core coefficients zero and all satellite powers equal. This is a sharp transition in the location of the extremizers of the normalized deficit.

## Assumptions and scope
Write \(A+A=\{a+a':a,a'\in A\}\), and similarly for sumsets. Assume: (1) the three sets \(A+A\), \(A+T\), and \(T+T\) are pairwise disjoint; (2) for distinct \(u,v\in T\), the translates \(A+u\) and \(A+v\) are disjoint; (3) the map taking unordered pairs \(\{u,v\}\) with repetition allowed to \(u+v\) is injective. These are purely additive conditions; the theorem is for arbitrary complex coefficients, every integer \(m\ge1\), and every integer support satisfying them. Example: \(T=\{10^j:1\le j\le m\}\) satisfies all three by decimal digit uniqueness and separation from the short progression. The result is not an assertion for all unions of a resonant triple with a Sidon set: the mixed-sum separation hypotheses are essential.

## Proof
Parseval applied to \(f^2\) yields \(\|f\|_4^4=\sum_n|\sum_{k+\ell=n}c_kc_\ell|^2\). Define \(s=\sum_{j=0}^2|a_j|^2\), \(r=\sum_{u\in T}|b_u|^2\), \(Q_A=\|a_0+a_1z+a_2z^2\|_4^4\). Sumset disjointness, the pairwise disjoint mixed translates, and Sidon uniqueness yield the **exact** identity
\[
\|f\|_4^4=Q_A+4sr+2r^2-\sum_{u\in T}|b_u|^4. \tag{1}
\]
For the core put \(U=|a_0|^2+|a_2|^2\), \(v=|a_1|^2\), and \(p=|a_0a_2|\). Expanding its five convolution coefficients gives
\[
Q_A=U^2+v^2+2p^2+4Uv+4\Re(a_0a_2\overline{a_1}^2).
\]
The exact nonnegative deficit decomposition is
\[
\frac{15}{7}s^2-Q_A=\frac72\left(v-\frac{3s}{7}\right)^2
+2\left(\frac{U^2}{4}-p^2\right)
+4\left(\frac{Uv}{2}-\Re(a_0a_2\overline{a_1}^2)\right). \tag{2}
\]
Each summand is nonnegative, using arithmetic-geometric mean and \(\Re(w)\le|w|\). For \(s>0\), equality forces \(v=3s/7\), \(|a_0|^2=|a_2|^2=2s/7\), and \(\arg(a_0a_2)=2\arg(a_1)\) modulo \(2\pi\), precisely the stated core extremizers.

Substitute (1) into the total deficit and use (2):
\[
\frac{15}{7}(s+r)^2-\|f\|_4^4
=\left(\frac{15}{7}s^2-Q_A\right)+\frac27sr+\frac17r^2+\sum_{u\in T}|b_u|^4.
\]
Cauchy–Schwarz gives \(\sum|b_u|^4\ge r^2/m\), with equality exactly for equal squared magnitudes. Hence for \(r>0\)
\[
\frac{(15/7)(s+r)^2-\|f\|_4^4}{(s+r)r}\ge
\frac27\frac{s}{s+r}+\left(\frac17+\frac1m\right)\frac{r}{s+r}\ge\delta_m.\tag{3}
\]
Taking sharp core data and letting \(r\downarrow0\) gives the first endpoint \(2/7\) as a sharp infimum; taking \(s=0\) and all \(|b_u|\) equal gives the other endpoint \(1/7+1/m\) exactly. At \(m=7\) both endpoints coincide, and (2) together with equality in Cauchy–Schwarz gives equality at every energy split. For \(m<7\), (3) strictly exceeds the minimum whenever \(r>0\); for \(m>7\), equality forces \(s=0\). Finally, (1)–(2) and the positive cross deficit show the first \(L^4\) inequality is strict unless \(r=0\) and the core is extremal. This proves all quantifiers and equality cases.

## Verification
The standalone file `check.py` uses exact rational arithmetic to evaluate convolution sums, the three-class sumset separation, the exact decomposition (1), and inequality (3) for the concrete supports \(T=\{10^j\}\), with \(m=1,2,3,5,7,8,9,12,20\) and 50 pseudo-random coefficient vectors per value. The identities and proof above establish all-support and all-complex-coefficient validity; these finite checks are corroborative, not a substitute for the proof. Exact equality at endpoints follows symbolically from equations (2) and (3).

## Relationship to prior work
Bourgain's \(\Lambda(p)\) selection theorem, as revisited by Burstein, Iosevich and Krause (2026), supplies a contemporary motivation for frequency-set design, without furnishing this specific sharp constant or sharp outlier-energy coefficient in its accessible abstract. Klemes (1999), Theorem 6.2, proves a uniform \(L^4\) bound for combinatorial forest-structured frequency sets; it does not state the present sharp deficit theorem. Other published fourth-moment classifications for resonant Fourier patterns involve different supports or optimization objectives. The exact convolution-collision method and the three-frequency \(L^4\) extremization are elementary predecessors acknowledged here. Novelty is asserted only relative to inspected evidence and is not an independence or priority certificate.

## Limitations
The source manuscript of Burstein–Iosevich–Krause was accessible only through its abstract. The Klemes article's searchable PDF text was read at its introduction and main theorem, but full-page screenshot verification was blocked by the host (403). The theorem requires complete additive separation and makes no claim for arbitrary Sidon unions. The phase-transition parameter is the number of satellite characters, not a universal stability cutoff for other geometries. Historical equivalent descriptions or stronger general decoupling theorems may exist; external independent verification remains outstanding.

## References
1. W. Burstein, A. Iosevich, B. Krause, *Bourgain's Lambda(p) selection theorem: a greedy proof with polynomial failure bounds*, first posted 2026-09-11, arXiv:2609.12566, https://arxiv.org/abs/2609.12566.
2. I. Klemes, *Examples of Lambda(4) sets E and a graph structure in E x E*, Studia Mathematica 133 (1999), 101–120, https://bibliotekanauki.pl/articles/1216952.pdf.
