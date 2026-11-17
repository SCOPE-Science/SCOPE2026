# Unbiased switching of transitive Volterra populations: exact fixation weights and extinction exponents

## Finding
Let \(m\ge2\), and let \(A=(a_{ij})_{1\le i,j\le m}\) be real and skew-symmetric, with \(0<a_{ij}<1\) whenever \(i<j\). On the probability simplex \(\Delta_{m-1}\), independently choose a fresh fair sign \(\sigma_{n+1}\in\{-1,+1\}\) each generation and apply
\[
 X_{n+1,i}=X_{n,i}\bigl(1+\sigma_{n+1}(AX_n)_i\bigr),\quad i=1,\ldots,m.
\]
For every deterministic starting vector \(x\in\Delta_{m-1}\), the process converges almost surely to a random vertex \(e_I\) with the **exact fixation law**
\[
 \mathbb P_x(I=i)=x_i\quad (1\le i\le m).
\]
If every initial coordinate is strictly positive, then, simultaneously for each \(j\ne I\),
\[
 \lim_{n\to\infty}\frac1n\log X_{n,j}
 =\frac12\log(1-a_{jI}^{\,2})<0\quad\text{almost surely}.
\]
Thus all competing types decay exponentially along a realized fixation path, and the rate of type \(j\), conditional on survival of type \(i\), depends only on their pairwise interaction intensity \(|a_{ij}|\), not on the other species.

## Assumptions and scope
The matrix \(A\) is fixed (not randomly resampled), antisymmetric, and has strictly positive entries strictly below one above its diagonal. This means its interaction tournament is transitive. The signs are independent identically distributed fair Rademacher variables and independent of the fixed initial composition. The probability statement applies to the closed simplex. The exponential-rate assertion assumes interior initial data; a coordinate initially zero stays zero. These are discrete-time Volterra quadratic stochastic maps, since the skew condition preserves total mass and the strict coefficient bound preserves coordinate positivity.

## Proof
Let \(\rho=\max_{i\ne j}|a_{ij}|<1\). Since \(|(Ax)_i|\le\rho\) on the simplex, the factors in the update belong to \([1-\rho,1+\rho]\). Hence the simplex is forward invariant, no positive coordinate ever becomes zero at finite time, and skew-symmetry gives
\[
 \sum_i X_{n+1,i}=\sum_i X_{n,i}+\sigma_{n+1}X_n^{\mathsf T}AX_n=1.
\]
The independent, unbiased sign gives \(\mathbb E[X_{n+1,i}\mid\mathcal F_n]=X_{n,i}\), so each coordinate is a bounded martingale and converges almost surely and in \(L^2\) to \(Y_i\). Taking conditional second moments yields the exact energy identity
\[
 \mathbb E[X_{n+1,i}^2\mid\mathcal F_n]
 =X_{n,i}^2+X_{n,i}^2(AX_n)_i^2.
\]
Summation and \(0\le X_{n,i}\le1\) imply
\[
 \sum_{n\ge0}\mathbb E[X_{n,i}^2(AX_n)_i^2]\le1.
\]
Consequently \(X_{n,i}^2(AX_n)_i^2\to0\) almost surely, and continuity of the polynomial gives \(Y_i(AY)_i=0\) for every \(i\). Suppose that the support \(S=\{i:Y_i>0\}\) contains two or more elements, and take its smallest index \(k\). Because \(a_{kj}>0\) for all \(j\in S\setminus\{k\}\),
\[
 (AY)_k=\sum_{j\in S,\,j>k}a_{kj}Y_j>0,
\]
contradicting \(Y_k(AY)_k=0\). Thus \(Y=e_I\) almost surely. Bounded martingale convergence implies \(\mathbb P(I=i)=\mathbb E Y_i=\mathbb E X_{0,i}=x_i\).

For the rate, assume \(x_i>0\) for every \(i\). All subsequent coordinates remain positive, and
\[
 \log X_{n,j}=\log x_j+\sum_{k=0}^{n-1}\log\bigl(1+\sigma_{k+1}(AX_k)_j\bigr).
\]
On the event \(Y=e_i\), \((AX_k)_j\to a_{ji}\). The logarithm is uniformly continuous for both sign choices because its argument remains in \([1-\rho,1+\rho]\); therefore the Cesàro mean of the difference between the displayed logarithmic increment and \(\log(1+\sigma_{k+1}a_{ji})\) tends to zero. The strong law for the original iid signs, on one common probability-one event, gives the time average \(\tfrac12\log(1+a_{ji})+\tfrac12\log(1-a_{ji})\). This equals \(\tfrac12\log(1-a_{ji}^{\,2})\). There are finitely many ordered pairs, so the assertions hold simultaneously. This completes the proof.

## Verification
The proof is analytic in every finite dimension. The reproducibility program `check_random_volterra.py` uses exact rational arithmetic to check mass preservation, the one-step martingale and quadratic-variation identities, and all sign words of length at most eight in dimensions two, three, and four. Successful execution reports `RANDOM_VOLTERRA_TRANSITIVE_EXACT_OK`. These finite checks supplement but do not establish the infinitely many-step convergence or strong-law statements.

## Relationship to prior work
Adilova, Jamilov and Reinfelds (2023) study the autonomous two-type SIS quadratic stochastic map, including signed interaction parameters, and characterize deterministic asymptotic dynamics. The present theorem instead draws a fresh unbiased sign at every step and treats all finite dimensions with transitive skew interactions; no deterministic fixed-sign convergence statement implies its exact random vertex-selection law. Jamilov, Scheutzow and Wilke-Berenguer (2014) prove almost-sure vertex convergence for certain randomly iterated Volterra operators, but their Theorem 3.1 requires a member of the random support squaring each respective coordinate. That hypothesis fails for this two-operator support when all interaction magnitudes are strictly below one. The present theorem further identifies every vertex probability and its pathwise conditional extinction exponents. Both earlier results are acknowledged rather than counted as new.

## Limitations
Transitive positive interaction signs, fair independent switching, and a strict magnitude bound are essential to this stated theorem. A cyclic interaction may have nonvertex equilibria, so the vertex argument does not extend unchanged. We give no quantitative error bound for finite-horizon fixation or fluctuations of the logarithmic extinction rates. This is a same-model proof and literature review, not independent external validation; possible equivalent results outside the inspected sources remain a priority risk.

## References
- F. Adilova, U. Jamilov and A. Reinfelds, *On Discrete-Time Models of Network Worm Propagation Generated by Quadratic Operators*, Mathematical Modelling and Analysis 28 (2023), 194–217, DOI: 10.3846/mma.2023.15999 (first public issue date 2023-03-21).
- U. U. Jamilov, M. Scheutzow and M. Wilke-Berenguer, *On the Random Dynamics of Volterra Quadratic Operators*, arXiv:1401.7840 (first public 2014-01-30), Theorem 3.1.
