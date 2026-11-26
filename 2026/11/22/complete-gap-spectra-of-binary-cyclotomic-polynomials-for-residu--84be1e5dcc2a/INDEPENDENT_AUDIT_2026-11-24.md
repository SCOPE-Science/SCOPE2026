# Independent mathematical audit

## correctness

PASS

The Bézout rectangle identity follows by clearing denominators; the positive and negative terms are disjoint modulo a and within each rectangle no degrees repeat. For b=as+2 the occupied residues form one interval per a-row; boundary lengths decrease by twos and then increase by twos, each stage of length s. For b=au−2, u=s+1≥2, the early two-component rows each contribute u occurrences of their even interior gap, the central separation contributes a further u at length two, and the late boundary stages give u of each even length from 4 through 2h−2. The outermost boundaries contribute 2(u−1) at 2h. At h=2 the late intermediate stages are empty and the last u−1 boundaries still have length 2h. The rectangle counts minus one minus the nonunit gaps give the two unit counts. This argument uses coprimality, not primality. Independent finite coefficient reconstruction followed by gap measurement (python3 /workspace/branches/f752dabd-f88a-4b0c-8710-5aaa8112414e/gap_spectrum_probe.py) matched all 224 cases a=5,7,…,31, s=1,…,8 and both signs, including (9,20) and (9,25). The uploaded checker was not run; the all-parameter result follows from the row proof.

## originality

PASS

Pass for the complete, uniform closed-form frequency law at odd a≥5 for both residue classes, not for the individual known maximum-gap count, the set of allowed lengths, the classical support representation, or the earlier b=a+2 slice. The same-day a=5 transition counts overlap that slice in a different direction without covering varying a or establishing priority. The broad coefficient representation gives raw support data but does not give the symbolic row-boundary and within-row frequency evaluation for unbounded a and s. The retrieved prior statements do not eliminate that evaluation as a new contribution.

## value

PASS

The uniform full distribution specifies how a natural polynomial support is spaced, including the unit gap mass and how the sign of the residue changes every interior even frequency but leaves the largest unchanged. The ±2 cases are adjacent to the previously fully evaluated ±1 residue classes and form two unbounded families, not an arbitrary finite slice. The multiplicities carry information beyond Bachman’s allowed gap set, total sparsity, and maximum-gap frequency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
