# Independent mathematical audit

## correctness

PASS

The graph automorphism group has exactly eight leader-pair orbits; the unmodified biclique inverse follows from a 2-block Schur complement and deleting one edge is a grounded rank-one Sherman–Morrison correction. Inspected verify.py recomputes all eight exact rational polynomials from the source formulas.json, proves positivity using shifted polynomial coefficient certificates on p>=6,q>=p and the complete p=3/4/5 unbounded strips, and checks all six remaining integer cases. Independent exact grounded Laplacian inverses for (3,3),(3,6),(3,7),(4,4),(4,5),(5,5),(5,6),(6,6),(6,7) matched the claimed optimizer classes and normalized trace (no factor of 1/2). Thus the infinite-domain proof uses symbolic sign certificates, not finite-size extrapolation.

## originality

PASS

The October 25 prior theorem directly covers exactly the balanced diagonal p=q, including threshold n=6 and all balanced equality sets: this part is NOT new. Its proof and hypotheses restrict it to K_{n,n} and cannot imply the asymmetric p<q transition. The independent infinite-strip classification at p=3 q>=7, p=4 q>=5, p=5 q>=6, and general p<q goes beyond this prior; neither intact-biclique leader allocation nor single-chord biclique results imply the deleted-cross-edge problem. Best-of-knowledge pass for the unbalanced extension; older nonindexed exact biclique-specialized results remain a risk.

## value

PASS

Changing community sizes and deleting a single edge creates the natural competing defect-endpoint versus ordinary-side placement regimes; classifying all optimal pairs and exact error values throughout two unbounded part-size parameters is a useful nontrivial structural robustness/leader-allocation theorem. New unbalanced regimes are not mechanically implied by balanced results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
