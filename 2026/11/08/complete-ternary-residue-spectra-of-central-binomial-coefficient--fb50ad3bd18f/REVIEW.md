# Scientific review

## Correctness — PASS
The complete result follows from Kummer's carry criterion and Lucas' digit formula, plus an explicit multiplicative-order construction of infinitely many positive-index witnesses. The proof checks both directions: absence of forbidden nonzero residues for fixed parity, and infinite occurrence of all permitted residues. The shift \(3^{Lt}\) preserves every chosen congruence class modulo \(b\) and digit pattern. The case \(b=1\), negative offsets, and the required index positivity are accounted for. The standalone finite checker verifies the constructions in bounded examples; no finite run is presented as a proof of infinite cases.

## Originality — PASS, with historical limitations
Guo–Krattenthaler (2013, Conjecture 7.1) propose universal attainment of every prime-field residue. Vsemirnov's earlier counterexamples concern the prime five. He–Yuan (2024), Section 3, defines general residue sets, proves closure properties, and poses their exact determination as Problem 3.6. Their positive-case theorem requires \(p>a>b\), excluded by \(a=2b\ge4,p=3\); their Theorem 3.8 concerns parameters with \(a\equiv b\) modulo a high power of three, not our coprime \(b\) specialization. The present complete symmetric prime-three arithmetic-progression spectrum and sharp parity dichotomy are not established in those examined statements. Published research-record searches and accessible prior claims found no dominating claim. A broad 2001 paper on digital binomial distributions was accessible only at abstract level and remains a historical-priority risk. An unavailable full historical source is not silently represented as checked. No claim of exhaustive novelty certification is made.

## Value — PASS
The theorem gives an exact natural residue-set classification for every progression of central indices coprime to three, explicitly resolving a slice of the general residue-set problem identified in the specialist literature. It also isolates the smallest odd-prime counterexample mechanism to a published conjecture and distinguishes the parity boundary with infinitely many constructive witnesses, not a single easy negative example. Exact attainable sets are substantive invariants, although this result does not imply a general asymptotic counting theorem.

## Verification and limitations
The included `artifacts/verify.py` runs independently of external packages. Historical priority is qualified; a specialist audit has not been performed. The theorem concerns the prime three, excludes \(3\mid b\), and does not address general nonsymmetric binomial parameters or frequencies.

Self-review: passed. Independent audit: not yet performed.
