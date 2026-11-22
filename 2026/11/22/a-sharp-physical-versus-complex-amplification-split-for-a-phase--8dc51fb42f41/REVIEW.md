# Review of the modified-energy and near-CFL amplification theorem

## Correctness — PASS

The full claim is a single mode-wise theorem. The original amplification polynomials imply \(C=-\rho\overline B\) and \(A^2+\rho|B|^2=1\), establishing exact Hermitian invariance for \(0<q^2<12\). The power identity yields an exact projected-output weighted-energy factor for all integer observation indices. The near-edge proof is uniform in that integer index, and integer quarter-period sampling proves both sharp limiting constants from the same real input. The symbolic polynomial certificate and sampled tests in `verify.py` have passed. The finite checks are auxiliary to the quantified analytic proof; the endpoint is excluded from boundedness.

## Originality — PASS (qualified)

The full primary source [Duan, Li and Guo, arXiv:2608.22315](https://arxiv.org/abs/2608.22315) was inspected across its modal matrix, CFL proposition, exact power representation, and real-output convention. Those underpin and receive credit for the method, its matrix, and the role of projection. They do not assert the sharp singular-CFL complex and physical gains, the exact weighted output-energy law, or the interior real-output notch. The full related [Bernier et al. 2023 paper](https://arxiv.org/abs/2303.10950) covers generic near-unitary conjugacy of different complex splitting schemes but not the specific quantitative modal claim. A published general triangular-multiplier result was compared by indexed scientific summary only because its linked complete text was inaccessible; it remains a documented priority risk. The source's explicit matrix means these are algebraic and asymptotic refinements, not a new algorithm or an independent rediscovery of its spectral bound.

## Value — PASS

Near-CFL mode amplitude is a motivated numerical-stability quantity. The positive modified invariant does **not** imply preservation of physical electromagnetic energy, while the real projection can suppress the modified norm even at stable interior modes. The two exact distinct leading blow-up constants show quantitatively how the hidden complex field differs from reported physical output. This is more informative than a qualitative strict-margin existence bound and supplies a sharp test at the edge without claiming higher global order or a PDE-wide result.

## Closest literature and limitations

The 2026 Maxwell source already supplies the composition, phase optimizer, critical CFL value, output projection, and Cayley-Hamilton power formula. The 2023 reversible-splitting theory supplies general related structure. A 2026 published triangular-multiplier result remains summary-only. The present theorem concerns one transverse Fourier polarization on a homogeneous periodic grid, with no uniform continuum PDE guarantee, no new time integrator, no physical Maxwell energy conservation, and no independent validation.

Self-review: passed. Independent audit: not yet performed.
