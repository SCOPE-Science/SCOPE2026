# Zariski-chamber support polynomials on section blow-ups of Hirzebruch surfaces

## Finding
Let \(e\ge2\) and \(n\ge e+2\). Set \(r=n-e\). On the Hirzebruch surface \(\mathbb F_e\), fix a negative section \(S_0\) with \(S_0^2=-e\), a ruling class \(F\), and a smooth disjoint section \(S_+\sim S_0+eF\). Let \(X_{e,n}\) be the blow-up at \(n\) distinct points on \(S_+\). Define \(Z_{e,n}(t)=\sum_{j\ge0}z_jt^j\), where \(z_j\) counts Zariski chambers whose negative part has support of cardinality \(j\), and the nef chamber contributes \(1\). Then

\[
\begin{aligned}
Z_{e,n}(t)={}&(1+2t)^n\\
&+t\sum_{f=0}^{e-1}\binom nf t^f(1+t)^{n-f}\\
&+t\sum_{a=0}^{r-1}\binom na t^a(1+t)^{n-a}\\
&+t^2\sum_{f=0}^{e-1}\sum_{a=0}^{r-1}\binom nf\binom{n-f}{a}t^{f+a}.
\end{aligned}
\]

The maximal support has size \(n+1\), attained in exactly
\[
\sum_{f=0}^{e-1}\binom nf+\sum_{a=0}^{r-1}\binom na=2^n-\binom ne
\]
chambers, and \(Z_{e,n}(t)=Z_{n-e,n}(t)\). In particular,
\[
Z_{2,4}(t)=1+10t+41t^2+76t^3+60t^4+10t^5,
\]
so \(X_{2,4}\) has exactly \(198\) chambers. Other examples are \(Z_{2,5}(1)=618\), \(Z_{3,6}(1)=2004\), and \(Z_{4,8}(1)=19526\).

## Assumptions and scope
The base field is \(\mathbb C\). The points are distinct and lie on \(S_+\), hence on distinct fibers. No general-position assumption is needed among those points. The term *Zariski chamber* refers to the decomposition of the big cone of the smooth blow-up by supports of negative parts, as in Bauer–Funke–Neumann. The theorem does not concern Mori chambers or volumes of individual chambers. The range \(e\ge2\), \(r\ge2\) isolates the genuinely two-weight family; the boundary \(e=1\) is the almost-collinear plane blow-up case.

## Proof
Write \(\pi:X_{e,n}\to\mathbb F_e\). Denote the exceptional curves by \(E_i\), and the strict transforms of the fibers through the blown-up points by \(G_i=\pi^*F_i-E_i\). Let \(A\) and \(B\) be the strict transforms of \(S_0\) and \(S_+\), respectively. Their self-intersections are
\[
A^2=-e,\quad B^2=e-n=-r,\quad E_i^2=G_i^2=-1.
\]
We first prove that these \(2n+2\) curves are **all** the negative irreducible curves on \(X_{e,n}\). A fiber either misses the centers, in which case its transform has square zero, or is one of the \(G_i\). It remains to consider an irreducible curve \(C\) on \(\mathbb F_e\) distinct from \(S_0\), \(S_+\), and every fiber. Its class is \(aS_0+bF\) with \(a\ge1\). Since \(C\) and \(S_0\) are distinct effective curves, \(C\cdot S_0=b-ea\ge0\). If \(m_i\) is its multiplicity at the center \(p_i\), intersection with the distinct fiber \(F_i\) implies \(m_i\le C\cdot F_i=a\). Intersection with the distinct section \(S_+\) implies \(\sum_i m_i\le C\cdot S_+=b\). Thus
\[
\widetilde C^{\,2}=-ea^2+2ab-\sum_i m_i^2
\ge -ea^2+2ab-a\sum_i m_i
\ge a(b-ea)\ge0.
\]
So no further negative curves occur. This argument also excludes negative strict transforms of arbitrary multisections and of other sections, not merely additional rational curves.

The complete nonzero off-diagonal pairings of the negative curves are
\[
A\cdot G_i=1,\qquad B\cdot E_i=1,\qquad E_i\cdot G_i=1
\]
for each \(i\); every other pair of distinct listed curves has intersection zero. In particular, \(A\cdot B=0\). A negative-definite support cannot contain both \(E_i\) and \(G_i\), since the principal intersection submatrix \(\bigl(\begin{smallmatrix}-1&1\\1&-1\end{smallmatrix}\bigr)\) has determinant zero. Accordingly each \(i\) contributes at most one leaf, chosen from \(E_i,G_i\).

Let \(f\) be the number of chosen \(G_i\) and \(a\) the number of chosen \(E_i\). With the chosen leaves ordered last, their intersection block is \(-I\). Taking its Schur complement gives the central diagonal entry \(-e+f\) if \(A\) is selected, and \(-r+a\) if \(B\) is selected. The off-diagonal central entry remains zero, because \(A\cdot B=0\) and no leaf meets both. Hence the support is negative definite exactly when \(f<e\) whenever \(A\) is selected, and \(a<r\) whenever \(B\) is selected. If a section is not selected, the associated inequality is absent.

By the negative-definite-support characterization of Zariski chambers [1, Proposition 1.1], every such support gives exactly one chamber, including the empty support. If neither section is selected, each index permits an absent leaf or one of the two leaves, giving \((1+2t)^n\). If only \(A\) is selected, choose \(f<e\) of the \(G_i\), and choose independently whether to include \(E_i\) among the remaining positions: this gives \(t\sum_{f<e}\binom nf t^f(1+t)^{n-f}\). The case of \(B\) alone is analogous with \(a<r\). If both are present, choose disjoint index sets of sizes \(f<e\) and \(a<r\), yielding the double sum with coefficient \(\binom nf\binom{n-f}a\). These four disjoint cases give the claimed polynomial.

Any support uses at most one leaf per index. With neither section it has size at most \(n\); with exactly one selected it has size at most \(n+1\); with both selected it has at most \((e-1)+(r-1)+2=n\) curves. For size \(n+1\), only the single-section cases contribute, with every index occupied. This gives the leading coefficient above, which equals \(2^n-\binom ne>0\) by the binomial theorem and \(\binom{n}{a}=\binom{n}{n-a}\). Exchanging \(A\leftrightarrow B\) and \(E_i\leftrightarrow G_i\), and simultaneously \(e\leftrightarrow r\), preserves the entire support test. This proves the polynomial symmetry, also reflecting the elementary transformation that contracts the \(G_i\) to produce \(\mathbb F_{n-e}\).

## Verification
The standalone standard-library program `VERIFIER.py` constructs the full integral intersection matrix on \(2n+2\) vertices and tests negative definiteness of every principal submatrix using exact rational elimination, independently of the formula's threshold argument. It compares all coefficients for \(3\le n\le6\) and every \(1\le e<n\), including the boundary cases as additional checks. It independently checks symmetry, the leading coefficient, and the vanishing coefficient of degree \(n+2\). Run with `python3 VERIFIER.py`; its recorded output is in `VERIFIER_OUTPUT.txt`. For the theorem's first non-boundary case \((e,n)=(2,4)\), the enumerated coefficients are \((1,10,41,76,60,10)\). Finite checks do not replace the proof for arbitrary \(e,n\).

## Relationship to prior work
Bauer–Funke–Neumann [1] proves that Zariski chambers correspond to negative-definite supports and computes smooth del Pezzo examples, not this ruled-surface family. Bauer–Schmitz [2] gives a general exact enumeration algorithm, but not this two-parameter closed support polynomial. De la Rosa-Navarro, Frías-Medina and Lahyane [3] analyze effective, nef and semi-ample monoids on related Hirzebruch blow-ups; its accessible abstract reports those cone descriptions but no chamber polynomial. Its full text could not be materially compared, so prior coverage within that paper remains an explicit historical risk. Brodie–Constantin [4] studies cohomology/Zariski chambers on various complex surfaces, including an isolated toric blow-up example, but does not present this section-blow-up family in its available full text. The \(e=1\) specialization is geometrically the almost-collinear plane blow-up; the point of the theorem is the two-weight \(e,r\ge2\) profile, including the reciprocal-section symmetry and exact leading coefficient. A general algorithm plus a list of negative classes does not by itself state the all-parameter closed support polynomial: the classification and Schur-complement count provide the missing implication.

## Limitations
Historical priority is provisional, particularly because [3] was accessible only at abstract level. The formula applies to points on a single smooth section and does not treat arbitrary point configurations or infinitely-near centers. It counts chamber supports, not chamber volumes, wall adjacencies, or arbitrary base-point behavior. The proof is over \(\mathbb C\), matching the cited chamber correspondence. Independent mathematical audit is not claimed.

## References
[1] T. Bauer, M. Funke, S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958v1 (first public 2009-12-04), Proposition 1.1.

[2] T. Bauer, D. Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373v1 (first public 2012-04-19), Section 1.

[3] B. L. de la Rosa-Navarro, J. B. Frías-Medina, M. Lahyane, *On the effective, nef, and semi-ample monoids of blowups of Hirzebruch surfaces at collinear points*, Canadian Mathematical Bulletin 66 (2023), 1179–1193, doi:10.4153/S0008439523000255 (abstract consulted; full text inaccessible).

[4] C. R. Brodie, A. Constantin, *Cohomology Chambers on Complex Surfaces and Elliptically Fibered Calabi–Yau Three-Folds*, Communications in Mathematical Physics 405 (2024), article 151, doi:10.1007/s00220-024-05055-x.
