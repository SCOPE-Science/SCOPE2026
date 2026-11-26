# Independent mathematical audit

## correctness

FAIL

The asymptotics follow conditionally: with a uniform bound CTn exp(−c m^α), choose cK^α>s+r+1, use T≤n^s and m^α≥K^α log n, and absorb C after retaining a strict exponent margin. Then log N=log n+O(log log n) and k=Θ(n) give both claimed size laws, and O(log m) gives the time law. But §I.1 describes its estimate as the overhead form of Theorem 81, which expressly invokes Remark 39's locally trivial seed condition. Bounded degrees and positive rate do not imply it: adjoining a free encoded qubit to each block of a bounded-size CSS block family leaves bounded degrees and positive rate, but a Pauli on that free qubit has zero syndrome and is not a stabilizer. The formal theorem also states p/p_RG≤a as a condition, not simply every p<p_RG with the same normalization. The frozen proof cannot apply this theorem to every seed family and rate it claims. This is a material hypothesis gap, not a counterexample to the decoder's actual reliability on those seeds.

## originality

FAIL

Yuan's finite-parameter theorem already implies the demonstrated family-level estimate at all admissible parameters: solving the bound for m and rewriting dimensions and runtime is a mechanical specialization. No exact matching standalone formulation was verified, but that is not necessary for coverage. The wider seed-family and noise quantifiers are not shown known; they are unsupported by the proof and leave no established distinct remainder.

## value

FAIL

The operating regime is a useful way to present Yuan's bound, but the frozen derivation just chooses a logarithmic exponent margin and converts between n and N. After retaining the actual source assumptions, there is no distinct improved threshold, overhead, decoder, family construction or tradeoff. Extending applicability to every bounded-degree positive-rate seed would be substantive, but the record does not establish it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
