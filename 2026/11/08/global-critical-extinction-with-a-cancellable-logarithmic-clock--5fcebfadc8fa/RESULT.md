# Global critical extinction with a cancellable logarithmic clock in an exponential predator-prey map

## Finding
For the exponential/rational two-population map of Li and Zhang at the critical intrinsic prey growth multiplier \(b=1\), the entire positive quadrant approaches extinction at an explicit algebraic rate, with a sharp second-order logarithmic correction and a nonempty hypersurface on which that correction disappears.

For positive parameters \(a,p,q,\alpha\), let
\[
 c=q+\alpha a,\qquad d=aq+a^2(\alpha-1-p),\qquad k=\alpha a\left[2q+a\left(\frac{3\alpha}{2}-1-p\right)\right].
\]
For every strictly positive initial state, a finite real constant \(C=C(y_0,z_0;a,p,q,\alpha)\) exists with
\[
 \frac1{z_n}=cn+\frac{k}{c}\log n+C+o(1),\qquad y_n=az_n+d z_n^2+O(z_n^3).
\]
Consequently \(n z_n\to1/c\) and \(n y_n\to a/c\). The logarithmic coefficient is zero exactly when \(p=p_*=3\alpha/2-1+2q/a\). If \(p_*>0\), crossing \(p=p_*\) changes the sign of the logarithmic clock drift without changing the leading algebraic extinction exponent or amplitude.

## Assumptions and scope
The recurrence is
\[
 y_{n+1}=\frac{a z_n e^{-y_n}}{1+p y_n},\qquad
 z_{n+1}=\frac{z_n e^{-\alpha y_n}}{1+q z_n},
\]
with \(n\in\{0,1,\ldots\}\), \(a,p,q,\alpha>0\), \(b=1\), and arbitrary \(y_0,z_0>0\). The variables are real, and all asymptotic statements concern \(n\to\infty\) with parameters and initial state fixed. The asymptotic constants in \(O(\cdot)\) depend on that fixed data. The coordinate axes are excluded from the universal two-population amplitude statement (on \(z_0=0\), extinction occurs after one iterate).

## Proof
**1. Positivity and global extinction.** Both recurrence formulas are positive on the strictly positive quadrant. Moreover
\[
 \frac1{z_{n+1}}=\frac{(1+qz_n)e^{\alpha y_n}}{z_n}\ge\frac1{z_n}+q.
\]
Thus \(0<z_n\le (q n+z_0^{-1})^{-1}\to0\). Since \(0<y_{n+1}\le a z_n\), also \(y_n\to0\). In particular all orbits are globally defined, bounded, and converge to the origin.

**2. Slaving of predator to prey.** Divide the recurrences at successive indices. For every \(n\ge1\), the exact identity is
\[
 \frac{y_n}{z_n}=a\,\frac{1+qz_{n-1}}{1+p y_{n-1}}\,e^{(\alpha-1)y_{n-1}}.
\]
Because both coordinates converge to zero, \(y_n/z_n\to a\). The bound \(y_{n-1}=O(z_{n-1})\), together with the displayed identity, implies \(y_{n-1}=a z_{n-1}+O(z_{n-1}^2)\). A second Taylor expansion, with remainders uniform in a sufficiently small positive neighborhood, gives
\[
 \frac{y_n}{z_n}=a+a\left[q+a(\alpha-1-p)\right]z_{n-1}+O(z_{n-1}^2).
\]
Also \(z_n=z_{n-1}(1+O(z_{n-1}))\), hence \(z_{n-1}=z_n+O(z_n^2)\). Therefore
\[
 y_n=a z_n+d z_n^2+O(z_n^3),\qquad d=a q+a^2(\alpha-1-p).
\]
This is a direct orbitwise estimate, not an unproved assumption of an invariant center manifold.

**3. Reciprocal increment.** Write \(u_n=z_n^{-1}\). The exact recurrence yields
\[
 u_{n+1}-u_n=\frac{(1+qz_n)e^{\alpha y_n}-1}{z_n}.
\]
Use the expansion just proved and the third-order Taylor bound for the exponential:
\[
 u_{n+1}-u_n=c+k z_n+O(z_n^2),
\]
where
\[
 c=q+\alpha a,\qquad k=\alpha d+\alpha q a+\frac{\alpha^2a^2}{2}
      =\alpha a\left[2q+a\left(\frac{3\alpha}{2}-1-p\right)\right].
\]
The remainder is summable because \(z_n=O(n^{-1})\). Summation first gives \(u_n=cn+O(\log n)\), hence
\[
 z_n=\frac1{cn}+O\!\left(\frac{\log n}{n^2}\right).
\]
The latter difference is absolutely summable. Consequently \(\sum_{j=1}^{n-1} z_j-(1/c)\log n\) converges to a finite real constant, as do the accumulated \(O(z_j^2)\) remainders. Summing the reciprocal-increment identity again shows that
\[
 u_n-cn-\frac{k}{c}\log n\longrightarrow C\in\mathbb R.
\]
This proves the claimed full two-term law including the finite part, and yields both leading extinction limits.

**4. Sharp logarithmic-correction boundary.** Since \(\alpha a^2>0\), the coefficient factors as \(k=\alpha a^2(p_*-p)\), with \(p_*=3\alpha/2-1+2q/a\). Thus it changes sign exactly on the stated admissible positive-parameter hypersurface. At \(k=0\) the previous limit reduces to \(u_n-cn\to C\). For example \((a,q,\alpha,p)=(2,1,1,3/2)\) lies on it, so the cancellation is genuinely attainable within the positive parameter domain.

## Verification
The standalone file `verify.py` checks the Taylor-coefficient identities using exact rational arithmetic for independent parameter tuples and compares direct orbit computations against the predicted leading amplitudes, quadratic slaving coefficient, and reciprocal-clock finite-part behavior. Run `python verify.py` using Python 3's standard library. The computer checks are finite and do not establish the infinite asymptotic statements; those follow from the preceding estimates.

## Relationship to prior work
Li and Zhang (2026), Eq. (2.1), introduced/studied this exact model. Their Theorem 2.1 determines existence of the positive equilibrium for \(b>1\), Lemma 2.1 analyzes the origin for \(b<1\) and \(b>1\), Section 3 establishes boundedness, and Section 4 treats geometric convergence to an asymptotically stable **positive** equilibrium. The critical case \(b=1\), whose origin has a unit multiplier, and its explicit reciprocal-time logarithmic correction are not stated in these inspected results. This theorem uses the same underlying map but is an orbitwise global asymptotic result at its nonhyperbolic extinction boundary, rather than a restatement of a local eigenvalue condition.

Beverton–Holt reciprocal transformations and parabolic-iteration expansions are standard methodological background. The new calculated coefficient and its cancellation surface depend on the coupling of the rational and exponential population responses in this specific two-dimensional map.

## Limitations
No explicit expression for the trajectory-dependent constant \(C\) is obtained. The theorem assumes strictly positive states and parameters, and exactly the critical multiplier \(b=1\). It does not describe basin boundaries for \(b>1\), coexistence-cycle bifurcations, noise, or environmental forcing. Novelty claims are relative to identified published material and recorded mathematical comparisons; exhaustive historical priority and independent verification are not asserted.

## References
1. B. Li and Q. Zhang, Neimark-Sacker bifurcation and dynamical behavior in a discrete predator-prey system with exponential terms, AIMS Mathematics 11 (2026), 23943–23963, DOI:10.3934/math.2026964 (published 2026-08-05). Full open-access paper: https://www.aimspress.com/aimspress-data/math/2026/8/PDF/math-11-08-964.pdf.
2. R. J. H. Beverton and S. J. Holt, *On the Dynamics of Exploited Fish Populations* (1957), classical rational recruitment dynamics, cited for methodological context, not an identical two-species theorem.
