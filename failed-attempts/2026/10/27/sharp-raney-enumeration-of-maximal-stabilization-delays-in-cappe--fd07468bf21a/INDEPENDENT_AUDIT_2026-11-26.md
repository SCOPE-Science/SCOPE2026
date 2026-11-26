# Independent mathematical audit

## correctness

PASS

With cumulative service m_i(t), conservation gives g_i(t)=g_i(0)+m_{i+1}(t)-m_i(t). Thus m_i(t+1)=min(m_i(t)+c,g_i(0)+m_{i+1}(t)). Induction gives lost service ct-m_i(t) as the maximum prefix deficit over lengths 0..t, and a full circuit has nonpositive deficit when H≥ck. Hence lost service ceases growing after time k−1, equivalent to every site being at or above capacity. Conversely a fixed point has all outgoing services equal; under H≥ck their common value is c. Attainment of τ=k−1 requires a strictly new deficit record at length k−1 at some i; subtracting all shorter prefixes gives exactly the strict backward partial-sum inequalities at the omitted site j. Two omitted sites cannot work since the strict inequalities for the complementary arcs would imply H<ck. In one event each backward word of length L=k−1 satisfying sum_{i≤s} a_i<cs leaves a uniquely determined inventory H−sum a_i≥c+1. In preorder with c initial root slots and c+1 slots added per internal vertex, immediately before the s-th internal vertex there are cs−sum_{i≤s}a_i slots; strict positivity is exactly what is needed, and the remaining slots become leaves. Lagrange inversion yields the stated Raney number; nonemptiness gives sharpness. The argument in fact also works for c=1, so c≥2 is a scope restriction, not necessary for the formula. Independent bounded replay: exhaust weak compositions of ck+j into k parts and simulate the displayed map until min(g_i)≥c, tabulating τ; all 24 cases c=2,3, k=2..5, j=0..2 agreed (e.g. k=5 counts 715 and 3060). The supplied verify.py in the frozen package is a separate, inspected but unexecuted replay. Finite agreement does not prove the general count.

## originality

FAIL

A distinct indexed result gives the same exact extremal theorem in deterministic high-speed traffic gaps. The parameter map is exact, and the only discrepancy in the count is the lift from labelled gaps to physical placements. No additional distinct mathematical content of the frozen finding is established. This is a finding of equivalent coverage, not an assertion about which work was discovered or released first.

## value

FAIL

The sharp delay and forest structure answer a natural traffic/transport question, but in this finding they reproduce the already covered high-speed gap theorem. Counting labelled gap vectors rather than indexed vehicles introduces only the elementary placement multiplicity; no new independent invariant or structural gain is shown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
