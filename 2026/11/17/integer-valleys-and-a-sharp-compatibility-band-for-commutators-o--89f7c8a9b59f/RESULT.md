# Integer valleys and a sharp compatibility band for commutators of equal-rank orthogonal projections

## Finding

For a real or complex Hilbert space \(H\) of dimension \(n\ge 2k\), fix an integer \(k\ge1\). Let \(P,Q\) range over **orthogonal** projections of rank \(k\) (not arbitrary idempotents), and define the normalized squared chordal distance and operator-norm commutator by
\[
D(P,Q)=\frac12\|P-Q\|_{\mathrm F}^{2}=k-\operatorname{Tr}(PQ),\qquad C(P,Q)=\|PQ-QP\|.
\]
Here \(\|\cdot\|_{\mathrm F}\) is the Hilbert–Schmidt (Frobenius) norm. Exactly the following complete compatibility band is attained:
\[
\{C(P,Q):D(P,Q)=d\}=[L_k(d),U_k(d)]\quad (0\le d\le k).
\]
When \(d\in\{0,1,\ldots,k\}\), \(L_k(d)=0\). Otherwise set \(m=\lfloor d\rfloor\), \(\delta=d-m\in(0,1)\), and
\[
a_k(d)=\min\!\left\{\frac{\delta}{k-m},\frac{1-\delta}{m+1}\right\},\qquad
L_k(d)=\sqrt{a_k(d)(1-a_k(d))}.
\]
The upper boundary is
\[
U_k(d)=
\begin{cases}
\sqrt{d(1-d)},&0\le d\le1/2,\\
1/2,&1/2\le d\le k-1/2,\\
\sqrt{(k-d)(d-k+1)},&k-1/2\le d\le k.
\end{cases}
\]
The middle interval is a single point if \(k=1\). In every cell \(m\le d\le m+1\), where \(0\le m<k\), the lower envelope has exactly one interior maximum,
\[
d_m^*=\frac{k(m+1)}{k+1},\qquad L_k(d_m^*)=\frac{\sqrt{k}}{k+1}.
\]
In particular, prescribed noninteger chordal distance forces a positive commutator, whereas at every integer distance commuting projection pairs exist. The common valley-peak height decays as the rank grows.

## Assumptions and scope

All norms are the usual matrix operator and Frobenius norms. Dimension \(n\ge2k\) ensures that every list of \(k\) principal angles between rank-\(k\) ranges is geometrically realizable. The result applies over \(\mathbb R\) and \(\mathbb C\); no hypothesis of generic position is made, and zero or right principal angles are allowed. No infinite-dimensional claim or nonorthogonal-idempotent claim is made.

For \(d=m+\delta\) with \(0<\delta<1\), the minimizing principal-angle multiset is completely determined as follows, with \(t_j=\sin^2\theta_j\). If \(\delta/(k-m)<(1-\delta)/(m+1)\), it consists of \(m\) ones and \(k-m\) copies of \(\delta/(k-m)\). If the reverse strict inequality holds, it consists of \(k-m-1\) zeros and \(m+1\) copies of \(1-(1-\delta)/(m+1)\). At equality of the fractions, both listed multisets minimize, and there are no others up to permutation. At integer \(d\), minimizers have exactly \(d\) ones and \(k-d\) zeros. The upper envelope is attained if and only if some \(t_j=1/2\) in the middle plateau; in the two exterior ranges its nontrivial component has \(t_j=d\) or \(t_j=d-k+1\), respectively, while the rest are at zero or one.

## Proof

**1. Principal-angle reduction.** The classical two-projection decomposition gives \(k\) angles \(0\le\theta_j\le\pi/2\). Set \(t_j=\sin^2\theta_j\in[0,1]\). The corresponding \(2\times2\) blocks may be taken as
\[
P_j=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
Q_j=\begin{pmatrix}1-t_j&\sqrt{t_j(1-t_j)}\\\sqrt{t_j(1-t_j)}&t_j\end{pmatrix}.
\]
They obey \(P_j^2=P_j=P_j^*\) and \(Q_j^2=Q_j=Q_j^*\). The squared Frobenius distance on each block is \(2t_j\); its commutator is skew-adjoint with off-diagonal entries \(\pm\sqrt{t_j(1-t_j)}\). Consequently
\[
D=\sum_{j=1}^k t_j,\qquad C=\max_{1\le j\le k}\sqrt{t_j(1-t_j)}.
\]
Conversely every \(t\in[0,1]^k\) is realized by taking the block direct sum and padding zero operators on \(H\ominus\mathbb F^{2k}\). Thus no spectra or angular configurations are lost.

**2. Upper envelope.** At fixed \(\sum_j t_j=d\), the possible value of any one coordinate is the entire interval \([\max(0,d-k+1),\min(1,d)]\), since the other \(k-1\) coordinates can fill the remaining sum. The concave parabola \(t(1-t)\) is maximized on this interval at the point nearest \(1/2\). This gives precisely the three stated branches of \(U_k\). At every branch, the remaining coordinates realize the required sum. On the middle plateau a coordinate exactly equal to \(1/2\) is necessary and sufficient; outside it, extremality forces the other coordinates to the indicated endpoints.

**3. Lower envelope.** If \(C\le c\le1/2\), set \(a=(1-\sqrt{1-4c^2})/2\in[0,1/2]\). The inequality \(t_j(1-t_j)\le c^2\) is equivalent to
\[
t_j\in[0,a]\ \cup\ [1-a,1].
\]
If exactly \(j\) of the \(k\) coordinates belong to the upper interval, their sum lies in
\[
[j(1-a),\ j+(k-j)a].
\]
Write \(d=m+\delta\) with \(0<\delta<1\). For \(j\le m\), feasibility implies
\[
a\ge\frac{d-j}{k-j}\ge\frac{d-m}{k-m}=\frac{\delta}{k-m},
\]
because the fraction decreases in \(j\) for \(d<k\). For \(j\ge m+1\), feasibility implies
\[
a\ge\frac{j-d}{j}\ge\frac{m+1-d}{m+1}=\frac{1-\delta}{m+1},
\]
since that fraction increases in \(j\) for \(d>0\). The smaller of these two bounds is therefore necessary, and no other count \(j\) can improve it. The smaller bound is at most \(1/(k+1)\), so is strictly below \(1/2\) except in the degenerate case \(k=1\), where it is still at most \(1/2\). It is attained by the two configurations in the assumptions section, with each bound achieved by its respective configuration. The function \(\sqrt{a(1-a)}\) is increasing for \(0\le a\le1/2\), completing the minimum formula. When the smaller bound is strict, the count \(j\) and all of its coordinates must saturate the displayed inequality; this proves the equality classification, including the two-pattern crossover. At integer \(d\), zero commutator occurs exactly when all \(t_j\in\{0,1\}\).

**4. Every intermediate value.** The fixed-sum polytope \(\{t\in[0,1]^k:\sum_jt_j=d\}\) is nonempty and convex, hence path connected. The function \(t\mapsto\max_j\sqrt{t_j(1-t_j)}\) is continuous; since it attains the stated minimum and maximum, its image is their entire closed interval. The block construction realizes every image value as a pair of projections.

**5. Integer-cell peaks.** For \(d=m+\delta\) the two candidates in \(a_k(d)\) are respectively strictly increasing and strictly decreasing in \(\delta\), and meet uniquely when
\[
\frac{\delta}{k-m}=\frac{1-\delta}{m+1}
\quad\Longleftrightarrow\quad\delta=\frac{k-m}{k+1}.
\]
Their common value is \(1/(k+1)\). Therefore \(L_k\) increases then decreases across the cell with the unique peak at \(d=k(m+1)/(k+1)\) and height \(\sqrt{k}/(k+1)\).

## Verification

Run `python check_projection_envelopes.py` using Python 3; NumPy enables additional explicit matrix tests. The included script independently assembles all minimum and maximum principal-angle patterns, checks exact rank-cell locations and evaluates random fixed-sum samples. During preparation, it passed 110,065 scalar/constructor/cell-peak tests and, with NumPy, 1,800 additional direct real matrix projection/commutator tests. These finite calculations are reproducibility stress tests, **not** a substitute for the preceding all-rank proof. All displayed claims, including the full interval and equality cases, are analytic.

## Relationship to prior work

The two-projection canonical-angle decomposition is classical, and none of its formulas is claimed as new. Aouichaoui (2026) gives sharp additive/multiplicative lengths for commutators of arbitrary idempotents; the present question instead fixes **orthogonal** projection ranks and their squared chordal distance. Loring (2013/2014) proves principal-angle normal forms and norm-controlled approximations by commuting projections, but studies an operator-norm perturbation objective rather than the exact joint \((D,C)\) compatibility band with rank-dependent integer valleys. Bourin and Lee (2026) rederive principal-angle normal forms and operator-norm identities; their stated corollaries do not give the fixed-trace extremization. Conde (2022) studies general commutator norm inequalities without this explicit fixed-trace envelope in the accessible text. The new portion is the complete conditional interval, both endpoints, all lower extremizer patterns, and the equal-height interior peaks.

## Limitations

No claim of optimality beyond the prescribed rank/distance problem is made. The ambient-dimension hypothesis is essential for the assertion that all \(k\)-tuples of angles occur; when \(n<2k\), forced intersections change the admissible region. Only real/complex finite-dimensional Hilbert geometry is treated. The novelty comparison is bibliographic best knowledge, not an exhaustive uniqueness certificate: older material expressing the same conditional optimization under an equivalent principal-angle constraint may exist. A source with relevant commutator inequalities (Conde, 2022) could not be inspected in full; the available landing-page text, not its inaccessible body, informed the comparison.

## References

1. M. A. Aouichaoui, *Optimal lengths of commutators of idempotents and similarity of nilpotent operators to their negatives*, arXiv:2611.01316v1 (31 Oct 2026), https://arxiv.org/html/2611.01316v1.
2. T. A. Loring, *Principal angles and approximation for quaternionic projections*, Ann. Funct. Anal. 5 (2014), 176–187, https://arxiv.org/abs/1306.1923.
3. J.-C. Bourin and E.-Y. Lee, *Involutions and angles between subspaces*, arXiv:2602.19599v1 (23 Feb 2026), https://arxiv.org/html/2602.19599v1.
4. C. Conde, *A note about the norm of the sum and the anticommutator of two orthogonal projections*, J. Math. Anal. Appl. 505 (2022), 125650, https://doi.org/10.1016/j.jmaa.2021.125650.
5. E. Andruchow and M. E. Di Iorio y Lucero, *p-Schatten commutators of projections*, arXiv:2010.15726 (2020), https://arxiv.org/abs/2010.15726.
