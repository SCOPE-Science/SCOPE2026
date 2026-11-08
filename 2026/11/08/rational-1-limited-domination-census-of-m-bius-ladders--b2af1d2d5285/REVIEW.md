# Mathematical assessment

## Correctness — PASS

The stated local predicate on the cubic graph is exactly checked by a two-row 16-state transfer (26 transitions). The crossing-edge bound proves \(|S|\ge n\) and the consecutive-arc construction proves \(|S|\le n+1\). An exact integer characteristic/adjugate calculation verifies the displayed rational generating function for all \(n\), not just a finite sample. Extracting its first two size diagonals yields the stated four-residue minimum and the \(4\), \(2n\), and \(3n\) labelled minimum counts. The separate direct graph enumerator agrees for every \(2\le n\le9\); the exact transfer is checked to width 16. The standalone `verify.py` was executed and printed `VERIFY_OK`.

## Originality — PASS (provisional historical priority)

Božović et al., arXiv:2606.22422, introduced limited domination and its regular-graph equivalence to internal-degree constrained domination. Radić and Tepeh, arXiv:2610.01796, study computational hardness and Goldberg snarks. Radić, Radić, and Tepeh, arXiv:2610.26259, establish general cut-defect structure and quote the prior perfect-matching-cut characterization of the half-order equality case. Those generic results do not provide the twisted Möbius-ladder generating polynomial, the family-specific modular minimum, or the exact counts. Search comparisons covered published mathematical records, alias terminology, relevant primary literature, and possible tabulations. The single \(n=2\) complete-graph boundary is not separately novel. The 2021 Fakharan et al. general cubic article was not obtained in full; examples not present in its accessible abstract remain a priority risk. Absence from a search result is not proof of uniqueness.

## Mathematical value — PASS

The calculation resolves a natural complete enumeration problem for a nonplanar vertex-transitive cubic family motivated by recent limited-domination research. The sharp mod-four criterion, including the equality/cut boundary and three different optimizer-count regimes, supplies reusable structural and enumerative information. It is not merely a rescaling of a known bound. There is no claim about other cubic graph families.

## Verification and limits

The polynomial identities are finite exact symbolic certificates, incorporated into a mathematical transfer proof. The independent external mathematical review is not performed; the successful computational replay is self-review. For \(n\ge2\) the labels refer to specific vertices, so counts are not divided by graph automorphisms. Historical priority requires further external assessment.

Self-review: passed. Independent audit: not yet performed.
