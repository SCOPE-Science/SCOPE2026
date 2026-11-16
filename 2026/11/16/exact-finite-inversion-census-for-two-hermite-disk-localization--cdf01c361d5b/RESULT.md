# Exact finite inversion census for two-Hermite disk localization

## Finding

For a disk in the time–frequency plane and two independent Gaussian and first-Hermite spectrogram channels, an arbitrarily small positive Gaussian channel eliminates all but finitely many of the infinitely recurring pure first-Hermite spectral-order reversals. More precisely, for the compact positive operator \(T_{\rho,s}\) defined below, the Hermite basis diagonalizes \(T_{\rho,s}\). Its eigenvalues \(\lambda_k(\rho,s)\), indexed by \(k=0,1,\ldots\), obey the **exact adjacent-gap identity**

\[
\lambda_k(\rho,s)-\lambda_{k+1}(\rho,s)
=\frac{e^{-s}s^k}{(k+1)!}\bigl[(s-k)(s-k-1)+\rho s\bigr].
\]

For \(\rho\ge1\), all these gaps are strictly positive at every disk area \(s>0\); the universal threshold \(1\) is sharp. For \(0<\rho<1\), define \(H_\rho=(1-\rho)^2/(4\rho)\). The exact number of distinct Hermite indices \(k\) that exhibit a strict adjacent-order reversal for some disk area is

\[
N(\rho)=\lceil H_\rho\rceil.
\]

In particular, \(N(\rho)\sim 1/(4\rho)\) as \(\rho\downarrow0\), while for the pure first-Hermite channel \(\rho=0\) every index reverses. For each \(k\ge1\), a strict reversal occurs precisely when \(0<\rho<\rho_k\), where

\[
\rho_k=(\sqrt{k+1}-\sqrt{k})^2,
\qquad
s\in\bigl(s_{k,-}(\rho),s_{k,+}(\rho)\bigr),
\]

\[
s_{k,\pm}(\rho)=\frac{2k+1-\rho\pm\sqrt{(1-\rho)^2-4k\rho}}2.
\]

At \(\rho=\rho_k\), the two consecutive eigenvalues touch once at \(s=\sqrt{k(k+1)}\) but never reverse. At \(k=0\) there is a reversal exactly when \(0\le\rho<1\) and \(0<s<1-\rho\); for \(\rho<1\) its positive-area equality is at \(s=1-\rho\). At any fixed area there is at most one reversed adjacent pair. For every \(\rho>0\), all integer-area adjacent gaps are strictly positive, so adding any nonzero Gaussian channel destroys the pure first-Hermite integer-area adjacent-gap collisions.

## Assumptions and scope

Work on \(L^2(\mathbb R)\) with normalized Hermite functions \(h_k\), indexed by \(k\ge0\), with \(h_0(t)=2^{1/4}e^{-\pi t^2}\) and \(h_1(t)=2\sqrt\pi\,t h_0(t)\). Define

\[
V_gf(x,\xi)=\int_{\mathbb R}f(t)\overline{g(t-x)}e^{-2\pi i t\xi}\,dt,
\qquad D_s=\{(x,\xi):\pi(x^2+\xi^2)\le s\}.
\]

The disk \(D_s\) has area \(s>0\), and \(\rho\ge0\) is the Gaussian-channel weight relative to the unit first-Hermite-channel weight. The channels are **incoherent** (their squared STFT magnitudes are added), not a single STFT with a superposed window. Define the positive trace-class operator by the quadratic form

\[
\langle T_{\rho,s}f,f\rangle
=\rho\int_{D_s}|V_{h_0}f|^2+\int_{D_s}|V_{h_1}f|^2.
\]

All findings refer to the order of the indexed eigenvalues \(\lambda_k\) versus \(\lambda_{k+1}\), not a claim that every nonadjacent pair is globally ordered. The complete adjacent-order phase diagram includes all real \(\rho\ge0\), \(s>0\), and integer \(k\ge0\).

## Proof

**Diagonalization.** The standard Hermite–STFT Laguerre identity gives, with \(t=\pi(x^2+\xi^2)\), the angular-independent squared magnitudes

\[
|V_{h_0}h_k|^2=e^{-t}\frac{t^k}{k!},
\qquad
|V_{h_1}h_k|^2=\begin{cases}
 t e^{-t},&k=0,\\
 e^{-t}t^{k-1}(k-t)^2/k!,&k\ge1.
\end{cases}
\]

For distinct Hermite indices the cross-STFT products contain a nonconstant angular character, so their integral over the disk vanishes. Thus every \(h_k\) is an eigenvector; the basis is complete. Write

\[
p_k(s)=e^{-s}s^k/k!,\qquad q_k(s)=\int_0^s e^{-t}t^k/k!\,dt.
\]

Integration by parts, including the separate \(k=0\) case, gives

\[
\lambda_k(\rho,s)=(1+\rho)q_k(s)+(k-s)p_k(s),\qquad k\ge0.
\]

**Gap identity.** Because \(q_k-q_{k+1}=p_{k+1}\) and \(p_{k+1}=s p_k/(k+1)\), subtracting consecutive eigenvalues gives precisely

\[
\lambda_k-\lambda_{k+1}
=\frac{p_k(s)}{k+1}\{(s-k)(s-k-1)+\rho s\}.
\]

The prefactor is positive for \(s>0\); hence only the scalar quadratic \(G_{k,\rho}(s)=(s-k)(s-k-1)+\rho s\) determines the sign.

**Complete classification.** If \(s\notin(k,k+1)\) then the product of the two consecutive factors is nonnegative, so \(G_{k,\rho}(s)\ge0\), with equality possible only when \(\rho=0\) and \(s\in\{k,k+1\}\). All open reversal intervals are contained in disjoint unit intervals. For \(k=0\), \(G_{0,\rho}(s)=s(s+\rho-1)\). For \(k\ge1\), the quadratic has constant term \(k(k+1)\) and linear coefficient \(\rho-2k-1\). It dips below zero for some \(s>0\) exactly when its discriminant \((1-\rho)^2-4k\rho\) is positive and its vertex lies in \((k,k+1)\). Equivalently \(\rho<(\sqrt{k+1}-\sqrt{k})^2\); at equality its unique zero is \(\sqrt{k(k+1)}\) and otherwise its two roots are \(s_{k,\pm}(\rho)\) as claimed. For positive \(\rho<1\) the reversal indices are \(k=0\) and all positive integers with \(k<H_\rho\); their number is \(\lceil H_\rho\rceil\). For \(\rho\ge1\), every gap is positive at every positive area. Sharpness follows from the \(k=0\) gap for every \(\rho<1\). The asymptotic count follows by expansion of \(H_\rho\).

At a positive integer area, \((s-k)(s-k-1)\ge0\) for all integer \(k\), and \(\rho s>0\) when \(\rho>0\). At \(\rho=0\), consecutive adjacent gaps vanish at \(s=k\) and \(s=k+1\); at positive integer areas these produce the familiar neighboring triple equality. These observations prove every asserted boundary case.

## Verification

The standalone script `check_mixed_disk.py` uses an independent numerical quadrature of the first-Hermite radial density to compare the spectral formula and gap identity for many areas, weights and indices, and symbolically checks the quadratic discriminant. It completed **3,081 checks** successfully (Python with `mpmath` and `sympy`). These finite checks are corroboration; the all-index and all-area statements rest on the exact proof above. Moreover, the trace identity \(\sum_{k\ge0}\lambda_k=(1+\rho)s\) follows from the STFT isometry and provides an independent normalization test.

## Relationship to prior work

Daubechies' Gaussian-window disk localization yields the Gaussian eigenvalues and Hermite basis. Hermite-window disk eigenvalue integrals, and their mixed-state extension, appear in Svela's October 24, 2024 preprint, particularly the Laguerre–STFT identity and Proposition 6.7 (infinite-dimensional diagonalization). The complete **mixed** adjacent-gap sign classification above is not a new diagonalization theorem; it is an exact parameter-dependent order classification derived from those spectral inputs.

Alaifari and Yang's October 7, 2024 multiwindow STFT study motivates independent Gaussian and Hermite channels, but addresses stable phase retrieval and ambiguity-function zeros rather than this disk-area phase diagram. Previously published pure first-Hermite disk localization results already describe the integer-area triple coincidences; this finding describes precisely how adding a strictly positive Gaussian channel removes all those coincidences and how many isolated reversal intervals remain. A specialized prior classification of the same two-channel eigenvalue order, if it exists under different terminology, would supersede the priority claim.

## Limitations

This is a theorem about **two incoherently combined, independently measured Hermite windows** and **centered circular masks**. It does not concern coherent window superpositions, arbitrary domains, weighted disk shapes, nonadjacent eigenvalue-order comparisons, noise-optimal channel allocation, or phase-retrieval guarantees. General mixed-state spectral formulas in prior literature supply the diagonalization and integral starting point. Historical novelty of the sharp adjacent-order classification is provisional; independent review has not occurred.

## References

1. I. Daubechies, *Time–Frequency Localization Operators: A Geometric Phase Space Approach*, IEEE Transactions on Information Theory 34 (1988), 605–612.
2. E. A. T. Svela, *Extensions of Daubechies' theorem: Reinhardt domains, Hagedorn wavepackets and mixed-state localization operators*, arXiv:2410.18769, first posted 2024-10-24. In particular §§3.3 and 6.
3. R. Alaifari and Y. Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval*, arXiv:2410.05486, first posted 2024-10-07.
4. H. Knutsen, *Daubechies' Time–Frequency Localization Operator on Cantor Type Sets I*, J. Fourier Anal. Appl. 26 (2020), article 47. DOI:10.1007/s00041-020-09751-9.
