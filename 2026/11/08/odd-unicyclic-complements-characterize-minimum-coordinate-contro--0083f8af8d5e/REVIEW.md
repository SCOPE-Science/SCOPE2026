# Review of odd-unicyclic complement classification

## Correctness — PASS

For every \(n\ge5\), the identity \(A=J+I-B^{\mathsf T}B\), together with \(BB^{\mathsf T}=(n-2)I+J\), gives all three pairwise distinct Laplacian eigenspaces of dimensions \(1\), \(\binom n2-n\), and \(n-1\). PBH forces at least \(\binom n2-n\) independent coordinate inputs. Equality makes the first nontrivial restriction precisely the invertibility of an unsigned incidence matrix on the unactuated pairs. Its block-rank criterion gives exactly odd-unicyclic components. The second eigenspace restriction is analyzed separately: a connected bipartite controlled-edge graph can support a nonzero zero-sum sign vector only when its bipartition is balanced; edge counts exclude this except for \(K_{3,3}\) at \(n=6\), whose ten complements are two triangles. Disconnected controlled-edge graphs have one isolated ground vertex and an otherwise nearly complete nonbipartite component, so the zero-sum condition resolves that case. The labeled-cycle EGF proves the enumeration. The extracted finite exact checker provides independent computational checks, not an infinite proof.

## Originality — PASS within inspected coverage

The 2014 qualitative-class controllability theorem and the 2019 exact Kneser zero-forcing theorem do not imply the fixed-Laplacian minimum; for \(n\ge7\) their robust zero-forcing bound \(\binom n2-6\) is strictly larger than \(\binom n2-n\). The 2017 two-subset Kneser critical-group paper supplies spectral context, not actuator selection. The 2022 odd-unicyclic unsigned-incidence criterion is known and is expressly credited. Searches of mathematical result records under Kneser/controllability/incidence/odd-pseudoforest aliases and comparison against related exact graph actuator results found no equal or dominating assertion. **Residual risk:** an unindexed or differently titled specialist result could establish the same graph- and input-specific classification; independent priority confirmation has not occurred.

## Value — PASS

A fixed dense, highly symmetric but multiply degenerate Laplacian has a natural actuator minimum significantly below its robust zero-forcing bound. The full minimum-set criterion is a graph-theoretic odd-cycle test, with a genuinely exceptional balanced-eigenspace obstruction at six ground labels. The exponential generating function counts all minimum placements and the theorem includes the Petersen graph. This is a complete structural classification of a motivated natural infinite family, not an isolated numerical rank table.

## Limits of assessment

The assertion is restricted to dedicated independent vertex inputs, no weight perturbations and minimum-size sets; finite checks do not certify the theorem on their own. Publication priority has not been independently established.

Self-review: passed. Independent audit: not yet performed.
