# Independent mathematical audit

## correctness

PASS

The standard Type-A pairwise criterion identifies graph edges with unique alternating phase toggles over the first-to-last differing interval. An interval pair yields another graph edge only if it shares one endpoint with free ends separated by at least two, or forms two adjacent disjoint intervals with an equal-symbol join and common unordered symbol pair. Pairwise constraints force one common-endpoint pencil, or two pencils straddling an equal-symbol boundary; the latter intervals cannot bridge that boundary because it would break alternation. The one/two-pencil free-endpoint packing gives at most floor(n/2) neighbors in a clique, and toggling even-length prefixes of a binary alternating base word attains floor(n/2)+1 for every q>=2. Independently enumerated all one-deletion balls and computed max cliques for (q,n)=(2,2),(2,4),(2,6),(3,4), agreeing with theorem; these finite tests are not its infinite proof.

## originality

PASS

PASS on best-of-knowledge inspected sources. Cai et al establish exactly the Type-A pairwise adjacency description which this theorem uses, not a global clique-family dichotomy. The Chrisnata–Kiah–Yaakobi 2022 paper constructs certain binary cliques in blocks of length 2ell but its inspected Lemma 7 does not give the universal upper bound, alphabet independence, or one/two-pencil classification. Published Resultary edge- and triangle-count results concern totals, not arbitrary clique extremality. No broader covering theorem was observed in actual targeted searches.

## value

PASS

PASS. Clique size is a canonical obstruction for placing multiple source words in a two-read reconstruction code; exact sharp order for every alphabet and length together with classification of all possible cliques is useful structural coding information. The two-pencil dichotomy is a nontrivial geometric restriction not determined by local degree, edge counts, or isolated constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
