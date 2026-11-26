# Independent mathematical audit

## correctness

PASS

Conflict-free sets are independent sets on U; every distinct attacker is attacked back, so they are all admissible. A stable set is necessarily maximal conflict-free, so it suffices to determine when every maximal independent set hits each marked neighborhood. A vertex of G[U] belongs to every maximal independent set iff isolated (otherwise extend a neighbor to a maximal independent set). For any fixed marked s, its unmarked neighbors are in different components of G[U], by acyclicity. If none is isolated one can choose independent-set extensions omitting the corresponding neighbor separately in each component and combine them to miss s. Conversely any isolated unmarked neighbor is included in all preferred sets. This handles empty neighborhoods and the empty forest. Independently recovered the all-length path series by runs: each 1 needs a neighboring singleton zero-run, so a 1-run of length one requires at least one adjacent singleton, a 1-run of length two requires both, and longer 1-runs are impossible. With zero-run types singleton/other, the 1-run weight matrix W has rows (t+t²,t) and (t,0); internal zero-run weights are Z=diag(t,t²/(1−t)) and end weights e=(t,1+t²/(1−t)). Then 1/(1−t)+e^T W(I−ZW)^{-1}e (including all-zero words) cancels exactly to the claimed numerator and denominator; exact series expansion recovered all thirteen displayed terms and yields the stated recurrence. The transfer has a unique cyclic strongly connected component with a self-loop, hence a spectrally unique simple positive PF root; its row sums are at most two and some inside the core are strictly less, giving λ<2. The polynomial changes sign between 1 and 2, so ρ=1/λ<1 and the numerator is positive there. The simple-pole coefficient and root were independently evaluated as 0.98314236892756006 and 1.54990607259428293 respectively (numerical approximations), confirming the exponential fraction and the constants.

## originality

PASS

Best-of-knowledge pass for the all-markings forest iff and the exact path marking census. The reduction of preferred extensions to maximal conflict-free sets under symmetry is not credited as new, and loopless coherence is known. The closest retrieved path record concerns a distinct counting object. Lack of journal full text leaves a genuine priority caveat, not evidence of noncoverage.

## value

PASS

The condition gives a linear-time test of agreement of the entire extension families on a standard sparse class without enumerating extensions. The path census is a natural all-length measure of robustness to self-attacks, with a non-obvious exact exponential rate and leading constant. It is not merely a different notation for counting extensions of a fixed path.

The dated certificate retains the supplied scientific assessment, sources and limitations.
