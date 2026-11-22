# A unique phenotype-mutation optimum on the four-state recognition cycle

## Finding

**Theorem.** In the finite periodic phenotype-assortment model of Kroumi (2026), take one phenotype coordinate, exactly four cyclically arranged phenotype values, positive discrimination strength \(\alpha>0\), and scaled strategy mutation \(\mu=1\). For every \(\alpha>0\), the weak-selection, large-population benefit-to-cost threshold \(\beta(\nu,\alpha)\) for cooperation has **exactly one** critical point on the phenotype-mutation interval \(\nu>0\). The point is a strict, nondegenerate global minimum: the threshold decreases strictly up to the optimum and increases strictly thereafter. The optimum is the unique positive zero of the explicit degree-ten polynomial \(H_q\) below, where \(q=e^{-\alpha}\).

For \(q=1/2\), the optimum is \(\nu_*=1.168773523305237\ldots\), with minimum threshold \(\beta(\nu_*,\log 2)=13.984680815057002\ldots\).

## Assumptions and scope

The phenotype space is \(\mathbb Z/4\mathbb Z\), with distance \(d(i,j)=\min(|i-j|,4-|i-j|)\) and conditional helping probability \(e^{-\alpha d(i,j)}\). Phenotype mutation is nearest-neighbor and symmetric, independently of strategy mutation. The strategy-mutation rate has the fixed scaled value \(\mu=1\). The phenotype-mutation parameter \(\nu\) is any positive real number, and \(q=e^{-\alpha}\in(0,1)\). We use the source paper's weak-selection, large-population stationary-abundance criterion (equations (29) and (A7)); this is not a finite-census fixation statement.

Define, for \(s\in\{1,3,5\}\),
\[
F_s(\nu,q)=\frac{(1+q)^2}{s}+\frac{2(1-q^2)}{s+2\nu}+\frac{(1-q)^2}{s+4\nu}.
\]
The exact threshold is
\[
\beta(\nu,q)=\frac{9F_1-6F_3+5F_5}{-3F_1+6F_3+5F_5}.
\]
There is no claim of optimality when \(\mu\ne1\), for a larger phenotype cycle, higher-dimensional phenotype tori, or a different mutation process.

## Proof

**1. Spectral specialization.** The recognition kernel on the cycle has values \((1,q,q^2,q)\) and discrete Fourier weights
\[
((1+q)^2,\ 1-q^2,\ (1-q)^2,\ 1-q^2).
\]
The corresponding random-walk relaxation rates for modes \(0,1,2,3\) are \(0,2\nu,4\nu,2\nu\). Substituting these weights and rates in the Fourier representation (A7), followed by \(\mu=1\) in equation (29), gives the displayed ratio. The common transform normalization cancels between numerator and denominator.

**2. Positive denominator.** Put
\[
U(\nu,q)=48q\nu^4+184q\nu^3+216q\nu^2+77q\nu+80\nu^4+360\nu^3+544\nu^2+321\nu+60.
\]
Direct clearing of denominators yields
\[
-3F_1+6F_3+5F_5=
\frac{64\nu(1-q)U(\nu,q)}{\prod_{s\in\{1,3,5\}}(s+2\nu)(s+4\nu)}>0.
\]
Thus the derivative exists throughout the stated domain and the threshold cannot have poles there.

**3. The derivative's unique positive zero.** Set \(H_q(\nu)=\sum_{j=0}^{10}h_j(q)\nu^j\), with coefficients listed from degree ten down to degree zero:
\[
\begin{aligned}
h_{10}&=2048(q+1)^2(3q+5),\\
h_9&=2048(q+1)^2(23q+45),\\
h_8&=256(561q^3+2459q^2+3181q+1271),\\
h_7&=128(1739q^3+8677q^2+11087q+3873),\\
h_6&=32(5751q^3+33709q^2+33821q+535),\\
h_5&=32(2381q^3+16861q^2-6565q-35073),\\
h_4&=4(3015q^3+22891q^2-266653q-461921),\\
h_3&=-480(45q^2+1720q+3056),\\
h_2&=-30(240q^2+9213q+21245),\\
h_1&=-450(77q+321),\\
h_0&=-13500.
\end{aligned}
\]
Exact algebra gives
\[
\frac{\partial\beta}{\partial\nu}=
\frac{H_q(\nu)}{2\nu^2(1-q)U(\nu,q)^2}.
\]
For every \(q\in(0,1)\), degrees ten through six have positive coefficients. Degrees five and four are strictly negative: using \(q^2,q^3<1\), their respective positive contributions are bounded above by \(2381+16861<35073\) and \(3015+22891<461921\); all omitted terms are nonpositive. Degrees three through zero are strictly negative. Consequently, the coefficients of \(H_q\), read in descending degree, change sign exactly once. Descartes' rule of signs therefore permits at most one strictly positive root counting multiplicity. But \(H_q(0)=-13500<0\) and the leading coefficient is positive, so continuity gives at least one positive root. It is unique and simple. The derivative is strictly negative before it and positive after it, giving a nondegenerate strict global minimum.

**4. Example.** Substituting \(q=1/2\), the polynomial is strictly negative at \(\nu=1.168\) and strictly positive at \(\nu=1.170\), and a numerical solve on that isolated interval gives the values in the theorem.

## Verification

The self-contained file `CHECK.py` performs exact SymPy simplification of both the denominator and derivative identities against the stated polynomials. It also tests the exact rational signs at the example's bracketing endpoints and calculates the root numerically. Run `python CHECK.py` with SymPy installed. This finite check verifies algebra and the example; the for-all-parameter uniqueness conclusion is the preceding coefficient-sign/Descartes argument, not a numerical extrapolation.

## Relationship to prior work

Kroumi (2026) derives the finite-torus coalescent/Fourier threshold and proves that phenotype mutation creates **at least one** interior optimum. Both the threshold and the existence of an optimum are therefore prior work. The additional result here is the **unique**, nondegenerate global optimum with an exact degree-ten polynomial specification on the first one-dimensional torus featuring two distinct nonzero spectral relaxation rates. Prior results on the binary two-state phenotype model do not imply uniqueness for this four-state, two-rate case. The earlier unbounded-lattice graded-recognition work concerns different asymptotics and does not supply the finite-cycle classification.

## Limitations

The theorem fixes scaled strategy mutation to one and applies only to four periodic phenotype values, weak selection, and a large-population stationary-abundance approximation. It neither classifies higher-cycle lengths nor identifies an optimal biological intervention. The algebraic minimizer does not have a claimed elementary radical expression. The historical novelty assessment is literature-bounded; independent audit has not been performed.

## References

- D. Kroumi, *Phenotypic Assortment and the Evolution of Cooperation in Finite Periodic Phenotype Spaces*, arXiv:2608.21872v1 (first publicly available 2026-08-22), equations (29), (A7), Appendix D. https://arxiv.org/abs/2608.21872
- D. Kroumi, *The evolution of cooperation under imperfect phenotypic recognition*, arXiv:2607.27570 (2026), concerning unbounded phenotype lattices. https://arxiv.org/abs/2607.27570
