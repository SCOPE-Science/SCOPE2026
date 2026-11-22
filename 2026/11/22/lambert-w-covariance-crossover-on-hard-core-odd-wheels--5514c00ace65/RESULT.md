# Lambert-\(W\) covariance crossover on hard-core odd wheels

## Finding
For every odd integer \(n=2m+1\ge7\), let \(W_n=K_1\vee C_n\) denote the wheel with rim vertices \(0,1,\ldots,n-1\) in cyclic order and one hub. In the grand-canonical hard-core gas at common positive activity \(z\), let \(X_j\) be the occupation indicator at rim vertex \(j\), and write \(K_n(z)=\operatorname{Cov}_z(X_0,X_3)\). Define the path independence polynomial \(P_k(z)\) by \(P_0=1\), \(P_1=1+z\), and \(P_k=P_{k-1}+zP_{k-2}\), and put \(C_n(z)=P_{n-1}(z)+zP_{n-3}(z)\). Then the **exact all-activity identity** is
\[
K_n(z)=\frac{z^2\bigl(P_{n-6}(z)[C_n(z)+z]-P_{n-3}(z)^2\bigr)}{[C_n(z)+z]^2}.
\]
For every such odd \(n\), \(K_n(z)>0\) for all sufficiently small \(z>0\), whereas \(K_n(z)<0\) for all sufficiently large \(z\). Thus it has at least one positive zero. More sharply, let \(W(x)\) be the positive principal Lambert function characterized by \(W(x)e^{W(x)}=x\), and for fixed real \(s\) define \(z_n(s)=W(ne^s)/n\). Along odd \(n\to\infty\),
\[
\frac{K_n(z_n(s))}{z_n(s)^4}\longrightarrow e^{-s}-1,
\]
uniformly for \(s\) in any bounded real interval. Consequently, there exist covariance zeros \(\xi_n>0\) (one for each sufficiently large odd \(n\)) such that
\[
n\xi_n-W(n)\longrightarrow0.
\]
No uniqueness of positive zeros is asserted.

## Assumptions and scope
All graphs are finite, simple and labelled, with wheel convention \(W_n=K_1\vee C_n\) (thus \(n+1\) total vertices); the rim length is odd \(n\ge7\). Every vertex has the same activity \(z>0\) and adjacent sites may not be simultaneously occupied. The distance three is measured along the rim, not in the entire wheel, where both sites are distance two through the hub. The observable is the connected equal-time occupation covariance in the equilibrium Gibbs law; there is no dynamics or thermodynamic-limit phase transition in the claim.

## Proof
**Exact marked partition functions.** The independence polynomial of the wheel is \(Z_n=C_n+z\): either the hub is vacant and the rim is a hard-core cycle, or the hub is occupied alone. Fixing rim site \(0\) occupied removes that site and its two rim neighbours, while excluding the hub, leaving the path of \(n-3\) sites. Thus \(Z_n\mathbb E X_0=zP_{n-3}\). Fixing both rim sites \(0\) and \(3\) occupied removes their six distinct rim-neighbourhood sites, leaving the path of \(n-6\) sites: \(Z_n\mathbb E(X_0X_3)=z^2P_{n-6}\). Subtracting the square of the single-site mean gives the stated exact covariance.

**Opposite endpoint signs.** For every fixed \(n\), the polynomial \(F_n=P_{n-6}(C_n+z)-P_{n-3}^2\) has \(F_n(0)=0\), \(F_n'(0)=1\): the derivative of \(P_{n-6}C_n-P_{n-3}^2\) vanishes by the first-order path and cycle coefficients. Therefore \(K_n(z)=z^3+O(z^4)>0\) near zero. Write \(n=2m+1\) with \(m\ge3\). The leading coefficients of \(P_{n-6},P_{n-3},C_n\) are respectively \(1,m,n\), with degrees respectively \(m-2,m-1,m\). The hub term \(zP_{n-6}\) has strictly smaller degree than \(2m-2\). Hence the leading coefficient of \(F_n\), at degree \(2m-2\), is \(n-m^2=2m+1-m^2<0\), and in fact \(\lim_{z\to\infty}K_n(z)=(n-m^2)/n^2<0\). Continuity establishes at least one positive zero.

**Critical scaling.** Put \(\Delta=\sqrt{1+4z}\), \(\lambda_\pm=(1\pm\Delta)/2\), and \(q=\lambda_-/\lambda_+\). For \(z>0\), \(-1<q<0\), and the standard path and cycle recurrence yields
\[
P_k(z)=\frac{\lambda_+^{k+2}-\lambda_-^{k+2}}{\Delta},\qquad C_n(z)=\lambda_+^n(1+q^n).
\]
Condition on the hub being vacant. Let \(\rho_n=zP_{n-3}/C_n\) and \(\eta_n=z^2P_{n-6}/C_n\) be the rim one-site and marked-pair probabilities in the cycle law, and let \(p_n=z/(C_n+z)\) be the hub occupation probability in the wheel. Its rim marginal is a mixture of the cycle law with an all-empty rim, so
\[
K_n(z)=(1-p_n)\rho_n^2[p_n-R_n],\qquad R_n=1-\frac{\eta_n}{\rho_n^2}.
\]
The transfer-root identity gives exactly
\[
R_n=1-(1-q^2)\frac{(1-q^{n-4})(1+q^n)}{(1-q^{n-1})^2}.
\]
For \(z=z_n(s)=W(ne^s)/n\), uniformly with \(s\) in a fixed compact interval, \(z=O(\log n/n)\), \(q=-z+O(z^2)\), \(R_n=z^2(1+o(1))\), and \(\rho_n=z(1+o(1))\). Also \(n z^2=o(1)\) and \(C_n=e^{nz}(1+o(1))\). By the defining identity for \(W\), \(z e^{nz}=e^s\), so \(p_n/z^2\to e^{-s}\), and \(1-p_n\to1\). Substitution yields the stated uniform normalized covariance profile.

For any fixed \(\varepsilon>0\), the profile implies positive covariance at \(z_n(-\varepsilon)\) and negative covariance at \(z_n(+\varepsilon)\), for all sufficiently large odd \(n\). Choose a zero between those activities. Uniformity of the profile on bounded intervals implies its corresponding scaling parameter tends to zero. Since \(W(ne^s)-W(n)\to s\) uniformly on bounded \(s\)-intervals, the zero satisfies \(n\xi_n-W(n)\to0\).

## Verification
The standalone `verify.py` performs independent labelled-configuration enumeration at rim lengths \(n=7,9,11,13\) and compares all coefficients of the three marked partition functions with their path-recurrence formulas. It also checks the leading and linear coefficients of the covariance numerator, opposite-sign finite examples, and the predicted signs on both sides of the Lambert window for \(n=101,301,1001,3001\). It checks numerical convergence of the normalized profile at \(n=10001\). Run `python3 verify.py` using the Python 3 standard library. The successful report ends with `ALL_NEW_WHEEL_CHECKS_PASSED`. These finite tests are supplementary, not the proof of the asymptotic statement.

## Relationship to prior work
Scott and Sokal (first public preprint, 2003) formulate the multivariate hard-core independence polynomial and give path and cycle recurrences and their transfer roots; those recurrences are explicitly used here. Alikhani and Peng (public online 2010) provide the *univariate* wheel independence polynomial, equivalent to \(C_n+z\), and study independence roots/fractals. Neither inspected source supplies the wheel's distance-three marked two-point covariance or its Lambert-\(W\) scaling profile. The new claim is a particular *observable and sharp crossover*, not a new independent-set partition identity. Existing published studies of wheel adsorption dynamics and wheel spanning trees use different measures and do not imply this equilibrium statement.

## Limitations
The existence of at least one positive covariance zero is proved for odd rims of length at least seven, and the asymptotic location is existential. No uniqueness, monotonicity of all zeros, root census, finite-temperature phase transition, or extension to even rims is claimed. The profile concerns precisely the distance-three rim pair and uniform vertex activity. A bibliographically undiscovered equivalent result remains possible; independent scientific audit has not been performed.

## References
- A. D. Scott and A. D. Sokal, *The repulsive lattice gas, the independent-set polynomial, and the Lovász local lemma*, public arXiv preprint cond-mat/0309352, September 15, 2003; J. Stat. Phys. 118 (2005), 1151–1261. https://arxiv.org/abs/cond-mat/0309352 ; lawful open text https://people.maths.ox.ac.uk/scott/Papers/lovasz.pdf .
- S. Alikhani and Y.-H. Peng, *Independence roots and independence fractals of certain graphs*, J. Appl. Math. Comput. 36 (2011), 89–100, first published online March 21, 2010. https://doi.org/10.1007/s12190-010-0389-4 .
