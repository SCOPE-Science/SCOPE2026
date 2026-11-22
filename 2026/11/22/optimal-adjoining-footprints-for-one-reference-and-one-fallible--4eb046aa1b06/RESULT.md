# Optimal adjoining footprints for one reference and one fallible wildlife detector

## Finding
Consider two freely positioned detectors on a real transect, each covering a closed interval of radius \(r>0\). A reference detector always reports a target in its footprint; a secondary detector independently reports a target in its footprint with probability \(q\in(0,1)\). The target location has a positive, continuously differentiable, even, strictly log-concave probability density \(f\) on \(\mathbb R\). The objective is the probability of at least one true detection.

**Theorem.** Every global optimum has the detector footprints adjoining without interior overlap or gap, and the two optimal layouts are reflections of one another. Writing the reference footprint as \([c-2r,c]\) and the fallible footprint as \([c,c+2r]\), the unique optimal touching point \(c_*(q)\) lies strictly between \(0\) and \(r\) and solves
\[
(1-q)f(c)-f(c-2r)+qf(c+2r)=0.
\]
It is strictly decreasing as \(q\) increases; moreover \(c_*(q)\to r\) as \(q\downarrow0\) and \(c_*(q)\to0\) as \(q\uparrow1\). Thus even a very unreliable supplementary detector should be placed beside, rather than atop, the perfectly detecting reference interval, and its optimal location shifts continuously toward a symmetric two-interval layout as quality increases.

For the normal location density with standard deviation \(\sigma>0\), set \(a=e^{-2r^2/\sigma^2}\). The unique positive solution is explicitly
\[
c_* = \frac{\sigma^2}{2r}\log\!\left(\frac{1-q+\sqrt{(1-q)^2+4qa^2}}{2a}\right).
\]
The detector centers are \(c_*-r\) (reference) and \(c_*+r\) (fallible), or their reflected layout. For \(r=\sigma=1\) and \(q=1/2\), \(c_*\approx0.670810453818787\), giving optimal detection probability approximately \(0.780630247637310\). A symmetric touching arrangement instead gives approximately \(0.715874802077731\).

## Assumptions and scope
The theorem applies to **exactly two** detectors with identical hard footprints of full width \(2r\), on an unbounded one-dimensional transect. The first detector is conditionally perfect inside its footprint; the second has constant conditional sensitivity \(q\), independent of location within its footprint. There are no false alarms. A target position \(X\) has density \(f\); there is a single target for the detection event. Strict log-concavity means \(\log f\) is strictly concave. The probability of either detector signaling is the performance objective, not detection-rate precision, occupancy estimation, or tracking accuracy. The result is for a mathematical idealization and does not assert that any actual field device is perfect.

## Proof
Let \(I_1\) and \(I_2\) denote the reference and secondary intervals. The detection probability is
\[
P(I_1,I_2)=\int_{I_1}f(x)\,dx+q\int_{I_2\setminus I_1}f(x)\,dx.
\]
If the intervals overlap and the secondary extends to the right, moving its left endpoint to the right endpoint of \(I_1\) strictly enlarges \(I_2\setminus I_1\) while leaving the reference integral fixed. The same holds by reflection if it extends left. If it lies within \(I_1\), moving it outside strictly improves detection because \(q>0\) and \(f>0\). Thus overlap cannot maximize.

If the intervals have a positive gap and the reference is left of the secondary, let their centers be \(u<v\). If \(u<0\), move the reference slightly right toward the mode while keeping the intervals disjoint. If \(u\ge0\), then \(v>0\), and move the secondary slightly left toward the mode while maintaining disjointness. The moved interval gains strictly more mass, because an even strictly log-concave density is strictly decreasing away from zero. The opposite ordering follows by reflection. Hence an optimum must have adjoining intervals.

By symmetry it suffices to study the reference-left layout above. Write \(F\) for the distribution function. Its detection probability is
\[
H_q(c)=F(c)-F(c-2r)+q[F(c+2r)-F(c)].
\]
Let \(g=\log f\) and divide the derivative by the strictly positive \(f(c)\):
\[
\frac{H_q'(c)}{f(c)}=(1-q)-\exp(g(c-2r)-g(c))+q\exp(g(c+2r)-g(c)).
\]
Since \(g'\) is decreasing, the first exponential ratio is strictly increasing in \(c\), while the second is strictly decreasing. Therefore the displayed derivative ratio is strictly decreasing, for all real \(c\). At \(c=0\) it is positive, because
\[
H_q'(0)=(1-q)[f(0)-f(2r)]>0,
\]
and at \(c=r\) it is negative, because
\[
H_q'(r)=q[f(3r)-f(r)]<0.
\]
There is exactly one derivative zero in \((0,r)\), with positive derivative before and negative derivative afterward. This is the unique global maximum of the touching-layout objective. Consequently there are exactly two optimal labeled layouts, related by reflection.

At any \(c\in(0,r)\), the derivative of \(H_q'(c)/f(c)\) with respect to \(q\) is \(-1+f(c+2r)/f(c)<0\). Since its derivative with respect to \(c\) is negative, the root moves strictly left as \(q\) increases. At \(q=0\), the unique root is \(c=r\); at \(q=1\), the unique root is \(c=0\); continuity proves the endpoint limits.

For a Gaussian density, the ratios in the derivative equation equal \(az\) and \(a/z\), respectively, where \(a=e^{-2r^2/\sigma^2}\) and \(z=e^{2rc/\sigma^2}\). The stationarity condition becomes
\[
az^2-(1-q)z-qa=0.
\]
The unique positive root gives the stated radical formula. Uniqueness and global optimality have already been proved for all densities in the stated class.

## Verification
Run \(\texttt{python3 checker.py}\) to test the Gaussian closed-form optimum against 160 numerical parameter sets and 161 touching-point comparisons per set, as well as nine logistic-prior cases. The script uses Python's standard library and prints an assertion total. These numerical tests are supplementary: the unrestricted global optimality and strict monotonicity follow from the preceding proof, not the finite test grid.

## Relationship to prior work
Palencia et al. (2024) investigated clustering and rotating camera traps using simulations and field data; their objective was detection-rate precision and their simulation treated detection inside a grid cell as perfect. The present result instead optimizes probability of an initial true alarm from a single uncertain target with a perfect reference and a fallible supplementary detector.

Litvak et al., *Increasing Detection Performance of Surveillance Sensor Networks*, §5.2.1, derive two-sensor coverage probabilities and a sufficient no-overlap criterion in a bounded interval with identical detector sensitivities. This does not state the present global, unequal-reliability, arbitrary even strictly log-concave optimizer or the Gaussian formula. Wettergren and Costa (2013) numerically optimize distributed sensor configurations; the present one-dimensional exact characterization is not their numerical optimization claim. General interval-rearrangement and log-concavity techniques are established tools, not claimed as new.

## Limitations
The result does not permit a fallible reference detector, non-identical footprint lengths, multiple correlated targets, false-positive constraints, a bounded transect, arbitrary multimodal location densities, or uncertainty about the prior \(f\). The strong log-concavity requirement ensures uniqueness but is not proved necessary. Near \(q=0\) the secondary placement affects the objective by only order \(q\), so applied benefits may be small. The numerical example does not validate any real camera system. Historical priority beyond the inspected sources is provisional; no independent external audit has been performed.

## References
1. Palencia, P., et al. (2024). *Clustered and rotating designs as a strategy to obtain precise detection rates in camera trapping studies*. Journal of Applied Ecology. First published 27 May 2024. https://doi.org/10.1111/1365-2664.14690
2. Litvak, N., et al. *Increasing Detection Performance of Surveillance Sensor Networks*, Section 5.2.1, pp. 88–90. https://miis.maths.ox.ac.uk/268/2/thales-report.pdf
3. Wettergren, T. A., and Costa, R. (2013). *Optimal Planning of Distributed Sensor Layouts for Collaborative Surveillance*. International Journal of Distributed Sensor Networks. https://doi.org/10.1155/2013/145496
