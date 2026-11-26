# Independent mathematical audit

## correctness

PASS

The frozen inverse and open band are correct; the frozen Limitations mislabeled the quadratic athermal approach as being at the upper fourth-cumulant boundary. The corrected RESULT.md in /workspace/repairs/4 states that it is at C_4=-M(V), i.e. the lower boundary, and gives the verified leading coefficient. In stationary position, an independent Gaussian contributes D/kappa to the variance and zero to the fourth cumulant. The spherical coordinate generator sends u^b to b(b-1)u^(b-2)-b(b+d-2)u^b, which with the harmonic filter drift gives the joint recurrence. Using the uniform sphere second and fourth moments 1/d and 3/[d(d+2)], the recurrence gives m20=m11=1/[d(1+(d-1)q)], m13=(m04+6q m11)/[1+3(d+1)q], m22=(m13+q m20)/(1+dq), and m40=3m22/[3+(d-1)q]. Subtracting the variance square with factor three and rescaling gives the stated C_4. At fixed V>0, B(q)>0 decreases, the positive root x(q) increases, and A(q)=V-Dx(q)>0 is nonincreasing, including constant A=V for D=0. The denominator of F_d is its numerator plus d(d-1)q², implying 0<F_d<1 and F_d strictly decreasing for q>0, with limits 1 and 0. Thus -C_4 decreases strictly from M(V) to zero, each admissible pair has unique q and x, and variance alone has a continuum of rate pairs. At D=0, 1-F_d~d(d-1)q²/3 as q→0, so the inverse rate D_r=q/x is not Lipschitz at the lower boundary. At fixed V both thermal cases yield unbounded D_r as C_4→0. Checked the symbolic moment, derivative, and onset identities with python /workspace/reproduce_frozen.py. The frozen checker was inspected, not run; its finite inverse examples are not certification of either boundary or the whole range.

## originality

PASS

Best of current knowledge, the distinct claim is the global two-unknown inverse with exactly the specified open attainable region for all dimensions and calibrated D>=0. The repaired source credits the forward radial and coordinate statistics through their exact isotropic equivalence; it does not claim the stationary moments or density as new.

## value

PASS

Two calibrated snapshot observables identify the two rates despite potentially misleading single-parameter kurtosis sweeps. The exact attainable band discriminates model-compatible population data, makes the inversion one-dimensional, and identifies regimes of ill conditioning. This is a useful inverse theorem beyond evaluating known forward moments and does not assert finite-sample inference performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
