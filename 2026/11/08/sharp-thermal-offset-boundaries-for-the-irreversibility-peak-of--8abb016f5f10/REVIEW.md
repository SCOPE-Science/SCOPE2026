# Scientific review: sharp thermal-offset boundaries for harmonic polytropic irreversibility

## Correctness (PASS)

The claim is deliberately limited to the harmonic entropy expression in Fu et al., Eq. (10), and the underdamped duration expression, Eq. (8). The integral representations of the functions \((e^{Lx}-1)/x\) and \((1-e^{-\ell x})/x\) establish differentiability at the endpoints. Strict concavity of the positive logarithm in the duration parametrization proves the reparametrization is monotone. Expansion is handled by a strictly decreasing derivative. In compression, the key global uniqueness step is not a numerical fit: the explicit identity for \(3F''^2-2F'F'''\) proves a necessary auxiliary function is strictly increasing, and therefore the derivative has exactly the asserted crossing pattern. A nondegenerate implicit-function calculation gives both linear endpoint-onset coefficients. The standalone symbolic/numerical diagnostic program passed, but finite samples do not substitute for the analytic proof.

**Correctness risk:** the thermodynamic interpretation is limited by the original harmonic derivation's dynamical assumptions. The duration relation is underdamped only; the overdamped entropy factor may be included without extending that duration claim. Neither the checker nor this review independently validates an experimental Langevin process beyond those assumptions.

## Originality (PASS, qualified)

**Closest source:** C. Fu, Y. Lin, S. Su and Y.-H. Ma, arXiv:2602.13765 (first public version February 14, 2026, revised October 21, 2026). Its harmonic Eq. (10) is precisely the input entropy curve, and Eq. (8) supplies the underdamped index-to-duration map. The source already supplies the exact scalar expression and demonstrates a nonmonotone peak for selected small thermal offsets; neither formula nor that example is a new finding. The present result addresses a distinct quantitative question: exactly for which full ranges of endpoint ratio and thermal offset is there an interior peak, whether there can be more than one, what happens at equality, and at what order the peak collides with the slow endpoint. A nontrivial global shape lemma is needed for large compression ratios; merely evaluating the scalar expression at particular parameter values does not provide this classification.

The other inspected literature on harmonically trapped Brownian-engine optimization concerns different control paths and cannot by itself yield the sharp conditions (2)–(3). Targeted published-finding corpus and public-literature searches for aliases, the mismatch threshold, compression/expansion inequalities, and global unimodality returned no claim establishing those thresholds. The closest indexed mathematical-entropy optimization and harmonic-sampler findings concern different objects and do not imply a polytropic-stroke extremum classification. 

**Originality risk:** the published exact entropy function contains all values from which these inequalities can in principle be derived; a reader may consider an unreported but sufficiently straightforward consequence covered. We regard the worldwide sharp phase diagram and rigorous large-ratio uniqueness argument as distinct structural content, rather than a change of notation or a small-parameter expansion. A previously unindexed or inaccessible supplemental/global-extrema analysis could nevertheless dominate this claim. The main relevant formulas and discussion of the primary full-text HTML were materially inspected; the full supplemental derivations were not independently recovered.

## Value (PASS)

A strong temperature mismatch can destroy the most-irreversible intermediate-duration protocol reported for weak mismatch, which changes whether a protocol designer should search for an interior maximum at all. The inequalities give two physically meaningful control boundaries directly in measurable quantities, distinguish compression from expansion, settle uniqueness even at very large compression ratios, and specify the linear critical onset. They are a complete shape classification of the natural fixed-endpoint harmonic steering family, not an arbitrary numerical slice. The finite maximum duration at nonzero fixed offset also prevents conflating the slow-index endpoint with an unlimited quasistatic time limit.

**Value risk:** practical physical realization additionally requires the original timescale separation and controllable initial offsets; no performance theorem for general protocols or anharmonic traps follows.

## Evidence and limitations

Primary scientific source: arXiv:2602.13765v2 HTML (harmonic equations (6)–(10), discussion of observed peaks); earliest public version arXiv:2602.13765v1 dated 2026-02-14. Contextual comparison: Prieto-Rodríguez, Prados and Plata, *Entropy* 27 (2025), 72. Actual mathematical checks are documented in `VERIFICATION.md` and the self-contained `verify.py`. Claims not proved: an extremum criterion for arbitrary physical driving schedules; an overdamped time-index relation; full experimental applicability; independent novelty certification.

Self-review: passed. Independent audit: not yet performed.
