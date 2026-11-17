# Scientific assessment

## Correctness — PASS
The walker dynamics is completely specified, including the advance-before-routing convention, labelled arms, pointer indexing, and state recurrence. Excursion decomposition proves the exact first-periodic-entry formula. The classical unicycle/Euler-tour criterion identifies the first time the walker is truly periodic rather than merely returning to the hub; the last blocking rotor is reached at the exact first recurrent state. The extremal optimization is strict in terminal arm order, blocker count, and all other-arm excursion lengths. The fixed-depth probability limit follows by a geometric tail and bounded law of large numbers. An independent brute-force map construction reproduces the formula, primitive period, maximum, and number of maximizers in all 24,344 tested states. The finite test is corroboration, not the infinite proof.

## Originality — PASS, with historical-priority qualification
Relevant full text inspected: Chalopin et al., arXiv:1407.3200, Sections 1 and 5.1, derives general rotor exploration phase inclusions and single-token prediction; it does not state the present per-initialization spider expression or its sharp statistical consequences. The public author manuscript of Bampas et al. gives general bounds and adversarial port-order results, not these explicit finite spider counts; its definition of completion of the first Euler tour differs from first periodic-state entry. The earlier path result of Menc et al. concerns a different starting position and graph topology. A semantic indexed finding search did not locate an equivalent rotor-spider record. Search incompleteness is not proof of priority; unindexed studies and general exploration identities might contain equivalent implications.

## Value — PASS
Rotor-router stabilization can take order \(|E|\operatorname{diam}(G)\) steps and depends strongly on initial local memory. Equal-arm spider trees supply a natural first multi-branch case where memory is carried both along arms and around a hub. The full initial-state formula is useful for exact transient statistics, identifies a unique extremal morphology for each hub phase, gives a quadratic-in-arm-depth sharp clock, and separates this exponentially rare worst case from the linear-in-branch-count typical clock. This goes beyond a numerical enumeration or restatement of the general Euler-tour theorem.

## Scope and risks
The result is not an arbitrary-tree theorem or a statement about first completed Euler tours. Formal priority, especially any equivalent spider specialization hidden in algorithmic rotor-router papers, remains a risk. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
