# Independent mathematical audit

## correctness

PASS

A mixed factor cannot repeat: two occurrences of an unequal-letter bigram would witness a,b,a,b. The counts of (k−1)-factors minus indegrees and outdegrees prescribe both endpoints of the order-(k−1) factor trail, including when they coincide; descending by factor counts and the prescribed suffix recovers all shorter counts from such a trail. After deleting homogeneous loops a^k, the only repeated vertices are a^{k−1} belonging to two separate runs. Each such run must have length exactly k−1, with no loops, since the multiplicity bound is 2k−2. Any deleted loops accordingly belong to vertices with just one remaining visit. Repeated vertices in the contracted source trail cannot interleave. To verify the step-5 uniqueness hinge, suppose another contracted trail first departs differently at v. The source must have two departures from v, so the rival takes the later one first. No vertex strictly between the two source visits to v occurs outside that interval, as that would interleave with v. Thus the internal vertices of the return segment have no entrance from outside except the bypassed first departure; the only unused incoming edge to v is the return from that segment. After taking the second departure first, the rival cannot get back to use the first, a contradiction. This proves uniqueness of the contracted trail, and the deleted loops restore uniquely at their sole visits. Rivals are not assumed noncrossing; shorter words are immediate from their complete spectra. The sharpness pair has precisely the same one a^k and the same k factors containing the singleton b, with matching (k−1)-suffix, hence identical complete spectra. The block containing 1 leaves j noncrossing subproblems and gives the stated generating function, while injectivity makes the whole source optimal. Independent bounded replay /workspace/branches/98027cd5-fac2-4cb9-aff5-b081fd1f5587/independent_check_record4.py (bounded_check.log beside it) found no collisions in the five tested alphabet/read/length ranges, checked sharpness for k=2 through 8 and counted bounded-block words through n=8. The supplied script was inspected, not executed; its multiplicity filter cannot remove a same-spectrum rival because letter counts are part of the data. Neither enumeration is an unbounded proof.

## originality

PASS

The data model, endpoint identities, general repeat criterion and noncrossing partition enumeration are known ingredients. The closest distinct indexed result is for exactly doubled noncrossing words and directed bigrams. Neither it nor the general antecedents inspected state or directly supply the source-specific sharp 2k−2 cutoff for all k, which uses homogeneous-loop placement as well as noninterleaving. The capacity consequence uses the standard count, not a novel enumeration formula.

## value

PASS

This resolves the exact error-free reconstruction boundary in a natural hereditary word class, including competitors outside that class. A one-unit increase in multiplicity yields collisions for every k. The result also gives a concrete maximum codebook on a natural partition source, with the familiar enumeration becoming its exact size rather than just an upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
