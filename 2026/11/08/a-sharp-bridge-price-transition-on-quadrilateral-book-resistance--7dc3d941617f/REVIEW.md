# Review of the bridge-price transition

## Correctness — PASS

The claim concerns all integers \(m\ge2\), all positive bridge prices \(d\), and all positive budgets \(B\), with independent nonnegative conductances on the stated graph. On connected supports, the trace-inverse objective is strictly convex in individual edge weights, giving uniqueness without an imposed orbit restriction. Page permutation and reflection then give exactly three edge classes. The full Laplacian decomposition yields equation (1) of RESULT.md; differentiating along a feasible budget-preserving direction rules out zero middle-edge conductances. The only remaining complementary-slackness inequality is the bridge derivative, which changes sign exactly at the stated price. The boundary optimization has one positive ratio \(r_m\). The limiting polynomial has a simple positive root, establishing the stated large-page asymptotics. The standalone exact-rational verifier returned `VERIFY_OK 124`; these checks are supplementary to the proof.

## Originality — PASS on inspected evidence, with a stated publication-priority risk

Ghosh--Boyd--Saberi (DOI 10.1137/050645452, full author-posted text, especially the convex program and Sections 4--5) supplies the general optimization and uniqueness framework, but its worked graph families are trees, wheels, and barbells, not the shared-edge quadrilateral book with a separately priced bridge. Liu--Zhang (arXiv:1812.02304, Introduction and Section 3) studies resistance indices for unweighted quadrilateral replacement graphs and does not optimize independently purchasable conductances. Bhoite--Dhuli--Werner--Kansanen (arXiv:2609.29790, Introduction and Section II) designs added edges around a fixed weighted base and imposes an exact edge-count constraint, unlike complete reallocation on the stated edge set. The optimized support boundary and its \(\(1/m\)\) asymptotic are not statements or immediate corollaries of those inspected results. A publication-priority risk remains for unindexed analytic network-design treatments.

## Value — PASS

The sharp threshold gives an economically actionable answer to whether a direct shortcut should be installed at all, while the optimal middle routes remain funded. It also distinguishes three-edge-route systems from lower-depth series--parallel reductions: the global resistance objective counts all intermediate vertex pairs and its optimized price law scales as \(\(1/m\)\). The closed bridge-off solution, exact positive-bridge equations, and asymptotic formula form a natural complete support classification rather than an arbitrary parameter sample.

## Scope and limitations

Path edges have common unit price; the direct edge has separate positive price. The theorem does not cover heterogeneous path-edge prices, a fixed positive base conductance, cardinality-constrained augmentation, or different metrics. General positive-bridge conductances are specified by a unique positive solution of two rational equations rather than closed radicals. A shorter 2006 conference version of the foundational framework has a month-known but day-unverified appearance, whereas the dated 2008 online text has a verified publication day. Independent audit and external priority certification have not been performed.

Self-review: passed. Independent audit: not yet performed.
