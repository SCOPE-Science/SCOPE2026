# FAILED ATTEMPT — NOT A VALIDATED FINDING

Record: `2026/09/11/017`  
Independent audit date: 2026-09-28 (UTC)  
Task: `65b419b9c1230ba286453b0c84691e86`

The table passes a bespoke tracial finite-stage test but omits standard Rokhlin-dimension norm coverage and centrality; it is not a valid dim_Rok^c<=2 witness.

## Audit basis

**Correctness:** The exact rational arithmetic for the three bespoke tests is correct: equivariance is exact, same-color overlap is 0.009801, and the normalized trace deficit is 0.02725. But these nine elements are not a Rokhlin-dimension-with-commuting-towers witness in the standard sense. Finite Rokhlin dimension requires equivariant order-zero towers whose total is the unit in the central sequence algebra (equivalently finite-stage norm partition-of-unity and approximate centrality conditions). Here the total S has eigenvalue 0.891 on the point corner, so ||1-S||=0.109, not a small norm cover at the record's 0.05 scale. Moreover the diagonal block elements are not approximately central against general matrix units in M_8; commutators across blocks have order-one-third size. A small trace remainder is a tracial condition and cannot replace these norm/centrality requirements.

**Originality:** The table is an elementary constant-diagonal construction satisfying a self-selected trace criterion. It does not instantiate the published definition of Rokhlin dimension, so it does not establish an original finite-stage Rokhlin-dimension result.

**Scientific value:** Because the construction omits the defining norm-cover and centrality requirements and the record itself disclaims any limit Rokhlin-dimension bound, it cannot serve as a valid transfer input for Rokhlin-dimension permanence theorems. Its value is limited to a toy tracial calculation.

## Consequence

This package is preserved as a failed research attempt rather than silently deleted. The importer should relocate the complete original package atomically to the designated failed path together with this audit material.

## Literature

- [Gardella–Hirshberg–Santiago, Rokhlin dimension: duality, tracial properties, and crossed products](https://arxiv.org/abs/1709.00222): Definition 1.3 requires equivariant order-zero maps whose images sum to the unit; the paper separately distinguishes tracial Rokhlin properties from finite Rokhlin dimension.
