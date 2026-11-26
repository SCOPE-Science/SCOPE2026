# Independent mathematical audit

## correctness

PASS

For rotations only, a cyclic word determines one Euler circuit on the labelled k-bit arcs, hence one successor permutation with one full cycle. At each (k−1)-bit suffix v, a local bit selects between the two bijections from 0v,1v to v0,v1; two cycles get two common (k+1)-factors or none at v according to equality of this bit. The constant k-bit states cannot succeed themselves, so the two constant suffix bits are forced and contribute four common factors for k≥2. Single-cycle permutations have the same sign, while each changed bit transposes two successor values. Therefore the number of differing bits is even and I=2^k−2d_H is divisible by four, including the identical-cycle case. Separate reproduction in /workspace/branches/55e54dc1-2e5b-48f1-a1e9-1eeb84cbb9d6/reproduce_order5.py exhausted the 16384 admissible masks, selected exactly 2048 by single-orbit testing, and counted all 2096128 unordered distinct pairs by both mask distance and literal circular factors. Counts at overlaps 4,8,12,16,20,24,28 are respectively 368,27104,254800,710976,758800,305376,38704. The two stated witness words each have 32 distinct circular five-factors, and their six-factor intersection is exactly {000001,011111,100000,111110}, with masks 0x80af and 0xff51. The complement of the 14 free bits is the only possible overlap-four partner; it is valid for 736 cycles. The frozen verifier was inspected, not executed. The computation proves only the order-five census; the universal assertion is analytic and does not claim overlap four is attainable for every order.

## originality

FAIL

The principal exact census is already present in the indexed catalogue in equivalent half-Hamming and cross-join distance coordinates, including the unique opposite partner for the same 736 cycles. The universal congruence is an immediate consequence of the established connected binary cross-join graph (each step toggles two suffix choices), and the four common factors come directly from the unavoidable entrance and exit of the constant states. The sign argument is a concise independent derivation, but does not leave a distinct scientific result for repair. The indexed copies have later path dates; exact mathematical coverage is established, not chronological priority.

## value

FAIL

Six-factor overlap is a natural finite statistic, but the exact order-five fact and best-partner census are an affine relabeling of an available complete table. The general bound and congruence extract a local consequence of the established switch structure without adding a new extremal range or classification. The self-contained formulation is useful exposition, but the submission as a distinct result adds no independently useful unknown invariant or structural fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
