# Independent mathematical audit

## correctness

PASS

By symmetric PBH, leaving two nonbridge twins uncontrolled makes their difference an invisible eigenvector, giving both quotas. For an exact-quota baseline the selected vertex equations imply that omitted nonbridge entries u,v have opposite entries at the respective gateways. The omitted-vertex equations are (ap-lambda)u=0 and (bq-lambda)v=0; a gateway equation is (lambda-ap)u+c(v-u)=0. With c>0 a nonzero solution has u=v nonzero and ap=bq. At resonance this is the unique invisible direction and has no zero in the four omitted coordinates, so any extra actuator removes it. This proves the all-set criterion and independence of positive c. The resonant minimum-set count has 2(p-1)(q-1) sets containing one gateway and (p-1)+(q-1) sets containing neither, not four times the baseline count; the claimed coefficient and polynomial are correct. For zero forcing two initial nonbridge whites are an obstruction until one of them is forced, which cannot first happen while both are white. A baseline stalls. From an admissible superset, if a gateway is initially blue, use a blue nonbridge neighbor on that side to force the sole possible remaining nonbridge white; if all nonbridge vertices on a side are blue, they can force the gateway. A fully blue side then forces across the bridge if needed, and the other side finishes. This spells out the force in the frozen wording without requiring a gateway to force while it still has two white neighbors. The finite modular checks were inspected, not rerun; the real-field proof does not rely on them.

## originality

FAIL

The current published catalogue contains a distinct record f2d043ae271c giving exactly the all-subset fixed-Laplacian resonance criterion, all enumerators and the zero-forcing comparison. The indexed path of that source is later than the frozen record's path; this is verified equivalent coverage, not a finding about who obtained the theorem first or whether either result derived from the other. No distinct mathematical claim remains to validate against the published corpus. The zero-forcing classification itself was already separately covered by 5431b532d7f2 and is properly acknowledged.

## value

PASS

As mathematics this is a natural complete classification for an independently actuated network: it identifies an exact weight collision, a one-dimensional invisible mode, and precisely when fixed-weight control needs fewer leaders than zero forcing. The duplicate-coverage objection is recorded on the originality axis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
