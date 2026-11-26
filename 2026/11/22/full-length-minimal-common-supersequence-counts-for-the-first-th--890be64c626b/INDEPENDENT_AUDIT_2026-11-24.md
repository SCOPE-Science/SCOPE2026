# Independent mathematical audit

## correctness

PASS

Any minimal common supersequence is covered by the union of any chosen pair of embeddings, so its length is at most 2n for these two n-letter inputs. At length 2n, the two embedding images must partition the output, and varying either while holding the other fixed contradicts coverage. Conversely disjoint unique embeddings make every position essential and distinguish successful masks as distinct words. Coordinatewise min/max with a competing embedding gives a comparable one; choosing its first leftward or last rightward difference yields a one-site replacement. Each step's opposite-letter comparisons in the grid test whether its letter could replace either adjacent assigned letter of the opposite input, so together the tests are necessary and sufficient. I independently derived the offset-strip reduction: interior U-step forbidden residues are 0,1 and V-step forbidden residues 1,2; U first is dead because the new unmatched letters agree. A transition below offset −(q−2) is possible only at i=0, but the resulting (0,q−1) is dead. On j=n, any surviving U-step follows the same band edges; i=n is reached only at the endpoint. Thus completed paths correspond exactly to closed walks of 2n steps from the endpoint of the path on q−1 vertices. For q=3 the return walk is unique; for q=4 each nonterminal even depth independently chooses either end, giving 2^(n−1); for q=5 the even-depth pair transforms by (a,b)→(2a+b,a+b), with (1,1) after two steps, so the projected endpoint count is F_(2n−1). These formulas cover k=1 and all later repetitions and are positive, proving 2n is attained. A separate direct check generated actual distinct shuffles, deleted each site and tested the original subsequences; it matches for q=3,4,5 and k=1,2 (including 4,181 out of 45,542 shuffles for q=5,k=2). Replay: python3 /workspace/branches/independent-check/word_checks.py; general argument in proof_notes.md.

## originality

PASS

Exact general enumerators can compute the finite instances but the inspected methods do not supply these symbolic counts for a periodic input family. The closest distinct indexed results switch to binary opposite-run inputs, a shortest-length statistic, or different subsequence observables; none contains the three maximum-length-layer formulas for these one-step cyclic shifts. This is a bounded statement-level comparison, not exhaustive priority certification.

## value

PASS

The largest achievable length is a natural extremum for minimal, not shortest, supersequences. The first three nonbinary cyclic alphabets exhibit distinct constant, power-of-two and Fibonacci behavior for the same input phase relation, explained by a small offset-walk structure and genuine word counts. Exact formulas for all repetition counts provide more than running a generic enumerator on a few instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
