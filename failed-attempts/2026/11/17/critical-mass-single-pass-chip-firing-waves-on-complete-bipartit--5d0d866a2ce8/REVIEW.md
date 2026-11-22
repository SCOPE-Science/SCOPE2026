# Independent mathematical audit

## correctness

PASS

For periodic mass |E|=mn and exactly one firing per vertex, a vertex scheduled at time tau(v) has x(v)>=deg(v)-number of neighbors fired earlier. Summing inequalities over v, any simultaneously-firing edge would force mass>|E|, impossible; equality gives x(v)=number of neighbors firing later. With no empty round and all firing rounds independent, every round lies within one shore and adjacent cyclic rounds must alternate, since a later vertex from the same shore could already fire earlier. Thus least period must be 2k with 1<=k<=min(m,n). Conversely arbitrary two ordered partitions into k nonempty blocks with one of two starting shores produce a unique valid initial chip vector, and the exact one-fire property prevents shorter period. Count gives 2(k!)^2 S(m,k)S(n,k) and divide by 2k for temporal orbits. Independently enumerated *every* nonnegative critical-mass configuration for K_(1,1), K_(1,3), K_(2,2), K_(2,3), K_(3,3) via distinct deterministic state-iteration code, matching counts (2); (2); (2,8); (2,24); (2,72,72) respectively. General formula established by the combinatorial bijection, not these finite checks.

## originality

FAIL

Decisive implication by another publicly indexed theorem: the same-day published Resultary work "Exact single-pass orbit census and sharp period interval on complete multipartite chip-firing graphs" proves in its Step 1 a phase-assignment bijection for *any* finite connected simple graph at precisely mass |E| and one firing per vertex, using exactly x(v)=deg(v)-number of earlier-firing neighbors and predecessor-phase condition. Its Step 2 counts proper cyclic part words with ordered Stirling partitions on complete multipartite graphs. Although its displayed main formula assumes >=3 parts, specializing its already-proved general phase lemma to two parts forces an alternating binary cyclic word and immediately yields 2(k!)^2 S(m,k)S(n,k), precisely this complete result. Thus the latter is a direct routine corollary and does not pass originality in the compared published corpus. Both works share a bulk 2026-11-17 reconciliation commit, so chronological priority within that day was not established; the statement-level coverage, not an unverified temporal ordering, is decisive.

## value

FAIL

Exact critical-mass orbit census on K_(m,n) is a natural invariant, and its proof is correct. However in the available mathematical record the complete formula is mechanically the two-letter specialization of an already established all-graph phase bijection and complete-multipartite Stirling enumeration. No additional non-implied structural invariant, unexpected cutoff, or independently useful unknown fact survives beyond that corollary. The period-six 72 configurations are an instance of that same covered expression; finite reproducibility alone does not add independent mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
