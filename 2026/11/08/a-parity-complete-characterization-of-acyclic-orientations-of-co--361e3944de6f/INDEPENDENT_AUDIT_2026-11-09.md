# Independent mathematical audit

## correctness

PASS

Necessity is parity of total indegree and existence of a source in any DAG. For sufficiency the given safe-source lemma tracks a,b counts of target-even vertices in bipartition and possible sinks of prescribed parity deg mod2. Under necessary conditions q>=1, and a suitable even-target source v can be removed with neighbors toggled while retaining both a possible source and sink; case q>=2 and q=1 with the four part-size parity combinations is checked in the proof. The global parity equation is invariant because removing degree d toggles d neighboring targets. A star is a constructive base case. Repeated re-insertion of a source is acyclic, satisfies all indegree parities, and the scan costs O((m+n)^2+mn). Independently enumerated every orientation for (m,n)=(1,1),(2,2),(2,3),(3,3),(3,4) checking signatures and the criterion; full stored verifier independently treats all m,n<=4 and sampled count profiles to 12, inspected but its logs alone were not used as proof. The orientation number per signature is not claimed.

## originality

PASS

West’s complete bipartite acyclic orientation paper gives alternating-block structural representation and independent-edge statistics, not the image of the parity map. Gravier–Petiteau–Sivignon 2026 discusses parity-constraint acyclic orientation and is highly relevant; full text could not be obtained from arXiv, the lawful OA copy or authorized Oxford (VPN disconnected). Its accessible abstract focuses Cartesian products, cliques and related classes. No decisive stronger K_{m,n} statement identified, so best-of-knowledge PASS with explicit material priority risk, not a false claim that the unread paper excludes coverage.

## value

PASS

Determines the exact feasibility image of the natural indegree-parity map for all complete bicliques, including its unique obstruction, supplies constructive witnesses, and turns an exponential orientation question into a sharp polynomial-time classification. This is a structural parity result, not a renaming of the alternating-block representation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
