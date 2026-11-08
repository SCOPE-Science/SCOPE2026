# A two-visit occupancy experiment breaks equal-effort optimality

## Finding

In a closed two-visit ecological occupancy experiment with a common, unknown detection rate, the locally D-optimal *division of a fixed observation-time budget* is independent of the unknown occupancy prevalence. Nevertheless its shape changes with the dimensionless total detection budget: equal visit lengths are uniquely optimal for all sufficiently small budgets, whereas unequal lengths are strictly better for some finite budgets and eventually an optimal design uses one bounded-length probe and one increasingly long probe. The bounded probe approaches a universal duration.

Precisely, let \(0<\psi<1\) and \(\lambda>0\). Define \(\theta=\lambda T\), \(x=\lambda t_1\), and
\[
f(u)=\frac{u^2}{e^u-1}\quad(u>0),\qquad f(0)=0.
\]
For \(0<t_1<T\), the determinant of the per-site Fisher information matrix for \((\psi,\lambda)\) is exactly
\[
\boxed{\det I(t_1,T-t_1)=\frac{(1-e^{-\theta})[f(x)+f(\theta-x)]-\theta^2e^{-\theta}}{\lambda^2(1-\psi+\psi e^{-\theta})}.}\tag{1}
\]
Thus the maximizing split depends on \(T,\lambda\) only through \(\theta\), not on \(\psi\). For all sufficiently small \(\theta>0\), the unique maximizer is \(x=\theta/2\).

The departure from equal splitting occurs at finite budget: at \(\theta=10\log2\), the split \(x=3\log2\) and \(\theta-x=7\log2\) strictly beats equal splitting. After removing the common positive multiplier \((\log2)^2/[\lambda^2(1-\psi+\psi2^{-10})]\), the two exact determinant numerators are respectively
\[
\frac{715639}{455168}\quad\text{and}\quad\frac{775}{512},
\qquad\text{difference }\frac{3333}{56896}>0.
\]
The unequal split has approximately \(3.87\%\) more Fisher determinant, for **every** \(0<\psi<1\).

Let \(a_*\in(1,2)\) be the unique positive root of \(2(1-e^{-a_*})=a_*\), numerically \(a_*=1.59362426004004\ldots\). For any global maximizer, write its shorter normalized length as \(s_\theta=\min\{x,\theta-x\}\). Then
\[
\boxed{s_\theta\longrightarrow a_*\quad\text{as }\theta\to\infty.}\tag{2}
\]
Furthermore, for fixed interior \(\psi\) and fixed \(\lambda>0\),
\[
\max\det I\longrightarrow\frac{a_*(2-a_*)}{\lambda^2(1-\psi)},\qquad
\frac{\max\det I}{\det I(T/2,T/2)}\sim\frac{2a_*(2-a_*)}{\theta^2}e^{\theta/2}.\tag{3}
\]
These claims do **not** assert uniqueness of the transition budget or of finite-budget asymmetric maximizers.

## Assumptions and scope

At each independently replicated site, occupancy \(Z\) is Bernoulli with probability \(\psi\). A site's state remains unchanged over both visits. Conditional on \(Z=1\), detections during a visit of length \(t_i\) follow an independent Poisson process of the same rate \(\lambda\); only a binary indicator of at least one detection is retained for each visit, not the event times or counts. Conditional on \(Z=0\), neither visit can report a detection. There are exactly two predetermined positive visit lengths, no per-visit setup charge, and \(t_1+t_2=T>0\). Each site has the same design, and the local D criterion is the determinant of the exact expected Fisher information for the parameter vector \((\psi,\lambda)\) from one site. The number of independent sites merely multiplies the information matrix and does not affect the optimum. Model parameters are interior: \(\psi\in(0,1)\), \(\lambda>0\).

## Proof

Put \(A=e^{-\lambda t_1}\), \(B=e^{-\lambda t_2}\), \(k=AB=e^{-\lambda T}\), and \(q=1-\psi+\psi k\). The four binary histories \((00,10,01,11)\) have respective probabilities
\[
q,\qquad \psi(1-A)B,\qquad\psi A(1-B),\qquad\psi(1-A)(1-B).
\]
Direct differentiation of these probabilities and summation of the score outer products yield
\[
I_{\psi\psi}=\frac{1-k}{\psi q},\qquad
I_{\psi\lambda}=\frac{Tk}{q},\qquad
I_{\lambda\lambda}=\psi S-\frac{\psi(1-\psi)kT^2}{q},
\]
where \(S=t_1^2/(e^{\lambda t_1}-1)+t_2^2/(e^{\lambda t_2}-1)\). The formula for \(I_{\lambda\lambda}\) may alternatively be checked by starting with the information when the latent occupancy indicator is observed and subtracting the missing score variance conditional on history \(00\). The determinant simplifies *exactly* to
\[
\det I=\frac{(1-k)S-kT^2}{q},
\]
which becomes (1). Both the variable-independent multiplier and the variable-independent subtracted term are positive or constant as appropriate, so maximizing (1) is equivalent to maximizing \(f(x)+f(\theta-x)\) on \([0,\theta]\). Since the two positive-duration binary histories identify \(\lambda\) through their positive-history ratio, and subsequently identify \(\psi\) from the chance of any detection, the information is positive definite for positive durations. It degenerates at either endpoint; hence each finite-budget maximum is attained in the interior.

To prove the small-budget assertion, set \(x=\theta z\), \(0\le z\le1\). The removable-singularity expansion \(f(u)=u-u^2/2+u^3/12+O(u^5)\), substituted into (1), gives
\[
(1-e^{-\theta})[f(\theta z)+f(\theta(1-z))]-\theta^2e^{-\theta}
=\theta^3z(1-z)+O(\theta^4).
\]
Because \(f\) extends analytically through zero, the expansion is uniform with its first two \(z\)-derivatives on \([0,1]\). In particular its second derivative is \(-2\theta^3+O(\theta^4)<0\) for all sufficiently small positive \(\theta\). Strict concavity and symmetry about \(z=1/2\) prove the unique equal split.

For the finite exact witness, put \(\theta=10\log2\). At \(x=3\log2\), all exponential survival probabilities are powers of \(1/2\). Direct substitution into the numerator of (1) gives \((\log2)^2(715639/455168)\); at \(x=5\log2\) it gives \((\log2)^2(775/512)\). The difference is exactly \((\log2)^2(3333/56896)>0\). Thus equal splitting is not always globally D-optimal.

Finally, \(f\) is positive on \((0,\infty)\), tends to zero at both ends, and its derivative has the sign of \(2(1-e^{-u})-u\). This quantity starts positive, becomes negative after its unique positive zero \(a_*\), and its derivative \(2e^{-u}-1\) is strictly decreasing through zero. Therefore \(f\) has the unique positive maximizer \(a_*\), with \(f(a_*)=a_*(2-a_*)\).

For \(\theta\to\infty\), choosing the competitor \((a_*,\theta-a_*)\) gives \(f(a_*)+f(\theta-a_*)\to f(a_*)>0\). If the shorter gap of any maximizing sequence diverged, both gaps would diverge, forcing the maximized sum to zero, a contradiction. Hence its shorter gaps are bounded; every subsequential limit \(s\) must maximize \(f(s)\), since the other gap diverges and its \(f\)-value vanishes. Uniqueness of the maximizer forces \(s=a_*\), proving (2). Equation (1), \(q\to1-\psi\), and the exact equal-split identity
\[
(1-e^{-\theta})\,2f(\theta/2)-\theta^2e^{-\theta}
=\frac{\theta^2}{2}(e^{-\theta/2}-e^{-\theta})
\]
give (3).

## Verification

Run `python verify.py` with Python 3.10 or later and SymPy 1.10 or later. The checker performs four independent symbolic Fisher-entry/determinant identities, 1,200 rational-history and positivity checks, four exact logarithmic-budget checks, two root checks, and four large-budget numerical diagnostics (1,214 checks in total). It uses an independent direct score-probability calculation for the rational checks, rather than only evaluating the closed formula. The theorem's continuum assertions and asymptotics are established by the proof, not by finite tests.

## Relationship to prior work

MacKenzie and Royle (2005) establish the standard occupancy detection framework and allocate effort across sites and numbers of visits under an occupancy-estimator precision criterion. Guillera-Arroita, Ridout, and Morgan (2010) explicitly consider joint precision and D-optimality for constant per-visit detectability and optimize the *number* of identical visits; the present result instead fixes the number of visits at two, makes their lengths variable under a fixed total, and optimizes the determinant for unknown Poisson detection intensity. The resulting prevalence-independence and finite-to-long-budget asymmetric geometry do not follow merely from their constant-probability replicate-count tables. Moore and colleagues (2014, 2016) study visit counts and spatial allocations when detectability varies between surveys, primarily optimizing detection probability rather than joint parameter information. Bornand and colleagues (2014) compare occurrence-estimation protocols using time-to-detection information, whereas here exact event times are discarded. These differences are differences of statistical experiment and objective, not claims that classical occupancy likelihood or D-optimality was previously unknown.

A search of closely related occupancy and optimal-design work did not establish an earlier equivalent of the complete fixed-two-visit theorem; that is limited novelty evidence, not a proof of historical priority.

## Limitations

This is an exact local-design theorem under closed occupancy, homogeneous Poisson detectability, no false positives, independent sites, fixed number of visits, zero overhead and binary recording. It does not optimize the number of visits, the number of sites, adaptive stopping, robustness to rate heterogeneity, finite-sample estimator MSE, or full event-time records. D-optimality is a local large-sample information criterion. The model is a mathematical benchmark, not a field-calibrated recommendation. The result does not prove a unique symmetry-breaking threshold for all finite budgets, nor independent historical priority or independent validation.

## References

1. MacKenzie, D. I., and Royle, J. A. (2005). *Designing occupancy studies: general advice and allocating survey effort*. Journal of Applied Ecology 42, 1105–1114. https://doi.org/10.1111/j.1365-2664.2005.01098.x (first online 2005-11-23).
2. Guillera-Arroita, G., Ridout, M. S., and Morgan, B. J. T. (2010). *Design of occupancy studies with imperfect detection*. Methods in Ecology and Evolution 1, 131–139. https://doi.org/10.1111/j.2041-210X.2010.00017.x (first online 2010-05-04).
3. Bornand, C. N., Kéry, M., Bueche, L., and Fischer, M. (2014). *Hide-and-seek in vegetation: time-to-detection is an efficient design for estimating detectability and occurrence*. Methods in Ecology and Evolution 5, 433–442. https://doi.org/10.1111/2041-210X.12171 (first online 2014-02-24).
4. Moore, A. L., McCarthy, M. A., Parris, K. M., and Moore, J. L. (2014). *The optimal number of surveys when detectability varies*. PLoS ONE 9, e115345. https://doi.org/10.1371/journal.pone.0115345 (online 2014-12-19).
5. Moore, A. L., McCarthy, M. A., and colleagues (2016). *Optimizing ecological survey effort over space and time*. Methods in Ecology and Evolution. https://doi.org/10.1111/2041-210X.12564.
6. Reich, H. T. (2020). *Optimal sampling design and the accuracy of occupancy models*. Biometrics 76, 1017–1027. https://doi.org/10.1111/biom.13203. (Different primary objective; only public abstract and accessible article sections compared.)
