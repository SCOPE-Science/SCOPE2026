# Scientific review

## Correctness — PASS
The finite constrained generator is explicitly defined, its reversible ergodic class is identified, and the eliminated eigenvalue equation yields a self-adjoint independent-refresh operator plus a positive rank-one perturbation. The constant test shows exactly one negative direction and min–max bounds the remaining spectrum away from zero for any putative eigenvalue below \(1-\sqrt{1-q}\). Explicit independent leaf-contrast eigenfunctions attain that bound; rank-one interlacing gives multiplicity \(n-1\). The \(n=1\) exception is computed separately. See `RESULT.md` for full quantifiers. Exact finite-state and independent numerical computations in `verify.py` passed.

## Originality — PASS on examined evidence; historical priority not certified
Fredrickson and Andersen (1984) introduced the facilitated-spin setting. Cancrini et al. (2006) prove scaling and lattice results, whereas Cancrini et al. (2007), Section 6, establish general-graph lower comparison bounds for the same nonempty-vacancy class. Shapira (2020) establishes upper bounds for other graph regimes. Section 6 of the 2007 full manuscript was read and compared specifically: its generality does not imply the sharp algebraic constant or \(n-1\) eigenmode multiplicity. Focused published-result searches and semantic research-record queries found no equivalent star formula. Residual risk: an earlier differently titled exact star calculation remains possible; the original 1984 paper was available only at abstract level in the inspected source.

## Mathematical value — PASS
The degree-independent exact rate sharply separates vacancy-controlled slow relaxation from graph-size growth on a natural high-degree family. It exposes an explicit \(n-1\)-dimensional leaf-contrast bottleneck despite all leaf dynamics being blocked whenever the hub is filled, and determines the unique order-two onset of this mechanism. This is stronger than generic positive-gap or scaling bounds, without asserting a full spectrum or a total-variation cutoff.

## Limits
The problem is finite-state and specialized to unit-rate FA-1f heat-bath rules. It does not resolve high-dimensional lattice exponents, other kinetic constraints, arbitrary star edge weights, or historical priority beyond the sources examined.

Self-review: passed. Independent audit: not yet performed.
