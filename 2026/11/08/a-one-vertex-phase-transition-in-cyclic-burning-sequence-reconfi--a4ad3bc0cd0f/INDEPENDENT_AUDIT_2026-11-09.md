# Independent mathematical audit

## correctness

PASS

PASS. For k>=3 final-time balls have lengths 2k-1,2k-3,...,1 totaling k^2; perfect-square coverage forces a circular disjoint tiling, leaving every source slide invalid. At n=k^2-1 there is exactly one duplicated endpoint and no triple overlaps; center distances ensure strict ignition. For fixed cyclic time-label order there are n*k states (choose defect interface and rotation), exactly two valid nearest-neighbor slides transferring the single overlap to neighboring arc interfaces. Clockwise defect transport moves each arc once per k steps, and after n such rounds winds through all n*k states, establishing one cycle per order, hence (k-1)! copies. k=2 checked separately. Independently enumerated all ordered tuples and legal neighbor slides for k=2,3,4: square 4,18,96 isolates; one-short 6,48,360 states in respectively 1,2,6 cycles, all degree 2.

## originality

PASS

PASS. Important square-order isolation and near-square configuration counts were previously known; a published 2026-10-26 theorem classifies a DIFFERENT exchange graph permitting arbitrary one-coordinate relocation (with (k-2)! components and nonuniform degrees), which does not give the exact restricted one-host-edge source-slide subgraph. The current sharp one-step slide component structure is mathematically distinct and cannot be identified with order-swap burning-schedule reconfiguration on path forests.

## value

PASS

PASS. The exact reconfiguration structure under physically local ignition moves, and its discontinuous transition from isolated optimal schedules to factorially many long cycles on deleting one vertex, is a natural structural question in graph burning. This adds edge-local dynamical information not supplied by the more permissive exchange graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
