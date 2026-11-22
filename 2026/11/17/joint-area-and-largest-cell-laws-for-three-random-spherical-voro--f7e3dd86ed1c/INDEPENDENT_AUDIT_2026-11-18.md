# Independent mathematical audit

## correctness

PASS

Read the full frozen RESULT.md and inspected verify.py. The two outward hemisphere normals at a site meet at Euclidean chord-triangle angle alpha_i; their intersection lune has area 2(pi-alpha_i), giving sum 4pi. The spherical Blaschke–Petkantschin shape-size disintegration (Akopyan–Edelsbrunner–Nikitenko, Lemma 5 and equation (9)) weights the uniform circle-angle simplex by chord triangle area 2r^2 product sin(alpha_i), so joint angle density is 8/(3pi) product sin alpha_i because its simplex integral is 3pi/8. Area-coordinate Jacobian is 1/4. For M<=m, each alpha_i >= pi-m/2; integrating the sine-sum identity over the truncated simplex gives the displayed CDF. Independently symbolically integrated normalization, mean and both boundary Taylor series, finding F(4pi/3+t)=9sqrt(3)t^2/(8pi)-9sqrt(3)t^4/(32pi)+O(t^5), 1-F(2pi-t)=t^2/2-t^4/24+O(t^5). The n=3 sampling has no degenerate atoms. A finite 350,000-trial verification is documented in the source VERIFICATION.md; I inspected rather than re-ran that Monte Carlo checker, and do not use its output as proof.

## originality

PASS

Best-knowledge PASS for the specifically joint labelled three-cell law and largest-cell exact statistic; not for single-cell marginal, acute-chord probability, or general spherical BP. The published single-cell CDF and covariance for the same 3-site model do not identify the joint density, whereas Akopyan et al. give shape-size independence and volume-weighting but not the joint-area/maximum formulas. Inaccessible Miles (1971) and Arbeiter–Zähle (1994) are genuine historical-priority risks.

## value

PASS

The labelled joint distribution determines all joint correlations and exact largest-cell extremes; neither can be recovered from individual marginals and sum constraint alone. The explicit special-function-free law and quadratic endpoint coefficients characterize a natural three-generator spherical tessellation, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
