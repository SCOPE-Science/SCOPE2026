# Independent mathematical audit

## correctness

PASS

Rechecked the repaired theorem for each n=2m−1≡1 mod 4, n≥5. Closed neighborhoods of size four force at least m tokens. A constructed word with one adjacent same-row pair and an even number m−1 of color-reversing empty columns attains m. Two tokens in one column spend all excess coverage at once and forbid further tokens in the next two columns on either side. To cover column 2 then requires two more tokens sharing a column, or an already forbidden column for n=5. Thus each occupied column has one token. Each empty column needs opposite row colors in its flanks; the m versus m−1 column counts force exactly one adjacent pair, whose members have the same color. For each of its n positions there are two complementary colorings and a same-support swap cannot connect them. Removing a singleton outside the pair creates two empty–empty edges; filling another column cannot fix both. Removing a pair member forces filling the neighboring empty column, in the row opposite to the departing token. Only these two moves are possible; other empty flanks are unchanged. The left move acts on pair position/color by (i,x)→(i−2, complement x), visiting every column in n steps and reversing the color on return because n is odd. Its inverse is the right move and the orbit has length 2n. Hence there are no slides, and the jump graph is C_(2n), with radius and diameter n. This proof is all-length; the unchanged finite support includes n=5 and 9 checked directly.

## originality

PASS

For the repaired residue n≡1 mod 4 the minimum ordinary state family is not independent, so the exact earlier independent exchange theorem does not transfer. Allagan already provides the count and a close state-word antecedent for this residue; no novelty is assigned to them. The additional exact move classification, exclusion of every slide and proof of a single jump orbit of linear diameter are not stated or supplied by an inspected exchange theorem for these states. The covered classes and the finite triangle case have been removed from the finding, not recast as new.

## value

PASS

At minimum cardinality on a natural cubic family, every placement can be reached from every other with jumps, yet no minimum placement admits even one slide. The proof gives the exact movement cost and its dependence on the exceptional adjacent pair, not just a finite example, an optimum-state count, or a numerical flexibility proxy. This is a useful reconfiguration benchmark in the residue where independent domination does not apply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
