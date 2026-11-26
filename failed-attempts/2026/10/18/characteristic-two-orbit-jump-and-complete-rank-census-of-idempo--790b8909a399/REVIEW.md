# Independent mathematical audit

## correctness

PASS

The derivation rule makes the central action B exactly Au∧v+u∧Av and permits an arbitrary central block f before imposing idempotence. For a projection A with image U and kernel W, B has eigenvalues 2, 1 and 0 on ∧²U, U∧W and ∧²W. This gives the stated admissible quotient ranks in both characteristics, including n=2. The only constraints on the lower-left block are f(U)⊆ker B and f(W)⊆im B, giving exactly h_p(r,s) parameters. A central shear with h|U=−f|U, h|W=f|W sends f to zero. The GL(V) lift then conjugates all projections of the same quotient rank; that rank is invariant under any automorphism. Counting complements and central blocks gives the claimed orbit sizes, and the block diagonal representative has rank r+rs. The maximum and collisions follow from the rank quadratic; the displayed examples are consistent. Independent full-matrix tests gave {0:1,2:16} at (n,q)=(2,2), {0:1,2:36} at (2,3), {0:1,3:1408,4:448} at (3,2), and {0:1,2:96} at (2,4) using genuine GF(4). Replay: python3 /workspace/branches/2df419c7-78fc-408d-9684-32abdcc22773/independent_repro.py. The two supplied verifiers were inspected, not executed; the computations check only bounded rank histograms, not the general theorem or orbit transitivity.

## originality

FAIL

The earlier indexed Resultary record 7d1f3c0e83de gives the same admissible ranks, central dimensions, automorphism orbits, rank enumerator and examples for n≥3. The only range extension is n=2, for which the same proof already works without any new argument, hypotheses or boundary phenomenon. This is established substantive coverage, not an inference from an inaccessible paper, a shared title or a catalogue date alone. It is a statement-level comparison, not a finding of personal publication priority.

## value

FAIL

The orbit-versus-full-rank distinction is meaningful in the general theorem, but the frozen record repeats that census, including its examples, in the substantive range. The only added case n=2 applies the same elementary block count to a one-dimensional center, with every nonzero operator of rank two and no new mechanism to resolve. This boundary extension does not justify a standalone repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
