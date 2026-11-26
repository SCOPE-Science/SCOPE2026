# Independent mathematical audit

## correctness

PASS

Each candidate supplies exactly two approval incidences, even at n=2. Each strict improver spends at least one such incidence, so a nonempty proposal needs at least n|T|/k voters but can reach at most 2|T|. If n=2k, a block forces equality: all approvers of each proposed candidate are among the improvers, all improvers have zero old utility and exactly one new approval. Either proposed candidate therefore lies at the centre of a vacant cyclic triple. Conversely, its singleton proposal and two approvers block with equality. When n=2 no such vacancy is possible; for k<3 at half budget there cannot be three vacant positions, while k=3 admits one and gives 14 of 20 stable committees. Distinguishing a chosen position gives 2k locations and an ordered list of k gaps of sizes 0,1,2 totaling k; divide by k, not by rotation or orbit size. The multinomial sum follows, and the uniform lattice law on {0,1,2} has span 1 and variance 2/3, giving the stated local-CLT constant after division by the central binomial coefficient. No inference from finite checks is needed.

## originality

FAIL

The stated facts are correct, but the actual structural threshold results are covered by the proofs in the distinct indexed three-quarter-threshold record 7f5b4dfc0244. With voter indices shifted by one it is precisely the same profile, utilities and blocking rule. Its proof explicitly shows no blocking below half, equates JR to no vacant triple at and above half, and proves that every JR committee is core up to but not including 3n/4. Non-JR gives a direct singleton block at half. The restriction n≥4 excludes only the immediate small cases relevant here. The stated existence theorem of the comparison is not itself the complete membership result; its proof establishes the covering statements. The census is a direct cyclic-gap coefficient extraction from that covered criterion, and its asymptotic is the standard central coefficient divided by a central binomial coefficient. I find no nonmechanical remainder. The comparison entry has a later displayed date; this is a scientific coverage decision, not a claim of chronological precedence or independent rediscovery.

## value

FAIL

The all-committees boundary and exact stability test are useful questions, but the strong same-profile comparison already resolves them. Once those are fixed, the balanced cyclic count and rate require just the standard marked-gap coefficient and a central coefficient asymptotic, with no remaining new structural constraint or separately motivated invariant not already mechanically implied. A narrower claim to the central-trinomial factor would not meet the scientific value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
