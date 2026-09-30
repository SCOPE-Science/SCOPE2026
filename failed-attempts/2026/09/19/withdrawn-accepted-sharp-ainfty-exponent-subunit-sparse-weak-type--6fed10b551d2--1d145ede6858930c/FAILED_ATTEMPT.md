# FAILED ATTEMPT — NOT A VALIDATED FINDING

Record: `2026/09/19/sharp-ainfty-exponent-subunit-sparse-weak-type--6fed10b551d2`  
Independent audit date: 2026-09-29 (UTC)  
Task: `42d1941178e9cb8d8735bd4ae0dff0c8`

The underlying mathematics was independently checked and is valid, but the record is not acceptable as a distinct validated research finding because its principal theorem was already present in earlier SCOPE repository work.

## Correctness retained

The nested dyadic construction is correct. With e_m=1-2^{-m}, the dyadic maximal function of omega_m=1+(2^m-1)1_{I_m} equals 1+e_m2^j on I_j\I_{j+1} and 2^m on I_m, giving the stated exact L1(v_m) norm. The Fujii--Wilson ratio over every possible dyadic interval reduces to the displayed ancestor formula, hence [omega_m]_{A_infinity} is comparable with m. For f=1_{I_0}, the sparse output is (m+1)^{1/r} on I_m while omega_m(I_m)=1, so division by the exact input norm gives the claimed m^{1/r-1} weak lower bound. Edge cases m>=2 and strict-superlevel conventions do not alter the conclusion.

## Decisive prior-art issue

A substantively identical SCOPE theorem predates the assigned record by more than a day. `2026/09/18/sharp-ainfty-endpoint-power-sparse-operators--ef01896cc9bb`, committed on 2026-09-18 at 08:47--08:50 UTC, already fixes the mixed A1 characteristic at 1 with v=M_D omega on the same nested dyadic chain, proves [omega]_{A_infinity} comparable with the chain length, and obtains the same weak L1 lower growth N^{1/r-1}, hence the same optimality statement for the A_infinity exponent. The assigned record was first committed on 2026-09-19 at 10:20:40 UTC. Its slightly different spike normalization and sharper exact constants do not create a distinct scientific theorem.

## Scientific-value consequence

The mathematics is valid and the exact maximal-function profile is clean, but as a separate validated finding it adds only normalization-level refinements to an earlier repository theorem with the same construction, obstruction mechanism, and headline optimality conclusion. It therefore lacks sufficient standalone scientific value for the validated inventory.

## Consequence

This package is relocated as a failed research attempt rather than silently deleted. It may remain useful as an alternative exposition or verification example, but its headline must not be represented as an independently original validated finding.

## Prior repository evidence

- `2026/09/18/sharp-ainfty-endpoint-power-sparse-operators--ef01896cc9bb/RESULT.md` (blob `0feb3429d1368d3645b27c8dcc456ab6b863c0ad`): Earlier theorem with the same nested-dyadic v=M_D omega construction, [omega,v]_{A1}=1, A_infinity growth comparable with N, and weak norm lower bound of order N^{1/r-1}.
