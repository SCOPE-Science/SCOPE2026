# Independent mathematical audit

## correctness

PASS

On Petersen KG(5,2), edges correspond to ten two-subsets of five elements and strict-majority neighbours are the three disjoint subsets, giving an exact 2^10-state map T. Actual checker check_petersen.py exhaustively determines T^6=T^4 and T^5≠T^3, recurrent set size124 with 14 fixed symbols and 55 two-cycle orbits; inverse T4 fibers have multiplicities 72 of size1, 50 of size10, two of size226, with check 72+500+452=1024. Independently reconstructed all Petersen masks and verified both iterate identities, fixed counts and full weight histogram; group orbit reduction covers all 34 isomorphism classes under S5. For the bipartite double GP(10,3), F(x,y)=(T(y),T(x)); on recurrent symbols R, T^2=I, so F conjugates to the swap on R×R, giving 124 fixed and C(124,2)=7626 primitive two-cycles. Fiber weights w are T-invariant and imply per-fixed basin w^2, per-two-orbit basin 2ww'. Direct independent cross-products of weights reproduce nine orbit classes fixed (1:72, 100:50, 51076:2), period-two (2:2556,20:3600,200:1225,452:144,4520:100,102152:1), with populations 107224+941352=1048576. Original check_desargues.cpp independently enumerates full 2^20-labelled functional graph using GP(10,3) edges and indegree pruning; its algorithm and expected counts were inspected. Exact first-entry table max t4 and sharp witness follow T^6=T^4≠T^3; finite enumeration is exhaustive for exactly specified graph, not infinite extrapolation.

## originality

PASS

QUALIFIED PASS only for genuinely surviving full Petersen fiber/orbit and nine-class Desargues per-orbit basin spectrum, not the already published Desargues recurrent counts, entry-time table or aggregate basin totals. Read full same-day Resultary source and explicitly delimit its dominant overlap. The weight histogram and lifted individual basin classification constitute a complete natural finer invariant, although their derivability by finite enumeration from the older shore maps is a real residual risk; global priority not certified.

## value

PASS

Petersen and Desargues are canonical cubic symmetric graphs, and the bipartite Petersen double is the natural incidence geometry of the Desargues graph. The three exact inverse-fiber weights 1/10/226 identify sharply unequal attraction among 124 recurrent symbols; their pair products yield a complete nine-class orbit-level basin spectrum, including 2,556 isolated temporal two-orbits and a unique orbit attracting 102,152 states. Although an earlier source already supplies aggregate Desargues dynamics, the exact fine basin hierarchy and Petersen 34-isomorphism-class explanation are motivated complete finite invariants, not just arbitrary sampled small graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
