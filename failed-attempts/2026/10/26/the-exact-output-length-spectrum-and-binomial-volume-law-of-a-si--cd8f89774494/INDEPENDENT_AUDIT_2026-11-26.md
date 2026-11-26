# Independent mathematical audit

## correctness

PASS

For a fixed received-length change δ, a shorter removal window can be extended to d=min(k,k−δ) on the input and padded with the unchanged letters on the corresponding sides of the inserted block. Such a containing window always exists since n≥k, including insertions at the ends. If i=d+δ>0, an output at a nonfinal position j has a later representation exactly when its first inserted symbol equals x_j: later positions preserve x_j, and matching it permits a shift by one and appending x_(j+d). Thus each nonfinal window contributes (q−1)q^(i−1) distinct rightmost representatives and the final one q^i. At δ=−k, deletion outputs at a<b agree exactly when x_j=x_(j+k) throughout a≤j<b; the outputs count equal runs. The k nontrivial nonpositive offsets sum to the geometric part of A, and δ=1,…,k gives the displayed arithmetic part. Along the residue-class paths there are q^k root assignments and exactly q−1 child choices for each edge designated unequal (one for each equal edge). This gives the full histogram, binomial law, all extrema and moments; n=k is degenerate and the normal limit only standardizes positive variance as n−k→∞ at fixed q. Exact replay in /workspace/review-replay.py (argument 1) independently built deduplicated outputs as strings and checked all layers, the closed-form baseline and entire center histogram on 44 triples and 17,413 centers; the symbolic argument supplies the unrestricted theorem. Minimum centers are precisely words having k as a period in the finite-word sense, not necessarily having least period dividing k.

## originality

FAIL

The frozen comparison misses the arbitrary-alphabet fixed-pair theorem of Sun, Lu, Zhang and Ge (arXiv:2403.11750v2, Theorem 1), not just the earlier binary formula. It covers exactly the two claimed positive-insertion shell counts after a one-step window-padding reduction. The only exceptional shell is the already published burst-deletion size formula. Its random-center law is obtained directly by freely choosing the first k letters and choosing at each subsequent position either the letter k places back (one choice) or any other letter (q−1 choices). Disjoint lengths then give the displayed binomial histogram without another counting problem. The complete aggregate was not located verbatim; the failure is straightforward implication from existing exact results, not a claim of verbatim prior publication or of incorrect formulas.

## value

FAIL

The error-ball distribution is a natural diagnostic, but this version writes out a direct aggregation of the known arbitrary-q fixed-burst formula and pure-deletion count. Padding determines the representative pair with no new overlap enumeration; the binomial law is immediate sequential counting once the deletion count is inserted. The result is useful as a summary of existing facts, but no nonmechanical exact gap remains and no independent code-size or inverse-ball result is proved. There is no substantive repair in the frozen scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
