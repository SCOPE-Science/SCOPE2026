# Scientific review

## Correctness — PASS

The finite claim has exact scope: the eighteen-vertex Pappus incidence graph, standard one-attack weak Roman feasibility, and unit-guard reconfiguration restricted to minimum functions. The support criterion in RESULT.md is a necessary and sufficient reduction of the definition. Exhaustive enumeration of every function of weight at most eight establishes the minimum and optimum counts. Independent affine-pair Python and ternary-code C++ implementations agree on \(2691\) optima and the three multiplicities. The affine checker generates all twenty full-automorphism orbits and proves that its group is complete by checking all nine-factorial point permutations; exhaustive shortest-path searches confirm the jump/slide graph data. Both packaged programs executed successfully.

## Originality — PASS (priority not certified)

The 2003 foundational paper and 2014 weak Roman bounds paper do not state this Pappus exact weighted configuration and relocation classification in the inspected materials. Earlier computational work on the same Pappus graph already covers the all-singleton, secure-domination subfamily: \(1755\) configurations, thirteen orbits and their transfer metrics. These are excluded from the novelty assertion. The new classification is the entire weak Roman optimum family, especially \(882+54=936\) mixed-guard optima in seven additional orbits, and the connected transfer graphs on all \(2691\) functions. Full historical publication priority has not been independently established; some potentially relevant records are not fully accessible.

## Value — PASS

This determines a natural optimal-configuration space under a historically motivated guard-defense rule on a canonical symmetric incidence graph. It shows that allowing two guards to occupy a vertex does not improve the minimum weight over secure domination, but substantially expands the optimizer family and changes both exact relocation metrics. The seven mixed-guard symmetry classes and sharp diameters supply precise structural information not provided by the known binary subcase. No infinite-family consequence is claimed or required.

## Evidence and limitations

The proof is an exhaustive finite determination with two distinct implementation strategies, not a sample and not an independent mathematical certification. The all-singleton subcase is prior coverage; inaccessible additional work remains a historical novelty risk. Full reproduction requires only Python 3 standard library and a C++17 compiler.

Self-review: passed. Independent audit: not yet performed.
