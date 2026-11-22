# Scientific assessment: three-particle four-cube top homology

## Correctness — PASS

The reduced Świątkowski comparison theorem identifies the stated integral weight-three complex with singular homology. The explicit top basis has 15,120 vectors; exhaustive signed chain construction and rank 14,991 modulo three bound top rational homology above by 129. All 1,112 pairwise-disjoint simple-cycle product tori (classified by the four possible cycle-length triples) are integral cycles. Exact rational column reduction yields their combined rank 128. A supplied 1,475-term integer cycle has zero full signed boundary and a nonzero *rational* reduction against that torus span. Thus at least 129 independent rational cycles exist. The rank sandwich proves the free top group is exactly \(\mathbb Z^{129}\); top homology is torsion-free as a subgroup of the free top chain module. `verify.py` reconstructs the model and all checks from the embedded witness. The claim does not confuse modular independence with rational non-membership.

## Originality — PASS, subject to publication-priority risk

Targeted semantic searches of mathematical records used aliases for the Q4/four-cube/hypercube graph, three-strand graph braid space, degree-three homology, non-toric cycles, and product three-tori. Closest inspected published records classify the Q4 *two-particle* torus lattice, the Q3 *three-particle* homology, and the truncated-tetrahedron *three-particle* top torus basis, respectively. Their conclusions concern different spaces and do not imply the 129-versus-128 statement. Primary results of An–Drummond-Cole–Knudsen supply a general computational model but no such finite evaluation; Maciążek–Sawicki explain product/non-product phenomena in different graph examples. No covering theorem was located. The remaining material risk is an equivalent unindexed computation or a stronger general theorem not found in the inspected sources; failure to locate one is not logical proof of uniqueness.

## Value — PASS

The gap is structurally motivated: product tori built from disjoint graph cycles are a canonical mechanism for third-dimensional graph-configuration classes, and Q4 is a natural symmetric nonplanar graph with many such cycles. The complete count of all 1,112 geometric tori rules out a false-negative caused by considering only square cycles, while a concrete non-toric integral cycle demonstrates a genuinely new homological mechanism. The exact rank-one rational obstruction distinguishes the three-particle configuration topology from its large family of geometric toric cycles. The result neither requires a uniform higher-cube formula nor claims a complete quotient-lattice Smith classification.

## Closest literature and limitations

An, Drummond-Cole and Knudsen, *Subdivisional Spaces and Graph Braid Groups*, arXiv:1708.02351, Definition 4.7 and Proposition 4.9; Barnett and Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180; Maciążek and Sawicki, *Non-Abelian Quantum Statistics on Graphs*, doi:10.1007/s00220-019-03583-5; and the three relevant published finite graph-configuration records cited in RESULT.md. The free rank, but not possible torsion, of the non-toric quotient is established. Exact finite computations and a standard established chain model are used; no independent validation or complete higher homology presentation is claimed.

Self-review: passed. Independent audit: not yet performed.
