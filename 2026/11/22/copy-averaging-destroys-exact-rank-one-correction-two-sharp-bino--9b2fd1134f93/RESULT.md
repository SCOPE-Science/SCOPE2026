# Copy averaging destroys exact rank-one correction: two sharp binomial risk laws

## Finding

Consider a minimal two-mode model of independently programmed approximate inverses. Every individual programmed copy has a residual error of rank one and therefore admits a *perfect* exact one-dimensional correction. Nonetheless, averaging two or more copies generally produces a residual with rank two, making even the best one-dimensional correction imperfect.

Two sign regimes have different **complete finite-copy laws** and different asymptotic behavior. Define \(U_D=\sum_{j=1}^D\xi_j\), where \(\xi_j\) are independent fair signs, and put \(m_D=\mathbb E|U_D|\). Explicitly,
\[
m_D=\begin{cases}
\displaystyle\frac{D\binom{D}{D/2}}{2^D},&D\text{ even},\\[4pt]
\displaystyle\frac{(D+1)\binom{D}{(D-1)/2}}{2^D},&D\text{ odd}.
\end{cases}
\]
For every integer \(D\ge1\) and every \(0<\alpha<1\), the exact optimally corrected squared Frobenius errors are
\[
\boxed{R_D^{\mathrm{centered}}=\frac{\alpha^2}{2D^2}(D-m_D^2)},\qquad
\boxed{R_D^{\mathrm{one\text{-}sided}}=\alpha^2\left(\frac14+\frac{1}{4D}-\frac{m_D}{2D}\right)}.
\]
In particular, the centered model satisfies
\[
\lim_{D\to\infty}\frac{D R_D^{\mathrm{centered}}}{\alpha^2}=\frac12-\frac1\pi,
\]
whereas the one-sided model satisfies
\[
\lim_{D\to\infty}R_D^{\mathrm{one\text{-}sided}}=\frac{\alpha^2}{4},\qquad
\frac{R_D^{\mathrm{one\text{-}sided}}}{\alpha^2}=\frac14-\frac1{\sqrt{2\pi D}}+\frac1{4D}+O(D^{-3/2}).
\]
Both risks equal zero at \(D=1\), equal \(\alpha^2/8\) at \(D=2\), and are strictly positive for all \(D\ge2\). Thus, lower pre-correction mean-square error does not imply smaller error after a rank-one correction learned anew from each averaged realization.

## Assumptions and scope

Let \(A=I_2\), and let \(e_1,e_2\) be the standard real coordinate basis. Fix a scalar \(0<\alpha<1\). For each independent programming realization \(j\), choose \(J_j\) uniformly from \(\{1,2\}\) and set
\[
B_j=I_2-\alpha\varepsilon_j e_{J_j}e_{J_j}^{\mathsf T},\qquad
\bar B_D=\frac1D\sum_{j=1}^D B_j.
\]
The signs \(\varepsilon_j\) are either independent equiprobable \(\pm1\) (centered case), independent of the indices, or identically \(+1\) (one-sided case). All \(B_j\) are symmetric positive definite: their eigenvalues are \(1\) and \(1-\alpha\varepsilon_j>0\). There is no fresh read noise, finite probing error, nonlinear state dependence, or right-hand-side restriction.

For each realized \(B\), allow an *oracle* selection of any unit vector \(z\in\mathbb R^2\), depending on all programmed copies, and apply the exact corrected operator
\[
M_z(B)=B+zz^{\mathsf T}(I_2-B).
\]
This is the one-column specialization of the standard residual correction for \(A=I_2\). The objective is
\[
R_D=\mathbb E\left[\min_{\|z\|_2=1}\left\|I_2-M_z(\bar B_D)\right\|_F^2\right].
\]
The minimum is taken **inside** the expectation. This is an optimistic best-correction benchmark rather than the error of a particular randomized probing implementation.

## Proof

**Step 1: exact residual and optimal rank-one direction.** Write
\[
S_i=\sum_{j:J_j=i}\varepsilon_j\quad(i=1,2),\qquad
E_D=I_2-\bar B_D=\frac{\alpha}{D}\operatorname{diag}(S_1,S_2).
\]
Then \(I_2-M_z(\bar B_D)=(I_2-zz^{\mathsf T})E_D\). For any fixed \(E_D\),
\[
\left\|(I_2-zz^{\mathsf T})E_D\right\|_F^2
=\|E_D\|_F^2-z^{\mathsf T}E_DE_D^{\mathsf T}z.
\]
The Rayleigh maximum of the second term is the largest eigenvalue of \(E_DE_D^{\mathsf T}\). Hence the exact samplewise optimal residual is
\[
\min_{\|z\|_2=1}\|I_2-M_z(\bar B_D)\|_F^2
=\frac{\alpha^2}{D^2}\min(S_1^2,S_2^2).\tag{1}
\]
The direction with the larger absolute signed sum is optimal; either direction is optimal on a tie. A single copy has only one nonzero signed sum and thus zero optimal error.

**Step 2: centered signs.** When \(\varepsilon_j\) are fair signs and \(J_j\) is uniform, define \(U=S_1+S_2\) and \(V=S_1-S_2\). Every step \((\Delta U,\Delta V)\) is one of \((1,1),(1,-1),(-1,1),(-1,-1)\) with probability \(1/4\). Therefore \(U\) and \(V\) are independent copies of the same \(D\)-step simple symmetric walk. Using \(S_1=(U+V)/2\) and \(S_2=(U-V)/2\),
\[
\min(S_1^2,S_2^2)=\frac14\bigl(|U|-|V|\bigr)^2.
\]
Since \(\mathbb EU^2=\mathbb EV^2=D\), independence gives
\[
\mathbb E\min(S_1^2,S_2^2)=\frac12(D-m_D^2).
\]
Equation (1) proves the centered exact formula.

**Step 3: one-sided signs.** If every sign equals \(+1\), then \(K=S_1\sim\operatorname{Binomial}(D,1/2)\) and \(S_2=D-K\). We have the pointwise identity
\[
\min(K^2,(D-K)^2)=\left(\frac D2-\left|K-\frac D2\right|\right)^2.
\]
By symmetry of the simple walk, \(2K-D\) has the law of \(U_D\); hence \(\mathbb E|K-D/2|=m_D/2\) and \(\mathbb E(K-D/2)^2=D/4\). Expanding and dividing by \(D^2\) proves the one-sided exact formula.

**Step 4: the closed walk moment and asymptotics.** Conditioned on \(U_n\), the expected increment of \(|U_n|\) after one fair step is \(1\) if \(U_n=0\), and \(0\) otherwise. Thus \(m_{n+1}-m_n=\Pr(U_n=0)\). For even \(n=2h\), this probability equals \(\binom{2h}{h}2^{-2h}\), and it vanishes for odd \(n\). Telescoping, using the elementary central-binomial identity, yields the displayed even and odd formulas for \(m_D\). Stirling's expansion gives
\[
m_D=\sqrt{\frac{2D}{\pi}}\bigl(1+O(D^{-1})\bigr).
\]
Substituting into the exact risk identities proves both limits and the stated one-sided expansion.

**Step 5: comparison with no correction and strict positivity.** The same independent-copy calculation gives
\[
\mathbb E\|I_2-\bar B_D\|_F^2=
\begin{cases}
\alpha^2/D,&\text{centered signs},\\
\alpha^2\bigl(1/2+1/(2D)\bigr),&\text{one-sided signs}.
\end{cases}
\]
Both expressions strictly decrease with \(D\). At \(D=1\), equation (1) vanishes; at \(D=2\), each model has probability \(1/2\) of choosing different coordinate directions, producing \(\alpha^2/4\) error on that event, so \(R_2=\alpha^2/8\). For every \(D\ge2\), the event that all signs are positive and both coordinate indices occur has positive probability and both \(|S_1|,|S_2|\) are nonzero. Equation (1) then proves \(R_D>0\).

## Verification

The accompanying `check.py` uses only the Python standard library. Running `python3 check.py` checks the oracle Rayleigh bound, exact multinomial sums against independent sequence enumeration for small copy counts, both binomial closed forms for many copy counts, and sample asymptotic constants. It executes 2,557 deterministic assertions. These finite checks are supplements, not replacements for the proof of the identities for every \(D\ge1\) or of the limits.

## Relationship to prior work

Shah, Li, Kalantzis and Xi (2026) propose analog block-Jacobi preconditioning with a digital low-rank residual correction, derive the exact projected residual identity, separate write and read errors, and explain that copy averaging alone need not make the *corrected* residual improve monotonically. In particular, this paper already states the qualitative possibility of nonmonotonicity. The present theorem does **not** claim that observation or the projection identity as new. It specializes to a two-mode programmed-copy model and supplies the complete exact finite-copy laws for two natural noise regimes, an immediate one-to-two-copy reversal, and the contrasting asymptotic rates. The Rayleigh/Eckart–Young characterization and simple-walk absolute moments used in the proof are classical ingredients.

Existing general low-rank and stochastic preconditioner analyses address different objectives or assumptions. The example is an explicit benchmark for how a fixed correction dimension interacts with independently programmed copy averaging, not an assertion of universal deterioration across models.

## Limitations

The error criterion is the squared Frobenius norm of the **one-application operator defect**, not the expected squared error for a particular right-hand side. The best correction direction is selected with full knowledge of the sampled matrices; a finite-cost probing algorithm can do worse. The model is two-dimensional, assumes independent coordinate defects of equal magnitude and fixed sign laws, and ignores fresh read fluctuations. The one-sided noise regime has nonzero programming bias. No full FGMRES convergence, hardware time/energy optimality, or general monotonicity classification is claimed. The risk is positive after copy averaging even though it tends to zero in the centered regime.

## References

- S. Shah, R. P. Li, V. Kalantzis and Y. Xi, *Noise-Adaptive Analog–Digital Preconditioning*, arXiv:2611.17251v1, first publicly available 2026-11-12. https://arxiv.org/html/2611.17251
- A. I. Osinsky, *On the existence of a close to optimal cross approximation in the Frobenius norm*, Sbornik Mathematics 216 (2025), doi:10.4213/sm10123e. Cited for background on classical best rank-one Frobenius approximation, not for this stochastic binomial law. https://doi.org/10.4213/sm10123e
