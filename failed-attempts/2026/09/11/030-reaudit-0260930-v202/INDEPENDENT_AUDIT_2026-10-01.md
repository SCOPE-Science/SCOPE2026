# Independent mathematical audit — SCOPE-20260911-030

Audit date: 2026-10-01 (UTC) UTC

## Final disposition

**failed**

## Correctness — PASS

A fresh independent implementation of the Fomin-Zelevinsky B/C mutation rule reproduced the green/red status sequence GGGG -> GRGG -> GRGR -> GGRR -> RGRG -> RRRG -> RRRR for w=(2,4,3,1,2,4), with terminal C columns (-e4,-e3,-e2,-e1). Thus every mutation is green and the terminal framed seed is all-red. This establishes the stated length-6 maximal green sequence for the named seed.

## Originality — PASS

No source located gives this exact quiver/word. Lawson-Mills covers minimal mutation-infinite quivers, while the record’s quiver is explicitly non-minimal; Muller shows MGS existence is not mutation invariant. published-finding corpus and direct searches returned the exact SCOPE record but no prior exact word.

### Equivalent formulations

An equivalent formulation is an all-green path to an all-red seed; no prior path for this seed was found.

### Broader coverage

Those theorems do not cover this non-minimal member.

### Exact database or table

The database inventory does not imply the exhibited word.

### Claim versus prior implication

The explicit word is not a corollary of the cited existence theorems.

## Scientific value — FAIL

The result is one short certificate for one database-selected rank-4 seed. It supplies no classification, obstruction boundary, family theorem, or mathematical reason that this exact seed/length is independently significant; the depth-5 minimality check is expressly secondary and not part of the claim. Under the shared bar, correctness and novelty of an isolated computational witness do not by themselves establish scientific value.

## Sources and residual risk

Checked sources: published-finding corpus exact query; Lawson-Mills arXiv:1610.08333; Muller arXiv:1503.04675; Quiver Mutation Database reference.

Residual risks: The database or an unindexed computation could contain the same word without searchable prose..
