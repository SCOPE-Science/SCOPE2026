# First phase-asymmetric cumulant of a cat-driven circle lift

## Finding

In the Chigarev–Kazakov–Pikovsky Anosov-driven circle map [1], suppress the Möbius restoring term by setting its parameter \(\varepsilon=0\). Let the Anosov initial coordinates \((t_0,s_0)\) have Haar (uniform) probability on \(\mathbb T^2\), let \(\alpha,c,\mu\in\mathbb R\) be fixed, and let \(\widetilde x_j\) be a real lift of the circle coordinate. For every integer \(n\ge1\), the centered physical-time displacement
\[
Y_n=\widetilde x_n-\widetilde x_0-nc=\mu\sum_{j=0}^{n-1}\sin(2\pi t_j+\alpha)
\]
has the **exact finite-time moments**
\[
\begin{aligned}
\mathbb E Y_n&=0,\\
\mathbb E Y_n^2&=\frac{n\mu^2}{2},\\
\mathbb E Y_n^3&=0,\\
\mathbb E Y_n^4&=\frac{3n(2n-1)\mu^4}{8},\\
\mathbb E Y_n^5&=\frac54(n-2)_+\mu^5\sin\alpha .
\end{aligned}
\]
Here \((u)_+=\max\{u,0\}\). Consequently, for cumulants \(\kappa_j\) of \(Y_n\),
\[
\kappa_1=0,\quad\kappa_2=\frac{n\mu^2}{2},\quad\kappa_3=0,\quad
\kappa_4=-\frac{3n\mu^4}{8},\quad
\boxed{\kappa_5=\frac54(n-2)_+\mu^5\sin\alpha}.
\]
Thus the first four moments coincide with those of \(n\) independent scaled arcsine increments, whereas the fifth moment detects a genuine arithmetic dependence when \(n\ge3\), \(\mu\ne0\), and \(\sin\alpha\ne0\). No independence of the increments is claimed.

## Assumptions and scope

The base map, following equation (1) of [1], is
\[
\begin{pmatrix}t_{j+1}\\s_{j+1}\end{pmatrix}
=\begin{pmatrix}2&1\\1&1\end{pmatrix}
\begin{pmatrix}t_j\\s_j\end{pmatrix}\pmod1,
\qquad
\widetilde x_{j+1}=\widetilde x_j+c+\mu\sin(2\pi t_j+\alpha).
\]
The phase is **unwrapped** before taking moments, rather than reduced modulo one. \(\widetilde x_0\) is arbitrary (possibly deterministic), and the only randomness is Haar selection of the base point. The result concerns \(\varepsilon=0\) only, not the forced regime \(\varepsilon\ne0\) where the displacement depends nonlinearly on \(\widetilde x_j\). There are no asymptotic or small-coupling assumptions on \(\alpha,c,\mu\).

## Proof

Write \(A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\), \(v_j=A^{\mathsf Tj}(1,0)^{\mathsf T}\in\mathbb Z^2\), and \(\theta_j=2\pi\langle v_j,(t_0,s_0)\rangle+\alpha\). The integer character sequence has \(v_0=(1,0)\), \(v_1=(2,1)\), and
\[
v_{j+2}+v_j=3v_{j+1}\qquad(j\ge0).
\]
If \(\lambda=(3+\sqrt5)/2\), then \(\lambda^{-1}=(3-\sqrt5)/2\), and a signed integer frequency relation \(\sum_{i=1}^k\sigma_i v_{j_i}=0\), \(\sigma_i\in\{\pm1\}\), is equivalent to simultaneous relations
\[
\sum_{i=1}^k\sigma_i\lambda^{j_i}=0,
\qquad \sum_{i=1}^k\sigma_i\lambda^{-j_i}=0.
\]
Indeed, the polynomial \(\sum\sigma_i z^{j_i}\) vanishes at both roots of the irreducible polynomial \(z^2-3z+1\) exactly when it is divisible by that polynomial. This is equivalent to the vector equation because the two coordinate sequences are linearly independent solutions of the recurrence (their initial coordinate determinant is one).

**Low-length resonance classification.** For a relation of length at most five, first discard any identical positive-negative index pairs. No remaining relation with at most four terms is possible. For a one-against-\(r\) split, multiplying the equalities at \(\lambda\) and \(\lambda^{-1}\) would equate \(1\) with \((\sum_{i=1}^r\lambda^{b_i})(\sum_{i=1}^r\lambda^{-b_i})\ge r^2\), impossible for \(r\ge2\). All equal signs are impossible. For two terms against two terms, multiplication gives the equality of \(2+\lambda^{|a-b|}+\lambda^{-|a-b|}\) on both sides. Strict monotonicity in the nonnegative gap forces equal gaps; equality of the original sums then forces identical unordered pairs, which were already discarded.

For a nontrivial five-term relation, the only possible sign split is two versus three. After reversing all signs if necessary, let the two positive exponents be \(a\le c\), and the negative exponents be \(b_1,b_2,b_3\). Since the signed polynomial is divisible by \(z^2-3z+1\), evaluating at \(-1\) shows \(\sum\sigma_i(-1)^{j_i}\) is divisible by five. It is a sum of five signs, hence equals \(\pm5\); all five summands therefore have the same sign. It follows that \(a,c\) have the same parity and all \(b_i\) have the opposite parity. Equal positive exponents are impossible by the same Cauchy-product inequality \(4<9\), so \(d=c-a\ge2\) is even.

Since \(\lambda>2\), the equality of positive powers forces \(\max b_i=c-1\): any larger opposite-parity exponent is at least \(c+1\), giving \(\lambda^{c+1}>\lambda^c+\lambda^a\), whereas if all three are at most \(c-3\), their sum is at most \(3\lambda^{c-3}<\lambda^c\). Applying the same argument to inverse powers forces \(\min b_i=a+1\). If \(d=2\), all negative exponents equal \(a+1\), yielding exactly
\[
\boxed{v_a+v_{a+2}=3v_{a+1}}.
\]
If \(d\ge4\), the third negative exponent \(b\) would satisfy
\[
(\lambda-1)(\lambda^{d-1}-1)=\lambda^{b-a}.
\]
Taking norms in \(\mathbb Q(\sqrt5)\) gives a contradiction: \(N(\lambda)=1\), \(N(\lambda-1)=-1\), but
\[
\left|N(\lambda^{d-1}-1)\right|=\lambda^{d-1}+\lambda^{-(d-1)}-2>1
\]
for \(d\ge4\). Hence, up to simultaneous reversal, all irreducible signed resonances of length five are the consecutive \((+1,-3,+1)\) patterns above.

**Moment evaluation.** Haar orthogonality kills every nonzero torus Fourier character. Expand each sine in exponentials and apply the classification. For moments of orders one and three no zero characters occur, for order two only identical-pair cancellations survive, and for order four only pairings survive. Using \(\mathbb E\sin^2\theta=1/2\) and \(\mathbb E\sin^4\theta=3/8\), this yields
\[
\mathbb E S_n^2=\frac n2,\qquad
\mathbb E S_n^4=\frac{3n}{8}+6\binom n2\frac14
=\frac{3n(2n-1)}8,
\]
where \(S_n=\sum_{j<n}\sin\theta_j\). At order five, each of the \(n-2\) consecutive triples has the only possible nonzero monomial, with one factor at each endpoint and three factors at its middle:
\[
\mathbb E[\sin\theta_a\sin^3\theta_{a+1}\sin\theta_{a+2}]
=\frac{\sin\alpha}{16}.
\]
There are \(5!/(1!3!1!)=20\) orderings per triple, giving \(\mathbb E S_n^5=(5/4)(n-2)_+\sin\alpha\). Centering and the standard moment-cumulant identities yield the stated cumulants; \(Y_n=\mu S_n\) supplies the powers of \(\mu\).

## Verification

The included standalone `check_fifth.py` reconstructs the vector character sequence, enumerates all \(\pm1\) Fourier expansions for \(1\le n\le8\) and moments \(1\le k\le5\) using exact integer arithmetic, and matches all 40 predicted zero-character polynomials. It separately computes 75 torus-grid quadratures for \(n\le5\), three phase offsets and the same five moments using a \(401\times401\) grid; all frequencies on those tests are strictly below the grid aliasing threshold, so the quadrature is exact for the trigonometric polynomial, apart from floating-point rounding. All 115 checks passed. Enumeration is corroboration, not the proof for arbitrary \(n\).

Run `python3 check_fifth.py` from the directory containing this file. Python standard library is sufficient for the exact checks; NumPy enables the optional independent-grid checks.

## Relationship to prior work

Chigarev, Kazakov and Pikovsky [1] introduce the Anosov-driven Möbius circle map, the phase-diffusion interpretation of its sinusoidal coupling, and the real lift; they study attractor/repeller collision, rotation number and Lyapunov exponents. Their model includes the \(\varepsilon=0\) slice considered here; their inspected results do not give its exact finite-time phase-increment cumulants. Aistleitner, Kabluchko and Prochno [2] establish broad cumulant results for scalar lacunary cosine sums, including eventual linearity for some algebraic recurrence frequencies. Their one-dimensional random-phase and scalar-frequency hypotheses do not contain the Haar two-dimensional cat-character family with a continuously shifted sine observable as a stated case. Their general character-counting method is an important conceptual precursor, but does not specify the exact phase-asymmetric coefficient in this dynamical observable.

The distinction is substantive: the observable here is the original-time **lift displacement** of an explicitly published skew system, and the nontrivial dependence is invisible at cumulant orders below five. No claim is made that Fourier orthogonality, cumulants or recurrence polynomial divisibility are new methods.

## Limitations

The phase-lift cumulants are not invariant under changing the additive observable by an arbitrary coboundary; the specified phase coordinate is part of the claim. The result does not treat \(\varepsilon\ne0\), nonlinear feedback, general initial base distributions, limit laws, or a whole characteristic function. The systematic literature comparison does not establish publication priority in every possible alternative formulation. No independent mathematical audit has been performed.

## References

[1] V. Chigarev, A. Kazakov and A. Pikovsky, *Attractor-repeller collision and the heterodimensional dynamics*, arXiv:2305.18172 (initial submission 29 May 2023), https://arxiv.org/abs/2305.18172 ; see especially equation (1) and Sections II–IV.

[2] C. Aistleitner, Z. Kabluchko and J. Prochno, *Arithmetic sensitivity of cumulant growth in lacunary sums: transcendental versus algebraic ratio limits*, arXiv:2512.15501 (17 December 2025), https://arxiv.org/abs/2512.15501 ; see Sections 1 and 5–6.
