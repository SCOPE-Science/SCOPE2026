# Independent mathematical audit

## correctness

PASS

With N=q^2+q+1, the retained graph must have >=2N-1 edges, whereas at most 2q selected vertices supply <=2q(q+1). At size 2q+1 both shores are nonempty. All selected points are joined through their connecting lines, and dually all selected lines are joined; the two cores are disjoint unless there is a selected point–line incidence. Thus connectivity is exactly domination plus at least one selected incidence. With a selected points the number of lines met is <=1+aq, so b>=q(q+1-a). If a<=q-1 this exceeds 2q+1-a by at least q-2. The boundary q=2,a=1 forces all four selected lines to avoid that point, violating the incidence condition. Duality forces shore sizes (q+1,q) or (q,q+1). For (q+1,q), at most q points are outside the union of selected lines, since all such points are selected and at least one selected point is covered. The union of q lines has <=q^2+1 points, with equality only for a pencil (automatic for q=2); equality is forced here. The uncovered points are the q points on the omitted line other than the center. Choosing these and any one point of the pencil union dominates both shores and supplies a selected incidence. The pencil determines its center and omitted line uniquely. There are N(q+1)(q^2+1) choices per dual type. Precisely the extra-center choices yield q selected incidence edges (not q independent pairs) and cycle rank zero; off-center choices yield one selected incidence and cycle rank q-1. This checks the exact total and refined counts for all existing planes using only incidence axioms. Both frozen census programs were inspected, not run; COUNTS.txt reports 210 (42 tree) and 1040 (104 tree), matching the formulas for q=2 and 3.

## originality

PASS

The prior ordinary-domination minima and pencil structures are real overlap, and a stronger small-minimal-domination result recovers the weak classification with an extra incidence argument for q>81. The distinct result supported here is the single weak-connectivity characterization and both exact counts for every finite projective plane, including small orders and without restrictions on coordinatization. The regular edge-count lower bound and the spanning-star-tree concept are not new.

## value

PASS

The all-order geometric rigidity and exact optimizer census settle a natural connectivity-constrained covering problem, without coordinatization or a small-plane exception table. The split into tree and cyclic optimizers explains the retained graph structure, not just its count. The value is in the uniform classification and dichotomy, not the elementary edge lower bound or the already-known ordinary pencil sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
