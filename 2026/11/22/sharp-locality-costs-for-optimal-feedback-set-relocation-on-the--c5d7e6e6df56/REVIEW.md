# Independent mathematical audit

## correctness

PASS

The cubic edge count gives 2k=10+e(X)+c for any deletion leaving a nonempty forest, hence k>=6. At size six there are 14 surviving vertices and 12+e(X) surviving edges, so acyclicity is equivalent to having exactly 2-e(X) components. An independent exhaustive calculation used this component-count test on all 38,760 masks, tested state-pair symmetric differences and base adjacency directly, and obtained exact shortest-path layers by bitset frontiers from every state. It reproduces both frozen metric distributions on all 4,088,370 unordered pairs, 2,860 states, 27,780/8,280 edges and eccentricity distributions {6:2860}/{9:520,10:2340}. The surcharge histogram agrees in all seven bins; all 210 maximum pairs have (overlap,jump,slide)=(4,2,8). The Johnson excess maxima and frequencies are 2 on 840 pairs and 6 on 240 pairs. Each move in both displayed witness paths is valid and each path is shortest. The independent check includes these joint and path assertions, rather than inferring them from marginal histograms or presuming the frozen scripts explicitly assert them.

## originality

PASS

The 2,860-state universe is covered and correctly credited, but the compared evidence does not establish prior coverage of the joint optimum-preserving jump/slide metric census or the sharp local-move cost. The available general reconfiguration claims do not imply the two metrics. This is a best-of-knowledge judgment, not a priority certificate.

## value

PASS

The canonical cubic incidence graph is a natural common test case for arbitrary exchanges versus local mobility under minimum cycle-breaking constraints. The exact cost separation includes pairs only two jumps apart but eight slides apart, distinguishes the locality cost from the Johnson lower-bound gap, and gives a reproducible reference for constrained shortest-path algorithms. This is information not provided by the known optimum count alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
