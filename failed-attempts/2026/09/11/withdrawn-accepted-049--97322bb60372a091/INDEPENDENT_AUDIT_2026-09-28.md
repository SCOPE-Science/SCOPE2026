# Independent Audit — 2026/09/11/049

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `54098baac50c3c4b73fc5c58e82e732cc5ae0e1a`  
**Disposition:** **FAILED**

## Correctness

For the literal full tangent bundle, the dimension count is correct. The universal hypersurface has dimension N_d+3, a smooth vertical 2-jet contributes two additional 3-dimensional derivative levels, and T_{J_2^v} therefore has rank N_d+9. Fifteen individual sections cannot span a rank at least 23 fibre when d>=2. The explicit d=2 affine-chart point has three independent jet-equation differentials, giving the stated tangent dimension. The principal-locus observation is also correct componentwise: a nonzero, nonunit principal equation on a regular component cuts codimension one, not codimension at least two.

## Originality

The headline combines two elementary general facts—at least rank(E) vectors are required to span a rank-r vector bundle fibre, and a single nonzero principal equation on a regular variety has codimension one—with the standard dimension formula for the universal vertical jet space. Merker and Darondeau already develop global generation of these jet tangent bundles using large indexed families of vector fields. The 15-versus-(N_d+9) contradiction is therefore a consistency check on the literal target formulation, not an original complex-geometric research result.

## Scientific value

The observation is useful for rejecting an internally impossible framing, but it does not advance the substantive pole-order/global-generation problem: the record explicitly leaves c_3(2)<=7 and the relative-tangent interpretation open. Since the obstruction is immediate from fibre dimension before any geometry of the slanted fields is used, it is best retained as target triage rather than a standalone validated finding.

## Limitations

- The audit accepts the obstruction only for the literal full tangent bundle and fifteen individual sections; a relative-tangent or family-indexed interpretation is a different statement.
- The record does not decide the pole-order bound c_3(2)<=7.
- The principal-locus statement must be read componentwise, excluding functions that vanish identically on a component.

## Evidence

- [Merker, Low pole order frames on vertical jets of the universal hypersurface](https://doi.org/10.5802/aif.2458): Develops global generation for vertical-jet tangent bundles via indexed families of vector fields; the relevant geometry predates this record and is not a 15-section problem in general.
- [Darondeau, Slanted Vector Fields for Jet Spaces](https://arxiv.org/abs/1404.0212): Constructs slanted-vector-field generation results for jet spaces with many building-block fields; supports treating the record’s rank count as a consistency check rather than a new generation theorem.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `54098baac50c3c4b73fc5c58e82e732cc5ae0e1a`; comparison against current `main` found no changes under this record path since the assignment snapshot. No repository writes were made by this audit.
