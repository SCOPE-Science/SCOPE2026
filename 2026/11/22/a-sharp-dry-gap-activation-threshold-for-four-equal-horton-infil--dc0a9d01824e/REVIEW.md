# Independent mathematical audit

## correctness

PASS

Check the model with rain saturating capacity throughout every prescribed wet burst, no ponded water during dry gaps, no switching costs, full initial capacity and nonnegative gaps. For general positive wet durations w_i let a_i=exp(-k w_i), u_i=1-a_i, and z_i=1-y_i be the deficit at the wet start. Wet j contributes f_min w_j+(Delta/k)u_j(1-z_j); afterwards a dry gap maps the new deficit to exp(-r d_j)(u_j+a_j z_j). Iterating with z_1=0 gives exactly the pair coefficient u_i u_j times the intermediate product of the a_m and the exponential of minus r times the intervening dry sum in the loss. The negative exponential for each adjacent pair supplies the strictly negative Hessian diagonal term -r²u_i u_{i+1} exp(-r d_i); the other pair contributions are negative semidefinite. Thus strict concavity and compactness give uniqueness, including boundary optima. For four equal bursts, reverse the gap order; uniqueness forces d_1=d_3=x. Up to constants the loss becomes 2exp(-rx)+exp(-r(D-2x))+2a exp(-r(D-x)). Its strict convexity and the sign of its derivative at zero, 2r[(1+a)exp(-rD)-1], give x=0 through equality at D_c. At D/2 the derivative is 2r[1-(1-a)exp(-rD/2)]>0, so the interior regime has a unique zero. Rearrangement gives exp(rD)=exp(3rx)+a exp(2rx) and d_2-d_1=log(1+a exp(-rx))/r>0, decreasing to zero as D→infinity. For three equal bursts the sum of the two single-gap exponentials is the only nonconstant part, hence equality of the gaps is always optimal; for two bursts there is no allocation choice. Independent bisection at k=r=w=D=1 gave x=0.24930539617380754, agreeing with the stated example. Inspected checker.py and VERIFICATION.md; did not execute the frozen script. The runoff equivalence uses the stated fixed total rainfall and immediate-runoff model; the theorem itself concerns infiltration volume.

## originality

PASS

The model mechanism is already in the SWMM manual, and related exact gap-allocation and storm-ordering records exist. The actual novelty determination concerns the support threshold, the persistent central-gap excess, and the strict concavity under redistributing fixed rest time in this existing model. The closest exact gap-allocation record changes both the state law and objective. The strongest plausible historical leads (Karmeli–Peri and Bauer) remain incompletely accessible; no whole-document noncoverage or publication priority is claimed. On inspected statements there is no direct or broader coverage of the particular optimization.

## value

PASS

For fixed wet exposure and dry time, the allocation is a natural control problem for this accepted empirical model. The first equal-burst count that changes which gaps should be used has an exact, nontrivial boundary, and evenly spaced gaps are strictly suboptimal even once all three gaps are positive. The general strict concavity also identifies a unique allocation for unequal predetermined pulses, making this useful as a benchmark for numerical scheduling. The result is not a field-validated recommendation; it assumes saturated wet input, no ponding in recovery, full initial capacity and no switching overhead.

The dated certificate retains the supplied scientific assessment, sources and limitations.
