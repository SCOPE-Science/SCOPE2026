# Independent mathematical audit

## correctness

PASS

Subtracting subdivision relations gives the stated linear first-difference rule. Subtracting again gives a second-difference transition with l1 column sum bounded q=1/2+4 omega<1; this proves uniform convergence of piecewise-linear refinements for every BV input and the summable variation increment. Interpolation preserves prior nodal values, so polygonal variations are monotone and their limit equals the continuous limit variation (retained-knot lower bound plus lower-semicontinuity upper bound). Translation linearity and jump decomposition give exact sharp norm from the unit jump. The inequality V_(k+1)-V_k<=4 omega W_k and q geometric tail prove a certified finite-to-infinite bracket. Independently computed exact rational levels through k=9 and found V1=5/4, V2=41/32 and consistent convergence; inspected the level-22 exact-integer C++ code and its declared 128-bit cap, but did not re-execute that expensive level-22 calculation.

## originality

PASS

The original four-point scheme, continuity and smoothness are credited to Dyn–Gregory–Levin; the sharp discrete-to-continuous variation operator norm and certified omega=1/16 numeric interval were not found in the inspected author report and nearby later stability literature.

## value

PASS

Exact BV cost of the canonical cubic-reproducing four-point subdivision is a natural invariant for edge-preserving interpolation. The recurrence plus explicit certified tail gives a reusable exact characterization and a narrow rigorous numerical interval unavailable from one or two refinement levels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
