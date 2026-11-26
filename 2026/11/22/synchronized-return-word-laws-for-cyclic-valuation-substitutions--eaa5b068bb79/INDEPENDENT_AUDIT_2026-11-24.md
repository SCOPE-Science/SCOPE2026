# Independent mathematical audit

## correctness

PASS

For every integer base, divisibility by powers gives ν_b(b^r t)=r+ν_b(t), so the ordered occurrences of r are the scaled ordered zero-residue set S. Its omissions are isolated multiples of b. Between adjacent multiples of b^r, for a nonzero offset i<b^r, dividing by b^ν_b(i) leaves a nonmultiple of b even after adding the larger multiple. Thus the common interval interior is exactly B_r for composite as well as prime b. A short gap has return rB_r; a long gap has an omitted residue s giving central symbol (r+s) mod q and the two copies of B_r. A site b^s is a witness for each long label s≥1, and b^q and its adjacent integers in S witness short gaps, including b=2. The labels are invariant under scaling. The first b−1 sites in each consecutive base block are in S; the last site has residue 1+u_j mod q. Hence each block contributes b−2 internal short gaps and either one long gap or two short gaps including its outgoing boundary, giving termwise h(u), from the first return onward. Exact valuation strata have densities (b−1)b^(−h−1); contributions beyond level H lie among multiples of b^H, justifying the sum over residue classes. The starting-position density of r is d_r=b^(−r)d_0. The bijection between omitted sites of residue s and long returns of type s gives limiting frequencies d_s/d_0=b^(−s) in the ordered returns (endpoint discrepancies are bounded); the rest is the positive short frequency. The average length is b^r times one plus the long mass, giving 1/d_r. An independently written divisibility-sieve check tested 12 pairs b∈{2,3,4,6}, q=2,3,4: for all 36 letter systems it observed every predicted type, no other type, and agreement with the coded prefix; exact rational reciprocal-density arithmetic was also checked. Replay: python3 -B /workspace/repro/4.py; /workspace/repro/4.log. This corroborates the proof but does not establish the infinite limits.

## originality

PASS

There is exact classical binary overlap and covered arbitrary-base binary gap behavior; neither is the distinct all-b, all-q contribution. The supported contribution is the uniform single-letter full return-word formula, common termwise coded sequence and limiting type law for the general cyclic alphabet and integer base. A same-day all-length binary-base frequency result supplies phase data for return frequencies in that base but not an explicit ordered return system for general b. Priority beyond the inspected sources is unresolved.

## value

PASS

A return-word system is a canonical induced symbolic system, and a full q-letter return classification with a common coded order across all distinguished letters is stronger than a length or frequency count. The long-label refinements, the explicit code and its measure data give a portable exact invariant for this natural substitution family. The contribution is a concise arithmetic classification, not a new general return-word theory or a claim about arbitrary factors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
