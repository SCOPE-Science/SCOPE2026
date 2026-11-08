# Resonant cubic singular-value decay for critical Fock integral commutators

## Finding

Let \(\mathcal F^2\) be the one-variable Gaussian Bargmann–Fock Hilbert space. For integers \(h\ge1\) and \(j\ge0\), put
\[
A_{h,j}=I^{h+j}M_{z^h}D^j,
\]
where \(I f(z)=\int_0^z f(w)\,dw\), \(Df=f'\), and \(M_{z^h}f=z^h f\). These operators have bounded, noncompact extensions on \(\mathcal F^2\).

Take any **distinct** pairs of integers \((h_1,j_1)\) and \((h_2,j_2)\) in this range; define \(K=A_{h_1,j_1}A_{h_2,j_2}-A_{h_2,j_2}A_{h_1,j_1}\) and \(\lambda_i=h_i+2j_i\). All such commutators are compact, infinite-rank weighted shifts. Their **exact leading singular-value laws** are
\[
 s_n(K)\sim
 \begin{cases}
 h_1h_2|\lambda_1-\lambda_2|\,n^{-2},&\lambda_1\ne\lambda_2,\\[2pt]
 \frac{h_1h_2}{2}|h_1^2-h_2^2|\,n^{-3},&\lambda_1=\lambda_2.
 \end{cases}
\]
In the second case distinctness forces \(h_1\ne h_2\), so both displayed leading coefficients are strictly positive in their respective cases.

Let \(r=2\) in the nonresonant case and \(r=3\) in the resonant case, with \(C\) the corresponding positive leading coefficient. Then for every real \(p>0\),
\[
 K\in\mathcal S_p\quad\Longleftrightarrow\quad p>1/r,
\qquad K\in\mathcal S_{1/r,\infty}\setminus\mathcal S_{1/r},
\]
and the critical logarithmic spectral sum has the exact coefficient
\[
 \lim_{N\to\infty}\frac1{\log N}\sum_{n=1}^{N}s_n(K)^{1/r}=C^{1/r}.
\]
If the two pairs coincide, the commutator is identically zero; the theorem otherwise concerns only \(h_i\ge1\).

## Assumptions and scope

Use the normalization
\[
 \|f\|_{\mathcal F^2}^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z),
 \qquad e_k(z)=\frac{z^k}{\sqrt{k!}},\quad k\ge0.
\]
These monomials form a complete orthonormal basis. Initially define each \(A_{h,j}\) on polynomials and take its unique bounded extension. Integration starts at \(0\). The result is for the complex Hilbert space, integer indices, and commutator products as ordered above. No statement is made about arbitrary nonmonomial coefficient vectors or other Fock–Sobolev norms.

## Proof

**1. Exact monomial coefficients and boundedness.** For \(k\ge j\), differentiation, multiplication, and \(h+j\) integrations give
\[
 A_{h,j}e_k=w_{h,j}(k)e_{k+2h},\quad
 w_{h,j}(k)=\frac{\prod_{u=1}^{h}(k-j+u)}{\sqrt{\prod_{u=1}^{2h}(k+u)}}.
\]
For \(k<j\), the image is zero. In particular \(w_{h,j}(k)>0\) for \(k\ge j\) and \(w_{h,j}(k)\to1\) as \(k\to\infty\). Since distinct input basis vectors have orthogonal outputs, each operator extends boundedly; its weights tending to one also show that it is noncompact.

**2. The commutator is a single weighted shift.** Write \(w_i=w_{h_i,j_i}\), extended by zero below \(j_i\). Then for every \(k\ge0\),
\[
 Ke_k=d(k)e_{k+2(h_1+h_2)},\quad
 d(k)=w_2(k)w_1(k+2h_2)-w_1(k)w_2(k+2h_1).
\]
Consequently \(K^*K e_k=|d(k)|^2e_k\). Its nonzero singular values, with multiplicities, are exactly the nonincreasing rearrangement of \((|d(k)|)_{k\ge0}\).

**3. Controlled logarithmic expansion.** For each fixed integer pair \(h\ge1\), \(j\ge0\), expand the finite products at \(k=\infty\):
\[
 \log w_{h,j}(k)=\frac{\alpha_{h,j}}k+\frac{\beta_{h,j}}{k^2}+O(k^{-3}),
\quad
 \alpha_{h,j}=-\frac{h(h+2j)}2,
\quad
 \beta_{h,j}=\frac{h(2h^2+2hj+h-2j^2+2j)}4.
\]
Indeed, the coefficients are respectively the first and negative half the second power sums of \((u-j)_{u=1}^h\), with half the corresponding power sums of \((u)_{u=1}^{2h}\) subtracted, as follows immediately from \(\log(1+t)=t-t^2/2+O(t^3)\). All error constants may depend on the fixed integer parameters.

For sufficiently large \(k\), set
\[
 P(k)=w_2(k)w_1(k+2h_2),\qquad
 Q(k)=w_1(k)w_2(k+2h_1).
\]
Because the unshifted logarithms cancel,
\[
 \log\frac{P(k)}{Q(k)}
 =\frac{E_2}{k^2}+\frac{E_3}{k^3}+O(k^{-4}),
\]
where
\[
 E_2=-2h_2\alpha_1+2h_1\alpha_2
 =h_1h_2(\lambda_1-\lambda_2),
\]
\[
 E_3=4h_2^2\alpha_1-4h_2\beta_1-4h_1^2\alpha_2+4h_1\beta_2.
\]
This requires the third-order expansion of the finite logarithmic products to control the remainder; their unshifted third-order terms cancel in the difference. These are ordinary convergent Taylor expansions for sufficiently large \(k\).

**4. Nonresonance and resonance.** If \(\lambda_1\ne\lambda_2\), then \(E_2\ne0\), and since \(P(k),Q(k)\to1\),
\[
 d(k)=E_2 k^{-2}+O(k^{-3}).
\]
If \(\lambda_1=\lambda_2=\lambda\), then \(E_2=0\). Substituting \(j=(\lambda-h)/2\) simplifies the second logarithmic coefficient to
\[
 \beta_{h,j}=\frac h8\left(h^2+4h\lambda+2\lambda-\lambda^2\right).
\]
Inserting this and \(\alpha_{h,j}=-h\lambda/2\) into \(E_3\) yields exactly
\[
 E_3=-\frac{h_1h_2}{2}(h_1^2-h_2^2).
\]
Distinctness and resonance imply \(h_1\ne h_2\), hence \(E_3\ne0\), and
\[
 d(k)=E_3 k^{-3}+O(k^{-4}).
\]
Both cases therefore have nonzero leading coefficients, and their commutators are compact of infinite rank.

**5. Sorting the singular values and the endpoint.** If a positive sequence satisfies \(a_k=Ck^{-r}(1+o(1))\) with \(C>0\), then its counting function obeys \(\#\{k:a_k>t\}\sim(C/t)^{1/r}\) as \(t\downarrow0\), by comparison with \((1\pm\delta)Ck^{-r}\) beyond a fixed cutoff. Its nonincreasing rearrangement is therefore asymptotic to \(Cn^{-r}\), irrespective of finitely many initial entries. Apply this to \(a_k=|d(k)|\). Summability of \(\sum_n s_n(K)^p\) is then equivalent to \(rp>1\), and at \(p=1/r\), the summands satisfy \(s_n(K)^{1/r}\sim C^{1/r}/n\); elementary logarithmic Cesàro averaging proves the final limit.

## Verification

The included standard-library Python program `CHECK.py` evaluates exact rational monomial-normalization identities and the logarithmic power-sum coefficients over finite grids, checks the two algebraic cancellation regimes on parameter pairs, and compares high-precision sample commutator weights with their asymptotic coefficients. Execute `python3 CHECK.py`. Its reported counts are 1,470 exact monomial identities, 98 exact logarithmic coefficient identities, 2,352 algebraic pair checks, and 12 asymptotic numerical corroborations. The infinite-dimensional assertions are proved above, not inferred from those finite computations.

## Relationship to prior work

Dong and Hu (2026) introduce this class of generalized Fock–Sobolev integrals and derive critical monomial weighted-shift formulas and essential norms. Their first-order compact-perturbation theory proves that the critical operators are represented by Laurent Toeplitz shifts in the Calkin algebra, but it does not determine the sharp singular-value decay of their products' commutators or the exceptional resonance. In fact, formula (50) of their paper is the starting monomial identity here; it is not presented as new.

Alpay–Cerejeiras–Kähler–Kling (2022) develop commutator calculus for integration and backward-shift pairs and generalized derivatives, not the present two-level Schatten classification for pairs of critical iterated-integral operators. Mengestie (2017), Mengestie–Worku (2018) and Biya (2023) treat boundedness, differences and Schatten properties of other Volterra/integral families, without a corresponding commutator resonance theorem in the inspected results. Pushnitski (2017, Theorem 1.2) establishes a general banded-matrix singular-asymptotic theorem: it provides broader spectral machinery *once a nonzero leading coefficient has been computed*, but neither its hypotheses nor its conclusions identify this family-specific cancellation law. The independent proof above uses the exact one-diagonal shift form instead.

## Limitations

The theorem concerns one-variable Gaussian Fock space only, monomial coefficients with integer parameters, and commutators of precisely two critical operators. It does not establish higher nested commutator asymptotics, general polynomial-symbol cancellation criteria, or results on weighted Fock–Sobolev spaces with positive Sobolev order. The asymptotic formulas give leading terms rather than every finite singular value. There may be an older, more general symbolic-calculus identity that implies the resonance algebra; publication-priority verification remains qualified rather than absolute. A related 2023 thesis was inspected using searchable full-text extraction; independent page-image retrieval was unavailable.

## References

1. J. Dong and S. Hu, *Carleson Measures and Integral Operators on Fock–Sobolev Spaces*, arXiv:2611.01959v1 (publicly submitted 2026-11-01), Sections 1.2 and 4.2, especially formula (50). https://arxiv.org/html/2611.01959v1
2. D. Alpay, P. Cerejeiras, U. Kähler and T. Kling, *Commutators on Fock spaces*, arXiv:2208.03394v1 (2022). https://arxiv.org/html/2208.03394v1
3. T. Mengestie, *Spectral properties of Volterra-type integral operators on Fock–Sobolev spaces*, arXiv:1702.08157v1 (2017). https://arxiv.org/abs/1702.08157
4. T. Mengestie and M. Worku, *Topological structures of generalized Volterra-type integral operators*, arXiv:1802.08414v1 (2018). https://arxiv.org/abs/1802.08414
5. A. Pushnitski, *Spectral asymptotics for a class of Toeplitz operators on the Bergman space*, arXiv:1710.02652v1 (2017), Theorem 1.2. https://arxiv.org/abs/1710.02652
6. K. Biya, *Schatten Class Generallized Integration Operators on Fock Spaces*, M.Sc. thesis, Jimma University (2023), Theorem 4.0.6. https://repository.ju.edu.et/handle/123456789/8787
