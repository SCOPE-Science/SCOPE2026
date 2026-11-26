# Independent mathematical audit

## correctness

PASS

Canonical restricted-growth generation gives exactly one word per partition, and absence of an alternating quadruple of two distinct block labels is equivalent to noncrossing. Each unknown positional deletion is recanonicalized and repeated outputs are counted once; the unique empty output at n=1 is included. Independently authored code exhausts the disjoint-shadow compatibility graph by inclusion/exclusion with proper coloring as an upper bound on any extension. It checked both displayed witnesses and returned exact M=(1,1,2,3,5,12). On the independently assembled incidence it checked nonnegativity, every rational primal/dual constraint via integer scaling, and objective equality at every length. Weak duality yields P=(1,1,2,3,95/16,32021/2390). At length five the gap is strict but floor(P_5)=5; at six floor(P_6)=13>12. This is a failure of sharpness, not of the validity of the rounded upper bound. Replay: python3 /workspace/branches/e6646979-4962-4482-9e0f-259ef8caba42/independent_check.py --max-n 6; replay_full.log there ends INDEPENDENT_CHECK_OK. The uploaded checker was read, not run. The result is only for the stated class and finite lengths.

## originality

PASS

Best-of-knowledge pass for the exact noncrossing profile and its own separate first strict-gap and first floor-gap lengths. The same channel and the first floor-gap phenomenon in unrestricted set partitions are materially overlapping indexed evidence and not credited as new here. The standard hypergraph formulation and Catalan enumeration likewise are background, not the checked novelty.

## value

PASS

The rounded fractional packing bound is a natural substitute for the exact code maximum. This finite classification distinguishes the first strict relaxation gap from the first rounded bound that is not sharp. At length five rounding still certifies the exact optimum; at length six it allows 13 even though 12 is maximal. Testing the hereditary noncrossing restriction is meaningful because distinct Catalan channels and the unrestricted partition channel have different exact packings. These are first thresholds with exhaustive lower-length checks, not an arbitrary six-point computation or a claimed improvement to the general method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
