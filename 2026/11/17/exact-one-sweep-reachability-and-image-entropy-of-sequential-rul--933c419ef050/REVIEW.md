# Scientific review

## Correctness — PASS

The scan is defined on labelled cyclic binary words, and the local truth table is \(f(l,c,r)=l\oplus(c\lor r)\). The three exact scan equations reduce interior target differences to Boolean OR constraints and supply a necessary-and-sufficient endpoint test, including the scan seam. Every passing test gives a concrete predecessor. The 12 relation states and all binary transitions are fully displayed in `RESULT.md`. Their exact vector identity \(T^2(T^3-2T^2+T-I)w=0\), reproduced with standard-library integer arithmetic, proves the recurrence for every ring length; the four base cases give the rational series. Pole analysis gives the entropy law. Independent direct simulation covers all inputs through length 16, including complete constructive inversion for lengths 3–12. The finite tests are not used as a substitute for the all-length proof.

## Originality — PASS, with historical-priority risk

The 1983 source establishing classical Rule 30 uses simultaneous updates, and its cyclic image is a different global function. The 2007 work on asynchronous cellular automata investigates update-order independence of periodic sets, which is logically different from determining the one-sweep image and its cardinality under one fixed scan. The 2025 work on multiway sequential cellular automata illustrates Rule 30 but mainly investigates a different small-system, multi-branch family; the inspected parts do not state an all-length left-to-right image language. A public synchronous Rule 30 image enumeration and public synchronous predecessor-multiplicity enumeration similarly address different maps. The sequential Rule 184 one-sweep image formula has a coincident growth denominator but different coefficients; its proof does not imply the present Rule 30 predecessor test. An older article or unindexed thesis on deterministic asynchronous Rule 30 might establish the same image distribution; priority is not independently certified.

## Mathematical value — PASS

Rule 30 is a canonical nonlinear elementary cellular automaton, and its fixed-order sequential map differs substantially from the usual simultaneous map. Exact single-sweep reachability measures which information has already been lost after one finite global operation, a natural dynamical invariant. The constructive predecessor criterion resolves every output, including subtle distinguished-seam constraints; the all-circumference rational enumeration and entropy characterize the full size dependence. This is more than a small computed table or renamed synchronous theorem. It deliberately does not assert further dynamics or downstream consequences.

## Closest literature and limits

- S. Wolfram, *Statistical Mechanics of Cellular Automata*, Reviews of Modern Physics **55** (1983), 601–644. https://doi.org/10.1103/RevModPhys.55.601.
- M. Macauley, J. McCammond and H. S. Mortveit, *Order Independence in Asynchronous Cellular Automata*, arXiv:0707.2360 (2007). https://arxiv.org/abs/0707.2360.
- M. H. Wong, *Multiway Sequential Cellular Automata*, Complex Systems **34** (2025), 325–372. https://doi.org/10.25088/ComplexSystems.34.3.325.
- *Exact periodic image law for elementary cellular automaton Rule 30*, public mathematics record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-periodic-image-law-for-elementary-cellular-automaton-rule--3077d0947284. Its claim is about simultaneous Rule 30.

The verification programs use no independent formal theorem prover. Third-party mathematical verification and archival-priority investigation remain incomplete.

Self-review: passed. Independent audit: not yet performed.
