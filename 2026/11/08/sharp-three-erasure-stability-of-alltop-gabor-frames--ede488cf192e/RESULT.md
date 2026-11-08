# Sharp three-erasure stability of Alltop Gabor frames

## Finding

For every prime \(p\ge 5\), set \(\omega=\exp(2\pi i/p)\) and
\[
 v_{a,b}(t)=p^{-1/2}\omega^{(t-a)^3+bt},
 \qquad a,b,t\in\mathbb F_p.
\]
For each three-element set \(E\subset\mathbb F_p^2\), let \(A_E\) denote the sharp lower frame bound of the surviving vectors \(\{v_{a,b}:(a,b)\notin E\}\) in \(\mathbb C^p\). Then
\[
 \boxed{\min_{|E|=3} A_E
 =p-1-\frac{2}{\sqrt p}
 \begin{cases}
 1,&p\equiv1\pmod4,\\
 \cos\!\left(\frac{\pi}{6p}\right),&p\equiv3\pmod4.
 \end{cases}}
\]
This minimum is attained by three erased vectors from three distinct translation classes. It is not attained by an erasure containing two vectors from the same translation class. The sharp worst-case condition number of the surviving **analysis** matrix is
\[
 \boxed{\sqrt{\frac{p}{\min_{|E|=3}A_E}}}.
\]
In particular, the optimum erased triple has zero projective Gram-cycle phase when \(p\equiv1\pmod4\), whereas in the other residue class its smallest achievable absolute phase is exactly \(\pi/(2p)\). The congruence-class distinction is an exact phase-quantization obstruction, not an asymptotic error term.

## Assumptions and scope

The vectors are the normalized, full finite Gabor orbit of the cubic Alltop window, and the ambient Hilbert space is \(\mathbb C^p\) with counting inner product. The erasures are *any three distinct labelled time-frequency shifts*, not random deletions. Frame bounds are those of the remaining \(p^2-3\) unit vectors; no spatial or temporal erasure restrictions are imposed. The prime \(p=3\) is excluded because cubic phases collapse and mutual unbiasedness used below fails. The result concerns linear complex frame measurements, not nonlinear magnitude-only phase retrieval, and does not optimize over alternative windows or over more than three erasures.

## Proof

**1. Complete frame and erasure reduction.** For each fixed translation \(a\), the \(p\) vectors obtained by varying \(b\) are an orthonormal basis (a diagonal unitary times the Fourier basis). Thus the complete frame operator is \(pI\). For any three erasures, let \(V_E\) be the synthesis matrix of the three deleted vectors and \(G_E=V_E^*V_E\) their \(3\times3\) Gram matrix. The surviving frame operator is \(pI-V_EV_E^*\). Its least eigenvalue is \(p-\lambda_{\max}(G_E)\). Since \(\operatorname{rank}(V_E)\le3<p\), its largest eigenvalue is exactly \(p\), which also proves the condition-number formula.

**2. Three possibilities for translation classes.** Expanding the cubic gives
\[
 (t-a)^3+bt=t^3+s_at^2+\beta_{a,b}t+\gamma_a,
 \quad s_a=-3a,\quad \beta_{a,b}=3a^2+b,\quad\gamma_a=-a^3.
\]
Because \(3\) is invertible, distinct translations give distinct slopes. The elementary quadratic Gauss sum
\[
 \sum_{t\in\mathbb F_p}\omega^{ut^2+vt}
 =\sqrt p\,\varepsilon_p\chi(u)\omega^{-v^2/(4u)}
 \qquad(u\ne0),
\]
where \(\chi\) is the quadratic character and \(\varepsilon_p=1\) for \(p\equiv1\pmod4\) and \(i\) for \(p\equiv3\pmod4\), shows that two vectors from different translation classes have inner-product modulus \(p^{-1/2}\). If all three deletions come from one class, \(\lambda_{\max}(G_E)=1\). If two come from one class and one from another, the eigenvalues are \(1\) and \(1\pm\sqrt{2/p}\), so \(\lambda_{\max}(G_E)=1+\sqrt{2/p}\).

**3. Exact Gram triangle for three distinct translations.** Label the deleted vectors by \(j=0,1,2\), with distinct slopes \(s_j\) and arbitrary linear coefficients \(\beta_j\). Put
\[
 P=(s_1-s_0)(s_2-s_1)(s_0-s_2),
 \qquad
 R=\beta_0(s_1-s_2)+\beta_1(s_2-s_0)+\beta_2(s_0-s_1).
\]
Both are interpreted in \(\mathbb F_p\), and \(P\ne0\). Let \(\rho\) be the normalized gauge-invariant Gram triangle
\[
 \rho=p^{3/2}
 \langle v_0,v_1\rangle
 \langle v_1,v_2\rangle
 \langle v_2,v_0\rangle.
\]
Applying the quadratic Gauss formula to each edge, and using
\[
 \frac{(\beta_1-\beta_0)^2}{s_1-s_0}
 +\frac{(\beta_2-\beta_1)^2}{s_2-s_1}
 +\frac{(\beta_0-\beta_2)^2}{s_0-s_2}
 =-\frac{R^2}{P},
\]
we obtain the **exact** phase identity
\[
 \boxed{\rho=\varepsilon_p^3\chi(P)\omega^{R^2/(4P)}}.
\]
The constant cubic coefficients \(\gamma_j\) cancel cyclically; no extra phase is hidden in the normalization. If \(\rho=e^{i\theta}\), with \(-\pi\le\theta\le\pi\), direct expansion of the characteristic polynomial of the Hermitian Gram matrix yields
\[
 \det(\tau I-\sqrt p(G_E-I))=\tau^3-3\tau-2\cos\theta.
\]
The largest root is \(2\cos(|\theta|/3)\), so
\[
 \lambda_{\max}(G_E)=1+\frac{2}{\sqrt p}\cos(|\theta|/3).
\]
This transforms the exact worst-case erasure problem into finding the smallest possible projective triangle angle.

**4. The arithmetic phase minimum and sharpness.** If \(p\equiv1\pmod4\), the Gauss factor \(\varepsilon_p^3=1\). Selecting a square \(P\) and \(R=0\) makes \(\rho=1\), hence the maximum possible Gram eigenvalue is \(1+2/\sqrt p\). If \(p\equiv3\pmod4\), the Gauss factor is \(-i\), and every possible phase has the form \(\pm i\omega^z\). The angular distance from such a point to \(1\) is at least \(\pi/(2p)\), since its angle in units of \(\pi/(2p)\) is an odd integer modulo \(4p\). This bound is attained by choosing \(\chi(P)=1\) and \(R^2=P\): indeed, \(\rho=-i\omega^{1/4}=\exp(i\pi/(2p))\), where the inverse fourth is evaluated modulo \(p\) and \(p\equiv3\pmod4\).

For completeness, these choices can always be implemented. Set \(s_0=0\), \(s_1=1\), \(s_2=u\), with \(u\in\mathbb F_p\setminus\{0,1\}\); then \(P=u(1-u)\). The elementary character identity \(\sum_{u\in\mathbb F_p}\chi(u(1-u))=-\chi(-1)\) implies that a square value \(P\) occurs for every odd prime \(p\ge5\). For a fixed such slope triple the linear map \((\beta_0,\beta_1,\beta_2)\mapsto R\) is surjective because \(s_1-s_2\ne0\); choose \(R=0\) in the first case or a square root of \(P\) in the second. Each prescribed \(\beta_j\) corresponds to a unique modulation \(b_j=\beta_j-3a_j^2\), with \(a_j=-s_j/3\). Thus the phase bounds are attained. Finally, both sharp three-class eigenvalues strictly exceed \(1+\sqrt{2/p}\), completing all case comparisons and the proof.

## Verification

Execute `python CHECK.py` with Python 3.10 or later and NumPy. The checker reconstructs the actual Alltop Gabor vectors and their Hermitian Gram matrices, checks tightness, exhaustively tests all unordered three-deletion sets for primes \(5,7,11\), and independently compares \(8{,}580\) direct Gram triple products with the arithmetic phase formula over primes \(5,7,11,13,17,19\). It verifies a constructed attaining deletion for every tested prime. Recorded output:

`CHECK_OK primes=6 exhaustive_erasure_triples=308704 direct_holonomies=8580`

These computations supplement, but do not replace, the finite-field Gauss-sum proof valid for every prime in the stated range. As a numerical cross-check, the sharp worst-case surviving analysis condition number at \(p=5\) is \(1.268861\ldots\), matching the corresponding three-erasure entry of Salanevich–Strachan's 2025 numerical table.

## Relationship to prior work

Salanevich and Strachan (arXiv:2509.01325; first posted September 1, 2025) proved dimension-uniform robustness guarantees for Gabor and mutually unbiased-basis frames, including the Alltop window. Their Theorems 1.5 and 5.5 give general erasure-rate/condition-number bounds, and their numerical Table 1 already includes a three-erasure computation in dimension five. The present infinite-prime theorem instead determines the *sharp* worst triple, its exact lower bound, and a congruence-dependent projective phase obstruction, without asserting novelty for their numerical dimension-five data.

Bengtsson, Blanchfield, Campbell and Howard (arXiv:1407.2713) investigate Alltop-vector Clifford orbits, particularly distinctions modulo three, not sharp three-deletion frame stability. Filippov and Man'ko (arXiv:1008.2675) develop general MUB projector triple-product relations, which are background for gauge-invariant phases but do not classify the Alltop Gram-triangle extremum. Previously published finite cyclic two-character frame-erasure results concern two-character harmonic frames rather than full Alltop Gabor frames. This distinction is by statements and implications, not merely titles.

## Limitations

The new claim is for exactly three deletions from the **full** normalized Gabor orbit in prime dimension at least five. It does not extend directly to nonprime cyclic groups, larger deletion numbers, partial time-frequency sampling or alternative windows. The 2025 source already tabulated the dimension-five numerical worst condition number; the novelty assessment concerns the uniform exact arithmetic formula and its attainers. While targeted searches did not reveal an equivalent general theorem, an older version formulated through triple Bargmann invariants or three-sparse restricted isometry may exist; publication priority has not been independently certified. Independent mathematical audit has not been performed.

## References

1. P. Salanevich and N. Q. D. Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions*, arXiv:2509.01325, first posted September 1, 2025. https://arxiv.org/abs/2509.01325
2. I. Bengtsson, K. Blanchfield, E. Campbell, and M. Howard, *Order 3 Symmetry in the Clifford Hierarchy*, arXiv:1407.2713 (2014). https://arxiv.org/html/1407.2713v3
3. S. N. Filippov and V. I. Man'ko, *Mutually unbiased bases: tomography of spin states and star-product scheme*, arXiv:1008.2675 (2010). https://arxiv.org/abs/1008.2675
4. M. Fickus and D. G. Mixon, *Numerically erasure-robust frames*, arXiv:1202.4525 (2012). https://arxiv.org/abs/1202.4525
