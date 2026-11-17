# Independent mathematical audit

## correctness

PASS

For odd n>=5 symmetric LV cycle, smallest cycle-adjacency eigenvalue is -2cos(pi/n); full positive coexistence uniquely stable for 0<alpha<a_n. In next open window a_n<alpha<a_{n-2}, all extinct sites must be isolated by invasion, odd surviving runs cannot be internally stable for alpha>1/2, and even surviving paths are stable only below their adjacency eigenvalue thresholds. Solving their endpoint recurrence yields alpha e_r=sin(r theta/2)/(sin(r theta/2)+sin((r+2)theta/2)), theta=arccos(1/(2alpha)). The sine product inequality prevents two even runs adjoining one extinct site; singleton-even-run invasion inequality alpha(e_r+1)>1 iff (r+3)theta>pi forces r=n-3. Thus exactly n rotations of one singleton plus one n-3 path with two isolated extinct sites are hyperbolic stable. Summing path equations yields B=1+(n-3+2alpha e)/(1+2alpha) and B-n/(1+2alpha)=2(alpha(1+e)-1)/(1+2alpha)>0. Endpoints unclassified.

## originality

PASS

The odd-cycle Fourier eigenvalue and path stability thresholds are standard prior spectral facts. To infer exact n equilibria, one additionally needs the invasion inequalities for two adjacent even runs and singleton/even-run endpoints. Neither the general antichain bound nor existence of locally feasible chains determines these global tests. Marcus–Turner–Bunin give exact intrinsic allowable-path thresholds in sparse graphs and study typical random large ecosystems, but explicitly distinguish local feasibility from global uninvadability; Hong–Pego give general exclusion and antichain multiplicity bounds, not exact first-window support enumeration of a fixed odd cycle. These earlier general results do not entail the submitted n-support theorem.

## value

PASS

Solves a natural full-graph stability and invasion question at the first Fourier instability of odd symmetric competitive cycles, giving exact n stable communities, support shapes, and biomass tradeoff for all odd sizes. This fills the global coexistence-versus-exclusion classification beyond known local chain feasibility cutoffs and is relevant to spatial ecological symmetry breaking.

The dated certificate retains the supplied scientific assessment, sources and limitations.
