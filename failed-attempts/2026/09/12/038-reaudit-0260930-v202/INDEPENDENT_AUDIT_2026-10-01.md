# Independent mathematical audit — SCOPE-20260912-038

**Audit date (UTC):** 2026-10-01 (UTC)  
**Disposition:** failed

## Final claim reviewed

Nonexistence of D2-symmetric disk 4-vertex stationary planar 2-clusters

## Correctness — PASS

After upgrading the finite arc-network symmetry from equality almost everywhere to exact face invariance, each chamber is invariant under the half-turn z↦-z. A nonempty connected simply connected proper planar domain invariant under this half-turn must contain the rotation center: otherwise the half-turn restricts to an orientation-preserving fixed-point-free involution with a 2-cycle, contradicting the Brouwer plane translation/fixed-point theorem; equivalently, a path from x to -x and its rotated copy gives a loop of odd winding about the missing center. Since two disjoint chambers cannot both contain the center, two such invariant disk chambers cannot coexist. The extra stationarity, equal-area, four-vertex and positive-interface hypotheses are unnecessary but do not invalidate the theorem.

## Originality — FAIL

The core rotation obstruction is a direct specialization of the classical Brouwer/Brown plane fixed-point theorem: an orientation-preserving plane homeomorphism with a periodic orbit (in particular an involution interchanging x and -x) has a fixed point. Conjugating a simply connected proper chamber to the plane/disk makes the record’s odd-winding lemma an equivalent classical fixed-point argument. Thus the cluster-flavored theorem is covered even though its exact wording is absent.

### Equivalent formulations
Reasoning: The half-turn on an invariant simply connected chamber interchanges x and -x; after a planar uniformization/homeomorphism, Brown’s theorem is the fixed-point version of the record’s winding lemma.

Searches:
- Resultary D2 planar cluster winding query
- Morton Brown fixed points interchange two points

Evidence:
- Brown’s theorem gives a fixed point for an orientation-preserving plane homeomorphism that interchanges two points.

### Broader coverage
Reasoning: This general fixed-point result dominates the special 180-degree symmetry obstruction.

Searches:
- Brouwer plane translation theorem
- Brown, Pacific J. Math. 143 (1990) 37-41

Evidence:
- Periodic points for orientation-preserving plane homeomorphisms force fixed points under the classical theorem used by Brown.

### Exact database or table
Reasoning: Exact cluster-table absence does not defeat coverage by the stronger topological theorem.

Searches:
- Resultary exact D2 disk-cluster query

Evidence:
- Resultary returned the same SCOPE record and no exact cluster table entry.

### Claim versus prior implication
Reasoning: The record’s contradiction follows immediately: each invariant disk chamber must contain the same center, impossible for disjoint chambers.

Searches:
- Brown 1990 theorem comparison

Evidence:
- A 2-cycle x↔-x in a simply connected invariant domain forces a fixed point, which for the half-turn is exactly the center.

### Source inspections

- **Fixed points for orientation preserving homeomorphisms of the plane which interchange two points** (doi:10.2140/pjm.1990.143.37). Trigger: the record’s half-turn/odd-winding lemma. Material read: primary full text and theorem statement concerning an orientation-preserving plane homeomorphism interchanging two points. Method: full-text PDF inspection. Assessment: stronger classical result covers the core obstruction. Evidence: The theorem supplies a fixed point from a two-point interchange; the record’s half-turn supplies exactly such a 2-cycle if the center were absent.
- **Minimal clusters of four planar regions with the same area** (arXiv:1612.00178). Trigger: closest cited planar-cluster literature. Material read: primary theorem/context on planar cluster topology and symmetry. Method: primary-source comparison. Assessment: relevant cluster background but not needed for the decisive topological obstruction. Evidence: The record’s contradiction does not use the variational or four-vertex hypotheses.

### Checked sources

- Resultary semantic search
- Brown 1990 primary paper
- Paolini-Tamagnini arXiv:1612.00178 cluster paper

### Residual risks

- The null-set-to-exact symmetry upgrade uses the finite arc-network hypotheses; the audit accepts that local face argument, but the rejection is already decisive on originality.

## Scientific value — FAIL

The stated cluster nonexistence collapses to a classical fixed-point/winding fact about two disjoint centrally symmetric simply connected planar domains; none of the stationarity, equal-area, pressure, four-vertex or positive-interface structure contributes. As a result it is a textbook topological deduction rather than a new isoperimetric-cluster boundary result.

## Limitations

- The audit accepts the finite-network argument upgrading almost-everywhere symmetry to exact chamber invariance; the scientific rejection is independently decisive on prior coverage/value.

The finding is not accepted because all three scientific axes do not pass. The original research files and evidence are preserved in the failed-attempt package.
