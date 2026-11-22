# Sharp Sobolev threshold and near-Lipschitz exceptional coboundaries for constant-type rotations

## Finding
Let \(\mathbb T=\mathbb R/\mathbb Z\), and let \(R_\alpha(x)=x+\alpha\) for an irrational \(\alpha\) with bounded continued-fraction coefficients. A *real coboundary* is \(g=H\circ R_\alpha-H\), with the indicated regularity of its transfer \(H\). Define the periodic Sobolev space \(H^s(\mathbb T)\) using Fourier weights \((1+k^2)^s\).

**Theorem (sharp Sobolev boundary, with quantitative endpoint).**

1. For each \(s>1\), every real, mean-zero \(g\in H^s(\mathbb T)\) has a continuous real transfer \(H\). This holds for *every* irrational rotation of bounded continued-fraction type.
2. For each such rotation there are continuous, mean-zero \(g\in H^1(\mathbb T)\) with an \(L^2\) transfer but no continuous real transfer. In particular one can attain the exact two-sided modulus
\[
\omega_g(h)\asymp h\log\log(1/h)\quad(h\downarrow0),\qquad
\omega_g(h):=\sup_{d(x,y)\le h}|g(x)-g(y)|.
\]
Thus the exponent \(1\) is the exact Hilbert-Sobolev threshold for a universal continuous real solution among mean-zero data, with no assertion at the unrelated Lipschitz endpoint.
3. More generally, for any positive, nonincreasing sequence \((a_j)\) such that \(\sum_j a_j^2<\infty\) and \(\sum_j a_j=\infty\), an explicitly given cocycle \(g_a\in H^1\) is an \(L^2\), but not continuous, real coboundary, and its full uniform modulus is
\[
\omega_{g_a}(h)\asymp h A_{J(h)},\quad
A_J=\sum_{j=1}^J a_j,\quad J(h)=\max\{j:q_j\le1/h\}.
\]
The frequencies \((q_j)\) are a fixed regularly spaced subsequence of even convergent denominators of \(\alpha\). Consequently, for **every** nondecreasing unbounded function \(L:[1,\infty)\to(0,\infty)\), coefficients can be chosen so that this same phenomenon occurs while \(\omega_g(h)=o(h L(1/h))\). There is no universal super-Lipschitz modulus assumption, however slowly its excess over the Lipschitz scale grows, that by itself forces continuous transfer for these measurable real coboundaries.

## Assumptions and scope
The bounded-type hypothesis means there is \(c_\alpha>0\) with \(\|n\alpha\|\ge c_\alpha/|n|\) for every nonzero integer \(n\); \(\|t\|\) denotes distance to the nearest integer. Fix the standard continued-fraction convergents \(p_n/q_n\) with even indices \(n=4j+2+4J_0\), where the fixed \(J_0\) is large enough that the positive errors \(\delta_j=q_j\alpha-p_j\) all lie in \((0,1/16)\). For simplicity the denominators on this subsequence are again written \(q_j\) and errors \(\delta_j\). Bounded type gives constants, independent of \(j\), such that
\[
1<\lambda_-\le q_{j+1}/q_j\le\lambda_+<\infty,
\qquad 0<c\le q_j\delta_j\le C.
\]
These constants depend on \(\alpha\) and the chosen subsequence; all asymptotic implicit constants may also depend on \((a_j)\). No assertion is made for rotations of unbounded type, higher-dimensional tori, or circle-valued rather than real coboundary equations.

The explicit family is
\[
H_a(x)=\sum_{j\ge1}a_j\cos(2\pi q_jx)\quad\text{in }L^2(\mathbb T),
\qquad
g_a(x)=\sum_{j\ge1}a_j\bigl[\cos(2\pi(q_jx+\delta_j))-\cos(2\pi q_jx)\bigr].
\]
The latter series converges uniformly; the transfer identity is understood almost everywhere. When \(a_j=1/j\), the explicit modulus is \(h\log\log(1/h)\).

## Proof
**(I) Positive Sobolev result.** In a dyadic block \(2^r\le |k|<2^{r+1}\), the points \(k\alpha\pmod1\) are separated by at least \(c_\alpha/2^{r+1}\), and each is that far from zero up to constants. Ordering their circle distances therefore yields
\[
\sum_{2^r\le |k|<2^{r+1}}\|k\alpha\|^{-2}\le C_\alpha 2^{2r}.
\]
Since \(|e^{2\pi i k\alpha}-1|\ge4\|k\alpha\|\), for every \(s>1\),
\[
B_s:=\sum_{k\ne0}(1+k^2)^{-s}|e^{2\pi i k\alpha}-1|^{-2}<\infty.
\]
For mean-zero \(g\in H^s\), Cauchy–Schwarz gives
\[
\sum_{k\ne0}\left|\frac{\widehat g(k)}{e^{2\pi i k\alpha}-1}\right|\le B_s^{1/2}\|g\|_{H^s}<\infty.
\]
The absolutely and uniformly converging Fourier series with these coefficients defines a continuous, real \(H\) (conjugate symmetry), and the transfer identity follows from Fourier coefficients and continuity. This proves part 1 with exact quantifiers.

**(II) Endpoint family and its obstruction.** The even convergent errors and bounded type give \(\delta_j\asymp1/q_j\) and geometric growth of \(q_j\). Thus the series for \(g_a\) converges absolutely in \(C^0\); its nonzero Fourier coefficients at \(\pm q_j\) have size \(\tfrac12 a_j|e^{2\pi i\delta_j}-1|\asymp a_j/q_j\). Hence \(g_a\in H^1\) exactly when \((a_j)\in\ell^2\) in this family. The series for \(H_a\) converges in \(L^2\), and Fourier coefficients verify \(g_a=H_a\circ R_\alpha-H_a\) there.

If \(\sum_j a_j=\infty\), the Fejér means of \(H_a\) at zero obey
\[
\sigma_{2q_J}H_a(0)\ge\tfrac12\sum_{j\le J}a_j\longrightarrow\infty.
\]
The Fejér kernels are positive probability kernels, so no essentially bounded representative of \(H_a\) is possible. Any other real measurable transfer differs from \(H_a\) by an invariant measurable function, hence by a constant almost everywhere because the irrational rotation is ergodic. A continuous real transfer is therefore impossible, for \(g_a\) or any nonzero real multiple.

**(III) Exact modulus.** Use the trigonometric identity
\[
\bigl(\cos(2\pi(q_jh+\delta_j))-\cos(2\pi q_jh)\bigr)-
\bigl(\cos(2\pi\delta_j)-1\bigr)
=-4\sin(\pi\delta_j)\sin(\pi q_jh)\cos(\pi\delta_j+\pi q_jh).
\]
Splitting frequencies at \(q_j\le1/h\), and using \(\delta_j\asymp1/q_j\), gives
\[
\omega_{g_a}(h)\le C\left(h\sum_{q_j\le1/h}a_j+\sum_{q_j>1/h}\frac{a_j}{q_j}\right)
\le C'h(A_{J(h)}+a_{J(h)+1}).
\]
For \(h_J=1/(8q_J)\), all terms with \(j\le J\) have the *same negative sign* and magnitude at least \(c a_jh_J\), because \(q_jh_J\le1/8\), \(\delta_j<1/16\), and \(q_j\delta_j\ge c\). The remaining tail has total magnitude at most \(C a_{J+1}/q_{J+1}=O(h_Ja_{J+1})\). As \(A_J\to\infty\), this proves \(\omega_{g_a}(h_J)\ge c'h_JA_J\) for large \(J\). The bounded ratio \(q_{j+1}/q_j\) and monotonicity of \(\omega\) extend this to every sufficiently small \(h\), giving the stated two-sided equivalence. For \(a_j=1/j\), \(A_J\asymp\log J\) and \(J(h)\asymp\log(1/h)\).

**(IV) Arbitrary near-Lipschitz gauges.** Given nondecreasing \(L\to\infty\), choose successive integer blocks \(B_m=[N_m,N_{m+1})\) of lengths \(\ell_m\) increasing so rapidly that \(\ell_m\ge2^m\) and \(L(q_{N_m})\ge m^2\); include an initial block if necessary. Set \(a_j=1/\ell_m\) throughout \(B_m\). Then \(a_j\) is nonincreasing, \(\sum_j a_j=\infty\) (one unit of mass per block), and \(\sum_j a_j^2=\sum_m1/\ell_m<\infty\). For \(J\in B_m\), \(A_J\le m+O(1)=o(L(q_J))\). With \(q_{J(h)}\le1/h\) and the modulus upper bound, \(\omega_{g_a}(h)/(hL(1/h))\to0\). This completes all claims.

## Verification
The standalone file `verify_rotation.py` computes Fibonacci convergent identities at the golden rotation, checks positive small divisors and geometric scales, verifies sample \(H^1\) coefficient-summability proxies, and evaluates the two-sided modulus ratio for several truncation levels at high precision. The proof above supplies the infinite statements; finite truncation and numerical ratios are not used to infer universal quantifiers or asymptotic convergence.

## Relationship to prior work
Akhmedli's 2026 construction of real measurable-but-not-continuous rotation coboundaries, especially Lemma 3.3, already supplies the qualitative pathology for arbitrary irrational rotations, including all nonzero scalar multiples. This theorem does **not** claim that existence as new. It isolates the exact universal Sobolev threshold for bounded-type angles and supplies a complete explicit family of endpoint moduli and an arbitrary near-Lipschitz realization statement. The dyadic reciprocal-small-divisor estimate is essential to the global positive direction; the matched Fejér obstruction and modulus lower estimate establish the endpoint independently of finite computations. The broader cohomological-equation literature concerns different regularity and dynamical settings and remains an historical-priority qualification, not evidence of definitive uniqueness.

## Limitations
Only real-valued coboundaries for bounded-type circle rotations are classified here. The result makes no claim about uniqueness of the construction, about all possible moduli at the Lipschitz endpoint, or about nonlinear/circle-valued extensions. A direct published theorem covering the same Sobolev threshold and arbitrary-gauge realization would remove the novelty claim; the limited literature comparison cannot exclude such a historical equivalent. The explicit series establishes existence, not numerical estimates for arbitrary input moduli without specifying the chosen blocks.

## References
- Seljon Akhmedli, *Hidden frequencies in topological dynamical systems*, arXiv:2611.12722v1, first posted 9 November 2026. https://arxiv.org/abs/2611.12722 . Relevant: Sections 1 and 3, especially Lemma 3.3.
- Giovanni Forni, *Sobolev regularity of solutions of the cohomological equation*, arXiv:0707.0940 (2007); Ergodic Theory and Dynamical Systems 41 (2021). https://arxiv.org/abs/0707.0940 . Discusses sharp Sobolev-loss issues for higher-genus translation flows, not the present circle-rotation result.
- Dalibor Volný, *BV coboundaries over irrational rotations*, Studia Mathematica 126 (1997), 253–271. https://doi.org/10.4064/sm-126-3-253-271 . Related existence and regularity phenomena.
- Dalibor Volný, *Constructions of smooth and analytic cocycles over irrational circle rotations*, Commentationes Mathematicae Universitatis Carolinae 36 (1995), 745–764. https://dml.cz/handle/10338.dmlcz/118802 . The accessible abstract concerns smooth/analytic constructions and nonintegrable transfers; a historical equivalent at the present Sobolev/modulus boundary is not excluded.
