# Exact four-lag strong two-window Fourier phase retrieval on the fourteen-cycle

## Finding

Let \(\mathbb Z_{14}\) be the fourteen-point cyclic group, equipped with the unnormalized discrete Fourier transform \(\widehat f(k)=\sum_{j=0}^{13}f(j)e^{-2\pi i jk/14}\). For each integer \(0\le m\le6\), define the real exponential window \(g_m(j)=2^j\) on \(j=0,\ldots,m\) and \(g_m(j)=0\) elsewhere. Then the pair \((g_m,\widehat g_m)\) performs **strong two-window STFT phase retrieval** on all of \(\mathbb C^{14}\) if and only if \(m\ge4\): every nonzero complex signal is determined up to one global phase by at least one of its two *individual complete* STFT magnitude arrays, whereas for \(m\le3\) one signal fails uniqueness for each array separately.

This is a complete finite-dimensional threshold, not merely a sufficient bound. It improves the general composite-order sufficient threshold \(m\ge5\) from Bartusel's 2026 theorem in the first unclassified twice-odd-prime dimension after ten and matches the obstruction coming from prime-period sectors. The ambiguity-function translation support needed for the strong property decreases from eleven to nine complete cyclic lag classes.

## Assumptions and scope

The STFT convention is
\[
V_g f(a,b)=\sum_{j=0}^{13}f(j)\overline{g(j-a)}e^{-2\pi i jb/14},\qquad a,b\in\mathbb Z_{14}.
\]
A signal \(f\ne0\) is phase retrievable with a window \(g\) when \(|V_g h|=|V_g f|\) at every pair \((a,b)\), for an arbitrary competing \(h\in\mathbb C^{14}\), implies \(h=\lambda f\) for some \(|\lambda|=1\). Strong two-window recovery requires that, for every \(f\), **at least one** of \(g_m\) and \(\widehat g_m\) separately has this property. The two arrays are not combined when testing uniqueness. The range \(0\le m\le6\) ensures that the window occupies at most half of the cycle and its ambiguity translation support is exactly \(\{-m,\ldots,m\}\).

For a nonempty subset \(S\subseteq\mathbb Z_{14}\), let \(G_m[S]\) be the graph with vertex set \(S\) and edges between distinct vertices whose least cyclic distance is at most \(m\). Disconnectedness always means at least two nonempty connected components. For \(m=0\), the graph has no edges.

## Proof

**1. Recoverable products and graph connectivity.** For \(0\le a\le m\), the ambiguity function of \(g_m\) is a nonzero constant multiple of a geometric sum with ratio \(4e^{-2\pi ib/14}\) and length \(m-a+1\). Its modulus ratio is four, so no such sum vanishes. For \(m<a<14-m\), the translated windows do not overlap, and negative displacements obey the conjugate symmetry. Consequently, Fourier inversion of the squared STFT magnitudes recovers exactly the products \(f(j)\overline{f(j-a)}\) for cyclic distances \(|a|\le m\), including all coordinate magnitudes at \(a=0\). Along a connected nonzero support graph these products determine every relative phase. If the graph has at least two components, independent phase rotations of its components preserve every recovered product but are not a common global phase. Hence \(f\) is phase retrievable with \(g_m\) exactly when \(G_m[\operatorname{supp} f]\) is connected. By Fourier covariance of the STFT, \(f\) is phase retrievable with \(\widehat g_m\) exactly when \(G_m[\operatorname{supp}\widehat f]\) is connected.

**2. The four-lag upper bound by an exhaustive cyclotomic certificate.** Suppose both graphs were disconnected at \(m=4\). Write \(S=\operatorname{supp}f\) and \(T=\operatorname{supp}\widehat f\). In that case the restriction
\[
\mathcal F_{14}[T^c,S]=\left(e^{-2\pi i jk/14}\right)_{j\in T^c,\,k\in S}
\]
would have a nonzero null vector and hence rank less than \(|S|\). The standalone `CHECK.py` exhaustively rules this out, as follows. It lists all \(2^{14}-1\) nonempty support masks and finds exactly \(560\) whose induced distance-four graphs disconnect. Their cyclic-translation orbits have exactly \(42\) representatives. Independently translating a Fourier restriction's row or column indices merely applies invertible diagonal factors, so rank is unchanged. Thus only \(42^2=1764\) pairs of representatives need examination.

For every pair, the certificate computes exact row rank over \(\mathbb F_{1009}\) of the matrix \((904^{jk})_{j\in T^c,k\in S}\), and obtains rank \(|S|\). The number \(1009\) is prime and \(904\) has multiplicative order \(14\) in this field. The homomorphism \(\mathbb Z[\zeta_{14}]\to\mathbb F_{1009}\) given by \(\zeta_{14}\mapsto904\) shows that any nonzero minor after reduction was nonzero before reduction: a vanishing complex cyclotomic determinant would reduce to zero in every such field. Thus **all** \(1764\) ranks certify full column rank over \(\mathbb C\). There is no nonzero complex signal with both support graphs disconnected at bandwidth four. This proves the upper implication; monotonicity of graph connectivity extends it to \(m=5,6\).

**3. Sharp failure at three lags.** Let \(\eta=e^{-2\pi i/7}\) and \(E=\{0,1,4,5\}\subset\mathbb Z_7\). Form the \(3\times4\) matrix \(H=(\eta^{re})_{r\in\{4,5,6\},e\in E}\). Each of its four three-column minors is nonzero, so its one-dimensional nullspace has a vector \(c=(c_e)_{e\in E}\) with every entry nonzero. Moreover, adjoining any one row indexed by \(0,1,2,3\) produces a nonsingular \(4\times4\) matrix, so the four remaining Fourier values of \(c\) are nonzero. These eight claims are checked by the same exact cyclotomic reduction in `CHECK.py`, using \(904^2\) as a seventh root of unity.

Define \(f(2e)=c_e\) for \(e\in E\), and zero at all other positions on \(\mathbb Z_{14}\). Then
\[
\operatorname{supp}f=\{0,2,8,10\},\qquad
\operatorname{supp}\widehat f=\{0,1,2,3,7,8,9,10\}.
\]
The first support has zero gaps of lengths five and three between its two components, while the second has two gaps of length three. Both induced bandwidth-three graphs are therefore disconnected. Neither window individually retrieves this \(f\); monotonicity gives failure at every \(m\le3\).

## Verification

The executable `CHECK.py` requires only Python's standard library and uses integer arithmetic throughout. Run `python CHECK.py` from the extracted package directory. The checked output is

`CHECK_OK prime=1009 order14_root=904 disconnected=560 translation_orbits=42 rank_pairs=1764 lower_minor_checks=8`

The script verifies primality, the exact order of the modular root, the complete enumeration and orbit reduction, every restricted Fourier rank, and the eight nonvanishing minors for the explicit lower witness. The finite computation is **exhaustive** because every possible disconnected support pair is covered by the certified orbit list; it is not a sample from the space of possible signals. The analytic reductions preceding it establish why the exact finite certificate is an all-signal proof.

## Relationship to prior work

Bartusel's 2026 *Uncertainty Principles as a Tool for STFT Phase Retrieval* introduces strong two-window recovery, its connected-support criterion, exponential band windows, and a general sufficient bound \(m>(d-1)/3\) for composite \(d\). At \(d=14\), that bound begins at \(m=5\); the present exact threshold begins at \(m=4\). A published prime-period Floquet-sector theorem proves the threshold \(m=4\) for translation-eigenvalue **subspaces** of \(\mathbb C^{14}\), with arbitrary competing signals, but does not treat all vectors in the full space. A published full-spark classification of order-fourteen Fourier row subsets addresses maximal minors for fixed row sets; it does not directly establish full rank for **every** pair of disconnected supports used here. The 42-by-42 restriction test settles those cross-support conditions directly.

## Limitations

This theorem concerns exact noiseless full STFT magnitude arrays, the fourteen-point cyclic group, and the specified exponential windows for \(0\le m\le6\). It does not establish noise stability, a formula at arbitrary composite lengths, or a universal claim for general window weights. The finite rank certificate is reproducible but not an independent mathematical audit. Publication-priority searches may miss equivalent prior formulations in sparse Fourier interpolation.

## References

1. D. Bartusel, *Uncertainty Principles as a Tool for STFT Phase Retrieval*, arXiv:2605.31507, first public May 29, 2026; especially Theorem 2.4, Lemma 2.5, Theorem 2.6, Remark 2.7, and Example 2.9.
2. *Sharp strong two-window STFT thresholds in prime-period Floquet sectors*, publicly available mathematical result, October 18, 2026, identifier `000a2ee07250`.
3. *Complete full-spark classification for row subsets of the order-14 Fourier matrix*, publicly available mathematical result, October 4, 2026, identifier `be518195ffd5`.
4. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286 (background only; the finite proof here does not assume its theorem).
