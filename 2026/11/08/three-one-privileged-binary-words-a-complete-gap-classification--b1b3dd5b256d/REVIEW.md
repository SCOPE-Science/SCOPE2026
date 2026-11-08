# Review of the three-one privileged-word classification

## Correctness — PASS
The scope fixes the binary alphabet and exactly three ones. The proof verifies the two-one auxiliary classification, rules out every possible privileged-border one-count (0, 1, 2, 3), establishes both sufficiency branches, and constructs a reversible parametrization by three nonnegative integers and one orientation. It separately counts all palindromic cases and derives the pole asymptotic. Direct recursive enumeration (40,920 examples) and an independent coefficient computation through length 700 passed. Numerical checks alone are not used as the infinite proof.

## Originality — PASS, with historical qualification
Peltomäki (2012, 2016) gives the underlying definition and rich-word theory, and explicitly identifies a shortest nonpalindromic privileged example. Forsyth–Jayakumar–Shallit (2013) proves endpoint-run equality, a related restricted three-one family, and a broad sufficient complete-return construction. These established facts are credited, not claimed. The full four-zero-gap criterion together with the exact weight-three nonpalindromic partition law is not present in the materially inspected portions of these sources. Nicholson–Rampersad (2015) treats unrestricted asymptotic bounds. OEIS A231208 and A235609 provide total counts and a finite list of words, rather than this all-length weight-refined formula. Unindexed equivalent statements and the possible simplicity of extracting this specialization from known structural results remain risks.

## Value — PASS
The first nonpalindromic privileged examples have exactly three ones, and three is thus a natural sparsity boundary between palindrome-like and genuinely privileged behavior. The theorem classifies the entire weight-three slice of a non-context-free language and gives a structural reason for the exact quasi-polynomial counting law: a bijection to partitions with parts 2, 3, and 4. The conclusion also quantifies how rarely privileged words occur within weight-three words. It is not a claim about a general new privileged-word algorithm or an unrestricted enumeration formula.

## Remaining limitations
The theorem covers only fixed content three and has no higher-weight extension. The published 2016 dissertation was available as extracted text at relevant sections, but PDF imagery could not be fetched. No independent reviewer has assessed the result or its historical priority.

Self-review: passed. Independent audit: not yet performed.
