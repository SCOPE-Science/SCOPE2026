# Mathematical review

## Correctness — PASS

The object is the unnormalized, real symmetric signed-intersection matrix on all \(k\)-subsets. The complete harmonic multiplicities come from the established Johnson-slice basis, and the action on each degree is reconstructed by summing over distinguished pairs. The resulting exact coefficient extraction is evaluated for offsets zero, one, and two. Monotonicity comparisons identify both extreme absolute eigenvalues; standard central-binomial and Catalan asymptotics then yield the precise condition-number constants. Direct numerical spectra of all twelve matrices at \(1\le k\le4\) agree with the complete predicted lists, and 447 larger arithmetic parameter checks agree with the coefficient forms. These finite checks support but do not substitute for the proof.

## Originality — PASS, bounded

The closest primary theory (Filmus, arXiv:1406.0142, sections 2 and 5) supplies the complete Johnson harmonic eigenspaces for all intersection kernels, and Podestá (arXiv:1603.09156, sections 2, 5 and 6) develops Krawtchouk/Catalan coefficient identities. These mathematical ingredients are acknowledged and are not claimed as new. Neither inspected presentation identifies the three consecutive near-central principal Walsh matrices' exact rank/invertibility threshold together with their sharp, contrasting \(\sqrt k\) versus \(k^{3/2}\) conditioning law and extremal sectors. Related Fourier *band-to-shell* restriction results use a different rectangular or concentration operator, so their rank laws do not imply this fixed-shell *square compression*. Search did not establish global historical uniqueness: a specialized Johnson association-scheme spectral result or an unstated consequence of a general eigenvalue theorem remains a realistic priority risk.

## Mathematical value — PASS

The matrix is the exact finite Fourier sampling/reconstruction map when both samples and Fourier coefficients are limited to one constant-weight slice. Its sharp rank and condition number distinguish recoverability from noise amplification. The one-coordinate restoration of invertibility immediately followed by a factor of order \(k\) increase in conditioning is a genuine structural boundary for the natural three consecutive ambient dimensions; the Catalan identity locates the worst harmonic mode exactly. It is not an isolated numerical slice or a claim to rediscover Johnson harmonic eigenvectors.

## Verification limits

No independent mathematical audit has been performed. The proof assumes the standard Johnson harmonic decomposition, explicitly cited and proved in the literature. The optional numerical checker uses NumPy and covers only finite dimensions; the symbolic identities and extremal inequalities are given separately in the proof. No statement extends to a moving gap \(n-2k\), and the literature check cannot rule out all stronger pre-existing theorems.

Self-review: passed. Independent audit: not yet performed.
