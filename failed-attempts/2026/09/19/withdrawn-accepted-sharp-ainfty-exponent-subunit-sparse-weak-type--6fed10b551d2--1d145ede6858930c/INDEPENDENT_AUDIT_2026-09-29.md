# Independent audit — Sharp A_infinity growth at the weak L1 endpoint for subunit sparse powers

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/sharp-ainfty-exponent-subunit-sparse-weak-type--6fed10b551d2`  
**Audited tree:** `3b85af15fdc6bf4f7f3340f9954197707134c27f`

## Disposition

**FAILED.** The mathematics is correct, but originality and standalone scientific value fail because decisive earlier repository coverage already contains the same theorem. The record should be relocated to its assigned failed-attempt path.

## Correctness

**PASS.** The nested dyadic construction is correct. With e_m=1-2^{-m}, the dyadic maximal function of omega_m=1+(2^m-1)1_{I_m} equals 1+e_m2^j on I_j\I_{j+1} and 2^m on I_m, giving the stated exact L1(v_m) norm. The Fujii--Wilson ratio over every possible dyadic interval reduces to the displayed ancestor formula, hence [omega_m]_{A_infinity} is comparable with m. For f=1_{I_0}, the sparse output is (m+1)^{1/r} on I_m while omega_m(I_m)=1, so division by the exact input norm gives the claimed m^{1/r-1} weak lower bound. Edge cases m>=2 and strict-superlevel conventions do not alter the conclusion.

## Originality

**FAIL.** A substantively identical SCOPE theorem predates the assigned record by more than a day. `2026/09/18/sharp-ainfty-endpoint-power-sparse-operators--ef01896cc9bb`, committed on 2026-09-18 at 08:47--08:50 UTC, already fixes the mixed A1 characteristic at 1 with v=M_D omega on the same nested dyadic chain, proves [omega]_{A_infinity} comparable with the chain length, and obtains the same weak L1 lower growth N^{1/r-1}, hence the same optimality statement for the A_infinity exponent. The assigned record was first committed on 2026-09-19 at 10:20:40 UTC. Its slightly different spike normalization and sharper exact constants do not create a distinct scientific theorem.

## Scientific value

**FAIL.** The mathematics is valid and the exact maximal-function profile is clean, but as a separate validated finding it adds only normalization-level refinements to an earlier repository theorem with the same construction, obstruction mechanism, and headline optimality conclusion. It therefore lacks sufficient standalone scientific value for the validated inventory.

## Independent checks

- Recomputed the piecewise dyadic maximal-function profile and the exact input L1(v_m) norm.
- Enumerated the possible dyadic intervals in the Fujii--Wilson supremum and rederived the ancestor formula and m-comparability.
- Recomputed the weak-level lower bound on the smallest interval, including the strict-superlevel convention.
- Compared the theorem and construction against the earlier 2026-09-18 SCOPE record and verified repository commit chronology.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.20531 — Gonçalves--Lorist, Sharp mixed A_p-A_infinity estimates for sparse operators on filtered and nonhomogeneous measure spaces; public arXiv abstract confirms the very recent endpoint weighted setting.
- https://arxiv.org/abs/2409.08921 — Nieraeth--Stockdale, Endpoint weak-type bounds beyond Calderón--Zygmund theory; endpoint context cited by the record.

- `2026/09/18/sharp-ainfty-endpoint-power-sparse-operators--ef01896cc9bb/RESULT.md` (blob `0feb3429d1368d3645b27c8dcc456ab6b863c0ad`) — Earlier theorem with the same nested-dyadic v=M_D omega construction, [omega,v]_{A1}=1, A_infinity growth comparable with N, and weak norm lower bound of order N^{1/r-1}.

## Limitations

- The failure is on originality and standalone scientific value, not mathematical correctness.
- The external Gonçalves--Lorist paper is extremely recent, but external-priority uncertainty is not needed for this disposition because the earlier SCOPE duplicate is decisive.
