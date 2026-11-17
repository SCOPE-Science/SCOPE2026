# Review of the finite-path first-collision theorem

## Correctness

**PASS.** The proof derives a sharp extinction bound from nonbacktracking excitation ancestry on a path, identifies the only possible terminal-wave endpoints, and gives a necessary-and-sufficient local criterion at the first critical refractory threshold. The only obstruction to a complete right-going front is a second initial excitation at the target endpoint together with a resting adjacent site; counting this excluded class yields the full bivariate polynomial. The left-going class is disjoint and obtained by reflection. Python exhaustive calculations check the full two-variable coefficient census for lengths four through seven; independently written C++ exhaustively checks extinction and one/two-excitation populations through length eight. The finite results support, but are not substituted for, the all-length proof.

## Originality

**PASS, with historical priority risks.** The closest prior one-dimensional work, Fisch and Gravner (1995), Section 5, explicitly defines noninteracting percolating paths only up to the number of colors and discusses possible edge collisions. It does not state the first-beyond-length finite open-path obstruction count or its initially refractory/two-source generating polynomial. A separate three-state finite-path terminal-shell result treats fixed palette size three; the claimed infinite family has palette size at least four and grows with the path length. The general 1993 Greenberg–Hastings preprint supplies the model and infinite-lattice context without an identified finite-path enumeration. The first-front product was already implicit in earlier work and is not asserted as new.

The published summary of the closest three-state finite-path result was available, but its full document was not inspected. Earlier unindexed finite-interval literature may narrow priority; no uniqueness guarantee follows from database searches.

## Value

**PASS.** The critical relation \(q=n-1\) is the first graph length at which an excitation can recover at the opposite endpoint exactly when a maximal front arrives. The theorem gives the exact deficit from the classical unopposed percolating-path count, resolves which two-source configurations survive, and refines the result by the number of initially refractory sites. The bivariate polynomial makes the collision mechanism a countable structural boundary, not a numerical increment or arbitrary small graph census.

## Limits and closest literature

The result concerns labelled open paths, threshold-one synchronous dynamics, and the first color/length collision threshold only. It does not settle subsequent collision regimes or any periodic-boundary model. The older general methods may enable alternative derivations of its formula, and no independent audit has been completed.

Self-review: passed. Independent audit: not yet performed.
