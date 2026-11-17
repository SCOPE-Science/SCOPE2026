# Scientific review

## Correctness — PASS

The update formula matches elementary Rule 18 (`001` and `100` produce a one). The temporal-history graph enforces every cell at each of the temporal slices, with correct cyclic time and cyclic spatial closures. The bitwise generator is obtained algebraically by solving the local constraint at all bits. A complete SCC decomposition finds no nonzero recurrent component for temporal heights 1, 3, 5, 7, and 9; hence the universal exclusion holds for any circumference. Direct complete-state enumeration for ring sizes 3 through 11 establishes the small-ring cutoff and exactly two primitive temporal eleven-orbits. The entire supporting proof and deterministic programs are embedded. No observation from a finite sample is extrapolated to all ring lengths.

## Originality — PASS (qualified)

The directly relevant primary works are Wolfram (1983), Hanson–Crutchfield (1991), and Sabrié–Törmä (2023 preprint/2026 article). Their detailed studied objects are domain/kink dynamics, statistically regular attractors, and limit sets; none of the inspected relevant passages supplies the five-height no-return theorem or the sharp eleven-site first occurrence. Previously catalogued Rule 18 one-step images, predecessor counts and temporal period two address different dynamical predicates. Searches for eleven-period Rule 18, minimum nontrivial odd temporal period, and short odd return exclusions did not locate an implication-equivalent complete result. A finite-period thesis table could not be inspected in full; historical priority cannot be certified, and that is a specific remaining risk.

## Mathematical value — PASS

Rule 18 is a canonical nonlinear cellular automaton whose quasi-linear regular domains and persistent kinks have a substantial literature. Whether those dynamics permit any nontrivial *odd* closed time orbit, and when one first appears, is a natural parity-sensitive recurrence question. The global absence of four successive odd periods across every ring, plus a sharp first temporal and spatial eleven-site onset and an exact orbit multiplicity, identifies a genuine boundary that is not a routine numerical extension of the temporal-two census. It is deliberately narrower than a full period-spectrum classification.

## Closest literature and remaining limitations

Wolfram's Rule 18/Rule 90 domain correspondence does not control all spatially periodic kink configurations. Hanson and Crutchfield explicitly allow spatially periodic exceptional states outside dominant regular-domain attraction, without their exact first odd-period census. Sabrié and Törmä address topological limit sets, not exact finite-ring short-time periodic points. A source potentially carrying older finite-period tables was inaccessible; an independent historical survey may find previous numerical examples. The period-eleven count is established only at eleven sites, while the absence for shorter odd periods is universal.

Self-review: passed. Independent audit: not yet performed.
