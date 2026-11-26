# Independent mathematical audit

## correctness

PASS

The actual model is the product-Bernoulli transition with unbiased empty-state reset, and the specified path α_v=(1−εg_v)a_v, β_v=(1−εg_v)b_v, γ_v=εg_v has strictly interior bit probabilities at positive ε. At zero quality, from a state with both channels present every bit is interior, giving positive one-step access to either monopoly. From a nonempty one-channel state the tendency of every incumbent bit is at least b_v and absent-channel bits stay zero, so access to the incumbent monopoly is positive. The all-empty state also has positive access to both. This independently establishes transience of every other state on the fixed finite space. In block notation (monopolies/transient), the exact trace kernel on the two monopolies is W_MM+W_MT(I−W_TT)^{-1}W_TM. Polynomial dependence on ε and a bounded inverse at zero give transient stationary mass O(ε) and off-diagonal trace terms ε[Aq_2+B(1−q_1)]+O(ε²) and its relabeling. Only one-bit departures occur at order ε, and all newcomer states can reach the rival monopoly in one step, so A>0. Before blackout a missing incumbent set U can only propagate to a subset of {v: some w in U has P_vw>0}. Choosing the entire set has positive probability because permissible zeros are strictly possible and all incumbent ones have probability ≥b_v. The maximal t-fold image from {w} is the support of column w of P^t. It stays inside one cyclic class for period >1, while primitivity makes that column all positive at some t; the empty-state reset then gives positive access to the rival monopoly. This proves B=0 precisely for period >1, for a single dropout in the zero-quality excursion, not for arbitrary initial states or all finite-ε transitions. Subtracting proportional weights gives the displayed numerator B(q_1−q_2)(q_1+q_2−1), with positive denominator. For undirected loopless connected supports, period two is equivalent to bipartiteness. Exact finite replay: enumerate six bits for the three-user path and triangle, multiply the six conditional Bernoulli probabilities, and solve the 62 transient rows of (I−Q_0)h=W_T,m2 over rationals; then sum the specified newborn/dropout entries. Path B=0 and p_1=4/7; triangle A=12409127317/21043306475, B=3/470 and p_1=99810294446/174533696303, with zero exact hitting-equation residual. A 90-digit positive-ε solve at 10^{−5} gives triangle monopoly mass 0.5718195152391303… and transient mass 0.000113217711642346…, validating the frozen approximation at about eleven decimal places for the former (its extra digits differ by about 4.96×10^{−12}). The packaged float checker was read, not executed. No finite example substitutes for the graph-period proof; none of the limits is stated uniformly in n.

## originality

PASS

The source process, zero-quality absorption, hitting-probability representations, small-quality monopoly concentration and generic trace-chain methods are prior. The surviving claim is the computed limiting relative weights and the precise identification of the dropout contribution with matrix primitivity, giving the quality-sum sign change. The primary 2026 paper and the highly relevant 2025 thesis were compared at their zero- and low-quality sections; neither inspected treatment supplies that characterization. One peripheral reference in the frozen record has incorrect attribution/title (details below); the core comparison with the correct primary model is unaffected.

## value

PASS

The result resolves relative monopoly occupation where the source only proves concentration. It gives a natural graph classification and a signed, testable mathematical departure from quality-proportional weights. The positive dropout effect and its vanishing on periodic supports explain why the network can matter even when an arbitrarily small quality weight is the only perturbation. No empirical validity is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
