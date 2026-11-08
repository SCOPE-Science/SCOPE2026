# Self-review: free degree-nine cubic–line arrangements

## Correctness — PASS

The theorem's quantifiers require a reduced complex projective divisor made of distinct smooth cubics and lines, total degree nine, exclusively \(A_1\), \(D_4\), and two-branch \(A_5\) singularities, and freeness. The proof first obtains the published minimal-syzygy-degree bound \(\operatorname{mdr}\ge4\) and hence the only free exponent pair \((4,4)\), giving \(\tau=48\). Its Bézout and Tjurina identities were reconstructed independently from the local intersection and Tjurina contributions. An order-three cubic–line contact consumes the entire cubic–line Bézout number and excludes any other point on that line–cubic pair. This geometric fact is used explicitly when bounding triple-point types; it is not inferred from a program's output.

For one cubic and six lines, only \(t_5=4,5,6\) are possible; the bound \(n_3\le4+\binom{6-t_5}{2}\) excludes the first two. The third violates Talar's published orbifold inequality. For two cubics and three lines, \(t_5\in\{8,9\}\). The first implies at most one ordinary triple point, contradicting the required two; the latter forces the unique necessary profile. The standalone enumeration of the arithmetic cases successfully reproduced these alternatives. All boundary configurations with line concurrence or shared tangency are covered by the allowed-singularity hypotheses. No existence of the surviving arrangement was proved or assumed.

Critical external inputs: Talar (arXiv:2305.01530), Theorems 2.2 and 3.1, and the standard free-curve Tjurina formula cited there. These are appropriate under the stated hypotheses. Direct exact arithmetic checks are reproducible using `python3 verify_profiles.py`; they do not certify the geometric or published theorems independently.

## Originality — PASS, subject to remaining priority risk

Closest source: P. Talar, *On cubic-line arrangements with simple singularities* (original arXiv version 2023-05-02; journal version 2024). The paper's Section 3 explicitly isolates four possible degree-nine weak combinatorics and says it does not decide geometric realizability. The present implication is strictly stronger: three of those four numerical candidates cannot be geometrically realized by free arrangements with the stated singularities. The extra step is the line–cubic flex-consumption and ordinary-triple incidence argument, not a reformulation of the same numeric bounds.

Dimca–Ilardi–Pokora–Sticlaru study adding inflectional tangent lines to obtain free curves and do not give this degree-nine necessary-profile elimination. Bannai–Guerville-Ballé–Shirane–Tokunaga study the topology of one cubic with up to six inflectional tangents and distinguish Zariski pairs; this does not imply the degree-nine freeness obstruction under the present singularity list. Comparisons with conic–line free/near-free records do not dominate a one-/two-cubic theorem. Targeted source, claim, parameter, and possible-equivalence searches did not locate covering statements. The absence of a search hit is not proof of priority: an unindexed paper or an implicit combination of standard geometric lemmas remains a risk.

## Mathematical value — PASS

The result eliminates the entire degree-nine one-cubic/six-line case and reduces a prominent unresolved four-profile geometric realization problem to one highly rigid profile. Its structural conclusion identifies all nine possible \(A_5\) contacts and requires all three lines to be common flex tangents of two smooth cubics. This is a motivated obstruction at the upper degree bound for free cubic–line arrangements, not an arbitrary choice of coefficients or a table recomputation. Completion of the remaining existence question is explicitly left open.

## Scope and review limits

The conclusion is necessary only, restricted to complex reduced divisors with the specified smooth components and singularities. It does not resolve existence of the last profile, nor does it include higher-order singularities, non-free/near-free arrangements, or positive-characteristic variants. No independent mathematical audit or validation has been performed; the review is a self-review, and an additional historical-priority check would be useful.

Self-review: passed. Independent audit: not yet performed.
