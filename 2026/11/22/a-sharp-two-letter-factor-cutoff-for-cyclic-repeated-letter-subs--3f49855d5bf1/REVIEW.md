# Independent mathematical audit

## correctness

PASS

For the one-sided fixed point prolonged at zero and contiguous factors, any constant run lies in one substitution block or crosses only one boundary, since each entire block contains two distinct symbols. It has length at most r+1; the boundary in σ((a−1)a) attains it for every a (all symbols occur, and each consecutive pair needed occurs inside an image). Every factor with at most two symbols and a full block σ(a) uses exactly {a,a+1}. Since q≥3 that set uniquely identifies the source letter for every full aligned block. Hence the number k of full blocks is at most B=r+1. With k≤r the partial fringes have length at most r each, giving |u|≤rB+2r=L−2; with k=B, maximality of the source run means neither neighboring source letter is a, so the only permissible nonempty fringes are the terminal a from σ(a−1) and an initial (a+1)-run from σ(a+1). Their lengths are at most 1 and r. This proves the upper bound and forces the stated E_a at equality, including for q=3. Attainment follows because σ((a−1)a) contains (a−1)a^(r+1)(a+1), whose image supplies the extremal fringes and full blocks. Prefixes of the extremals and the constant-run bound give the complete stated ranges of m(n). All supplied scripts and saved outputs were inspected, not executed. The finite closure script computes 245 length/parameter sets but counts L−1 without an associated assertion (it asserts at the other four selected lengths); no part of the universal proof depends on that printed verification count.

## originality

PASS

Pass concerns the exact support-cardinality cutoff and full list of extremal words for independent q≥3 and r≥2, not introduction of the morphisms, cyclic digit descriptions, elementary pair coverage, or binary Abelian complexity. The closest inspected same-family results do not give this cutoff or classify length-(r+1)(r+2) factors with exactly two symbols.

## value

PASS

The first factor length forcing three letters is a natural local coverage invariant of this cyclic substitution family. The q-independent threshold and complete extremal words are useful beyond a sampled census: they specify exactly when local windows stop behaving as two-letter words and, for q=3, determine the largest gaps in sightings of each letter. A run estimate or general recurrence alone would not determine the unequal fringe contributions or the full extremal list.

The dated certificate retains the supplied scientific assessment, sources and limitations.
