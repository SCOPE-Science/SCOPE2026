# Review of sharp contiguous-read reconstruction of noncrossing words

## Correctness — PASS

For the full contiguous factor-count readout through length \(k\), endpoints and directed de Bruijn graph are determined. The proof rules out repeated heterogeneous factors by the noncrossing condition, then removes homogeneous loops. A letter appearing at most \(2k-2\) times cannot support both a homogeneous loop and a distinct return excursion, or two distinct return excursions. Remaining repeated vertices cannot interleave. The standard endpoint-fixed Euler-trail switching criterion therefore yields a unique spelling. The sharp collision \(a^kba^{k-1}\) versus \(a^{k-1}ba^k\) was checked algebraically. Bounded independent word and partition enumerations passed. Unbounded correctness relies on the proof, not those checks.

## Originality — PASS (qualified)

The general relation (Karhumäki–Saarela–Zamboni, 2013) and the spectrum assembly Eulerian condition (Bresler–Bresler–Tse, 2013, citing Ukkonen/Pevzner) are acknowledged antecedents. Lin–Fu's 2017 work concerns the noncrossing restricted-growth source, not its directed factor-spectrum reconstruction. An earlier noncrossing fully-doubled two-gram theorem is a strict special case. Targeted literature and mathematical-record searches did not locate the all-\(k\) sharp \(2k-2\) boundary or its corresponding partition-code capacity. An earlier unindexed equivalent or an inaccessible assembly paper could still cover it.

## Value — PASS

The sharp threshold is universal in read length and alphabet size, is attained by an explicit minimal two-letter obstruction, and establishes exact finite-block zero-error capacities for all bounded-block noncrossing partition sources. The counting coefficients alone are standard; the global recoverability and exact sharp boundary are the new scientific content.

## Scope and external limitations

No claim is made for noisy, circular, reverse-complement-pooled, or scattered-subsequence observations. Independent mathematical verification and an exhaustive literature guarantee are not available.

Self-review: passed. Independent audit: not yet performed.
