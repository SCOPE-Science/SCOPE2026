# A sharp finite-time zero dichotomy for inverse-age quantum-reset coherence

## Finding

Fix a reset strength \(0<\gamma<1\) and an integer horizon \(t\geq1\). A qubit initialized in \(\lvert+\rangle=(\lvert0\rangle+\lvert1\rangle)/\sqrt2\) is subjected at each discrete step either to a complete reset to \(\lvert+\rangle\) with probability \(r_n=\gamma/(n+1)\), where \(n\) is the number of consecutive phase gates since the previous reset, or to a phase gate \(U_\phi=\operatorname{diag}(1,e^{i\phi})\) with the complementary probability. A reset consumes a step and does not apply the gate.

Writing \(a=1-\gamma\), \(b=\gamma\), and \(z=e^{i\phi}\), the exact off-diagonal coherence is \(2\langle1\rvert\rho_t\lvert0\rangle=P_t(z)\), where

\[
P_t(z)=\sum_{k=0}^t\frac{(a)_k(b)_{t-k}}{k!(t-k)!}z^k=[w^t](1-w)^{-b}(1-zw)^{-a}.
\]

Here \((c)_n=c(c+1)\cdots(c+n-1)\), with \((c)_0=1\). The degree-\(t\) polynomial \(P_t\) has this exact zero-location trichotomy:

- If \(0<\gamma<1/2\), **all** its \(t\) complex zeros lie strictly inside the unit disk.
- If \(1/2<\gamma<1\), **all** its \(t\) complex zeros lie strictly outside the closed unit disk.
- If \(\gamma=1/2\), its \(t\) simple zeros lie exactly on the unit circle and have phases \(\phi_j=2\arccos(x_{t,j})\) modulo \(2\pi\), where \(x_{t,j}\in(-1,1)\) run through the \(t\) distinct roots of the ordinary Legendre polynomial of degree \(t\).

In particular, exact disappearance of the ensemble off-diagonal coherence at a finite positive time and a physical gate phase is possible if and only if \(\gamma=1/2\) and the phase is one of the listed Legendre phases. The balanced-case formula and its Legendre zeros were previously known; the contribution assessed here is the strict **all-degree, all-phase asymmetric zero exclusion and full inside/outside dichotomy**.

## Assumptions and scope

Time is integer-valued, the reset action restores precisely the same pure qubit state, and the age-dependent reset Bernoulli trials are conditionally independent given their current ages. The reset strength is strictly between zero and one. There is no additional decoherence or measurement conditioning, and the gate phase is fixed across steps. The theorem concerns finite-time *ensemble* coherences and polynomial zeros for each fixed integer \(t\ge1\). It makes no claim for a different hazard exponent, time-dependent gates, or local noise.

The relevant probability law is the beta-binomial distribution with shapes \(a=1-\gamma\) and \(b=\gamma\), whose sum is one. In particular the root-location theorem should not be read as an arbitrary-parameter beta-binomial zero theorem.

## Proof

**1. Exact renewal weights.** The probability of surviving \(k\) gate applications without a reset is

\[
S_k=\prod_{j=0}^{k-1}\left(1-\frac{b}{j+1}\right)=\frac{(a)_k}{k!}.
\]

Its generating function is \(S(w)=(1-w)^{-a}\). If \(f_m=S_{m-1}-S_m\) is the first reset-interval probability, then \(1-F(w)=(1-w)S(w)=(1-w)^b\). The renewal mass at time \(m\) (including the initial event at time zero) is the coefficient of \(1/(1-F(w))=(1-w)^{-b}\), namely \(u_m=(b)_m/m!\). Therefore the probability that the most recent reset is \(t-k\) and is followed by exactly \(k\) gate applications is \(u_{t-k}S_k\), giving the displayed polynomial. The generalized binomial theorem gives \(P_t(1)=1\), ensuring normalization.

**2. Exact polynomial recurrence.** Put \(P_0=1\) and \(P_1=b+az\). Differentiating the two-factor generating function with respect to \(w\) yields, for all integers \(n\ge1\),

\[
(n+1)P_{n+1}(z)=\big[(n+b)+(n+a)z\big]P_n(z)-nzP_{n-1}(z).
\]

For \(z=e^{2i\theta}\), \(0<\theta<\pi\), set \(x=\cos\theta\), \(y=\sin\theta>0\), and \(\delta=a-b=1-2\gamma\). Define \(Q_n=e^{-in\theta}P_n(e^{2i\theta})\). The recurrence becomes

\[
(n+1)Q_{n+1}=\big[(2n+1)x+i\delta y\big]Q_n-nQ_{n-1},\quad Q_0=1,\quad Q_1=x+i\delta y.
\]

Let \(R_n=n!Q_n/(2n-1)!!\), with \((-1)!!=1\). Thus

\[
R_{n+1}=\left(x+\frac{i\delta y}{2n+1}\right)R_n-\frac{n^2}{4n^2-1}R_{n-1}.
\]

**3. A definite-imaginary-part determinant excludes every unit-circle zero.** The standard continuant recurrence identifies \(R_t\) with the determinant of the \(t\)-by-\(t\) matrix

\[
M_t=xI_t-J_t+i\delta y D_t,
\]

where \(J_t\) is real symmetric tridiagonal, has zero diagonal, and has off-diagonal entries \((J_t)_{j,j+1}=j/\sqrt{4j^2-1}\) for \(1\le j<t\); and \(D_t=\operatorname{diag}(1,1/3,\ldots,1/(2t-1))\) is strictly positive definite. If \(\delta\ne0\), then for every nonzero complex vector \(v\),

\[
\operatorname{Im}(v^*M_tv)=\delta y\,v^*D_tv\ne0.
\]

Consequently \(M_t\) is nonsingular, so \(P_t(e^{2i\theta})\ne0\) for every \(0<\theta<\pi\). The omitted phase \(z=1\) is nonzero because \(P_t(1)=1\). This proves global unit-circle zero exclusion for every \(\gamma\ne1/2\), with no appeal to a finite enumeration.

**4. All zeros lie strictly on the specified side.** For each fixed \(t\), polynomial coefficients depend continuously on \(\gamma\). Its leading coefficient \((a)_t/t!\) never vanishes for \(0\le\gamma<1\), and the preceding step rules out all unit-circle crossings on \(0\le\gamma<1/2\). At \(\gamma=0\) the polynomial is \(z^t\), so all zeros are strictly inside for the entire interval \(0<\gamma<1/2\). The reciprocity identity

\[
P_t(z; a,b)=z^t P_t(z^{-1};b,a)
\]

then puts every zero strictly outside when \(1/2<\gamma<1\). (Both constant and leading coefficients are nonzero in the open parameter range, so the reciprocal correspondence is valid.)

**5. Sharp boundary.** At \(a=b=1/2\), \(\delta=0\) and the recurrence for \(Q_t\) reduces to the ordinary Legendre recurrence. Thus \(Q_t=L_t(x)\), the degree-\(t\) Legendre polynomial. Its \(t\) simple roots are all in \((-1,1)\). The map \(\theta\mapsto e^{2i\theta}\) is a bijection from \((0,\pi)\) to the unit circle without \(1\), giving exactly the claimed simple phase zeros. This Legendre specialization is acknowledged prior knowledge, not asserted as an original discovery.

## Verification

Run `python checker.py` with Python 3, NumPy, and SymPy. The standalone checker compares the independent age-state recursion with the closed beta-binomial weights, checks the generating-function recurrence and coefficient reversal using exact rational arithmetic, evaluates the tridiagonal determinant directly, and checks finite-degree polynomial zeros and the Legendre specialization. In its packaged run it passed 835 assertions. These checks are finite consistency diagnostics; the all-degree conclusion follows from positive definiteness, continuants, and root-location continuity in the proof.

## Relationship to prior work

Wald, Yao, Platini, Hooley, and Carollo, arXiv:2410.11497v1 (first public 2024-10-15), define general discrete-time quantum resetting. Their equations (1)–(5), Section IV, and Appendix C contain the age recursion and critical inverse-age hazard \(r_n=\gamma/(n+1)\), and discuss late-time relaxation. They do not classify roots of the finite-horizon coherence polynomial. Their subsequent journal publication was in May 2025 and is not used as its first-public date.

The published result *Exact Legendre entanglement nodes and Bessel scaling under a critical discrete reset clock* (published-finding corpus identifier `2026/10/26/SCOPE-exact-legendre-entanglement-nodes-and-bessel-scaling-under-a-cri--4532bc9cfbd9`) already derives the beta-binomial weights and the \(\gamma=1/2\) Legendre zero classification for Bell-state entanglement. It is explicitly credited and supplies no strict asymmetric zero-location theorem. The published *Half-index interference threshold for coherence under infinite-mean renewal resetting of a quantum gate* (`2026/11/8/SCOPE-half-index-interference-threshold-for-coherence-under-infinite-m--669edc24d60f`) gives sharp long-time asymptotics for a different exact power-law survival clock, not the finite-degree zero-location theorem. The published *Phase rigidity and complex-zero escape for asymmetric Beta Fourier transforms* (`2026/10/25/SCOPE-phase-rigidity-and-complex-zero-escape-for-asymmetric-beta-fouri--1985d778d78f`) gives real-frequency nonvanishing of a continuous Beta Fourier transform, not zeros of the finite beta-binomial probability-generating polynomials. The latter's continuous transform is a scaling limit, which does not in itself exclude finite-degree polynomial zeros on the unit circle.

## Limitations

The zero dichotomy requires the precise inverse-age hazard, a single fixed phase gate, full reset to the same coherent preparation, finite integer horizons, and \(0<\gamma<1\). It does not provide quantitative lower bounds on nonzero coherence or uniform root-to-circle distances as degree grows. The proof is analytic but its originality assessment is literature-limited: a previously unindexed theorem about finite beta-binomial generating-polynomial zeros could subsume the mathematical claim. No independent scientific audit has been performed.

## References

1. S. Wald, L. H. Yao, T. Platini, C. Hooley, and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497v1, first publicly posted 2024-10-15, https://arxiv.org/abs/2410.11497 . Full open version: https://ar5iv.labs.arxiv.org/html/2410.11497 .
2. *Exact Legendre entanglement nodes and Bessel scaling under a critical discrete reset clock*, publicly available at https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-legendre-entanglement-nodes-and-bessel-scaling-under-a-cri--4532bc9cfbd9 .
3. *Half-index interference threshold for coherence under infinite-mean renewal resetting of a quantum gate*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-half-index-interference-threshold-for-coherence-under-infinite-m--669edc24d60f .
4. *Phase rigidity and complex-zero escape for asymmetric Beta Fourier transforms*, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-phase-rigidity-and-complex-zero-escape-for-asymmetric-beta-fouri--1985d778d78f .
5. NIST Digital Library of Mathematical Functions, Chapter 18 (Legendre polynomials and zeros), https://dlmf.nist.gov/18 .
