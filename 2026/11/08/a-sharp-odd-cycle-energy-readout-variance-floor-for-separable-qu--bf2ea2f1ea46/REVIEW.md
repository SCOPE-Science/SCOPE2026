# Scientific assessment

## Correctness — PASS

The joint density operator is a convex mixture of locally diagonal normalized Pauli stabilizer projectors, proving full separability in the stated parameter range. Exact Born traces give uniform measurement outcome weights and a Walsh expansion of conditional battery energy. Parseval reduces the branch variance to a sum of field penalties and squared equatorial edge inner products. For an odd cycle the optimization is multi-affine in squared equatorial Bloch lengths; vertex reduction separates configurations with a vertical axis (sharp value \(h^2\)) from all-equatorial configurations. The least adjacency eigenvalue \(-2\cos(\pi/n)\) supplies a universal lower bound and its unit Fourier eigenmode realizes equality. The checker tests Born/Pauli algebra and boundary constructions but finite checks do not replace the proof. Validity is restricted to nonadaptive rank-one product-projective readout and conditional expected energy.

## Originality — PASS, qualified

The primary recent quantum-battery paper studies adaptive readout with two pure charger qubits and iterative collision dynamics, not the finite odd-cycle optimized energy-branch variance in a separable mixed state. Crucially, Liu–Yang–Shi–Yu's 2023/2025 quantum-metrological local-measurement framework already includes an explicit incompatible three-site planar-orthogonality system. Thus qualitative impossibility on triangles and familiar odd-cycle spectral geometry are prior ideas and not the novelty claim. Their Example 3 and general metrological criteria do not provide the present exact minimum over *all* qubit Bloch axes, nor its field-versus-coupling crossover and explicit fully separable state. Relevant database searches found related Pauli and product-measurement results but no directly implying quantitative statement. Possible unlocated general optimal-diagonal-flattening theorems and physical comparability with adaptive protocols remain priority risks.

## Value — PASS

Uniform conditional energy across measurement outcomes is a concrete precision objective of measurement-assisted quantum batteries. The exact positive, tunable variance floor in an entirely separable source separates readout-geometry frustration from entanglement as a prerequisite. A nontrivial transition occurs between a uniformly distributed angular frustration pattern and sacrificing one site's transverse sensitivity; the optimal threshold \(h/J=\sqrt{n(1-\cos(\pi/n))/2}\) resolves a complete family, rather than a convenient three-qubit numerical example. It is useful as an analytic baseline for restricted-readout architectures, without being advertised as a statement about arbitrary quantum-battery charging devices.

## Closest literature and limitations

Gong–Zhang–Li, arXiv:2610.31242 (2026), motivates conditional-energy uniformity but differs in available adaptivity, initial states and dynamical setting. Liu–Yang–Shi–Yu, arXiv:2310.00285 (2023/2025), Section IV C Example 3, explicitly describes mutually incompatible planar local-measurement orthogonality conditions. That earlier qualitative obstacle is not new here. The present optimization only treats predetermined tensor-product projective bases and the dispersion of branch-conditional mean energies; it does not imply restrictions on feedforward, collective POVMs, or repeated charging.

Self-review: passed. Independent audit: not yet performed.
