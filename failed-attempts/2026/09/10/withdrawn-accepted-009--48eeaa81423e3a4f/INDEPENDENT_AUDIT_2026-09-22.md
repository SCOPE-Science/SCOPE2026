# Independent audit — Euler–Reynolds helicity-source subsolution
- Record: `2026/09/10/009`
- Audited tree: `778161800ccc6953a7ae69c9ff14bd8d55414e6a`
- Audited branch/commit: `main` / `e96707428e1608ae0287a471173e57e9f975206d`
- Disposition: **FAILED**

## Correctness

**PASS**

- The explicit field U* is divergence-free with curl U*=2U*, giving E*=6*pi^3 and H*=12*pi^3; W=(sin 8z,-cos 8z,0) is divergence-free with curl W=-8W.
- For v0=(1-t/8)U*+(t/8)W, Fourier orthogonality removes U*-W energy/helicity cross terms, so the helicity derivative at t=0 is exactly -H*/4.
- The committed anti-divergence verifier reports Euler-Reynolds residual 2.76e-14, tracelessness 1.39e-17, nonzero stress, and a Fourier-l1 stress upper bound far below E*/8. The displayed anti-divergence identity div(sym grad Delta^-1 P)=P+grad Delta^-1 div P is correct, with pressure absorbing the gradient/trace terms.
- The construction is therefore a valid smooth strict Euler-Reynolds subsolution with the stated initial helicity derivative and generous stress cap.

## Originality

**FAIL**

- The scientific mechanism is a standard Euler-Reynolds anti-divergence lift: prescribe a smooth divergence-free velocity path, compute its Euler defect, and apply a symmetric trace-free anti-divergence operator to realize that defect as Reynolds stress.
- De Lellis-Székelyhidi's Euler-Reynolds framework predates this record by many years, and standard convex-integration literature uses precisely such right inverses of divergence. Choosing one Beltrami mode U*, a second Fourier mode W, and coefficients calibrated to a desired derivative/cap is a parameter specialization of that machinery, not a distinct construction principle.
- The record's 'first helicity-source Euler subsolution' phrasing rests mainly on a search for the exact words/datum. Absence of that exact datum from prior papers does not establish substantive originality when the construction follows mechanically from standard anti-divergence theory.

## Scientific value

**FAIL**

- The output is only an Euler-Reynolds subsolution, not a weak Euler solution or a new convex-integration iteration preserving a helicity profile.
- Because essentially any sufficiently regular divergence-free path can be lifted to an Euler-Reynolds subsolution by standard anti-divergence, the one-time derivative -H*/4 and loose stress cap E*/8 do not isolate a difficult or reusable obstruction/invariant.
- The construction may be a useful worked example or seed, but it does not by itself establish the claimed research-level advance in helicity flexibility.

## Reproducibility and source checks

- Re-derived curl/divergence identities and E*, H* exactly.
- Re-derived the helicity formula and derivative -H*/4 from Fourier orthogonality.
- Inspected the committed verifier source and archived verifier outputs, including the Fourier-l1 stress certificate.
- Checked the algebraic anti-divergence/pressure identity used by the Euler-Reynolds equation.

## Literature comparison

- [Dissipative continuous Euler flows](https://arxiv.org/abs/1202.1751): De Lellis and Székelyhidi use the Euler-Reynolds framework underlying convex integration; the record's stress-lifting mechanism belongs to this established framework.
- [Energy conservation and Onsager's conjecture for the Euler equations](https://arxiv.org/abs/0704.0759): Cheskidov, Constantin, Friedlander and Shvydkoy establish regularity thresholds including helicity conservation; this motivates helicity questions but does not confer novelty on a standard Euler-Reynolds lift.

## Limitations

- The audit rejects originality/value of the research claim while accepting the displayed subsolution's correctness.
- The failed disposition is scientific, not an operational or reproducibility failure.
- The numerical residual is a consistency check; mathematical exactness comes from the finite Fourier identities.
- No claim is made that the standard anti-divergence operator itself is novel.

## Publication decision

The record is scientifically rejected and should be relocated atomically, with its complete existing package preserved, to `failed-attempts/2026/09/10/withdrawn-accepted-009--48eeaa81423e3a4f`. This audit adds evidence and a `FAILED_ATTEMPT.md` marker before relocation. No GitHub change is claimed as already applied.
