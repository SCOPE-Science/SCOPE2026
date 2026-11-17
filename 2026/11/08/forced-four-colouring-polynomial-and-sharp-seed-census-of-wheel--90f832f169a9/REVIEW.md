# Independent mathematical audit

## correctness

PASS

PASS: For any proper 4-coloured wheel, the hub uses one named colour and the rim uses at most the remaining three. If the hub is seeded, a blank rim vertex must have both rim neighbours initially seeded with distinct colours, so blank positions form a good independent set. If the hub is blank, it must be forced first from three distinct initially seeded rim colours. The 12-state (previous colour,current colour,seed bit) transfer enforces exactly these local conditions; inclusion-exclusion over seeded colours enforces hub-first feasibility and the weights p^{n+1-j}r^j and p^{n-j}r^{j+1} are correct. At minimum seed for n>=5, every other rim position is blank, giving two maximum independent sets for even n or n for odd n; seeded constraint graph is C_t and its surjective proper 3-colouring count is Q_t=2^t+2(-1)^t-6*1_even. The n=4 exception includes 96 hub-blank and 48 hub-seeded size-three assignments. Independent direct adjacency-rule enumeration reproduced coefficient distributions n=4,5,6 (including M_4=144, M_5=120, M_6=48). The infinite claim is supported by the complete transfer/construction proof rather than these tests.

## originality

PASS

PASS best-of-knowledge: in the inspected published records no exact wheel-specific four-colour local-forcing transfer and optimum seed census was found. Farr defines the local process and proves general results, not known to imply the wheel structural criterion without new work; inaccessible later full text is a real residual priority risk.

## value

PASS

PASS: A natural full counting polynomial at the graph chromatic palette and a sharp parity-dependent extremal seed census for every wheel size, with a fixed-size transfer matrix and exceptional small boundary, are mathematically useful nontrivial structured enumerations, not a routine substitution of the ordinary chromatic polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
