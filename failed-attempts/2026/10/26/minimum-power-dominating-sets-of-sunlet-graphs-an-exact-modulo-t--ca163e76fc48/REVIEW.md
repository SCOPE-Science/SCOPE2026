# Independent mathematical audit

## correctness

PASS

A core vertex outside the closed neighborhood of the projected seeds is not observed in the first step and cannot be the first target of a force: each neighboring core lacks an initially observed private leaf and cannot force that leaf while the target remains unobserved. A private leaf cannot deliver a first observation of its own unobserved core. Thus the projection dominates and selecting an optimum all-core domination set attains the bound. At minimum each selected index receives one core/leaf mark. In each length-three gap the internal vertex on a leaf-marked side cannot be observed from the other internal vertex before its own observation, by the same private-leaf obstruction. Therefore a leaf mark between two long gaps blocks, and a length-two gap with two leaf marks blocks if neither end can start propagation from its other side. In an adjacent two-short-gap cluster with three endpoints, an all-leaf assignment is blocked; any core mark starts forcing across the cluster, because it observes an intermediate and a leaf-marked endpoint with one observed core neighbor can force its other one. A length-one gap supplies each of its selected endpoints an already observed neighbor even with two leaf marks. The n=4 case has the same two endpoints on both short gaps and must be counted separately. The resulting admissible counts per pattern are 1 (all long), 3 (one length-two), 4 (one length-one), 7 or 9 (two length-two gaps adjacent or disjoint, k≥3) and 3 for the opposite pair at n=4. Cyclic marking counts adjacent double-short gaps in n ways and disjoint ones in n(k-3)/2, giving the displayed formula. A separate adjacency-set enumeration of all subsets through the claimed minimum for n=3–8 found no smaller successes and recovered 3,22,15,3,77,24. This is corroboration; the gap argument proves all orders. The frozen checker was inspected, not run.

## originality

FAIL

The distinct October 18 Resultary finding 3df9f1b5745a, whose publication date is explicit in its metadata, already counts exactly the same labeled minimum sets for all n≥3, includes n=4, and describes every successful seed placement through gap patterns and explicit permissible leaf positions. It also refines the census by leaf count. The frozen projection-gap representation changes which selected indices define the gaps, but does not classify a new set of objects or give a new invariant.

## value

FAIL

The all-order lowest-degree coefficient and feasible sensor patterns are natural mathematical objects, but already classified. The frozen count is even a sum of an existing finer profile. The alternate cyclic marking is helpful exposition of the same selection patterns and gives no surviving new exact result to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
