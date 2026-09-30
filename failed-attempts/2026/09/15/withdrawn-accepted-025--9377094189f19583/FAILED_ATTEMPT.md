# FAILED ATTEMPT — NOT A VALIDATED FINDING

Source record: `2026/09/15/025`
Independent audit date: 2026-09-29 (UTC)
Task ID: `6e99684776f375147ebec4d4fe9e3a36`
Relocation target: `failed-attempts/2026/09/15/withdrawn-accepted-025--9377094189f19583`

This record did not pass the required three-axis independent audit and must not remain presented as a validated finding.

- Correctness: **PASS** — The structural label U≅T(2^3,1^4) is correct. MSS’s Morita reduction sends the problem to Delta(1^7)⊗Delta(1^3); exterior-power Weyl modules are tilting, their tensor product is tilting, and its indecomposable direct summands are tilting. In the p=3,k=7,j=3 case, Henke’s criterion gives exactly two summands; the simple L(2,1^8) lies in the separate block, so the remaining five-factor block summand U is indecomposable and tilting. Its highest Weyl factor is Delta(2^3,1^4), forcing U to be the unique indecomposable tilting T(2^3,1^4). The record properly does not claim to have determined the unresolved Loewy layers. The Rule-15 computations are consistent with the supplied scripts and do exhibit Weyl modules with more than two factors.
- Originality: **FAIL** — The main identification is a short formal consequence of information already assembled in Muth–Speyer–Sutton. Their paper explicitly singles out Example 5.21 as the p=3,k=7,j=3 difficult case, works through the same Schur-algebra tensor product, and supplies the Morita equivalence, tilting closure, summand count/block information, and the three Weyl factors. Once these published ingredients are put together, naming the remaining indecomposable summand T(2^3,1^4) follows immediately from standard highest-weight uniqueness; it does not require a new theorem or computation. The Rule-15 witness scan is likewise a direct evaluation of the paper’s decomposition criterion.
- Scientific value: **FAIL** — The observation that the unresolved summand carries the tilting-module label is a useful clarification, but it does not resolve the hard part highlighted by MSS—the Loewy/Alperin structure—or determine the missing graded internal structure. The finite Rule-15 scan only demonstrates why one existing stacking proof cannot be copied verbatim. As packaged, these are helpful deductions about an open example rather than a standalone advance of sufficient research value.

See `INDEPENDENT_AUDIT_2026-09-29.md` and `INDEPENDENT_AUDIT_2026-09-29.json` for the complete evidence and limitations.
