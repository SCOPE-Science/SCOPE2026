# Review of Exact generating function for cyclic binary trigram profiles

## Correctness — PASS
Every cyclic trigram profile is an integral nonnegative balanced flow on the four length-two states whose nonzero support is connected. Conversely the finite directed Eulerian theorem constructs a circular word from each such flow, including the cases with loops and short rings. Conservation forces the unique parameters \(a,b,t,d,h\), \(0\le b,d\le t\), and length \(n=a+h+2t+b+d\). The four disjoint support types are exhaustively classified in RESULT.md and give the displayed exact generating series for all \(n\ge1\). Exact integer-polynomial multiplication establishes its reduced form. Independent word enumeration through 16, independent balanced-flow enumeration through 40, and an exact polynomial identity check all pass. The computation does not substitute for the all-length Eulerian argument.

## Originality — PASS, qualified
Kiah–Puleo–Milenkovic [1] already give the general de Bruijn DNA-profile framework and the precise asymptotic constant \(c(2,3)=1/288\) in their table; those are excluded from the originality claim. Jacquet–Knessl–Szpankowski [2,3] analyze first-order Markov types and discuss higher-order asymptotics, not the finite-size cyclic binary order-two support correction established here. The inspected relevant sections of these primary texts, related full-text searches, published research records, and previously recorded mathematical claims disclosed no exact all-length rational series for eight cyclic trigram counts. The distinction is the fully explicit all-length enumeration with connected-support corrections and a constructive Eulerian proof. The 2012 extended Markov-types article [4] was not fully accessible, and independent historical-priority verification remains necessary; a failed search is not proof of novelty.

## Value — PASS
The complete trigram multiset is a natural noiseless DNA reconstruction and order-two Markov observation. The exact number of attainable outputs is the maximum size of a zero-error code using this observation. The exact small-blocklength count, short-ring boundary behavior, and explicit identification of balanced but disconnected nonrealizable frequency vectors are not supplied by the known leading asymptotic. The method highlights where merely imposing stationary-flow constraints overcounts realizable cyclic strings.

## Closest literature and limitations
[1] H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Storage Channels*, arXiv:1410.8837 (original version 2014-10-31), https://arxiv.org/abs/1410.8837; asymptotic \(c(2,3)\) table and general profile framework.

[2] P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types* (2010), https://dmtcs.episciences.org/en/articles/2768; first-order balanced transition counts.

[3] P. Jacquet, C. Knessl, W. Szpankowski, *Markov Types Again Revisited* (2009), https://www.cs.purdue.edu/homes/spa/papers/markov-types.pdf; broad asymptotic higher-order discussion.

[4] P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs* (2012), DOI 10.1109/TIT.2012.2191476; title and abstract inspected, full text unavailable.

No assertion is made about alphabet size three, length-four windows, linear boundary conditions, observation noise, multistep channels, independent verification, or exhaustive historical priority. The known leading coefficient is not recharacterized as original.

Self-review: passed. Independent audit: not yet performed.
