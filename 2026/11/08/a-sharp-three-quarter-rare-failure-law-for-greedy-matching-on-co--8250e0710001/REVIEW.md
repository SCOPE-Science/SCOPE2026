# Scientific review

## Correctness: PASS

The stated object is precisely the uniform-feasible-edge random greedy matching on \(K_{2n}\setminus M_n\), for integer \(n\ge2\). Because every nonedge is one deleted pair and the remaining vertex set is even, only a complete matching or a maximal matching leaving one intact deleted pair can result. The state \((m,f)\) suffices for exact transitions. The coefficients \(\binom{2(m-f)}2\), \(4f(m-f)\), and \(2f(f-1)\) sum to \(m(2m-1)-f\), with indicated changes of intact-pair count. The proof's one-pair survival equation and telescoping first moment are checked algebraically; two-pair survival bounds the needed factorial moment without assuming pair independence. The positive polynomial \(4(m-2)^4+26(m-2)^3+54(m-2)^2+39(m-2)+4\) proves the key universal comparison. The finite-sample bound and \(3/4\) limit follow from a harmonic sum. Exact labeled process enumeration and 4,287 checker assertions were replayed. These finite checks are supporting evidence, not the proof of asymptotic quantifiers.

## Originality: PASS (qualified)

Dyer–Frieze's 1991 work studies precisely the random-feasible-edge algorithm on fixed graphs, but accessible abstract and supporting sources emphasize worst-case and sparse/forest approximation guarantees. Its full text remained inaccessible, so unconfirmed historical coverage is an explicit residual risk. Arnosti's full paper studies the same algorithm on *random bipartite inputs*, not the fixed dense nonbipartite cocktail-party family. Glebov–Luria–Simkin study the reverse process of *adding* random edges to regular bipartite graphs; Bennett–Bohman give broad unmatched-vertex bounds in random greedy hypergraph matching, too coarse to imply a sharp order-\(1/n\) failure probability and constant. No matching statement or stronger implication appeared in searches of the public mathematical research index for the process, graph aliases, rare-event asymptotics and exact recurrence, or in recoverable earlier claims checked for overlap. The positive evidence establishes a distinct stated specialization, but search failures do not certify historical novelty and the 1991 unread work remains a priority risk.

## Value: PASS

For a dense graph of degree \(2n-2\), maximal greedy matching is automatically within one edge of optimal; approximation ratio alone conceals the failure risk. The exact probability of that sole possible error is natural for evaluating reliability, and its leading \(3/4\) constant is nontrivially different from the \(1/2\) leading constant for an unbiased terminal pair. The exact finite recurrence and explicit uniform-in-\(n\) quantitative error make the fact useful both for finite performance calculation and asymptotic benchmark comparisons. It is not merely a renaming of a generic bound, a known table lookup, or an arbitrary parameter slice.

## Closest literature and limitations

- Dyer and Frieze, *Randomized greedy matching* (1991), DOI 10.1002/rsa.3240020104: exact algorithm, full text inaccessible; cannot rule out an unstated covering example or lemma.
- Arnosti, *Greedy Matching in Bipartite Random Graphs* (2021 first online), DOI 10.1287/stsy.2021.0082: algorithm taxonomy, different random-bipartite scope; full publicly accessible PDF introduction, model definitions, main results and discussion inspected.
- Glebov, Luria and Simkin, *Perfect Matchings in Random Subgraphs of Regular Bipartite Graphs* (arXiv v1 2018-05-17): random edge-addition hitting time, different process; primary text inspected.
- Bennett and Bohman, *A natural barrier in random greedy hypergraph matching* (arXiv 2012): general random greedy bounds, different precision and hypotheses; source inspected.

Second-order sharpness, other dense graph families, and independent audit are not claimed.

Self-review: passed. Independent audit: not yet performed.
