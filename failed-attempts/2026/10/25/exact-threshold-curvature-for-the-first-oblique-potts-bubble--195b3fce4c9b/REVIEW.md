# Independent mathematical audit

## correctness

PASS

For first oblique two-kink threshold of leading extreme-ferromagnetic Potts approximation, α=4/(3v), F(p,v)=e^{ip}J_{1−α cos p}(α)+4J_{−α cos p}(α), G(α)=F(0,v). At the first root α*, F_p(0,a1)=iJ_{1−α*}(α*) and F_v(0,a1)=−(3α*²/4)G’(α*). J denominator cannot vanish there: then adjacent-order Bessel recurrence would give a solution and derivative both zero, contradicting Bessel ODE uniqueness. IFT gives p1(v)=i c1(v−a1)+O((v−a1)²), c1=−(3α*²/4)G’/J; cosine expansion of E=2−(4g/3)cos p gives E_min−E1=(2/3)c1²g(v−a1)²+O(g|v−a1|³). Independent high-precision mpmath evaluation reproduced α*=0.906338059174892129878, c1≈8.696131059428713262743 and K≈50.41513026850716994685, but decimals are not rigorously interval enclosed. No nonperturbative full-chain assertion.

## originality

FAIL

The pre-existing 2025 Potts source gives the full oblique Jost secular function and the same simple-root/first-bubble expansion. The exact derivative expression is −F_v/F_p with F_p at p=0, and K is the standard quadratic cosine coefficient; no new lemma, boundary, classification or nontrivial reduction is required. A previously implicit coefficient is not necessarily a novel contribution merely because the source did not print its decimal.

## value

FAIL

The coefficient is physically interpretable, but its entire derivation is a routine one-line implicit derivative of an already stated Jost secular equation followed by the textbook Taylor expansion cos p=1−p²/2+…. The submitted result adds a single non-certified decimal to a known quadratic law, with no rigorous error estimate, new structural phenomenon, phase boundary or independent finite classification. Under the common bar, this tiny unmotivated analytical specialization is not an independently valuable new mathematical claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
