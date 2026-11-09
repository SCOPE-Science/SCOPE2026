# Review of the cyclic Rule 126 formula

## Correctness: PASS

Cyclic differences give \(y_i=1-m_{i-1}m_i\) and force the exact global parity \(\sum m_i\equiv n\pmod2\). Every admissible \(m\) has two indexed binary integrations. The all-one branch is the parity-projected independence polynomial of a cycle, giving Lucas terms and the period-three correction; mixed branches factor into independent-set polynomials of paths, with parity extraction and complete global image condition. The proof covers the \(n=1,2\) index-wrap degeneracies and derives the unique maximum for all \(n\geq3\). Finite direct and transfer-matrix verifiers agree.

## Originality: PASS, qualified

The 1989 Jen paper explicitly knows Rule-126 Fibonacci-product preimage formulas **for finite observation strings with free/infinite-lattice boundaries**, and the generic cyclic matrix trace formula is known, notably from de Bruijn methods explained by Gómez Soto (2006). These methods are relevant and imply efficient algorithmic access; they are not new in this contribution. The compared texts do not provide the parity-adjusted exact closed formula for **every indexed cyclic target**, the global Garden-of-Eden criterion, or proof of the unique all-one maximizer. Searches for cyclic Rule-126 count, parity-run specialization, and equivalent preimage matrix expressions did not locate direct coverage. That absence does not establish absolute historical novelty. Unread specialist tables and unknown direct corollaries are residual risks.

## Value: PASS

The new image criterion answers which finite-ring outputs are attainable, including a nonlocal parity obstruction beyond the standard local factor prohibition. The all-length fiber formula quantifies inverse ambiguity of each output and pins down the unique worst-case uncertainty exactly. These are natural finite-periodic dynamical invariants for a benchmark elementary cellular automaton and a motivated extension beyond the open-boundary formulas; no result for arbitrary rules is implied.

## Checks and limits

The included `verify_formula.py` enumerates every source and target through length 15, and `verify_transfer.py` uses a separate de Bruijn trace and parity dynamic program on all outputs through length 12 and selected longer outputs through length 64. Original full-text PDFs consulted: relevant passages from Jen (1989), Gómez Soto (2006), and the 2015 Rule-126-with-memory study; the 2012 Rule-126 arXiv record was checked for exact day-resolution and context. The earlier 1989 article has a verified publication year but no verified day in the consulted record; 2012-12-01 is the day-resolved date of the linked historical Rule-126 arXiv reference, not a claim of first-ever publication of the topic. Neither code enumeration proves the infinitely quantified statement without the written proof.

Self-review: passed. Independent audit: not yet performed.
