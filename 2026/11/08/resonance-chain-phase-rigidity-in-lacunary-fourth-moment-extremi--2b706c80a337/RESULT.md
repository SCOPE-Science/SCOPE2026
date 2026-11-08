# Resonance-chain phase rigidity in lacunary fourth-moment extremizers

## Finding

Write \(\mathbb T=\{z\in\mathbb C:|z|=1\}\) with probability Haar measure. For integers \(m\ge1\) and \(q\ge2\), set
\[
D_{q,m}=\{0,1,q,q^2,\ldots,q^{m-1}\},\qquad
P_c(z)=c_0+\sum_{j=1}^{m}c_jz^{q^{j-1}},
\]
and define the fourth-power sharp synthesis constant
\[
K_{q,m}=\max_{c\ne0}\frac{\int_{\mathbb T}|P_c(z)|^4\,dm(z)}{(\sum_{j=0}^{m}|c_j|^2)^2}.
\]
The following complete phase-and-support dichotomy holds.

**Dyadic case.** For every \(m\ge2\), every extremizer for \(K_{2,m}\) has *all* \(m+1\) coefficients nonzero. There are real \(\gamma,\theta\) such that
\[
\frac{c_j}{|c_j|}=e^{i(\gamma+2^{j-1}\theta)}\quad(1\le j\le m),
\qquad \frac{c_0}{|c_0|}=e^{i\gamma}.
\]
Conversely, applying these two phase symmetries to any nonnegative maximizing magnitude vector preserves extremality. The sharp fourth-power constants are strictly increasing:
\[
K_{2,1}=\frac32,\qquad K_{2,2}=\frac{15}{7},\qquad
K_{2,m+1}>K_{2,m}\quad(m\ge1).
\]
In particular no maximizer for a longer dyadic set is supported on a proper subset, and for \(m\ge2\) the fourth-power constant is strictly larger than \(2-1/(m+1)\).

**Higher integer lacunarity.** For every \(q\ge3\) and \(m\ge1\),
\[
K_{q,m}=2-\frac1{m+1}.
\]
Equality holds precisely when all \(m+1\) coefficient magnitudes are equal; their phases are arbitrary. Hence the resonances peculiar to the dyadic base are exactly what convert an unrestricted phase torus into a character-phase two-torus for every length \(m\ge2\).

## Assumptions and scope

The coefficients are unrestricted complex numbers, the underlying Fourier characters have infinite order on the continuous unit circle, and all norms use normalized Haar measure. There is no additional symmetry, sparsity, positivity or finite-grid sampling hypothesis. The theorem is an all-length statement; it does not give a closed expression for the dyadic sharp magnitude profile or the constants \(K_{2,m}\) when \(m\ge3\). The statement about phases classifies the phase *fibers* of maximizers, not the number of distinct maximizing nonnegative magnitude vectors.

## Proof

**1. Exact fourth-moment identity.** For any finite spectrum \(D\), convolution of the coefficient vector with itself gives
\[
\int_{\mathbb T}|P_c|^4\,dm
=\sum_{s\in D+D}\left|\sum_{d+e=s}c_dc_e\right|^2.
\]
The baseline in which all unordered pair sums are different is
\[
2\left(\sum_{d\in D}|c_d|^2\right)^2-\sum_{d\in D}|c_d|^4.
\]
For the dyadic spectrum, uniqueness of binary expansion shows that *the only* repeated unordered pair sums are
\[
0+2^{j-1}=2^{j-2}+2^{j-2}\qquad (2\le j\le m).
\]
Consequently, with \(S=\sum_{j=0}^{m}|c_j|^2\),
\[
\int_{\mathbb T}|P_c|^4\,dm
=2S^2-\sum_{j=0}^{m}|c_j|^4
+4\sum_{j=2}^{m}\operatorname{Re}(c_0c_j\overline{c_{j-1}}^{\,2}). \tag{1}
\]
For \(q\ge3\) there are no repeated unordered pair sums at all, since two base-\(q\) digits never generate a carry. Thus the last summation is absent. The resulting baseline is maximized for fixed \(S\) exactly by equal coefficient magnitudes, by Cauchy–Schwarz, giving the formula and free-phase equality class for \(q\ge3\).

**2. Positivity reduction and compression.** Put \(a_j=|c_j|\). Formula (1) implies the upper bound
\[
\mathcal F_m(a)=2\left(\sum a_j^2\right)^2-\sum a_j^4
+4a_0\sum_{j=1}^{m-1}a_j^2a_{j+1}, \tag{2}
\]
with equality if and only if all active resonant phases align. In particular a nonnegative coefficient vector attains the maximum for any prescribed magnitudes.

For a nonnegative vector having \(a_0>0\) but only \(r\le m\) nonzero entries, compress the occupied positive dyadic exponents in increasing order to \(1,2,\ldots,2^{r-2}\), without changing the magnitudes. Every resonant adjacency in the old set remains an adjacency in the compressed set, while additional nonnegative interactions may appear. The baseline is unchanged. Its fourth moment cannot decrease, so the original value is at most \(K_{2,r-1}\). If instead \(a_0=0\), the remaining powers of two form a Sidon set for pair sums; with \(r\) active entries its fourth-power ratio is at most \(2-1/r<2\) for \(r\ge1\).

**3. Strict growth and full support by induction.** For \(m=1\), the spectrum is \(\{0,1\}\); its sharp fourth-power ratio is \(3/2\) and all maximizing vectors have two nonzero entries. For any nonnegative, normalized full-support maximizer at length \(m\), append a new coefficient \(\varepsilon>0\) at frequency \(2^m\). The numerator changes by
\[
4a_0a_m^2\varepsilon+O(\varepsilon^2),
\]
while the squared coefficient norm changes only by \(O(\varepsilon^2)\). Since \(a_0a_m>0\), this gives \(K_{2,m+1}>K_{2,m}\).

At length two, setting the squared sum of the endpoint magnitudes equal to \(s\) and symmetrizing them gives the sharp upper bound
\[
\mathcal F_2\le1+4s-\frac72s^2\le\frac{15}{7}
\]
for \(S=1\), with equality for squared magnitudes \((2/7,3/7,2/7)\). Thus \(K_{2,2}=15/7>2\).

Now suppose all length-\(m\) maximizing vectors have full support. The appended-vector argument establishes strict growth. A length-\(m+1\) maximizing vector with a zero and a nonzero constant coefficient would, by compression, have ratio at most \(K_{2,m}\), a contradiction. One with zero constant coefficient has ratio below \(2\), also less than \(K_{2,m+1}\) (for the base \(m=1\) transition use the two-positive-frequency bound \(3/2=K_{2,1}\)). This proves full support and strict growth for all lengths.

**4. Phase rigidity.** At a maximizing vector all coefficients are nonzero. Since replacing the coefficients by their magnitudes cannot decrease the fourth moment, equality must hold term-by-term in (1). Therefore for \(2\le j\le m\),
\[
2\arg c_{j-1}\equiv\arg c_0+\arg c_j\pmod{2\pi}.
\]
Writing \(\gamma=\arg c_0\), \(\theta=\arg c_1-\gamma\), induction yields \(\arg c_j\equiv\gamma+2^{j-1}\theta\pmod{2\pi}\). These are exactly the phases induced by a scalar multiplication and rotation of the argument \(z\). They clearly preserve the fourth moment, proving both directions of the phase-fiber description.

## Verification

The accompanying standalone script `check_dyadic_fourth.py` enumerates all unordered pair-sum collisions for \(1\le m\le10\), verifies the dyadic collision chain and the absence of collisions for integer bases three through seven, and compares the convolution calculation of fourth moments with (1) and the Sidon baseline on reproducible complex-integer coefficient examples. It additionally checks the exact base case \(K_{2,2}=15/7\). Execution returns `EXACT_MOMENT_CHECKS_PASS 1297`. The script is finite diagnostic evidence; the unrestricted all-length theorem follows from the proof above.

## Relationship to prior work

Ciccone and Gonçalves (arXiv:2208.09441, first posted August 19, 2022) study Fourier extension from the geometric circle under additive restrictions including lacunary \(P(3)\)-sets. Their discussion explicitly distinguishes the ratio-two lacunary case from their sparse regime. Their extension operator maps circle functions into \(L^6(\mathbb R^2)\), unlike the present one-dimensional coefficient-synthesis \(\ell^2\to L^4(\mathbb T)\) problem. Dyakonov (arXiv:2005.08885, first posted May 18, 2020) characterizes extreme and exposed points of lacunary polynomial \(L^1\) balls, not the fourth-moment maximizing phase and support structure here.

A published full-text result on the four-character spectrum \(\{0,1,2,4\}\) already gives its exact fourth-power constant and a rigid phase family; that four-character case is **not claimed as new**. The present scope is the proof of full support, strict growth and phase rigidity for *all larger dyadic truncations*, alongside the exact change at lacunarity base three. Full-text comparison with this four-mode precedent and separate literature searches did not identify an all-length theorem implying these conclusions. The search is not proof of historical priority, and a general additive-resonance extremizer theorem may still contain a stronger result.

## Limitations

For dyadic length \(m\ge3\), the maximizing magnitude vector and its sharp constant have not been determined in closed form; neither magnitude-profile uniqueness nor numerical stability of near-maximizers is claimed. The theorem concerns continuous-circle Haar integration, not finite cyclic grids with aliasing. The closest four-mode published result was read in full alongside relevant primary literature; historical priority remains at risk from more general resonance-graph extremizer theorems.

## References

- Valentina Ciccone and Felipe Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441 (first posted 2022-08-19), https://arxiv.org/abs/2208.09441 .
- Konstantin M. Dyakonov, *Lacunary polynomials in \(L^1\): geometry of the unit sphere*, arXiv:2005.08885 (first posted 2020-05-18), https://arxiv.org/abs/2005.08885 .
- *Sharp fourth moments for linked-midpoint four-character spectra*, published research record ID `2026/10/11/SCOPE-sharp-fourth-moments-for-linked-midpoint-four-character-spectra--0b57c5d24021` (four-character precedent; no attribution of its result to this work).
