# Scientific review: Exact sixth Fourier moments of finite middle-thirds Cantor spectra

## Correctness — PASS

The claim is restricted to ordinary integer six-tuple equality at all finite digit depths. A column difference is counted by \(\binom 6{3+d}\), and the unique integer carry recurrence \(d_j=3c_{j+1}-c_j\) has precisely three possible states, including endpoint zero. The displayed full transfer matrix and reflection reduction produce the exact two-dimensional matrix with trace 26 and determinant 90. Both initial values are explicit, hence Cayley--Hamilton gives the exact recurrence and rational generating function without extrapolation. The interval-support induction is independent. The spectral leading coefficient is strictly positive. An independent histogram-based checker executed successfully at levels 0 through 8 and confirmed all stated initial values, the exact carry matrix, support and 30 more recurrence steps. Finite checks are corroboration only.

## Originality — PASS with material residual priority risk

The precise proposed difference is the **full finite-level six-variable integer-energy sequence** and its generating numerator, not the general transfer-matrix method or continuous moment exponent. Hare--Sidorov (2022), arXiv:2210.07671, treats twofold sumsets and uniqueness without this count. Lau--Ngai (2000) is a substantially closer source: their Theorem 1.4 and integer-\(q\) Theorem 5.1 analyze the *same* threefold Cantor convolution. Their tabulated \(q=2\) equation \(45z^2-832z+2048=0\) transforms under \(z=64/\lambda\) into the characteristic polynomial \(\lambda^2-26\lambda+90\), so the leading growth exponent is **already implied by prior work**. The inspected results do not give the all-depth raw integer count \(E_k\), its initial conditions or rational generating function. Fong--Hare--Johnstone (2011) and Hare--Hare--Shen (2019) treat multifractal dimensions, not the exact discrete count. Related exact energy results for different digit alphabets cannot be specialized to the ternary two-digit family. Priority remains at risk if an existing finite-type identity implicitly packages precisely the same numerator and boundary vector.

## Mathematical value — PASS

The classical ternary Cantor approximation is a canonical arithmetic model and its triple sumset is a full integer interval. Computing its entire sixth Fourier moment for **every** depth, rather than just its already-known scaling exponent, quantifies the exact arithmetic multiplicities of that complete sumset. The rational all-level law and sharp leading constant form a natural exact invariant useful for precise finite-scale collision estimates. The distinction between full interval support and exponentially increasing normalized collision energy motivates the computation. No universal theorem or downstream application is required for this finite-scale model problem.

## Residual limitations

The \(q=2\) spectral root and correlation dimension are not new. A close equivalence to the preexisting transfer formalism is a material priority concern, even though the exact finite-level statement and its coefficients were not located. Searches are not proofs of novelty; no independent verification has been performed.

Self-review: passed. Independent audit: not yet performed.
