# A certified attracting period-three window in a fractional sine map

## Finding

Consider the one-parameter interval map
\[
f_r(x)=\frac{\sin(\pi x)}{1+rx},\qquad 0\le x\le1,\qquad r>0.
\]
For **every**
\[
r\in R=\left[\frac{124999}{1000000},\frac{125001}{1000000}\right]
\]
there is a primitive, asymptotically attracting three-cycle \(x_0\mapsto x_1\mapsto x_2\mapsto x_0\), with
\[
\begin{aligned}
x_0&\in I_0=[0.1632,0.1633],\\
x_1&\in I_1=[0.48073,0.48100],\\
x_2&\in I_2=[0.94158,0.94161].
\end{aligned}
\]
The period-three multiplier \(\Lambda=f_r'(x_0)f_r'(x_1)f_r'(x_2)\) satisfies the uniform strict bound
\[
-0.499<\Lambda<-0.479.
\]
Each cycle has an open interval basin of attraction. In particular its asymptotic orbit Lyapunov exponent is \(\frac13\log|\Lambda|<0\). The interval \(R\) lies strictly inside the parameter range described as robustly chaotic, without periodic windows, for this fractional sine family in the originating 2023 article. The theorem does **not** assert that no other chaotic invariant set exists.

## Assumptions and scope

The function is considered in exact real arithmetic, not finite-precision digital iteration. The source's notation is
\[
f(x)=\frac{\mu\sin(\pi x)}{e x+\mu},\qquad \mu,e>0.
\]
Dividing numerator and denominator by \(\mu\) gives \(r=e/\mu\). Thus the certified parameter interval corresponds to the positive parameter ratios \(e/\mu\in R\), and includes \(\mu=8e\). Every parameter in this interval has an attracting three-cycle. No classification of all periodic orbits, global attractors, or cryptographic behavior is claimed.

## Proof

Let \(R=[r_-,r_+]\) and let \(I_0,I_1,I_2\) be the three rational intervals specified above. The derivative is
\[
f'_r(x)=\frac{\pi\cos(\pi x)(1+rx)-r\sin(\pi x)}{(1+rx)^2}.
\]
For \(0<x<1\), the parameter derivative \(\partial_r f_r(x)=-x\sin(\pi x)/(1+rx)^2\) is negative. Rigorous rational interval enclosures, valid simultaneously for every \(r\in R\), give
\[
\begin{array}{c|c|c}
\text{interval}&\text{strict derivative enclosure}&\text{strict image containment}\\\hline
I_0&(2.62344,2.62406)& f_r(I_0)\subset\operatorname{int}(I_1)\\
I_1&(0.06575,0.06828)& f_r(I_1)\subset\operatorname{int}(I_2)\\
I_2&(-2.78190,-2.78179)& f_r(I_2)\subset\operatorname{int}(I_0).
\end{array}
\]
These are not floating-point assumptions. They are consequences of the fully rational enclosure procedure in `check_certificate.py`: Machin's identity expresses \(\pi\) using two alternating arctangent series; Taylor polynomials for sine and cosine, with Lagrange remainders and the \(\pi\)-enclosure error, bound all endpoint values; exact fraction interval operations then establish the displayed inequalities. The derivative signs determine the monotonicity on each interval; monotonicity in \(r\) determines the correct parameter endpoints of each image interval.

Therefore \(f_r^3\) maps \(I_0\) strictly inside itself. The chain rule and the derivative enclosures show that, throughout \(I_0\),
\[
-0.499<(f_r^3)'<-0.479,
\]
so \(f_r^3\) is a contraction on the complete interval \(I_0\). The contraction theorem gives a unique fixed point \(x_0\in I_0\). Its first two images lie in the disjoint intervals \(I_1,I_2\), so the least period is exactly three. The same strict inclusions and contraction show that the cycle attracts all points initially in the union of the three intervals and hence possesses an open basin. The multiplier bound is precisely the chain-rule bound at \(x_0\). This completes the proof simultaneously for every \(r\in R\).

## Verification

Run the standalone, Python-standard-library-only checker with `python check_certificate.py`. Its arithmetic is based on `fractions.Fraction`, not sampled trajectories. It asserts the image-inclusion inequalities, derivative signs and strict multiplier bounds. The checker reports rationally certified decimal displays, for orientation only:
\[
\begin{aligned}
f_r(I_0)&\subset (0.48073177,0.48099431),\\
f_r(I_1)&\subset (0.94158654,0.94160549),\\
f_r(I_2)&\subset (0.16320140,0.16328514).
\end{aligned}
\]
The final interval bounds in the proof are checked using exact fractions; these displayed decimals are not used as axioms. The program completed successfully, including every assertion, at the time the result was packaged.

## Relationship to prior work

Zhu, Deng, Zhang and Zhu (2023) introduce this exact family and give numerical bifurcation and Lyapunov analyses. Their Section 2.2 characterizes fixed-point instability and Section 2.3 describes the region above a parameter-ratio threshold as robustly chaotic, with no small periodic windows. The present strict three-cycle contraction certificate concerns an orbit type not analysed there, and demonstrates an attracting periodic regime within that parameter range. The result is a counterexample to a global no-periodic-window interpretation, not a claim about the absence of all chaos.

An indexed 2026 result entitled *The exact two-cycle threshold and supercritical flip of a rational sine map* analyzes primitive two-cycles for the same normalized family. A classification of two-cycles does not logically establish or rule out the certified attracting primitive three-cycle. General one-dimensional unimodal-map theory predicts that periodic windows can occur, but does not by itself supply the particular explicit interval \(R\) or its exact verified multiplier bounds.

## Limitations

The window \(R\) is a certified **subinterval**, not a sharp or exhaustive stability tongue. Other attracting, repelling or chaotic invariant sets elsewhere in the interval may coexist. The result establishes no statements about finite-precision implementations, the security of image encryption, or global ergodicity. Published or unindexed work could already contain equivalent cycle certificates; the literature comparison does not prove uniqueness or publication priority.

## References

1. S. Zhu, X. Deng, W. Zhang, and C. Zhu, *Image Encryption Scheme Based on Newly Designed Chaotic Map and Parallel DNA Coding*, Mathematics **11** (2023), 231, https://doi.org/10.3390/math11010231 (first published January 2, 2023), especially Sections 2.1–2.3.
2. *The exact two-cycle threshold and supercritical flip of a rational sine map*, public mathematical research synopsis (2026); consulted for comparison of the same one-parameter family. The available synopsis concerns primitive period two, not the period-three assertion proved here.
