# A unique positive-coupling construction of arbitrary-order exceptional points with one terminal loss

## Finding
For every integer \(m\ge2\) and decay scale \(\beta>0\), the resonant \(m\)-site nearest-neighbor chain with **only its last site damped** possesses a full-order exceptional point if and only if its damping and positive couplings have the following form:
\[
\gamma=m\beta,\qquad
 g_j^2=\beta^2\frac{j(2m-j)}{[2(m-j)-1][2(m-j)+1]},\qquad 1\le j<m.
\]
In the frame rotating at the common on-site energy, the full spectrum is the single eigenvalue \(-\beta\), with geometric multiplicity one and algebraic multiplicity \(m\). For a fixed \(m\) and \(\beta\), this positive-coupling terminal-loss realization is unique. Equivalently, with a fixed positive terminal rate \(\gamma\), take \(\beta=\gamma/m\); no further tuning freedom remains apart from physically irrelevant signs of the hoppings and an overall common site energy.

## Assumptions and scope
Let \(m\in\{2,3,\ldots\}\), \(g_j>0\), \(\gamma>0\), and let \(A\) be the complex symmetric tridiagonal matrix with \(A_{jj}=0\) for \(j<m\), \(A_{mm}=-\gamma\), \(A_{j,j+1}=A_{j+1,j}=-i g_j\), and all other entries zero. This is the linear no-jump/Heisenberg drift of a resonant coherent chain when the terminal site alone undergoes amplitude damping at rate \(\gamma\). The conventional Lindblad population-loss rate is \(2\gamma\). A common on-site energy \(\epsilon\) adds \(-i\epsilon I\) and shifts all eigenvalues without changing the finding. All \(g_j\) are real and strictly positive; the claim does not allow arbitrary diagonal detuning, hopping phases, or additional loss sites.

## Proof
Write \(Q_k(z)\) for the determinant of \(zI\) minus the undamped leading \(k\times k\) subchain. Expanding successive terminal minors gives
\[
Q_0=1,\quad Q_1=z,\quad Q_{k+1}=zQ_k+g_k^2Q_{k-1}\quad(1\le k<m).
\]
All \(Q_k\) are monic and have parity \(k\). By expanding the last damped diagonal of \(zI-A\), the actual characteristic polynomial is
\[
P(z)=Q_m(z)+\gamma Q_{m-1}(z).
\]
If all eigenvalues equal \(-\beta\), comparison of the coefficient of \(z^{m-1}\) yields \(\gamma=m\beta\). The identity \(P(z)=(z+\beta)^m\), together with opposite parities of \(Q_m\) and \(Q_{m-1}\), uniquely determines both polynomials:
\[
Q_m(z)=\frac{(z+\beta)^m+(-1)^m(\beta-z)^m}{2},\quad
Q_{m-1}(z)=\frac{(z+\beta)^m-(-1)^m(\beta-z)^m}{2m\beta}.
\]
The second numerator has leading term \(2m\beta z^{m-1}\). Starting with these two known monic polynomials, the identity \(Q_{k+1}-zQ_k=g_k^2Q_{k-1}\) uniquely recovers \(g_k^2\) as the leading coefficient of the left side, then uniquely recovers \(Q_{k-1}\) by division. Descending induction proves *at most one* positive-coupling solution.

For existence, put \(\lambda=\tfrac12-m\), and let \(C_k^{(\lambda)}\) denote the Gegenbauer polynomial of degree \(k\), normalized to be monic. For \(0\le k\le m\), its leading coefficient is nonzero because \(\lambda\) is a negative half-integer. The standard three-term identity for monic Gegenbauer polynomials is
\[
Q_{k+1}(z)=zQ_k(z)-\beta^2\frac{k(k+2\lambda-1)}{4(k+\lambda)(k+\lambda-1)}Q_{k-1}(z)
=zQ_k(z)+\beta^2\frac{k(2m-k)}{[2(m-k)-1][2(m-k)+1]}Q_{k-1}(z).
\]
Here the monic polynomials are evaluated at \(z/\beta\) and scaled by \(\beta^k\). For every \(1\le k<m\) the displayed squared coupling is strictly positive. The recurrence is also verifiable directly from the Gegenbauer differential equation or its finite coefficient expansion, and the associated coefficient checker is included.

To identify its final pair, the (scaled) Gegenbauer equation is
\[
(\beta^2-z^2)y''+(2m-2)zy'-m(m-1)y=0
\]
for both degrees \(m\) and \(m-1\), because they have the same Gegenbauer eigenvalue when \(\lambda=\tfrac12-m\). Both \((z+\beta)^m\) and \((z-\beta)^m\) solve this equation. Their monic parity components are therefore exactly \(Q_m\) and \(Q_{m-1}\) displayed above. (Within each fixed parity and degree, the monic polynomial solution is unique: descending the coefficient recurrence has nonzero denominators for all lower terms of that parity.) Thus \(Q_m+m\beta Q_{m-1}=(z+\beta)^m\).

Finally, because every off-diagonal entry is nonzero, an eigenvector is determined uniquely up to scale by its first coordinate: if that coordinate is zero, the first row forces the second to zero, and the row recurrence forces every coordinate to zero. Hence every eigenvalue has geometric multiplicity one. The sole eigenvalue \(-\beta\) with algebraic multiplicity \(m\) therefore has one length-\(m\) Jordan block: a genuine order-\(m\) exceptional point. Together with the descending uniqueness argument this proves the claim.

## Verification
The standalone `verify_ep.py` uses exact rational polynomial arithmetic. It checks the recurrence, predicted characteristic polynomial, positive coupling squares, parity identities and descending inverse recovery for all integers \(2\le m\le45\) at \(\beta\in\{1,2/3,5/4\}\). Finite checks confirm the algebra in tested dimensions but do not substitute for the preceding all-\(m\) proof. Example squared couplings in units of \(\beta^2\): for \(m=3\), \((1/3,8/3)\); for \(m=4\), \((1/5,4/5,5)\). No arbitrary-precision numerical eigenvalue clustering is used as proof of a defective spectrum.

## Relationship to prior work
Holst, Blasi and Khandelwal (2026), Section VIII.1, formulate exactly this resonant terminal-damped reaction-coordinate chain and establish the Erlang escape-time law *conditional on* a maximal exceptional point. The contribution here is the explicit all-size positive parameter synthesis together with its uniqueness, not the previously derived escape law. The classical Gegenbauer polynomial recurrence is not claimed as new. Znojil (2010) gives a tridiagonal Gegenbauer-based quantum model with eigenvalues given by zeros of polynomials, but its stated construction does not give this rank-one terminal-damping inverse design with one repeated eigenvalue. Wiersig and Chen (2025) construct higher-order EPs by composite tensor products, not the specified single-loss irreducible path. These comparisons do not establish absolute publication priority.

## Limitations
The theorem is restricted to uniform real site energies, strictly positive real nearest-neighbor couplings and a single damped end site. It is an exact finite-dimensional inverse spectral theorem, not a claim that a finite device realizes arbitrary amplitudes without calibration error. Stability under disorder, fabrication tolerance and spectral splitting are not covered. Only the inspected portions of the motivating source and accessible comparable literature support the novelty assessment; implicit equivalences in specialist inverse-spectral literature remain possible. Independent review has not been performed.

## References
1. D. Holst, G. Blasi and S. Khandelwal, *Non-Markovian exceptional points and information backflow: a Heisenberg reaction-coordinate approach* (first public 2026-10-19), arXiv:2610.26620v1, https://arxiv.org/abs/2610.26620.
2. M. Znojil, *Gegenbauer-solvable quantum chain model*, Phys. Rev. A **82**, 052113 (2010), https://doi.org/10.1103/PhysRevA.82.052113.
3. J. Wiersig and W. Chen, *Higher-order exceptional points in composite non-Hermitian systems* (2025), arXiv:2504.06906, https://arxiv.org/abs/2504.06906.
