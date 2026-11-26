# Independent mathematical audit

## correctness

PASS

The frozen periodic counting proof is valid: for each edge every excited event can match at most one opposite event at a time offset ±1 (spacing at least three), and at half degree the incoming threshold saturates the global edge bound. This gives Au_t=r(u_{t−1}+u_{t+1}); B^TB−2I has spectrum {2r,n−4,−2}; for n≥5 the two nonprincipal ratios to r=n−2 are nonintegral rationals, impossible for a root-of-unity sum. This is correct, but not distinct. The repair claims only the n=5,6 transient census. For disjoint excited/refractory masks X,Y with K_n-endpoint degrees d_X, an edge uv outside X is eligible iff d_X(u)+d_X(v)≥n−2; no excited edge is counted twice. The successor (Z,X) with Z subset of eligible E(X) has exactly 2^(m−|X|−|E(X)|) predecessors with that X, because Y on E(X) is fixed and the remaining bits outside X are free. Only all-rest needs reassignment from time 1 to 0. Ran the self-written exact replay `python /workspace/repairs/4/verification/exact_grouped.py 5 6`: 14,476 groups/59,049 states and 1,662,308 groups/14,348,907 states, exact repaired histograms and minimum base-three time-four witnesses 94 and 3199. Direct evaluation of the displayed witnesses separately confirms the last refractory-to-rest step. The frozen C++ sources and verification notes were inspected, not executed; no compiler is needed for the new proof. An earlier independent traversal also gave one fixed point and two primitive three-cycles for n=3,4, now cited background only.

## originality

PASS

Frozen originality fails for its headline: same-day distinct records directly cover the infinite-family extinction and the small recurrent exceptions; their exact UTC order is not inferred. The repaired finding expressly attributes those results and contributes only the sharp finite settling-time cutoff and full histograms at the first two extinguishing orders. None of the checked originals gives these transient invariants or implies them by a parameter substitution.

## value

PASS

The scopes n=5 and n=6 are motivated as the first two extinguishing family members immediately past the periodic exceptions. At a threshold exactly equal to half degree a recurrent-mode obstruction alone has no implication for rapid settling. The exact worst case of four and distribution of late transients give concrete small-order baselines for further settling-time theory or validation of dynamics on this natural family; the precise four-step fractions are immediately available. The repair does not pitch routine spectral specialization or larger-order extrapolation as novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
