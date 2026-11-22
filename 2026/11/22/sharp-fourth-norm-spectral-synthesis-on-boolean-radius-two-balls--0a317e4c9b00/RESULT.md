# Sharp fourth-norm spectral synthesis on Boolean radius-two balls

## Finding

Let \(d\ge2\), \(G_d=(\mathbb Z/2\mathbb Z)^d\), and \(S_d=\{x\in G_d:|x|\le2\}\), where \(|x|\) is Hamming weight. Equip the Fourier side with **counting** \(\ell^4\) norm and use the unitary Walsh transform
\[
\widehat f(\xi)=2^{-d/2}\sum_{x\in G_d}f(x)(-1)^{x\cdot\xi}.
\]
Set \(m=d+1\), \(n=\binom m2\), and
\[
t_j=\frac{(m-2j)^2-m}{m(m-1)}\quad(0\le j\le m),\qquad
M_m(u)=2^{-m}\sum_{j=0}^m\binom mj(1-u+ut_j)^4.
\]
Let \(u_m>0\) denote the unique real solution of the **explicit cubic equation**
\[
\sum_{j=0}^m\binom mj(1-t_j)(1-u+ut_j)^3=0.
\]
Then the exact sharp synthesis constant is
\[
\boxed{\mathcal C_4(S_d):=\sup_{0\ne f:\operatorname{supp}f\subseteq S_d}
\frac{\|\widehat f\|_{\ell^\infty}}{\|\widehat f\|_{\ell^4}}
=2^{-d/4}M_m(u_m)^{-1/4}.}
\]
Every nonzero complex extremizer, and no other one, is a scalar multiple of a character modulation of the following real two-level function:
\[
g_m(x)=\begin{cases}
1-u_m,&x=0,\\
u_m/n,&|x|=1\text{ or }2,\\0,&|x|>2.
\end{cases}
\]
In particular, the center weight \(1-u_m\) is strictly positive for \(2\le d\le4\) and strictly negative for every \(d\ge5\). The noncentral weights are positive in every dimension. Thus the support indicator ceases to be optimal before the origin coefficient changes sign.

There is also a sharp high-dimensional law. Let \(v>0\) be the unique positive root of \(v^3+6v-8=0\) (\(v=1.1071475644\ldots\)). Then
\[
u_m=1+\frac{v}{m}+o(m^{-1}),\qquad
\mathcal C_4(S_d)=2^{-d/4}\frac{d+1}{(60-32v+12v^2+v^4)^{1/4}}(1+o(1)).
\]

## Assumptions and scope

The result holds for all integers \(d\ge2\), arbitrary complex Fourier coefficients supported on the complete *radius-two* Hamming ball, and unitary Walsh normalization with counting norms. The quotient is invariant under nonzero scalar multiplication. No positivity assumption is imposed on \(f\); indeed the optimizer is signed for \(d\ge5\). The stated dimension asymptotic keeps the Hamming radius fixed while \(d\to\infty\).

## Proof

**1. Hidden edge-orbit symmetry.** Identify \(G_d\) linearly with the even-parity subspace \(V\) of \(\mathbb F_2^m\) using
\[
(x_1,\ldots,x_d)\longmapsto(x_1,\ldots,x_d,x_1+\cdots+x_d).
\]
The nonzero points of \(S_d\) become precisely the vectors \(e_i+e_j\) for \(1\le i<j\le m\), i.e. the edges of a complete graph on \(m\) vertices. The coordinate-permutation group \(\mathfrak S_m\) acts by invertible linear maps on \(V\), fixes \(0\), and acts transitively on the \(n\) edges.

**2. Strict convexity and all equality cases.** Modulate an arbitrary \(f\) so that a Fourier coefficient of largest modulus occurs at frequency \(0\), and scale it to ensure \(\sum_x f(x)=1\). The functional \(f\mapsto2^{-d}\sum_{\xi}|\sum_x f(x)(-1)^{x\cdot\xi}|^4\) is strictly convex on this complex affine hyperplane: fourth-power modulus is strictly convex in \(\mathbb C\), and the Walsh transform is injective. Hence it has a unique minimizer. The objective and normalization are invariant under \(\mathfrak S_m\), so uniqueness forces the minimizer to be constant on each of the two support orbits. Complex conjugation also preserves the objective and normalization, hence both levels are real. Write the origin weight as \(a=1-u\) and every edge weight as \(b=u/n\). Strict convexity also proves that every extremizer, after normalization and modulation, coincides with this unique profile.

**3. Exact Fourier moment.** The characters of the even-parity subspace correspond to sign vectors \(\eta\in\{\pm1\}^m\) modulo simultaneous sign reversal. For \(j\) negative signs, the sum of characters over all edges is
\[
E_j=\sum_{i<k}\eta_i\eta_k=\frac{(m-2j)^2-m}{2}=nt_j.
\]
Therefore the unnormalized Fourier value of the two-level function is \(1-u+ut_j\). The uniform dual average of its fourth power equals \(M_m(u)\); the factor \(2^{-m}\binom mj\) is valid because every dual character is represented by exactly two sign vectors. Since the unitary transform contributes a common factor \(2^{-d/2}\), converting the dual average to counting \(\ell^4\) norm gives \(\mathcal C_4(S_d)=2^{-d/4}(\min_u M_m(u))^{-1/4}\).

**4. Cubic and uniqueness.** Differentiation yields
\[
M_m'(u)=-4\,2^{-m}\sum_{j=0}^m\binom mj(1-t_j)(1-u+ut_j)^3.
\]
The real quartic \(M_m\) is strictly convex, as follows either from Step 2 or because at least one \(1-t_j\ne0\). It tends to infinity with \(|u|\), and \(M_m'(0)=-4\), so its unique critical point \(u_m\) is positive. This proves the formula and all complex extremizers.

**5. Exact center-sign threshold.** Let \(E=\sum_{i<j}\eta_i\eta_j\) with independent uniform signs and \(n=\binom m2\). Character orthogonality and elementary even-degree subgraph counting give
\[
\mathbb E E^2=n,\quad \mathbb E E^3=6\binom m3,\quad
\mathbb E E^4=3n^2-2n+72\binom m4.
\]
Indeed a triple of distinct edges contributes only if it forms a triangle, and a quadruple of distinct edges contributes only if it forms a four-cycle (three cycles per four vertices); the repeated-edge pairings contribute \(3n^2-2n\). Since \(t=E/n\),
\[
M_m'(1)=4(\mathbb E t^4-\mathbb E t^3)
=-\frac{m(m-1)}{n^4}\left(2m^3-21m^2+67m-68\right).
\]
The cubic in parentheses is negative at \(m=3,4,5\), positive at \(m=6\), and strictly increasing for every real \(m\ge6\) (its derivative is \(6m^2-42m+67>0\) there). Strict convexity implies \(u_m<1\) for \(3\le m\le5\), but \(u_m>1\) for \(m\ge6\). Since \(m=d+1\), this is precisely the claimed threshold.

**6. Dimension limit.** For independent Rademacher signs put \(W_m=m^{-1/2}\sum_i\eta_i\). Then \(mt=m(W_m^2-1)/(m-1)\) converges in all fixed moments to \(H=Z^2-1\), where \(Z\) is standard normal. The competitor \(u=1\) has \(M_m(1)=O(m^{-4})\). By \(\mathbb E|F|^4\ge(\mathbb E|F|^2)^2\) and \(\mathbb E F^2=(1-u)^2+u^2/n\), the minimizer obeys \(u_m=1+O(m^{-1})\). Set \(v_m=m(u_m-1)\), so every subsequential limit minimizes \(\mathbb E(H-v)^4\). The latter strictly convex quartic is
\[
Q(v)=60-32v+12v^2+v^4,
\]
whose unique minimizer satisfies \(v^3+6v-8=0\). Thus \(v_m\to v\), \(m^4M_m(u_m)\to Q(v)\), and the sharp asymptotic formula follows.

## Verification

Run `python3 check.py` using Python 3's standard library. The included checker verifies the character moment identities by full finite enumeration for \(2\le m\le9\), compares exact rational direct Walsh fourth moments with the orbit formula for four rational parameters in each such dimension, and checks the center-sign and high-dimensional formulas numerically over additional dimensions. It reports `PASS: 214 exact or numerical supplementary checks`. The infinite-dimensional claims above are established by Steps 1–6; the finite checker does **not** certify the universal quantifiers by enumeration.

## Relationship to prior work

Iosevich, Li and Yu (2026) define the same counting-norm synthesis ratio for finite groups and prove an exact formula for supports having a transitive affine symmetry group. The present Hamming ball has a transparent permutation symmetry with **two** orbits, and its sharp weights are not the support indicator for \(d\ge4\), so that transitive-indicator formula does not give this constant. Their general support bounds concern a different level of precision. Bhowmik, Deodhar and Iosevich (2025) prove general finite spectral-synthesis inequalities, not the present Hamming-ball optimizer classification. Work on positive-definite Turán mass and spectral concentration of Hamming balls studies other constraints and norms and does not furnish this fourth-norm synthesis constant by a direct implication.

## Limitations

The formula concerns the fourth Fourier norm only and Boolean radius-two balls; it does not cover general Hamming radii, arbitrary frequency alphabets, or other exponents. The exact finite-dimensional constants are specified by the unique root of an explicit cubic rather than a uniform elementary radical expression. The originality comparison is based on the inspected papers and indexed mathematical records, not a proof that no equivalent theorem exists in older unindexed literature. Independent mathematical validation is not asserted.

## References

1. A. Iosevich, Z. Li, and K. Yu, *Spectral synthesis with the complexity parameter in* \(\mathbb Z_N^d\), arXiv:2609.25404v1, first publicly submitted 2026-09-21. https://arxiv.org/abs/2609.25404
2. P. Bhowmik, S. Deodhar, and A. Iosevich, *On spectral synthesis in* \(\mathbb Z_N^d\), arXiv:2508.12194v1, first publicly submitted 2025-08-17. https://arxiv.org/abs/2508.12194
3. A. Avni and A. Samorodnitsky, *Eigenvalues and eigenfunctions of a Hamming ball*, arXiv:2411.14597v1, submitted 2024-11-21. https://arxiv.org/abs/2411.14597 (a different spectral problem).
