# Scientific assessment of the \(GP(25,2)\) strong-metric finding

## Correctness

**PASS.** The claim specifies a single simple cubic graph with explicit vertices and edges, and uses the standard strong-resolution distance equality. Its proof reduces strong resolving sets to vertex covers of the mutually-maximally-distant (MMD) graph, proving both implications. Independently generated shortest-path tables establish the exact MMD edge differences and absence of cross-layer edges. The outer-layer independence number is \(6\), with exactly \(25\) maximum independent sets, by an exhaustive \(14\)-candidate anchored classification; the inner-layer independence number is \(10\), with exactly five maximum independent sets, using five disjoint pentagons and exhaustive compatibility of the \(3125\) extremal candidates. Thus the complement of a largest MMD independent set has cardinality \(34\), with exactly \(125\) choices. A separate verifier checks all \(125\) such sets against the original strong-resolution distance condition for every unordered vertex pair. The proof does not mistake sampling for exhaustion.

## Originality

**PASS, subject to historical priority uncertainty.** The first 2015 public version of Kratica, Kovačević-Vujčić and Čangalović explicitly poses equality \(\operatorname{sdim}(GP(4k+1,2))=5k+5\) for \(k\ge5\) as Open Problem 1. Its 2017 journal text offers only the corresponding upper bound and a conjectural equality, and its table of computed dimensions stops at index \(19\). The exact value \(34\) at index \(25\) directly contradicts the proposed equality value \(35\). Their conjecture is not being misrepresented as a proven theorem. The standard 2007 MMD/vertex-cover reduction is credited; it does not compute the necessary independence number or classify these optima. The 2020 mixed-metric dimension paper studies a different distinguishing condition. A 2021 survey excerpt repeats the upper bound, without resolving this exact instance in the material checked. Targeted searches located no prior statement asserting this same value or count, but retrieval coverage cannot establish uniqueness.

## Value

**PASS.** The result settles a natural, exact first-undetermined-type order of an explicit published infinite conjecture, disproving it rather than supplying an arbitrary small numerical datum. The complete \(125\)-basis classification adds positive structural information: exactly \(25\) outer six-hole patterns and five inner ten-hole residue patterns are combined independently. This is directly useful in deciding the extent of failure of the old conjecture and in designing corrected all-order predictions. It does not claim such a corrected formula.

## Closest literature and limitations

Kratica et al. (arXiv:1507.00881, July 2015; *Appl. Anal. Discrete Math.* 11 (2017)) is the nearest same-object work. Oellermann and Peters-Fransen (*Discrete Appl. Math.* 155 (2007)) supplies the general strong-resolving-graph framework. Raza and Ji (*Frontiers in Physics*, 2020) computes mixed rather than strong metric dimension. Benakli et al. (2021) examines threshold variants, and the accessible section refers to the earlier upper bound. The proof is finite and is accompanied by two independently constructed exact programs. Publication priority and independent review remain unverified.

Self-review: passed. Independent audit: not yet performed.
