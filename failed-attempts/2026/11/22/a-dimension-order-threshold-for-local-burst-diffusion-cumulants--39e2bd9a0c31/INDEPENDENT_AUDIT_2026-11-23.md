# Independent mathematical audit

## correctness

PASS

The exact law and asymptotic constants check out. For a burst of age t the count in a detector A is Bin(J,a(t)) with a(t)=e^(−μt)∫_A p_D(t,z)dz. Only finitely many past bursts contribute almost surely, since their expected number is bounded by bm_1/μ. The log pgf of the marked process is the stated age integral for −1<z≤0; its r-th differentiated integrand there is bounded by m_r e^(−rμt) for 1≤r≤k, and finite m_k ensures each such moment is finite. Differentiating from the left gives F_k=bm_k∫a(t)^k dt, also zero when m_k=0. For a source ball substitute u=Dt/ε² and use Q_d(u)^k=c_{d,k}u^(−dk/2)(1+O(1/u)). For dk>2 the integral is dominated by min(1,c_{d,k}u^(−dk/2)); for dk=2 subtract c_{d,k}/u beyond u=1 to get a bounded remainder and c_{d,k}log(D/(μ ε²)), where k only changes the bounded term. For dk<2 the unscaled, volume-normalized integrand is bounded by c_{d,k}(Dt)^(−dk/2)e^(−kμt) and its integral gives the stated gamma factor. Away from the source the normalized integrand has the additional Gaussian bound exp(−k|x|²/(16Dt)) for ε<|x|/2. An independent check of C_{2,2} uses the 4D zero-mortality Green kernel 1/(4π²|z|²) integrated on the unit disk product: radial squared variables give (1/4)∫_0^1∫_0^1(α+β)^−1 dα dβ=(log 2)/2. In 3D the unit ball gives ∫_0^1 r dr=1/2. In 1D the exponential resolvent integrated over [−ε,ε] gives the exact stated mean. Replay: RESULT.md (1) and proof steps 1–4; checker.py was inspected, not executed, and tests scaled source integrals, not the off-source law.

## originality

FAIL

The higher-order occupancy has exactly the established one-particle mean resolvent in dimension dk, integrated over a product detector, with source intensity bm_k and mortal rate kμ. This is stronger coverage by explicit product-process reduction, not a claim that a d-dimensional mean by itself specifies higher cumulants. The motivating prior paper and standard factorial-cumulant formula together give the entire local threshold and the off-source law by the standard near-zero behavior of the same radial kernel. The planar numerical constant is an elementary integration of that kernel over two disks, not a separate surviving hierarchy.

## value

FAIL

The source/off-source contrast and planar pair constant are useful benchmarks. But as a standalone research claim, the hierarchy is the textbook dimension-two Green singularity under an exact dimension substitution, and the two constants are elementary integrations of the already determined kernels. The record resolves no remaining structural comparison or independent detector invariant beyond those deductions. This is not a criticism of its mathematical correctness or usefulness as an explanatory note.

The dated certificate retains the supplied scientific assessment, sources and limitations.
