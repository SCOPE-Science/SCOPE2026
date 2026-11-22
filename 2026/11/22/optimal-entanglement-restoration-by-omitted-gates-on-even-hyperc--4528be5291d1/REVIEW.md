# Scientific review

## Correctness — PASS

The proof reduces pure-state Schmidt entropy to \(\mathbb F_2\) cut rank, checks the original hypercube baseline using \(A(Q_{n-1})^2=I\), identifies the fully omitted graph as \(P_4\square Q_{n-2}\), and gives an explicit tensor-nilpotence inverse for its adjacency. Rank-perturbation bounds from both ends force every partial subset to gain one bit per gate, and prove no smaller deletion set can maximize the entropy. The hypotheses \(n\ge2\) even, qubits, Hamming-parity cut and ideal gate omissions are used throughout. Exact finite checker code and separately oriented elimination passed the documented 65,794 subset tests; enumeration is not substituted for the infinite proof. The saturation bound concerns number of omitted controlled-\(Z\) gates, not hardware quality.

## Originality — PASS, with historical-priority risk

The general cut-rank/one-gate bound is established by Hein–Eisert–Briegel (2003), and the even-cube checkerboard baseline is explicitly present in *Parity-cut Schmidt spectra of antipodally augmented hypercube graph states*; neither is claimed new. Full-text comparisons with that result, *Paired omitted-bond cancellation in three-dimensional toroidal cluster states*, and *Sharp incidence-matching fault threshold for graph-state entanglement on even-order projective planes* find no theorem implying the exact \(P_4\square Q_{n-2}\) rank-restoring construction and its all-subset minimality for even cubes. The full hypercube scrambling article of Hashizume and collaborators does not assess this gate-omission extremum. Aliases, stronger coverage, tables and direct implications were explicitly compared. An earlier unknown equivalent modular-algebra theorem could cover the construction; the searched evidence is not a proof of novelty.

## Mathematical value — PASS

The proof answers a natural, nontrivial extremal question: determine the minimum number and a working placement of omitted gates needed for maximal balanced entanglement of the even-dimensional hypercube graph state. Its exact answer is \(2^{n-2}\), and the strict unit gain for all subsets is an additional structural law. It is an infinite-family result, not arbitrary numerical optimization. The gain is mathematical, not a claim that uncontrolled device faults are desirable.

## Limitations

Ideal pure qubit graph states; fixed even/odd Hamming-weight bipartition; even dimension. No results on arbitrary cuts, qudit arithmetic, noisy implementation, or general hardware optimization. Independent validation and historical-priority certification are not asserted.

Self-review: passed. Independent audit: not yet performed.
