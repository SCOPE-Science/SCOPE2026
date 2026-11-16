# A sharp three-lag strong two-window phase-retrieval threshold on the ten-cycle

## Finding

Let \(\mathbb Z_{10}\) be the ten-point cyclic group, and let \(V_g f\) be the complete discrete short-time Fourier transform (STFT) of \(f\) with a known window \(g\). Write \(\widehat g\) for the discrete Fourier transform of \(g\). **Strong two-window phase retrieval** means that for every nonzero \(f\), at least one of the two entire magnitude arrays \(|V_gf|\) and \(|V_{\widehat g}f|\), *on its own*, determines \(f\) up to global phase among arbitrary complex ten-vectors.

**Theorem (sharp ten-site bandwidth).** Define \(g_m(j)=2^j\) for \(0\le j\le m\) and \(g_m(j)=0\) otherwise, for integers \(0\le m\le4\). Then \((g_m,\widehat g_m)\) does strong two-window phase retrieval **if and only if** \(m\ge3\). More generally, every window \(g\) with nonvanishing ambiguity function at *all* modulation indices for each of the seven translation lags \(0,\pm1,\pm2,\pm3\) has strong two-window phase retrieval with its Fourier transform. Sharpness at two lags has an explicit signal with both cyclic time support and cyclic Fourier support disconnected at displacement at most two.

In particular, the universal sufficient threshold for this composite dimension is three, improving the earlier general-composite estimate (which requires \(m\ge4\)) by one full translation lag. Unlike a prime-period translation-sector result, the statement covers *every* vector in \(\mathbb C^{10}\).

## Assumptions and scope

All indices are modulo ten. Fix the Fourier convention \(\widehat f(k)=\sum_{j=0}^{9}f(j)\exp(-2\pi i jk/10)\) and the STFT \(V_gf(a,b)=\sum_jf(j)\overline{g(j-a)}\exp(-2\pi i jb/10)\). For a signal \(f\) and bandwidth \(m\), form the undirected graph on \(\operatorname{supp}f\) joining distinct \(x,y\) whenever \(x-y\) modulo ten lies in \(\{\pm1,\ldots,\pm m\}\). Call the support \(m\)-disconnected when that graph has at least two components. Zero and one-vertex supports are not disconnected.

The complete set of translations and modulations is measured for each window, with arbitrary complex signals and no noise. Nonzero ambiguity on the seven stated lag rows is the only condition for the general sufficiency assertion. The exact-support-band assertion for \(g_m\) uses \(0\le m\le4\), so there is no wrapped overlap outside the band.

## Proof

**1. Convert magnitude data to phase edges.** Two-dimensional Fourier transformation of \(|V_gf|^2\) gives, up to a known nonzero normalization and index sign, the pointwise product of the ambiguity functions of \(f\) and \(g\). If the ambiguity of \(g\) is nonzero for every modulation at translation \(a\), Fourier inversion in modulation recovers each product \(f(j)\overline{f(j-a)}\). At \(a=0\), this includes every \(|f(j)|^2\). Recovering products for \(|a|\le m\) therefore recovers the phase on each connected component of the \(m\)-support graph; a connected graph suffices for uniqueness up to one global phase. Fourier covariance of the STFT says that a signal \(f\) is retrievable with \(\widehat g\) precisely when \(\widehat f\) is retrievable with \(g\). For the exponential bands \(g_m\), their ambiguity is nonzero exactly for lags \(-m,\ldots,m\): for a fixed overlap lag, the summands are a geometric progression with consecutive modulus ratio four, so no modulation can cancel them. Thus for those windows the connectedness criterion is also *necessary*: independent component phase rotations leave all known products unchanged.

**2. There is no simultaneously three-disconnected time/Fourier support in dimension ten.** A complete, exact finite argument follows. Enumerate all nonempty subsets of \(\mathbb Z_{10}\); a breadth-first search with edges of cyclic lengths one, two, and three finds exactly 60 disconnected sets. Modulo cyclic rotation their seven representatives, ordered by cardinality, are

\[
\{0,4\},\ \{0,5\},\ \{0,1,5\},\ \{0,1,6\},\ \{0,2,6\},\ \{0,1,2,6\},\ \{0,1,5,6\}.
\]

For putative time and Fourier supports \(S,T\), let \(F_{T^c,S}\) be the matrix with rows indexed by \(\mathbb Z_{10}\setminus T\), columns indexed by \(S\), and entries \(\zeta^{kj}\), where \(\zeta=\exp(-2\pi i/10)\). A nonzero signal supported inside \(S\) whose Fourier transform is supported inside \(T\) exists only if \(F_{T^c,S}\) fails to have full column rank.

The prime \(1021\) satisfies \(1021\equiv1\pmod {10}\), and \(\rho=432\in\mathbb F_{1021}\) has exact multiplicative order ten; in particular \(\Phi_{10}(\rho)=\rho^4-\rho^3+\rho^2-\rho+1=0\). Thus there is a specialization \(\mathbb Z[\zeta]\to\mathbb F_{1021}\), \(\zeta\mapsto\rho\). If an algebraic Fourier minor vanishes over \(\mathbb C\), its reduction modulo 1021 also vanishes. Contrapositively, full column rank of the reduced matrix certifies full column rank over \(\mathbb C\).

The embedded script `CHECK.py` independently enumerates all 60 disconnected supports and checks **all 3,600 ordered pairs** \((S,T)\). For every pair it performs exact Gaussian elimination modulo 1021 on \((\rho^{kj})_{k\notin T,j\in S}\), obtaining rank exactly \(|S|\). It also verifies the seven rotation representatives and all 49 representative-pair ranks. The finite test is *exhaustive*, not a statistical sample: all subsets and every ordered pair have been checked. Therefore no nonzero ten-vector can have both its time support and its Fourier support three-disconnected.

By Step 1, for every ten-vector either \(g\) or \(\widehat g\) recovers it whenever the ambiguity of \(g\) is nowhere zero on the three-lag band. This proves the general statement, and also establishes the sufficiency for \(g_3,g_4\).

**3. Sharpness at bandwidth two.** Put \(\omega=\exp(2\pi i/10)\) and let the coefficient vector \(f\) be defined by the generating polynomial

\[
\sum_{j=0}^{9}f(j)z^j=(1+z^5)(z-1)(z-\omega^{-4}).
\]

All six indicated coefficients are nonzero and \(\operatorname{supp}f=\{0,1,2,5,6,7\}\). Its two occupied triples are separated by the zero pairs \(\{3,4\}\) and \(\{8,9\}\), so its two-lag support graph is disconnected. Since \(\widehat f(k)\) is the displayed polynomial evaluated at \(\omega^{-k}\), the factor \(1+z^5\) removes all odd frequencies, and the remaining two factors remove precisely frequencies 0 and 4. Consequently

\[
\operatorname{supp}\widehat f=\{2,6,8\},
\]

whose two-lag graph is also disconnected (the vertex 2 is isolated from the pair 6,8). The full-band ambiguity support of \(g_2\) and the phase-rotation argument in Step 1 show that neither \(g_2\) nor \(\widehat g_2\) retrieves this signal; the same witness works for narrower bands \(g_0,g_1\). Hence the threshold of three is sharp.

## Verification

Run `python CHECK.py` with Python 3 and no third-party dependencies. The expected output is `CHECK_OK disconnected_supports=60 rotation_orbits=7 exact_modular_ranks=3600 sharp_witness=verified`. The script checks primality, exact order and cyclotomic congruence for the finite-field root, the complete support graph census, all 3,600 exact ranks, and the explicit counterexample's supports via an exact modular specialization. Nonvanishing mod 1021 is only used in the direction which rigorously implies nonvanishing over the characteristic-zero cyclotomic field; vanishing of the counterexample's Fourier coefficients is proved by the displayed factorization over \(\mathbb C\). No finite heuristic is used as an infinite proof; the claim concerns a fixed ten-point cyclic group.

## Relationship to prior work

Bartusel (2026) develops strong two-window STFT phase retrieval and gives the composite-order sufficient criterion \(m>(d-1)/3\), which only yields \(m\ge4\) for \(d=10\). The present exact ten-site threshold is \(m=3\). Bartusel (2023) proves the connected-support characterization used in the reduction. The previously published *Sharp strong two-window STFT thresholds in prime-period Floquet sectors* establishes \(m\ge3\) for each translation eigenspace of period five in the ten-cycle; its explicit limitation is that it does **not** cover arbitrary combinations of eigensector vectors. Our rank argument applies to the full ten-dimensional signal space and does not follow from individual-sector injectivity. The exact order-eight/nine Fourier support-incidence tables in related work concern different cyclic orders and do not supply the ten-site full-space implication.

## Limitations

This is a fixed, natural first-composite-order sharp classification, not a formula for every composite order. It does not establish robustness constants, an optimal result for pairs of unrelated windows, or a criterion for arbitrary incomplete modulation sampling. The full-rank computations are exact over one prime and form a finite certificate that is independently reproducible; no independent mathematical audit has been performed. Historical priority beyond the inspected primary sources and databases remains provisional.

## References

1. D. Bartusel, *Uncertainty Principles as a Tool for STFT Phase Retrieval*, arXiv:2605.31507 (first publicly posted 2026-05-29), especially Theorem 2.4, Lemma 2.5, Theorem 2.6 and Corollary 2.8. https://arxiv.org/abs/2605.31507
2. D. Bartusel, *Injectivity Conditions for STFT Phase Retrieval on \(\mathbb Z\), \(\mathbb Z_d\) and \(\mathbb R^d\)*, J. Fourier Anal. Appl. 29, 53 (2023), DOI:10.1007/s00041-023-10026-2, especially Theorem 2.2.3. https://doi.org/10.1007/s00041-023-10026-2
3. *Sharp strong two-window STFT thresholds in prime-period Floquet sectors*, published research record, 2026-10-18, identifier `000a2ee07250`, in particular the stated restriction to individual translation eigenspaces. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-strong-two-window-stft-thresholds-in-prime-period-floquet--000a2ee07250
