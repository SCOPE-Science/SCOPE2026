# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Bilinearized Strictness Gap on a Named 6_3 Pair: DISPROOF (Target resolved negatively)

## Claim (negative resolution of target_claim)
No Legendrian fronts G1, G2 of smooth type 6_3 with tb=-1 and r=0 exist, so the
target's claimed rank-2-versus-rank-0 bilinearized gap is vacuous: the premise
is impossible. The target is thereby **disproved** (not merely blocked).

## Proof
1. **MFW bound (theorem).** For any Legendrian knot L in standard contact R^3,
   tb(L) + |rot(L)| <= mindeg_v P_L(v,z) - 1, where P_L is the HOMFLY-PT
   polynomial (Morton–Franks–Williams; Fuchs–Tabachnikov form). Calibrated in
   `output/artifacts/skein.py` + `verify_mfw.py`: the engine reproduces
   P(unknot) = 1, P(kink+) = P(kink-) = 1, P(trefoil closure s1^3) =
   2v^2 - v^4 + v^2 z^2, and P(figure-8) = v^{-2} - 1 - z^2 + v^2, all classical.
2. **HOMFLY-PT of 6_3 (independently recomputed).** From the braid
   BR[3, {-1,-1,2,-1,2,2}] (katlas entry for 6_3), the terminating Conway skein
   recursion in `skein.py` computes
   P(6_3) = -v^{-2} - v^{-2} z^2 + 3 + 3 z^2 + z^4 - v^2 - v^2 z^2,
   matching the katlas HOMFLY-PT value term-for-term
   (3 - a^2 - a^{-2} + 3z^2 - a^2 z^2 - a^{-2} z^2 + z^4). Hence
   mindeg_v P = -2 and **tb + |rot| <= -3** for every Legendrian 6_3.
   The polynomial is symmetric in v <-> v^{-1}, so the same bound holds for the
   mirror; both orientations are covered.
3. **Contradiction.** The target requires tb = -1, r = 0, i.e. tb + |rot| = -1,
   exceeding the bound by 2. No such fronts exist; the ordered augmentation
   pairs and their bilinearized ranks cannot exist as specified.
4. **Corroboration.** The Ng atlas max-tb representatives of 6_3 (K6_3.0,
   K6_3.1) have tb = -4, rot = 1 (sum -3, sharp for the bound), verified in
   `verify_63atlas.py`. They admit no Z-graded augmentations; their ungraded
   (mod-1) linearized data coincide ('4*t^0', 384 augmentations each) and their
   ordered-pair bilinearized distributions are IDENTICAL
   (dim 4 x 49152, dim 2 x 98304), so no nearby reading of the claim survives.

## Evidence summary
- `output/artifacts/skein.py`: terminating skein-tree HOMFLY-PT engine (stdlib
  only) with descending-diagram induction (measure: crossings, then bad
  crossings); validated on unknot/kinks/trefoil/figure-8.
- `output/artifacts/verify_mfw.py`: prints VERIFY_OK; certifies all
  calibrations plus term-for-term agreement of recomputed P(6_3) with katlas.
- `output/artifacts/verify_63atlas.py`: prints VERIFY_OK; certifies atlas
  6_3 data (tb/rot, augmentation counts, identical bilinearized distributions).

## Limitations / uncertainty
- The MFW inequality itself is cited as a published theorem (Morton–Franks–
  Williams; see Fuchs–Tabachnikov exposition), not re-proved here; everything
  downstream (polynomial, degrees, atlas data) is recomputed in-repo.
- The disproof kills the target as stated; it does not classify which nearby
  Legendrian pairs (other smooth types or tb/rot) admit bilinearized gaps.

## Route: TARGET (negative resolution — rigorous impossibility proof)
