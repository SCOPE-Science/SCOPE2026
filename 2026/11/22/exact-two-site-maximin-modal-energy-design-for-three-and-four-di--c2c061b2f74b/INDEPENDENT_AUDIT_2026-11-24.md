# Independent mathematical audit

## correctness

PASS

The frozen spatial theorem is correct, but the frozen Fisher-information assertion fails under its variance-only assumptions. For regular location errors the coefficient information is the squared mode amplitude times the location Fisher information, not generally the inverse variance. Take Gaussian mode-1 errors and Laplace errors of scale σ/√2 in each other mode, all independent and of variance σ². Location information is σ⁻² and 2σ⁻² respectively. The frozen fifth-grid pairs have least Fisher eigenvalue 5/(4σ²), whereas the repeated site x=y=2/5 gives (5−√5)/(2σ²)>5/(4σ²), for either band. Thus even the inferred design can fail. The complete repaired RESULT.md, METADATA.json and SLOGAN.txt under /workspace/repairs/5/ retain the spatial result and restrict the Fisher interpretation to independent common-variance Gaussian errors, whose likelihood Hessian is the claimed diagonal matrix. The repaired raw-sampling comparison correctly concerns its m×m Gram eigenvalue. For the repaired global theorem let C_k=T_k(a)+T_k(b), a=cos(2πx), b=cos(2πy), s=a+b. If all C_1,C_2,C_3≤−1/2 then s≤−1/2 and C_3+1/2−3s(C_2+1/2)=(1−s)(2s+1)²/2≤0, impossible unless s=−1/2. The two remaining inequalities then fix ab=−1/4. The two cosine roots give exactly the four unordered pairs on the full closed interval, and fifth-root summation gives equality also in mode 4. The repeated-site bound 1 follows by the three interval tests in the proof and is attained at x=y=1/4. The polynomial identity, four equal energies and equal-variance counterexample replay exactly via `cd /workspace && python -B -c 'import independent_checks as c; c.modal_energy()'`. The frozen script was read, not executed; its finite numerical checks neither establish the all-site theorem nor test Fisher information.

## originality

PASS

For the final repaired claim, the supported distinct result is that the sharp two-site value and all fifth-grid equality pairs are already forced by the first THREE harmonics. The four-harmonic upper bound and its equality follow directly from classical Fejér positivity, and the Gaussian Fisher rescaling is standard; neither is credited as separately novel. No verified earlier result covering the three-harmonic equal-weight paired minimax and equality classification was located in the bounded comparisons.

## value

PASS

The corrected result is a genuine exact two-site continuum design theorem: it shows that all equally weighted first-three-mode optima are fifth-grid designs, 25% above the sharp repeated-site threshold, and that they also equalize a fourth mode. The crucial three-mode optimum is not a direct Fejér-four-mode recomputation, and the resolved Gaussian interpretation supplies a precise sensing setting. The repair does not claim noise-law robustness, performance after demixing, or raw underdetermined spatial E-optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
