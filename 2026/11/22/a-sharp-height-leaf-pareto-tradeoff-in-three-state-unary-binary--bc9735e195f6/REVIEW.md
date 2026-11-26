# Independent mathematical audit

## correctness

PASS

Independent leaf assignments make the set images of compositions exact. The proof as written gives an insufficient reason for the small Pareto rectangle: bounds on the two separate minima do not, by themselves, certify bounds on all nondominated pairs. The census itself is correct. Indeed, from any synchronizing term choose a synchronizing term with no larger height or leaf count and with the fewest nodes subject to those two bounds. It has no proper singleton-image subtree (that subtree could replace the whole term) and no repeated image along a root-to-leaf path (the lower subtree could replace the upper one without changing the image or increasing either cost). Thus on that path there is at most one root singleton and the four nonsingleton images, including Q at the leaf: height at most four and hence at most sixteen leaves. A separate exact recurrence enumerated all 531441 operation tables for exact leaf counts 1 through 16 without bounding height. With one leaf it closes Q under shortest unary paths; with more leaves it combines every ordered split and images at a binary root with height 1 plus the greater child height, then closes under all unary paths. This is exhaustive because stripping the leading unary chain leaves either a leaf or a binary root. Scanning leaves in increasing order and keeping only strict decreases in optimal height gives the true frontier. The run reproduced both full histograms, 242997 synchronizing, 288444 nonsynchronizing, 8712 at min height four (5220 at min leaves three and 3492 at four), and exactly 18 and 180 two-point frontiers of the stated kinds. No additional points occur outside the small rectangle. The two frozen outputs also suffice jointly: bounded and unrestricted feasible-machine counts coincide, and bounded per-machine minima can only increase; equality of the summed height and leaf minima over all machines forces equality individually. Thus a minimizer for each coordinate exists inside the rectangle and dominates any point outside on the corresponding excessive coordinate. For the explicit witness, u(Q)={1,2}, B({1,2},{1,2})={0,2}, B({0,2},{0,2})={0}, and U(B(Q,{0,2}))={2}; at height at most three the first singleton costs four leaves, while with at most two leaves only Q and {1,2},{0,2} are attainable at any height. On two states without a constant basic operation the images all stay equal to Q; a constant unary gives the optimum (1,1), and with only a constant binary there is no one-leaf synchronizer and (1,2) dominates. This verifies the first state-size boundary.

## originality

PASS

Best of checked evidence for the exact joint leaf/height frontier census and first-size conflict. The known single-objective height upper bound is credited rather than treated as new. In the closest published primary and indexed comparisons, neither minimum leaf count nor incompatibility of the two minima is determined for this class.

## value

PASS

The ranked signature is the smallest natural one that allows both branching and unary compression, and three states are the first size permitting a conflict. The comparison addresses two genuinely different resources of a synchronizing term, depth and number of independent inputs. The nontrivial height-three versus height-four witness and exact frequency of both types determine when a shortest term cannot also use the fewest leaves; a universal height bound or a count of synchronizing machines alone cannot answer that question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
