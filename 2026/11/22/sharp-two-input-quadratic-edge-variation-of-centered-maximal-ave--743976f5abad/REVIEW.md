# Independent mathematical audit

## correctness

PASS

The four counting-ball families have sizes 4,3,3,4. On the nonnegative cone every affine segment of the coordinatewise maximum has a derivative given by one of the 144 row selectors, including segments with persistent ties (tied affine forms along the segment have the same slope). Each selector preserves constants, so its edge-space matrix H acts on the three unconstrained edge coordinates; the step representatives are a right inverse of the edge difference. I independently enumerated all 144 selectors and checked the coefficients of det(tI+216I-144 H^T H) over the rationals: all were nonnegative, with leading coefficient 1. Hence that polynomial has no positive root and symmetry gives 216I-144 H^T H positive semidefinite. The defect is singular only for masks (0,2,2,0) and (3,0,0,3). Integrating edge derivatives gives the stated bound for all pairs, including constant differences. For the frozen positive rational witness, independently evaluated ball averages strictly select (0,2,2,0) at both ends; their output difference is (3,3/2,3/2,0)/100, giving squared ratio 3/2. Replay: python3 /workspace/checks/frozen_exact.py 1. The submitted checker was read, not run. The result does not cover a signed absolute-value-input map or other graph sizes.

## originality

PASS

The checked evidence supports the distinct exact two-input edge-Hilbert coefficient on this particular centered path operator. The identical indexed record is not separate coverage. The near matches change the norm, the graph, or a difference of nonlinear outputs to a single output. This is a qualified assessment, not a priority guarantee.

## value

PASS

Quadratic edge variation is the natural square root of the graph Dirichlet energy. An explicit strictly positive expansion example and a sharp coefficient on the first open path not a star give a usable benchmark for graph-maximal perturbation bounds in that geometry. The extremizing active selector exposes a norm-dependent mechanism distinct from the adjacent-l1 result on the same path. No path-family conclusion or equality classification is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
