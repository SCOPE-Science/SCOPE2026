# Independent mathematical audit

## correctness

PASS

Reconstructed scalar R(z)=(4+4z-z^2)/[(z+1)(z+2)^2]; independent Sympy derivative gives (z^3−10z^2−20z−8)/[(z+1)^2(z+2)^3], one positive minimizer. Exact SOS R+1/27=[z(z−12)^2+2(z−7)^2+14]/[27(z+1)(z+2)^2]>0 and R(12)=−23/637 <−1/28 establish dimension cutoff via spectral weights |v_j(i)|² summing to (n−1)/n. Equality forces Le_i=λ(e_i−1/n), thus all hub edges equal, and conversely; other edges irrelevant. Universal hub diagonal polynomial P_n(z) has exactly two positive roots for n>=29 by sign changes and z=12 negative. Independently checked symbolic derivatives, exact rational bound, n=28 positive 4/4459 and n=29 negative −1/2639=−7/18473. Source matrix verifier inspected; finite checks are not global proof.

## originality

PASS

Earlier work gives Richardson formula and scalar positivity loss for backward Euler; neither entails the worst-case diagonal bound across all weighted graphs, 28/29 sharp size threshold or equality network rigidity. The prior 2010 stability papers were not read in full; substantive priority risk retained.

## value

PASS

Sharp universal sign boundary for a standard higher-order accelerated diffusion operator, identifying first graph size with negative self-transition and all equality networks; useful to numerical positivity and graph heat discretization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
