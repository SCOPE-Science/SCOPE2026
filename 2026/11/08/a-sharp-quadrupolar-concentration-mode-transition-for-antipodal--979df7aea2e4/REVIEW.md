# Scientific review: antipodal-cap quadrupolar concentration

## Correctness — PASS

The concentration operator is diagonal on the three transverse-orthogonal quadratic sectors, whose dimensions sum to the full space dimension. Normalized spherical second/fourth moments and conditional transverse moments reconstruct all eigenvalues; the two boundary-antiderivative identities establish strict eigenvalue ordering and the unique crossing at \(a=1/\sqrt d\). Both cap and complement contain nonempty open sets, ensuring all eigenvalues are strictly between zero and one. The included independent moment-integral checker makes 420 successful assertions. Finite computations are checks, not the proof.

## Originality — PASS (provisional historical priority)

The closest material is Simons and Dahlen (2006), which already treats the same double-polar-cap geometry, derives general fixed-order concentration matrices on the **ordinary two-sphere**, and develops a commuting-operator method for complete low-pass bands. The present claim does not repeat those general algorithms: it treats pure degree-two harmonics in all higher sphere dimensions, gives exactly three eigenvalue branches and derives a closed universal RMS-coordinate crossing that switches the *global* maximizing symmetry sector. Formula (66) of the 2006 article does in principle generate the ambient three-dimensional special case, so no claim of first introducing the cap problem or that special matrix is made. Michel, Plattner, and Seibert (2021) and Roddy and McEwen (2021) provide relevant concentration settings but no corresponding universal dimension-indexed sharp mode classification in the available statements.

Priority risk: a specialized high-dimensional spherical-harmonic or geophysical treatment could already contain the explicit crossing in a different notation. The two contextual 2021 papers were checked at their accessible abstracts, rather than entirely; the most closely matched 2006 article was inspected in its substantive kernel sections and graphical proof pages. No independent historical-priority verification has been performed.

## Mathematical value — PASS

The cap family is the natural axisymmetric model of antipodal observation gaps. The precise crossing \(a=1/\sqrt d\), dimensional jump of the optimal eigenspace from \(d-1\) to one, exact degeneracy at equality and explicit *entire* quadrupolar spectral ordering are nontrivial structural features useful in selecting the most observable quadratic mode and calculating sharp continuous restriction conditioning. These are not arbitrary numerical slices or known-table restatements; the transition and all-dimensional comparison are proved by exact boundary-term identities. The result is specific to pure quadrupoles and does not claim higher-band, finite-grid, noisy or non-antipodal results.

## Closest literature and limitations

Simons & Dahlen, *Geophysical Journal International* (2006), DOI `10.1111/j.1365-246X.2006.03065.x`, §§4.2, 5.2. Michel, Plattner & Seibert, arXiv:`2103.14650` (March 26, 2021). Roddy & McEwen, arXiv:`2106.02023` (June 3, 2021). Scientific derivation, reproducibility and exact limitations are in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
