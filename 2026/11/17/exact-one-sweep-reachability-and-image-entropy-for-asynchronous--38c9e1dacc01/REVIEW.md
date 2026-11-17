# Scientific review: exact one-sweep reachability for sequential Rule 184

## Correctness — PASS
The object is a labelled binary ring of length \(n\ge3\), with the in-place scan \(0,1,\ldots,n-1\) and the exact Wolfram Rule 184 local Boolean function. The proof derives the three classes of site equations, establishes three necessary output tests, and supplies an explicit predecessor for every word satisfying all three. The associated four-state graph is a deterministic cyclic factor automaton for forbidden `101`; boundary failures are removed using two disjoint matrix entries, producing the stated generating function by a formal resolvent. Perron–Frobenius applies because the graph is primitive; the leading pole is not canceled. The standalone original-map enumeration checks every binary input and potential output for all lengths three through eighteen, and separate symbolic and transfer computations reproduce the rational function and the recurrence. Neither enumeration nor the program logs replace the all-length proof.

## Originality — PASS (historical priority qualified)
The same finite-ring dynamics is *not* the synchronous traffic Rule 184 map: the latter conserves particle number and its one-step image is cyclic `1100`-avoidance, with a different rational generating function and exponential base; the present sweep can delete a single car and has scan-origin boundary exclusions. The 2007 asynchronous Rule-184 article's Rule-184 proposition describes order-independence of eventual periodic states rather than the one-sweep image. The 2014 asynchronous-conservation treatment and the 2025 sequential cycle survey address particle conservation or recurrent dynamics, not the exact boundary-sensitive image criterion. Two directly relevant published synchronous image results were inspected in complete RESULT.md texts and explicitly assume simultaneous updates. Searches of accessible published results using the update schedule, candidate forbidden word, boundary tests and growth polynomial returned no statement that covers or implies the present theorem. Unindexed or inaccessible studies remain a genuine priority risk; absence from search results does not prove uniqueness.

## Mathematical value — PASS
The one-sweep reachable language of a natural classical cellular automaton under a standard deterministic asynchronous schedule is a fundamental dynamical observable. The theorem recognizes *all* possible outputs at every ring size, gives a constructive inverse, determines the exact number of Garden-of-Eden outputs, and quantifies the entropy change from the synchronous rule. Its boundary-sensitive obstruction is structural rather than a finite table or an isolated numerical count. The fact that asynchronous scanning can destroy particles further separates the observable from the well-known conservation picture.

## Closest literature and risks
- Macauley, McCammond and Mortveit, arXiv:0707.2360 (2007): Rule-184 eventual periodic order-independence (Proposition 6.3), not the one-sweep language.
- Hazari and Das, *Complex Systems* 23 (2014): number conservation across asynchronous schedules; related but different claim.
- Donoso-Leiva et al., arXiv:2505.10645 (2025): comparison of synchronous and asynchronous cyclic dynamics and recurrent states.
- *Exact one-step reachability, inversion, and density spectrum of the cyclic traffic automaton* (2026): simultaneous Rule 184, image `1100`-avoidance.
- *Exact cyclic one-step image and density-resolved enumerator of traffic Rule 184* (2026): same simultaneous-update restriction.

The claim concerns only a single prescribed left-to-right scan, not arbitrary schedules, repeated-sweep convergence, or exact fiber multiplicities. Historical priority beyond inspected public materials is not certified.

Self-review: passed. Independent audit: not yet performed.
