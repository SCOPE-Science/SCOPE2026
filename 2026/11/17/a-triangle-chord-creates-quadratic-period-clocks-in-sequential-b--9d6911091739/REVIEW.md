# Independent mathematical audit

## correctness

PASS

Explicit upper prefixes T_r and lower blocks B_j form a grid of (beta+1)(beta+2) states plus beta-2 intermediate empty-lower-row states. The stated vertexwise sweep table acts on grid as (p,q)->(p+1,q-1) modulo beta+1,beta+2, except one edge is subdivided by the extra chain. Those moduli are consecutive and coprime, hence grid translation is one cycle of full product order; inserting beta-2 delay states yields beta(beta+4). Independently implemented the local sequential closed-neighborhood sweep and verified every designated state/transition and primitive cycle for beta=2,3,4,5,8,13 (periods 12,21,32,45,96,221), including beta=2 empty-chain boundary. The universal proof is the transition table and coprime translation, not finite enumeration.

## originality

PASS

Kuhlman et al. built long-period unchorded trees under the same (1,3) update; the exact one-edge chorded unicyclic graph and beta(beta+4) clock were not found in primary text or indexed finite tree/cycle classifications.

## value

PASS

A single edge of a classical long-period H-tree creates an exact, all-size quadratic primitive-period construction, answering a motivated edge-perturbation question for a natural deterministic hysteresis rule. The explicit coprime-clock mechanism is useful independently of a full attractor census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
