# Review of the four-color bipartite temporal classification

## Correctness

PASS. The update rule factors exactly through initially occupied color classes on each shore. All 225 pairs of nonempty color supports are covered, and tagged representatives preserve the original-labelled trajectory including coalescences. Replayed coefficient matrices give the ten classes; a separate direct-neighbor implementation confirms 92,752 fully labelled states. The proof of general \(m,n\) is the surjection lift of the exact 225-case certificate, not a finite-size extrapolation. The code is supplied for rerun and its full finite catalogue is readable.

## Originality

PASS, qualified. The 1993 lattice work treats multi-color CCA but not complete-bipartite exact first-entry counts; the 2016 arbitrary-graph result addresses three colors. The closest prior four-color complete-tripartite theorem assumes three nonempty shores and has only periods one and four, whereas this proof exhibits genuine primitive six-cycles and an exact bipartite ten-class census. Searches of literature and published research statements found no equivalent or dominating theorem. Full 1993 source inspection was unavailable and unindexed equivalents remain a residual priority risk; lack of a search hit alone is not claimed as a proof of novelty.

## Mathematical value

PASS. The complete, natural two-parameter classification resolves precise first-entry distributions beyond general eventual-period bounds. The period-six resonance is confined to exactly four ordered pairs of three-color supports, and sharply separates the bipartite and previously classified tripartite dynamics. Exact cycle populations, finite-shore cutoffs, and the vanishing density of six-cycles explain a structural dynamical distinction that a small numerical experiment alone would not settle.

## Scope and limitations

Applies only to synchronous four-state successor-contact updating on labelled complete bipartite graphs. There is no assertion of independent certification or historical uniqueness. Full text of one old general cellular-automata reference was not accessible; the comparison therefore rests on its published abstract and domain, not an alleged page-by-page exclusion.

Self-review: passed. Independent audit: not yet performed.
